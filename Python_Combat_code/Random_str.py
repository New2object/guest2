import random, sys

MAX = 5
LOW = 1
HIGH = 99

while True:  # game loop
    target = random.randint(LOW, HIGH)
    # 用户尝试的次数
    times = 0
    print('I am thinking of a number between 1 and 100')
    print(target)

    while True:
        user_number = 0
        if times == MAX:
            sys.exit('Game over, the correct number is %s' % target)
        while True:
            user_input = input("take a guess or enter 'q' to quit\n")
            # 按Q或者q键均可退出.....
            if user_input.strip().lower() == 'q':
                sys.exit('Goodbye......')
            if user_input.isdigit():
                user_number = int(user_input)
                break
            else:
                print('invalid input......')

        if user_number > target:
            times = times + 1
            print('Your guess is too high......')
        elif user_number < target:
            print('Your guess is too low......')
            break

"""
    有两种处理非数字输入的方法:
        1.try异常处理:
            while True:
                number_input = 0
                while True:
                    user_input = input("take a guess\n")
                    try:
                        user_number = int(user_input)
                        break
                    except:
                        print('invalid input')


        2.用isdigit()判断input是否为int type:
            if user_input.isdigit() == True:
                    user_input = int(user_input)
                    if user_input > target:
                        print('Your guess is too high')
                    elif user_input < target:
                        print('Your guess is too low')
                    else:
                        print('Good job, the correct number is %s' % target)
                        break
                else:
                    print('invalid input')


"""
