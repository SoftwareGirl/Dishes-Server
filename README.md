# Dishes Server

## Introduction
This project is a FastAPI server that provides endpoints to retrieve dish data and images. The server is designed to handle requests for dish information and images efficiently and securely.

## Endpoints
The FastAPI server exposes the following endpoints:

1. **GET /dishes/**
   - Returns a JSON object containing dish data.
   - Example response: `{"data": {"dish_1": ["img_1.jpg", "img_2.jpg"], ...}}`
   - This endpoint provides an overview of all available dishes and their associated images.

2. **GET /img_1.jpg**
   - Returns a blob of the requested image.
   - This endpoint allows clients to retrieve specific images by their filename.

3. **GET /dishes/dish_1**
   - Returns a list of image filenames associated with a specific dish.
   - Example response: `["img_1", "img_2", ...]`
   - This endpoint provides detailed information about a specific dish, including its associated images.

## User Interface
Please access the UI client with this URL: https://github.com/SoftwareGirl/Dishes-Client

## Dependencies
This project relies on the following dependencies:

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- Uvicorn: A lightning-fast ASGI server implementation, using uvloop and httptools.
- Other dependencies specified in the `requirements.txt` file.
- In addition to Python requirements, one needs to download dishes image collection from this Google drive Link and unzip it to the project root: https://drive.google.com/file/d/1WYjnjsDGQp-icIRSs6JVslNqfy4FoBHz/view?usp=sharing

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository from [GitHub](https://github.com/your-repo-link).
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Start the FastAPI server by running `uvicorn main:app --reload`.
4. Access the endpoints using the provided URLs, such as `http://127.0.0.1:8000/dishes/`.

## References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

