import re

def solution(s):
    # cleanString = re.sub("[^a-zA-Z\d]", "", s).lower()
    # n = len(cleanString)
    # if n == 1:
    #     return False

    # for i in range(n//2):
    #     if not cleanString[i] == cleanString[n-1-i]:
    #         return False
    # return True
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        
        if not s[left].lower() == s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    
    return True


if __name__ == "__main__":
    print(solution("A man, a plan, a canal: Panama")) # true
    print(solution("race a car")) # false
    print(solution(" ")) # true
    print(solution("0P")) # false
