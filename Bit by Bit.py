import base64
import string

HIDDEN_FLAG = 'YmluYXJ5cmVmaW5lcnl8JiY+PnxeXl4mJnx8fg=='


def decode_flag(encoded_flag):
    return base64.b64decode(encoded_flag).decode()


def get_list_of_chars_from_flag_cubed(flag):
    return [ord(char) ** 3 for char in flag if char in string.ascii_letters]


def get_list_of_operators_from_flag_cubed(flag):
    operators = [char for char in flag if char not in string.ascii_letters]
    for i, operator in enumerate(operators):
        if operator == '>':
            operators[i] = '>>'
            del operators[i + 1]

    return operators


def apply_operator(operator, operand_1, operand_2):
    if operator == '~':
        return ~operand_1
    return eval(str(operand_1) + operator + str(operand_2))


def solve_bit_by_bit(encoded_flag):
    flag = decode_flag(encoded_flag)
    numerals_of_chars = get_list_of_chars_from_flag_cubed(flag)
    operators = get_list_of_operators_from_flag_cubed(flag)

    current_number = numerals_of_chars[0]
    for operator_start_index in range(len(operators)):
        for operator_index in range(operator_start_index, len(operators)):
            current_number = apply_operator(operators[operator_index], current_number,
                                            numerals_of_chars[operator_index + 1])
    return current_number


print(solve_bit_by_bit(HIDDEN_FLAG))
