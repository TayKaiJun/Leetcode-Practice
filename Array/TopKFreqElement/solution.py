def solution(nums, k):
    freq = {}
    for i in nums:
        freq[i] = 1 if i not in freq else freq[i] + 1
    
    sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    print(sorted_freq)

    result = []
    for i in range(k):
        result.append(sorted_freq[i][0])
    return result

if __name__ == "__main__":
    print(solution(['a','b','b','a','a','a','c','c'], 2)) # returns [1,2]
    print(solution([1,1,1,2,2,3], 2)) # returns [1,2]
    print(solution([1], 1)) # returns [1]
