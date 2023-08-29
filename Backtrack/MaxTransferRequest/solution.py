def solution(n, requests):
    buildings = [0] * k
    total = 0
    length = len(requests)

    def backtrack(req, i=0, dist=0):
        nonlocal buildings, total
        
        if req < length:
            buildings[requests[req][0]] -= 1
            buildings[requests[req][1]] += 1
            backtrack(req+1, i, dist+1)
        


    backtrack(0)


if __name__ == "__main__":
    print(solution(5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))   # 5
    print(solution(3, [[0,0],[1,2],[2,1]]))                     # 3
    print(solution(4, [[0,3],[3,1],[1,2],[2,0]]))               # 4
