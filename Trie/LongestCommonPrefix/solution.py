def solution(strs):

    size = len(strs)

    # if size is 0, return empty string
    if (size == 0):
        return ""

    if (size == 1):
        return strs[0]

    # sort the array of strings (will sort by both alphabetical and length!)
    strs.sort()

    # find the minimum length from
    # first and last string
    end = min(len(strs[0]), len(strs[size - 1]))

    # find the common prefix between
    # the first and last string
    i = 0
    while (i < end and strs[0][i] == strs[size - 1][i]):
        i += 1

    pre = strs[0][0: i]
    return pre


if __name__ == "__main__":
    print(solution(["dog","racecar","car"])) # Ans: ""
    print(solution(["fly", "flowery","owly","flighty"]))
    print(solution(["flower","flow","flight"])) # Ans: "fl"

