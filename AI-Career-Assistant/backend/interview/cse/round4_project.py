# =====================================================================
# CSE - ROUND 4: PROJECT & RESUME TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_cse_project_questions(projects=None, skills=None, used_ids=None):
    """
    Generates a pool of EXACTLY 15 Project & Resume Technical Questions.
    Dynamically parameterized based on candidate's parsed resume projects and skills.
    Contains 3 questions with detailed model answers.
    """
    projects = projects or []
    skills = skills or []
    used_set = set(used_ids or [])

    if projects and len(projects) > 0:
        p1 = projects[0]
        p2 = projects[1] if len(projects) > 1 else projects[0]
    elif skills:
        p1 = f"{skills[0]} & {skills[1] if len(skills)>1 else 'SQL'} Software Project"
        p2 = f"Full-Stack {skills[0]} Application"
    else:
        p1 = "Computer Science Software Project"
        p2 = "Web & Data Management System"

    s1 = skills[0] if skills else "Python"
    s2 = skills[1] if len(skills) > 1 else (skills[0] if skills else "SQL")
    s3 = skills[2] if len(skills) > 2 else "REST APIs"

    master_pool = [
        {
            "id": "cse_proj_1",
            "difficulty": "Easy",
            "category": f"Project Architecture ({p1})",
            "question": f"Walk me through the overall high-level system architecture and key components of your project '{p1}'. What was your specific individual contribution?",
            "acceptable_answers": [
                f"High-level architecture of {p1} includes client interface, backend service, database layer, and third-party APIs.",
                f"Detailed explanation of system modules, data flow, and individual responsibilities in {p1}.",
                "Detailed architecture explanation covering frontend, backend, and database integration."
            ],
            "model_answer": f"Model Answer Structure:\n1. Problem Statement: Explain the core real-world challenge addressed by '{p1}'.\n2. System Architecture: Outline the multi-tier structure (e.g. Frontend UI -> REST API Gateway -> Backend Service -> Database/Cloud Storage).\n3. Individual Role: Specify your direct code contributions, such as designing API endpoints, database schema normalization, or feature integration.\n4. Impact: Highlight concrete metrics (e.g., reduced processing latency, improved user throughput)."
        },
        {
            "id": "cse_proj_2",
            "difficulty": "Medium",
            "category": f"Technology Stack Rationale ({s1} & {s2})",
            "question": f"Why did you choose **{s1}** and **{s2}** for your project '{p1}' over alternative technical frameworks?",
            "acceptable_answers": [
                f"Chosen {s1} and {s2} due to ease of integration, community support, library ecosystem, and performance trade-offs in {p1}.",
                f"Selected {s1} for rapid prototyping/libraries and {s2} for reliable relational data storage.",
                "Technical evaluation comparing framework trade-offs, developer productivity, and scalability."
            ]
        },
        {
            "id": "cse_proj_3",
            "difficulty": "Medium",
            "category": f"Database Design ({s2})",
            "question": f"Explain the database schema design, indexing, and normalization strategy used in your project '{p1}'. How did you handle data integrity using **{s2}**?",
            "acceptable_answers": [
                f"Normalized tables to 3NF, established primary/foreign key constraints, and created B-Tree indexes on frequently queried columns in {p1}.",
                "Implemented relational schema with foreign key constraints and index optimization to prevent queries bottlenecks."
            ]
        },
        {
            "id": "cse_proj_4",
            "difficulty": "Hard",
            "category": "Debugging & Production Problem Solving",
            "question": f"Describe the most complex technical bug or bottleneck you encountered during the implementation of '{p1}' and how you systematically diagnosed and resolved it.",
            "acceptable_answers": [
                f"Identified bottleneck using logging/profiling tools, diagnosed memory leak or N+1 query issue in {p1}, and optimized implementation.",
                "Systematic debugging approach involving error logs, step-by-step isolation, benchmarking, and refactoring."
            ],
            "model_answer": f"Model Answer Structure:\n1. Root Cause Identification: Describe how error logs or performance benchmarks pinpointed the bug in '{p1}'.\n2. Diagnostic Tools: Mention profiling tools (e.g., Chrome DevTools, Py-Spy, SQL EXPLAIN query plans).\n3. Resolution: Explain the code fix (e.g., converting iterative queries to batch joins, caching redundant computations).\n4. Verification: Describe regression testing to confirm resolution."
        },
        {
            "id": "cse_proj_5",
            "difficulty": "Hard",
            "category": f"Scalability & Optimization ({p1})",
            "question": f"If user traffic or dataset size for '{p1}' increases by 100x, what structural scaling modifications (caching, load balancing, sharding) would you implement?",
            "acceptable_answers": [
                f"Implement Redis/Memcached caching layer, load balancer (NGINX), database read-replicas, and asynchronous message queue for {p1}.",
                "Horizontal scaling with microservices, load balancing, database sharding, and CDN asset delivery."
            ]
        },
        {
            "id": "cse_proj_6",
            "difficulty": "Easy",
            "category": f"Core Competency Integration ({s3})",
            "question": f"How did you integrate **{s3}** into your project '{p1}'? What challenges arose during setup?",
            "acceptable_answers": [
                f"Integrated {s3} into {p1} by configuring dependencies, managing environment variables, and establishing API contracts.",
                f"Used {s3} for specialized functionality, resolving version compatibility and deployment issues."
            ]
        },
        {
            "id": "cse_proj_7",
            "difficulty": "Medium",
            "category": f"Secondary Project Details ({p2})",
            "question": f"What was the main technical objective of your secondary project '{p2}'? How did you validate system accuracy or performance?",
            "acceptable_answers": [
                f"Engineered {p2} to solve domain challenge, validating performance via unit tests, integration testing, and performance metrics.",
                "Built secondary project with specific functional requirements, verified using automated tests or user testing."
            ]
        },
        {
            "id": "cse_proj_8",
            "difficulty": "Hard",
            "category": "API & Integration Security",
            "question": f"How did you handle authentication, authorization, and data security in your project '{p1}'?",
            "acceptable_answers": [
                f"Implemented JWT tokens / OAuth2, hashed passwords using bcrypt/Argon2, and sanitized user inputs against SQL injection & XSS in {p1}.",
                "Secured API endpoints using token-based authentication, environment secrets, and CORS configuration."
            ],
            "model_answer": f"Model Answer for '{p1}':\nSecurity Implementation:\n1. Authentication: Used JWT (JSON Web Tokens) or OAuth2 with HTTPS transport.\n2. Password Storage: Hashed passwords using bcrypt with salt.\n3. Input Sanitization: Escaped parameters to prevent SQL Injection and Cross-Site Scripting (XSS).\n4. Environment Management: Stored sensitive API keys in .env files outside version control."
        },
        {
            "id": "cse_proj_9",
            "difficulty": "Hard",
            "category": "Asynchronous Processing & Concurrency",
            "question": f"Did your project '{p1}' involve any asynchronous tasks or background job queues? If so, how did you handle concurrent execution?",
            "acceptable_answers": [
                f"Used Celery / Redis / AsyncIO in {p1} to offload heavy background tasks from the main request thread.",
                "Implemented event loops or thread pools for non-blocking I/O operations."
            ]
        },
        {
            "id": "cse_proj_10",
            "difficulty": "Easy",
            "category": "Version Control & Collaboration",
            "question": f"How did you manage Git branching strategies, pull requests, and code reviews during the development of '{p1}'?",
            "acceptable_answers": [
                f"Used Git feature branching workflow, main/dev branches, PR code reviews, and resolved merge conflicts systematically in {p1}.",
                "Maintained clean commit history, used Git branching strategy, and automated checks."
            ]
        },
        {
            "id": "cse_proj_11",
            "difficulty": "Medium",
            "category": "Testing & QA Automation",
            "question": f"What automated unit tests, integration tests, or edge-case tests did you write for '{p1}'?",
            "acceptable_answers": [
                f"Wrote unit tests using PyTest / JUnit / Jest covering core business logic and edge cases in {p1}.",
                "Implemented test suite for API endpoints, database operations, and utility functions."
            ]
        },
        {
            "id": "cse_proj_12",
            "difficulty": "Hard",
            "category": "CI/CD & Deployment",
            "question": f"How was '{p1}' deployed? Explain your containerization (Docker) or CI/CD pipeline setup.",
            "acceptable_answers": [
                f"Containerized application {p1} using Docker multi-stage builds and deployed via GitHub Actions to cloud platform.",
                "Configured CI/CD pipeline for automated testing, build artifact generation, and server deployment."
            ]
        },
        {
            "id": "cse_proj_13",
            "difficulty": "Easy",
            "category": "Requirements & User Feedback",
            "question": f"How did you gather requirements and translate user feedback into feature updates for '{p1}'?",
            "acceptable_answers": [
                f"Iterative development lifecycle for {p1}, prioritizing features based on user usability feedback and functional requirements.",
                "Structured requirements backlog and user stories."
            ]
        },
        {
            "id": "cse_proj_14",
            "difficulty": "Medium",
            "category": "Refactoring & Tech Debt",
            "question": f"Looking back at '{p1}', what part of your code or architecture would you refactor if you rebuilt it today?",
            "acceptable_answers": [
                f"Refactor monolithic components into modular services, improve error handling, and upgrade legacy libraries in {p1}.",
                "Improve code modularity, separation of concerns, and query optimization."
            ]
        },
        {
            "id": "cse_proj_15",
            "difficulty": "Hard",
            "category": "Future Enhancements & AI Integration",
            "question": f"What advanced features (e.g. AI capabilities, microservices, real-time WebSockets) would you add to '{p1}' next?",
            "acceptable_answers": [
                f"Integrate real-time analytics using WebSockets, add predictive ML models, or migrate to microservices for {p1}.",
                "Add AI recommendation capabilities, real-time push notifications, and cloud auto-scaling."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
