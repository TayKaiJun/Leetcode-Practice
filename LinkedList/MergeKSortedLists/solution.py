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

        
        print(min_heap)


def linkedListGenerator(lists):
    result = []
    for l in lists:
        head = ListNode(l[0])
        result.append(head)
        for i in range(1, len(l)):
            head.next = ListNode(l[i])
            head = head.next
    
    return result

if __name__ == "__main__":
    lists = linkedListGenerator([[1,4,5],[1,3,4],[2,6]])
    print(Solution.mergeKLists(lists)) # insert input in the quotes
