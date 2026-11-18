def get_recommendation(
    score
):

    if score >= 80:

        return (
            "Excellent performance! "
            "You have demonstrated strong "
            "knowledge."
        )

    elif score >= 60:

        return (
            "Good performance! "
            "Keep practicing to improve "
            "your technical knowledge."
        )

    elif score >= 40:

        return (
            "Average performance. "
            "More practice is recommended."
        )

    else:

        return (
            "You need more preparation. "
            "Practice your technical and "
            "project concepts."
        )