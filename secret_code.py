
import random
import string

def coding(message):
    words = message.split()
    result = []

    for word in words:
        if len(word) >= 3:
            word = word[1:] + word[0]

            random_chars = ''.join(
                random.choices(string.ascii_letters, k=3)
            )

            word = random_chars + word + random_chars
        else:
            word = word[::-1]

        result.append(word)

    return ' '.join(result)


def decoding(message):
    words = message.split()
    result = []

    for word in words:
        if len(word) < 3:
            word = word[::-1]
        else:
            word = word[3:-3]
            word = word[-1] + word[:-1]

        result.append(word)

    return ' '.join(result)


message = input("Enter your message here: ")

coded_message = coding(message)
print("Coded message:", coded_message)

decoded_message = decoding(coded_message)
print("Decoded message:", decoded_message)
