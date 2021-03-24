import core

def encode_message(file):
    result_file = open("result.txt", "a")
    line = ""
    while line != "end":
        line = file.readline()

        for char in line:
            if(char != " " and char != "\n"):
                code = core.get_code_of_char(char)
                result_file.write(code+" ")
            else:
                result_file.write(" ")
        result_file.write(" ")
    result_file.close()

def decode_message(file):
    result_file = open("result.txt", "a")
    message = file.read()
    lines = message.split("   ")
    for line in lines:
        line = line.strip()
        words = line.split("  ")
        for word in words:
            chars = word.split(" ")
            for char in chars:
                char = core.get_char_of_code(char)     
                result_file.write(char)
            result_file.write(" ")
        result_file.write("\n")
    result_file.close()

while True:
    print("What you want?")
    print("1: encode")
    print("2: decode")
    print("3: exit")

    rule = int(input())

    if rule == 1:
        file = open("message.txt", "r")
        encode.encode_message(file)

    elif rule == 2:
        file = open("message.txt", "r")
        decode.decode_text(file)

    else:
        exit()