# character Hashing
# how many times does a charecter appear here?
def character_hashing(str, times):
    hashmap = {}
    for i in str:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for j in times:
        if j in hashmap:
            print(j, hashmap[j])


str = 'abbcdegcccfa'
times = 'abc'
res = character_hashing(str, times)
