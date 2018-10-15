from string import ascii_lowercase as letters
word = list(input(''))
closestVowel = 0
wordInNumbers = []
translated = []
for i in range(len(word)):

    wordInNumbers.append(ord(word[i])-96)

for i in range(len(word)):
    if wordInNumbers[i] == 1:
        translated.append('a')
    elif wordInNumbers[i] == 5:
        translated.append('e')
    elif wordInNumbers[i] == 9:
        translated.append('i')
    elif wordInNumbers[i] == 15:
        translated.append('o')
    elif wordInNumbers[i] == 21:
        translated.append('u')
    elif wordInNumbers[i] < 4:
        translated.append(chr(wordInNumbers[i]+96)+'e'+chr(wordInNumbers[i]+97))
    elif 5<wordInNumbers[i]<8:
        translated.append(chr(wordInNumbers[i]+96)+'e'+chr(wordInNumbers[i]+97))
    elif 9<wordInNumbers[i]<13:
        translated.append(chr(wordInNumbers[i]+96)+'i'+chr(wordInNumbers[i]+97))
    elif 15<wordInNumbers[i]<19:
        translated.append(chr(wordInNumbers[i]+96)+'o'+chr(wordInNumbers[i]+97))
    elif 21<wordInNumbers[i]<26:
        translated.append(chr(wordInNumbers[i]+96)+'u'+chr(wordInNumbers[i]+97))
    elif wordInNumbers[i]==26:
        translated.append('zuz')
    elif wordInNumbers[i] == 4:
        translated.append("def")
    elif wordInNumbers[i] == 8:
        translated.append("hij")
    elif wordInNumbers[i] == 14:
        translated.append("nop")
    elif wordInNumbers[i] == 20:
        translated.append("tuv")
    elif wordInNumbers[i] == 13:
        translated.append("mon")
    elif wordInNumbers[i] == 19:
        translated.append("sut")

final = ''.join(map(str, translated))
print(final)

