# =====================================================================
# ENGINEERING BRANCHES & CAREER CONSTANTS
# =====================================================================

ENGINEERING_BRANCHES = [
    "CSE",
    "ECE",
    "Mechanical",
    "Civil"
]

BRANCH_FULL_NAMES = {
    "CSE": "CSE – Computer Science & Engineering",
    "ECE": "ECE – Electronics & Communication Engineering",
    "Mechanical": "Mechanical Engineering",
    "Civil": "Civil Engineering"
}

# Categorization of technical skills into clear functional domains per branch
SKILL_DOMAINS = {
    "CSE": {
        "Programming Languages": ["Python", "Java", "C++", "C", "JavaScript"],
        "Web & Frameworks": ["HTML", "CSS", "React", "Flask", "Django", "Streamlit"],
        "Data Science & AI": ["Machine Learning", "Deep Learning", "Scikit-learn", "NLP"],
        "Databases & Core CS": ["SQL", "Operating Systems", "Computer Networks", "DBMS", "Cloud Computing"]
    },
    "ECE": {
        "Embedded Systems": ["Embedded C", "Microcontrollers", "Arduino", "Raspberry Pi", "IoT"],
        "Electronics & Circuits": ["Digital Electronics", "Analog Electronics", "PCB Design", "Sensors"],
        "VLSI & Hardware": ["VLSI", "Verilog", "VHDL", "Microprocessors"],
        "Signals & Telecom": ["Signals and Systems", "Communication Systems", "MATLAB", "Simulink"]
    },
    "Mechanical": {
        "Thermal & Fluids": ["Thermodynamics", "Fluid Mechanics", "Heat Transfer", "HVAC"],
        "Design & Materials": ["Strength of Materials", "Machine Design", "Materials Science", "Engineering Mechanics"],
        "CAD/CAM & Simulation": ["AutoCAD", "SolidWorks", "CATIA", "ANSYS", "CAD/CAM"],
        "Manufacturing & Production": ["CNC", "Manufacturing Processes", "Production Engineering", "Robotics"]
    },
    "Civil": {
        "Structural & Materials": ["Structural Engineering", "Concrete Technology", "Steel Structures", "Structural Analysis"],
        "Geotechnical & Site": ["Soil Mechanics", "Geotechnical Engineering", "Surveying", "Foundation Engineering"],
        "Hydraulics & Environment": ["Hydraulics", "Fluid Flow", "Environmental Engineering", "Transportation Engineering"],
        "Design & Management": ["AutoCAD", "STAAD.Pro", "ETABS", "Construction Management", "Estimation", "Revit"]
    }
}

