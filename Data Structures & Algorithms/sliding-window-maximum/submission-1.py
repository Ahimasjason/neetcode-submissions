class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = []
        for i in range(k):
            while q and q[-1][1] < nums[i]:
                q.pop()
            q.append((i, nums[i]))

        rv = [q[0][1]]

        for i in range(k, len(nums)):

            # we already have k iterms
            # check if the 0 item falls into the range
            max_item = q[0]
            if (i - max_item[0]) >= k:
                # remove that item
                q.pop(0)

            while q and q[-1][1] < nums[i]:
                q.pop()

            q.append((i, nums[i]))
            rv.append(q[0][1])

        return rv


        