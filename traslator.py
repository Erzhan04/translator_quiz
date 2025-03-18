from googletrans import Translator
import random


# print("\033[31mRed\033[0m")
# print("\033[32mGreen\033[0m")
# print("\033[34mBlue\033[0m")

translator = Translator()

vocab = """
yes heat mind though during hate shining worst being calm agree remind wet also  accident prefer lastly often warm enjoy
heat mind though during 
""".split()
# print(vocab)
# print(len(vocab))
score = 0
not_correct = []

for i in vocab:
    print("ВВедите перевод этого слова: " )
    my_answer = input(i + ':')
    # print(my_answer)
    result = translator.translate(i, dest="ru")
    if my_answer.lower() == result.text.lower():
        print("\033[32m Верно \033[0m")
        score += 1
    else:
        print(f"\033[31m Не верно \033[0m. Правильный ответ:  \033[32m{result.text}\033[0m")
        not_correct.append(i)

print("\033[34mВаш результат\033[0m: ", score, 'из', len(vocab))

second_score = 0
sec_not_correct = []

print("Хотите поработать с ошибками? (да/нет)")
answer = input()
if answer.lower() == 'да':
    while True:
        for j in not_correct:
            print("ВВедите перевод этого слова: " )
            my_answ = input(j + ':')
            result = translator.translate(j, dest="ru")
            if my_answ.lower() == result.text.lower():
                print('\033[32mПравильноо\033[0m')
                second_score += 1
            else:
                print(f"\033[31m Не верно \033[0m. Правильный ответ:  \033[32m{result.text}\033[0m")
                sec_not_correct.append(j)
        print('Your score is: ', second_score, '/', len(sec_not_correct), '\nХотите еще пройти этих ошибок? Enter yes or no')
        answer = input().lower()
        if answer != 'да':
            break

