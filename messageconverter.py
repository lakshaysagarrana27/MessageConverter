#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def readingTranslationFile():
   
    fullForm = [] #consists of lists. each list consists of every word in a line
    shortFormList = [] #consists of all words like "LOL" ,"ROFL" (only short forms)
                       #not entire abbreviations
    counter = 0 
    with open("Translations.txt","r") as translationFile: #opening a file
        #fullForm = [] #list to hold entire line as string in one index  
        for line in translationFile:
           if line == "\n":
               pass
           else:
             # fullForm.append(line.strip()) #strip function to remove spaces 
                                            #from front and behind
              #print("append Done! "+ str(counter))
              #counter = counter +1
              cuttingLine = line.split(" ") #cutting the line into lists by spaces
              fullForm.append(cuttingLine) #appending  as a list
              shortFormList.append(fullForm[counter][0]) #appending only acronym
              counter = counter + 1
              
    #print(len(fullForm))
#    for line in fullForm:
#        cuttingLine = line.split(" ")
#        #print(cuttingLine)
#        fullForm2.append(cuttingLine)
#    
#         
#    for counter in range(0,len(fullForm2)):
#        shortFormList.append(fullForm2[counter][0])
    
    #print(shortFormList)
    #print(str(" ".join(fullForm2[0][2:])))
    return(shortFormList,fullForm) #returning as a tuple 
    
def readingTextMessage():
     #saving the whole text message as list
    text = []
    with open("message.txt","r") as textMessage:
        message = textMessage.read()
        text = message.split()
    
    
    return text                   
       
 
def searchingAndCreating(shortForm,fullForm,message):
    newText =[]
    #print(shortForm[0])
    #print(fullForm)
    #print(message)
    for word in message:
        found = None
        counter = 0
        for word2 in shortForm:
            if word2 == word:
                found = True
                for word3 in fullForm[counter][2:]:
                    newText.append(word3)
                break
                
            elif word2 != word:
                found = False                
                counter = counter + 1
            
        if found is False:
            newText.append(word)
    print(newText)
    for word in newText:
        print(word,end=" ")
     
        
        
        
        
        
        

    
def main():    
    shortFormTuple = readingTranslationFile()      
    textMessage = readingTextMessage()
    searchingAndCreating(shortFormTuple[0],shortFormTuple[1],textMessage)
    
main()
