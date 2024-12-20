import random

print('Самый надёждый генератор паролей приветствует!')
print('Какую хотите длину пароль? (желательно от 8!)')
lenpo = int(input())
count = 0
print('Какие буквы хотите использовать? (Английские или Русские)')
bykvi = input()
print('Можно ли использовать символы? (Да или Нет)')
mona = input()
rus = {1: "а", 2: "б", 3: "в", 4: "г", 5: "д", 6: "е", 7: "ё", 8: "ж", 9: "з", 10: "и", 11: "й",
       12: "к", 13: "л", 14: "м", 15: "н", 16: "о", 17: "п", 18: "р", 19: "с", 20: "т", 21: "у",
       22: "ф", 23: "х", 24: "ц", 25: "ч", 26: "ш", 27: "щ", 28: "ъ", 29: "ы", 30: "ь", 31: "э",
       32: "ю", 33: "я"
       }
ang = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j",
       11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s",
       20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
sim = {1: "_", 2: "{", 3: "}", 4: "[", 5: "]",
       6: ";", 7: "'", 8: ",", 9: ".",
       10: "/", 11: "?"
       }
otvet = []
nevar = True
while True:
    count += 1
    if bykvi == 'Русские':
        ran = random.randint(1, 3)
        if ran == 1:
            byk = random.randint(1, 33)
            bs = random.randint(1, 2)
            if bs == 1:
                otvet.append(rus[byk].upper())
            elif bs == 2:
                otvet.append(rus[byk].lower())
        elif ran == 2:
            chislo = random.randint(0,9)
            otvet.append(chislo)
        elif ran == 3:
            if mona == 'Да':
                c = random.randint(1, 11)
                otvet.append(sim[c])
    elif bykvi == 'Английские':
        ran = random.randint(1, 3)
        if ran == 1:
            byk = random.randint(1, 26)
            bs = random.randint(1, 2)
            if bs == 1:
                otvet.append(ang[byk].upper())
            elif bs == 2:
                otvet.append(ang[byk].lower())
        elif ran == 2:
            chislo = random.randint(0, 9)
            otvet.append(chislo)
        elif ran == 3:
            if mona == 'Да':
                c = random.randint(1, 11)
                otvet.append(sim[c])
    else:
        print('Вы выбрали не правильный варинт алфавита(')
        print('Попробуйте ещё раз!')
        nevar = False
    if count == lenpo:
        break
    if count % 3 == 0:
        otvet.append('-')
if nevar:
    print('Вот ваш пароль! (🤫 мы никому не скажем...)')
    print(*otvet, sep='')
m reliable-password-generator
