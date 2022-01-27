puntuaciones = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'L': 1,
    'M': 3,
    'N': 1,
    'Ñ': 8,
    'O': 1,
    'P': 3,
    'Q': 5,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'X': 8,
    'Y': 4,
    'Z': 10,
}

palabra= input("Write a word here: ")

for letra in palabra.upper():
     if letra not in puntuaciones.keys():
          raise Exception(f"Symbol '{letra}' is not valid.")

punto = 0
for letra in palabra.upper():
     punto = punto + puntuaciones[letra]

if len(palabra) > 7:
     raise Exception("Word couldn`t have more than 7 letters.")

print(f"For playing the word:'{palabra.upper()}', you add '{punto}' pints to your score.") 