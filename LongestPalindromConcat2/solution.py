def solution(words):
    seen = {}
    for word in words:
        if word in seen:
            seen[word][0] += 1
        else:
            seen[word] = [1, False]

        if word[::-1] in seen:
            seen[word][1] = True
            seen[word[::-1]][1] = True

    pairs = 0
    identical = False
    for word in seen:
        invertedWord = word[::-1]
        if invertedWord == word:
            if not identical and seen[word][0] % 2 == 1:
                pairs += 1
                seen[word][0] -= 1
                identical = True
            pairs += seen[word][0] if seen[word][0] % 2 == 0 else seen[word][0]-1

        elif invertedWord in seen and seen[invertedWord][1]:
            pairs += 2 * min(seen[word][0], seen[invertedWord][0])
            seen[word][1] = False
            seen[invertedWord] = False

    return pairs * 2


if __name__ == "__main__":
    print(solution(["cc","ll","xx"])) # 2
    print(solution(["ab","ty","yt","lc","cl","ab"])) # 8
    print(solution(["lc","cl","gg"])) # 6
    print(solution(["lc","cl","cl", "cl", "lc"])) # 8
    print(solution(["aa","aa","aa", "cl", "jk"])) # 6
