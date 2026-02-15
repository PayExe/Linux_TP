def cesar_decode(texte):
    for i in range(26):
        rep = ""
        for char in texte:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                rep += chr((ord(char) - start - i) % 26 + start)
            else:
                rep += char
        print(i,rep)

message = "Shwlwh sdxvh txdqg wx dv wurxyh oh ghxalhph phvvdjh"
cesar_decode(message)
