class Solution(object):
                
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i=0
        while(i<len(nums)):
            if nums[i]<=len(nums) and nums[i]>0 and nums[nums[i]-1]!=nums[i] and nums[i]!= i+1 :
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                continue
            i+=1
        print nums
        for i in range(0,len(nums)):
            if nums[i]!=i+1 :
                return i+1
        return len(nums)+1
            

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            
            ret = Solution().firstMissingPositive(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
