def calculate_score(correct=0, wrong=0):
    penalty_per_wrong = 0.25

    correct = correct or 0
    wrong = wrong or 0

    final_score = correct - (wrong * penalty_per_wrong)

    return round(final_score, 2)


# Example
data = {
    "correct": 8,
    "wrong": 2
}

result = {
    "final_score": calculate_score(
        data.get("correct"),
        data.get("wrong")
    )
}

print(result)