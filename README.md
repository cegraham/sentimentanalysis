# sentimentanalysis
cisc367 proj on sentiment analysis of slack conversation

Scripts.py: Script that first finds all of the URL's suggested in the CSV file of python data from Slack conversations. Then, once it finds the url, it removes the beginning (http://, https://, www., etc.) and removes the end (.com, .edu, .gov, etc.) leaving us with an output csv file of only the domain names for each of the three years of python chat data. The second part of the script uses the csv files of chat data and finds the response given right after a URL suggestion. These responses are then sent to an output csv file where we store the responses to run NLTK sentiment analysis using our 2019NLTK scrit. 

NLTK2019.ipynb: This script uses NLTK to take in a CSV file that has all of the responses a user provided when they were given a URL. It then takes these responses, tokenizes them and runs a sentiment analysis. Polarity is calcualted and positive, negative or neutral is assigned to each response. This was done for all three years of data.

Output: The output files contain the domain count, the respoense to the URL, and the sentiment analysis of that response 

Input: The 2017, 2018, and 2019 data sets we analyzed.


