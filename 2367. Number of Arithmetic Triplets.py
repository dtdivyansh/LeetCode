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


# OPTIMISATION

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        first_dict = {}
        second_dict = {}

        for num in nums:
            count += second_dict.get(num, 0)
            second_dict[num + diff] = second_dict.get(num + diff, 0) + first_dict.get(num, 0)
            first_dict[num + diff] = first_dict.get(num + diff, 0) + 1

        return count
