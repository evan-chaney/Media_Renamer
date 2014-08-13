#Evan Chaney
#August 6, 2014
__author__ = 'Evan Chaney'

import os
from string import punctuation,letters

class media:
        def __init__(self,name,number,date,fileExt,mediaType):
            self.n=number
            self.name=name
            self.date=date
            self.ext=fileExt
            self.mediaType=mediaType

#Maybe add different functions for different media types?

#Function to decide what main delimiter is, although it most likely will be a period.
def delimFind(s):
    l=[]
    for char in s:
        if char in punctuation:
            l.append(char)
    return max(set(l),key=l.count)

def movieortv(s, delim):
    eFound=False
    yearFound=False
    for x in s.split(delim):
        for p in punctuation:
            x.strip(p)
        if str(x).isdigit() and len(x)==4:
            yearFound=True
        elif (str(x)[0].lower() =='e' or str(x)[:2].lower()=='ep')  and (str(x)[-3:].isdigit() or (len(x)<3)):
            eFound=True
    if yearFound and eFound:
        return "TV"
    elif eFound:
        return "TV"
    elif yearFound:
        return "Movie"
    else:
        return "TV"

#Find name and episode number
def nameAndEpisodeFinder(s, delim):
    l=s.split(delim)
    eCharValue=False
    eNumValue=''
    for x in l:
        if str(x).lower().startswith('e') and len(x) <6 and l.index(x) >1:
            eCharValue=x
            if len(x)>2 and str(x)[-1].isdigit() and str(x)[-2].isdigit():
                eNumValue=x
    showName=''
    for x in l[:l.index(eCharValue)]:
        showName+=str(x)+' '
    showName=showName[:-1]
    if eCharValue==eNumValue:
        return (showName,eCharValue)
    else:
        return (showName,str(eCharValue)+' '+str(eNumValue))

#Find just the name and year (for movies)
def nameAndYear(s, delim):
    l=s.split(delim)
    yearValue=''
    movieName=''
    for x in l:
        if len(x)==4 and str(x).isdigit():
            yearValue=str(x)
    for x in l[:l.index(yearValue)]:
        movieName=movieName+str(x)+' '
    movieName=movieName[:-1]
    return (movieName, yearValue)



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



for f in files:
    print f
    delim=delimFind(f)
    print "delim: "+str(delim)
    #Decide media type
    mediaType=movieortv(f,delim)

    if mediaType=='TV':
        #find name
        showName=nameAndEpisodeFinder(f,delim)[0]
        #find episode number
        eNumber=nameAndEpisodeFinder(f,delim)[1]
        #find date
        eDate=datefinder(f,delim)
        #find file extension
        fExt=f.lower()[-4:]
        #Add file object to list of finished files
        finishedFiles.append(media(showName,eNumber,eDate,fExt,mediaType))

        print str(showName)+' EP '+str(eNumber)+' '+str(eDate)+str(fExt)
    else:
        #find name
        movieName=nameAndEpisodeFinder(f,delim)[0]
        #find episode number
        movieYear=nameAndEpisodeFinder(f,delim)[1]
        #find file extension
        fExt=f.lower()[-4:]
        #Add file object to list of finished files
        finishedFiles.append(media(showName,eNumber,eDate,fExt,mediaType))

        print str(movieName)+' ['+str(movieYear)+'] '+str(fExt)
    #This is just for testing purposes
    raw_input("Press enter to continue")


#Add something to skip a file if the delim is a space
#Change Episode naming so it's EP XX

