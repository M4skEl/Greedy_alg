import sys


def one_counter(str):
    return str.count('1')


def zero_count(str):
    count = 0
    for i in range(len(str)):
        if str[len(str) - 1 - i] == '0':
            count += 1
        if str[len(str) - 1 - i] == '1':
            break
    return count


def made_bin(number):
    str = bin(number)
    return str[2:]


def main():
    command_list = []
    sum = int(input())

    while sum != 0:
        half = made_bin(sum)
        if half[-1] == '0':
            sum = int(sum / 2)
            command_list.append('dbl')
        elif half[-1] == '1':
            count_1 = one_counter(made_bin(sum - 1))
            count_2 = one_counter(made_bin(sum + 1))
            if count_1 < count_2:
                sum = sum - 1
                command_list.append('inc')
            elif count_1 > count_2:
                sum = sum + 1
                command_list.append('dec')
            elif count_1 == count_2:
                zero_count_1 = zero_count(made_bin(sum - 1))
                zero_count_2 = zero_count(made_bin(sum + 1))
                if zero_count_1 < zero_count_2 and len(made_bin(sum + 1)) <= len(made_bin(sum - 1)):
                    sum = sum + 1
                    command_list.append('dec')
                else:
                    sum = sum - 1
                    command_list.append('inc')

    print(len(command_list))
    for i in range(len(command_list)):
        print(command_list[len(command_list) - 1 - i])


main()
