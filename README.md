# CI/CD Pipeline with GitHub Actions, Docker, and Kubernetes (FastAPI App)

## 📌 Overview
This project demonstrates how to build, test, and deploy a **FastAPI application** using a **CI/CD pipeline powered by GitHub Actions**. The application is packaged into a Docker container and deployed to a Kubernetes cluster.  

---

## 🚀 Workflow Description

1. **Code Development (FastAPI App)**
   - The backend application is developed using **FastAPI**.
   - The main endpoint `/` returns `"Hello World"`.
   - The endpoint `/docs` will open interactive API docs.


2. **Version Control (GitHub)**
   - Source code, Dockerfile, Kubernetes manifests, and workflow files are stored in a GitHub repository.

3. **Continuous Integration (GitHub Actions)**
   - On every code push or pull request:
     - Runs **Pytest** to validate code and functionality.
     - Builds a **Docker image**.
     - Pushes the image to **DockerHub** (or any container registry).
   - Uses GitHub secrets for secure storage of **DockerHub credentials** and **Kubernetes config**.

4. **Continuous Deployment (Kubernetes)**
   - GitHub Actions applies the updated Kubernetes manifests.
   - Kubernetes pulls the latest Docker image from DockerHub.
   - The updated application is deployed automatically.

---

## 🛠️ Tech Stack
- **FastAPI (Python Framework)**
- **Docker**
- **Kubernetes (Minikube or any cluster)**
- **GitHub Actions (CI/CD Pipeline)**
- **Pytest (Testing)**

---

## 📂 Project Structure

```bash
.
├── app/
│ └── main.py # FastAPI application
├── tests/
│ └── test_main.py # Pytest test cases
├── Dockerfile # Docker build file
├── requirements.txt # Python dependencies
├── deployment.yaml # Kubernetes Deployment + Service
├── .github/workflows/
│ └── ci-cd.yml # GitHub Actions pipeline
└── README.md
```


---

## ☸️ Kubernetes Deployment Flow
1. GitHub Actions pushes the Docker image to DockerHub.
2. The Kubernetes deployment manifest (`deployment.yaml`) is applied.
3. Kubernetes updates the running pods with the new Docker image.
4. The **Kubernetes Service** exposes the application to the outside world.

---

## 🔄 GitHub Actions CI/CD Pipeline
- **Trigger**: On push or pull request to the `main` branch.  
- **Steps**:
  1. Check out the repository.
  2. Set up Python and install dependencies.
  3. Run Pytest for automated testing.
  4. Log in to DockerHub.
  5. Build and push Docker image.
  6. Apply Kubernetes manifests to deploy the new version.

---

## ✅ API Endpoints
- **GET /** → Returns `"Hello World"`
- **GET /docs** → will open interactive API docs

---

## 🔑 Secrets Required in GitHub Actions
To ensure secure deployment, the following secrets must be set in the GitHub repository:
- `DOCKERHUB_USERNAME` → Your DockerHub username  
- `DOCKERHUB_TOKEN` → DockerHub access token or password
---
