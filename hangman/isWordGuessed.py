def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for index in range(0, len(lettersGuessed)):
        if len(secretWord) == 0:
            break
        while lettersGuessed[index] in secretWord:
            pos = secretWord.index(lettersGuessed[index])
            temp_Word = secretWord[:pos]
            temp_Word += secretWord[pos+1:]
            secretWord = temp_Word
    
    if( len (secretWord) == 0 ):
        return True
    return False