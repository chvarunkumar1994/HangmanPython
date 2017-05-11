def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    result = ''
    allLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = ''    
    for index in range(0, len(allLower)):
        if allLower[index] not in lettersGuessed:
            result += allLower[index]
    
    return result