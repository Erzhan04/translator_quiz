from googletrans import Translator
import random

translator = Translator()

vocab = """
heat mind though during hate shining worst being calm agree remind wet also  accident prefer lastly often warm enjoy
""".split()
print(vocab)
print(len(vocab))

score = 0
not_correct = []

for i in vocab:
    print("ВВедите перевод этого слова: " )
    my_answer = input(i + ':')
    # print(my_answer)
    result = translator.translate(i, dest="ru")
    if my_answer.lower() == result.text.lower():
        print("Верно")
        score += 1
    else:
        print("Не верно. Правильный ответ: ", result.text)
        not_correct.append(i)

print("Ваш результат: ", score, 'из', len(vocab))

second_score = 0
sec_not_correct = []

print("Хотите поработать с ошибками? (да/нет)")
answer = input()
while True:
    if answer.lower() == 'да':
        for j in not_correct:
            print("ВВедите перевод этого слова: " )
            my_answ = input(j + ':')
            result = translator.translate(j, dest="ru")
            if my_answ.lower() == result.text.lower():
                print('Right')
                second_score += 1
            else:
                print('That answer is not correct. Right answer is - ', result.text)
                sec_not_correct.append(j)
    print('Your score is: ', second_score, '/', len(sec_not_correct), '\nХотите еще пройти этих ошибок? Enter yes or no')
    answer = input().lower()
    if answer != 'да':
        break

