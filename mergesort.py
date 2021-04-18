def mergesort(array):
    n = len(array)
    #for last level
    if(n==1):
        return array
    #split
    m = n//2 if (n%2==0) else n//2+1
    l = array[:m]
    r = array[m:]
    l_prime = mergesort(l)
    r_prime = mergesort(r)
    #merge
    new_arr=[]
    left_finger = 0
    right_finger = 0
    #two finger algorithm
    while True:
        if (left_finger>len(l_prime)-1):
            new_arr.extend(r_prime[right_finger:])
            break
        elif(right_finger>len(r_prime)-1):
            new_arr.extend(l_prime[left_finger:])
            break
        if(l_prime[left_finger]<r_prime[right_finger]):
            new_arr.append(l_prime[left_finger])
            left_finger = left_finger + 1
        else:
            new_arr.append(r_prime[right_finger])
            right_finger = right_finger + 1
    return new_arr

print(mergesort([3,1,2,4,5,7,9,8,2,4,3,100,50]))
