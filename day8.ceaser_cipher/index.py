from ascii_paint import logo
print(logo)
#ascii char numbers for a - z 97 -122
def encode_decoder(text, shift, encode_or_decode):
    encripted_text = ""
    start = 97
    end = 122
    for char in text:
        char_num = ord(char)
        if(encode_or_decode == "encode"):
            new_char_num = char_num + shift
            if new_char_num > end:
                temp = new_char_num - 122
                new_char_num = start + 1 + temp
            encripted_text += chr(new_char_num)
        else:
            new_char_num = char_num - shift
            if new_char_num < start:
                temp = start - new_char_num
                new_char_num = end + 1 - temp
            encripted_text += chr(new_char_num)

    print(encripted_text)

go_again = ""

while not go_again == "no":
    encode_or_decode = input("Do you want to encode or decode?\n")
    message = input("Type your message: \n").lower()
    can_continue = False
    while not can_continue:
        for index, char in enumerate(message):
            if(ord(char) < 97 or ord(char) > 122):
                print("Please, enter a valid word, with no symbols, digits or whitesaces.")
                message = input("Type your message: \n").lower()
                break
            elif index == len(message) - 1:
                can_continue = True
    shift_number = int(input("Type the shift number: \n"))
    encode_decoder(message, shift_number, encode_or_decode)
    go_again = input("Type 'yes' if you want to go again, otherwise type 'no': \n")