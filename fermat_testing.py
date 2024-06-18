import math
import random as r
import decimal
# file = open(r"C:\Users\Cole\Desktop\RSA_math_IA\billion-primes.txt", 'r')

# # .readlines() returns a list of strings of each line in the file
# lines = file.readlines()
# #print(len(lines))

# cutoffs = [0]
# cap = 1_000
# count = 0
# for x in lines:
#     if int(x) < cap:
#         count += 1
#     else:
#         cutoffs.append(count)
#         count += 1
#         #print(x)
#         cap += 1_000
# #cutoffs.append(len(lines))
# #print(cutoffs)

#     #set cap to 1000000
#     # go through each element adding one each time
#     #once value is greater than cap then add sum to list and reset sum, increase cap by 1 mill


# # close the file as we have all the information we need
# file.close()

# # generates product of two primes where each prime could be a prime from 2 to 100k
# def gen_product(start, end):
#     index1 = r.randint(start, end)
#     index2 = r.randint(start, end)
#     return int(lines[index1])*int(lines[index2])

# returns number of iterations to find two factors of n using fermats factoring method
def fermat(n, cap):
    iterations = 0
    n = decimal.Decimal(n)
    a = math.ceil(n.sqrt())
    a = decimal.Decimal(a)
    while (iterations < cap):

        b = a*a - n
        if b < 0:
            print (b)
        #if (math.sqrt(b) == int(math.sqrt(b))):
        if (b.sqrt() == int(b.sqrt())):
            b = b.sqrt()
            return [iterations, (a+b), (a-b), (a+b)*(a-b)]
            #   [iterations, (a+b), (a-b), (a+b)*(a-b)]
        a += 1
        iterations += 1

    return -1

#num = gen_product(0, cutoffs[101])
num = 13195650934101362003
print(fermat(num, 1_000_000))