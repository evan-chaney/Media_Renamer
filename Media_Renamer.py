#Evan Chaney
#August 6, 2014
__author__ = 'Evan Chaney'

import os
from string import punctuation,letters

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

#Find name and episode number
def nameAndEpisodeFinder(s, delim):
    l=s.split(delim)
    eCharFound=False
    eCharValue=False
    eNumFound=False
    eNumValue=''
    for x in l:
        if str(x).lower().startswith('e') and len(x) <6 and l.index(x) >1:
            eCharFound=True
            eCharValue=x
            if len(x)>2 and str(x)[-1].isdigit() and str(x)[-2].isdigit():
                eNumFound=True
                eNumValue=x
    showName=''
    for x in l[:l.index(eCharValue)]:
        showName+=str(x)+' '
    showName=showName[:-1]
    if eCharValue==eNumValue:
        return (showName,eCharValue)
    else:
        return (showName,str(eCharValue)+' '+str(eNumValue))


#Find the date in a tv show episode
def datefinder(s,delim):
    l=s.split(delim)
    dateFound=False
    dateValue=''
    for x in l:
        if (len(x)==6) and (str(x).isdigit()):
            dateFound=True
            dateValue=x
        if not dateFound:
            for char in punctuation:
                x.strip(char)
            if (len(x)==6) and (str(x).isdigit()):
                dateFound=True
                dateValue=x
    if dateFound:
        return dateValue
    else:
        return False

#Iterate through all the files in a directory and add them to the list of files if they have an acceptable file extension
filesinit=os.listdir('.')
files=[]
acceptedTypes=['.mp4','.mkv','.m4v','.avi','.ass','.srt']
for f in filesinit:
    if f.lower()[-4:] in acceptedTypes:
        files.append(f)

finishedFiles=[]

#This is only for TV shows right now
for f in files:
    print f
    delim=delimFind(f)
    print "delim: "+str(delim)
    #find name
    showName=nameAndEpisodeFinder(f,delim)[0]
    #find episode number
    eNumber=nameAndEpisodeFinder(f,delim)[1]
    #find date
    eDate=datefinder(f,delim)
    #dinf file extension
    fExt=f.lower()[-4:]
    #Add file object to list of finished files

    print str(showName)+' '+str(eNumber)+' '+str(eDate)+str(fExt)
    #This is just for testing purposes
    raw_input("Press enter to continue")

#Add a thing that tries to figure out if it's a tv show or movie by looking for E## or EP##
#Change Episode naming so it's EP XX

