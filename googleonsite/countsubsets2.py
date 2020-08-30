class Solution():
    def countsubsets(self,nums,k):
        sum = 0
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i-1]:
                continue
            smaller = self.smaller(nums[:i],nums[i])
            greater = self.greater(nums[i+1:],nums[i])
            print(nums[:i],nums[i],smaller,greater)
            sum +=smaller*greater
        return sum

    def smaller(self,nums,a):
        
        nums.sort()
        # print(a,nums)
        l,r = 0,len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]>=a:
                r=mid
            else:
                l= mid+1
        
        if nums[l]==a:
            return l
        else: return l+1
    def greater(self,nums,a):
        nums.sort()
        # print(a,nums)
        l,r = 0,len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]>a:
                r=mid
            else:
                l= mid+1
        return len(nums)-l
    def pivot(self,arr,low,high):
        i = low-1
        pivot = arr[high]
        for j in range(low,high):
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    def quicksort(self,arr,low,high):
        if low <high:
            pi = self.pivot(arr,low,high)
            self.quicksort(arr,low,pi-1)
            self.quicksort(arr,pi+1,high)
        return arr
a = Solution()
nums = [1,7,9,3,3,4,6]
n = 3
print(a.quicksort(nums,0,6))
# print(a.smaller([1, 2, 2], 3))

        