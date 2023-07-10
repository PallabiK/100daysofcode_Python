MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


use_cipher = True
while use_cipher:
    choice = input("Encrypt or Decrypt text: ").lower()
    text = input("Enter your text: ").upper()
    if choice == "encrypt":
        cipher = ''

        for letter in text:
            if letter != '':
                cipher += MORSE_CODE_DICT[letter] + ''
            else:
                cipher += ''
        print(f"The encrypted text is {cipher}.")
    elif choice == "decrypt":
        text += ''
        decipher = ''
        citext = ''
        for letter in text:
            if letter != '':
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += ''
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                                  .values()).index(citext)]
                    citext = ''

        print(f"The decrypted text is {decipher}.")

    else:
        print ("Choice does not exist.")

    go_again = input("Do you have another message? Type 'Yes' or 'No': ").lower()
    if go_again == "yes":
        use_cipher = True
    elif go_again == "no":
        use_cipher = False



