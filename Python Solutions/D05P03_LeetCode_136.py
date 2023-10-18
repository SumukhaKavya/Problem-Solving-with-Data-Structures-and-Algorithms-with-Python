#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

