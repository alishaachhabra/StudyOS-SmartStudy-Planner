# StudyOS – Smart Study Planner & Student Productivity System

StudyOS is a Flask-based student productivity application designed to organize subjects, academic tasks, deadlines, and study plans. The project also includes a separate C++ DSA engine for priority-based study-plan generation.

## Key Features

- User signup, login, sessions, and profile management
- Subject and task management
- Task attributes including deadline, estimated study time, importance, mandatory status, and notes
- Priority-based study-plan generation within available study time
- Calendar and progress/analytics views
- C++ DSA engine for task scheduling

## DSA Implementation

The C++ component includes:

- Heap-based priority queue
- Stack
- Queue
- Trie
- Graph using an adjacency list
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Priority-based scheduler

The scheduler calculates task priority using importance, mandatory status, and estimated study time, then selects tasks without exceeding the available study time.

## Tech Stack

**Frontend:** HTML, CSS, JavaScript

**Backend:** Python, Flask

**Database:** SQLite, Flask-SQLAlchemy

**Algorithms:** C++, Data Structures & Algorithms

## Project Structure

```text
StudyOS/
├── app.py
├── cpp/
├── database/
├── templates/
├── static/
├── utils/
├── requirements.txt
├── .env.example
└── README.md
```

## Run Locally

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Optionally set a `SECRET_KEY` environment variable.
4. Run the Flask application:

```bash
python app.py
```

5. Open the local address shown by Flask in your browser.

## Note

The repository intentionally excludes the local virtual environment, SQLite database, Python cache files, and compiled binaries.
