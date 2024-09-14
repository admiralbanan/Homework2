# Цикл продолжается, пока не введут правильный год
while True:
    pushkin_year = input("Введите год рождения А.С. Пушкина: ")
    if pushkin_year == "1799":
        print("Верно")
        break
    else:
        print("Неверно, попробуйте снова.")
