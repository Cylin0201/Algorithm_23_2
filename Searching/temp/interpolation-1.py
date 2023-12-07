import math
def interpolationSearch(S, x):
    low = 0
    high = len(S) - 1
    location = -1
    
    if (S[low] <= x and x <= S[high]):
        while (low <= high and location == -1):
            if (x < S[low] or x > S[high]):
                break
            denominator = S[high] - S[low]
            if (denominator == 0):
                mid = low
            else:
                mid = low + math.floor(((x - S[low]) * (high - low)) / denominator)

            if (x == S[mid]):
                location = mid
            elif (x < S[mid]):
                high = mid - 1
            else:
                low = mid + 1
    return location
    
S = [1,3,4,7,8,11,13,15,16,20,22,25,29,30,33,36,37,39,41,43,45,48]
x = 11
print(S)
print(f'Location of {x:d} is {interpolationSearch(S,x):d}th')

##########################################################################
##########################################################################

import math
def robustInterpolationSearch(S, x):
    low = 0
    high = len(S) - 1
    location = -1 
    denominator = S[high] - S[low]
    if (denominator == 0):
        mid = low
    else:
        mid = low + math.floor(((x - S[low]) * (high - low)) / denominator)
    
    if (S[low] <= x and x <= S[high]):
        while (low <= high and location == -1):
            if (x < S[low] or x > S[high]):
                break
            gap = math.floor(math.sqrt(high - low + 1))
            
            denominator = S[high] - S[low]
            if (denominator == 0):
                mid = low
            else:
                mid = min(high - gap, max(mid, low + gap))

            if (x == S[mid]):
                location = mid
            elif (x < S[mid]):
                high = mid - 1
            else:
                low = mid + 1
    return location
    
S = [1,3,4,7,8,11,13,15,16,20,22,25,29,30,33,36,37,39,41,43,45,48]
x = 11

print(S)
print(f'Location of {x:d} is {robustInterpolationSearch(S,x):d}th')


##########################################################################
##########################################################################


import time
import random

S = list(range(10000))
x = random.choice(S)
S.append(100000000)

start = time.time()
print(f'Location of {x:d} is {interpolationSearch(S,x):d}th. Process time is {round(time.time()-start, 6)}')

start = time.time()
print(f'Location of {x:d} is {robustInterpolationSearch(S,x):d}th. Process time is {round(time.time()-start, 6)}')