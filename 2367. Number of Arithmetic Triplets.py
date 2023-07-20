#https://leetcode.com/problems/number-of-arithmetic-triplets/description/

class Solution:

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dic = {}
        ans = 0
        for i in range(len(nums)):
            a = nums[i]
            b = a + diff
            c = b + diff

            if b in dic:
                if dic[b] > i:
                    if c in dic:
                        if dic[c] > dic[b]:
                            ans += 1
                        else:
                            continue
                    else:
                        try:
                            ind = nums.index(c)
                            dic[c] = ind
                            if dic[c] > dic[b]:
                                ans += 1
                            else:
                                continue
                        except:
                            continue
                else:
                    continue
            else:
                try:
                    ind = nums.index(b)
                    dic[b] = ind
                    if dic[b] > i:
                        if c in dic:
                            if dic[c] > dic[b]:
                                ans += 1
                            else:
                                continue
                        else:
                            try:
                                ind = nums.index(c)
                                dic[c] = ind
                                if dic[c] > dic[b]:
                                    ans += 1
                                else:
                                    continue
                            except:
                                continue
                    else:
                        continue
                except:
                    continue

        return ans
