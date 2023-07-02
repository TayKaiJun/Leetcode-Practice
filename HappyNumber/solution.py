def solution(n: int) -> bool:
        existing = set()
        while n != 1:
            if n in existing:
                return False
            else:
                existing.add(n)

            n = sum([int(i) ** 2 for i in str(n)])
        return True


if __name__ == "__main__":
    print(solution(19))
    print(solution(2))
    print(solution(7))
    print(solution(1111111))
    print(solution(11111111))
    print(solution(111111111))
    print(solution(1111111111))
    print(solution(11111111111))
    print(solution(111111111111))
    print(solution(1111111111111))
    print(solution(11111111111111))
    print(solution(111111111111111))
    print(solution(1111111111111111))
    print(solution(11111111111111111))
    print(solution(111111111111111111))