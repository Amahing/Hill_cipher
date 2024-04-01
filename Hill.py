import random

alphabet = (
    'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
    'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'ь', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї',
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', ',', '.', '+', '-', '/', '*', '–', '—', '(',
    ')', ':', ";", '[', ']', '{', '}')

def Hill_generate_key_ecrypt():
    while True:
        key = []
        for x in range(9):
            key.append(random.randint(-50, 50))
        if (key[0] * (key[4] * key[8] - key[5] * key[7]) -
            key[1] * (key[3] * key[8] - key[5] * key[6]) +
            key[2] * (key[3] * key[7] - key[4] * key[6])) == 1:
            break
    return key


def Hill_encrypt(text, key):
    text = list(text)
    while len(text) % 3 != 0:
        text.append(' ')

    ciphertext = []
    for i in range(0, len(text) // 3):
        x1 = alphabet.index(text[i * 3])
        x2 = alphabet.index(text[i * 3 + 1])
        x3 = alphabet.index(text[i * 3 + 2])
        ciphertext.append(alphabet[(x1 * key[0] + x2 * key[3] + x3 * key[6]) % len(alphabet)])
        ciphertext.append(alphabet[(x1 * key[1] + x2 * key[4] + x3 * key[7]) % len(alphabet)])
        ciphertext.append(alphabet[(x1 * key[2] + x2 * key[5] + x3 * key[8]) % len(alphabet)])

    return ciphertext


def Hill_decrypt(ciphertext, key):
    temp = key[1]
    key[1] = key[3]
    key[3] = temp

    temp = key[2]
    key[2] = key[6]
    key[6] = temp

    temp = key[5]
    key[5] = key[7]
    key[7] = temp

    inverse_matrix = []
    inverse_matrix.append(key[4] * key[8] - key[7] * key[5])
    inverse_matrix.append(-1 * (key[3] * key[8] - key[6] * key[5]))
    inverse_matrix.append(key[3] * key[7] - key[6] * key[4])
    inverse_matrix.append(-1 * (key[1] * key[8] - key[7] * key[2]))
    inverse_matrix.append(key[0] * key[8] - key[6] * key[2])
    inverse_matrix.append(-1 * (key[0] * key[7] - key[6] * key[1]))
    inverse_matrix.append(key[1] * key[5] - key[4] * key[2])
    inverse_matrix.append(-1 * (key[0] * key[5] - key[3] * key[2]))
    inverse_matrix.append(key[0] * key[4] - key[3] * key[1])

    decrypted = []
    for i in range(0, len(ciphertext) // 3):
        x1 = alphabet.index(ciphertext[i * 3])
        x2 = alphabet.index(ciphertext[i * 3 + 1])
        x3 = alphabet.index(ciphertext[i * 3 + 2])
        decrypted.append(
            alphabet[(x1 * inverse_matrix[0] + x2 * inverse_matrix[3] + x3 * inverse_matrix[6]) % len(alphabet)])
        decrypted.append(
            alphabet[(x1 * inverse_matrix[1] + x2 * inverse_matrix[4] + x3 * inverse_matrix[7]) % len(alphabet)])
        decrypted.append(
            alphabet[(x1 * inverse_matrix[2] + x2 * inverse_matrix[5] + x3 * inverse_matrix[8]) % len(alphabet)])

    return decrypted

# Run for testing:

my_key = Hill_generate_key_ecrypt()
encrypted = Hill_encrypt("Привіт", my_key)
print("Зашифрований текст:", encrypted)
encrypted = ''.join(encrypted)
print("Дешифрований текст:", Hill_decrypt(encrypted, my_key))