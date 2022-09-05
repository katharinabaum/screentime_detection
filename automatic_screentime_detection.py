import easyocr
import os
import numpy
import openpyxl
import csv

os.chdir("/Users/username/folderwithimagesandcsv")

filenames = os.listdir("/Users/username/Desktop/folderwithjustimages")

filenames.sort()

file = open("/Users/username/folderwithimagesandcsv/tescsvfile.csv", 'w')

writer = csv.writer(file)

reader = easyocr.Reader(["en"])

for x in filenames: 

    result = reader.readtext(x, detail = 0, blocklist = "Z")

    if "Social" in result:
        index1 = result.index("Social") + 2
    elif "Social Networking" in result:
        index1 = result.index("Social Networking") + 2
    elif "Networking" in result:
        index1 = result.index("Networking") + 2    
    else: 
        index1 = 0

    if "Other" in result:
        index2 = result.index("Other") + 2
    else: 
        index2 = 0

    if "Finance" in result:
        index3 = result.index("Finance") + 2
    elif "Productivity & Finance" in result:
        index3 = result.index("Productivity & Finance") + 2
    elif "Productivity" in result: 
        index3 = result.index("Productivity") + 2
    else: 
        index3 = 0

    if "Travel" in result:
        index4 = result.index("Travel") + 2
    else: 
        index4 = 0

    if "Education" in result:
        index5 = result.index("Education") + 2
    else:
        index5 = 0

    if "Shopping & Food" in result: 
        index6 = result.index("Shopping & Food") + 2
    elif "Food" in result: 
        index6 = result.index("Food") + 2    
    else:
        index6 = 0

    if "Creativity" in result: 
        index7 = result.index("Creativity") + 2
    else: 
        index7 = 0

    if "Entertainment" in result:
        index8 = result.index("Entertainment") + 2
    else: 
        index8 = 0

    if "Information & Reading" in result:
        index9 = result.index("Information & Reading") + 2
    elif "Reading & Reference" in result:
        index9 = result.index("Reading & Reference") + 2
    elif "Reference" in result:
        index9 = result.index("Reference") + 2
    else: 
        index9 = 0

    if "Utilities" in result:
        index10 = result.index("Utilities") + 2
    else: 
        index10 = 0

    if "Health & Fitness" in result:
        index11 = result.index("Health & Fitness") + 2
    elif "Fitness" in result:
        index11 = result.index("Fitness") + 2
    else:index11 = 0

    if "Games" in result: 
        index12 = result.index("Games") + 2
    else: 
        index12 = 0 

    indeces = [index1, index2, index3, index4, index5, index6, index7, index8, index9, index10, index11, index12]

    print(indeces)

    result.append("NA")

    result.insert(0,"NA")

    print(result)

    res2 = numpy.array(result)

    times = res2[indeces]

    lst = list(times)

    lst.append(x)

    lst = [l.replace('T', '1') for l in lst]

    lst = [l.replace('I', '1') for l in lst]

    lst = [l.replace('S', '5') for l in lst]

    lst = [l.replace('O', '0') for l in lst]

    writer.writerow(lst)