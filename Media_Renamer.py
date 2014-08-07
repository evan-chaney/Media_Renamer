#Evan Chaney
#August 6, 2014
__author__ = 'Evan Chaney'

import os
from string import punctuation

class media:
        def __init__(self,name,number,date,fileExt):
            self.n=number
            self.name=name
            self.date=date
            self.ext=fileExt

#Maybe add different functions for different media types?

#Function to decide what main delimiter is, although it most likely will be a period.
def delimFind(s):
    l=[]
    for char in s:
        if char in punctuation:
            l.append(char)
    return max(set(l),key=l.count)

#Iterate through all the files in a directory and add them to the list of files if they have an acceptable file extension
filesinit=os.listdir('.')
files=[]
acceptedTypes=['.mp4','.mkv','.m4v','.avi']
for f in filesinit:
    if f.lower()[-4:] in acceptedTypes:
        files.append(f)

finishedFiles=[]

for f in files:
    delim=delimFind(f)
    #find name
    #find episode number
    #find date
    #dinf file extension
    fExt=f.lower()[-4:]
    #Add file object to list of finished files

#Add a thing that tries to figure out if it's a tv show or movie buy looking for E## or EP##
