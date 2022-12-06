import collections
import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    check = collections.deque(maxlen=4)
    for i, letter in enumerate(s.strip(), start=1):
        check.append(letter)
        if len(check) <= 3 or len(check) != len(set(check)):
            continue
        print(i)
        break
    return 0


if __name__ == "__main__":
    raise SystemExit(solver(file_reader(file)))
