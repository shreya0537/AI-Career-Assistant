# AI-Driven Career Assistant with Resume Analysis and Interview Evaluation

A Streamlit-based career preparation application that analyzes PDF resumes, identifies engineering branches and skills, recommends suitable job roles, provides a placement-readiness dashboard, and supports a five-round mock interview workflow.

## Features

- User registration and login using SQLite
- Resume PDF text extraction using PyMuPDF
- Engineering branch detection for CSE, ECE, Mechanical, and Civil
- Resume skill and project analysis
- Job-role recommendations and missing-skill identification
- Placement-readiness dashboard
- Five-stage mock interview: Aptitude, Coding, Technical, Project, and HR
- Answer evaluation using scikit-learn

## Project structure

```text
AI-Career-Assistant/
├── backend/
│   ├── ai/
│   ├── branches/
│   ├── interview/
│   ├── auth.py
│   ├── constants.py
│   ├── dashboard.py
│   ├── database.py
│   ├── interview.py
│   └── resume.py
├── frontend/
│   ├── assets/
│   │   └── hero_career_ai.jpg
│   ├── app.py
│   └── style.css
├── .gitignore
├── README.md
└── requirements.txt
```

## Run locally

Use Python 3.10 or newer (choose a version supported by the packages in `requirements.txt`).

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Start the application from the project root:

```bash
streamlit run frontend/app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, choose **Create app**.
3. Select the GitHub repository and branch.
4. Set **Main file path** to `frontend/app.py`.
5. Deploy.

## Data and privacy notes

- The SQLite database is created automatically when the application starts. The database file is intentionally excluded from this repository.
- Uploaded resumes are processed by the app and are not included in this repository.
- Streamlit Community Cloud local files are not a durable database. User accounts and other SQLite records may not persist across app restarts or redeployments. Use a managed database for persistent public use.
- Do not commit real resumes, personal data, passwords, API keys, `.env` files, or Streamlit secrets.
