import random

def hangman(length,word):
    chance = 7
    flag = 0
    guessed_word = list('_' * len(word))
    print('****Hangman Game****')
    while True:
        if chance == 0:
            break
        print('\nChances left :',chance)
        print(guessed_word)
        letter = input().lower()
        if letter in word:
            for i in range(length):
                if letter == word[i]:
                    guessed_word[i] = letter
            if list(word) == guessed_word:
                flag=1
                break
        else:
            chance-=1
    if flag == 1:
        print('You Won! The word was',word)
    else:
        print('You Lost! The correct word was',word)

if __name__ == "__main__":
    #List of 20 words for the game
    words = ['cat','india','google','human','food','brain','stomach','aeroplane','notebook','pencil','magnet','medicine','computer','python','java','train','youtube','mobile','maths','biology']
    word = words[random.randint(0,len(words)-1)]
    hangman(len(word),word)