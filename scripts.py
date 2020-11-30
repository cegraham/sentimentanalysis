from textblob import TextBlob
import csv
import collections
import nltk
from nltk import word_tokenize

domains = []
starting_index = 0
ending_index = 0
flag = False
nextline = False
nextlines = []
thisline = []
sentiments = []

#nltk.download()

#Opens and reads the 2019 file, the script and files need to be in the same place on computer
with open('2017PythonData.csv', 'r') as csv_file:
    #This goes through the csv_file line by line and checks for URLs. If found it drops the https:// and .com and returns just the domian name
    for line in csv_file:
        if (nextline == True) :
            nextlines.append(line)
            nextline = False
        #We are assuming that people use spaces properly, however some of our results hsow this isn't always the case, so this will be a limitaion to
        #acknowledge
        words = line.split(' ')
        for word in words:
            starting_index = word.find("https://")
            starting_index1 = word.find("http://")
            starting_index2 = word.find("www.")
            #Need to make it work for things like .org, .edu, .gov, and others
            if (word.find(".com") != -1) :
                ending_index = word.find(".com")
            elif (word.find(".org") != -1) :
                ending_index = word.find(".org")
            elif (word.find(".net") != -1) :
                ending_index = word.find(".net")
            elif (word.find(".edu") != -1) :
                ending_index = word.find(".edu")
            elif (word.find(".co") != -1) :
                ending_index = word.find(".co")
            elif (word.find(".gov") != -1) :
                ending_index = word.find(".gov")
            startflag = False
            endflag = False
            if (starting_index != -1 and starting_index2 != -1) :
                starting_index += 12
                startflag = True
            elif (starting_index1 != -1 and starting_index2 != -1) :
                starting_index += 11
                startflag = True
            elif (starting_index1 != -1) :
                starting_index += 7

                startflag = True
            elif(starting_index != -1) :
                starting_index += 8
                startflag = True
            elif(starting_index2 != -1) :
                starting_index += 5
                startflag = True
            if(ending_index != -1) :
                endflag = True
            domain = word[starting_index : ending_index]
            if ((startflag == True) and (endflag == True)) :
                domains.append(domain)
                thisline.append(line)
                nextline = True
           
#Counts
Counter = collections.Counter(domains)


#This writes a csvfile-
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Thread ID", "Domains", "Count"])
    #Changing the range changes the amount of domains outputted in the output csvfile
    for i in range(1, len(domains)):
        writer.writerow([i, domains[i], Counter.get(domains[i])])

# This does not output the same number of messages as domains. This is because there may be multipe URLs in a single message, however
# theres only 1 next message for all of the URLs and so it would only do 1 message for multiple URLs in a single message. Easy to prove just
# move the if statement into the innermost for loop, the for word in words one.
with open('output2.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Thread ID", "URL line"])
    #Changing the range changes the amount of domains outputted in the output csvfile
    for i in range(1, len(nextlines)):
        writer.writerow([i, thisline[i]])
 
