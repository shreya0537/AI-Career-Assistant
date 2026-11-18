# =====================================================================
# CIVIL - ROUND 2: BRANCH PROBLEM SOLVING (NON-CODING ASSESSMENT)
# =====================================================================

def get_civil_coding(skills=None, projects=None, used_ids=None, resume_text=""):
    """
    Generates a pool of 15 Non-Coding Civil Engineering Problem Solving Questions.
    Tailored specifically for Civil Engineering (Structural, Geotechnical, Surveying, Hydraulics).
    No programming/coding required under any circumstances!
    """
    skills = skills or []
    projects = projects or []
    used_set = set(used_ids or [])

    sk1 = skills[0] if skills else "Structural Engineering / AutoCAD"
    proj = projects[0] if projects else "Civil Project"

    master_pool = [
        {
            "id": "civil_noncode_1",
            "difficulty": "Easy",
            "category": f"Concrete Mix Estimation ({sk1})",
            "question": f"Calculate the required bags of cement (50kg each), sand volume (m³), and aggregate volume (m³) for 10 m³ of M15 concrete (mix ratio 1:2:4, dry volume factor 1.54, cement density 1440 kg/m³). Show step-by-step math. (Resume Skill: {sk1})",
            "expected_input_output": "Input: Wet Concrete Vol = 10 m³, Ratio 1:2:4\nOutput: Cement Bags = 63.4, Sand = 4.4 m³, Aggregate = 8.8 m³",
            "solution_code": "",
            "time_complexity": "N/A - Civil Calculation",
            "space_complexity": "N/A - Material Estimation",
            "model_answer": "Model Solution & Steps:\n1. Dry Volume = 10 m³ * 1.54 = 15.4 m³\n2. Total Parts = 1 + 2 + 4 = 7\n3. Cement Vol = (1/7) * 15.4 = 2.2 m³\n4. Cement Weight = 2.2 * 1440 = 3168 kg -> Bags = 3168 / 50 = 63.36 bags\n5. Sand Vol = (2/7) * 15.4 = 4.4 m³\n6. Aggregate Vol = (4/7) * 15.4 = 8.8 m³.",
            "acceptable_answers": [
                "Dry volume = 15.4 m3, Cement bags = 63.4, Sand = 4.4 m3, Aggregate = 8.8 m3.",
                "Multiply 10m3 by 1.54 dry factor, divide by 7 parts, convert cement m3 to 50kg bags."
            ]
        },
        {
            "id": "civil_noncode_2",
            "difficulty": "Medium",
            "category": f"Surveying Leveling Data ({proj})",
            "question": f"Compute the Reduced Levels (RL) for '{proj}' using the Height of Instrument (HI) method. Benchmark RL = 100.00 m, Backsight = 1.25 m, Foresights at stations P1 and P2 are 1.85 m and 2.10 m respectively.",
            "expected_input_output": "Input: Initial RL = 100.0, BS = 1.25, FS1 = 1.85, FS2 = 2.10\nOutput: HI = 101.25 m, RL(P1) = 99.40 m, RL(P2) = 99.15 m",
            "solution_code": "",
            "time_complexity": "N/A - Surveying Math",
            "space_complexity": "N/A - Leveling Analysis",
            "acceptable_answers": [
                "HI = 100.00 + 1.25 = 101.25 m; RL(P1) = 101.25 - 1.85 = 99.40 m; RL(P2) = 101.25 - 2.10 = 99.15 m.",
                "Calculate HI by adding backsight to benchmark RL, then subtract foresights to find station RLs."
            ]
        },
        {
            "id": "civil_noncode_3",
            "difficulty": "Hard",
            "category": "RC Beam Ultimate Bending Moment Capacity",
            "question": "According to IS 456 Limit State Design, calculate the Ultimate Bending Moment Capacity Mu for a singly reinforced rectangular beam (b = 250 mm, effective depth d = 400 mm, fck = 20 MPa, fy = 415 MPa, tension steel Ast = 3 #16mm bars = 603 mm²).",
            "expected_input_output": "Input: b = 250mm, d = 400mm, fck = 20MPa, fy = 415MPa, Ast = 603mm²\nOutput: Neutral axis xu = 87.0 mm (xu < xu_max), Mu = 78.4 kNm",
            "solution_code": "",
            "time_complexity": "N/A - IS 456 Design",
            "space_complexity": "N/A - Structural Analysis",
            "model_answer": "Model Solution Steps (IS 456):\n1. xu = (0.87 * fy * Ast) / (0.36 * fck * b) = (0.87 * 415 * 603) / (0.36 * 20 * 250) = 87.0 mm\n2. xu_max for Fe 415 = 0.48 * 400 = 192 mm. Since xu < xu_max, section is under-reinforced.\n3. Mu = 0.87 * fy * Ast * d * [1 - (Ast * fy)/(b * d * fck)] = 78.4 kNm.",
            "acceptable_answers": [
                "xu = 87.0 mm, xu_max = 192 mm (under-reinforced), Mu = 78.4 kNm.",
                "Calculate depth of neutral axis xu using 0.87*fy*Ast/(0.36*fck*b) and evaluate moment capacity Mu = 78.4 kNm."
            ]
        },
        {
            "id": "civil_noncode_4",
            "difficulty": "Easy",
            "category": "Fluid Mechanics Pipe Discharge (Continuity)",
            "question": "Calculate the volumetric discharge rate Q (in liters per second, L/s) through a 150 mm diameter circular pipe if water flows at a uniform velocity v = 2.5 m/s.",
            "expected_input_output": "Input: Diameter D = 0.15 m, Velocity v = 2.5 m/s\nOutput: Area A = 0.01767 m², Discharge Q = 44.18 L/s",
            "solution_code": "",
            "time_complexity": "N/A - Hydraulics Math",
            "space_complexity": "N/A - Fluid Dynamics",
            "acceptable_answers": [
                "Area A = pi * (0.15^2) / 4 = 0.01767 m2; Q = A * v = 0.04418 m3/s = 44.18 L/s.",
                "Multiply pipe cross-sectional area by flow velocity to get 44.18 liters per second."
            ]
        },
        {
            "id": "civil_noncode_5",
            "difficulty": "Medium",
            "category": "Soil Bearing Capacity (Terzaghi Formula)",
            "question": "Calculate the ultimate bearing capacity qu of a 2.0 m wide strip footing on cohesionless soil (c = 0) with soil unit weight gamma = 18 kN/m³, depth Df = 1.5 m, and Terzaghi factors Nq = 18.4, Ngamma = 22.4.",
            "expected_input_output": "Input: B = 2.0m, Df = 1.5m, γ = 18 kN/m³, Nq = 18.4, Nγ = 22.4\nOutput: qu = γ*Df*Nq + 0.5*γ*B*Nγ = 496.8 kPa",
            "solution_code": "",
            "time_complexity": "N/A - Geotechnical Engineering",
            "space_complexity": "N/A - Foundation Design",
            "acceptable_answers": [
                "qu = gamma * Df * Nq + 0.5 * gamma * B * Ngamma = (18 * 1.5 * 18.4) + (0.5 * 18 * 2.0 * 22.4) = 496.8 kPa.",
                "Apply Terzaghi strip footing equation for cohesionless soil yielding 496.8 kPa ultimate bearing capacity."
            ]
        },
        {
            "id": "civil_noncode_6",
            "difficulty": "Hard",
            "category": "Structural Truss Joint Force Equilibrium",
            "question": "For a symmetrical 60° equilateral pin-jointed truss loaded with vertical force P = 50 kN at the apex joint, calculate the tensile force in the bottom chord member and compressive force in the sloping rafter members.",
            "expected_input_output": "Input: Apex Load P = 50 kN, 60° truss\nOutput: Rafter Compression = 28.87 kN, Bottom Chord Tension = 14.43 kN",
            "solution_code": "",
            "time_complexity": "N/A - Structural Mechanics",
            "space_complexity": "N/A - Statics Analysis",
            "acceptable_answers": [
                "Support reactions = 25 kN each. Rafter compression = 25 / sin(60°) = 28.87 kN; Bottom chord = 25 * cot(60°) = 14.43 kN.",
                "Use Method of Joints: Vertical reaction 25kN gives rafter force 28.87 kN compression and bottom member 14.43 kN tension."
            ]
        },
        {
            "id": "civil_noncode_7",
            "difficulty": "Easy",
            "category": "Highway Stopping Sight Distance (SSD)",
            "question": "Calculate the Stopping Sight Distance (SSD) for a highway design speed V = 80 km/h (22.22 m/s) assuming reaction time t = 2.5 seconds and coefficient of longitudinal friction f = 0.35 on a level road.",
            "expected_input_output": "Input: V = 22.22 m/s, t = 2.5s, f = 0.35\nOutput: Lag Distance = 55.55 m, Braking Distance = 71.45 m, SSD = 127.0 m",
            "solution_code": "",
            "time_complexity": "N/A - Transportation Engineering",
            "space_complexity": "N/A - Highway Design",
            "acceptable_answers": [
                "SSD = (v * t) + (v^2 / (2 * g * f)) = (22.22 * 2.5) + (22.22^2 / (2 * 9.81 * 0.35)) = 55.55 + 71.45 = 127.0 m.",
                "Sum lag distance (v*t = 55.55m) and braking distance (v^2/(2gf) = 71.45m) to get 127 meters SSD."
            ]
        },
        {
            "id": "civil_noncode_8",
            "difficulty": "Medium",
            "category": "Quantity Surveying Rate Analysis",
            "question": "Perform rate analysis to calculate required number of modular bricks (size 19cm x 9cm x 9cm) for 1 m³ of 1:6 cement-sand brick masonry work (allowing 10% extra for mortar joints and wastage).",
            "expected_input_output": "Input: Masonry Vol = 1 m³, Nominal brick size = 20cm x 10cm x 10cm\nOutput: Modular Bricks Required = 500 bricks",
            "solution_code": "",
            "time_complexity": "N/A - Estimation & Costing",
            "space_complexity": "N/A - Quantity Surveying",
            "acceptable_answers": [
                "Nominal brick volume with mortar = 0.20 x 0.10 x 0.10 = 0.002 m3. Bricks per m3 = 1 / 0.002 = 500 bricks.",
                "Standard modular brick volume including mortar is 0.002 m3, resulting in exactly 500 bricks per m3."
            ]
        },
        {
            "id": "civil_noncode_9",
            "difficulty": "Hard",
            "category": "Consolidation Settlement of Clay Layer",
            "question": "Calculate the primary consolidation settlement Sc of a 4.0 m thick saturated clay layer (Cc = 0.3, initial void ratio e0 = 0.8, initial effective stress sigma0' = 100 kPa, increase in stress delta_sigma' = 50 kPa).",
            "expected_input_output": "Input: H = 4.0m, Cc = 0.3, e0 = 0.8, σ0' = 100 kPa, Δσ' = 50 kPa\nOutput: Settlement Sc = (0.3 * 4.0 / 1.8) * log10(150 / 100) = 0.1174 m (117.4 mm)",
            "solution_code": "",
            "time_complexity": "N/A - Soil Mechanics",
            "space_complexity": "N/A - Geotechnical Analysis",
            "acceptable_answers": [
                "Sc = (Cc * H / (1 + e0)) * log10((sigma0 + delta_sigma) / sigma0) = (0.3 * 4.0 / 1.8) * log10(1.5) = 0.1174 m = 117.4 mm.",
                "Apply Terzaghi 1D consolidation settlement equation to obtain 117.4 mm settlement."
            ]
        },
        {
            "id": "civil_noncode_10",
            "difficulty": "Easy",
            "category": "BOD Removal Efficiency in Wastewater",
            "question": "Calculate the BOD removal efficiency (%) of a primary settling tank if raw sewage influent BOD5 is 250 mg/L and effluent BOD5 is 165 mg/L.",
            "expected_input_output": "Input: Influent BOD = 250 mg/L, Effluent BOD = 165 mg/L\nOutput: BOD Removal Efficiency = 34.0%",
            "solution_code": "",
            "time_complexity": "N/A - Environmental Engineering",
            "space_complexity": "N/A - Wastewater Treatment",
            "acceptable_answers": [
                "Efficiency = ((250 - 165) / 250) * 100 = (85 / 250) * 100 = 34.0%.",
                "Subtract effluent BOD from influent BOD and divide by influent BOD to get 34% removal efficiency."
            ]
        },
        {
            "id": "civil_noncode_11",
            "difficulty": "Medium",
            "category": "Retaining Wall Sliding Stability Factor",
            "question": "Calculate the Factor of Safety against sliding (FSS) for a gravity retaining wall. Total vertical weight W = 200 kN/m, soil friction angle delta = 30°, active earth pressure force Pa = 50 kN/m.",
            "expected_input_output": "Input: Weight W = 200 kN/m, tan(30°) = 0.577, Pa = 50 kN/m\nOutput: Sliding Force = 50 kN/m, Resisting Force = 115.4 kN/m, FSS = 2.31",
            "solution_code": "",
            "time_complexity": "N/A - Geotechnical Retaining Wall",
            "space_complexity": "N/A - Stability Analysis",
            "acceptable_answers": [
                "Resisting Force Fr = W * tan(delta) = 200 * 0.577 = 115.47 kN; FSS = Fr / Pa = 115.47 / 50 = 2.31.",
                "Multiply wall weight by tan(30°) to get friction resistance 115.4 kN, then divide by active pressure 50 kN to get FSS = 2.31."
            ]
        },
        {
            "id": "civil_noncode_12",
            "difficulty": "Hard",
            "category": "I-Beam Neutral Axis & Moment of Inertia",
            "question": "State the steps to calculate the Moment of Inertia Ixx about the centroidal X-X axis for an asymmetrical I-section beam using Parallel Axis Theorem (I = I_g + A * d²).",
            "expected_input_output": "Input: Asymmetrical I-beam dimensions\nOutput: 1. Find y_bar centroid, 2. Compute local Ig for flanges and web, 3. Add A*d² transfer distance for each component.",
            "solution_code": "",
            "time_complexity": "N/A - Solid Mechanics",
            "space_complexity": "N/A - Structural Mechanics",
            "acceptable_answers": [
                "Find centroid y_bar = Sum(A*y)/Sum(A), compute local Ig = b*h^3/12 for each rectangle, sum Ig + A*d^2.",
                "Locate neutral axis centroid, apply parallel axis theorem Ig + A*d^2 to top flange, web, and bottom flange."
            ]
        },
        {
            "id": "civil_noncode_13",
            "difficulty": "Easy",
            "category": "Concrete Water-Cement Ratio & Strength",
            "question": "Explain Abram's Law regarding water-cement ratio and compressive strength of concrete. What happens to compressive strength if w/c ratio is increased from 0.45 to 0.60?",
            "expected_input_output": "Input: w/c ratio increase from 0.45 to 0.60\nOutput: Compressive strength decreases significantly (Abram's Law inverse relationship).",
            "solution_code": "",
            "time_complexity": "N/A - Concrete Technology",
            "space_complexity": "N/A - Materials Science",
            "acceptable_answers": [
                "Abram's law states concrete strength is inversely proportional to water-cement ratio. Increasing w/c from 0.45 to 0.60 decreases strength.",
                "Compressive strength decreases as water-cement ratio increases due to increased porosity in cement paste matrix."
            ]
        },
        {
            "id": "civil_noncode_14",
            "difficulty": "Medium",
            "category": "Surveying Whole Circle to Quadrantal Bearing",
            "question": "Convert the Whole Circle Bearings (WCB) of lines AB (45° 30'), BC (135° 15'), CD (225° 45'), and DA (315° 00') into Quadrantal Bearings (QB).",
            "expected_input_output": "Input: 45°30', 135°15', 225°45', 315°00'\nOutput: AB: N 45°30' E, BC: S 44°45' E, CD: S 45°45' W, DA: N 45°00' W",
            "solution_code": "",
            "time_complexity": "N/A - Surveying Bearings",
            "space_complexity": "N/A - Compass Surveying",
            "acceptable_answers": [
                "AB = N 45°30' E, BC = S 44°45' E, CD = S 45°45' W, DA = N 45°00' W.",
                "Q1: N 45°30' E, Q2: S (180-135°15') E = S 44°45' E, Q3: S (225°45'-180) W = S 45°45' W, Q4: N (360-315) W = N 45°00' W."
            ]
        },
        {
            "id": "civil_noncode_15",
            "difficulty": "Hard",
            "category": "Flexible Pavement Layer Thickness (CBR Method)",
            "question": "Calculate the total pavement thickness T (cm) required using the IRC CBR formula T = sqrt[(1.75 * P / CBR) - (A / pi)] where commercial wheel load P = 4100 kg, subgrade CBR = 4%, contact area A = 640 cm².",
            "expected_input_output": "Input: P = 4100 kg, CBR = 4%, A = 640 cm²\nOutput: T = sqrt[(1.75 * 4100 / 4) - (640 / 3.1416)] = sqrt[1793.75 - 203.7] = 39.87 cm (~40 cm)",
            "solution_code": "",
            "time_complexity": "N/A - Pavement Engineering",
            "space_complexity": "N/A - Transportation Design",
            "acceptable_answers": [
                "T = sqrt[(1.75 * 4100 / 4) - (640 / pi)] = sqrt[1793.75 - 203.7] = 39.87 cm.",
                "Apply IRC CBR empirical pavement thickness equation yielding approximately 40 cm total pavement depth."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
