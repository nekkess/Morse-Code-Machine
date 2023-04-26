MORSE_DICT = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-',
              # my custom additions
              ' ': '', ',': '--..--', ':': '---...', "'": '.----.'}


def encode(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            try:
                cipher += MORSE_DICT[letter.upper()] + ' '
            except KeyError:
                continue
        else:
            cipher += ' '

    return cipher


def decode(message):
    # the next line reverses the morse dict
    morse_dict_rev = {v: k for k, v in MORSE_DICT.items()}
    cipher = ''
    for code in message.split(" "):
        cipher += morse_dict_rev[code]

    return cipher


if __name__ == "__main__":
    action = input("Would you like to decode or encode a message?\n").lower()
    if action == 'encode':
        msg_str = input("Enter message which convert to Morse code:\n")
        print(f"The morse sipher for this text is:\n{encode(msg_str)}")
    elif action == 'decode':
        msg_str = input("Enter message which convert to Morse code:\n")
        print(f"The decoded message is:\n{decode(msg_str)}")
    else:
        print("I don't understand what do you want from me.")