# Master Job-Role Dataset per Branch (Authoritative Dataset)
MASTER_JOB_ROLES = {
    "CSE": [
        {
            "role": "Python Developer",
            "required_skills": ["Python", "SQL", "Flask", "Django", "Git", "REST APIs", "Data Structures"],
            "explanation": "Strong match for candidates with backend development, SQL querying, and Python programming capabilities."
        },
        {
            "role": "Data Analyst",
            "required_skills": ["Python", "SQL", "Power BI", "MS Excel", "Scikit-learn", "Machine Learning"],
            "explanation": "Ideal for candidates with skills in data analysis, query optimization, visualization, and statistical modeling."
        },
        {
            "role": "Software Engineer",
            "required_skills": ["Java", "C++", "Python", "Data Structures", "Algorithms", "DBMS", "Operating Systems", "Computer Networks"],
            "explanation": "Suitable for candidates demonstrating solid CS core concepts, algorithmic logic, and software engineering."
        },
        {
            "role": "Web Developer",
            "required_skills": ["HTML", "CSS", "JavaScript", "React", "Flask", "Django", "REST APIs"],
            "explanation": "Fits candidates skilled in full-stack or frontend web development, responsive interfaces, and API integrations."
        },
        {
            "role": "Machine Learning Engineer",
            "required_skills": ["Python", "Machine Learning", "Deep Learning", "Scikit-learn", "NLP", "SQL"],
            "explanation": "Direct match for profiles featuring AI, machine learning pipelines, model development, and predictive analytics."
        },
        {
            "role": "Database / Cloud Engineer",
            "required_skills": ["SQL", "DBMS", "Operating Systems", "Computer Networks", "Cloud Computing", "Python"],
            "explanation": "Aligned with database architecture, system operations, network protocols, and cloud technologies."
        }
    ],
    "ECE": [
        {
            "role": "Embedded Systems Engineer",
            "required_skills": ["Embedded C", "Microcontrollers", "Arduino", "Raspberry Pi", "C", "C++", "Sensors", "IoT"],
            "explanation": "Matches candidate's firmware development, micro-controller programming, and hardware interfacing background."
        },
        {
            "role": "VLSI Design Engineer",
            "required_skills": ["VLSI", "Verilog", "VHDL", "Digital Electronics", "Microprocessors", "Analog Electronics"],
            "explanation": "Highly relevant for digital circuit synthesis, HDL simulation, and microelectronic hardware design."
        },
        {
            "role": "Electronics Engineer",
            "required_skills": ["PCB Design", "Digital Electronics", "Analog Electronics", "Sensors", "Microcontrollers"],
            "explanation": "Aligned with circuit design, schematic routing, electronic component testing, and PCB development."
        },
        {
            "role": "IoT Systems Engineer",
            "required_skills": ["IoT", "Sensors", "Embedded C", "Microcontrollers", "Communication Systems", "Arduino"],
            "explanation": "Great fit for wireless telemetry, connected sensor networks, and edge device architecture."
        },
        {
            "role": "Signal Processing Specialist",
            "required_skills": ["MATLAB", "Simulink", "Signals and Systems", "Communication Systems", "Digital Electronics"],
            "explanation": "Suited for signal analysis, communication system simulation, and mathematical domain modeling."
        }
    ],
    "Mechanical": [
        {
            "role": "Mechanical Design Engineer",
            "required_skills": ["SolidWorks", "AutoCAD", "CATIA", "Machine Design", "Strength of Materials", "Engineering Mechanics"],
            "explanation": "Direct match for 3D modeling, CAD drafting, structural tolerance, and mechanical component design."
        },
        {
            "role": "Thermal Systems Engineer",
            "required_skills": ["Thermodynamics", "Heat Transfer", "Fluid Mechanics", "ANSYS", "HVAC"],
            "explanation": "Ideal for thermal fluid design, heat exchanger modeling, energy systems, and fluid dynamics analysis."
        },
        {
            "role": "Manufacturing Engineer",
            "required_skills": ["CNC", "Manufacturing Processes", "Production Engineering", "CAD/CAM", "Materials Science"],
            "explanation": "Aligned with shop-floor manufacturing, CNC programming, tool design, and production engineering."
        },
        {
            "role": "FEA / Simulation Engineer",
            "required_skills": ["ANSYS", "SolidWorks", "Strength of Materials", "Machine Design", "CAD/CAM"],
            "explanation": "Tailored for finite element analysis, material stress simulation, and mechanical structural testing."
        },
        {
            "role": "Robotics & Automation Engineer",
            "required_skills": ["Manufacturing Processes", "CNC", "CAD/CAM", "Python", "Engineering Mechanics"],
            "explanation": "Matches automated assembly line design, robotic control systems, and industrial mechatronics."
        }
    ],
    "Civil": [
        {
            "role": "Structural Engineer",
            "required_skills": ["STAAD.Pro", "ETABS", "Structural Engineering", "Concrete Technology", "AutoCAD", "Revit"],
            "explanation": "Direct fit for building code compliance, concrete/steel structure analysis, and load design."
        },
        {
            "role": "Civil Site Engineer",
            "required_skills": ["Surveying", "Concrete Technology", "Soil Mechanics", "Construction Management", "Estimation"],
            "explanation": "Matches site execution, land surveying, material quality testing, and construction supervision."
        },
        {
            "role": "Geotechnical Engineer",
            "required_skills": ["Soil Mechanics", "Geotechnical Engineering", "Hydraulics", "Surveying", "Structural Engineering"],
            "explanation": "Suited for foundation design, soil bearing evaluation, retaining structures, and earthworks engineering."
        },
        {
            "role": "AutoCAD / BIM Draftsman",
            "required_skills": ["AutoCAD", "Revit", "Construction Management", "Estimation", "Structural Engineering"],
            "explanation": "Aligned with architectural detailing, 3D BIM modeling, structural drafting, and quantity estimation."
        },
        {
            "role": "Construction Project Manager",
            "required_skills": ["Construction Management", "Estimation", "AutoCAD", "Transportation Engineering"],
            "explanation": "Fits project planning, cost estimation, site logistics, safety compliance, and contract execution."
        }
    ]
}

