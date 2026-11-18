# =====================================================================
# CIVIL - ROUND 3: CORE CIVIL TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_civil_technical(used_ids=None):
    used_set = set(used_ids or [])

    master_pool = [
        {
            "id": "civil_tech_1",
            "difficulty": "Easy",
            "category": "Concrete Technology (Grade & Workability)",
            "question": "What does 'M20' grade concrete mean? Explain the Slump Test for measuring concrete workability.",
            "acceptable_answers": [
                "M20 stands for Mix with 20 MPa characteristic compressive strength of 150mm cube at 28 days. Slump test measures consistency/workability.",
                "M20 means 20 N/mm² compressive strength at 28 days. Slump cone measures subsidence."
            ],
            "model_answer": "Model Answer:\nM20 Grade: 'M' stands for Mix, and '20' represents the characteristic 28-day compressive strength of a 150mm cube in N/mm² (MPa).\nSlump Test: A frustum cone (300mm high) is filled with fresh concrete in 4 tamped layers, inverted, and removed. The vertical drop (slump in mm) measures workability (e.g. 25-50mm for mass concrete, 75-100mm for heavily reinforced sections)."
        },
        {
            "id": "civil_tech_2",
            "difficulty": "Medium",
            "category": "Structural Engineering (Limit State Method)",
            "question": "Differentiate between Limit State of Collapse and Limit State of Serviceability according to IS 456.",
            "acceptable_answers": [
                "Limit State of Collapse deals with structural strength/failure (flexure, compression, shear, torsion). Serviceability deals with user comfort (deflection, cracking, vibration).",
                "Collapse = ultimate load capacity/yielding. Serviceability = deflection limits and crack width control."
            ]
        },
        {
            "id": "civil_tech_3",
            "difficulty": "Medium",
            "category": "Geotechnical Engineering (Compaction vs Consolidation)",
            "question": "Differentiate between Soil Compaction and Soil Consolidation.",
            "acceptable_answers": [
                "Compaction is rapid mechanical expulsion of air voids. Consolidation is slow time-dependent expulsion of pore water under sustained load.",
                "Compaction = air expulsion (instantaneous). Consolidation = pore water expulsion (gradual over time)."
            ]
        },
        {
            "id": "civil_tech_4",
            "difficulty": "Hard",
            "category": "Structural Analysis (Moment Distribution Method)",
            "question": "Explain Hardy Cross's Moment Distribution Method. What are Stiffness Factor and Distribution Factor?",
            "acceptable_answers": [
                "Moment distribution is an iterative method for analyzing indeterminate beams/frames. Stiffness factor k = 4EI/L (far end fixed). Distribution factor DF = k / Sum(k).",
                "Iterative method balancing joint moments based on member stiffness ratios."
            ],
            "model_answer": "Model Answer:\nMoment Distribution Method:\n1. Lock all joints and calculate Fixed End Moments (FEM).\n2. Calculate Stiffness Factor k for each member (k = 4EI/L if far end fixed, 3EI/L if far end hinged).\n3. Distribution Factor DF = k / sum(k) at a joint.\n4. Iteratively distribute unbalanced joint moments and carry over 50% (0.5) to far fixed ends until convergence."
        },
        {
            "id": "civil_tech_5",
            "difficulty": "Hard",
            "category": "Environmental Engineering (BOD vs COD)",
            "question": "Differentiate between Biochemical Oxygen Demand (BOD) and Chemical Oxygen Demand (COD) in wastewater analysis.",
            "acceptable_answers": [
                "BOD measures oxygen required by microorganisms to decompose biodegradable organic matter. COD measures oxygen required to chemically oxidize all organic matter (both bio and non-biodegradable). COD > BOD.",
                "BOD = biodegradable organic content (5-day test). COD = total chemical oxidation (higher value)."
            ]
        },
        {
            "id": "civil_tech_6",
            "difficulty": "Easy",
            "category": "Surveying (Total Station vs Leveling)",
            "question": "What is Total Station surveying and what parameters does it measure simultaneously?",
            "acceptable_answers": [
                "Total Station combines Electronic Distance Measurement (EDM) and electronic theodolite, measuring slope distance, horizontal angle, and vertical angle.",
                "Measures electronic distance, horizontal angles, and vertical angles simultaneously to compute 3D coordinates (X, Y, Z)."
            ]
        },
        {
            "id": "civil_tech_7",
            "difficulty": "Medium",
            "category": "Transportation Engineering (Flexible vs Rigid Pavement)",
            "question": "Compare Flexible Pavements (Bituminous) and Rigid Pavements (Concrete) in load distribution mechanism.",
            "acceptable_answers": [
                "Flexible pavement distributes load grain-to-grain layer by layer to subgrade. Rigid pavement acts as a slab transmitting load over wider area via flexural strength.",
                "Flexible = layer-by-layer pressure reduction. Rigid = slab action flexural distribution."
            ],
            "model_answer": "Model Answer:\n- Flexible Pavement (Asphalt): Low flexural strength. Distributes wheel load grain-to-grain down through sub-base to subgrade. Fails by rutting/fatigue cracking.\n- Rigid Pavement (RCC Slab): High flexural rigidity (slab action). Transmits load over a wide area like a beam/plate, bridging minor subgrade weaknesses."
        },
        {
            "id": "civil_tech_8",
            "difficulty": "Medium",
            "category": "Fluid Mechanics & Hydraulics (Specific Energy)",
            "question": "Define Specific Energy in open channel flow and explain Critical Depth.",
            "acceptable_answers": [
                "Specific energy E = y + V^2 / (2g) measured with respect to channel bed. Critical depth yc occurs at minimum specific energy for a given discharge.",
                "Specific energy is total energy head per unit weight above channel bottom. Critical depth yields minimum specific energy."
            ]
        },
        {
            "id": "civil_tech_9",
            "difficulty": "Hard",
            "category": "Prestressed Concrete (Pre-tensioning vs Post-tensioning)",
            "question": "Explain the difference between Pre-tensioning and Post-tensioning in Prestressed Concrete (PSC).",
            "acceptable_answers": [
                "Pre-tensioning stretches tendons BEFORE casting concrete; bond transfers prestress. Post-tensioning stretches tendons in ducts AFTER concrete hardens, anchored at ends.",
                "Pre-tensioning = tendon tensioned before pour. Post-tensioning = tendon tensioned after concrete reaches strength."
            ]
        },
        {
            "id": "civil_tech_10",
            "difficulty": "Easy",
            "category": "Foundation Engineering (Shallow vs Deep)",
            "question": "What is the criteria for classifying a foundation as Shallow or Deep according to Terzaghi?",
            "acceptable_answers": [
                "Shallow foundation: Depth of foundation D <= Width of foundation B. Deep foundation: D > B (e.g. Pile foundation).",
                "Foundation is shallow if D <= B; deep if depth is significantly greater than width."
            ]
        },
        {
            "id": "civil_tech_11",
            "difficulty": "Medium",
            "category": "Construction Management (CPM vs PERT)",
            "question": "Compare Critical Path Method (CPM) and Project Evaluation & Review Technique (PERT).",
            "acceptable_answers": [
                "CPM is deterministic (known activity durations) used in construction. PERT is probabilistic (3 time estimates: optimistic, most likely, pessimistic) used in R&D.",
                "CPM = deterministic time estimates. PERT = probabilistic beta distribution."
            ]
        },
        {
            "id": "civil_tech_12",
            "difficulty": "Hard",
            "category": "Seismic & Earthquake Design (IS 1893)",
            "question": "What is Response Reduction Factor (R) and Ductility detailing in earthquake-resistant design?",
            "acceptable_answers": [
                "Response reduction factor R accounts for inelastic energy dissipation. Ductility detailing (IS 13920) provides closely spaced stirrups to prevent brittle shear failure.",
                "R reduces elastic design seismic forces based on structural ductility. Ductile detailing prevents sudden collapse."
            ]
        },
        {
            "id": "civil_tech_13",
            "difficulty": "Easy",
            "category": "Building Materials (Bricks)",
            "question": "What are the characteristics of a First Class Brick according to IS specifications?",
            "acceptable_answers": [
                "Uniform color, sharp edges, metallic ringing sound when struck, water absorption < 20% by weight, compressive strength >= 10.5 N/mm².",
                "Metallic sound, uniform red color, no cracks, water absorption under 20%."
            ]
        },
        {
            "id": "civil_tech_14",
            "difficulty": "Medium",
            "category": "Soil Mechanics (Atterberg Limits)",
            "question": "Explain Liquid Limit (LL), Plastic Limit (PL), and Plasticity Index (IP).",
            "acceptable_answers": [
                "Liquid limit is boundary between liquid and plastic state. Plastic limit is boundary between plastic and semi-solid state. Plasticity Index IP = LL - PL.",
                "IP = LL - PL. Measures range of moisture content over which soil behaves plastically."
            ]
        },
        {
            "id": "civil_tech_15",
            "difficulty": "Hard",
            "category": "Hydrology (Unit Hydrograph)",
            "question": "What is a Unit Hydrograph (UH) and what are its fundamental assumptions?",
            "acceptable_answers": [
                "Unit Hydrograph is direct runoff hydrograph resulting from 1 cm of effective rainfall over specified duration. Assumptions: Linear response and time invariance.",
                "Direct runoff from 1 cm effective rainfall. Assumes linearity and time invariance."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
