def fill_file_with_hw():
    with open("file.txt", 'w') as file:
        for i in range(1, 1001):
            file.write("Hello World\n")

if __name__ == '__main__':
    fill_file_with_hw()
