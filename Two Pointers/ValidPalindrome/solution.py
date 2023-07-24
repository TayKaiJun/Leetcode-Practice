import re

def solution(s):
    cleanString = re.sub("[^a-zA-Z\d]", "", s).lower()
    n = len(cleanString)
    if n == 1:
        return False

    for i in range(n//2):
        if not cleanString[i] == cleanString[n-1-i]:
            return False
    return True


if __name__ == "__main__":
    print(solution("A man, a plan, a canal: Panama")) # true
    print(solution("race a car")) # false
    print(solution(" ")) # true
    print(solution("0P")) # true
