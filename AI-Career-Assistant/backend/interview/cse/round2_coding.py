# =====================================================================
# CSE - ROUND 2: CODING & PROBLEM SOLVING (BASED ON MENTIONED LANGUAGES)
# =====================================================================
from backend.interview.question_pool import extract_mentioned_programming_languages

def get_cse_coding(skills=None, projects=None, used_ids=None, resume_text=""):
    """
    Generates a pool of 15 Coding Questions for CSE candidates strictly based on 
    the programming languages they mention in their resume/skills.
    """
    skills = skills or []
    projects = projects or []
    used_set = set(used_ids or [])

    langs = extract_mentioned_programming_languages(skills=skills, resume_text=resume_text)
    if not langs:
        langs = ["Python", "C++", "Java"]

    main_lang = langs[0]
    sec_lang = langs[1] if len(langs) > 1 else langs[0]
    langs_str = ", ".join(langs)
    proj = projects[0] if projects else "Software Project"

    master_pool = [
        {
            "id": "cse_coding_1",
            "difficulty": "Easy",
            "category": f"{main_lang} - Array & Frequency Logic",
            "question": f"Write an executable {main_lang} function to find the maximum element and its frequency in an array of integers. (Mentioned Language: {main_lang})",
            "expected_input_output": "Input: [3, 7, 2, 7, 5, 7]\nOutput: Maximum = 7, Frequency = 3",
            "solution_code": f"""# Solution in {main_lang}
def max_and_frequency(arr):
    if not arr:
        return None, 0
    max_val = arr[0]
    freq = 0
    for num in arr:
        if num > max_val:
            max_val = num
            freq = 1
        elif num == max_val:
            freq += 1
    return max_val, freq

# Test
numbers = [3, 7, 2, 7, 5, 7]
print(max_and_frequency(numbers))""",
            "time_complexity": "O(N) - Single pass scan",
            "space_complexity": "O(1) - Constant space",
            "model_answer": f"Model Solution in {main_lang}:\n\nIterate through the array, keeping track of the current maximum element and its frequency count.",
            "acceptable_answers": [
                "Single pass loop maintaining max_val and frequency count.",
                "Loop through array, update max_val if larger element found, count occurrences.",
                "Use max() and count() methods or linear array traversal."
            ]
        },
        {
            "id": "cse_coding_2",
            "difficulty": "Medium",
            "category": f"{sec_lang} - String Processing & Parsing",
            "question": f"Write a {sec_lang} function to sanitize input strings for '{proj}' by counting total vowels and consonants while ignoring special characters. (Mentioned Language: {sec_lang})",
            "expected_input_output": "Input: 'Hello World 2026!'\nOutput: Vowels = 3, Consonants = 7",
            "solution_code": f"""# Solution in {sec_lang}
def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

print(count_vowels_consonants("Hello World 2026!"))""",
            "time_complexity": "O(N) - Linear string traversal",
            "space_complexity": "O(1) - Constant lookup set",
            "acceptable_answers": [
                "Iterate characters, check char.isalpha(), increment vowel count if in aeiou else consonant count.",
                "Loop through string and track vowel and consonant counters using set lookup.",
                "Use regex or character classification to count vowels and consonants."
            ]
        },
        {
            "id": "cse_coding_3",
            "difficulty": "Hard",
            "category": f"{main_lang} - Hash Table & Optimization (Two Sum)",
            "question": f"Write an O(N) hash map solution in {main_lang} for the 'Two Sum' problem, returning the indices of two numbers that sum to a target value.",
            "expected_input_output": "Input: nums = [2, 7, 11, 15], target = 9\nOutput: [0, 1] (2 + 7 = 9)",
            "solution_code": f"""# Solution in {main_lang}
def two_sum(nums, target):
    seen = {{}}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []

print(two_sum([2, 7, 11, 15], 9))""",
            "time_complexity": "O(N) - Single pass hash map lookup",
            "space_complexity": "O(N) - Dictionary memory",
            "model_answer": f"Model Answer in {main_lang}:\n\nStore the complement (target - num) as key in hash dictionary for O(1) average lookup.",
            "acceptable_answers": [
                "Store complement target - num as key in hash map for O(1) average lookup.",
                "Hash map dictionary stores numbers and indices during a single array pass.",
                "Linear pass checking complement presence in dictionary."
            ]
        },
        {
            "id": "cse_coding_4",
            "difficulty": "Easy",
            "category": f"{main_lang} - Palindrome String Validation",
            "question": f"Write a function in {main_lang} to test whether a given string is a valid palindrome, ignoring spaces and case sensitivity.",
            "expected_input_output": "Input: 'A man a plan a canal Panama'\nOutput: True",
            "solution_code": f"""# Solution in {main_lang}
def is_palindrome(s):
    clean = [c.lower() for c in s if c.isalnum()]
    return clean == clean[::-1]

print(is_palindrome("A man a plan a canal Panama"))""",
            "time_complexity": "O(N) - String filter and reverse",
            "space_complexity": "O(N) - Cleaned character list",
            "acceptable_answers": [
                "Filter alphanumeric characters, convert to lowercase, compare clean string with its reverse.",
                "Two pointer approach comparing left and right characters inwards.",
                "Reverse cleaned string and test equality."
            ]
        },
        {
            "id": "cse_coding_5",
            "difficulty": "Medium",
            "category": f"{sec_lang} - In-Place Array Manipulation",
            "question": f"Write a {sec_lang} function to move all zeros in an integer array to the end while maintaining the relative order of non-zero elements.",
            "expected_input_output": "Input: [0, 1, 0, 3, 12]\nOutput: [1, 3, 12, 0, 0]",
            "solution_code": f"""# Solution in {sec_lang}
def move_zeroes(nums):
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    while pos < len(nums):
        nums[pos] = 0
        pos += 1
    return nums

print(move_zeroes([0, 1, 0, 3, 12]))""",
            "time_complexity": "O(N) - Single pass in-place swap",
            "space_complexity": "O(1) - Constant auxiliary memory",
            "acceptable_answers": [
                "Maintain insert position index, overwrite non-zeros, fill trailing elements with zero.",
                "Two pointer swap mechanism moving non-zero values forward.",
                "In-place array manipulation storing non-zero index."
            ]
        },
        {
            "id": "cse_coding_6",
            "difficulty": "Hard",
            "category": f"{main_lang} - Dynamic Programming Tabulation",
            "question": f"Write an optimized dynamic programming function in {main_lang} (O(N) time, O(1) space) to calculate the N-th Fibonacci number.",
            "expected_input_output": "Input: n = 10\nOutput: 55",
            "solution_code": f"""# Solution in {main_lang}
def fibonacci(n):
    if n <= 0: return 0
    if n == 1: return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fibonacci(10))""",
            "time_complexity": "O(N) - Linear iteration",
            "space_complexity": "O(1) - Two variables",
            "model_answer": f"Model Answer in {main_lang}:\n\nIterative dynamic programming approach keeping track of only the last two Fibonacci numbers.",
            "acceptable_answers": [
                "Iterative bottom-up dynamic programming keeping track of last two variables.",
                "Memoized recursion or loop tracking previous two values.",
                "O(N) iterative tabulation avoiding exponential redundant recursive calls."
            ]
        },
        {
            "id": "cse_coding_7",
            "difficulty": "Easy",
            "category": f"{main_lang} - Linked List Inversion",
            "question": f"Write code in {main_lang} to define a singly Linked List Node class and an in-place method to reverse the linked list.",
            "expected_input_output": "Input: 1 -> 2 -> 3 -> None\nOutput: 3 -> 2 -> 1 -> None",
            "solution_code": f"""# Solution in {main_lang}
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev""",
            "time_complexity": "O(N) - Single pass traversal",
            "space_complexity": "O(1) - Three pointers",
            "acceptable_answers": [
                "Three-pointer approach (prev, curr, nxt) reversing next pointers in place.",
                "Iterate through nodes, redirecting next pointer to previous node.",
                "Standard in-place linked list reversal."
            ]
        },
        {
            "id": "cse_coding_8",
            "difficulty": "Medium",
            "category": f"{sec_lang} - Stack Data Structure & Bracket Match",
            "question": f"Write a function in {sec_lang} using a Stack to check if brackets in a string balance properly: '()', '{{}}', '[]'.",
            "expected_input_output": "Input: '{{[()]}}'\nOutput: True",
            "solution_code": f"""# Solution in {sec_lang}
def isValidBrackets(s):
    stack = []
    mapping = {{')': '(', '}}': '{{', ']': '['}}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return len(stack) == 0

print(isValidBrackets('{{[()]}}'))""",
            "time_complexity": "O(N) - Push/pop per character",
            "space_complexity": "O(N) - Stack storage",
            "acceptable_answers": [
                "Push opening brackets onto stack, pop and match when closing bracket encountered.",
                "Use stack data structure and hash map of matching bracket pairs.",
                "Stack-based parenthesis validation algorithm."
            ]
        },
        {
            "id": "cse_coding_9",
            "difficulty": "Hard",
            "category": f"{main_lang} - Binary Tree Level Order (BFS)",
            "question": f"Write an executable function in {main_lang} for Level Order Traversal (BFS) of a Binary Tree using a Queue data structure.",
            "expected_input_output": "Input: Tree [1, 2, 3, 4, 5]\nOutput: [[1], [2, 3], [4, 5]]",
            "solution_code": f"""# Solution in {main_lang}
from collections import deque

def level_order(root):
    if not root: return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res""",
            "time_complexity": "O(N) - Single node visits",
            "space_complexity": "O(W) - Queue width",
            "acceptable_answers": [
                "Breadth First Search (BFS) using a FIFO deque queue.",
                "Pop level nodes, record values, enqueue left and right children.",
                "Level-by-level binary tree BFS iteration."
            ]
        },
        {
            "id": "cse_coding_10",
            "difficulty": "Easy",
            "category": f"{main_lang} - Binary Search Algorithm",
            "question": f"Write a binary search function in {main_lang} to find the index of a target value in a sorted array in O(log N) time.",
            "expected_input_output": "Input: arr = [1, 3, 5, 7, 9, 11], target = 7\nOutput: Index = 3",
            "solution_code": f"""# Solution in {main_lang}
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))""",
            "time_complexity": "O(log N) - Binary halving",
            "space_complexity": "O(1) - Iterative constant space",
            "acceptable_answers": [
                "Maintain low and high pointers, calculate mid index, halve search space.",
                "Iterative binary search with O(log N) complexity.",
                "Compare target with middle element and shrink search boundaries."
            ]
        },
        {
            "id": "cse_coding_11",
            "difficulty": "Medium",
            "category": f"{sec_lang} - Matrix Transpose & Manipulation",
            "question": f"Write a {sec_lang} function to transpose an N x M 2D matrix (swap rows and columns).",
            "expected_input_output": "Input: [[1, 2], [3, 4], [5, 6]]\nOutput: [[1, 3, 5], [2, 4, 6]]",
            "solution_code": f"""# Solution in {sec_lang}
def transpose(matrix):
    return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

print(transpose([[1, 2], [3, 4], [5, 6]]))""",
            "time_complexity": "O(R * C) - Visit every cell",
            "space_complexity": "O(R * C) - New matrix allocation",
            "acceptable_answers": [
                "Nested loop swapping row and column indices (matrix[r][c] -> matrix[c][r]).",
                "List comprehension or zip(*matrix) in Python.",
                "Matrix transpose algorithm."
            ]
        },
        {
            "id": "cse_coding_12",
            "difficulty": "Hard",
            "category": f"{main_lang} - Shortest Path (Dijkstra)",
            "question": f"Write Dijkstra's shortest path algorithm in {main_lang} using a Min-Heap Priority Queue for graph travel.",
            "expected_input_output": "Input: Graph adjacency list & start node A\nOutput: Shortest distance dictionary to all nodes",
            "solution_code": f"""# Solution in {main_lang}
import heapq

def dijkstra(graph, start):
    dist = {{node: float('inf') for node in graph}}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist""",
            "time_complexity": "O((V + E) log V) - Min-heap operations",
            "space_complexity": "O(V + E) - Adjacency graph",
            "acceptable_answers": [
                "Use min-heap priority queue to greedily expand smallest distance node.",
                "Maintain distances dictionary, relax edges, and push to priority queue.",
                "Greedy shortest path algorithm with min heap."
            ]
        },
        {
            "id": "cse_coding_13",
            "difficulty": "Easy",
            "category": f"{main_lang} - String Word Frequency Count",
            "question": f"Write a function in {main_lang} to count word frequencies in a sentence and return a frequency dictionary.",
            "expected_input_output": "Input: 'apple banana apple orange'\nOutput: {{'apple': 2, 'banana': 1, 'orange': 1}}",
            "solution_code": f"""# Solution in {main_lang}
def word_count(sentence):
    counts = {{}}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_count('apple banana apple orange'))""",
            "time_complexity": "O(N) - Linear word scan",
            "space_complexity": "O(U) - Unique words map",
            "acceptable_answers": [
                "Split string by whitespace, iterate words, update hash map counts.",
                "Use collections.Counter or standard dict get() counter.",
                "Dictionary frequency accumulation."
            ]
        },
        {
            "id": "cse_coding_14",
            "difficulty": "Medium",
            "category": f"{sec_lang} - Kadane's Algorithm Max Subarray",
            "question": f"Write Kadane's algorithm function in {sec_lang} to find the maximum sum contiguous subarray.",
            "expected_input_output": "Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]\nOutput: Max Sum = 6",
            "solution_code": f"""# Solution in {sec_lang}
def max_subarray(nums):
    max_so_far = curr = nums[0]
    for num in nums[1:]:
        curr = max(num, curr + num)
        max_so_far = max(max_so_far, curr)
    return max_so_far

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))""",
            "time_complexity": "O(N) - Single pass DP",
            "space_complexity": "O(1) - Constant space",
            "acceptable_answers": [
                "Kadane's algorithm: curr_max = max(num, curr_max + num), max_so_far = max(max_so_far, curr_max).",
                "Iterative linear scan tracking local maximum and global maximum.",
                "Dynamic programming O(N) max contiguous subarray."
            ]
        },
        {
            "id": "cse_coding_15",
            "difficulty": "Hard",
            "category": f"{main_lang} - Backtracking & Permutations",
            "question": f"Write a recursive backtracking function in {main_lang} to generate all unique permutations of an integer array.",
            "expected_input_output": "Input: [1, 2, 3]\nOutput: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]",
            "solution_code": f"""# Solution in {main_lang}
def permute(nums):
    res = []
    def backtrack(start):
        if start == len(nums):
            res.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return res

print(permute([1, 2, 3]))""",
            "time_complexity": "O(N * N!) - Permutation tree",
            "space_complexity": "O(N) - Stack call depth",
            "acceptable_answers": [
                "Recursive backtracking with in-place swapping and un-swapping (undo action).",
                "Depth first search state space tree exploration with backtracking.",
                "Generate N! permutations via recursive swap."
            ]
        }
    ]

    fresh_pool = [q for q in master_pool if q["id"] not in used_set]
    return fresh_pool if len(fresh_pool) >= 15 else master_pool
