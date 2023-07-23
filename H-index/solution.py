def solution(citations):
    citations.sort(reverse=True)
    count = 0
    for i in citations:
        if i > count:
            count += 1
        else:
            break
    return count


if __name__ == "__main__":
    print(solution([3,0,6,1,5])) # 3
    print(solution([1,3,1])) # 1
    print(solution([1,1,1])) # 1
    print(solution([0,0,0])) # 0
    print(solution([3,3,3])) # 3
    print(solution([9, 7, 6, 2, 1])) # 3
