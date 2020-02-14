guess_list = []


def is_secret_word(word1):
    if ' ' in word1:
        return False
    elif '?' in word1:
        return False
    else:
        return True


def get_secret_word(prompt):
    while True:
        str_num = input(prompt)
        if is_secret_word(str_num):
            return str(str_num)


def is_guess(prompt1):
    guess1 = prompt1.strip()
    if len(guess1) == 1:
        return True
    elif len(guess1) > 1:
        print('You can only guess a single character.')
        return False
    elif guess1 == '':
        print('You must enter a guess.')
        return False
    else:
        return False


def get_guess(prompt1):
    while True:
        str_num1 = input(prompt1)
        if is_guess(str_num1):
            return str(str_num1).strip()


def is_game_over(a, b):
    if a == b:
        return True
    else:
        return False


def display_hangman(a):
    b = int(a)
    if b == 1:
        print(' |\n')
    elif b == 2:
        print(' |')
        print(' 0\n')
    elif b == 3:
        print(' |')
        print(' 0')
        print(' |\n')
    elif b == 4:
        print(' |')
        print(' 0')
        print('/|\n')
    elif b == 5:
        print(' |')
        print(' 0')
        print('/|\\\n')
    elif b == 6:
        print(' |')
        print(' 0')
        print('/|\\')
        print('/\n')
    elif b == 7:
        print(' |')
        print(' 0')
        print('/|\\')
        print('/ \\\n')


def display_guesses():
    pass


pass


def main():
    word = get_secret_word('Please enter a word to be guessed\nthat does not contain ? or white space: ')
    print('\n' * 29)
    wordl = list(word)
    wordwenhao = len(word) * '?'
    list1 = ''
    hang = 0
    caide = str('?' * len(word))
    caidel = list(caide)
    print(caide)
    print('So far you have guessed: ')
    n = 1

    while n <= 7:
        z = 1
        guess = get_guess('Please enter your next guess: ')

        if is_guess(guess):
            while guess in list1:
                print('You already guessed the character: ', end='')
                print(guess)
                guess = get_guess('Please enter your next guess: \n')
            list1 = list1 + guess

            if guess in word:
                while z <= len(word):
                    if guess == wordl[z - 1]:
                        caidel[z - 1] = guess
                        z = z + 1
                    else:
                        z = z + 1
                if caidel == wordl:
                    print('You correctly guessed the secret word:', ''.join(caidel))
                    break
                else:
                    display_hangman(hang)
            else:

                if (n == 7) and (caidel != wordl):
                    display_hangman(7)
                    print('You failed to guess the secret word:', word)
                    break
                hang = hang + 1
                display_hangman(hang)
                n = n + 1


        print(''.join(caidel))

        print('So far you have guessed: ', end='')
        y = 1

        for a in range(len(list1)):
            list2 = list(list1)
            list2 = sorted(list2)
            if y < len(list1):
                print(list2[y - 1], end='')
                print(',', end=' ')
                y = y + 1
            else:
                print(list2[y - 1])




main()
