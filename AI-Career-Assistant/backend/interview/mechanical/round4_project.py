# =====================================================================
# MECHANICAL - ROUND 4: PROJECT & RESUME TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_mech_project_questions(projects=None, skills=None, used_ids=None):
    projects = projects or []
    skills = skills or []
    used_set = set(used_ids or [])

    if projects and len(projects) > 0:
        p1 = projects[0]
        p2 = projects[1] if len(projects) > 1 else projects[0]
    elif skills:
        p1 = f"{skills[0]} & {skills[1] if len(skills)>1 else 'ANSYS'} Mechanical System"
        p2 = f"Thermal / CAD {skills[0]} Rig"
    else:
        p1 = "Mechanical Design & Simulation Project"
        p2 = "Thermal / Fluid Mechanical Rig"

    s1 = skills[0] if skills else "SolidWorks"
    s2 = skills[1] if len(skills) > 1 else "ANSYS"

    master_pool = [
        {
            "id": "mech_proj_1",
            "difficulty": "Easy",
            "category": f"Project Design Overview ({p1})",
            "question": f"Walk me through the overall mechanical design and operating principles of your project '{p1}'. What was your individual role?",
            "acceptable_answers": [
                f"Detailed explanation of mechanical components, CAD modeling, material selection, and testing for {p1}.",
                "Explanation of project objective, CAD assembly, structural analysis, and physical prototyping."
            ],
            "model_answer": f"Model Answer Structure:\n1. Objective: Explain the mechanical engineering goal of '{p1}'.\n2. Design Approach: Outline CAD modeling in {s1}, material selection, and stress simulation in {s2}.\n3. Individual Role: Specify component sizing, FEA validation, or machining fabrication."
        },
        {
            "id": "mech_proj_2",
            "difficulty": "Medium",
            "category": f"CAD & Simulation Tools ({s1} & {s2})",
            "question": f"Why did you select **{s1}** and **{s2}** for modeling and analyzing '{p1}'? What boundary conditions did you apply?",
            "acceptable_answers": [
                f"Used {s1} for parametric 3D modeling and {s2} for finite element stress/thermal boundary condition analysis in {p1}.",
                "Applied fixed supports, load vectors, and mesh refinement in FEA package."
            ]
        },
        {
            "id": "mech_proj_3",
            "difficulty": "Medium",
            "category": "Material Selection & Factor of Safety",
            "question": f"What material did you select for key load-bearing components in '{p1}' and what Factor of Safety (FOS) was targeted?",
            "acceptable_answers": [
                f"Selected material for {p1} based on yield strength, weight, cost, and fatigue limits, targeting FOS between 1.5 and 2.5.",
                "Evaluated material mechanical properties (tensile strength, ductility) and applied appropriate design factor of safety."
            ]
        },
        {
            "id": "mech_proj_4",
            "difficulty": "Hard",
            "category": "FEA Mesh Convergence & Accuracy",
            "question": f"How did you perform mesh convergence studies in '{p1}' to ensure FEA simulation results were independent of element size?",
            "acceptable_answers": [
                f"Systematically refined mesh size in high-stress gradient areas of {p1} until stress results converged within 5% variation.",
                "Refined mesh around fillets and holes, monitoring von Mises stress stability."
            ],
            "model_answer": f"Model Answer for '{p1}':\n1. Initial Coarse Mesh: Ran FEA with default global mesh size.\n2. Local Refinement: Applied local mesh controls at fillets, notches, and high stress gradients.\n3. Convergence Plot: Plotted Peak von Mises Stress vs Number of Nodes.\n4. Verification: Selected mesh size where stress change between iterations was under 3%."
        },
        {
            "id": "mech_proj_5",
            "difficulty": "Hard",
            "category": f"Failure Analysis & Optimization ({p1})",
            "question": f"Did any component in '{p1}' experience deflection or failure during physical testing/simulation? How did you redesign it?",
            "acceptable_answers": [
                f"Identified localized yielding or buckling in {p1}, added stiffening ribs/fillets, and increased section modulus.",
                "Redesigned component cross-section, modified material grade, or adjusted geometry to reduce peak stress."
            ]
        },
        {
            "id": "mech_proj_6",
            "difficulty": "Easy",
            "category": "Manufacturing Feasibility (DFM)",
            "question": f"How did you ensure Design for Manufacturing (DFM) compliance for parts in '{p1}'?",
            "acceptable_answers": [
                f"Incorporated draft angles, uniform wall thickness, standard hole sizes, and accessible tool clearances for machining/casting in {p1}.",
                "Designed parts considering CNC tool access, standard stock sizes, and manufacturing tolerances."
            ]
        },
        {
            "id": "mech_proj_7",
            "difficulty": "Medium",
            "category": f"Secondary Project Details ({p2})",
            "question": f"Explain the thermal or mechanical fluid flow analysis conducted for your secondary project '{p2}'.",
            "acceptable_answers": [
                f"Analyzed heat dissipation or fluid pressure drop in {p2} using theoretical equations and CFD/thermal simulation.",
                "Evaluated flow rates, pressure losses, or thermal boundaries."
            ]
        },
        {
            "id": "mech_proj_8",
            "difficulty": "Hard",
            "category": "Thermal Heat Dissipation",
            "question": f"If thermal loads on '{p1}' doubled, what cooling or heat exchanger modifications would you introduce?",
            "acceptable_answers": [
                f"Increase surface area with cooling fins, implement forced convection fans, or use higher conductivity thermal interfaces in {p1}.",
                "Add heat sinks, liquid cooling loops, or optimize fin geometry."
            ],
            "model_answer": f"Model Answer for '{p1}':\n1. Surface Area Expansion: Add pin/plate heat sink fins to increase convective area.\n2. Convection Mode Shift: Transition from natural convection to forced air/liquid cooling.\n3. Interface Materials: Apply high thermal conductivity TIM (Thermal Interface Material) to minimize contact resistance."
        },
        {
            "id": "mech_proj_9",
            "difficulty": "Hard",
            "category": "Dynamic Balancing & Kinematics",
            "question": f"How did you analyze kinematic movement and dynamic balancing of moving parts in '{p1}'?",
            "acceptable_answers": [
                f"Simulated mechanism kinematics using CAD motion analysis, ensuring dynamic balancing of rotating masses in {p1}.",
                "Evaluated linkage trajectory, joint reactions, and counterweight mass balancing."
            ]
        },
        {
            "id": "mech_proj_10",
            "difficulty": "Easy",
            "category": "Tolerance Stack-up Analysis",
            "question": f"Did you perform tolerance stack-up analysis for the assembly of '{p1}'?",
            "acceptable_answers": [
                f"Performed worst-case and RSS (Root Sum Square) tolerance stack-up analysis to guarantee proper fit and clearance in {p1}.",
                "Calculated dimensional chain tolerances for proper mating."
            ]
        },
        {
            "id": "mech_proj_11",
            "difficulty": "Medium",
            "category": "Prototyping & Fabrication",
            "question": f"What prototyping methods (3D printing/FDM, CNC machining, sheet metal fabrication) were used to build '{p1}'?",
            "acceptable_answers": [
                f"Utilized 3D printing for rapid plastic prototyping and CNC milling / sheet metal bending for functional metal parts in {p1}.",
                "Fabricated components via machining, 3D printing, and welding."
            ]
        },
        {
            "id": "mech_proj_12",
            "difficulty": "Hard",
            "category": "Cost & Weight Optimization",
            "question": f"How did you optimize '{p1}' for weight reduction (generative design / topology optimization) while maintaining structural integrity?",
            "acceptable_answers": [
                f"Applied topology optimization to remove material from low-stress regions, reducing weight while preserving stiffness in {p1}.",
                "Used generative design algorithms to minimize mass."
            ]
        },
        {
            "id": "mech_proj_13",
            "difficulty": "Easy",
            "category": "Standards & Safety Compliance",
            "question": f"What engineering standards (ISO, ASME, ASTM, IS codes) guided your design process for '{p1}'?",
            "acceptable_answers": [
                f"Followed ASME design standards for pressure/structural components and ASTM material specifications in {p1}.",
                "Adhered to ISO/IS standards for machine drawings, fits, and tolerances."
            ]
        },
        {
            "id": "mech_proj_14",
            "difficulty": "Medium",
            "category": "Testing & Sensor Instrumentation",
            "question": f"What sensors (strain gauges, thermocouples, tachometers) were used to collect experimental data during '{p1}' testing?",
            "acceptable_answers": [
                f"Instrumented rig with strain gauges for stress measurement and thermocouples for temperature logging in {p1}.",
                "Used sensors and data acquisition hardware to record physical parameters."
            ]
        },
        {
            "id": "mech_proj_15",
            "difficulty": "Hard",
            "category": "Commercialization & Future Enhancements",
            "question": f"What modifications would be required to convert '{p1}' into a mass-manufactured commercial product?",
            "acceptable_answers": [
                f"Transition from custom machining to die casting / injection molding, streamline assembly steps, and reduce part count in {p1}.",
                "Design for mass production using die casting, stamping, and automated assembly."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
