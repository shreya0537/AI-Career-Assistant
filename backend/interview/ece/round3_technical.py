# =====================================================================
# ECE - ROUND 3: CORE ECE TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_ece_technical(used_ids=None):
    used_set = set(used_ids or [])

    master_pool = [
        {
            "id": "ece_tech_1",
            "difficulty": "Easy",
            "category": "Embedded Systems (Microcontroller Peripherals)",
            "question": "Differentiate between UART, SPI, and I2C communication protocols in terms of wires, duplex mode, and speed.",
            "acceptable_answers": [
                "UART is asynchronous 2-wire point-to-point. SPI is synchronous 4-wire full duplex high speed. I2C is synchronous 2-wire multi-master half duplex.",
                "SPI uses 4 wires (MOSI, MISO, SCK, CS), I2C uses 2 wires (SDA, SCL), UART uses 2 wires (TX, RX)."
            ],
            "model_answer": "Model Answer:\n- UART: Asynchronous, 2 wires (TX, RX), Point-to-Point, Full Duplex, Moderate Speed.\n- SPI: Synchronous, 4 wires (MOSI, MISO, SCK, CS), Master-Slave, Full Duplex, High Speed (>10 Mbps).\n- I2C: Synchronous, 2 wires (SDA, SCL), Multi-Master/Multi-Slave, Half Duplex, Standard Speed (100k/400k/3.4M Hz)."
        },
        {
            "id": "ece_tech_2",
            "difficulty": "Medium",
            "category": "VLSI Design (CMOS Inverter)",
            "question": "Explain the structure and operation of a CMOS Inverter. Why does it consume negligible static power?",
            "acceptable_answers": [
                "CMOS inverter consists of PMOS pull-up and NMOS pull-down network. Static power is zero because one transistor is always OFF when input is stable.",
                "PMOS connected to VDD, NMOS connected to GND. When Vin=0, PMOS is ON, NMOS is OFF. When Vin=VDD, NMOS is ON, PMOS is OFF. No direct DC path."
            ]
        },
        {
            "id": "ece_tech_3",
            "difficulty": "Medium",
            "category": "Digital Electronics (Setup & Hold Time)",
            "question": "Define Setup Time and Hold Time in digital flip-flops. What happens if setup or hold time is violated?",
            "acceptable_answers": [
                "Setup time is minimum duration input data must be stable BEFORE active clock edge. Hold time is minimum duration data must remain stable AFTER clock edge. Violation causes Metastability.",
                "Metastability occurs when data changes during setup/hold window, causing unpredictable output voltage."
            ]
        },
        {
            "id": "ece_tech_4",
            "difficulty": "Hard",
            "category": "Signals & Systems (DFT vs FFT)",
            "question": "Explain the Discrete Fourier Transform (DFT) and how the Fast Fourier Transform (FFT) algorithm reduces computational complexity.",
            "acceptable_answers": [
                "DFT converts discrete time domain signal to frequency domain with O(N^2) complexity. FFT (Cooley-Tukey divide and conquer) reduces complexity to O(N log N).",
                "FFT reduces N^2 operations to N log2 N by exploiting symmetry and periodicity of twiddle factors."
            ],
            "model_answer": "Model Answer:\nDFT Equation: X[k] = sum_{n=0}^{N-1} x[n] * e^{-j 2 pi k n / N}\nComputational Complexity:\n- Standard DFT: Requires N^2 complex multiplications and additions -> O(N^2).\n- FFT Algorithm: Uses Cooley-Tukey Radix-2 divide-and-conquer strategy, exploiting twiddle factor periodicity (W_N^{k+N/2} = -W_N^k). Reduces complexity to O(N log2 N)."
        },
        {
            "id": "ece_tech_5",
            "difficulty": "Hard",
            "category": "VLSI (Setup & Hold Slack)",
            "question": "How are Setup Time Slack and Hold Time Slack calculated in static timing analysis (STA)? How do you fix a hold time violation?",
            "acceptable_answers": [
                "Setup Slack = Required Time - Arrival Time. Hold Slack = Arrival Time - Required Time. Fix hold violation by inserting buffer delays into the data path.",
                "Hold violation is independent of clock period. Fixed by adding delay buffers in the data path."
            ]
        },
        {
            "id": "ece_tech_6",
            "difficulty": "Easy",
            "category": "Analog Electronics (Op-Amp Ideal Characteristics)",
            "question": "List 5 ideal characteristics of an Operational Amplifier (Op-Amp).",
            "acceptable_answers": [
                "Infinite open-loop gain, infinite input impedance, zero output impedance, infinite bandwidth, zero offset voltage.",
                "A_v = infinity, R_in = infinity, R_out = 0, BW = infinity, CMRR = infinity."
            ]
        },
        {
            "id": "ece_tech_7",
            "difficulty": "Medium",
            "category": "Communication Systems (Modulation Techniques)",
            "question": "Compare Amplitude Modulation (AM), Frequency Modulation (FM), and Phase Modulation (PM). Why is FM less susceptible to noise?",
            "acceptable_answers": [
                "AM varies carrier amplitude; FM varies carrier frequency; PM varies carrier phase. FM is less susceptible to noise because environmental noise affects amplitude, which FM limiters clip off.",
                "Noise impacts amplitude. FM limiters strip amplitude noise without altering frequency information."
            ],
            "model_answer": "Model Answer:\n- AM: Carrier amplitude varies with message. Simple receiver, but highly vulnerable to atmospheric noise.\n- FM: Carrier frequency varies with message. Superior noise immunity because atmospheric noise is amplitude-based and can be eliminated using hard limiters.\n- PM: Carrier phase varies with message derivative. Closely related to FM."
        },
        {
            "id": "ece_tech_8",
            "difficulty": "Medium",
            "category": "Microprocessors & ARM (Architecture)",
            "question": "Compare Von Neumann and Harvard Memory Architectures. Which architecture is commonly used in modern ARM microcontrollers?",
            "acceptable_answers": [
                "Von Neumann shares a single bus for code and data. Harvard uses separate instruction and data buses for simultaneous fetch. ARM Cortex uses Harvard architecture.",
                "Harvard has independent instruction and data buses, allowing simultaneous instruction fetch and data read."
            ]
        },
        {
            "id": "ece_tech_9",
            "difficulty": "Hard",
            "category": "Communication Systems (OFDM & 5G)",
            "question": "Explain Orthogonal Frequency Division Multiplexing (OFDM) and Cyclic Prefix in modern wireless communications (4G/5G/Wi-Fi).",
            "acceptable_answers": [
                "OFDM splits high-speed data stream into orthogonal subcarriers. Cyclic Prefix appends guard interval to eliminate Inter-Symbol Interference (ISI).",
                "OFDM uses closely spaced orthogonal sub-channels. Cyclic prefix converts dispersive channel convolution into cyclic convolution, eliminating ISI."
            ]
        },
        {
            "id": "ece_tech_10",
            "difficulty": "Easy",
            "category": "Digital Electronics (Combinational vs Sequential)",
            "question": "What is the key difference between Combinational and Sequential digital circuits?",
            "acceptable_answers": [
                "Combinational circuit outputs depend ONLY on present inputs (e.g. MUX, Adder). Sequential circuit outputs depend on present inputs AND past history (memory element, e.g. Flip-Flop).",
                "Sequential circuits contain memory elements (latches/flip-flops) and clock, combinational circuits have no memory."
            ]
        },
        {
            "id": "ece_tech_11",
            "difficulty": "Medium",
            "category": "Embedded Systems (Interrupt Service Routine)",
            "question": "What is an Interrupt Service Routine (ISR)? What restrictions apply when writing code inside an ISR?",
            "acceptable_answers": [
                "ISR is a hardware interrupt handler function. Restrictions: Keep ISR extremely short, avoid blocking delays, don't use printf/malloc, declare shared variables volatile.",
                "ISR should execute fast, avoid floating-point math, avoid dynamic allocation, and declare shared flags volatile."
            ]
        },
        {
            "id": "ece_tech_12",
            "difficulty": "Hard",
            "category": "Analog Electronics (Feedback Topologies)",
            "question": "Explain Voltage-Series, Voltage-Shunt, Current-Series, and Current-Shunt negative feedback topologies.",
            "acceptable_answers": [
                "Voltage series increases R_in, decreases R_out (Voltage Amplifier). Current series increases R_in, increases R_out (Transconductance Amplifier). Voltage shunt decreases R_in, decreases R_out. Current shunt decreases R_in, increases R_out.",
                "Negative feedback stabilizes gain, increases bandwidth, and reduces distortion."
            ]
        },
        {
            "id": "ece_tech_13",
            "difficulty": "Easy",
            "category": "Antennas & Electromagnetic Waves",
            "question": "Define Antenna Gain, Radiation Pattern, and Half-Power Beamwidth (HPBW).",
            "acceptable_answers": [
                "Radiation pattern shows directional radiation intensity. Antenna gain measures power density in peak direction relative to isotropic radiator. HPBW is angle between 3dB points.",
                "HPBW is angular width where radiated power drops to half (3dB) of maximum value."
            ]
        },
        {
            "id": "ece_tech_14",
            "difficulty": "Medium",
            "category": "Control Systems (Stability & Bode Plot)",
            "question": "Explain Gain Margin (GM) and Phase Margin (PM) on a Bode Plot. What condition guarantees closed-loop system stability?",
            "acceptable_answers": [
                "System is stable if both Gain Margin and Phase Margin are positive (GM > 0 dB, PM > 0 degrees).",
                "Gain margin is DB value at phase crossover (-180°). Phase margin is angle above -180° at gain crossover (0 dB)."
            ]
        },
        {
            "id": "ece_tech_15",
            "difficulty": "Hard",
            "category": "VLSI (Low Power Design)",
            "question": "What techniques are used in modern VLSI layout to reduce dynamic power (CV^2f) and static leakage power?",
            "acceptable_answers": [
                "Dynamic power reduced by Clock Gating, Voltage Scaling (DVFS), and lowering capacitance. Static power reduced by Power Gating, Multi-Vt transistors, and sleep modes.",
                "Clock gating for dynamic power; Power gating and high-Vt transistors for leakage reduction."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
