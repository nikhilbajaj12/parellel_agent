# Mergington High School Activities API

A simple FastAPI-based API for managing extracurricular activities at a high school.

This project provides endpoints to view current activities and sign up students for these activities. It uses an in-memory data store, meaning all data resets when the server restarts.

## Setup / Installation

Install dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

## Usage

Run the application using Uvicorn from the `src` directory:

```
cd src
uvicorn app:app --reload
```

Open your browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation.


## Project Structure

- `src/app.py`: Main FastAPI application.
- `src/static/`: Static files served by the API.
- `requirements.txt`: Project dependencies.
- `pytest.ini`: Pytest configuration file.

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

