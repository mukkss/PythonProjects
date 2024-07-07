# Morse Code Dictionary for Encoding and Decoding
symbols = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

# Reverse MorseCode Dictionary for Decoding and Creates a New Dictionary with the MorseCode as the key and the Alphabets as the value
morse_code_dict = {v: k for k, v in symbols.items()}

# Function to Encode Text to Morse Code
def encode_to_morse(text):
    text = text.lower()#changes the Input alphabets into lower case
    length = len(text)#Checks for the length of the input
    output = ""

    for i in range(length):
        if text[i] in symbols.keys():
            output = output + " " + symbols.get(text[i])

    return output.strip()

# Function to Decode Morse Code to Text
def decode_from_morse(morse_code):
    words = morse_code.split(' / ') #spilts the each morse code into each alphabets 
    decoded_message = ""

    for word in words:
        for char in word.split():
            decoded_message += morse_code_dict.get(char, '')
        decoded_message += " "

    return decoded_message.strip()

# User Interface
def main():
    choice = input("Type 'e' to encode text to Morse code or 'd' to decode Morse code to text: ").lower()
    
    if choice == 'e':
        text = input("Type your word: ")
        print("Encoded Morse Code:", encode_to_morse(text))
    elif choice == 'd':
        morse_code = input("Type your Morse code (use '/' to separate words): ")
        print("Decoded Text:", decode_from_morse(morse_code))
    else:
        print("Invalid choice. Please type 'e' to encode or 'd' to decode.")

if __name__ == "__main__":
    main()
