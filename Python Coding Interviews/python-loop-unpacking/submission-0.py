from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    sorted_scores = sorted(scores, reverse = True, key = lambda tup : tup[1])
    return sorted_scores[0][0]

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
