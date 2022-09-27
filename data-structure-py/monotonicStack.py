'''

'''

class monotonicStack:
    
    def nextGreater_right_idx(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] < arr[idx]:
                stack.pop()
            if not stack:
                #no greater element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans
                
    def nextGreater_left_idx(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] <= arr[idx]:
                stack.pop()
            if not stack:
                #no greater element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans 
                
    def nextSmaller_right_idx(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] > arr[idx]:
                stack.pop()
            if not stack:
                #no smaller element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans 
        
    def nextSmaller_left_idx(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[idx]:
                stack.pop()
            if not stack:
                #no smaller element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans 


def subArrayRanges(nums):
    mon = monotonicStack()
    
    # for each element, check in how many sub-arrays arrays, it can be max
    # find the prev and next greater element

    # for each element, check in how many sub-arrays arrays, it can be min
    # find the prev and next smaller element
    
    nse_l = mon.nextSmaller_left_idx(nums)
    nse_r = mon.nextSmaller_right_idx(nums)
    nge_l = mon.nextGreater_left_idx(nums)
    nge_r = mon.nextGreater_right_idx(nums)
    
    ans = 0
    
    for idx in range(len(nums)):
        smaller_left, smaller_right = nse_l[idx], nse_r[idx]
        greater_left, greater_right = nge_l[idx], nge_r[idx]
        
        if smaller_right == -1:
            smaller_right = len(nums)
        if greater_right == -1:
            greater_right = len(nums)
        
        min_val = (idx - smaller_left) * (smaller_right - idx) * nums[idx]
        max_val = (idx - greater_left) * (greater_right - idx) * nums[idx]
        
        ans += (max_val - min_val)
    return ans
        
