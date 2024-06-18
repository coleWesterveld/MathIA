import csv

import matplotlib.pyplot as plt
import numpy as np
classical_dictionary = np.load('classical4.npy',allow_pickle='TRUE').item()
fermat_dictionary = np.load('fermat4.npy',allow_pickle='TRUE').item()

with open('file5.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['number', 'fermat method', 'classical method'])
    for keys, value in fermat_dictionary.items():
        writer.writerow([keys, fermat_dictionary[keys], classical_dictionary[keys]])
    #print(keys)
    #for x in range(999):
        

# Output:
# The CSV file named 'file.csv' will be created and two rows of data will be written to it.



# Load

#print(read_dictionary['hello']) # displays "world"
#print(classical_dictionary)
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