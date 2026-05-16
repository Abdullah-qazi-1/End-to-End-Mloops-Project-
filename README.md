# Network Security - Phishing Website Detection

A production-grade MLOps project that detects phishing websites using machine learning. 
The system ingests data from MongoDB Atlas, runs it through a complete training pipeline 
with automated hyperparameter tuning, tracks experiments via MLflow and DagsHub, 
and deploys on AWS EC2 through a fully automated CI/CD pipeline using GitHub Actions and Docker.

## Tech Stack

- **ML & Data:** Python, Scikit-learn, Pandas, NumPy
- **API:** FastAPI
- **Database:** MongoDB Atlas
- **Experiment Tracking:** MLflow, DagsHub
- **Cloud:** AWS S3, ECR, EC2
- **DevOps:** Docker, GitHub Actions