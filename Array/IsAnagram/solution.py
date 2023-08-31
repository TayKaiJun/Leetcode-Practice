def solution(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
        
    letters = {}

    for l in s:
        letters[l] = 1 if l not in letters else letters[l] + 1

    for l in t:
        if l not in letters:
            return False
        letters[l] -= 1
        if letters[l] < 0:
            return False
    
    return True

if __name__ == "__main__":
    print(solution("anagram", "nagaram")) # insert input in the quotes
