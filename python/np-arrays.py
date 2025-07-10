import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    mList = list(map(float,arr))
    return numpy.flip(numpy.array(mList))
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)