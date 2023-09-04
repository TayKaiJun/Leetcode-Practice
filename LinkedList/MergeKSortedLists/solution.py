import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        min_heap = []
        index = 0
        for ll in lists:
            if ll:
                heapq.heappush(min_heap, (ll.val, index, ll))
                index += 1
        
        if min_heap:
            res = heapq.heappop(min_heap)[2]
            head = res
            if res.next:
                heapq.heappush(min_heap, (res.next.val, index, res.next))
                index += 1
        else:
            return None
        
        while min_heap:
            res.next = heapq.heappop(min_heap)[2]
            res = res.next
            if res.next:
                heapq.heappush(min_heap, (res.next.val, index, res.next))
                index += 1
                
        # while head:
        #     print(head.val)
        #     head = head.next
        
        return head if head else None


def linkedListGenerator(lists):
    result = []
    for l in lists:
        if l:
            head = ListNode(l[0])
            result.append(head)
            for i in range(1, len(l)):
                head.next = ListNode(l[i])
                head = head.next
    
    return result

if __name__ == "__main__":
    lists1 = linkedListGenerator([[1,4,5],[1,3,4],[2,6]])
    sol = Solution()
    print(sol.mergeKLists(lists=lists1)) # insert input in the quotes
    print(sol.mergeKLists([[],[]]))
    print(sol.mergeKLists([]))
    lists2 = linkedListGenerator([[1,4,5],[]])
    print(sol.mergeKLists(lists=lists2))
