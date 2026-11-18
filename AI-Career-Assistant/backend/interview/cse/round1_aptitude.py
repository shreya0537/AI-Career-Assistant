# =====================================================================
# CSE - ROUND 1: APTITUDE QUESTIONS (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_cse_aptitude(used_ids=None):
    """
    Generates a pool of EXACTLY 15 Aptitude Questions for CSE.
    Contains 3 questions with detailed model answers.
    """
    used_set = set(used_ids or [])

    master_pool = [
        {
            "id": "cse_apt_1",
            "category": "Quantitative Aptitude (Time & Work)",
            "difficulty": "Easy",
            "question": "Q1: If 12 software engineers can complete a web development project in 6 days, how many days will 8 engineers take to complete the exact same project at the same rate?",
            "options": ["A) 7 days", "B) 8 days", "C) 9 days", "D) 10 days"],
            "correct_option": "C) 9 days",
            "explanation": "Using inverse proportion: (12 engineers * 6 days) / 8 engineers = 9 days.",
            "model_answer": "Step 1: Calculate total engineer-days required = 12 engineers * 6 days = 72 engineer-days.\nStep 2: Days required for 8 engineers = 72 engineer-days / 8 engineers = 9 days."
        },
        {
            "id": "cse_apt_2",
            "category": "Quantitative Aptitude (Ratios & Data)",
            "difficulty": "Easy",
            "question": "Q2: The ratio of frontend to backend developers in a software firm is 4:5. If the number of frontend developers increases by 20%, what is the new ratio of developers?",
            "options": ["A) 24:25", "B) 5:6", "C) 6:5", "D) 12:25"],
            "correct_option": "A) 24:25",
            "explanation": "4 * 1.2 = 4.8. The ratio 4.8 : 5 simplifies to 48 : 50 = 24 : 25."
        },
        {
            "id": "cse_apt_3",
            "category": "Logical Reasoning (Binary & Series)",
            "difficulty": "Medium",
            "question": "Q3: Find the missing number in the computational series: 3, 6, 12, 24, 48, ?",
            "options": ["A) 60", "B) 72", "C) 96", "D) 108"],
            "correct_option": "C) 96",
            "explanation": "Each term doubles the previous number (multiplied by 2). 48 * 2 = 96."
        },
        {
            "id": "cse_apt_4",
            "category": "Analytical Reasoning (Pattern Encoding)",
            "difficulty": "Medium",
            "question": "Q4: In a logic algorithm pattern, COMPUTER is encoded as RFUVQNPC. Applying the exact same pattern, how is MEDICINE encoded?",
            "options": ["A) EOJDEJFM", "B) MFEJEDJO", "C) EOJDJEFM", "D) MFEDEJJO"],
            "correct_option": "A) EOJDEJFM",
            "explanation": "Reverse the letter sequence and shift each letter forward by +1."
        },
        {
            "id": "cse_apt_5",
            "category": "Verbal Ability (Technical Grammar)",
            "difficulty": "Easy",
            "question": "Q5: Select the grammatically correct sentence for technical documentation:",
            "options": [
                "A) Neither of the engineers have submitted the report on time.",
                "B) Neither of the engineers has submitted the report on time.",
                "C) Neither of the engineer have submitted the report on time.",
                "D) Neither of the engineer has submit the report on time."
            ],
            "correct_option": "B) Neither of the engineers has submitted the report on time.",
            "explanation": "'Neither' is a singular pronoun requiring the singular verb 'has'."
        },
        {
            "id": "cse_apt_6",
            "category": "Quantitative Aptitude (Speed & Distance)",
            "difficulty": "Medium",
            "question": "Q6: Data packets travel across a network node at 600 Mbps for 4 seconds and at 900 Mbps for 6 seconds. What is the average transmission speed?",
            "options": ["A) 750 Mbps", "B) 780 Mbps", "C) 800 Mbps", "D) 820 Mbps"],
            "correct_option": "B) 780 Mbps",
            "explanation": "Total data = (600*4) + (900*6) = 2400 + 5400 = 7800 Mb. Total time = 10s. Avg speed = 7800/10 = 780 Mbps.",
            "model_answer": "Formula: Average Speed = Total Data Transferred / Total Time Taken.\nTotal Data = (600 * 4) + (900 * 6) = 2400 + 5400 = 7800 Mb.\nTotal Time = 4 + 6 = 10 seconds.\nAverage Speed = 7800 / 10 = 780 Mbps."
        },
        {
            "id": "cse_apt_7",
            "category": "Logical Reasoning (Permutations)",
            "difficulty": "Medium",
            "question": "Q7: In how many ways can the letters of the word 'DATABASE' be arranged?",
            "options": ["A) 5040", "B) 6720", "C) 10080", "D) 40320"],
            "correct_option": "B) 6720",
            "explanation": "DATABASE has 8 letters with A repeated 3 times. Total permutations = 8! / 3! = 40320 / 6 = 6720."
        },
        {
            "id": "cse_apt_8",
            "category": "Quantitative Aptitude (Probability)",
            "difficulty": "Hard",
            "question": "Q8: A server cluster contains 5 healthy servers and 3 faulty servers. If 2 servers are picked at random, what is the probability that both are healthy?",
            "options": ["A) 5/14", "B) 10/28", "C) 15/28", "D) 3/7"],
            "correct_option": "A) 5/14",
            "explanation": "Probability = (5C2) / (8C2) = 10 / 28 = 5/14."
        },
        {
            "id": "cse_apt_9",
            "category": "Logical Reasoning (Coding Decoding)",
            "difficulty": "Easy",
            "question": "Q9: If ALGORITHM is coded as 1-12-7-15-18-9-20-8-13, how is SYSTEM coded?",
            "options": ["A) 19-25-19-20-5-13", "B) 18-24-18-19-4-12", "C) 19-24-19-20-5-13", "D) 20-26-20-21-6-14"],
            "correct_option": "A) 19-25-19-20-5-13",
            "explanation": "Each letter corresponds to its 1-indexed alphabetical position (S=19, Y=25, S=19, T=20, E=5, M=13)."
        },
        {
            "id": "cse_apt_10",
            "category": "Quantitative Aptitude (Percentages)",
            "difficulty": "Medium",
            "question": "Q10: An IT product's price was increased by 25% and subsequently discounted by 20%. What is the net percentage change in price?",
            "options": ["A) 5% increase", "B) 0% change", "C) 5% decrease", "D) 2% increase"],
            "correct_option": "B) 0% change",
            "explanation": "100 -> 125 -> 125 * 0.8 = 100. Net change = 0%.",
            "model_answer": "Let initial price = 100.\nAfter 25% increase = 100 * 1.25 = 125.\nAfter 20% discount = 125 * (1 - 0.20) = 125 * 0.80 = 100.\nNet change = 100 - 100 = 0% change."
        },
        {
            "id": "cse_apt_11",
            "category": "Logical Reasoning (Blood Relations)",
            "difficulty": "Medium",
            "question": "Q11: Pointing to a photograph of a tech founder, Rahul said 'His mother is the only daughter of my mother.' How is Rahul related to the founder?",
            "options": ["A) Father", "B) Uncle (Maternal)", "C) Brother", "D) Grandfather"],
            "correct_option": "B) Uncle (Maternal)",
            "explanation": "Only daughter of Rahul's mother is Rahul's sister. The founder is Rahul's sister's son, making Rahul his maternal uncle."
        },
        {
            "id": "cse_apt_12",
            "category": "Data Interpretation (Bar Graph & Charts)",
            "difficulty": "Hard",
            "question": "Q12: A software dev team completed 40 tasks in Week 1, 60 in Week 2, and 80 in Week 3. What is the percentage increase in task completion from Week 1 to Week 3?",
            "options": ["A) 50%", "B) 75%", "C) 100%", "D) 120%"],
            "correct_option": "C) 100%",
            "explanation": "Increase = ((80 - 40) / 40) * 100 = (40 / 40) * 100 = 100%."
        },
        {
            "id": "cse_apt_13",
            "category": "Analytical Reasoning (Syllogisms)",
            "difficulty": "Hard",
            "question": "Q13: Statements: All programmers are logical thinkers. Some logical thinkers are designers. Conclusion: (I) Some programmers are designers. (II) Some designers are logical thinkers.",
            "options": ["A) Only I follows", "B) Only II follows", "C) Both follow", "D) Neither follows"],
            "correct_option": "B) Only II follows",
            "explanation": "Since some logical thinkers are designers, it directly implies some designers are logical thinkers (II). Programmer-designer intersection is not guaranteed."
        },
        {
            "id": "cse_apt_14",
            "category": "Quantitative Aptitude (Averages)",
            "difficulty": "Easy",
            "question": "Q14: The average test score of 5 software QA testers is 84. If one tester with score 92 is excluded, what is the new average score of the remaining 4 testers?",
            "options": ["A) 80", "B) 81", "C) 82", "D) 83"],
            "correct_option": "C) 82",
            "explanation": "Total sum = 5 * 84 = 420. Remaining sum = 420 - 92 = 328. New average = 328 / 4 = 82."
        },
        {
            "id": "cse_apt_15",
            "category": "Verbal Reasoning (Critical Reasoning)",
            "difficulty": "Hard",
            "question": "Q15: Identify the assumption: 'Adopting Automated Testing will reduce software release delays by 40%.'",
            "options": [
                "A) Manual testing is completely useless.",
                "B) Release delays are currently caused at least in part by manual testing bottlenecks.",
                "C) Automated testing tools are expensive.",
                "D) All developers know how to write unit tests."
            ],
            "correct_option": "B) Release delays are currently caused at least in part by manual testing bottlenecks.",
            "explanation": "The claim assumes that testing bottlenecks contribute to delays that automation can eliminate."
        }
    ]

    # Filter unused questions if available
    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
