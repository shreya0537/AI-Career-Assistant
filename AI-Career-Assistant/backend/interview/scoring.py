import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def normalize_text(text):
    """Normalizes text by lowercasing and stripping non-alphanumeric characters."""
    if not text:
        return ""
    text_clean = str(text).lower()
    text_clean = re.sub(r"[^a-z0-9\s]", " ", text_clean)
    return re.sub(r"\s+", " ", text_clean).strip()


def evaluate_question_answer(user_text, acceptable_answers):
    """
    Evaluates user answer against 3-4 acceptable key-answer patterns.
    Returns dict with attempted status, correctness, score, and expected patterns.
    """
    if not user_text or not user_text.strip():
        return {
            "attempted": False,
            "is_correct": False,
            "score": 0,
            "user_answer": "",
            "acceptable_answers": acceptable_answers
        }

    user_clean = normalize_text(user_text)
    if not user_clean:
        return {
            "attempted": False,
            "is_correct": False,
            "score": 0,
            "user_answer": user_text,
            "acceptable_answers": acceptable_answers
        }

    # 1. Concept / Keyword Matching against acceptable patterns
    best_similarity = 0.0
    matched_pattern = False

    for pattern in acceptable_answers:
        pattern_clean = normalize_text(pattern)
        if not pattern_clean:
            continue

        # Check key terms overlap
        pattern_words = set(w for w in pattern_clean.split() if len(w) > 3)
        user_words = set(w for w in user_clean.split() if len(w) > 3)

        if pattern_words:
            overlap_ratio = len(pattern_words.intersection(user_words)) / len(pattern_words)
            if overlap_ratio >= 0.4:
                matched_pattern = True

        # TF-IDF Cosine Similarity
        try:
            vectorizer = TfidfVectorizer(stop_words="english")
            vectors = vectorizer.fit_transform([user_clean, pattern_clean])
            sim = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
            if sim > best_similarity:
                best_similarity = sim
        except ValueError:
            pass

    is_correct = matched_pattern or (best_similarity >= 0.25)
    score = round(max(best_similarity * 100, 100 if is_correct else 0))

    return {
        "attempted": True,
        "is_correct": is_correct,
        "score": score if is_correct else max(score, 40 if best_similarity > 0.15 else 0),
        "user_answer": user_text,
        "acceptable_answers": acceptable_answers
    }


def calculate_round_summary(evaluations):
    """
    Calculates summary metrics for a round:
    - Total questions
    - Attempted questions
    - Correct answers
    - Incorrect answers
    - Unanswered questions
    - Score percentage calculated strictly based on ATTEMPTED questions.
    """
    total_q = len(evaluations)
    attempted_list = [ev for ev in evaluations if ev.get("attempted", False)]
    attempted_q = len(attempted_list)
    unanswered_q = total_q - attempted_q

    correct_q = sum(1 for ev in attempted_list if ev.get("is_correct", False))
    incorrect_q = attempted_q - correct_q

    # Attempted score formula: Correct / Attempted * 100
    if attempted_q > 0:
        score_pct = round((correct_q / attempted_q) * 100, 2)
    else:
        score_pct = 0.0

    return {
        "total": total_q,
        "attempted": attempted_q,
        "correct": correct_q,
        "incorrect": incorrect_q,
        "unanswered": unanswered_q,
        "score": score_pct
    }
