#ΒΑΖΑΙΟΣ ΣΤΥΛΙΑΝΟΣ Α.Μ.: 1054284
import os
import sys
from operator import itemgetter

#FUNCTIONS

def  cosineSim(doc1,doc2): #This function calculates the cosine similarity for each pair of documents-dictionaries
    global sim
    lend1=0
    lend2=0
    sum=0
    for word in wordArray:
        multiply = doc1[word]*doc2[word]
        sum = sum + multiply#eswteriko ginomeno

        lmd1 = doc1[word]*doc1[word]
        lend1 = lend1 + lmd1
        lmd2 = doc2[word]*doc2[word]
        lend2 = lend2 + lmd2
    finall1 = (lend1**0.5)#length of doc1 vector
    finall2 = (lend2**0.5)#length of doc2 vector
    similarity = (sum/(finall1*finall2))
    print(similarity*100,"%")
    sim=similarity*100

def wordArrayCreation(DocNum): #This function creates a list that contains all the words with out duplicates in  the specified documents
    global wordArray
    x = 0
    while (x < DocNum):
        fname = os.listdir(mydir + "\Documents")[x] #fname is the name of each document
        fpath = mydir + "\\Documents" + "\\" + fname #the currnet path to the current fname document to open
        with open(fpath, "r") as f:
            for line in f: #for each line of the fname document loop
                for word in line.split():   #this splits  each word in a line into a list and it takes each word in the loop
                    y = 0
                    checkDuplicate = 0 #variable to check the uniquennes of the word
                    while (y < len(wordArray)): #loop to search for uniqueness in the list with all words
                        if (wordArray[y] == word):
                            checkDuplicate = 1 #if word already exists checkDuplicate=1
                        y = y + 1
                    if (checkDuplicate == 0):   #if word is unique
                        wordArray.append(word)  #insert to array
        x = x + 1

def renameSpaceToUnderscore(): #this function renames the documents that have spaces " " in their names and replaces " " with underscore "_"
    path = os.getcwd() + "\Documents"
    filenames = os.listdir(path)
    for filename in filenames:
        os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '_')))



#FUNCTIONS END


#MENU BEGINING
message="Welcome To Similarity Check"
menu="Menu"
caution="CAUTION"
mydir=os.getcwd()
print(message.center(80,'*'))

