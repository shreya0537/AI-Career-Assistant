# =====================================================================
# CSE - ROUND 5: HR & BEHAVIORAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_cse_hr(username="Candidate", skills=None, used_ids=None):
    """
    Generates a pool of EXACTLY 15 HR & Behavioral Questions.
    Evaluates communication clarity, career goals, teamwork, leadership, and problem solving under pressure.
    Contains 3 questions with detailed model answers.
    """
    skills = skills or []
    used_set = set(used_ids or [])

    top_skill = skills[0] if skills else "Computer Science"

    master_pool = [
        {
            "id": "cse_hr_1",
            "difficulty": "Easy",
            "category": "Self Introduction & Alignment",
            "question": f"Tell me about yourself, {username}. What inspired you to pursue a career in Computer Science, and how have your skills in **{top_skill}** prepared you for this role?",
            "acceptable_answers": [
                "Structured introduction covering educational background, passion for software engineering, technical projects, and career alignment.",
                "Summary of academic achievements, technical projects, and enthusiasm for technology innovation."
            ],
            "model_answer": f"Model Answer Structure (Elevator Pitch):\n1. Background: 'I am a Computer Science graduate passionate about software engineering and problem solving.'\n2. Key Strengths: 'During my studies, I mastered core technical areas including {top_skill}, database architecture, and full-stack development.'\n3. Practical Experience: 'I have applied these skills in building real-world projects, focusing on scalable clean code.'\n4. Goal Alignment: 'I am excited about this role because it allows me to contribute to impactful engineering solutions.'"
        },
        {
            "id": "cse_hr_2",
            "difficulty": "Medium",
            "category": "Conflict Resolution & Teamwork",
            "question": "Describe a situation where you had a technical disagreement with a team member during a project. How did you resolve it?",
            "acceptable_answers": [
                "Used data-driven decision making, listened actively, evaluated trade-offs collaboratively, and agreed on the optimal technical path.",
                "Discussed pros and cons objectively, conducted proof-of-concept tests, and reached team consensus."
            ]
        },
        {
            "id": "cse_hr_3",
            "difficulty": "Medium",
            "category": "Handling Pressure & Tight Deadlines",
            "question": "Tell me about a time when you faced a critical project deadline or system outage. How did you prioritize tasks and handle the pressure?",
            "acceptable_answers": [
                "Prioritized core critical features, communicated proactively with stakeholders, managed time effectively, and delivered on time.",
                "Broke down tasks, maintained calm focus under pressure, and delivered functional MVP."
            ],
            "model_answer": "Model Answer Structure (STAR Method):\n- Situation: 'During a final semester major project deadline, a critical API integration broke 24 hours before presentation.'\n- Task: 'I needed to restore core functionality without compromising data consistency.'\n- Action: 'I prioritized essential workflow endpoints, implemented temporary fallback handling, and coordinated task allocation.'\n- Result: 'We successfully delivered the working project on schedule and earned top evaluation grades.'"
        },
        {
            "id": "cse_hr_4",
            "difficulty": "Hard",
            "category": "Failure & Growth Mindset",
            "question": "Describe a project or task that did not turn out as planned. What mistakes were made, and what vital lessons did you learn?",
            "acceptable_answers": [
                "Owned responsibility for the oversight, analyzed root cause failure, implemented corrective measures, and adopted new preventive habits.",
                "Reflected on initial mistakes in scope planning, learned key technical lessons, and improved subsequent execution."
            ]
        },
        {
            "id": "cse_hr_5",
            "difficulty": "Hard",
            "category": "Career Goals & Professional Vision",
            "question": "Where do you see your technical career progression in the next 3 to 5 years, and how does our organization fit into that vision?",
            "acceptable_answers": [
                "Aiming to grow into a senior software engineering / technical lead role, mastering cloud architecture and mentoring junior developers.",
                "Seeking long-term growth by contributing to core engineering systems and expanding technical domain expertise."
            ]
        },
        {
            "id": "cse_hr_6",
            "difficulty": "Easy",
            "category": "Work Ethic & Motivation",
            "question": "What motivates you to write high-quality code every day, and how do you stay updated with rapidly changing tech trends?",
            "acceptable_answers": [
                "Motivated by solving real-world user problems through elegant code; stay updated via tech blogs, GitHub, documentation, and open source.",
                "Driven by technical curiosity and quality execution; follow tech community updates and continuous learning."
            ],
            "model_answer": "Model Answer:\n'My primary motivation stems from seeing software solve real human problems efficiently. Writing clean, maintainable code is both a technical craft and a commitment to team productivity. I stay current by following tech blogs, contributing to GitHub projects, reading official docs, and experimenting with new frameworks on weekends.'"
        },
        {
            "id": "cse_hr_7",
            "difficulty": "Medium",
            "category": "Adaptability & Rapid Learning",
            "question": "How do you approach learning a completely new programming language or framework required for an urgent project?",
            "acceptable_answers": [
                "Start with official documentation, build a hands-on proof-of-concept project, leverage community tutorials, and consult experienced peers.",
                "Read documentation, build small starter applications, and apply concepts immediately to real tasks."
            ]
        },
        {
            "id": "cse_hr_8",
            "difficulty": "Medium",
            "category": "Ethics & Professional Integrity",
            "question": "What would you do if a senior developer asked you to skip code reviews or bypass security checks to meet a launch date?",
            "acceptable_answers": [
                "Politely raise security/quality risks with empirical evidence, offer compromised staging solutions, and escalate if severe risk persists.",
                "Communicate risk trade-offs professionally, suggest quick essential checks, and ensure code safety."
            ]
        },
        {
            "id": "cse_hr_9",
            "difficulty": "Hard",
            "category": "Leadership & Initiative",
            "question": "Give an example of a time when you took initiative without being asked by a supervisor or team lead.",
            "acceptable_answers": [
                "Identified inefficient repetitive manual task, wrote automated script/tool to automate it, saving team time.",
                "Recognized missing documentation or project bug, proactively fixed and shared solution with team."
            ]
        },
        {
            "id": "cse_hr_10",
            "difficulty": "Easy",
            "category": "Work Environment Preference",
            "question": "Do you prefer working independently or in a collaborative team environment?",
            "acceptable_answers": [
                "Thrive in team environments for brainstorming and architecture, while self-directed for deep focused coding tasks.",
                "Balanced approach: collaborative for design and planning, independent for deep execution."
            ]
        },
        {
            "id": "cse_hr_11",
            "difficulty": "Medium",
            "category": "Constructive Feedback",
            "question": "How do you handle receiving critical feedback during code reviews or performance evaluations?",
            "acceptable_answers": [
                "Welcome feedback objectively as growth opportunities, ask clarifying questions, and implement suggested improvements.",
                "View code reviews constructively, focus on code quality rather than personal bias, and apply learnings."
            ]
        },
        {
            "id": "cse_hr_12",
            "difficulty": "Hard",
            "category": "Prioritization & Multitasking",
            "question": "How do you prioritize your work when assigned multiple urgent tasks simultaneously by different team leads?",
            "acceptable_answers": [
                "Assess impact and urgency matrix (Eisenhower Box), communicate with both leads to align on priority, and set clear expectations.",
                "Evaluate business urgency, discuss conflicting deadlines with leads, and execute systematically."
            ]
        },
        {
            "id": "cse_hr_13",
            "difficulty": "Easy",
            "category": "Strengths & Key Selling Point",
            "question": "What is your single greatest technical or personal strength, and how will it benefit our engineering team?",
            "acceptable_answers": [
                "Strong analytical problem-solving and structured debugging discipline, enabling fast resolution of complex system issues.",
                "Persistence, quick technical adaptability, and dedication to clean maintainable code."
            ]
        },
        {
            "id": "cse_hr_14",
            "difficulty": "Medium",
            "category": "Company Knowledge & Role Interest",
            "question": "Why do you specifically want to join our organization rather than other software companies?",
            "acceptable_answers": [
                "Attracted by the company's innovation in AI/tech, strong engineering culture, and opportunities for technical growth.",
                "Impressed by product impact, engineering standards, and alignment with my career aspirations."
            ]
        },
        {
            "id": "cse_hr_15",
            "difficulty": "Hard",
            "category": "Salary & Location Expectations",
            "question": "What are your expectations regarding job location, work mode (remote/hybrid/onsite), and career growth?",
            "acceptable_answers": [
                "Flexible regarding location and work mode; focused primarily on technical learning, mentorship, and impactful growth.",
                "Open to relocation/hybrid work, seeking fair industry standard compensation aligned with contribution."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
