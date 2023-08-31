from collections import defaultdict

def isAnagram(letters, t):
    newTemplate = {}
    result = True
    for l in t:
        newTemplate[l] = 1 if l not in newTemplate else newTemplate[l] + 1
        if l not in letters:
            result = False
        else:
            letters[l] -= 1
            if letters[l] < 0:
                result = False
    
    return (result, newTemplate)


def solution(strs):
    groupbylen = defaultdict(list)
    for string in strs:
        groupbylen[len(string)].append(string)
    # print("### groupbylen ###")
    # print(groupbylen)
    
    def subGroupings(strings):
        first = {}
        for l in strings[0]:
            first[l] = 1 if l not in first else first[l] + 1
        templates = [first]
        results = [[strings[0]]]
        for string in strings[1:]:
            for i in range(len(templates)):
                curr_template = templates[i].copy()
                result, newTemplate = isAnagram(curr_template, string)
                if result:
                    results[i].append(string)
                    break
                elif i == len(templates) - 1:
                    templates.append(newTemplate)
                    results.append([string])
        # print("### results ###")
        # print(results)
        return results
    
    answer = []
    for groupAnagramsOfSameLen in groupbylen.values():
        answer += [group for group in subGroupings(groupAnagramsOfSameLen)]
    # print("### answers ###")
    
    return answer


if __name__ == "__main__":
    # print("----------------------")
    # print(solution(["anagram", "nagaram", "ana"]))                     # returns [["anagram","nagaram"], ["ana"]]
    print("----------------------")
    print(solution(["eat","tea","tan","ate","nat","bat"]))      # returns [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    print("----------------------")
    print(solution([""]))                                       # returns [[""]]
    print("----------------------")
    print(solution(["a"]))                                      # returns [["a"]]