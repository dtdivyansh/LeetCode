class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        while(num>0):
            arr.append(num%10)
            num = num//10
        arr.sort()
        return int( str(arr[0])+str(arr[3]) ) + int(str(arr[1])+str(arr[2]))
