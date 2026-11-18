# =====================================================================
# MECHANICAL - ROUND 2: BRANCH PROBLEM SOLVING (NON-CODING ASSESSMENT)
# =====================================================================

def get_mech_coding(skills=None, projects=None, used_ids=None, resume_text=""):
    """
    Generates a pool of 15 Non-Coding Mechanical Engineering Problem Solving Questions.
    Tailored specifically for Mechanical Engineering (Thermodynamics, Materials, Fluid, Design, Machining).
    No programming/coding required under any circumstances!
    """
    skills = skills or []
    projects = projects or []
    used_set = set(used_ids or [])

    sk1 = skills[0] if skills else "SolidWorks / Thermodynamics"
    proj = projects[0] if projects else "Mechanical Project"

    master_pool = [
        {
            "id": "mech_noncode_1",
            "difficulty": "Easy",
            "category": f"Stress & Strain Analysis ({sk1})",
            "question": f"Calculate Normal Stress (in MPa) and Longitudinal Strain for a steel bar subjected to axial tensile force F = 50 kN. Bar cross-sectional area A = 250 mm², initial length L0 = 500 mm, and measured elongation ΔL = 0.5 mm. Show calculation steps. (Resume Skill: {sk1})",
            "expected_input_output": "Input: F = 50000 N, A = 250 mm², L0 = 500 mm, ΔL = 0.5 mm\nOutput: Stress σ = 200.0 MPa, Strain ε = 0.001",
            "solution_code": "",
            "time_complexity": "N/A - Mechanical Calculation",
            "space_complexity": "N/A - Solid Mechanics",
            "model_answer": "Model Solution & Steps:\n1. Stress σ = Force / Area = 50,000 N / 250 mm² = 200 N/mm² = 200.0 MPa\n2. Strain ε = ΔL / L0 = 0.5 mm / 500 mm = 0.001 (dimensionless).",
            "acceptable_answers": [
                "Stress = 200 MPa, Strain = 0.001.",
                "Divide force 50,000 N by area 250 mm2 to get 200 MPa stress; divide elongation 0.5 mm by 500 mm to get 0.001 strain."
            ]
        },
        {
            "id": "mech_noncode_2",
            "difficulty": "Medium",
            "category": f"Simply Supported Beam Maximum Deflection ({proj})",
            "question": f"Calculate the maximum deflection d (in mm) at the center of a simply supported beam for '{proj}' subjected to a concentrated point load P = 10 kN at mid-span. Beam span L = 3.0 m, Young's Modulus E = 210 GPa, Moment of Inertia I = 5 x 10^-6 m^4. (Formula: d = P*L^3 / (48*E*I)).",
            "expected_input_output": "Input: P = 10000 N, L = 3 m, E = 210e9 Pa, I = 5e-6 m^4\nOutput: Deflection d = 5.36 mm",
            "solution_code": "",
            "time_complexity": "N/A - Beam Theory Math",
            "space_complexity": "N/A - Structural Mechanics",
            "acceptable_answers": [
                "d = (10000 * 3^3) / (48 * 210e9 * 5e-6) = 270000 / 50400000 = 0.005357 m = 5.36 mm.",
                "Apply point load deflection equation d = PL^3/(48EI) yielding 5.36 mm maximum center deflection."
            ]
        },
        {
            "id": "mech_noncode_3",
            "difficulty": "Hard",
            "category": "Compound Gear Train Output RPM & Torque",
            "question": "A compound gear train consists of Driver Gear A (20 teeth) driving Gear B (40 teeth) on intermediate shaft 1, which also key-mounts Gear C (15 teeth) driving Output Gear D (45 teeth). If input motor speed NA = 1440 RPM and input torque TA = 50 Nm, calculate Output RPM ND and Output Torque TD (assuming 100% efficiency).",
            "expected_input_output": "Input: NA = 1440 RPM, Teeth A=20, B=40, C=15, D=45, TA = 50 Nm\nOutput: Speed Ratio = 1/6, ND = 240 RPM, Output Torque TD = 300 Nm",
            "solution_code": "",
            "time_complexity": "N/A - Machine Design",
            "space_complexity": "N/A - Gear Kinematics",
            "model_answer": "Model Solution Steps:\n1. Speed Ratio i = (TA/TB) * (TC/TD) = (20/40) * (15/45) = (1/2) * (1/3) = 1/6\n2. Output Speed ND = NA * i = 1440 / 6 = 240 RPM\n3. Output Torque TD = TA / i = 50 * 6 = 300 Nm.",
            "acceptable_answers": [
                "Overall gear ratio = (20/40)*(15/45) = 1/6; ND = 1440 / 6 = 240 RPM; TD = 50 * 6 = 300 Nm.",
                "Multiply driver/driven teeth ratios to find 1/6 speed ratio. Output speed is 240 RPM and torque is 300 Nm."
            ]
        },
        {
            "id": "mech_noncode_4",
            "difficulty": "Easy",
            "category": "Composite Wall Heat Transfer Rate",
            "question": "Calculate the steady-state heat transfer rate Q (in Watts) per m² area through a two-layer composite wall. Layer 1 (brick): thickness L1 = 0.1 m, k1 = 0.8 W/m·K. Layer 2 (insulation): thickness L2 = 0.05 m, k2 = 0.04 W/m·K. Temperature difference ΔT = 100 °C.",
            "expected_input_output": "Input: L1 = 0.1m, k1 = 0.8, L2 = 0.05m, k2 = 0.04, ΔT = 100°C\nOutput: Total Thermal Resistance R = 1.375 K·m²/W, Heat Rate Q = 72.73 W/m²",
            "solution_code": "",
            "time_complexity": "N/A - Heat Transfer",
            "space_complexity": "N/A - Conduction Analysis",
            "acceptable_answers": [
                "R1 = 0.1/0.8 = 0.125; R2 = 0.05/0.04 = 1.25; Total R = 1.375; Q = 100 / 1.375 = 72.73 W/m2.",
                "Sum layer thermal resistances (0.125 + 1.25 = 1.375) and divide 100°C by total resistance to get 72.73 Watts per m2."
            ]
        },
        {
            "id": "mech_noncode_5",
            "difficulty": "Medium",
            "category": "Otto Cycle Ideal Thermal Efficiency",
            "question": "Calculate the ideal thermal efficiency (%) of an air-standard Otto cycle operating with a compression ratio r = 8.5 and specific heat ratio gamma (γ) = 1.4. (Formula: η = 1 - (1 / r^(γ-1))).",
            "expected_input_output": "Input: Compression ratio r = 8.5, γ = 1.4\nOutput: Thermal Efficiency η = 57.52%",
            "solution_code": "",
            "time_complexity": "N/A - Thermodynamics Math",
            "space_complexity": "N/A - IC Engine Analysis",
            "acceptable_answers": [
                "η = 1 - (1 / 8.5^0.4) = 1 - (1 / 2.3536) = 1 - 0.4248 = 0.5752 = 57.52%.",
                "Apply Otto cycle efficiency equation 1 - 1/(r^(gamma-1)) for compression ratio 8.5 yielding 57.52%."
            ]
        },
        {
            "id": "mech_noncode_6",
            "difficulty": "Hard",
            "category": "Lathe Machining Cutting Speed & Turning Time",
            "question": "A cylindrical workpiece (diameter D = 50 mm, length L = 200 mm) is turned on a lathe at spindle speed N = 500 RPM with feed rate f = 0.2 mm/rev. Calculate Cutting Speed V (m/min) and Total Machining Time T (minutes).",
            "expected_input_output": "Input: D = 50 mm, L = 200 mm, N = 500 RPM, f = 0.2 mm/rev\nOutput: Cutting Speed V = 78.54 m/min, Machining Time T = 2.0 minutes",
            "solution_code": "",
            "time_complexity": "N/A - Manufacturing Processes",
            "space_complexity": "N/A - Machining Calculations",
            "acceptable_answers": [
                "V = (pi * D * N) / 1000 = (3.1416 * 50 * 500) / 1000 = 78.54 m/min; T = L / (f * N) = 200 / (0.2 * 500) = 2.0 min.",
                "Calculate cutting speed V = pi*D*N/1000 = 78.54 m/min and machining time T = L/(f*N) = 2 minutes."
            ]
        },
        {
            "id": "mech_noncode_7",
            "difficulty": "Easy",
            "category": "Fluid Mechanics Bernoulli Pressure Head",
            "question": "In a horizontal pipe conveying water, section 1 has diameter D1 = 200 mm, pressure P1 = 200 kPa, velocity v1 = 2 m/s. Section 2 constricts to diameter D2 = 100 mm. Calculate velocity v2 and static pressure P2 at section 2 (ignoring friction).",
            "expected_input_output": "Input: D1 = 0.2m, P1 = 200 kPa, v1 = 2 m/s, D2 = 0.1m\nOutput: Velocity v2 = 8 m/s, Pressure P2 = 170 kPa",
            "solution_code": "",
            "time_complexity": "N/A - Fluid Dynamics",
            "space_complexity": "N/A - Bernoulli Analysis",
            "acceptable_answers": [
                "v2 = v1 * (D1/D2)^2 = 2 * 4 = 8 m/s; Bernoulli: P1 + 0.5*rho*v1^2 = P2 + 0.5*rho*v2^2 -> P2 = 200k + 0.5*1000*(4 - 64) = 170 kPa.",
                "Continuity gives v2 = 8 m/s. Applying Bernoulli's equation yields Section 2 pressure P2 = 170 kPa."
            ]
        },
        {
            "id": "mech_noncode_8",
            "difficulty": "Medium",
            "category": "Refrigeration Cycle COP (Carnot Limit)",
            "question": "A domestic refrigerator maintains food at T_cold = -5 °C (268 K) while rejecting heat to ambient air at T_hot = 35 °C (308 K). Calculate maximum theoretical Carnot Coefficient of Performance (COP_ref).",
            "expected_input_output": "Input: T_cold = 268 K, T_hot = 308 K\nOutput: COP_Carnot = 268 / (308 - 268) = 6.70",
            "solution_code": "",
            "time_complexity": "N/A - Refrigeration & HVAC",
            "space_complexity": "N/A - Thermal Science",
            "acceptable_answers": [
                "COP = T_cold / (T_hot - T_cold) = 268 / (308 - 268) = 268 / 40 = 6.70.",
                "Divide absolute low temperature 268 K by temperature difference 40 K to obtain maximum Carnot COP of 6.70."
            ]
        },
        {
            "id": "mech_noncode_9",
            "difficulty": "Hard",
            "category": "Torsional Shear Stress in Circular Shaft",
            "question": "Calculate maximum shear stress τ (in MPa) in a solid circular steel shaft of diameter d = 50 mm transmitting Torque T = 2.5 kNm. (Formula: τ = 16*T / (pi * d^3)).",
            "expected_input_output": "Input: Torque T = 2500 Nm, Diameter d = 0.05 m\nOutput: Max Torsional Shear Stress τ = 101.86 MPa",
            "solution_code": "",
            "time_complexity": "N/A - Strength of Materials",
            "space_complexity": "N/A - Shaft Design",
            "acceptable_answers": [
                "τ = (16 * 2500) / (pi * 0.05^3) = 40000 / 0.0003927 = 101859163 Pa = 101.86 MPa.",
                "Apply torsion formula tau = 16T/(pi*d^3) for 2.5 kNm torque and 50 mm diameter shaft to get 101.86 MPa."
            ]
        },
        {
            "id": "mech_noncode_10",
            "difficulty": "Easy",
            "category": "Thin Cylindrical Pressure Vessel Stress",
            "question": "A thin cylindrical boiler drum (diameter D = 1.0 m, wall thickness t = 10 mm) is subjected to internal steam pressure p = 2.0 MPa. Calculate the Hoop (Circumferential) Stress and Longitudinal Stress.",
            "expected_input_output": "Input: D = 1000 mm, t = 10 mm, p = 2.0 MPa\nOutput: Hoop Stress σ_h = 100.0 MPa, Longitudinal Stress σ_l = 50.0 MPa",
            "solution_code": "",
            "time_complexity": "N/A - Pressure Vessel Design",
            "space_complexity": "N/A - Solid Mechanics",
            "acceptable_answers": [
                "Hoop Stress = p*D/(2*t) = (2 * 1000)/(2 * 10) = 100 MPa; Longitudinal Stress = p*D/(4*t) = 50 MPa.",
                "Hoop stress pd/(2t) is 100 MPa; Longitudinal stress pd/(4t) is 50 MPa."
            ]
        },
        {
            "id": "mech_noncode_11",
            "difficulty": "Medium",
            "category": "Flywheel Energy Storage & Speed Fluctuation",
            "question": "A punch press flywheel absorbs maximum fluctuation of energy ΔE = 3000 Joules during a punching operation. Mean speed N = 300 RPM (omega = 31.42 rad/s) and coefficient of fluctuation of speed Cs = 0.04. Calculate required Mass Moment of Inertia I (kg·m²).",
            "expected_input_output": "Input: ΔE = 3000 J, ω = 31.42 rad/s, Cs = 0.04\nOutput: Moment of Inertia I = 3000 / (0.04 * 31.42^2) = 76.0 kg·m²",
            "solution_code": "",
            "time_complexity": "N/A - Dynamics of Machinery",
            "space_complexity": "N/A - Flywheel Design",
            "acceptable_answers": [
                "I = ΔE / (Cs * omega^2) = 3000 / (0.04 * 987.2) = 75.97 kg·m2.",
                "Apply energy fluctuation formula deltaE = I * Cs * omega^2 to solve for moment of inertia I = 76 kg·m2."
            ]
        },
        {
            "id": "mech_noncode_12",
            "difficulty": "Hard",
            "category": "Chvorinov's Rule Solidification Time in Casting",
            "question": "Using Chvorinov's Rule (t = B * (V/A)²), calculate solidification time t (minutes) for a spherical steel casting of diameter D = 0.2 m if mold constant B = 2.0 min/cm².",
            "expected_input_output": "Input: Sphere D = 20 cm, V/A = D/6 = 3.33 cm, B = 2.0 min/cm²\nOutput: Solidification Time t = 2.0 * (3.33)² = 22.2 minutes",
            "solution_code": "",
            "time_complexity": "N/A - Casting & Foundry",
            "space_complexity": "N/A - Manufacturing Processes",
            "acceptable_answers": [
                "For sphere: V/A = (pi*D^3/6) / (pi*D^2) = D / 6 = 20 cm / 6 = 3.33 cm. t = 2.0 * (3.33^2) = 22.2 minutes.",
                "Volume to surface ratio for sphere is D/6 = 3.33 cm. Chvorinov solidification time is 2 * (3.33)^2 = 22.2 min."
            ]
        },
        {
            "id": "mech_noncode_13",
            "difficulty": "Easy",
            "category": "Hooke's Law & Modulus of Rigidity (G)",
            "question": "State the relationship between Young's Modulus E, Modulus of Rigidity G, and Poisson's Ratio ν (nu). Calculate Shear Modulus G if E = 200 GPa and ν = 0.3.",
            "expected_input_output": "Input: E = 200 GPa, ν = 0.3\nOutput: Formula E = 2G(1+ν) -> Shear Modulus G = 76.92 GPa",
            "solution_code": "",
            "time_complexity": "N/A - Elasticity Theory",
            "space_complexity": "N/A - Materials Science",
            "acceptable_answers": [
                "G = E / (2 * (1 + nu)) = 200 / (2 * 1.3) = 200 / 2.6 = 76.92 GPa.",
                "Relationship is E = 2G(1+nu). Substituting E=200 GPa and Poisson ratio 0.3 yields Shear Modulus G = 76.92 GPa."
            ]
        },
        {
            "id": "mech_noncode_14",
            "difficulty": "Medium",
            "category": "Reynolds Number & Laminar/Turbulent Flow",
            "question": "Calculate the Reynolds Number (Re) for oil flowing through a 50 mm diameter pipe at velocity v = 1.2 m/s. Oil density rho = 850 kg/m³, dynamic viscosity mu = 0.15 Pa·s. Classify whether the flow is Laminar or Turbulent.",
            "expected_input_output": "Input: D = 0.05 m, v = 1.2 m/s, ρ = 850 kg/m³, µ = 0.15 Pa·s\nOutput: Re = 340 (Re < 2000 -> Laminar Flow)",
            "solution_code": "",
            "time_complexity": "N/A - Fluid Mechanics",
            "space_complexity": "N/A - Flow Regimes",
            "acceptable_answers": [
                "Re = (rho * v * D) / mu = (850 * 1.2 * 0.05) / 0.15 = 51 / 0.15 = 340. Since Re < 2000, flow is Laminar.",
                "Calculate Reynolds number Re = (rho*v*D)/mu = 340. Flow is laminar because Re is well below 2000."
            ]
        },
        {
            "id": "mech_noncode_15",
            "difficulty": "Hard",
            "category": "IC Engine Brake Power & Thermal Efficiency",
            "question": "A 4-cylinder 4-stroke petrol engine running at 3000 RPM produces a brake torque T = 150 Nm and consumes fuel at a rate of 12 kg/hour. Fuel calorific value CV = 44,000 kJ/kg. Calculate Brake Power (kW) and Brake Thermal Efficiency (%).",
            "expected_input_output": "Input: N = 3000 RPM, T = 150 Nm, Fuel = 12 kg/h, CV = 44000 kJ/kg\nOutput: Brake Power = 47.12 kW, Heat Input = 146.67 kW, Brake Thermal Efficiency = 32.13%",
            "solution_code": "",
            "time_complexity": "N/A - Thermal Engineering",
            "space_complexity": "N/A - Engine Performance",
            "acceptable_answers": [
                "Brake Power = (2 * pi * 3000 * 150) / 60000 = 47.12 kW; Heat Input = (12/3600) * 44000 = 146.67 kW; Efficiency = 47.12 / 146.67 = 32.13%.",
                "Power = 2*pi*N*T/60000 = 47.12 kW. Fuel energy rate = 146.67 kW. Brake thermal efficiency = 32.13%."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
