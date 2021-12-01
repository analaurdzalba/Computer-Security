#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Assignment 1: Computer Security
#Part 1
#Ana Laura Rodriguez Alba, AR21359
#November 19, 2021

def encryptMessage(userkey,text):
    #this function encrypts messages that are sent in by the user
    text = text.upper() #change text to uppercase to match alphabet
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    end = ''
    
    for char in text:
        if char in alpha:
            index = (alpha.find(char)+userkey)% len(alpha)
            #use the key to modify letter to new index
            end = end + alpha[index]
        else:
            end = end+char
            
    #sends back encrypted message 
    return end

def decryptMessage(userkey,text):
    #this function decrypts messages / can be used to verify encryption was done correctly
    text = text.upper()
    #changes text to upper case to use with alphabet
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    end = ''
    
    for char in text:
        if char in alpha: 
            index = (alpha.find(char)-userkey % len(alpha))
            #returns letters to their original index 
            end = end + alpha[index]
        else: 
            end = end + char
            
    return end


def main():
    secretMessage = input("Insert text you wish to encrypt here: ") 
    #user input
    key = input("Insert key you wish to use here: ")
    #user input
    fKey = open('key.txt','w')
    #creates file with the user's key
    fKey.write(key)
    fKey.close()
    
    key = int(key)
    
    encryptSecret = encryptMessage(key,secretMessage)
    #calls function encryptMessage to encrypt user's message
    
    fMessage = open('secretMessage.txt','w')
    #creates file 
    fMessage.write(encryptSecret)
    #Writes file with encrypted message created with function encryptMessage
    fMessage.close()
    
    decryptSecret = decryptMessage(key,encryptSecret)
        #calls function decryptMessage to encrypt user's message
    fDMessage = open('decryptSecret.txt','w')
    fDMessage.write(decryptSecret)
    #Writes file with encrypted message created with function decryptMessage
    
    
main()


# In[ ]:




