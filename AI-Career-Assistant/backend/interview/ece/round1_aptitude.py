# =====================================================================
# ECE - ROUND 1: APTITUDE (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_ece_aptitude(used_ids=None):
    used_set = set(used_ids or [])

    master_pool = [
        {
            "id": "ece_apt_1",
            "category": "Quantitative Aptitude (Frequency & Wavelength)",
            "difficulty": "Easy",
            "question": "Q1: An electromagnetic radio signal travels at 3 x 10^8 m/s with a frequency of 100 MHz. What is its wavelength in meters?",
            "options": ["A) 1.5 meters", "B) 3.0 meters", "C) 30 meters", "D) 300 meters"],
            "correct_option": "B) 3.0 meters",
            "explanation": "Wavelength lambda = c / f = (3 x 10^8) / (100 x 10^6) = 3.0 meters.",
            "model_answer": "Formula: Wavelength (lambda) = Speed of Light (c) / Frequency (f)\nlambda = (3 x 10^8 m/s) / (100 x 10^6 Hz) = 3.0 meters."
        },
        {
            "id": "ece_apt_2",
            "category": "Quantitative Aptitude (Ohm's Law & Resistors)",
            "difficulty": "Easy",
            "question": "Q2: Three 60-ohm resistors are connected in parallel across a 12V DC power supply. What is the total current drawn from the supply?",
            "options": ["A) 0.2 A", "B) 0.6 A", "C) 1.2 A", "D) 1.8 A"],
            "correct_option": "B) 0.6 A",
            "explanation": "Equivalent resistance R_eq = 60 / 3 = 20 ohms. Current I = V / R_eq = 12 / 20 = 0.6 A."
        },
        {
            "id": "ece_apt_3",
            "category": "Logical Reasoning (Binary & Hexadecimal)",
            "difficulty": "Medium",
            "question": "Q3: Convert the hexadecimal number 3F to decimal equivalent.",
            "options": ["A) 48", "B) 57", "C) 63", "D) 72"],
            "correct_option": "C) 63",
            "explanation": "3F in hex = (3 * 16) + (15 * 1) = 48 + 15 = 63."
        },
        {
            "id": "ece_apt_4",
            "category": "Analytical Reasoning (Sampling Rate)",
            "difficulty": "Medium",
            "question": "Q4: According to Nyquist Sampling Theorem, what is the minimum sampling rate required for an audio signal with maximum frequency component of 15 kHz?",
            "options": ["A) 15 kHz", "B) 20 kHz", "C) 30 kHz", "D) 45 kHz"],
            "correct_option": "C) 30 kHz",
            "explanation": "Nyquist rate f_s >= 2 * f_max = 2 * 15 kHz = 30 kHz."
        },
        {
            "id": "ece_apt_5",
            "category": "Verbal Ability (Technical Clarity)",
            "difficulty": "Easy",
            "question": "Q5: Select the grammatically correct sentence:",
            "options": [
                "A) The microcontroller execute the interrupt service routine.",
                "B) The microcontroller executes the interrupt service routine.",
                "C) The microcontroller executing the interrupt service routine.",
                "D) The microcontroller have executed the interrupt service routine."
            ],
            "correct_option": "B) The microcontroller executes the interrupt service routine.",
            "explanation": "Singular subject 'microcontroller' takes singular verb 'executes'."
        },
        {
            "id": "ece_apt_6",
            "category": "Quantitative Aptitude (Op-Amp Gain)",
            "difficulty": "Medium",
            "question": "Q6: An non-inverting operational amplifier circuit has Rf = 90 k-ohm and R1 = 10 k-ohm. What is the closed-loop voltage gain?",
            "options": ["A) 9", "B) 10", "C) 90", "D) 100"],
            "correct_option": "B) 10",
            "explanation": "Gain A_v = 1 + (Rf / R1) = 1 + (90 / 10) = 1 + 9 = 10.",
            "model_answer": "Formula: Non-inverting Op-Amp Gain A_v = 1 + (Rf / R1)\nA_v = 1 + (90 / 10) = 1 + 9 = 10."
        },
        {
            "id": "ece_apt_7",
            "category": "Logical Reasoning (Logic Gates)",
            "difficulty": "Medium",
            "question": "Q7: What is the output of a 2-input XOR gate when both inputs A and B are HIGH (1)?",
            "options": ["A) 0 (LOW)", "B) 1 (HIGH)", "C) High Impedance", "D) Undefined"],
            "correct_option": "A) 0 (LOW)",
            "explanation": "XOR gate output is HIGH only when inputs differ. When A=1 and B=1, output is 0."
        },
        {
            "id": "ece_apt_8",
            "category": "Quantitative Aptitude (Capacitor Energy)",
            "difficulty": "Hard",
            "question": "Q8: A 100 uF capacitor is charged to 20V. What is the stored electrical energy in Joules?",
            "options": ["A) 0.01 J", "B) 0.02 J", "C) 0.04 J", "D) 0.10 J"],
            "correct_option": "B) 0.02 J",
            "explanation": "Energy E = 0.5 * C * V^2 = 0.5 * (100 x 10^-6) * 400 = 0.5 * 0.04 = 0.02 Joules."
        },
        {
            "id": "ece_apt_9",
            "category": "Logical Reasoning (Series)",
            "difficulty": "Easy",
            "question": "Q9: Complete the clock frequency series: 1 MHz, 2 MHz, 4 MHz, 8 MHz, 16 MHz, ?",
            "options": ["A) 20 MHz", "B) 24 MHz", "C) 32 MHz", "D) 64 MHz"],
            "correct_option": "C) 32 MHz",
            "explanation": "Each frequency value doubles the preceding value (32 MHz)."
        },
        {
            "id": "ece_apt_10",
            "category": "Quantitative Aptitude (Signal-to-Noise Ratio)",
            "difficulty": "Medium",
            "question": "Q10: If a communications channel has a power SNR of 100, what is the SNR expressed in decibels (dB)?",
            "options": ["A) 10 dB", "B) 20 dB", "C) 30 dB", "D) 40 dB"],
            "correct_option": "B) 20 dB",
            "explanation": "SNR_dB = 10 * log10(SNR) = 10 * log10(100) = 10 * 2 = 20 dB.",
            "model_answer": "SNR (dB) = 10 * log10(Power Ratio)\nSNR = 10 * log10(100) = 10 * 2 = 20 dB."
        },
        {
            "id": "ece_apt_11",
            "category": "Logical Reasoning (De Morgan's Theorem)",
            "difficulty": "Medium",
            "question": "Q11: According to De Morgan's Theorem, the complement of a product (A . B)' is equal to what?",
            "options": ["A) A' . B'", "B) A' + B'", "C) (A + B)'", "D) A . B'"],
            "correct_option": "B) A' + B'",
            "explanation": "(A . B)' = A' + B' (NAND gate equals OR gate with inverted inputs)."
        },
        {
            "id": "ece_apt_12",
            "category": "Data Interpretation (ADC Resolution)",
            "difficulty": "Hard",
            "question": "Q12: An 8-bit Analog-to-Digital Converter (ADC) has a reference voltage of 5.12V. What is its step size (resolution)?",
            "options": ["A) 10 mV", "B) 20 mV", "C) 50 mV", "D) 100 mV"],
            "correct_option": "B) 20 mV",
            "explanation": "Number of levels = 2^8 = 256. Step size = Vref / 256 = 5.12 V / 256 = 0.020 V = 20 mV."
        },
        {
            "id": "ece_apt_13",
            "category": "Analytical Reasoning (BJT Current Gain)",
            "difficulty": "Hard",
            "question": "Q13: In a Bipolar Junction Transistor (BJT), if alpha = 0.98, what is the beta (common-emitter current gain)?",
            "options": ["A) 49", "B) 50", "C) 98", "D) 100"],
            "correct_option": "A) 49",
            "explanation": "beta = alpha / (1 - alpha) = 0.98 / (1 - 0.98) = 0.98 / 0.02 = 49."
        },
        {
            "id": "ece_apt_14",
            "category": "Quantitative Aptitude (Filter Cutoff)",
            "difficulty": "Easy",
            "question": "Q14: For an RC low-pass filter with R = 1 k-ohm and C = 0.1 uF, what is the cutoff frequency fc in Hz?",
            "options": ["A) 1591 Hz", "B) 3182 Hz", "C) 1000 Hz", "D) 500 Hz"],
            "correct_option": "A) 1591 Hz",
            "explanation": "fc = 1 / (2 * pi * R * C) = 1 / (2 * pi * 1000 * 1e-7) = 1 / (6.283 x 10^-4) = 1591.5 Hz."
        },
        {
            "id": "ece_apt_15",
            "category": "Verbal Ability (Electronics Terminology)",
            "difficulty": "Hard",
            "question": "Q15: Select the correct term for 'the unwanted emission of electromagnetic energy from an electronic device into another':",
            "options": ["A) Electromagnetic Interference (EMI)", "B) Thermal Noise", "C) Crosstalk", "D) Attenuation"],
            "correct_option": "A) Electromagnetic Interference (EMI)",
            "explanation": "EMI is unwanted disturbance generated by external electromagnetic radiation."
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
