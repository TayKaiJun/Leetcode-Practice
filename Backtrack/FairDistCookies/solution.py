class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0] * k
        mindist = float('inf')

        list_len = len(cookies)

        def backtrack(i):
            nonlocal mindist, dist

            if i == list_len:
                mindist = min(mindist, max(dist))
                return
            
            if mindist <= max(dist):
                return
            
            for j in range(k):
                dist[j] += cookies[i]
                backtrack(i+1)
                dist[j] -= cookies[i]


        backtrack(0)
        return mindist