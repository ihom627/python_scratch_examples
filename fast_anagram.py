def anagram(word1, word2):
    dictionary1 = {}
    dictionary2 = {}
    
    if (len(word1) == 0 or len(word2) == 0):
        return(0)
    
    if (len(word1) != len(word2)):
        return(0)


    # use caching to either store the previous dictionaries
    # or cache if two words have been compared before and return results
    
    for i in range(0, len(word1)):
       if word1[i] in dictionary1:
           dictionary1[i] += 1
       else:
           dictionary1[i] = 1
           
    for i in range(0, len(word2)):
       if word2[i] in dictionary2:
           dictionary2[i] += 1
       else:
           dictionary2[i] = 1           
           
    if (dictionary1 == dictionary2):
       return(1)
    else:
       return(0)          
