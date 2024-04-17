def Frequency(arr, n):
    mp = {}
    max_freq = 0
    min_freq = 0
    max_key = 0
    min_key = 0
    for i in range(0, n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    print(mp)
    for key, value in mp.items():
        if value > max_freq:
            max_freq = value
            max_key = key
        elif value < max_freq:
            min_freq = value
        if value <= min_freq:
            min_freq = value
            min_key = key

    print(max_key, min_key)


if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    Frequency(arr, n)
