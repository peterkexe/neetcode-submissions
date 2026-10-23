import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for n in nums:
            # Start of Sequence
            if n - 1 not in nums:
                length = 1
                while n + length in nums:
                    length += 1
                best = max(best, length)
        return best
        
        # # minheap solution: nlogn
        # if not nums:
        #     return 0
        # heap = nums
        # heapq.heapify(nums)

        # sequences: List[List[int]] = []

        # prev = heapq.heappop(heap)
        # seq = [prev]
        # # print('popped prev:', prev)
        # while heap:
        #     num = heapq.heappop(heap)
        #     # print('popped:', num)
        #     if num == prev:
        #         pass
        #     elif num == prev + 1:
        #         seq.append(num)
        #     else:
        #         sequences.append(seq)
        #         seq = [num]
        #     prev = num
        #     # print('sequences:', sequences, 'seq:', seq, 'prev:', prev)
        # sequences.append(seq)
        # ans = max(sequences, key=len)
        # # print(ans)
        # return len(ans)