# -*- coding: utf-8 -*-
from pypdf import PdfReader

#initialized global variables
PDF_Name : str
Word_Search : str
Word_Location = []
My_Reader : PdfReader

#functions
#read the described file
def Read_File():
    global My_Reader
    try:
        # get file name/localisation
        PDF_Name = str(input("Write file name or its localisation: ")) + ".pdf"
        # read file
        My_Reader = PdfReader(PDF_Name)
        return My_Reader
    except Exception as e:
        #exception for file error
        print("An error occured while reading the file: " + str(e))
        Read_File()
    return My_Reader

#find word in file and number of occurrences
def Word_Occurrence(My_Reader: PdfReader):
    #local vars
    Word_Count = 0
    Output_Line = ""

    #user input and info
    Word_Search = str(input("Enter a word you want to search for: "))
    print("Searching...")

    #occurance counter and pages
    for i in range(0, len(My_Reader.pages)):
        if Word_Search.lower() in My_Reader.pages[i].extract_text().lower():
            #add page location and increase word count
            Word_Location.append(i+1)
            Word_Count += 1

    #return statement
    if Word_Count == 0:
        #no occurrence
        return "The word does not occur in pdf or could not be found."
    else:
        #string line output creation if there is occurrence
        for i in range(0, len(Word_Location)):
            Output_Line += str(Word_Location[i]) + ", "
        return "Word occurs in text " + str(Word_Count) + " times on pages: " + Output_Line

def Run_Search_In_File():
    print(Word_Occurrence(Read_File()))