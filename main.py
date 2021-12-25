import sys


def one_counter(str):
    count = 0
    while str != 0:
        if str % 2 == 1:
            count += 1
        str = int(str / 2)
    return count


def zero_count(str):
    count = 0
    while str % 2 == 0:
        str = str / 2
        count += 1
    return count


def main():
    command_list = []
    sum = int(input())

    while sum != 0:
        half = bin(sum)
        if sum % 2 == 0:
            sum = int(sum / 2)
            command_list.append('dbl')
        else:
            count_1 = one_counter(sum - 1)
            count_2 = one_counter(sum + 1)

            if count_1 < count_2:
                sum = sum - 1
                command_list.append('inc')

            elif count_1 > count_2:
                sum = sum + 1
                command_list.append('dec')

            elif count_1 == count_2:
                zero_count_1 = zero_count(sum - 1)
                zero_count_2 = zero_count(sum + 1)
                if zero_count_1 < zero_count_2 and len(bin(sum + 1)) <= len(bin(sum - 1)):
                    sum = sum + 1
                    command_list.append('dec')
                else:
                    sum = sum - 1
                    command_list.append('inc')

    print(len(command_list))
    for i in range(len(command_list)):
        print(command_list[len(command_list) - 1 - i])


main()
