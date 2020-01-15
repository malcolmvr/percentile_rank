def percentRank(arr, value):

    for i in range(len(arr)):
        if (arr[i] == value):
            return i / (len(arr) - 1)

    for i in range(len(arr)):
        if (arr[i] < value and value < arr[i + 1]):
            x1 = arr[i]
            x2 = arr[i + 1]
            y1 = percentRank(arr, x1)
            y2 = percentRank(arr, x2)
            return (((x2 - value) * y1 + (value - x1) * y2)) / (x2 - x1)

    raise Exception('Out of bounds')
