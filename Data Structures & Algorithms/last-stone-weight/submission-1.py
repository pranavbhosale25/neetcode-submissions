import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq.heapify(-1 * stones)
        stones = [-s for s in stones]
        heapq.heapify(stones)
        # print(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            # print("got ", s1, " and ", s2)

            if s1 != s2:
                # print("inserting ",s1-s2 )
                heapq.heappush(stones,s1-s2)
            
        if len(stones) == 1:
            return -stones[0]

        return 0




        