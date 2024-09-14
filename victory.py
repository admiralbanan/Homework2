# victory.py

# Знаменитости и их годы рождения
famous_people = {
    "А.С. Пушкин": "1799",
    "Л.Н. Толстой": "1828",
    "М.В. Ломоносов": "1711",
    "Ф.М. Достоевский": "1821",
    "П.И. Чайковский": "1840"
}

# Счетчики правильных и неправильных ответов
correct_answers = 0
total_questions = len(famous_people)

# Начало викторины
for person, year in famous_people.items():
    user_answer = input(f"Введите год рождения {person}: ")
    if user_answer == year:
        print("Верно!")
        correct_answers += 1
    else:
        print(f"Неверно! Правильный ответ: {year}")

# Подсчет статистики
wrong_answers = total_questions - correct_answers
correct_percentage = (correct_answers * 100) / total_questions
wrong_percentage = 100 - correct_percentage

# Вывод статистики
print(f"\nКоличество правильных ответов: {correct_answers}")
print(f"Количество ошибок: {wrong_answers}")
print(f"Процент правильных ответов: {correct_percentage:.2f}%")
print(f"Процент неправильных ответов: {wrong_percentage:.2f}%")

# Спрашиваем, хочет ли пользователь сыграть снова
while True:
    play_again = input("\nХотите начать сначала? (да/нет): ").lower()
    if play_again == "да":
        correct_answers = 0
        for person, year in famous_people.items():
            user_answer = input(f"Введите год рождения {person}: ")
            if user_answer == year:
                print("Верно!")
                correct_answers += 1
            else:
                print(f"Неверно! Правильный ответ: {year}")
        wrong_answers = total_questions - correct_answers
        correct_percentage = (correct_answers * 100) / total_questions
        wrong_percentage = 100 - correct_percentage
        print(f"\nКоличество правильных ответов: {correct_answers}")
        print(f"Количество ошибок: {wrong_answers}")
        print(f"Процент правильных ответов: {correct_percentage:.2f}%")
        print(f"Процент неправильных ответов: {wrong_percentage:.2f}%")
    elif play_again == "нет":
        print("Игра завершена.")
        break
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")
