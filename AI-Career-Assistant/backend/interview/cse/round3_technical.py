# =====================================================================
# CSE - ROUND 3: CORE CS TECHNICAL (15-QUESTION POOL GENERATOR)
# =====================================================================

def get_cse_technical(used_ids=None):
    """
    Generates a pool of EXACTLY 15 Core CS Technical Questions.
    Covers DBMS, OS, Computer Networks, OOP, Data Structures, Algorithms, Software Engineering.
    Contains 3 questions with detailed model answers.
    """
    used_set = set(used_ids or [])

    master_pool = [
        {
            "id": "cse_tech_1",
            "difficulty": "Easy",
            "category": "DBMS (Database Indexing)",
            "question": "What is a Database Index (e.g. B-Tree index) and why is it used in relational databases?",
            "acceptable_answers": [
                "A B-Tree database index speeds up data retrieval queries by reducing disk I/O.",
                "Data structure that improves search operation speed on a database table.",
                "Indexes allow fast lookup of rows without scanning the entire table (full table scan)."
            ],
            "model_answer": "Model Answer:\nA Database Index is a data structure (typically a B-Tree or B+ Tree) that speeds up data retrieval queries on a database table at the cost of additional write overhead and storage.\nKey Benefits:\n1. Reduces time complexity of queries from O(N) full table scan to O(log N).\n2. Enforces uniqueness constraint on primary keys and unique columns."
        },
        {
            "id": "cse_tech_2",
            "difficulty": "Medium",
            "category": "Operating Systems (Process vs Thread)",
            "question": "Explain the fundamental differences between a Process and a Thread in operating system management.",
            "acceptable_answers": [
                "A process has its own isolated address space while threads share memory within the same process.",
                "Process context switching is heavier than thread context switching.",
                "Threads within a process share code, data, and open file handles, but have separate stacks."
            ]
        },
        {
            "id": "cse_tech_3",
            "difficulty": "Medium",
            "category": "Computer Networks (TCP vs UDP)",
            "question": "Compare TCP and UDP protocols. When would you choose UDP over TCP?",
            "acceptable_answers": [
                "TCP is connection-oriented, reliable, and guarantees packet order, whereas UDP is connectionless and fast.",
                "UDP is chosen for real-time applications like video streaming, gaming, and VoIP where low latency is critical.",
                "TCP performs three-way handshake and retransmission, UDP has minimal overhead without handshakes."
            ]
        },
        {
            "id": "cse_tech_4",
            "difficulty": "Hard",
            "category": "DBMS (ACID Properties)",
            "question": "Explain the ACID properties in database management systems and why they are essential for financial transactions.",
            "acceptable_answers": [
                "ACID stands for Atomicity, Consistency, Isolation, and Durability.",
                "Atomicity ensures all-or-nothing execution; Consistency maintains database invariants.",
                "Isolation prevents concurrent transaction interference; Durability guarantees committed data persists across crashes."
            ],
            "model_answer": "Model Answer:\nACID properties guarantee reliable database processing:\n1. Atomicity: 'All or nothing' execution. If any operation fails, the entire transaction rolls back.\n2. Consistency: Database moves from one valid state to another, respecting all constraints.\n3. Isolation: Concurrent transactions execute independently without partial read side-effects.\n4. Durability: Committed updates persist permanently on non-volatile storage even during hardware failures."
        },
        {
            "id": "cse_tech_5",
            "difficulty": "Hard",
            "category": "Operating Systems (Deadlock Conditions)",
            "question": "What are Coffman's 4 necessary conditions for a Deadlock to occur in an operating system?",
            "acceptable_answers": [
                "Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait.",
                "Deadlock requires mutual exclusion, process hold and wait, no resource preemption, and circular waiting chain."
            ]
        },
        {
            "id": "cse_tech_6",
            "difficulty": "Easy",
            "category": "Object-Oriented Programming (Polymorphism)",
            "question": "Explain Compile-Time Polymorphism vs Run-Time Polymorphism in OOP with examples.",
            "acceptable_answers": [
                "Compile-time polymorphism is function overloading / operator overloading. Run-time polymorphism is method overriding using virtual functions.",
                "Overloading is resolved at compile time; Overriding is resolved at runtime using vtable / dynamic binding."
            ]
        },
        {
            "id": "cse_tech_7",
            "difficulty": "Medium",
            "category": "Software Engineering (REST API Standards)",
            "question": "What makes an API RESTful? Explain GET, POST, PUT, and DELETE HTTP verbs.",
            "acceptable_answers": [
                "RESTful APIs are stateless, client-server, cacheable interfaces using standard HTTP methods.",
                "GET reads data, POST creates resources, PUT updates/replaces resources, DELETE removes resources."
            ],
            "model_answer": "Model Answer:\nREST (Representational State Transfer) adheres to 6 constraints: Statelessness, Client-Server architecture, Cacheability, Uniform Interface, Layered System, and Code on Demand.\nHTTP Verbs:\n- GET: Read/retrieve resource (Idempotent)\n- POST: Create new resource\n- PUT: Update existing resource completely (Idempotent)\n- DELETE: Remove specified resource (Idempotent)"
        },
        {
            "id": "cse_tech_8",
            "difficulty": "Medium",
            "category": "Computer Networks (DNS Resolution)",
            "question": "Explain the step-by-step process of what happens when you type a URL into a web browser until the page loads.",
            "acceptable_answers": [
                "DNS resolution maps domain to IP -> TCP 3-way handshake -> TLS handshake -> HTTP GET request -> Server returns HTML/CSS -> Browser renders DOM.",
                "Browser checks cache, queries DNS server for IP address, establishes TCP connection, sends HTTP request, and renders response."
            ]
        },
        {
            "id": "cse_tech_9",
            "difficulty": "Hard",
            "category": "Data Structures & Algorithms (Hash Collision)",
            "question": "How are Hash Collisions handled in Hash Tables? Compare Chaining vs Open Addressing.",
            "acceptable_answers": [
                "Chaining uses linked lists or trees at each bucket index to store colliding keys.",
                "Open addressing probes for alternative open slots in the hash table array (Linear probing, Quadratic probing, Double hashing)."
            ]
        },
        {
            "id": "cse_tech_10",
            "difficulty": "Easy",
            "category": "Operating Systems (Virtual Memory)",
            "question": "What is Virtual Memory and what is a Page Fault?",
            "acceptable_answers": [
                "Virtual memory maps disk storage to extend physical RAM.",
                "A Page Fault occurs when a program attempts to access a memory block not currently mapped in physical RAM."
            ]
        },
        {
            "id": "cse_tech_11",
            "difficulty": "Medium",
            "category": "DBMS (Normalization)",
            "question": "What is Database Normalization? Differentiate between 1NF, 2NF, and 3NF.",
            "acceptable_answers": [
                "Normalization eliminates data redundancy and prevents insertion/update/deletion anomalies.",
                "1NF removes repeating groups, 2NF removes partial dependency, 3NF removes transitive dependency."
            ]
        },
        {
            "id": "cse_tech_12",
            "difficulty": "Hard",
            "category": "Software Engineering (SOLID Principles)",
            "question": "Explain the SOLID principles in Object-Oriented Software Design.",
            "acceptable_answers": [
                "Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.",
                "S: Single Responsibility, O: Open for extension closed for modification, L: Subtypes substitutable, I: Segregated interfaces, D: Depend on abstractions."
            ]
        },
        {
            "id": "cse_tech_13",
            "difficulty": "Easy",
            "category": "Computer Networks (OSI Layers)",
            "question": "List the 7 layers of the OSI Model from lowest to highest.",
            "acceptable_answers": [
                "Physical, Data Link, Network, Transport, Session, Presentation, Application.",
                "Physical (L1), Data Link (L2), Network (L3), Transport (L4), Session (L5), Presentation (L6), Application (L7)."
            ]
        },
        {
            "id": "cse_tech_14",
            "difficulty": "Medium",
            "category": "Algorithms (Sorting Complexity)",
            "question": "Compare Merge Sort and Quick Sort in terms of average time, worst-case time, and space complexity.",
            "acceptable_answers": [
                "Merge Sort is O(N log N) in all cases with O(N) extra space. Quick Sort is average O(N log N), worst-case O(N^2), but in-place O(log N) space.",
                "Merge Sort guarantees O(N log N) time; Quick Sort can degrade to O(N^2) if pivot selection is poor."
            ]
        },
        {
            "id": "cse_tech_15",
            "difficulty": "Hard",
            "category": "Operating Systems (CPU Scheduling)",
            "question": "Compare Round Robin CPU scheduling with Shortest Remaining Time First (SRTF) scheduling.",
            "acceptable_answers": [
                "Round Robin uses fixed time quantum slices for fair CPU sharing.",
                "SRTF is preemptive shortest job first, minimizing average waiting time but susceptible to process starvation."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
