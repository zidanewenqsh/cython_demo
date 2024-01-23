def compute_average(list numbers):
    cdef int sum = 0
    cdef int count = 0
    for number in numbers:
        sum += number
        count += 1
    return sum / count
