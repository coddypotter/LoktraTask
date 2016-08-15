#TASK 2
#Web Crawler for Shopping.com

#imports
from requests.exceptions import ConnectionError
import requests
import sys

#function to fetch the web page contents
def crawlUrl(url):
    htmlCode = requests.get(url).text #get the contents of the passed URL in text
    count = htmlCode.count('gridItemTop') #count the number of div tags with ID gridItemTop
    return count #return the count

valid_flag = True 

#Handling command line inputs 
try:
    if(sys.argv[1]):
        urlConstruct = "http://www.shopping.com/products?KW="+sys.argv[1]
    elif(sys.argv[2]):
        urlConstruct = "http://www.shopping.com/products~"+sys.argv[2]+"?KW="+sys.argv[1]
    else:
        valid_flag = False
        urlConstruct = "\nInvalid Inputs \nPlease provide input in the following format\n\n>task2.py <keyword>\n>task2.py <keyword> <page number>"

    if(valid_flag):
        crawl = crawlUrl("http://www.shopping.com/products?KW=1")
        print("Number of results for the specified keyword are "+str(crawl))
    else:
        print(urlConstruct)
except(IndexError): #handle input via cmd
    print("\nInvalid Inputs \nPlease provide input in the following format\n\n>task2.py <keyword>\n>task2.py <keyword> <page number>")
except ConnectionError as e: #handle network errors
    print("You need an active internet connection to crawl. Please connect to the internet and try again later.")
