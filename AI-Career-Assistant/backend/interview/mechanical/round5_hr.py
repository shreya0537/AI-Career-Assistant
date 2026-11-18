# =====================================================================
# MECHANICAL - ROUND 5: HR & BEHAVIORAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_mech_hr(username="Candidate", skills=None, used_ids=None):
    skills = skills or []
    used_set = set(used_ids or [])
    top_skill = skills[0] if skills else "Mechanical Engineering"

    master_pool = [
        {
            "id": "mech_hr_1",
            "difficulty": "Easy",
            "category": "Self Introduction & Domain Passion",
            "question": f"Introduce yourself, {username}. What drew you to Mechanical Engineering and how have your skills in **{top_skill}** shaped your practical design approach?",
            "acceptable_answers": [
                "Structured self introduction focusing on mechanical background, hands-on workshop/CAD projects, and passion for manufacturing/design.",
                "Summary of academic achievements, mechanical projects, and industrial interest."
            ],
            "model_answer": f"Model Answer Structure:\n1. Educational Background: 'I am a Mechanical Engineering graduate with strong passion for machine design and thermal fluid systems.'\n2. Key Technical Skills: 'I have hands-on proficiency in {top_skill}, CAD modeling, FEA simulation, and workshop fabrication.'\n3. Practical Projects: 'Applied these skills in designing functional prototypes and performing stress analysis.'\n4. Career Goal: 'Excited to contribute to real-world mechanical design and plant operations.'"
        },
        {
            "id": "mech_hr_2",
            "difficulty": "Medium",
            "category": "Shop-floor Safety & Quality",
            "question": "How do you ensure strict adherence to industrial safety (PPE, 5S) and quality control when working on a manufacturing shop floor?",
            "acceptable_answers": [
                "Follow 5S methodology, strictly wear mandatory PPE, conduct risk assessments, and follow standard operating procedures (SOP).",
                "Prioritize safety compliance, quality inspection checklists, and clean organized workspace."
            ]
        },
        {
            "id": "mech_hr_3",
            "difficulty": "Medium",
            "category": "Handling Fabrication Delays",
            "question": "Describe a scenario during a mechanical project where raw material delivery or machining was delayed. How did you manage the timeline?",
            "acceptable_answers": [
                "Reordered workflow tasks, worked on parallel CAD/simulation modeling, and communicated with suppliers to recover lost time.",
                "Adjusted project schedule, focused on secondary components, and met project deadline."
            ],
            "model_answer": "Model Answer Structure (STAR):\n- Situation: 'During major project fabrication, CNC raw material delivery was delayed by one week.'\n- Task: 'Needed to prevent project schedule slippage.'\n- Action: 'Advanced CAD simulation and drawing documentation in parallel, pre-assembled standard hardware, and arranged accelerated machining.'\n- Result: 'Completed project testing on schedule with full quality compliance.'"
        },
        {
            "id": "mech_hr_4",
            "difficulty": "Hard",
            "category": "Interdisciplinary Team Collaboration",
            "question": "How do you effectively collaborate with electrical, electronics, and software engineers on mechatronic product designs?",
            "acceptable_answers": [
                "Establish clear interface standards, communicate spatial/mounting constraints early, and participate in joint design reviews.",
                "Collaborate openly, defining clear mechanical-electrical interfaces and sensor mounting points."
            ]
        },
        {
            "id": "mech_hr_5",
            "difficulty": "Hard",
            "category": "Career Vision in Manufacturing/Design",
            "question": "Where do you see yourself in 3 to 5 years within the mechanical engineering industry?",
            "acceptable_answers": [
                "Aiming to grow into a Senior Mechanical Design / Operations Engineer, leading product innovation and plant optimization.",
                "Seeking expertise in advanced CAD/FEA simulation, product development, or manufacturing management."
            ]
        },
        {
            "id": "mech_hr_6",
            "difficulty": "Easy",
            "category": "Hands-on Workshop Experience",
            "question": "What hands-on machine shop tools (lathe, milling machine, 3D printer, welding rig) are you most confident operating?",
            "acceptable_answers": [
                "Experienced with lathe turning, milling, drilling, and 3D printing setup.",
                "Hands-on experience in machine shop tools and additive manufacturing."
            ],
            "model_answer": "Model Answer:\n'I am confident operating conventional lathe and milling machines for turning and facing operations, as well as FDM 3D printers for rapid prototyping. I pay close attention to tool speeds, feeds, and safety guards.'"
        },
        {
            "id": "mech_hr_7",
            "difficulty": "Medium",
            "category": "Cost vs Quality Trade-offs",
            "question": "How do you balance structural quality and safety margins against manufacturing cost constraints?",
            "acceptable_answers": [
                "Use value engineering, select cost-effective standard materials, optimize manufacturing processes, while maintaining required FOS.",
                "Apply DFM and material optimization to reduce cost without compromising safety."
            ]
        },
        {
            "id": "mech_hr_8",
            "difficulty": "Medium",
            "category": "Handling Engineering Changes (ECO)",
            "question": "How do you handle late Engineering Change Orders (ECO) from clients or senior managers after production has started?",
            "acceptable_answers": [
                "Assess impact on tooling, cost, and lead time, document ECO changes clearly, and update CAD/drawing revisions.",
                "Evaluate modification feasibility, update BOM, and communicate revised schedule."
            ]
        },
        {
            "id": "mech_hr_9",
            "difficulty": "Hard",
            "category": "Root Cause Failure Investigation",
            "question": "Describe your approach to investigating a field component failure (fatigue crack, wear, corrosion).",
            "acceptable_answers": [
                "Use 5-Why analysis, inspect fracture surface (beach marks for fatigue), test material hardness/chemistry, and redesign part.",
                "Conduct failure analysis using visual inspection, stress evaluation, and root cause methodology."
            ]
        },
        {
            "id": "mech_hr_10",
            "difficulty": "Easy",
            "category": "Work Preference (Site vs Design Office)",
            "question": "Are you comfortable working on industrial plant sites or shop floors in challenging physical environments?",
            "acceptable_answers": [
                "Fully comfortable working on plant sites and shop floors; value hands-on field experience alongside office design work.",
                "Enthusiastic about hands-on site work and plant operations."
            ]
        },
        {
            "id": "mech_hr_11",
            "difficulty": "Medium",
            "category": "Constructive Feedback in Design",
            "question": "How do you respond when a senior design checker rejects your CAD model or drawing during design review?",
            "acceptable_answers": [
                "Understand the feedback regarding tolerances or DFM, revise the CAD model promptly, and learn drawing best practices.",
                "Accept constructive critique, review tolerance stack-up, and update drawing standards."
            ]
        },
        {
            "id": "mech_hr_12",
            "difficulty": "Hard",
            "category": "Resource Allocation & Shift Management",
            "question": "How would you handle a situation where two CNC machines break down simultaneously during a critical production run?",
            "acceptable_answers": [
                "Notify maintenance immediately, re-route priority jobs to backup machines, adjust shift schedules, and communicate revised ETA.",
                "Prioritize critical customer orders, coordinate maintenance repair, and optimize remaining machine capacity."
            ]
        },
        {
            "id": "mech_hr_13",
            "difficulty": "Easy",
            "category": "Key Engineering Strength",
            "question": "What is your biggest strength as a Mechanical Engineer?",
            "acceptable_answers": [
                "Strong spatial visualization, proficiency in 3D CAD modeling, and methodical approach to stress and thermal calculations.",
                "Practical problem solving, attention to GD&T tolerances, and dedication to safety."
            ]
        },
        {
            "id": "mech_hr_14",
            "difficulty": "Medium",
            "category": "Company & Industry Alignment",
            "question": "Why do you want to work for our manufacturing / engineering organization?",
            "acceptable_answers": [
                "Impressed by company's advanced manufacturing capabilities, product quality, and opportunities for mechanical engineering growth.",
                "Strong alignment with company's engineering domain and industrial projects."
            ]
        },
        {
            "id": "mech_hr_15",
            "difficulty": "Hard",
            "category": "Continuous Learning & Automation Trends",
            "question": "How are you preparing for Industry 4.0, smart manufacturing, and AI in mechanical design?",
            "acceptable_answers": [
                "Learning Python for engineering automation, studying IoT sensor integration, and exploring generative CAD design.",
                "Keeping updated with additive manufacturing, smart sensors, and automated CAD workflows."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
