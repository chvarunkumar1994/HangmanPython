def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
       len_secretWord = len(secretWord)
    mistakesMade = 0
    chances = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', +len_secretWord, 'letters long.' )        
    
    
    while( mistakesMade < chances ):
        
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')        
            break
        
        print('You have', +(chances - mistakesMade), 'guesses left.')
        print('Available letters:' +getAvailableLetters(lettersGuessed) )
        guess = input('Please guess a letter:')
        
        if guess[0] in lettersGuessed:
            print("Oops! You've already guessed that letter:" +getGuessedWord(secretWord, lettersGuessed))
        elif guess[0] not in secretWord:
            lettersGuessed.append(guess[0])            
            mistakesMade += 1
            print("Oops! That letter is not in my word: " +getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess[0])
            print('Good guess:' +getGuessedWord(secretWord, lettersGuessed))
    print('-------------')         
    if(mistakesMade == chances):
        print('Sorry, you ran out of guesses. The word was ' +secretWord +'.')
    