try:    #this try
    if not os.path.exists('./Documents'):
        os.makedirs('Documents')
        print("Folder Documents was created")
        print ("Please restart the programm having the Documents you want to check in the specified Documents file")
    else:
        print("Folder Documents already exists")
        print("\n")
        print(caution.center(80,'*'))
        print("Please ensure that all the documents to be checked are included in the file \"Documents\" in the folowing directory:\n %s\Documents" %(mydir))
        print("Also any filenames that have spaces, are going to have the spaces replaced by underscores(_).")
        print(menu.center(80,'-'))

        renameSpaceToUnderscore() #function call to rename the documents
        allDocNum=len(os.listdir(mydir + "\Documents"))#number of documents inside the Documents Folder
        wordArray=[] #initialize the array that will contain all the words
        sim = 0.0   #sim will have the result of cosineSim()
        TopKsimilarArray = [] #this array will be a 2d array and will have three columns in each row  the two first for the documents and the third one for the similarity number of those two
        fileNames=[]    #this list will save the names of the documents inside the folder Documents
        #Menu options:
        print("Info: Folder Documents has %d files inside it"%(allDocNum))
        print("Actions:")
        print("0 -> Show the Documents included in the \"Documents\" folder")
        print("1 -> Choose a specified number of documents to be checked")
        print("2 -> Choose all documents to be checked")
        choice=input("Please choose an action (0 or 1 or 2): ")
        choice=int(choice)  #this is the input of the first menu
        boolchoice=False #this variable will be used to loop on each of the submenus

        #switch_case(choice)#cases

        if(choice==0):  #choice 0 print all documents inside Documents Folder
            print("\n")
            if (allDocNum==0):
                print("There's no documents to check Please check the Documents file!!!")
                sys.exit()
            print("The files inside the Documents folder are:")
            print(os.listdir(mydir + "\Documents"))

        elif(choice==1):    #---------------------------choice 1 for Specified amount of documents
            docNumbers = input("Please insert the numbers of documents to check:")
            docNumbers = int(docNumbers)
            confirmation = input("The documents you want to check are:%d\n (yes or no)" % (docNumbers))
            if (confirmation == "yes" or confirmation == "YES"):
                print("Confirmed(",confirmation,")")
                print("\n")
                if (docNumbers == 0):
                    print("You choosed 0 documents to check")
                elif(docNumbers==1):
                    print("You can't choose only one Document to be compared. Yoy need at least one pair of documents!!!")
                elif (docNumbers > allDocNum):
                    print("There aren't so many documents in the documents folder. Please check the Documents folder!!!")
                else:

                    print("The documents to be checked are:")
                    dn = 0
                    while (dn <= docNumbers-1):
                        nameD = os.listdir(mydir + "\Documents")[dn]
                        print(nameD)
                        dn = dn + 1
                    print("\n")

                    wordArrayCreation(DocNum=docNumbers) #function call to create the list that will have all the words of the specified documents

                    # initialWordFrequency, Initailize the each dictionary with value 0 for all keywords
                    #name of each dictionary is the name of the document and keys of the dictionary all all the words from the selected documents
                    z = 0
                    while (z < docNumbers):
                        nameD = os.listdir(mydir + "\Documents")[z]
                        fileNames.append(nameD)
                        vars()[fileNames[z]] = {word: 0 for word in wordArray}
                        z = z + 1
                    # initialWordFrequency END

                    #correctWordFrequency(DocNum=docNumbers)
                    #This loop reads how many times a specific word from the current document is found and  it increases the specific value of the specified keyword of the dictionary as many times it finds the specific word.
                    print("The frequency of words in each documents is:")
                    c = 0
                    while (c < docNumbers):
                        filename = os.listdir(mydir + "\Documents")[c]
                        filepath = mydir + "\\Documents" + "\\" + filename
                        with open(filepath, "r") as file:
                            for line in file:
                                for word in line.split():
                                    y = 0
                                    while (y < len(wordArray)):
                                        if (word == wordArray[y]):
                                            vars()[fileNames[c]][word] += 1 #increase value +1 of the specific key of the specific dictionary
                                            fileNames[c]
                                        y = y + 1
                            print(fileNames[c])
                            print(vars()[fileNames[c]])
                            c = c + 1
                            print("\n")
                    # correctWordFrequency END

                    #simCheck
                    #These loops helps as take pairs of documents we want to check for similarities without taking a pair more than one time
                    #this is succeded by a sequense  to specify which documents were aldready used for pairs using the variables ds, de and diffnum
                    ds = 0
                    de = 1
                    checkNum = 0
                    diffNum = 0
                    while (checkNum < docNumbers):  # This while loop let as take the sequence number we need for the next while loop so we will not get any duplicate on comparing documents that have already been compared
                        difference = (docNumbers - checkNum)
                        if (difference == 2):
                            diffNum = checkNum
                        checkNum = checkNum + 1
                    while (ds < docNumbers - 1):
                        while (de < docNumbers):
                            Doc1cmp = fileNames[ds]
                            Doc2cmp = fileNames[de]
                            if not (Doc1cmp == Doc2cmp):
                                print("The similarity between ", Doc1cmp, " and ", Doc2cmp, " is:")
                                cosineSim(vars()[Doc1cmp], vars()[Doc2cmp]) #Function call for the pair of documents to be compared
                                topKinput = Doc1cmp + " " + Doc2cmp + " " + str(sim) #make a string with spaces in order to insert into the right cells to the 2d list TopKsimilarArray
                                row = topKinput.split()
                                for i in range(len(row)):   #insert into the 2d list TopKsimilarity in a row [[documentname1,documentname2,similarityResult],....]
                                    row[i] = (row[i])
                                TopKsimilarArray.append(row)
                                de = de + 1
                            else:
                                de = de + 1
                        de = de - diffNum
                        ds = ds + 1
                    print("\n")

                    #simCheck END

                    while (boolchoice == False): #submenu loop until exit for the option 1 of the start menu

                        print("Actions of Specified Documents:")
                        print("0 -> Print the word Array of specified Documents")
                        print("1 -> Print the Top-K Most Similar Documents (the K number is user defined)")
                        print("2 -> EXIT ")
                        choice1 = input("Please choose an action (0 or 1 or 2)")
                        print("\n")
                        choice1 = int(choice1)

                        if (choice1 == 0):
                            print("The Words that exist in the  specified Documents are: ", len(wordArray))
                            print(wordArray)
                            print("\n")

                        elif (choice1 == 1):
                            print(" Reminder, you can choose ONLY between 1 to ", len(TopKsimilarArray))
                            numberK = input(
                                "Please choose the amount of documents you want to see the percetage(%) of most similarity: ")
                            numberK = int(numberK)
                            print("\n")
                            if (numberK > len(TopKsimilarArray)):
                                print(
                                    "There aren't so many documents pairs to check. Please check the Documents folder!!!")
                                print("\n")
                                sys.exit()
                            TopKsimilarArray.sort(key=itemgetter(2), reverse=True) #sort the 2d list based on the similarity result thats on the third column  and sort from bigger to smaller
                            print("The Top ", numberK, " most similar documents are:")
                            rowNum = 0
                            while (rowNum < numberK):   #prints the top K rows of the 2d list TopKsimilarArray
                                print("The similarity between ", TopKsimilarArray[rowNum][0], " and ",
                                      TopKsimilarArray[rowNum][1], " is: ", TopKsimilarArray[rowNum][2],"%")
                                rowNum += 1
                            print("\n")

                        elif (choice1 == 2):
                            boolchoice = True
                            print("Exiting....")
                            sys.exit()

                        else:
                            print("Error")
                            print("Choose only between the specified options('0' or '1' or '2')")
                            print("\n")

            elif (confirmation == "no" or confirmation == "NO"):
                print("Confirmed(no)")
                sys.exit()
            else:
                print("Error!,....exiting")
                sys.exit()

        elif (choice==2):#--------------------------------------------------------------choise for ALLDOCUMENTS
            if (allDocNum==0):
                print("There's no documents to check Please check the Documents folder!!!")
                sys.exit()
            print("All documents inside Documents folder are about to be checked!")
            print("Checking all files....")
            print("\n")
            wordArrayCreation(DocNum=allDocNum)

            # initialWordFrequency, Initailise the each dictionary with value 0 for all keywords
            # name of each dictionary is the name of the document and keys of the dictionary all all the words from the selected documents
            z = 0
            while (z < allDocNum):
                nameD = os.listdir(mydir + "\Documents")[z]
                fileNames.append(nameD)
                vars()[fileNames[z]] = {word: 0 for word in wordArray}
                z = z + 1
            # initialWordFrequency END

            #correctWordFrequency
            # This loop reads how many times a specific word from the current document is found and
            #it increases the specific value of the specified keyword of the dictionary as many times it finds the specific word.
            print("The frequency of words in each documents is:")
            print("\n")
            c = 0
            while (c < allDocNum):
                filename = os.listdir(mydir + "\Documents")[c]
                filepath = mydir + "\\Documents" + "\\" + filename
                with open(filepath, "r") as file:
                    for line in file:
                        for word in line.split():
                            y = 0
                            while (y < len(wordArray)):
                                if (word == wordArray[y]):
                                    vars()[fileNames[c]][word] += 1 #increase value +1 of the specific key of the specific dictionary
                                    fileNames[c]
                                y = y + 1
                    print(fileNames[c])
                    print(vars()[fileNames[c]])
                    c = c + 1
                    print("\n")

            #correctWordFrequency END

            #simCheck(DocNum=allDocNum)
            # These loops helps as take pairs of documents we want to check for similarities without taking a pair more than one time
            # this is succeded by a sequense  to specify which documents were aldready used for pairs using the variables ds, de and diffnum
            ds = 0
            de = 1
            checkNum = 0
            diffNum = 0
            while ( checkNum < allDocNum):  # This while loop let as take the sequence number we need for the next while loop so we will not get any duplicate on comparing documents that have already been compared
                difference = (allDocNum - checkNum)
                if (difference == 2):
                    diffNum = checkNum
                checkNum = checkNum + 1
            while (ds < allDocNum - 1):
                while (de < allDocNum):
                    Doc1cmp = fileNames[ds]
                    Doc2cmp = fileNames[de]
                    if not (Doc1cmp == Doc2cmp):
                        print("The similarity between ", Doc1cmp, " and ", Doc2cmp, " is:")
                        cosineSim(vars()[Doc1cmp], vars()[Doc2cmp]) #Function call for the pair of documents to be compared for similarity
                        topKinput = Doc1cmp + " " + Doc2cmp + " " + str(sim) #make a string with spaces in order to insert into the right cells to the 2d list TopKsimilarArray
                        row = topKinput.split()
                        for i in range(len(row)):    #insert into the 2d list TopKsimilarity in a row [[documentname1,documentname2,similarityResult],....]
                            row[i] = (row[i])
                        TopKsimilarArray.append(row)
                        de = de + 1
                    else:
                        de = de + 1
                de = de - diffNum
                ds = ds + 1
            print("\n")

            #simCheck END

            while (boolchoice == False):    #This is the second submenu for the option 2 check all documets
                print("Actions of All Documents:")
                print("0 -> Print the word Array of all Documents")
                print("1 -> Print the Top-K Most Similar Documents (the K number is user defined)")
                print("2 -> EXIT ")
                choice2=input("Please choose an action (0 or 1 or 2)")
                print("\n")
                choice2 = int(choice2)

                if(choice2==0):
                    print("The Words that exist in the  specified Documents are: ", len(wordArray))
                    print(wordArray)
                    print("\n")

                elif(choice2==1):
                    print(" Reminder, you can choose ONLY between 1 to ",len(TopKsimilarArray))
                    numberK = input("Please choose the amount of documents you want to see the percetage(%) of most similarity:" )
                    print("\n")
                    numberK=int(numberK) #typecast the number from string to int
                    if (numberK > len(TopKsimilarArray)):
                        print("There aren't so many documents pairs to check. Please check the Documents folder!!!")
                        print("\n")
                        sys.exit()
                    TopKsimilarArray.sort(key=itemgetter(2), reverse=True) #sort the 2d list based on the similarity result thats on the third column  and sort from bigger to smaller
                    print("The Top ", numberK, " most similar documents are:")
                    rowNum = 0
                    while (rowNum < numberK):   #prints the top K rows of the 2d list TopKsimilarArray
                        print("The similarity between ", TopKsimilarArray[rowNum][0], " and", TopKsimilarArray[rowNum][1]," is", TopKsimilarArray[rowNum][2],"%")
                        rowNum +=1
                    print("\n")

                elif(choice2==2):
                    boolchoice = True
                    print("Exiting....")
                    sys.exit()

                else:
                    print("Error")
                    print("Choose only between the specified options('0' or '1' or '2')")
                    print("\n")

        else:
            print("Error")
            print("Choose only between the specified options('0' or '1' or '2')")

        print("\n")
except OSError:
    print("Error creating directory %s\Documents" %(mydir))
#ΒΑΖΑΙΟΣ ΣΤΥΛΙΑΝΟΣ Α.Μ.: 1054284