def solution(a: int, b: int, c: int) -> str | int:
    if c < 0:
        return "No solutions"
    if c == 0:
        return -b // a
    return (c ** 2 - b) // a
