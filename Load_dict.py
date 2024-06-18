import matplotlib.pyplot as plt
import numpy as np


# Load
classical_dictionary = np.load('classical.npy',allow_pickle='TRUE').item()
fermat_dictionary = np.load('fermat.npy',allow_pickle='TRUE').item()
#print(read_dictionary['hello']) # displays "world"
print(classical_dictionary)
# if (-1 in freq_dict.keys()):
#     print(freq_dict[-1])
# #mylist = getList(freq_dict)
# #mylist.sort()
# #print(mylist[-1])
# #print(freq_dict)
plt.plot(range(999), fermat_dictionary.values(), label = "fermat") 
# plt.plot(range(999), fermat_means.values(), label = "classical") 
plt.legend() 
plt.show()