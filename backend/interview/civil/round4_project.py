# =====================================================================
# CIVIL - ROUND 4: PROJECT & RESUME TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_civil_project_questions(projects=None, skills=None, used_ids=None):
    projects = projects or []
    skills = skills or []
    used_set = set(used_ids or [])

    p1 = projects[0] if projects else "Civil Structural / Site Project"
    p2 = projects[1] if len(projects) > 1 else (projects[0] if projects else "Geotechnical / Environmental Project")
    s1 = skills[0] if skills else "AutoCAD"
    s2 = skills[1] if len(skills) > 1 else "STAAD.Pro"

    master_pool = [
        {
            "id": "civil_proj_1",
            "difficulty": "Easy",
            "category": f"Structural / Site Project Overview ({p1})",
            "question": f"Walk me through the overall structural design, site layout, and engineering scope of your project '{p1}'. What was your individual role?",
            "acceptable_answers": [
                f"Detailed explanation of structural analysis, CAD drafting, soil report evaluation, and site execution for {p1}.",
                "Detailed summary of project scope, load calculations, structural framing, and site supervision."
            ],
            "model_answer": f"Model Answer Structure:\n1. Project Scope: Describe the civil engineering goal of '{p1}'.\n2. Design Approach: Outline drafting in {s1} and structural analysis in {s2}.\n3. Site Execution: Detail concrete mix selection, foundation depth, and rebar scheduling."
        },
        {
            "id": "civil_proj_2",
            "difficulty": "Medium",
            "category": f"Design Software ({s1} & {s2})",
            "question": f"Why did you choose **{s1}** and **{s2}** for modeling and analyzing '{p1}'? How did you verify the software output against manual IS code calculations?",
            "acceptable_answers": [
                f"Used {s1} for architectural/structural drafting and {s2} for 3D frame analysis, validating bending moments against IS 456 manual formulas.",
                "Cross-checked software shear force and moment diagrams with manual calculations."
            ]
        },
        {
            "id": "civil_proj_3",
            "difficulty": "Medium",
            "category": "Soil Investigation & Foundation Type",
            "question": f"What soil bearing capacity data was used for '{p1}' and how did you select between isolated footings vs raft/pile foundations?",
            "acceptable_answers": [
                "Selected foundation type based on Soil Investigation Report (SBC), column loads, and water table depth.",
                "Evaluated safe bearing capacity (SBC) from SPT soil test report to size footings."
            ]
        },
        {
            "id": "civil_proj_4",
            "difficulty": "Hard",
            "category": "Site Problem Solving & Defect Correction",
            "question": f"Describe a major site challenge or structural discrepancy encountered during '{p1}' (e.g. honeycombing, soil settlement, formwork displacement) and how you resolved it.",
            "acceptable_answers": [
                f"Identified concrete honeycombing or soil differential settlement in {p1}, applied non-shrink epoxy grouting or soil compaction, and re-inspected.",
                "Diagnosed structural defect on site, applied remedial grouting or structural retrofitting."
            ],
            "model_answer": "Model Answer Structure:\n1. Defect Identification: Detected honeycombing in column-beam junction during formwork stripping.\n2. Root Cause: Inadequate compaction / high rebar congestion blocking aggregate flow.\n3. Remedial Action: Chipped away loose concrete, cleaned with compressed air, applied polymer-modified bonding agent, and pressure-grouted non-shrink micro-concrete.\n4. Quality Inspection: Tested sound integrity using Ultrasonic Pulse Velocity (UPV)."
        },
        {
            "id": "civil_proj_5",
            "difficulty": "Hard",
            "category": f"Seismic & Wind Load Analysis ({p1})",
            "question": f"How did you apply seismic lateral loads (IS 1893) or wind loads (IS 875 Part 3) to the structural frame of '{p1}'?",
            "acceptable_answers": [
                f"Applied equivalent static / response spectrum seismic load combinations according to IS 1893 in {s2}.",
                "Calculated basic wind speed and zone factor for lateral load analysis."
            ]
        },
        {
            "id": "civil_proj_6",
            "difficulty": "Easy",
            "category": "Bar Bending Schedule (BBS) & Estimation",
            "question": f"How did you prepare the Bar Bending Schedule (BBS) and material quantity estimation for '{p1}'?",
            "acceptable_answers": [
                "Calculated cutting lengths including lap lengths, bend deductions, and development lengths (Ld) per IS 456.",
                "Tabulated rebar diameter, shape codes, cutting lengths, and steel tonnage."
            ]
        },
        {
            "id": "civil_proj_7",
            "difficulty": "Medium",
            "category": f"Secondary Project Scope ({p2})",
            "question": f"What was the main environmental, hydraulic, or transportation objective of your secondary project '{p2}'?",
            "acceptable_answers": [
                f"Designed drainage system, pavement layer, or water treatment process for {p2}.",
                "Executed secondary civil project focusing on site hydraulics or environmental treatment."
            ]
        },
        {
            "id": "civil_proj_8",
            "difficulty": "Hard",
            "category": "Quality Control & Concrete Testing",
            "question": f"What field and laboratory quality control tests (cube compression, slump, compaction factor, non-destructive UPV) were performed for '{p1}'?",
            "acceptable_answers": [
                "Cast 150mm cubes for 7-day and 28-day compression testing, monitored slump, and verified subgrade compaction with core cutter.",
                "Conducted 28-day cube strength testing, rebound hammer tests, and slump checks."
            ],
            "model_answer": "Model Answer:\nQuality Control Program:\n1. Fresh Concrete: Slump test for workability on every transit mixer load.\n2. Strength Verification: Cast 6 cubes per 50 m³ pour (tested at 7 and 28 days for characteristic strength).\n3. Non-Destructive Testing: Rebound Hammer & UPV testing for cured elements.\n4. Earthwork: Sand replacement / Core cutter test for 95% MDD compaction."
        },
        {
            "id": "civil_proj_9",
            "difficulty": "Hard",
            "category": "Drainage & Stormwater Management",
            "question": f"How did you design the surface drainage and rainwater runoff collection for '{p1}'?",
            "acceptable_answers": [
                "Calculated peak runoff using Rational Method (Q = C*I*A) and sized trapezoidal/box storm drains.",
                "Designed slope gradients, catch basins, and rainwater harvesting retention tanks."
            ]
        },
        {
            "id": "civil_proj_10",
            "difficulty": "Easy",
            "category": "Surveying & Setting Out",
            "question": f"Describe how you transferred grid lines and benchmarks to the construction site during setting out of '{p1}'.",
            "acceptable_answers": [
                "Established baseline and reference benchmarks using Total Station / Auto Level, marking column grid intersections with batter boards.",
                "Set out centerlines using Total Station and established site TBM."
            ]
        },
        {
            "id": "civil_proj_11",
            "difficulty": "Medium",
            "category": "Project Cost & Material Procurement",
            "question": f"How did you prepare the Bill of Quantities (BOQ) and Schedule of Rates (SOR) for '{p1}'?",
            "acceptable_answers": [
                "Detailed rate analysis for concrete, steel, masonry, and excavation based on PWD / CPWD Schedule of Rates.",
                "Estimated material quantities, labor rates, overheads, and total project cost."
            ]
        },
        {
            "id": "civil_proj_12",
            "difficulty": "Hard",
            "category": "Retaining Structure & Excavation Shoring",
            "question": f"If project '{p1}' involved deep excavation near existing buildings, what shoring or retaining wall system did you specify?",
            "acceptable_answers": [
                "Specified contiguous bored piles, sheet piling, or soldier piles with tieback anchors to prevent ground movement.",
                "Designed RCC cantilever retaining wall or soil nailing to stabilize slope."
            ]
        },
        {
            "id": "civil_proj_13",
            "difficulty": "Easy",
            "category": "Environmental & Safety Compliance",
            "question": "What environmental impact mitigations (dust suppression, noise control, waste management) were planned for the site of '{p1}'?",
            "acceptable_answers": [
                "Implemented water spraying for dust control, debris chutes, barricading, and proper concrete washwater disposal.",
                "Followed site safety rules, barricading, and waste management guidelines."
            ]
        },
        {
            "id": "civil_proj_14",
            "difficulty": "Medium",
            "category": "Formwork & Deshuttering Schedule",
            "question": f"What deshuttering (stripping) schedule was specified for slabs, beams, and columns in '{p1}' per IS 456?",
            "acceptable_answers": [
                "Columns/walls: 16-24 hrs; Slab soffits (props left under): 3 days; Beam soffits (props left under): 7 days; Prop removal: 7-21 days based on span.",
                "Stripping times: vertical faces 24h, slab soffits 3 days, beam props 14-21 days."
            ]
        },
        {
            "id": "civil_proj_15",
            "difficulty": "Hard",
            "category": "Green Building & Sustainable Civil Engineering",
            "question": f"What sustainable civil engineering practices (fly ash concrete, rainwater harvesting, solar integration) were integrated into '{p1}'?",
            "acceptable_answers": [
                "Used PPC cement with fly ash, recycled concrete aggregates, rainwater harvesting systems, and solar shading.",
                "Incorporated green building materials, fly ash concrete, and water recycling."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
