# Flask Calculator App with CI/CD Pipeline

## 📘 Project Overview

This project is a simple Flask web application that performs basic arithmetic operations: addition, subtraction, multiplication, and division. It also includes a CI/CD pipeline using GitHub Actions and Docker to automate testing and deployment.

## 🛠️ Features

- Perform basic arithmetic operations via REST API
- Unit testing with pytest
- Containerized with Docker
- Automated CI/CD pipeline

## 📂 Project Structure

```
ci-pipeline-midterm/
├── app/
│   ├── app.py                # Main Flask app
│   └── __init__.py          # Init file for module recognition
├── tests/
│   └── test_app.py          # Test cases for API endpoints
├── Dockerfile               # Docker configuration file
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## API Endpoints

- **Addition:** `GET /add?a=5&b=3` → `{ "result": 8 }`
- **Subtraction:** `GET /subtract?a=10&b=4` → `{ "result": 6 }`
- **Multiplication:** `GET /multiply?a=3&b=3` → `{ "result": 9 }`
- **Division:** `GET /divide?a=10&b=2` → `{ "result": 5 }`

## How to Run the Application

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/ci-pipeline-midterm.git
cd ci-pipeline-midterm
```

2. **Set up a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Flask app:**
```bash
python app/app.py
```

5. **Test the endpoints:**
```bash
curl "http://localhost:5000/add?a=5&b=3"
```

## 🐳 Docker Setup

1. **Build the Docker image:**
```bash
docker build -t flask-app .
```

2. **Run the container:**
```bash
docker run -p 5000:5000 flask-app
```

3. **Access the API:**
```bash
curl "http://localhost:5000/add?a=5&b=3"
```

## ✅ Testing with Pytest

1. **Run tests locally:**
```bash
pytest tests/
```

2. **Run tests inside Docker:**
```bash
docker exec <container_id> pytest tests/
```

## 🛠️ CI/CD Pipeline (GitHub Actions)

The project uses GitHub Actions to automate:
- **Build:** Create Docker images
- **Test:** Run the test suite
- **Deploy:** Push Docker images to Docker Hub (on passing tests)

### Configure GitHub Secrets

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

## 📄 Workflow File (ci.yml)

Located in `.github/workflows/ci.yml`, this file automates the build, test, and deploy steps whenever code is pushed.

## Contributors

- **Shiron Kurian** 

## 🏁 Conclusion

This project demonstrates a complete web application lifecycle — from development to deployment — using Flask, Docker, and GitHub Actions. It's a solid foundation for learning CI/CD and cloud-native development