# =====================================================================
# CIVIL - ROUND 1: APTITUDE (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_civil_aptitude(used_ids=None):
    used_set = set(used_ids or [])

    master_pool = [
        {
            "id": "civil_apt_1",
            "category": "Quantitative Aptitude (Scale & Maps)",
            "difficulty": "Easy",
            "question": "Q1: On a civil engineering site plan, a scale of 1 cm = 5 meters is used. What actual ground distance is represented by a line measuring 8.4 cm on the plan?",
            "options": ["A) 38 meters", "B) 42 meters", "C) 45 meters", "D) 50 meters"],
            "correct_option": "B) 42 meters",
            "explanation": "Actual Distance = 8.4 cm * 5 m/cm = 42 meters.",
            "model_answer": "Actual distance = Map measurement * Scale factor\nDistance = 8.4 cm * 5 m/cm = 42 meters."
        },
        {
            "id": "civil_apt_2",
            "category": "Quantitative Aptitude (Concrete Volume)",
            "difficulty": "Easy",
            "question": "Q2: Calculate the total volume of concrete required for 4 identical columns of rectangular cross-section 0.5 m x 0.5 m and height 4 meters.",
            "options": ["A) 2.0 m³", "B) 4.0 m³", "C) 8.0 m³", "D) 16.0 m³"],
            "correct_option": "B) 4.0 m³",
            "explanation": "Volume of 1 column = 0.5 * 0.5 * 4 = 1.0 m³. For 4 columns = 4 * 1.0 = 4.0 m³."
        },
        {
            "id": "civil_apt_3",
            "category": "Logical Reasoning (Survey Bearings)",
            "difficulty": "Medium",
            "question": "Q3: If the Whole Circle Bearing (WCB) of a survey line is 225°, what is its Reduced Bearing (RB)?",
            "options": ["A) N 45° E", "B) S 45° W", "C) S 45° E", "D) N 45° W"],
            "correct_option": "B) S 45° W",
            "explanation": "225° lies in 3rd quadrant (SW). RB = WCB - 180° = 225° - 180° = S 45° W."
        },
        {
            "id": "civil_apt_4",
            "category": "Analytical Reasoning (Slope & Gradient)",
            "difficulty": "Medium",
            "question": "Q4: A road gradient rises by 3 meters over a horizontal distance of 60 meters. What is the gradient expressed as a percentage and ratio?",
            "options": ["A) 5% (1 in 20)", "B) 10% (1 in 10)", "C) 2% (1 in 50)", "D) 4% (1 in 25)"],
            "correct_option": "A) 5% (1 in 20)",
            "explanation": "Gradient = 3 / 60 = 1 / 20. Percentage = (3/60) * 100 = 5%."
        },
        {
            "id": "civil_apt_5",
            "category": "Verbal Ability (Technical Standards)",
            "difficulty": "Easy",
            "question": "Q5: Choose the correct technical sentence for site reports:",
            "options": [
                "A) The concrete slump test indicate good workability.",
                "B) The concrete slump test indicates good workability.",
                "C) The concrete slump test indicating good workability.",
                "D) The concrete slump test have indicated good workability."
            ],
            "correct_option": "B) The concrete slump test indicates good workability.",
            "explanation": "Singular subject 'test' takes singular verb 'indicates'."
        },
        {
            "id": "civil_apt_6",
            "category": "Quantitative Aptitude (Soil Void Ratio)",
            "difficulty": "Medium",
            "question": "Q6: If volume of voids Vv in a soil sample is 0.4 m³ and volume of solids Vs is 0.8 m³, what is the void ratio e?",
            "options": ["A) 0.33", "B) 0.50", "C) 0.67", "D) 1.20"],
            "correct_option": "B) 0.50",
            "explanation": "Void Ratio e = Vv / Vs = 0.4 / 0.8 = 0.50.",
            "model_answer": "Formula: Void Ratio (e) = Volume of Voids (Vv) / Volume of Solids (Vs)\ne = 0.4 / 0.8 = 0.50."
        },
        {
            "id": "civil_apt_7",
            "category": "Logical Reasoning (Flow Rate)",
            "difficulty": "Medium",
            "question": "Q7: Water flows through a pipe of cross-sectional area 0.05 m² at a velocity of 4 m/s. How many cubic meters of water pass in 10 seconds?",
            "options": ["A) 1.0 m³", "B) 2.0 m³", "C) 4.0 m³", "D) 8.0 m³"],
            "correct_option": "B) 2.0 m³",
            "explanation": "Flow rate Q = A * V = 0.05 * 4 = 0.2 m³/s. Total volume in 10s = 0.2 * 10 = 2.0 m³."
        },
        {
            "id": "civil_apt_8",
            "category": "Quantitative Aptitude (Earthwork Estimation)",
            "difficulty": "Hard",
            "question": "Q8: Using Trapezoidal rule, calculate volume of earthwork for 3 sections spaced 20 m apart with areas 10 m², 15 m², and 20 m².",
            "options": ["A) 400 m³", "B) 600 m³", "C) 800 m³", "D) 500 m³"],
            "correct_option": "B) 600 m³",
            "explanation": "V = d * [(A1 + A3)/2 + A2] = 20 * [(10 + 20)/2 + 15] = 20 * [15 + 15] = 20 * 30 = 600 m³."
        },
        {
            "id": "civil_apt_9",
            "category": "Logical Reasoning (Series)",
            "difficulty": "Easy",
            "question": "Q9: Find the missing number in rebar diameter series: 8, 10, 12, 16, 20, 25, 32, ?",
            "options": ["A) 36", "B) 40", "C) 45", "D) 50"],
            "correct_option": "B) 40",
            "explanation": "Standard IS reinforcement bar diameters in mm: 8, 10, 12, 16, 20, 25, 32, 40."
        },
        {
            "id": "civil_apt_10",
            "category": "Quantitative Aptitude (Cement Mix)",
            "difficulty": "Medium",
            "question": "Q10: In a M20 grade concrete mix of ratio 1:1.5:3 (Cement : Sand : Aggregate), what percentage of the total dry volume is cement?",
            "options": ["A) 18.18%", "B) 25.0%", "C) 33.33%", "D) 15.0%"],
            "correct_option": "A) 18.18%",
            "explanation": "Total parts = 1 + 1.5 + 3 = 5.5 parts. Cement fraction = 1 / 5.5 = 18.18%.",
            "model_answer": "Total mix ratio parts = 1 + 1.5 + 3 = 5.5\nCement percentage = (1 / 5.5) * 100 = 18.18%."
        },
        {
            "id": "civil_apt_11",
            "category": "Logical Reasoning (Contour Lines)",
            "difficulty": "Medium",
            "question": "Q11: Closely spaced concentric contour lines with higher values inside indicate what terrain feature?",
            "options": ["A) Pond", "B) Hill / Peak", "C) Valley", "D) Plain"],
            "correct_option": "B) Hill / Peak",
            "explanation": "Contours with higher elevation inside indicate a hill/peak."
        },
        {
            "id": "civil_apt_12",
            "category": "Data Interpretation (Stress Strain)",
            "difficulty": "Hard",
            "question": "Q12: A concrete cylinder of 150 mm diameter fails under an axial compressive load of 353.4 kN. What is the compressive strength?",
            "options": ["A) 15 MPa", "B) 20 MPa", "C) 25 MPa", "D) 30 MPa"],
            "correct_option": "B) 20 MPa",
            "explanation": "Area = pi * (75)^2 = 17,671.5 mm². Strength = 353,400 N / 17,671.5 mm² = 20 N/mm² = 20 MPa."
        },
        {
            "id": "civil_apt_13",
            "category": "Analytical Reasoning (Structural Determinacy)",
            "difficulty": "Hard",
            "question": "Q13: A pin-jointed plane truss has 5 joints (j=5) and 7 members (m=7). Is the truss statically determinate?",
            "options": ["A) Yes (m = 2j - 3)", "B) No, deficient", "C) No, indeterminate", "D) Unstable"],
            "correct_option": "A) Yes (m = 2j - 3)",
            "explanation": "2j - 3 = 2(5) - 3 = 7. Since m = 7 = 2j - 3, the truss is statically determinate."
        },
        {
            "id": "civil_apt_14",
            "category": "Quantitative Aptitude (Leveling RL)",
            "difficulty": "Easy",
            "question": "Q14: Benchmark Reduced Level (RL) is 100.00 m. Backsight reading is 1.45 m. What is the Height of Instrument (HI)?",
            "options": ["A) 98.55 m", "B) 101.45 m", "C) 100.00 m", "D) 102.90 m"],
            "correct_option": "B) 101.45 m",
            "explanation": "HI = RL + Backsight = 100.00 + 1.45 = 101.45 m."
        },
        {
            "id": "civil_apt_15",
            "category": "Verbal Ability (Site Terminology)",
            "difficulty": "Hard",
            "question": "Q15: Select the correct technical term for 'the ratio of settlement of a foundation to the applied pressure':",
            "options": ["A) Modulus of Subgrade Reaction", "B) Bulk Modulus", "C) Coefficient of Permeability", "D) Compression Index"],
            "correct_option": "A) Modulus of Subgrade Reaction",
            "explanation": "Modulus of subgrade reaction (k) is pressure per unit settlement (N/mm³ or kN/m³)."
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
