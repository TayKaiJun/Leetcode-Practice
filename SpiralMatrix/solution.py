def solution(matrix):
    result = []
    if len(matrix) == 1:
        return matrix[0]
    elif len(matrix) == 2:
        return matrix[0] + matrix[1][::-1]
    else:
        result += matrix.pop(0)
        last_col = []
        i = 0
        while i < len(matrix)-1 :
            if len(matrix[i]) > 0:
                result.append(matrix[i].pop(-1))
            if len(matrix[i]) > 0:
                last_col.append(matrix[i].pop(0))
            if len(matrix[i]) == 0:
                matrix.pop(i)
                i -= 1
            i += 1
        result += matrix.pop(-1)[::-1]
        result += last_col[::-1]
        if len(matrix) > 0:
            result += solution(matrix)
    return result


if __name__ == "__main__":
    print(solution([[1,2],[3,4]])) # [1,2,4,3]
    print(solution([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
    print(solution([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
    print(solution([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])) # [1,2,3,4,5,10,9,8,7,6]
    print(solution([[1,2,3,4,5,6,7,8,9,10]])) # [1,2,3,4,5,6,7,8,9,10]
    print(solution([[1,2],[3,4],[5,6],[7,8],[9,10]])) # [1,2,4,6,8,10,9,7,5,3]