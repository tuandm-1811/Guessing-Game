import random

attempts_list = []
# khai báo 1 biến rỗng để khi bắt đầu thì sẽ không có giá trị nào được trả về

def show_score():
    if not attempts_list:
        print('There is currently no high score,'
              'it\'s yours for the taking!')

    else:
        print(f'The current high score is: '
              f' {min(attempts_list)} attempts')

def start_game():
    attempts = 0
	# định nghĩa số lần thử
    rand_num = random.randint(1, 10)
	# rand_int là để trả về một giá trị số nguyên được chọn trong phạm vi được chỉ định
    print('Welcome to the guessing game!')
    player_name = input('Your name is: ')
    wanna_play = input(
        f'Hello, {player_name}, would you like to play '
        f'the guessing game?  (Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number within the given range!!!')

            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('You are right')
                print(f'Took you {attempts} attempts')
                wanna_play = input(
                    'Do you want to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not right. Please try again...')
            print(err)

if __name__ == '__main__':
    start_game()