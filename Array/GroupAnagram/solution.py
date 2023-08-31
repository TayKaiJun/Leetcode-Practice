from collections import defaultdict

def solution(strs):
    answer = defaultdict(list)
    for s in strs:
        new_s = str(sorted(s))
        answer[new_s].append(s)
    return list(answer.values())


if __name__ == "__main__":
    print(solution(["anagram", "nagaram", "ana"]))                    # returns [["anagram","nagaram"], ["ana"]]
    print(solution(["eat","tea","tan","ate","nat","bat"]))      # returns [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    print(solution([""]))                                       # returns [[""]]
    print(solution(["a"]))                                      # returns [["a"]]