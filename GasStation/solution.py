def solution(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    
    #####
    # Scenario for failure: If the sum of gas is less than the sum of cost, then there is no possible solution.
    # Greedy solution: Start from the position after the last station where the difference between gas and cost is the largest.
    # Idea is that if that station is the last, we can gather as much gas as possible before that station.
    #####
    
    if sum(gas) < sum(cost):
        return -1
    
    diff_list = []
    next_possible = []
    current_sum = 0
    for i in range(len(gas)):
        gas_diff = gas[i] - cost[i]
        diff_list.append(gas_diff)
        if current_sum + gas_diff <= 0:
            next_possible.append(i+1)
            current_sum = 0
        else:
            current_sum += gas_diff
    
    print(diff_list)
    
    local_max = float('-inf')
    last_index = 0
    for index in next_possible:
        if index < len(gas) and diff_list[index] > local_max:
            local_max = diff_list[index]
            last_index = index
        else:
            if diff_list[0] > local_max:
                local_max = diff_list[0]
                last_index = 0
    
    return last_index


if __name__ == "__main__":
    print(solution([1,2,3,4,5], [3,4,5,1,2]))   # return 3
    print(solution([2,3,4], [3,4,3]))           # return -1
    print(solution([5,8,2,8], [6,5,6,6]))       # return 3
    print(solution([5,1,2,3,4], [4,4,1,5,1]))       # return 4
    print(solution([1,1,10,1,1], [2,5,1,5,1]))       # return 2
    print(solution([5,1,2,3,4], [4,4,1,5,1]))       # return 4