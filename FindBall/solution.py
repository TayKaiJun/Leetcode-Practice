def solution(input):
    num_balls = len(input[0])
    ball = [i for i in range(num_balls)]
    for row in input:
        for i in range(num_balls):
            curr_pos = ball[i]

            if curr_pos == -1:
                continue

            if curr_pos+row[curr_pos] < 0 or curr_pos+row[curr_pos] >= num_balls:
                # this directs the ball to the wall
                ball[i] = -1
            elif row[curr_pos] == 1 and curr_pos+1 < num_balls and row[curr_pos+1] == -1:
                # ball stuck in V on the right
                ball[i] = -1
            elif row[curr_pos] == -1 and curr_pos-1 > 0 and row[curr_pos-1] == 1:
                # ball stuck in V on the left
                ball[i] = -1
            else:
                ball[i] += row[curr_pos]

    return ball

if __name__ == "__main__":
    print(solution([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])) # [1, -1, -1, -1 ,-1]
    print(solution([[-1]]))
    print(solution([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
    print(solution([[1,1,1],[1,1,1],[1,1,1]]))