# coding=utf-8

import random

HANGMANPICS = [
    '''
    +---+
    |   |
        |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
==========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
==========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
==========''']

words = 'ada ruby python java groovy elixir basic sharp swift rails'.split()


def getRandomWord(wordList):
    # 从列表里面随机返回一项
    wordIndex = random.randint(0, len(wordList) - 1)  # 随机选取一个索引,但不能超出索引长度,不然就会溢出
    return wordList[wordIndex]


def displayBoard(HANGMANPICS, missdLetters, correctLetters, secretWord):
    # 最精妙的地方: 绞刑图又missLetters的状态控制,错一个就print画一个头的图,错两个就print一个头和一个身体的图
    print(HANGMANPICS[len(missdLetters)])
    print()
    print('Missed letters: ')
    tmp = ''
    for letter in missdLetters:
        tmp = tmp + letter + ''
        # print('%s' %letter)
    print(tmp)

    #  _ _ _ _ _ -> _ a _
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters 遍历
        if secretWord[i] in correctLetters:
            # blanks[:i]从第0位切到第i位, blanks[i+1:]从第i位切到最后一位,这样其实是把第i位给切没了,secretWord[i]表示加上第i位的字母
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]  # 最难的地方
    tmp = ''
    for letter in blanks:  # show the secret word with spaces in between each letter
        tmp = tmp + letter + ' '
        print(tmp)
        print()


# 猜过了的字母不能再猜(对Input parity)
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        # guess = raw_input
        guess = input()
        guess = guess.lower()  # 转换成小写
        if len(guess) != 1:  # input len不能 大于 1
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:  # 已经input not in input
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':  # not in input abcdefghijklmnopqrstuvwxyz  以外的字符
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    print('Do you want to play again? (yes/no)')
    # return raw_input().lower().startswith('y')
    return input().lower().startswith('y')  # 只要用户input 以 y 开头就说明用户想再玩一盘


print('H A N G M A N')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter' + str(len(missedLetters)) + 'missed guesses and ' + str(
                len(correctLetters)) +
                  'correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
