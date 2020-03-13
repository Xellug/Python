inputNums = [10, 140, 45, 55, 245, 350, 250, 10, 10, 10, 260, 8, 5, 5, 99, 109, 441, 1, 0, 1, 989]

out = []
inLen = len(inputNums)

def main():
    assert (inLen < 10001), "The maximum lenght was exceeded"
    iter = 0
    
    while iter < inLen:
        i = iter + 8

        while i < inLen:
            assert (inputNums[iter] < 1001)  and (inputNums[i] < 1001), "The maximum value was exceeded"
            k = inputNums[iter] * inputNums[i]
            out.append(k)
            i += 1
        iter += 1
        
def maximum():
    i = 0
    m = 1
    while m < len(out):
        if out[m] > out[i]:
            i = m 
            m = i + 1 
        else:
            m += 1
    return out[i]

try:
    main()
    print(maximum())
except:
    raise


