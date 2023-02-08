# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
#
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
#
# Напишите программу, которая вычисляет стоимость введенного
# пользователем слова. Будем считать, что на вход подается
# только одно слово, которое содержит либо только английские,
# либо только русские буквы и заранее известно какой алфавит надо использовать.
#
# Примеры/Тесты:
# Input:   ноутбук
# Output:  12
#
# Input:   notebook
# Output:  14
# (*) Примечание.
# Подумайте о том какие структуры данных здесь наиболее удобно использовать,
# чтобы просто проверять в какую группу попадает буква, а также просто накапливать сумму очков.

dict_en = {"AEIOULNSTR": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
dict_rus = {"АВЕИНОРСТ": 1, "ДКЛМПУ": 2, "БГЁЬЯ": 3, "ЙЫ": 4, "ЖЗХЦЧ": 5, "ШЭЮ": 8, "ФЩЪ": 10}
word = input()
sum = 0
for el in word:
    for key, val in dict_en.items():
        if el.upper() in key:
            sum += val
    else:
        for key1, val1 in dict_rus.items():
            if el.upper() in key1:
                sum += val1
print(sum)