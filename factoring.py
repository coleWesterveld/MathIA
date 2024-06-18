#there are 9592 primes from 2 - 100 000

# randomly pic two prime numbers from primes to 100k
# multiply
# run fermarts theorem to attmept to factor
# record and graph using matplotlib the number fo iterations taken to factor
# maybe cap iterations at like 1k or something
import random as r
import math
import matplotlib.pyplot as plt
import numpy as np

file = open(r"C:\Users\Cole\Desktop\RSA_math_IA\billion-primes.txt", 'r')

# .readlines() returns a list of strings of each line in the file
lines = file.readlines()
#print(len(lines))

cutoffs = [0]
cap = 1_000
count = 0
for x in lines:
    if int(x) < cap:
        count += 1
    else:
        cutoffs.append(count)
        count += 1
        #print(x)
        cap += 1_000
#cutoffs.append(len(lines))
print(cutoffs)

    #set cap to 1000000
    # go through each element adding one each time
    #once value is greater than cap then add sum to list and reset sum, increase cap by 1 mill


# close the file as we have all the information we need
file.close()

# generates product of two primes where each prime could be a prime from 2 to 100k
def gen_product(start, end):
    index1 = r.randint(start, end)
    index2 = r.randint(start, end)

    
    #print("primes:", lines[index1], lines[index2])
    #print(str(int(lines[index1])*int(lines[index2])), " is the product of: ", lines[index1], lines[index2])
    return int(lines[index1])*int(lines[index2])

#print(gen_product(0, 1000))

# returns number of iterations to find two factors of n using fermats factoring method
def fermat(n, cap):
    iterations = 0
    a = math.ceil(math.sqrt(n))
    while (iterations < cap):

        b = (a*a) - n

        if (math.sqrt(b) == int(math.sqrt(b))):
            b = math.sqrt(b)
            return iterations
            #   [iterations, (a+b), (a-b), (a+b)*(a-b)]
        a += 1
        iterations += 1

    return -1

# returns number of iterations taken to get factors of n
def factor_traditional(n):
    if n % 2 == 0:
        return 1
    for x in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if  n % x == 0:
            return ((x + 1) / 2)
        
#print("factor", factor_traditional(100))
#num = gen_product(0, 1000)

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
         
    return list
#print(factor(num, 1_000_000))
#print(num)

# 

# test 1000 batches of 1 million:
    # for each batch, test it 1000 times:
        # fermats theorem and classical factoring
        # average steps required for each one, store in a dictionary according to batch
fermat_means = {}
classical_means = {}

for x in range(999):
    if (x % 10 == 0):
        print(str((x)/10), "percent done")
    fermat_sum = 0
    classical_sum = 0
    sum_nums = 0
    cycles = 1000
    for y in range(cycles):
        num = gen_product(0, cutoffs[x + 1])
        sum_nums += num
    #print("factoring: ", type(factor_traditional(num)), " sum:", type(classical_sum), "number:", num)
        fermat_sum += fermat(num, 1_000_000)
        classical_sum += factor_traditional(num)
    sum_nums = round(sum_nums / cycles)
    fermat_means[sum_nums] = fermat_sum / cycles
    classical_means[sum_nums] = classical_sum / cycles
    #print("number to factor:", num)
    #print("fermat", fermat_sum / cycles)
    #print("classical:", classical_sum / cycles)

np.save('fermat4.npy', fermat_means) 
np.save('classical4.npy', classical_means) 
#for x in range(1_000):
    #
    # 
    
    # n = fermat(gen_product(), 1_000_000)
    # if ((n//2000)*2 in freq_dict.keys()):
    #     freq_dict[(n//2000)*2] += 1
    # else:
    #     freq_dict[(n//2000)*2] = 1

# freq_dict = dict(sorted(freq_dict.items()))
    
# Save



# Load
#read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()
#print(read_dictionary['hello']) # displays "world"

# if (-1 in freq_dict.keys()):
#     print(freq_dict[-1])
# #mylist = getList(freq_dict)
# #mylist.sort()
# #print(mylist[-1])
# #print(freq_dict)
print("fermat: ", fermat_means)
print("\n\n\n\n\n\n\n\n\n\n")
print("classical: ", classical_means)

plt.plot(range(999), classical_means.values(), label = "classical") 
plt.plot(range(999), fermat_means.values(), label = "fermat") 
plt.legend() 
plt.show()

# # for python 2.x:
# plt.bar(range(len(freq_dict)), freq_dict.values(), align='center')  # python 2.x
# plt.xticks(range(len(freq_dict)), freq_dict.keys())  # in python 2.x


