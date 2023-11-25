from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from typing import List
import os
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to list all images in a folder
def list_images_in_folder(folder: str) -> List[str]:
    images = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg")):
                images.append(os.path.join(root, file).lstrip("./dishes/"))
    return images

# Endpoint 1: Get all images from all dishes with pagination
@app.get("/dishes/")
async def get_all_images(page: int = 0, page_size: int = 10):
    with open("meta.txt", "r") as file:
        dishes = file.read().splitlines()
    all_images = {}
    for dish in dishes:
        all_images[dish] = list_images_in_folder('./dishes/'+dish)

    total_pages = len(all_images) // page_size + (len(all_images) % page_size > 0)
    start = page * page_size
    end = start + page_size

    paginated_images = {k: all_images[k] for k in list(all_images)[start:end]}
    return {"page": page, "total_pages": total_pages, "data": paginated_images}

# Endpoint 2: Get images of a specific dish
@app.get("/dishes/{dish_name}")
async def get_specific_dish_images(dish_name: str):
    full_path='./dishes/'+dish_name
    if os.path.exists(full_path):
        return list_images_in_folder(full_path)
    return {"error": "Dish not found"}

@app.get("/{path:path}")
async def serve_image(path: str):
    full_path = os.path.join('dishes', path)
    if os.path.exists(full_path) and os.path.isfile(full_path):
        return FileResponse(full_path)
    return {"error": "Image not found"}