# Next-step learning recommendations mapped to branch and target job roles
SKILL_ROADMAP_SUGGESTIONS = {
    "CSE": {
        "Python Developer": ["FastAPI", "Docker", "Git & GitHub", "PyTest", "PostgreSQL"],
        "Machine Learning Engineer": ["PyTorch / TensorFlow", "MLflow", "Pandas & NumPy", "Data Pipelines"],
        "Data Analyst": ["Tableau", "Pandas", "Statistical Analysis", "Advanced SQL Window Functions"],
        "Web Developer": ["Node.js", "TypeScript", "RESTful APIs", "Responsive CSS Frameworks"],
        "Software Engineer": ["Data Structures & Algorithms", "System Design", "Git", "CI/CD Pipelines"]
    },
    "ECE": {
        "Embedded Systems Engineer": ["RTOS Basics", "ARM Cortex Architecture", "I2C/SPI/UART Protocols", "Embedded C++"],
        "VLSI Design Engineer": ["SystemVerilog", "Cadence Virtuoso", "Digital ASIC Design", "FPGA Prototyping"],
        "IoT Engineer": ["MQTT Protocol", "ESP32 Firmware", "AWS IoT Core", "Sensor Interfacing"],
        "Electronics Engineer": ["Circuit Simulation (LTSpice)", "PCB Layout Routing", "Signal Integrity", "Microcontroller Timers"]
    },
    "Mechanical": {
        "Mechanical Design Engineer": ["Geometric Dimensioning & Tolerancing (GD&T)", "SolidWorks Surface Modeling", "FEA Analysis (ANSYS)", "DFM/DFA Principles"],
        "Thermal Systems Engineer": ["CFD (Fluent)", "Refrigeration Cycles", "Finite Volume Method", "Thermal Interface Materials"],
        "Manufacturing Engineer": ["Lean Manufacturing & 5S", "CNC G-Code / M-Code", "Quality Control (Six Sigma)", "Tool Design"],
        "Robotics Engineer": ["ROS (Robot Operating System)", "Kinematics & Dynamics", "PLC Programming", "Actuator Controls"]
    },
    "Civil": {
        "Structural Engineer": ["IS 456 / IS 800 Building Codes", "ETABS Seismic Design", "STAAD.Pro Concrete Design", "Revit Structure"],
        "Civil Site Engineer": ["Total Station Surveying", "Quality Inspection & Concrete Testing", "Bar Bending Schedules (BBS)", "Site Safety Compliance"],
        "Geotechnical Engineer": ["PLAXIS 2D/3D", "Retaining Wall Design", "Soil Mechanics Lab Testing", "PCC & Pile Foundation Design"],
        "Construction Project Manager": ["MS Project / Primavera P6", "Quantity Surveying & Estimation", "BIM Management", "Contract Management"]
    }
}
