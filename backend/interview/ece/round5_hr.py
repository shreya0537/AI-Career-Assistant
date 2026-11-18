# =====================================================================
# ECE - ROUND 5: HR & BEHAVIORAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_ece_hr(username="Candidate", skills=None, used_ids=None):
    skills = skills or []
    used_set = set(used_ids or [])
    top_skill = skills[0] if skills else "Electronics & Communication"

    master_pool = [
        {
            "id": "ece_hr_1",
            "difficulty": "Easy",
            "category": "Self Introduction & Tech Interest",
            "question": f"Tell me about yourself, {username}. What inspired you to choose Electronics & Communication Engineering, and how have your skills in **{top_skill}** shaped your technical profile?",
            "acceptable_answers": [
                "Structured introduction highlighting interest in embedded hardware, VLSI, or telecom, alongside academic and project achievements.",
                "Summary of ECE academic background, hands-on lab work, and hardware/software skills."
            ],
            "model_answer": f"Model Answer Structure:\n1. Educational Foundation: 'I am an ECE graduate with a strong interest in embedded systems, digital electronics, and signal processing.'\n2. Key Technical Skills: 'I have developed solid competencies in {top_skill}, C/C++ programming, microcontroller interfacing, and circuit design.'\n3. Practical Exposure: 'I have applied these skills in building embedded hardware prototypes and driver code.'\n4. Career Goal: 'Enthusiastic about contributing to innovative hardware/embedded product development.'"
        },
        {
            "id": "ece_hr_2",
            "difficulty": "Medium",
            "category": "Hardware vs Software Balance",
            "question": "Do you view yourself primarily as an Embedded Software Engineer, VLSI Hardware Engineer, or Telecom Specialist?",
            "acceptable_answers": [
                "Clear preference for embedded firmware / VLSI design / telecom, explaining how ECE background bridges hardware and software.",
                "Positioned at the intersection of hardware circuit design and low-level software driver development."
            ]
        },
        {
            "id": "ece_hr_3",
            "difficulty": "Medium",
            "category": "Hardware Debugging Under Deadline",
            "question": "Describe a scenario where a hardware prototype stopped working right before a project demonstration. How did you handle the situation?",
            "acceptable_answers": [
                "Stayed calm, used systematic hardware debugging (multimeter, scope, serial logs), isolated faulty solder joint / code bug, and fixed it on time.",
                "Systematically checked power rails, pin connections, and code flags to resolve issue quickly."
            ],
            "model_answer": "Model Answer Structure (STAR):\n- Situation: 'During a final project demonstration rehearsal, our IoT board failed to initialize wireless communications.'\n- Task: 'Locate and resolve the hardware/firmware fault within 2 hours.'\n- Action: 'Checked power rail voltages with multimeter, monitored UART debug logs, and discovered a loose jumper wire and missing pull-up resistor.'\n- Result: 'Soldered resistor, re-verified wireless payload delivery, and delivered a successful demonstration.'"
        },
        {
            "id": "ece_hr_4",
            "difficulty": "Hard",
            "category": "Handling Hardware Component Obsolescence",
            "question": "What would you do if a critical IC component selected for a design becomes unavailable or end-of-life (EOL)?",
            "acceptable_answers": [
                "Search datasheets for pin-compatible alternatives, evaluate voltage/timing specs, modify firmware drivers if necessary, and re-test.",
                "Evaluate substitute components with matching footprints, pinouts, and electrical parameters."
            ]
        },
        {
            "id": "ece_hr_5",
            "difficulty": "Hard",
            "category": "Career Aspirations in Electronics",
            "question": "Where do you see yourself in 3 to 5 years within the semiconductor, embedded, or telecom industry?",
            "acceptable_answers": [
                "Aiming to become a Senior Embedded Architect / VLSI Design Specialist, leading chip/system development.",
                "Seeking deep expertise in hardware product development, RTOS systems, or digital IC design."
            ]
        },
        {
            "id": "ece_hr_6",
            "difficulty": "Easy",
            "category": "Lab & Instrument Experience",
            "question": "What lab instruments (Digital Storage Oscilloscope, Logic Analyzer, Function Generator, Soldering station) are you most comfortable using?",
            "acceptable_answers": [
                "Confident using Oscilloscopes for signal measurement, Multimeters for continuity/voltage checks, and Soldering irons for SMT/THT assembly.",
                "Hands-on experience with DSO, logic analyzer, multimeter, and soldering tools."
            ],
            "model_answer": "Model Answer:\n'I am highly comfortable using Digital Storage Oscilloscopes to view signal waveforms and bus timing, Logic Analyzers for debugging SPI/I2C packets, Digital Multimeters for voltage/current checks, and fine-tip soldering stations for SMT component soldering.'"
        },
        {
            "id": "ece_hr_7",
            "difficulty": "Medium",
            "category": "Continuous Learning in Semiconductor",
            "question": "How do you stay updated with rapidly advancing semiconductor nodes, RISC-V, and IoT security trends?",
            "acceptable_answers": [
                "Follow IEEE publications, semiconductor news, open-source RISC-V developments, and embedded forums.",
                "Read tech articles, research datasheets, and follow industry developments."
            ]
        },
        {
            "id": "ece_hr_8",
            "difficulty": "Medium",
            "category": "Quality vs Time-to-Market",
            "question": "How do you balance thorough hardware testing against aggressive time-to-market product launch schedules?",
            "acceptable_answers": [
                "Use automated test scripts, prioritize critical safety/functional tests, and conduct staged prototyping.",
                "Balance regression testing with agile hardware iterations."
            ]
        },
        {
            "id": "ece_hr_9",
            "difficulty": "Hard",
            "category": "Team Collaboration with Software Teams",
            "question": "How do you bridge communication gaps between hardware engineers and high-level software application developers?",
            "acceptable_answers": [
                "Create clear Hardware Abstraction Layer (HAL) APIs, document register maps clearly, and provide emulated hardware environments.",
                "Define precise API specifications and data structure formats for cross-team alignment."
            ]
        },
        {
            "id": "ece_hr_10",
            "difficulty": "Easy",
            "category": "Work Style Preference",
            "question": "Do you prefer hands-on bench testing in a hardware lab or writing firmware code at a workstation?",
            "acceptable_answers": [
                "Enjoy both equally: bench testing validates physical reality while firmware programming brings hardware to life.",
                "Appreciate the combination of lab testing and firmware software development."
            ]
        },
        {
            "id": "ece_hr_11",
            "difficulty": "Medium",
            "category": "Handling Peer Code/Design Review",
            "question": "How do you respond when a peer identifies a flaw in your circuit schematic or C code during a design review?",
            "acceptable_answers": [
                "Appreciate early error detection, review datasheets/code together, and update schematic/code promptly.",
                "Value peer feedback objectively to prevent costly hardware respawns."
            ]
        },
        {
            "id": "ece_hr_12",
            "difficulty": "Hard",
            "category": "Prioritizing Hardware Issues",
            "question": "How do you prioritize when faced with simultaneous issues in power management, RF interference, and firmware crashes?",
            "acceptable_answers": [
                "First stabilize power rails (foundation of all hardware), then resolve firmware stability, and finally optimize RF performance.",
                "Prioritize power system stability first, then firmware execution, followed by RF tuning."
            ]
        },
        {
            "id": "ece_hr_13",
            "difficulty": "Easy",
            "category": "Core Engineering Strength",
            "question": "What is your single greatest strength as an Electronics Engineer?",
            "acceptable_answers": [
                "Analytical circuit troubleshooting, fast datasheet comprehension, and structured C driver programming.",
                "Strong grasp of digital electronics, microcontroller peripherals, and signal debugging."
            ]
        },
        {
            "id": "ece_hr_14",
            "difficulty": "Medium",
            "category": "Company & Industry Alignment",
            "question": "Why do you want to work for our electronics / embedded technology company?",
            "acceptable_answers": [
                "Attracted by the company's cutting-edge products, innovation in embedded systems/VLSI, and strong engineering reputation.",
                "Strong alignment with company's hardware portfolio and technical growth opportunities."
            ]
        },
        {
            "id": "ece_hr_15",
            "difficulty": "Hard",
            "category": "Future Tech & AI on Edge",
            "question": "What are your thoughts on TinyML (Machine Learning on Microcontrollers) and AI at the Edge?",
            "acceptable_answers": [
                "TinyML enables ultra-low-power, low-latency intelligence on edge devices without cloud dependency, revolutionizing IoT.",
                "Edge AI minimizes bandwidth and latency while protecting user privacy."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
