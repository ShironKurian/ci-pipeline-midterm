# ci-pipeline-midterm
Midterm Practical for CI Pipeline with GitHub Actions
CI Pipeline for Flask Application
Overview
This project sets up a Continuous Integration (CI) pipeline for a simple Flask application using GitHub Actions. The pipeline performs the following tasks:

Builds the application
Runs unit tests
Uploads the application as a Docker image to Docker Hub
Directory Structure
bash
Copy
Edit
ci-pipeline-midterm/
├── app/
│   ├── app.py                 # Flask application
│   ├── Dockerfile             # Docker instructions
│   ├── requirements.txt       # Python dependencies
│
├── tests/
│   ├── test_app.py            # Unit tests
│   └── __init__.py            # Marks this as a package
│
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI pipeline
│
├── README.md                  # Documentation
└── .gitignore                 # Ignored files
Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
2. Install Dependencies
Ensure you have Python 3 and pip installed. Run:

bash
Copy
Edit
pip install -r app/requirements.txt
3. Run the Flask Application
bash
Copy
Edit
python app/app.py
Access the application at http://127.0.0.1:5000.

4. Run Unit Tests
bash
Copy
Edit
pytest tests/
Docker Setup
1. Build the Docker Image
bash
Copy
Edit
docker build -t your-dockerhub-username/flask-app:v1 app/
2. Run the Docker Container
bash
Copy
Edit
docker run -p 5000:5000 your-dockerhub-username/flask-app:v1
Now visit http://127.0.0.1:5000.

3. Push Docker Image to Docker Hub
Ensure you are logged in:

bash
Copy
Edit
docker login
Then push the image:

bash
Copy
Edit
docker push your-dockerhub-username/flask-app:v1
GitHub Actions CI Pipeline
The CI pipeline is defined in .github/workflows/ci.yml. It automates the following:

Build Phase: Installs dependencies and builds the application
Test Phase: Runs unit tests and ensures all tests pass
Upload Phase: Builds and pushes the Docker image to Docker Hub
Trigger
The workflow runs on every push or pull request to the main branch.

Jenkins Pipeline (Bonus Task)
If using Jenkins, create a Jenkinsfile in the root directory with equivalent stages:

Build Stage: Install dependencies
Test Stage: Run unit tests
Upload Stage: Push Docker image to Docker Hub
Ensure Jenkins is properly configured with the necessary credentials.
