def minSteps( d):
        # code he#User function Template for python3


        i = 0
        sum = 0
        while sum < d:
            i += 1
            sum +=i
        if sum == d:
            return i
        else:
            while (sum - d) % 2 != 0:
                i += 1
                sum += i
            return i
print(minSteps(2))