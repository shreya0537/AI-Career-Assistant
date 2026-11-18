# =====================================================================
# CIVIL - ROUND 5: HR & BEHAVIORAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_civil_hr(username="Candidate", skills=None, used_ids=None):
    skills = skills or []
    used_set = set(used_ids or [])
    top_skill = skills[0] if skills else "Civil Engineering"

    master_pool = [
        {
            "id": "civil_hr_1",
            "difficulty": "Easy",
            "category": "Self Introduction & Site Commitment",
            "question": f"Introduce yourself, {username}. What inspired you to pursue Civil Engineering and how have your skills in **{top_skill}** prepared you for site supervision and structural design?",
            "acceptable_answers": [
                "Structured introduction highlighting civil engineering passion, surveying/CAD proficiency, and commitment to infrastructure development.",
                "Summary of academic accomplishments, site training, and structural analysis projects."
            ],
            "model_answer": f"Model Answer Structure:\n1. Background: 'I am a Civil Engineering graduate dedicated to building safe, sustainable infrastructure.'\n2. Technical Capabilities: 'I am proficient in {top_skill}, structural design (IS 456 / IS 800), surveying, and quantity estimation.'\n3. Practical Experience: 'I have managed site layout tasks, concrete quality testing, and structural framing projects.'\n4. Career Objective: 'Eager to contribute to structural engineering and large-scale site execution.'"
        },
        {
            "id": "civil_hr_2",
            "difficulty": "Medium",
            "category": "Contractor & Labor Management",
            "question": "How do you handle site labor conflicts, contractor non-compliance, or delays on a construction site?",
            "acceptable_answers": [
                "Communicate clearly, enforce contract specifications, resolve disputes through daily toolbox meetings, and maintain site discipline.",
                "Firm and fair labor management, checking work against BOQ specifications."
            ]
        },
        {
            "id": "civil_hr_3",
            "difficulty": "Medium",
            "category": "Handling Weather Delays & Monsoon Planning",
            "question": "Describe how you would manage construction progress during heavy monsoon rains or unforeseen soil conditions.",
            "acceptable_answers": [
                "Plan indoor/structural work during heavy rain, protect excavation pits with dewatering pumps, and adjust CPM schedule.",
                "Implement site drainage, dewatering, and adjust activity priorities."
            ],
            "model_answer": "Model Answer Structure (STAR):\n- Situation: 'Monsoon rains threatened to flood foundation excavation pits.'\n- Task: 'Protect foundation soil from saturation and maintain safety.'\n- Action: 'Installed perimeter drainage channels, deployed submersible dewatering pumps, and covered exposed slopes with tarpaulins.'\n- Result: 'Prevented slope collapse and resumed concrete pouring immediately after rain stopped.'"
        },
        {
            "id": "civil_hr_4",
            "difficulty": "Hard",
            "category": "Ethics & Quality Compromise Pressure",
            "question": "What would you do if a site contractor attempts to use substandard aggregate or skip steel reinforcement rebar tieing?",
            "acceptable_answers": [
                "Reject non-conforming materials immediately, issue a formal Stop Work Notice, and report to the Project Manager.",
                "Enforce IS code compliance strictly and refuse to approve substandard pours."
            ]
        },
        {
            "id": "civil_hr_5",
            "difficulty": "Hard",
            "category": "Career Vision in Civil Engineering",
            "question": "Where do you see yourself in 3 to 5 years within structural engineering or construction management?",
            "acceptable_answers": [
                "Aiming to become a Licensed Structural Engineer or Site Project Manager leading high-rise or infrastructure developments.",
                "Seeking growth in structural design, BIM management, or site execution."
            ]
        },
        {
            "id": "civil_hr_6",
            "difficulty": "Easy",
            "category": "Site Mobility & Remote Relocation",
            "question": "Are you willing to relocate to remote infrastructure project sites (highways, dams, bridges) across different states?",
            "acceptable_answers": [
                "Fully open to site relocation; value hands-on field experience on major infrastructure projects.",
                "Enthusiastic about site-based civil engineering roles anywhere required."
            ],
            "model_answer": "Model Answer:\n'Yes, I am fully prepared to relocate to project sites. As a civil engineer, I understand that major infrastructure projects happen where the development is needed. Field experience is invaluable for my professional growth.'"
        },
        {
            "id": "civil_hr_7",
            "difficulty": "Medium",
            "category": "Site Safety Compliance (HSE)",
            "question": "How do you enforce Health, Safety, and Environment (HSE) rules like hard hats, scaffolding safety, and trench shoring on site?",
            "acceptable_answers": [
                "Conduct daily morning safety briefings (Toolbox Talk), inspect scaffolding tags, mandate PPE, and stop unsafe acts.",
                "Strictly enforce safety gear, scaffolding stability checks, and site hazard signs."
            ]
        },
        {
            "id": "civil_hr_8",
            "difficulty": "Medium",
            "category": "Handling Client Change Requests",
            "question": "How do you handle mid-construction architectural change requests from clients that impact structural stability?",
            "acceptable_answers": [
                "Explain structural implications objectively, re-run structural calculations, submit variation order cost/time estimates.",
                "Consult structural design team before approving any architectural modifications on site."
            ]
        },
        {
            "id": "civil_hr_9",
            "difficulty": "Hard",
            "category": "Root Cause Analysis of Structural Crack",
            "question": "How would you investigate and categorize hairline plastic shrinkage cracks vs structural shear cracks in a freshly poured slab?",
            "acceptable_answers": [
                "Plastic shrinkage cracks are superficial and non-structural due to rapid drying; Shear cracks run diagonally near supports indicating structural distress.",
                "Inspect crack depth, direction, and structural location to determine if remedial epoxy injection or structural shoring is needed."
            ]
        },
        {
            "id": "civil_hr_10",
            "difficulty": "Easy",
            "category": "Work Style (Office vs Field)",
            "question": "Do you prefer structural CAD drafting in office or site supervision on field?",
            "acceptable_answers": [
                "Enjoy both: site supervision gives practical execution insights, while office design sharpens analytical IS code skills.",
                "Balanced interest in both structural analysis office work and field execution."
            ]
        },
        {
            "id": "civil_hr_11",
            "difficulty": "Medium",
            "category": "Handling Pressure during Concreting Pours",
            "question": "How do you maintain quality control during a massive continuous 12-hour concrete slab pour?",
            "acceptable_answers": [
                "Rotate inspection staff, continuously test slump and temperature, ensure backup vibrators are on site, and coordinate RMC transit mixers.",
                "Organize shifts, verify slump on every truck, and ensure continuous compaction."
            ]
        },
        {
            "id": "civil_hr_12",
            "difficulty": "Hard",
            "category": "Budget Overrun Mitigation",
            "question": "What steps do you take when project costs exceed the estimated Bill of Quantities (BOQ)?",
            "acceptable_answers": [
                "Audit material wastage on site, optimize rebar cutting lengths, negotiate supplier rates, and track daily labor productivity.",
                "Perform variance analysis, eliminate material wastage, and implement value engineering."
            ]
        },
        {
            "id": "civil_hr_13",
            "difficulty": "Easy",
            "category": "Key Strength",
            "question": "What is your primary technical strength as a Civil Engineer?",
            "acceptable_answers": [
                "Strong grasp of IS structural codes, precision in quantity estimation, and dedicated site supervision discipline.",
                "Accuracy in CAD modeling, surveying calculations, and structural detailing."
            ]
        },
        {
            "id": "civil_hr_14",
            "difficulty": "Medium",
            "category": "Company Alignment",
            "question": "Why do you want to join our civil engineering / construction firm?",
            "acceptable_answers": [
                "Respect the firm's landmark infrastructure portfolio, commitment to quality construction, and engineering culture.",
                "Strong desire to contribute to company's prestigious structural projects."
            ]
        },
        {
            "id": "civil_hr_15",
            "difficulty": "Hard",
            "category": "Future Civil Tech & BIM",
            "question": "How are you preparing for Building Information Modeling (BIM), 3D Concrete Printing, and Drone Surveying in Civil Engineering?",
            "acceptable_answers": [
                "Learning Revit BIM software, following drone photogrammetry developments, and studying sustainable green building materials.",
                "Keeping updated with BIM 4D/5D modeling and automated site surveying."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
