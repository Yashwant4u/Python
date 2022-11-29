#script should replace the keys with the values in a text file in the nested directories where keys and values are 
#present in a text file in a root directory


#script to get keys and values from a text file into a dictonary
with open("test.txt", "r") as file:
    rows = (line.rstrip('\n').split(' ') for line in file)
    print(rows)
    h1 = { row[0]:row[1] for row in rows }
    print(h1)


#script to replace all the keys with values in a nested directory

import os
for dname, dirs, files in os.walk("C:\\Users\\Yashwant_Ramalingapp\\yashwant"):
    for fname in files:
        fpath = os.path.join(dname, fname)
        if fpath.endswith(".txt"):
            with open(fpath,'r') as file:
                data = file.read()
                #print(data)
                for key in h1:
                    data = data.replace(key,h1[key])
            with open(fpath,'w') as file:
                file.write(data)

