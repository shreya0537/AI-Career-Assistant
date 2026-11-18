# =====================================================================
# ECE - ROUND 4: PROJECT & RESUME TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_ece_project_questions(projects=None, skills=None, used_ids=None):
    projects = projects or []
    skills = skills or []
    used_set = set(used_ids or [])

    p1 = projects[0] if projects else "Embedded Systems / Electronics Project"
    p2 = projects[1] if len(projects) > 1 else (projects[0] if projects else "IoT / Signal Rig")
    s1 = skills[0] if skills else "Microcontrollers"
    s2 = skills[1] if len(skills) > 1 else "Embedded C"

    master_pool = [
        {
            "id": "ece_proj_1",
            "difficulty": "Easy",
            "category": f"Hardware Architecture ({p1})",
            "question": f"Walk me through the overall hardware schematic, microcontroller selection, and firmware architecture for your project '{p1}'. What was your individual role?",
            "acceptable_answers": [
                f"Detailed explanation of microcontroller pinouts, sensor interfacing, firmware architecture, and hardware testing for {p1}.",
                "Detailed summary of circuit diagram, microcontroller choice, protocol configuration, and firmware debugging."
            ],
            "model_answer": f"Model Answer Structure:\n1. Hardware Overview: Explain the core hardware system of '{p1}'.\n2. Component Selection: Justify choosing {s1} based on clock speed, flash memory, and peripheral availability (SPI/I2C/ADC).\n3. Firmware Design: Describe writing modular drivers in {s2}.\n4. Individual Contribution: Highlight specific PCB layout or code driver development."
        },
        {
            "id": "ece_proj_2",
            "difficulty": "Medium",
            "category": f"Firmware & Driver Development ({s1} & {s2})",
            "question": f"How did you write the firmware peripheral drivers using **{s1}** and **{s2}** for '{p1}'? Did you use bare-metal register programming or HAL libraries?",
            "acceptable_answers": [
                f"Wrote register-level drivers in {s2} for direct hardware control, managing timer interrupts and peripheral registers.",
                "Used vendor HAL API / bare-metal C for low latency register manipulation."
            ]
        },
        {
            "id": "ece_proj_3",
            "difficulty": "Medium",
            "category": "Communication Protocol Interfacing",
            "question": f"What communication bus protocol (UART, SPI, I2C, CAN) was used to connect sensors/modules in '{p1}'? How did you resolve data frame errors?",
            "acceptable_answers": [
                "Configured baud rate / clock polarity, added pull-up resistors for I2C, and verified signals with oscilloscope / logic analyzer.",
                "Handled packet framing, parity checks, and signal integrity."
            ]
        },
        {
            "id": "ece_proj_4",
            "difficulty": "Hard",
            "category": "Hardware Debugging & Signal Integrity",
            "question": f"Describe a difficult hardware bug or signal noise problem you encountered during '{p1}' (e.g. ground loops, power supply ripple, floating pins) and how you debugged it.",
            "acceptable_answers": [
                f"Identified power supply noise or floating input pins in {p1}, added decoupling capacitors / pull-down resistors, and verified with oscilloscope.",
                "Used digital oscilloscope / multimeter to trace voltage drops, ground noise, and signal glitches."
            ],
            "model_answer": "Model Answer Structure:\n1. Symptom: Erratic sensor readings and unexpected microcontroller resets in '{p1}'.\n2. Diagnosis: Connected oscilloscope probe to VCC rail, discovering 300mV AC ripple caused by inductive load switching.\n3. Hardware Fix: Added 0.1uF ceramic decoupling capacitor near MCU power pins and 100uF electrolytic bulk capacitor on main rail.\n4. Verification: Confirmed clean DC rail and stable firmware operation."
        },
        {
            "id": "ece_proj_5",
            "difficulty": "Hard",
            "category": f"Power Optimization & Battery Life ({p1})",
            "question": f"If project '{p1}' were deployed as a remote battery-powered IoT node, what low-power sleep modes and energy harvesting techniques would you implement?",
            "acceptable_answers": [
                f"Configure MCU deep sleep mode, disable unused peripheral clocks, use RTC wake-up interrupts, and optimize duty cycle for {p1}.",
                "Implement sleep modes, turn off sensor power rails via MOSFET switches, and optimize wake intervals."
            ]
        },
        {
            "id": "ece_proj_6",
            "difficulty": "Easy",
            "category": "PCB Design & Layout",
            "question": f"Did you design a printed circuit board (PCB) for '{p1}' using tools like EasyEDA, KiCad, or Altium? How did you handle trace width and grounding?",
            "acceptable_answers": [
                "Designed schematic and PCB layout in KiCad/Altium, routed signal and power traces, and included dedicated ground plane.",
                "Created custom PCB layout, ensuring proper trace widths for current capacity and ground plane fills."
            ]
        },
        {
            "id": "ece_proj_7",
            "difficulty": "Medium",
            "category": f"Secondary Project Scope ({p2})",
            "question": f"Explain the signal processing or wireless telemetry implementation in your secondary project '{p2}'.",
            "acceptable_answers": [
                f"Implemented DSP filtering, RF wireless transmission (LoRa, ESP-NOW, Bluetooth), or MATLAB processing for {p2}.",
                "Analyzed signal filtering or wireless data packet transmission."
            ]
        },
        {
            "id": "ece_proj_8",
            "difficulty": "Hard",
            "category": "RTOS Multithreading & Synchronization",
            "question": f"Did you use a Real-Time Operating System (FreeRTOS) for '{p1}'? How did you manage task priorities, semaphores, and queue messaging?",
            "acceptable_answers": [
                "Created FreeRTOS tasks for sensor reading, processing, and communication, using queues for inter-task data and mutexes for shared hardware resource locking.",
                "Used RTOS tasks, binary semaphores for ISR synchronization, and message queues."
            ],
            "model_answer": "Model Answer:\nFreeRTOS Integration:\n1. Tasks: Created sensor_task (Priority 2) and display_task (Priority 1).\n2. Synchronization: Used binary semaphore to wake processing task immediately from GPIO interrupt ISR.\n3. Resource Protection: Protected I2C bus access using Mutex to prevent simultaneous task access."
        },
        {
            "id": "ece_proj_9",
            "difficulty": "Hard",
            "category": "Sensor Calibration & Noise Filtering",
            "question": f"How did you calibrate physical sensors and filter out measurement noise (Kalman filter, Moving Average, Low-pass filter) in '{p1}'?",
            "acceptable_answers": [
                "Implemented exponential moving average or Digital FIR filter to smooth raw sensor ADC readings before processing.",
                "Calibrated sensor zero offset and applied software digital filter."
            ]
        },
        {
            "id": "ece_proj_10",
            "difficulty": "Easy",
            "category": "Component Sourcing & Datasheet Reading",
            "question": "How did you read component datasheets to determine voltage levels, pin configurations, and operating limits for your components?",
            "acceptable_answers": [
                "Consulted Electrical Characteristics and Pinout sections of datasheet to verify VCC limits, logic high/low thresholds, and timing diagrams.",
                "Checked datasheet absolute maximum ratings, pinouts, and recommended operating conditions."
            ]
        },
        {
            "id": "civil_proj_11",
            "difficulty": "Medium",
            "category": "Wireless Telemetry (Wi-Fi/BLE/LoRa)",
            "question": f"How was wireless connectivity established in '{p1}'? Explain payload formatting and reconnection handling.",
            "acceptable_answers": [
                "Used MQTT / HTTP POST over Wi-Fi / BLE advertising, formatting JSON data packets and implementing automatic reconnection loops.",
                "Configured wireless module for reliable data packet transmission and automatic retry logic."
            ]
        },
        {
            "id": "ece_proj_12",
            "difficulty": "Hard",
            "category": "FPGA Hardware Acceleration",
            "question": f"If you converted a software algorithm from '{p1}' into hardware on an FPGA (Verilog/VHDL), how would pipeline stages increase throughput?",
            "acceptable_answers": [
                "Pipelined execution breaks calculation into sequential registers, increasing clock frequency and output throughput.",
                "Implemented hardware pipelining in Verilog to achieve one result per clock cycle."
            ]
        },
        {
            "id": "ece_proj_13",
            "difficulty": "Easy",
            "category": "Enclosure & Thermal Management",
            "question": f"How did you house and cool the electronic components in '{p1}'?",
            "acceptable_answers": [
                "3D printed custom ABS/PLA enclosure with ventilation slots and heatsinks for power components.",
                "Housed components in protective enclosure with proper heat dissipation."
            ]
        },
        {
            "id": "ece_proj_14",
            "difficulty": "Medium",
            "category": "Firmware Over-The-Air (FOTA)",
            "question": f"How would you implement Firmware Over-The-Air (FOTA) updates for remote units running '{p1}'?",
            "acceptable_answers": [
                "Dual-bank flash memory partition: download verified firmware image to secondary bank, perform CRC check, and swap bootloader vector.",
                "Download encrypted binary image over Wi-Fi/Cellular, verify checksum, and flash via bootloader."
            ]
        },
        {
            "id": "ece_proj_15",
            "difficulty": "Hard",
            "category": "EMC / EMI Compliance",
            "question": f"What design steps would you take to pass Electromagnetic Compatibility (EMC) testing for mass production of '{p1}'?",
            "acceptable_answers": [
                "Add ferrite beads, solid ground planes, TVS diodes for ESD protection, shielded cables, and metal enclosure shielding.",
                "Implement ESD protection, EMI filtering, and ground plane shielding."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
