# =====================================================================
# MECHANICAL - ROUND 3: CORE MECHANICAL TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_mech_technical(used_ids=None):
    used_set = set(used_ids or [])

    master_pool = [
        {
            "id": "mech_tech_1",
            "difficulty": "Easy",
            "category": "Thermodynamics (First & Second Law)",
            "question": "State the First and Second Laws of Thermodynamics and their physical significance in mechanical systems.",
            "acceptable_answers": [
                "First Law is conservation of energy (dU = dQ - dW). Second Law states heat flows spontaneously from hot to cold, and entropy increases.",
                "First law introduces internal energy and energy conservation. Second law introduces entropy and limits thermal efficiency."
            ],
            "model_answer": "Model Answer:\nFirst Law: Energy cannot be created or destroyed, only transformed (dQ = dU + dW).\nSecond Law: Clausius statement (heat cannot spontaneously flow from cold to hot without external work) and Kelvin-Planck statement (no heat engine operating in a cycle can convert all absorbed heat into work). Defines Entropy."
        },
        {
            "id": "mech_tech_2",
            "difficulty": "Medium",
            "category": "Fluid Mechanics (Bernoulli's Equation)",
            "question": "State Bernoulli's Equation and list the key assumptions required for its validity.",
            "acceptable_answers": [
                "P + 0.5*rho*v^2 + rho*g*z = Constant. Assumptions: Incompressible, inviscid (frictionless), steady flow, along a streamline.",
                "Bernoulli's principle connects pressure, velocity, and elevation head for ideal, non-viscous steady flow."
            ]
        },
        {
            "id": "mech_tech_3",
            "difficulty": "Medium",
            "category": "Strength of Materials (SFD & BMD)",
            "question": "Differentiate between Shearing Force (SF) and Bending Moment (BM). Where does maximum bending moment occur on a beam?",
            "acceptable_answers": [
                "Shearing force is algebraic sum of vertical forces; Bending moment is sum of moments. Maximum BM occurs where SF is zero or changes sign.",
                "Maximum bending moment occurs at points where Shear Force passes through zero."
            ]
        },
        {
            "id": "mech_tech_4",
            "difficulty": "Hard",
            "category": "Machine Design (Fatigue & Stress Concentration)",
            "question": "What is Stress Concentration and how is Goodman's Criterion used in designing components subjected to fluctuating fatigue loads?",
            "acceptable_answers": [
                "Stress concentration occurs at geometric discontinuities (notches, holes). Goodman line relates mean stress and alternating stress against yield/endurance limit.",
                "Goodman criterion: (sigma_m / sigma_ut) + (sigma_a / sigma_e) = 1/N for fatigue design under fluctuating stress."
            ],
            "model_answer": "Model Answer:\nStress Concentration: Localization of high stress around geometric irregularities (notches, keyways, fillets).\nGoodman Criterion: Linear fatigue failure theory combining mean stress (sigma_m) and alternating stress (sigma_a):\n(sigma_a / Se) + (sigma_m / Sut) = 1 / Factor of Safety\nWhere Se = Endurance limit, Sut = Ultimate tensile strength."
        },
        {
            "id": "mech_tech_5",
            "difficulty": "Hard",
            "category": "Heat Transfer (Modes & Dimensionless Numbers)",
            "question": "Explain Conduction, Convection, and Radiation. What is the physical significance of Nusselt Number and Reynolds Number?",
            "acceptable_answers": [
                "Conduction (Fourier's law), Convection (Newton's cooling), Radiation (Stefan-Boltzmann). Nusselt = ratio of convective to conductive heat transfer; Reynolds = ratio of inertial to viscous forces.",
                "Nusselt number measures convective heat transfer enhancement. Reynolds number determines laminar vs turbulent flow regime."
            ]
        },
        {
            "id": "mech_tech_6",
            "difficulty": "Easy",
            "category": "Materials Science (Iron-Carbon Diagram)",
            "question": "What is the Eutectoid Point on the Iron-Iron Carbide (Fe-Fe3C) phase diagram, and what phase transformation occurs there?",
            "acceptable_answers": [
                "Eutectoid point occurs at 0.76% carbon and 727°C where Austenite transforms into Pearlite (ferrite + cementite).",
                "Solid Austenite transforms into alternate layers of Ferrite and Cementite (Pearlite) at 727°C."
            ]
        },
        {
            "id": "mech_tech_7",
            "difficulty": "Medium",
            "category": "Manufacturing (Casting vs Forging)",
            "question": "Compare Casting and Forging manufacturing processes. Which process yields superior mechanical strength and structural integrity?",
            "acceptable_answers": [
                "Forging yields superior grain structure, strength, and fatigue resistance due to mechanical plastic deformation.",
                "Casting pours molten metal into molds (good for complex shapes). Forging deforms solid metal, aligning grain flow for higher strength."
            ],
            "model_answer": "Model Answer:\n- Casting: Molten metal poured into mold cavity. Ideal for complex geometries, internal passages, and large components. May contain porosity.\n- Forging: Solid metal deformed under compressive forces (hammer/press). Refines grain boundary alignment along stress direction, yielding superior tensile strength and impact toughness."
        },
        {
            "id": "mech_tech_8",
            "difficulty": "Medium",
            "category": "CAD/CAM (GD&T Principles)",
            "question": "What is GD&T (Geometric Dimensioning & Tolerancing)? Explain Maximum Material Condition (MMC) and Least Material Condition (LMC).",
            "acceptable_answers": [
                "GD&T defines allowable geometric variation. MMC is the condition where feature contains maximum volume of material (e.g. smallest hole, largest shaft).",
                "MMC represents maximum weight/material state; LMC represents minimum weight/material state."
            ]
        },
        {
            "id": "mech_tech_9",
            "difficulty": "Hard",
            "category": "Theory of Machines (Governors vs Flywheels)",
            "question": "Differentiate between a Governor and a Flywheel in engine speed control.",
            "acceptable_answers": [
                "Flywheel controls speed fluctuations within a single cycle (energy reservoir). Governor regulates mean engine speed over varying load conditions by controlling fuel supply.",
                "Flywheel smooths cyclic torque variations; Governor adjusts fuel flow to maintain mean speed under load changes."
            ]
        },
        {
            "id": "mech_tech_10",
            "difficulty": "Easy",
            "category": "Fluid Machinery (Pumps vs Turbines)",
            "question": "Compare Centrifugal Pumps and Axial Flow Pumps in terms of head and discharge capacity.",
            "acceptable_answers": [
                "Centrifugal pumps develop high head at low/moderate discharge. Axial flow pumps deliver high discharge at low head.",
                "Centrifugal = high head, low flow. Axial = low head, high volumetric flow rate."
            ]
        },
        {
            "id": "mech_tech_11",
            "difficulty": "Medium",
            "category": "HVAC & Psychrometrics",
            "question": "What is Relative Humidity, Dew Point Temperature, and Sensible vs Latent Heat in HVAC systems?",
            "acceptable_answers": [
                "Relative humidity is ratio of actual water vapor pressure to saturation pressure. Sensible heat changes temperature; Latent heat changes phase.",
                "Dew point is temperature at which moisture condenses. Sensible heat alters temperature, latent heat alters phase."
            ]
        },
        {
            "id": "mech_tech_12",
            "difficulty": "Hard",
            "category": "Vibrations (Resonance)",
            "question": "What is Mechanical Resonance, and how can engineers prevent catastrophic resonant failures in rotating machinery?",
            "acceptable_answers": [
                "Resonance occurs when operating excitation frequency matches natural frequency, causing maximum amplitude vibration.",
                "Prevented by changing stiffness/mass, adding dampers, or avoiding critical operating speeds."
            ]
        },
        {
            "id": "mech_tech_13",
            "difficulty": "Easy",
            "category": "Welding & Joining",
            "question": "Compare TIG (GTAW) and MIG (GMAW) welding processes.",
            "acceptable_answers": [
                "TIG uses non-consumable tungsten electrode with separate filler. MIG uses continuously fed consumable wire electrode.",
                "TIG = non-consumable tungsten electrode (precise, clean). MIG = consumable continuous wire feed (faster)."
            ]
        },
        {
            "id": "mech_tech_14",
            "difficulty": "Medium",
            "category": "Power Plant Engineering",
            "question": "Explain the Rankine Cycle used in thermal power plants and methods used to increase its thermal efficiency.",
            "acceptable_answers": [
                "Rankine cycle uses boiler, turbine, condenser, pump. Efficiency increased by superheating steam, reheating, and regenerative feedwater heating.",
                "Standard vapor power cycle. Improved via steam superheating, reheat cycles, and feedwater preheating."
            ]
        },
        {
            "id": "mech_tech_15",
            "difficulty": "Hard",
            "category": "Tool Design & Metal Cutting",
            "question": "Explain Merchant's Circle Diagram in metal cutting and how shear angle influences cutting forces.",
            "acceptable_answers": [
                "Merchant's circle relates cutting force, thrust force, friction force, and normal force. Larger shear angle reduces shear plane area and cutting power requirement.",
                "Analytical vector representation of cutting forces on single-point tool. Higher shear angle lowers power consumption."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
