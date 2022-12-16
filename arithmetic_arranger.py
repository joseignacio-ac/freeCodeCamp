def arithmetic_arranger(operations, answer = False):
    first_line, second_line, third_line, fourth_line = "", "", "", "\n"
    error_1, error_2, error_3, error_4 = False, False, False, False

    for string in operations:
        string_splitted = string.split()
        if not(string_splitted[1] == "+" or string_splitted[1] == "-"):
            error_1 = True

        if len(string_splitted[0]) > 4:
            error_2 = True
        elif len(string_splitted[2]) > 4:
            error_2 = True

        try:
            if str(type(int(string_splitted[0]))).split()[1].split("'")[1] != 'int':
                error_3 = True
            elif str(type(int(string_splitted[2]))).split()[1].split("'")[1] != 'int':
                error_3 = True
        except:
            error_3 = True

    if error_1 == True:
        return "Error: Operator must be '+' or '-'."

    if error_2 == True:
        return 'Error: Numbers cannot be more than four digits.'

    if error_3 == True:
        return 'Error: Numbers must only contain digits.'

    if len(operations) > 5:
        error_4 = True
        return "Error: Too many problems."


    if all((not error_1, not error_2, not error_3, not error_4)):
        for string in operations:
            string_splitted = string.split()
            length_arrange = max(list(len(string_splitted[i]) for i in range(len(string_splitted))))

            if string_splitted[1] == '+':
                result = str(int(string_splitted[0]) + int(string_splitted[2]))
            elif string_splitted[1] == '-':
                result = str(int(string_splitted[0]) - int(string_splitted[2]))

            count = 0
            while True:
                if (length_arrange + 2) - len(string_splitted[0]) - count > 0:
                    first_line += " "
                elif (length_arrange + 2) - len(string_splitted[0]) - count == 0:
                    first_line += string_splitted[0]

                if len(string_splitted[2]) >= len(string_splitted[0]):
                    if count == 0:
                        second_line += string_splitted[1]
                    elif count == 1:
                        second_line += " "
                    elif (length_arrange + 2) - len(string_splitted[2]) - count == 0:
                        second_line += string_splitted[2]
                elif len(string_splitted[2]) < len(string_splitted[0]):
                    if count == 0:
                        second_line += string_splitted[1]
                    elif (length_arrange + 2) - len(string_splitted[2]) - count > 0:
                        second_line += " "
                    elif (length_arrange + 2) - len(string_splitted[2]) - count == 0:
                        second_line += string_splitted[2]

                third_line += '-'

                if (length_arrange + 2) - len(result) - count > 0:
                    fourth_line += " "
                elif (length_arrange + 2) - len(result) - count == 0:
                    fourth_line += result

                count += 1

                if count >= length_arrange + 2:
                    break

            for _ in range(4):
                first_line += " "
                second_line += " "
                third_line += " "
                fourth_line += " "


        if answer == True:
            return first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip() + fourth_line.rstrip()
        elif answer == False:
            return first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()
