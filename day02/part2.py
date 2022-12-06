from __future__ import annotations

import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file) as f:
        return f.read()


def solver(s: str) -> int:
    _translation = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"}
    weights = {"R": 1, "P": 2, "S": 3}
    values = {"X": 0, "Y": 3, "Z": 6}
    winning_losing_scores = {"R": "S", "P": "R", "S": "P"}
    losing_scores = {v: k for k, v in winning_losing_scores.items()}
    total_score = 0
    for line in s.splitlines():
        opp_orig, my_orig = line.split(" ")
        opp, _ = _translation[opp_orig], _translation[my_orig]
        total_score += values[my_orig]
        if values[my_orig] == 0:
            total_score += weights[winning_losing_scores[opp]]
        elif values[my_orig] == 3:
            total_score += weights[opp]
        elif values[my_orig] == 6:
            total_score += weights[losing_scores[opp]]
    return total_score


def main() -> int:
    print(solver(file_reader(file)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
