# =====================================================================
# MECHANICAL - ROUND 1: APTITUDE (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_mech_aptitude(used_ids=None):
    used_set = set(used_ids or [])
    master_pool = [
        {
            "id": "mech_apt_1",
            "category": "Quantitative Aptitude (Ratios & Geometry)",
            "difficulty": "Easy",
            "question": "Q1: A gear wheel with 30 teeth rotates at 120 RPM and drives a smaller gear with 15 teeth. What is the rotational speed of the smaller gear?",
            "options": ["A) 60 RPM", "B) 180 RPM", "C) 240 RPM", "D) 300 RPM"],
            "correct_option": "C) 240 RPM",
            "explanation": "Gear ratio N1*T1 = N2*T2. 120 * 30 = N2 * 15 => N2 = 3600/15 = 240 RPM.",
            "model_answer": "Gear ratio equation: N1 * T1 = N2 * T2\n120 * 30 = N2 * 15\nN2 = 3600 / 15 = 240 RPM."
        },
        {
            "id": "mech_apt_2",
            "category": "Quantitative Aptitude (Work & Power)",
            "difficulty": "Easy",
            "question": "Q2: An engine delivers 75 kW of power while consuming fuel at 15 kg/hr. What is the specific fuel consumption (SFC) in kg/kWh?",
            "options": ["A) 0.1 kg/kWh", "B) 0.2 kg/kWh", "C) 0.5 kg/kWh", "D) 5.0 kg/kWh"],
            "correct_option": "B) 0.2 kg/kWh",
            "explanation": "SFC = Fuel Consumption Rate / Power = 15 kg/hr / 75 kW = 0.2 kg/kWh."
        },
        {
            "id": "mech_apt_3",
            "category": "Logical Reasoning (Spatial Angles)",
            "difficulty": "Medium",
            "question": "Q3: In a mechanical linkage mechanism, if 3 links form a closed loop with 3 turning pairs, what is the degree of freedom (mobility) according to Kutzbach's criterion?",
            "options": ["A) 0 (Structure)", "B) 1 (Mechanism)", "C) 2", "D) -1"],
            "correct_option": "A) 0 (Structure)",
            "explanation": "F = 3(L-1) - 2j - H = 3(3-1) - 2(3) - 0 = 6 - 6 = 0. A 3-bar chain is a rigid structure."
        },
        {
            "id": "mech_apt_4",
            "category": "Analytical Reasoning (Work Done)",
            "difficulty": "Medium",
            "question": "Q4: A force of 500 N pushes a mechanical component across a friction surface by a distance of 10 meters in 5 seconds. What is the power exerted?",
            "options": ["A) 500 W", "B) 1000 W", "C) 2500 W", "D) 5000 W"],
            "correct_option": "B) 1000 W",
            "explanation": "Work = Force * Distance = 500 * 10 = 5000 J. Power = Work / Time = 5000 / 5 = 1000 W."
        },
        {
            "id": "mech_apt_5",
            "category": "Verbal Ability (Technical Documentation)",
            "difficulty": "Easy",
            "question": "Q5: Choose the correct technical sentence:",
            "options": [
                "A) The turbine efficiency increase when temperature rises.",
                "B) The turbine efficiency increases when temperature rises.",
                "C) The turbine efficiency increasing when temperature rise.",
                "D) The turbine efficiency increased when temperature rise."
            ],
            "correct_option": "B) The turbine efficiency increases when temperature rises.",
            "explanation": "Singular subject 'efficiency' takes singular verb 'increases'."
        },
        {
            "id": "mech_apt_6",
            "category": "Quantitative Aptitude (Thermal Expansion)",
            "difficulty": "Medium",
            "question": "Q6: A steel rod of length 2 meters expands by 1.2 mm when heated by 50°C. What is the coefficient of linear thermal expansion?",
            "options": ["A) 1.2 x 10^-5 /°C", "B) 2.4 x 10^-5 /°C", "C) 1.2 x 10^-6 /°C", "D) 6.0 x 10^-5 /°C"],
            "correct_option": "A) 1.2 x 10^-5 /°C",
            "explanation": "dL = L * alpha * dT => 0.0012 = 2 * alpha * 50 => alpha = 0.0012 / 100 = 1.2 x 10^-5 /°C.",
            "model_answer": "Formula: dL = L * alpha * dT\n0.0012 m = 2 m * alpha * 50°C\nalpha = 0.0012 / 100 = 1.2 x 10^-5 /°C."
        },
        {
            "id": "mech_apt_7",
            "category": "Logical Reasoning (Velocity Ratio)",
            "difficulty": "Medium",
            "question": "Q7: In a belt drive system, driver pulley diameter is 200 mm and driven pulley diameter is 400 mm. If driver speed is 1400 RPM, what is driven speed?",
            "options": ["A) 700 RPM", "B) 1400 RPM", "C) 2800 RPM", "D) 350 RPM"],
            "correct_option": "A) 700 RPM",
            "explanation": "N1 * D1 = N2 * D2 => 1400 * 200 = N2 * 400 => N2 = 700 RPM."
        },
        {
            "id": "mech_apt_8",
            "category": "Quantitative Aptitude (Pressure & Depth)",
            "difficulty": "Hard",
            "question": "Q8: What is the gauge pressure at a depth of 20 meters in a water reservoir (density = 1000 kg/m³, g = 9.81 m/s²)?",
            "options": ["A) 98.1 kPa", "B) 196.2 kPa", "C) 294.3 kPa", "D) 392.4 kPa"],
            "correct_option": "B) 196.2 kPa",
            "explanation": "P = rho * g * h = 1000 * 9.81 * 20 = 196,200 Pa = 196.2 kPa."
        },
        {
            "id": "mech_apt_9",
            "category": "Logical Reasoning (Number Series)",
            "difficulty": "Easy",
            "question": "Q9: Complete the series of machining feed rates: 0.1, 0.2, 0.4, 0.8, 1.6, ?",
            "options": ["A) 2.0", "B) 2.4", "C) 3.2", "D) 4.0"],
            "correct_option": "C) 3.2",
            "explanation": "Each term doubles the preceding term. 1.6 * 2 = 3.2."
        },
        {
            "id": "mech_apt_10",
            "category": "Quantitative Aptitude (Efficiency)",
            "difficulty": "Medium",
            "question": "Q10: A heat engine absorbs 500 J of heat from a hot reservoir and rejects 300 J of heat to a cold sink. What is its thermal efficiency?",
            "options": ["A) 20%", "B) 40%", "C) 60%", "D) 80%"],
            "correct_option": "B) 40%",
            "explanation": "Efficiency = (Q_in - Q_out) / Q_in = (500 - 300) / 500 = 200 / 500 = 40%.",
            "model_answer": "Efficiency = Work Output / Heat Input = (Q_h - Q_c) / Q_h\nEfficiency = (500 - 300) / 500 = 200 / 500 = 0.40 = 40%."
        },
        {
            "id": "mech_apt_11",
            "category": "Logical Reasoning (Vectors)",
            "difficulty": "Medium",
            "question": "Q11: Two perpendicular forces of 30 N and 40 N act on a mechanical component. What is the magnitude of the resultant force?",
            "options": ["A) 50 N", "B) 70 N", "C) 10 N", "D) 1200 N"],
            "correct_option": "A) 50 N",
            "explanation": "Resultant R = sqrt(30^2 + 40^2) = sqrt(900 + 1600) = sqrt(2500) = 50 N."
        },
        {
            "id": "mech_apt_12",
            "category": "Data Interpretation (Stress Strain)",
            "difficulty": "Hard",
            "question": "Q12: A tensile test specimen of cross-sectional area 100 mm² experiences a load of 20 kN. What is the stress induced?",
            "options": ["A) 20 MPa", "B) 200 MPa", "C) 2000 MPa", "D) 2 MPa"],
            "correct_option": "B) 200 MPa",
            "explanation": "Stress = Force / Area = 20,000 N / 100 mm² = 200 N/mm² = 200 MPa."
        },
        {
            "id": "mech_apt_13",
            "category": "Analytical Reasoning (Cam Profile)",
            "difficulty": "Hard",
            "question": "Q13: In a cam mechanism, if follower displacement is simple harmonic motion (SHM), what is the shape of its velocity curve?",
            "options": ["A) Straight line", "B) Parabola", "C) Sine / Cosine wave", "D) Constant"],
            "correct_option": "C) Sine / Cosine wave",
            "explanation": "Derivative of SHM displacement (sine) is SHM velocity (cosine curve)."
        },
        {
            "id": "mech_apt_14",
            "category": "Quantitative Aptitude (Mass & Torque)",
            "difficulty": "Easy",
            "question": "Q14: A torque of 100 Nm is applied to a flywheel of moment of inertia 5 kg·m². What is the angular acceleration?",
            "options": ["A) 20 rad/s²", "B) 25 rad/s²", "C) 50 rad/s²", "D) 500 rad/s²"],
            "correct_option": "A) 20 rad/s²",
            "explanation": "Torque T = I * alpha => alpha = 100 / 5 = 20 rad/s²."
        },
        {
            "id": "mech_apt_15",
            "category": "Verbal Ability (Precision Terms)",
            "difficulty": "Hard",
            "question": "Q15: Select the word that best describes 'the degree of closeness of repeated measurements to each other':",
            "options": ["A) Accuracy", "B) Precision", "C) Tolerance", "D) Calibration"],
            "correct_option": "B) Precision",
            "explanation": "Precision refers to repeatability/closeness of repeated measurements."
        }
    ]
    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
