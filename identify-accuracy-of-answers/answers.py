# ===========================================
# AI Truth Analysis System (File Input Version)
# ===========================================

def analyze_answer(answer):
    """Analyzes one answer and returns a truth score."""
    answer = answer.lower().strip()
    score = 100  # start from full truth

    # Signs of hesitation or uncertainty
    hesitation_words = ["uh", "um", "maybe", "not sure", "i think", "can't remember"]
    for word in hesitation_words:
        if word in answer:
            score -= 15

    # Signs of defensiveness or evasion
    defensive_words = ["why are you asking", "i don't know", "leave me alone", "stop asking"]
    for word in defensive_words:
        if word in answer:
            score -= 25

    # Honest indicators (direct, short, confident)
    honest_words = ["yes", "no", "sure", "definitely", "of course"]
    for word in honest_words:
        if word in answer:
            score += 10

    # Too long or complicated answers might indicate lying
    if len(answer.split()) > 15:
        score -= 10

    # Cap score between 0 and 100
    return max(0, min(score, 100))


def ai_truth_detector_from_file(filename):
    """Reads answers from a text file and analyzes them."""
    print("=== AI Truth Detection System ===")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            answers = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    if not answers:
        print("No answers found in the file.")
        return

    total_score = 0
    for i, ans in enumerate(answers, start=1):
        score = analyze_answer(ans)
        print(f"Answer {i}: {ans}")
        print(f" → Truth Score: {score}%\n")
        total_score += score

    avg_truth = total_score / len(answers)
    print("=== Summary ===")
    print(f"Average Truth Percentage: {avg_truth:.2f}%")

    if avg_truth >= 75:
        print("Conclusion: Answers appear truthful.")
    elif avg_truth >= 40:
        print("Conclusion: Mixed honesty detected.")
    else:
        print("Conclusion: High chance of deception.")


# Example usage:
# Make sure you have a file called 'answers.txt' in the same folder
# Each line should contain one answer.

ai_truth_detector_from_file("generated answers.txt")

