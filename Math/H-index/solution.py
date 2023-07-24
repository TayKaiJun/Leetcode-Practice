def solution(citations):
    n = len(citations)
    freq = [0] * (n+1)

    for i in citations:
        if i > n:
            freq[n] += 1
        else:
            freq[i] += 1
    # print(freq)

    result = 0
    for j in range(n,-1,-1):
        result += freq[j]
        if result >= j:
            while result > j:
                result -= 1
            break
    
    return result


if __name__ == "__main__":
    print(solution([3,0,6,1,5])) # 3
    print(solution([1,3,1])) # 1
    print(solution([1,1,1])) # 1
    print(solution([0,0,0])) # 0
    print(solution([3,3,3])) # 3
    print(solution([9, 7, 6, 2, 1])) # 3
