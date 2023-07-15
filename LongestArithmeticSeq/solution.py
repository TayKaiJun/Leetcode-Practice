def solution(arr, difference):
    """
    :type arr: List[int]
    :type difference: int
    :rtype: int
    """
    subseqLen = [1] * len(arr)

    for i in range(len(arr)):
        next = arr[i] + difference
        for j in range(i, len(arr)):
            if arr[j] == next:
                subseqLen[j] = max(subseqLen[j], subseqLen[i]+1)
                break



    return max(subseqLen)



if __name__ == "__main__":

    print(str(solution([1,5,7,8,5,3,4,2,1], -2))) # expect 4

    #### this is the timeout case

    # test_file = open("test_case.txt", "r")
    # test_case = test_file.readline()
    # diff = int(test_file.readline())
    # data_string = test_case.split(",")
    # data = [eval(i) for i in data_string]
    # # print(str(solution(data, diff))) # insert input in the quotes
    # test_file.close()
