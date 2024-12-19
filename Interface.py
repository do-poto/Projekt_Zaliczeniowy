import FileCrawler
import IMGClassification
import WebCrawler

#global variables
#menu strings
#main menu string bloc
Starting_Statement = ("###############################################\n"
                      "Which command would you like to run: \n"
                      "-----------------------------------------------\n"
                      "[1] Web Crawler \n"
                      "[2] Search in file \n"
                      "[3] Image classificator \n"
                      "[q] Close the program \n")
#Invalid input str
Invalid_Input_Str = "This is not a valid input please try again \n"

#other
#for empty return statements
x = ""

def Starting_Menu():
    global x
    print(Starting_Statement)
    #User input
    Starting_Input = str(input())
    if(Starting_Input == "1"):
        # run web crawler
        WebCrawler.Run_WebCrawler()
        # ask if to run again
        Run_Again_Menu(WebCrawler.Run_WebCrawler)
    elif(Starting_Input == "2"):
        #run file crawler
        FileCrawler.Run_Search_In_File()
        #ask if to run again
        Run_Again_Menu(FileCrawler.Run_Search_In_File)
    elif(Starting_Input == "3"):
        #run image classifier
        IMGClassification.Run_IMG_Classification()
        # ask if to run again
        Run_Again_Menu(IMGClassification.Run_IMG_Classification)
    elif(Starting_Input == "q"):
        #close program
        print("Program Closed")
        quit()
    else:
        #invalid input
        print(Invalid_Input_Str)
        Starting_Menu()
    return x

def Run_Again_Menu(Repeated_Method):
    global x

    print("Would you like to run the program again? (y/n)")
    Run_Again_Input = str(input())
    if(Run_Again_Input == "y"):
        #run function again
        Repeated_Method()
        Run_Again_Menu(Repeated_Method)
    elif(Run_Again_Input == "n"):
        #call the other menu
        Quit_To_Main_Menu()
    else:
        #invalid input
        print(Invalid_Input_Str)
        Run_Again_Menu(Repeated_Method)
    return x

def Quit_To_Main_Menu():
    global x
    print("Would you like to return to main menu? (y/n)")
    Quit_To_Main_Input = str(input())
    if(Quit_To_Main_Input == "y"):
        Starting_Menu()
    elif(Quit_To_Main_Input == "n"):
        #close program
        print("Closing Program")
        quit()
    else:
        #invalid input
        print(Invalid_Input_Str)
        Quit_To_Main_Menu()
    return x

Starting_Menu()