import validators
import requests
from bs4 import BeautifulSoup

#initialized variables
URL_Queue = []
Length : int
My_URL : requests

#functions
#ask user for url
def Get_User_URL():
    global My_URL
    try:
        #ask for URL
        My_URL = requests.get(input("Paste the URL of the website: "))
        #does URL work
        if My_URL.status_code != 200:
            print("This URL does not work try another one.")
            Get_User_URL()
        return My_URL
    except Exception as e:
        # URL is not valid
        print("An error occured while getting the URL: " + str(e))
        Get_User_URL()
    return My_URL

#get urls from the website
def Find_Website_URLs(My_URL):
    global URL_Queue
    #convert response content into a html type with bs4
    Parsed_HTML = BeautifulSoup(My_URL.content, "html.parser")

    #find all links in the html content
    File_Extract = Parsed_HTML.select("a[href]")

    #search through content
    for File_Extract in File_Extract:
        New_URL = File_Extract["href"]
        #validate if it's an url and add to queue
        if validators.url(New_URL) == True:
            URL_Queue.append(New_URL)
    return URL_Queue

#print all links from queue
def Display_All_URLs(URL_Queue):
    Length = len(URL_Queue)
    while not bool(URL_Queue) == False:
        print(URL_Queue.pop())
    print("Number of URLs found: ", Length)

def Run_WebCrawler():
    Display_All_URLs(Find_Website_URLs(Get_User_URL()))