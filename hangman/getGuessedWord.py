def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    for index in range(0, len(secretWord)):
        if secretWord[index] not in lettersGuessed:
            temp = secretWord[:index]
            temp += '_'
            temp += secretWord[index+1:]
            secretWord = temp
    
    return secretWord
            