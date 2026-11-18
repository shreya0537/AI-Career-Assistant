# =====================================================================
# ECE - ROUND 2: PROBLEM SOLVING & CODING (DEPENDENT ON MENTIONED LANGUAGES)
# =====================================================================
from backend.interview.question_pool import extract_mentioned_programming_languages

def get_ece_coding(skills=None, projects=None, used_ids=None, resume_text=""):
    """
    Generates Round 2 questions for ECE:
    - IF programming languages are mentioned (e.g. C, C++, Embedded C, Python, Verilog, etc.):
      gives CODING questions tailored to those programming languages.
    - OTHERWISE (if no programming languages are mentioned):
      gives non-coding Core Electronics Engineering Problem Solving questions.
    """
    skills = skills or []
    projects = projects or []
    used_set = set(used_ids or [])

    langs = extract_mentioned_programming_languages(skills=skills, resume_text=resume_text)
    has_programming = bool(langs)

    proj = projects[0] if projects else "Electronic System"
    sk1 = skills[0] if skills else "Electronics"

    if has_programming:
        # CODING QUESTIONS FOR ECE BASED ON MENTIONED LANGUAGES
        main_lang = langs[0]
        langs_str = ", ".join(langs)

        master_pool = [
            {
                "id": "ece_coding_1",
                "difficulty": "Easy",
                "category": f"Bitwise Register Masking ({main_lang})",
                "question": f"Write an executable {main_lang} function to SET bit 3, CLEAR bit 5, and TOGGLE bit 1 of an 8-bit register byte. (Mentioned Language: {main_lang})",
                "expected_input_output": "Input: initial_byte = 0b00100000 (0x20)\nOutput: modified_byte = 0b00001010 (0x0A)",
                "solution_code": f"""# Solution in {main_lang}
def modify_register(reg_byte):
    reg_byte |= (1 << 3)   # Set bit 3
    reg_byte &= ~(1 << 5)  # Clear bit 5
    reg_byte ^= (1 << 1)   # Toggle bit 1
    return reg_byte

print(hex(modify_register(0x20)))""",
                "time_complexity": "O(1) - Bitwise operations",
                "space_complexity": "O(1) - Primitive byte return",
                "model_answer": f"Model Code in {main_lang}:\n\nUse |= (1<<3) to set bit 3, &= ~(1<<5) to clear bit 5, and ^= (1<<1) to toggle bit 1.",
                "acceptable_answers": [
                    "Set bit 3 using |= (1<<3), Clear bit 5 using &= ~(1<<5), Toggle bit 1 using ^= (1<<1).",
                    "Bitwise OR for set, bitwise AND with inverted mask for clear, bitwise XOR for toggle."
                ]
            },
            {
                "id": "ece_coding_2",
                "difficulty": "Medium",
                "category": f"ADC Sensor Conversion ({main_lang})",
                "question": f"Write a {main_lang} script for '{proj}' to convert a 10-bit ADC raw integer value (0-1023) into Voltage (V) and Temperature (°C) for an LM35 sensor (10mV/°C, 3.3V Vref).",
                "expected_input_output": "Input: raw_adc = 512\nOutput: Voltage = 1.652 V, Temperature = 165.2 °C",
                "solution_code": f"""# Solution in {main_lang}
def adc_to_temp(raw, vref=3.3):
    voltage = (raw / 1024.0) * vref
    temp = voltage / 0.010
    return round(voltage, 3), round(temp, 1)

print(adc_to_temp(512))""",
                "time_complexity": "O(1) - Scaling arithmetic",
                "space_complexity": "O(1) - Scalar values",
                "acceptable_answers": [
                    "Voltage = (adc_raw / 1024) * 3.3, Temp = Voltage / 0.01.",
                    "Scale 10-bit ADC reading to reference voltage 3.3V and divide by 10mV per degree C."
                ]
            },
            {
                "id": "ece_coding_3",
                "difficulty": "Hard",
                "category": f"PWM Timer Counter Setup ({main_lang})",
                "question": f"Write a {main_lang} function to calculate Timer Reload value and OCR register value for generating a 1 kHz PWM signal with 40% duty cycle (16 MHz clock, prescaler = 64).",
                "expected_input_output": "Input: F_cpu = 16MHz, F_pwm = 1kHz, Prescaler = 64, Duty = 40%\nOutput: TOP = 249, OCR Match = 100",
                "solution_code": f"""# Solution in {main_lang}
def pwm_timer(f_cpu=16000000, f_pwm=1000, prescaler=64, duty=40):
    top = int((f_cpu / (prescaler * f_pwm)) - 1)
    ocr = int((top + 1) * (duty / 100.0))
    return top, ocr

print(pwm_timer())""",
                "time_complexity": "O(1) - Hardware formula math",
                "space_complexity": "O(1) - Register values",
                "model_answer": f"Model Solution in {main_lang}:\n\nTOP = (F_cpu / (prescaler * F_pwm)) - 1, OCR = (TOP + 1) * duty_pct.",
                "acceptable_answers": [
                    "TOP = (F_cpu / (prescaler * F_pwm)) - 1, OCR = TOP * duty_cycle.",
                    "Calculate timer ARR/TOP reload value and OCR compare match value."
                ]
            },
            {
                "id": "ece_coding_4",
                "difficulty": "Easy",
                "category": f"UART Packet XOR Checksum ({main_lang})",
                "question": f"Write an executable {main_lang} function to compute an 8-bit XOR checksum for a byte array payload.",
                "expected_input_output": "Input: payload = [0xAA, 0x05, 0x12, 0x34]\nOutput: Checksum = 0x87",
                "solution_code": f"""# Solution in {main_lang}
def calc_checksum(data):
    chk = 0
    for b in data: chk ^= b
    return chk

print(hex(calc_checksum([0xAA, 0x05, 0x12, 0x34])))""",
                "time_complexity": "O(N) - Loop over bytes",
                "space_complexity": "O(1) - XOR accumulator",
                "acceptable_answers": [
                    "XOR all bytes sequentially to generate 8-bit checksum.",
                    "Iterate packet payload accumulating bitwise XOR."
                ]
            },
            {
                "id": "ece_coding_5",
                "difficulty": "Medium",
                "category": f"I2C Bus Address Scanner ({main_lang})",
                "question": f"Write a {main_lang} script simulating an I2C bus scanner that tests addresses 0x08 to 0x77 and returns active device hex addresses.",
                "expected_input_output": "Input: Active devices [0x27, 0x68]\nOutput: Detected: ['0x27', '0x68']",
                "solution_code": f"""# Solution in {main_lang}
def scan_i2c(active=[0x27, 0x68]):
    return [hex(a) for a in range(0x08, 0x78) if a in active]

print(scan_i2c())""",
                "time_complexity": "O(1) - Fixed 112 address scan",
                "space_complexity": "O(K) - Output list",
                "acceptable_answers": [
                    "Iterate addresses 0x08 to 0x77, send START condition, check ACK response.",
                    "Loop through 7-bit I2C address space detecting ACKs."
                ]
            },
            {
                "id": "ece_coding_6",
                "difficulty": "Hard",
                "category": f"Verilog / HDL Logic Synthesis ({main_lang})",
                "question": f"Write code in {main_lang} or Verilog HDL for a 4-bit synchronous up-counter with active-low asynchronous reset.",
                "expected_input_output": "Input: clk, rst_n\nOutput: [3:0] q counter value",
                "solution_code": f"""# Verilog / HDL Equivalent in {main_lang}
class Counter4Bit:
    def __init__(self): self.q = 0
    def clock(self, rst_n):
        if not rst_n: self.q = 0
        else: self.q = (self.q + 1) & 0x0F
        return self.q

c = Counter4Bit()
print([c.clock(1) for _ in range(4)])""",
                "time_complexity": "O(1) - Register increment",
                "space_complexity": "O(1) - 4-bit flip-flop",
                "acceptable_answers": [
                    "Verilog module with always @(posedge clk or negedge rst_n) block.",
                    "Asynchronous reset if (!rst_n) q<=0 else q<=q+1."
                ]
            },
            {
                "id": "ece_coding_7",
                "difficulty": "Easy",
                "category": f"GPIO Digital Pin Control ({main_lang})",
                "question": f"Write a {main_lang} function to configure GPIO Pin 4 as output, set it HIGH for 500ms, then set it LOW.",
                "expected_input_output": "Input: Pin 4 toggle request\nOutput: Pin 4 set HIGH -> sleep(0.5) -> set LOW",
                "solution_code": f"""# Solution in {main_lang}
import time

def toggle_pin(pin=4, delay=0.5):
    # Simulated GPIO output
    pin_state = 1 # HIGH
    time.sleep(delay)
    pin_state = 0 # LOW
    return pin_state

print(toggle_pin())""",
                "time_complexity": "O(1) - Hardware register set",
                "space_complexity": "O(1) - Constant",
                "acceptable_answers": [
                    "Set pin direction to OUTPUT, write HIGH (1), delay 500ms, write LOW (0).",
                    "Configure GPIO direction register and write data output register."
                ]
            },
            {
                "id": "ece_coding_8",
                "difficulty": "Medium",
                "category": f"FIR Digital Filter Implementation ({main_lang})",
                "question": f"Write a 3-tap Moving Average Low-Pass FIR filter function in {main_lang}: y[n] = (x[n] + x[n-1] + x[n-2]) / 3.",
                "expected_input_output": "Input: signal = [10, 20, 30, 40, 50]\nOutput: Filtered = [3.33, 10.0, 20.0, 30.0, 40.0]",
                "solution_code": f"""# Solution in {main_lang}
def moving_average_fir(signal):
    filtered = []
    for i in range(len(signal)):
        x0 = signal[i]
        x1 = signal[i-1] if i >= 1 else 0
        x2 = signal[i-2] if i >= 2 else 0
        filtered.append(round((x0 + x1 + x2) / 3.0, 2))
    return filtered

print(moving_average_fir([10, 20, 30, 40, 50]))""",
                "time_complexity": "O(N) - Linear convolution pass",
                "space_complexity": "O(N) - Output filtered array",
                "acceptable_answers": [
                    "y[n] = (x[n] + x[n-1] + x[n-2]) / 3.",
                    "3-point moving average FIR convolution averaging current and two previous samples."
                ]
            },
            {
                "id": "ece_coding_9",
                "difficulty": "Hard",
                "category": f"SPI Protocol Frame Transmitter ({main_lang})",
                "question": f"Write a {main_lang} function simulating SPI full-duplex transmission (driving MOSI on SCLK edge while sampling MISO).",
                "expected_input_output": "Input: tx_byte = 0x55\nOutput: rx_byte = 0xAA (Simulated full-duplex response)",
                "solution_code": f"""# Solution in {main_lang}
def spi_transfer_byte(tx_byte):
    rx_byte = 0
    for i in range(7, -1, -1):
        mosi = (tx_byte >> i) & 1
        miso = 1 if i % 2 == 0 else 0 # Simulated MISO read
        rx_byte = (rx_byte << 1) | miso
    return hex(rx_byte)

print(spi_transfer_byte(0x55))""",
                "time_complexity": "O(1) - 8 clock cycle bit shift",
                "space_complexity": "O(1) - Bit registers",
                "acceptable_answers": [
                    "Loop 8 bits: shift MSB onto MOSI, pulse SCLK, read MISO bit into rx_byte.",
                    "Full-duplex SPI bit-banging shifting MSB to LSB over 8 SCLK clock cycles."
                ]
            },
            {
                "id": "ece_coding_10",
                "difficulty": "Easy",
                "category": f"Sampling Rate & Nyquist Rate Calculation ({main_lang})",
                "question": f"Write a {main_lang} function to calculate minimum Nyquist Sampling Frequency and total samples for a signal with maximum frequency f_max over time T.",
                "expected_input_output": "Input: f_max = 5000 Hz, T = 2 seconds\nOutput: Nyquist Rate = 10000 Hz, Minimum Samples = 20000",
                "solution_code": f"""# Solution in {main_lang}
def nyquist_sampling(f_max, duration_sec):
    nyquist_rate = 2 * f_max
    total_samples = int(nyquist_rate * duration_sec)
    return nyquist_rate, total_samples

print(nyquist_sampling(5000, 2))""",
                "time_complexity": "O(1) - Math formula",
                "space_complexity": "O(1) - Primitive scalars",
                "acceptable_answers": [
                    "Nyquist rate Fs >= 2 * Fmax; total samples = Fs * duration.",
                    "Multiply maximum signal frequency by 2 for minimum sampling frequency."
                ]
            },
            {
                "id": "ece_coding_11",
                "difficulty": "Medium",
                "category": f"Ring Buffer for Serial Data ({main_lang})",
                "question": f"Write a fixed-size Circular Ring Buffer class in {main_lang} with push() and pop() methods for UART RX interrupts.",
                "expected_input_output": "Input: Buffer size = 4, Push: [10, 20, 30]\nOutput: Pop: 10, Remaining: [20, 30]",
                "solution_code": f"""# Solution in {main_lang}
class RingBuffer:
    def __init__(self, capacity=4):
        self.cap = capacity
        self.buf = [None] * capacity
        self.head = self.tail = self.size = 0

    def push(self, val):
        if self.size < self.cap:
            self.buf[self.head] = val
            self.head = (self.head + 1) % self.cap
            self.size += 1

    def pop(self):
        if self.size > 0:
            val = self.buf[self.tail]
            self.tail = (self.tail + 1) % self.cap
            self.size -= 1
            return val
        return None

rb = RingBuffer(4)
rb.push(10); rb.push(20)
print(rb.pop())""",
                "time_complexity": "O(1) - Push/pop enqueue dequeue",
                "space_complexity": "O(K) - Fixed capacity array",
                "acceptable_answers": [
                    "Maintain head, tail, size variables with modulo capacity wrapping.",
                    "Circular FIFO buffer using modulo arithmetic for head and tail pointer increments."
                ]
            },
            {
                "id": "ece_coding_12",
                "difficulty": "Hard",
                "category": f"State Machine Logic ({main_lang})",
                "question": f"Write a finite state machine (FSM) in {main_lang} for a traffic light controller (RED -> GREEN -> YELLOW -> RED).",
                "expected_input_output": "Input: Initial state = RED, 3 ticks\nOutput: Transitions: RED -> GREEN -> YELLOW -> RED",
                "solution_code": f"""# Solution in {main_lang}
def fsm_traffic_light(initial="RED", ticks=3):
    transitions = {{"RED": "GREEN", "GREEN": "YELLOW", "YELLOW": "RED"}}
    curr = initial
    history = [curr]
    for _ in range(ticks):
        curr = transitions[curr]
        history.append(curr)
    return " -> ".join(history)

print(fsm_traffic_light())""",
                "time_complexity": "O(T) - T state transitions",
                "space_complexity": "O(T) - History log",
                "acceptable_answers": [
                    "State dictionary or switch statement mapping current state to next state on clock pulse.",
                    "FSM state transition table implementation."
                ]
            },
            {
                "id": "ece_coding_13",
                "difficulty": "Easy",
                "category": f"Resistor Color Code Calculation ({main_lang})",
                "question": f"Write a {main_lang} function to compute 4-band resistor resistance value given color bands: band1, band2, multiplier.",
                "expected_input_output": "Input: 'Brown' (1), 'Black' (0), 'Red' (10^2)\nOutput: Resistance = 1000 Ohms (1 kOhm)",
                "solution_code": f"""# Solution in {main_lang}
COLOR_MAP = {{'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6}}

def decode_resistor(b1, b2, mult):
    d1 = COLOR_MAP[b1.lower()]
    d2 = COLOR_MAP[b2.lower()]
    m = 10 ** COLOR_MAP[mult.lower()]
    return (d1 * 10 + d2) * m

print(f"{{decode_resistor('brown', 'black', 'red')}} Ohms")""",
                "time_complexity": "O(1) - Color map lookup",
                "space_complexity": "O(1) - Constant memory",
                "acceptable_answers": [
                    "Resistance = (Digit1 * 10 + Digit2) * 10^Multiplier.",
                    "Map color names to digits 0-9 and compute exponential multiplier value."
                ]
            },
            {
                "id": "ece_coding_14",
                "difficulty": "Medium",
                "category": f"PWM Duty Cycle Signal Analysis ({main_lang})",
                "question": f"Write a {main_lang} function to compute Average Voltage and Duty Cycle % from a digital signal sample array of 1s and 0s (Vhigh = 3.3V).",
                "expected_input_output": "Input: signal = [1, 1, 0, 0, 1, 0, 0, 0]\nOutput: Duty Cycle = 37.5%, V_avg = 1.238 V",
                "solution_code": f"""# Solution in {main_lang}
def pwm_analysis(samples, vhigh=3.3):
    duty = sum(samples) / float(len(samples))
    v_avg = duty * vhigh
    return round(duty * 100, 1), round(v_avg, 3)

print(pwm_analysis([1, 1, 0, 0, 1, 0, 0, 0]))""",
                "time_complexity": "O(N) - Linear sample sum",
                "space_complexity": "O(1) - Scalar values",
                "acceptable_answers": [
                    "Duty cycle = (count of 1s / total samples) * 100, V_avg = Duty * Vhigh.",
                    "Calculate fraction of high logic state samples and multiply by high voltage."
                ]
            },
            {
                "id": "ece_coding_15",
                "difficulty": "Hard",
                "category": f"CRC-8 Error Detection Code ({main_lang})",
                "question": f"Write a {main_lang} function implementing CRC-8 error detection algorithm using polynomial 0x07.",
                "expected_input_output": "Input: data = [0x31, 0x32, 0x33]\nOutput: CRC-8 Checksum byte",
                "solution_code": f"""# Solution in {main_lang}
def crc8(data, poly=0x07):
    crc = 0x00
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ poly) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
    return hex(crc)

print(crc8([0x31, 0x32, 0x33]))""",
                "time_complexity": "O(N) - 8 bit iterations per byte",
                "space_complexity": "O(1) - CRC register",
                "acceptable_answers": [
                    "Iterate bytes, XOR with CRC register, shift left 8 times applying polynomial 0x07 on MSB set.",
                    "Bit-wise CRC-8 calculation loop using generator polynomial."
                ]
            }
        ]

    else:
        # NON-CODING CORE ELECTRONICS ENGINEERING PROBLEM SOLVING
        master_pool = [
            {
                "id": "ece_noncode_1",
                "difficulty": "Easy",
                "category": "Op-Amp Circuit Gain Analysis",
                "question": "Calculate the closed-loop voltage gain Av of an inverting amplifier circuit with input resistor Rin = 10 kΩ and feedback resistor Rf = 100 kΩ. Provide step-by-step formula and numerical answer.",
                "expected_input_output": "Input: Rin = 10 kΩ, Rf = 100 kΩ\nOutput: Voltage Gain Av = -10 (or 10 in magnitude)",
                "solution_code": "",
                "time_complexity": "N/A - Engineering Math",
                "space_complexity": "N/A - Engineering Math",
                "model_answer": "Model Solution & Calculation Steps:\n\nFor an inverting op-amp configuration:\nGain Av = - (Rf / Rin)\nAv = - (100 kΩ / 10 kΩ) = -10.\nThe negative sign indicates a 180° phase shift.",
                "acceptable_answers": [
                    "Av = - (Rf / Rin) = -10.",
                    "Inverting amplifier gain formula Av = -Rf/Rin gives gain of -10."
                ]
            },
            {
                "id": "ece_noncode_2",
                "difficulty": "Medium",
                "category": "RLC Circuit Resonant Frequency",
                "question": "Calculate the resonant frequency fr of a series RLC circuit with L = 10 mH, C = 0.1 µF, and R = 50 Ω. Show the resonant frequency formula and final value in kHz.",
                "expected_input_output": "Input: L = 10 mH, C = 0.1 µF\nOutput: Resonant Frequency fr = 5.03 kHz",
                "solution_code": "",
                "time_complexity": "N/A - Engineering Math",
                "space_complexity": "N/A - Engineering Math",
                "acceptable_answers": [
                    "fr = 1 / (2 * pi * sqrt(L * C)) = 5.03 kHz.",
                    "Calculate resonant frequency using 1/(2*pi*sqrt(L*C)) yielding approximately 5.03 kHz."
                ]
            },
            {
                "id": "ece_noncode_3",
                "difficulty": "Hard",
                "category": "BJT Transistor Q-Point Biasing",
                "question": "For a BJT fixed bias circuit with VCC = 12V, RB = 240 kΩ, RC = 2.2 kΩ, and beta (β) = 100, calculate Base Current IB, Collector Current IC, and Collector-Emitter Voltage VCE.",
                "expected_input_output": "Input: VCC = 12V, RB = 240kΩ, RC = 2.2kΩ, β = 100\nOutput: IB = 47.08 µA, IC = 4.71 mA, VCE = 1.64 V",
                "solution_code": "",
                "time_complexity": "N/A - Transistor DC Biasing Math",
                "space_complexity": "N/A - DC Analysis",
                "model_answer": "Model Solution & Calculation Steps:\n\n1. IB = (VCC - VBE) / RB = (12 - 0.7) / 240k = 47.08 µA\n2. IC = β * IB = 100 * 47.08µA = 4.71 mA\n3. VCE = VCC - (IC * RC) = 12 - (4.71mA * 2.2k) = 1.64 V.",
                "acceptable_answers": [
                    "IB = (VCC - 0.7)/RB = 47µA, IC = β*IB = 4.71mA, VCE = VCC - IC*RC = 1.64V.",
                    "Calculate IB using base-emitter 0.7V drop, IC as beta times IB, and VCE via KVL across collector resistor."
                ]
            },
            {
                "id": "ece_noncode_4",
                "difficulty": "Easy",
                "category": "Boolean Logic Gate Minimization",
                "question": "Simplify the Boolean expression F = A·B + A·B' + A'·B using Boolean algebra theorems. Show the step-by-step reduction.",
                "expected_input_output": "Input: F = A·B + A·B' + A'·B\nOutput: Simplified F = A + B",
                "solution_code": "",
                "time_complexity": "N/A - Boolean Minimization",
                "space_complexity": "N/A - Logic Design",
                "acceptable_answers": [
                    "F = A(B + B') + A'B = A(1) + A'B = A + B.",
                    "Factor A to get A(B+B') + A'B = A + A'B, then apply distributive law to get A + B."
                ]
            },
            {
                "id": "ece_noncode_5",
                "difficulty": "Medium",
                "category": "Amplitude Modulation (AM) Index",
                "question": "An AM signal has a carrier amplitude Vc = 10V and peak modulating signal amplitude Vm = 6V. Calculate the Modulation Index m and Total Transmitted Power Pt if carrier power Pc = 50W.",
                "expected_input_output": "Input: Vc = 10V, Vm = 6V, Pc = 50W\nOutput: Modulation Index m = 0.6 (60%), Total Power Pt = 59.0 W",
                "solution_code": "",
                "time_complexity": "N/A - Communication Systems",
                "space_complexity": "N/A - Communication Math",
                "acceptable_answers": [
                    "m = Vm / Vc = 0.6; Pt = Pc * (1 + (m^2 / 2)) = 50 * (1 + 0.18) = 59 W.",
                    "Modulation index is Vm/Vc = 0.6. Total power Pt = Pc(1 + m^2/2) = 59W."
                ]
            },
            {
                "id": "ece_noncode_6",
                "difficulty": "Hard",
                "category": "Quarter-Wave Antenna Wavelength & Length",
                "question": "Calculate the physical length of a quarter-wave (λ/4) dipole antenna designed for an operating frequency f = 300 MHz in free space (speed of light c = 3 x 10^8 m/s).",
                "expected_input_output": "Input: f = 300 MHz, c = 3 x 10^8 m/s\nOutput: Wavelength λ = 1.0 m, Antenna Length = 0.25 m (25 cm)",
                "solution_code": "",
                "time_complexity": "N/A - Antenna Theory",
                "space_complexity": "N/A - Electromagnetics",
                "acceptable_answers": [
                    "λ = c / f = (3e8) / (300e6) = 1.0 m. Length L = λ / 4 = 0.25 m = 25 cm.",
                    "Wavelength is 1 meter. Quarter wavelength length is 0.25 meters."
                ]
            },
            {
                "id": "ece_noncode_7",
                "difficulty": "Easy",
                "category": "ADC Resolution & Quantization Step",
                "question": "Calculate the quantization step size (resolution voltage) of an 8-bit ADC operating with a full-scale reference voltage Vref = 5.0 V.",
                "expected_input_output": "Input: 8-bit resolution, Vref = 5.0 V\nOutput: Step Size = 5.0 / 256 = 19.53 mV",
                "solution_code": "",
                "time_complexity": "N/A - Signal Processing",
                "space_complexity": "N/A - Instrumentation",
                "acceptable_answers": [
                    "Step size = Vref / 2^N = 5.0 / 256 = 0.01953 V = 19.53 mV.",
                    "Divide 5V by 2^8 (256 levels) to obtain 19.53 mV quantization step size."
                ]
            },
            {
                "id": "ece_noncode_8",
                "difficulty": "Medium",
                "category": "4-bit Synchronous Counter Flip-Flops",
                "question": "Explain the design principles of a 4-bit synchronous binary up-counter using JK flip-flops. State the excitation inputs required for each flip-flop.",
                "expected_input_output": "Input: 4-bit Counter logic\nOutput: J0=K0=1, J1=K1=Q0, J2=K2=Q0·Q1, J3=K3=Q0·Q1·Q2",
                "solution_code": "",
                "time_complexity": "N/A - Digital Design",
                "space_complexity": "N/A - Logic Gates",
                "acceptable_answers": [
                    "J0=K0=1, J1=K1=Q0, J2=K2=Q0*Q1, J3=K3=Q0*Q1*Q2.",
                    "Each JK flip-flop toggles when all lower order output bits are high (AND gate combination)."
                ]
            },
            {
                "id": "ece_noncode_9",
                "difficulty": "Hard",
                "category": "PCM Bandwidth & Bit Rate",
                "question": "An analog audio signal with bandwidth 4 kHz is sampled at the Nyquist rate and quantized into 256 levels (8 bits/sample). Calculate the bit rate (bps) and transmission bandwidth required.",
                "expected_input_output": "Input: Fmax = 4 kHz, Levels = 256 (n=8 bits)\nOutput: Sampling Fs = 8 kHz, Bit Rate Rb = 64 kbps, Bandwidth B = 32 kHz (or 64 kHz)",
                "solution_code": "",
                "time_complexity": "N/A - Telecommunications",
                "space_complexity": "N/A - Communication Theory",
                "acceptable_answers": [
                    "Fs = 2 * 4 kHz = 8 kHz; Bit rate Rb = 8 kHz * 8 bits = 64 kbps; Bandwidth = Rb / 2 = 32 kHz.",
                    "Sampling rate 8000 Hz times 8 bits gives 64 kbps bit rate. Minimum bandwidth is 32 kHz."
                ]
            },
            {
                "id": "ece_noncode_10",
                "difficulty": "Easy",
                "category": "Zener Diode Voltage Regulation",
                "question": "A 5.1V Zener diode is used to regulate voltage across a load from an un-regulated 12V DC input. If maximum Zener current IZmax = 50 mA, calculate the minimum series resistance Rs required.",
                "expected_input_output": "Input: Vin = 12V, Vz = 5.1V, IZmax = 50 mA\nOutput: Rs_min = (12 - 5.1) / 0.050 = 138 Ω",
                "solution_code": "",
                "time_complexity": "N/A - Semiconductor Physics",
                "space_complexity": "N/A - Power Supply Design",
                "acceptable_answers": [
                    "Rs = (Vin - Vz) / Iz = (12 - 5.1) / 0.05 = 138 Ω.",
                    "Subtract Zener voltage 5.1V from 12V input and divide by 50 mA maximum current to get 138 Ohms."
                ]
            },
            {
                "id": "ece_noncode_11",
                "difficulty": "Medium",
                "category": "555 Timer Astable Multivibrator Frequency",
                "question": "Calculate the output frequency and duty cycle of a 555 timer in astable mode with R1 = 1 kΩ, R2 = 10 kΩ, and C = 0.1 µF.",
                "expected_input_output": "Input: R1 = 1kΩ, R2 = 10kΩ, C = 0.1µF\nOutput: Frequency f = 686 Hz, Duty Cycle = 52.4%",
                "solution_code": "",
                "time_complexity": "N/A - Linear IC Design",
                "space_complexity": "N/A - Circuit Design",
                "acceptable_answers": [
                    "f = 1.44 / ((R1 + 2*R2)*C) = 1.44 / (21k * 0.1µ) = 685.7 Hz; Duty = (R1+R2)/(R1+2R2) = 52.4%.",
                    "Astable frequency is 1.44/((R1+2R2)C) giving 686 Hz and duty cycle is 52.4%."
                ]
            },
            {
                "id": "ece_noncode_12",
                "difficulty": "Hard",
                "category": "MOSFET Threshold Voltage & Drain Current",
                "question": "An N-channel enhancement MOSFET has Vth = 1.5 V, Kn = 2 mA/V². Calculate Drain Current ID when VGS = 3.5 V in saturation mode.",
                "expected_input_output": "Input: Vth = 1.5V, Kn = 2 mA/V², VGS = 3.5V\nOutput: ID = (Kn / 2) * (VGS - Vth)² = 1 * (2.0)² = 4.0 mA",
                "solution_code": "",
                "time_complexity": "N/A - VLSI Design",
                "space_complexity": "N/A - MOSFET Physics",
                "acceptable_answers": [
                    "ID = (Kn / 2) * (VGS - Vth)^2 = 1 * (2.0)^2 = 4.0 mA.",
                    "Apply saturation current equation ID = 0.5 * Kn * (VGS - Vth)^2 to get 4 mA."
                ]
            },
            {
                "id": "ece_noncode_13",
                "difficulty": "Easy",
                "category": "Phase Locked Loop (PLL) Lock Range",
                "question": "Define the concepts of Capture Range and Lock Range in a Phase Locked Loop (PLL) circuit. State which range is always larger.",
                "expected_input_output": "Input: PLL theory\nOutput: Lock Range is always larger than or equal to Capture Range.",
                "solution_code": "",
                "time_complexity": "N/A - Communication Systems",
                "space_complexity": "N/A - PLL Theory",
                "acceptable_answers": [
                    "Lock range is the frequency range over which PLL maintains lock. Lock range is always larger than capture range.",
                    "Capture range is range over which PLL acquires lock; Lock range is range it maintains lock (Lock Range >= Capture Range)."
                ]
            },
            {
                "id": "ece_noncode_14",
                "difficulty": "Medium",
                "category": "Dual-Slope ADC Noise Immunity",
                "question": "Explain why Dual-Slope ADCs offer high noise immunity and rejection of 50/60 Hz power line interference compared to Flash ADCs.",
                "expected_input_output": "Input: Dual-slope ADC concept\nOutput: Integration over fixed time period cancels out high-frequency and line noise.",
                "solution_code": "",
                "time_complexity": "N/A - Analog Instrumentation",
                "space_complexity": "N/A - Data Converters",
                "acceptable_answers": [
                    "Dual-slope ADC integrates input signal over fixed period, averaging out AC line noise.",
                    "Integration phase cancels periodic noise fluctuations equal to multiples of integration period."
                ]
            },
            {
                "id": "ece_noncode_15",
                "difficulty": "Hard",
                "category": "Microcontroller Interrupt Latency",
                "question": "Calculate the Interrupt Latency (in nanoseconds) for an 8-bit microcontroller running at 20 MHz clock speed if handling an ISR requires 8 clock cycles.",
                "expected_input_output": "Input: Clock = 20 MHz (T_clk = 50 ns), Cycles = 8\nOutput: Interrupt Latency = 8 * 50 ns = 400 ns",
                "solution_code": "",
                "time_complexity": "N/A - Embedded Architecture",
                "space_complexity": "N/A - Hardware Timing",
                "acceptable_answers": [
                    "Clock period = 1 / 20 MHz = 50 ns; Latency = 8 * 50 ns = 400 ns.",
                    "Multiply 8 clock cycles by 50 ns period to get 400 nanoseconds interrupt latency."
                ]
            }
        ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
