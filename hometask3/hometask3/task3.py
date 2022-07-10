def get_file_extension(file_name):
    file_parts = file_name.rsplit('.', 1)
    file_extension = ''
    if len(file_parts) > 1:
        file_extension = file_parts[1]
    return file_extension


def get_digits(text_string):
    digits_string = ''
    for char in text_string:
        if char.isdigit():
            digits_string += char
    return digits_string


if __name__ == '__main__':
    test_file_name = 'file123.txt'
    print(get_file_extension(test_file_name))
    print(get_digits(test_file_name))
