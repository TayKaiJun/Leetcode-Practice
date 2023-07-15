def solution(arr, difference):
    """
    :type arr: List[int]
    :type difference: int
    :rtype: int
    """
    len_map = {}
    answer = 1

    for i in range(len(arr)):
        curr = arr[i]
        if curr - difference in len_map:
            len_map[curr] = len_map[curr-difference] + 1
        else:
            len_map[curr] = 1
        answer = max(len_map[curr], answer)

    return answer



if __name__ == "__main__":

    print(str(solution([1,2,3,4], 1))) # expect 4
    print(str(solution([1,3,5,7], 1))) # expect 1
    print(str(solution([1,5,7,8,5,3,4,2,1], -2))) # expect 4

    #### this is the timeout case

    # test_file = open("test_case.txt", "r")
    # test_case = test_file.readline()
    # diff = int(test_file.readline())
    # data_string = test_case.split(",")
    # data = [eval(i) for i in data_string]
    # # print(str(solution(data, diff))) # insert input in the quotes
    # test_file.close()
