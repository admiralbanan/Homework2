while True:
    pushkin_year = input("Введите год рождения А.С. Пушкина: ")
    if pushkin_year == "1799":
        # Спрашиваем день рождения, если год введен правильно
        while True:
            pushkin_day = input("Введите день рождения А.С. Пушкина (день месяца): ")
            if pushkin_day == "6":
                print("Верно")
                break
            else:
                print("Неверный день рождения, попробуйте снова.")
        break
    else:
        print("Неверный год рождения, попробуйте снова.")
