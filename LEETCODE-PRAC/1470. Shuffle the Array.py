class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:int(len(nums)/2)]
        nums2 = nums[int(len(nums)/2):]
        nums3 = []
        for _ in range(int(len(nums)/2)):
            nums3.append(nums1[_])
            nums3.append(nums2[_])
        return nums3