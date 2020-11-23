def findMedianSortedArrays(nums1, nums2):
    # not O(log(m+n))
    res = sorted(nums1 + nums2)
    if(len(res) % 2):
        return res[len(res) // 2]
    else:
        return (res[(len(res) // 2) - 1] + res[(len(res) // 2)]) / 2

# to get a handmade O(log(m+n)) solution:
#   let nums1 shorter than nums2
#   if med1 < med2, med1+ and med2-
#   else med1- and med2 +
#   until result (many ways to check)
#   use bisection (step based on nums) to get log O
