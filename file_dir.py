import os
import datetime
import glob
​

#code that given that path, will tell you which file is newest. So, you have a directory called test with 3 files, let’s call them test1.txt, test2.txt and test3.txt.
#lets say that test2.txt was the one most recently updated.  Looking for Python to detect that this is the newest from those 3 in the directory and give the full path to it.


def modification_date(filename):
​
    t = os.path.getmtime(filename)
​
    return datetime.datetime.fromtimestamp(t)
​
def MostRecentModified(path):
    fileNames = glob.glob(path)
​
    fileName2lastModified = {}
​
    for file in fileNames:
        fileName2lastModified[file] = modification_date(file)
​
    mostRecentDate = modification_date(fileNames[0])
    mostRecentName = ""
​
    for key in fileName2lastModified:
        if fileName2lastModified[key] > mostRecentDate:
            mostRecentDate = fileName2lastModified[key]
            mostRecentName = key
​
    return mostRecentName, mostRecentDate
​
print(MostRecentModified("*.txt"))