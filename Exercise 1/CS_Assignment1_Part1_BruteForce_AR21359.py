#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Assignment 1: Computer Security
#Part 1: bruteforce
#Ana Laura Rodriguez Alba, AR21359
#November 19, 2021
def bForce():
    secretMessage = open("secretMessage.txt","r")
    #opens encrypted message file
    realM = secretMessage.readlines()
    #reads file / retrieves contents
    secretMessage.close()
    
    realM = str(realM[:]).upper()
    #transforms file contents to upper cases
    realM = realM[2:-2]
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for key in range(len(alpha)):
        end = ''
        
        for char in realM:
            if char in alpha:
                index = (alpha.find(char)-key)% len(alpha)
                #reverts message contents and moves from key numbers until for reaches end
                
                end += alpha[index]
            else:
                end += char
        print('Key #%s: %s' % (key, end))
        #prints key number and result

def main():
    bForce()

main()


# In[ ]:




