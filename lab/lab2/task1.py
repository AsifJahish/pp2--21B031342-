
def minsum_maxsum(num):
    minSum= sum(num)- max(num)
    MaxSum= sum(num)-min(num)
    return minSum, MaxSum

minSum, maxSum = minsum_maxsum([1,3,5,7,9])
print(f"Minimum sum is {minSum}\nMaximum sum is {maxSum}")