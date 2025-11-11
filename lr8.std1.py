# Автор: Маліяд Р.О.
# Завдання: створити текстовий файл і записати прізвище та питання

def main():
    try:
        with open("students_questions.txt", "w", encoding="utf-8") as file:
            file.write("Студент 1: Маліяд.Р.О.\n")
            file.write("Питання: Що таке змінна у Python і як її оголосити?\n")
        print("Файл створено і заповнено успішно.")
    except Exception as e:
        print(f"Помилка під час роботи з файлом: {e}")

if __name__ == "__main__":
    main()

# Автор: Головчук Н.В 
# Завдання: Дописати у файл відповідь на питання Студента 1 та поставити своє питання

def main():
    try:
        with open("students_questions.txt", "a", encoding="utf-8") as file:
            file.write("\nСтудент 2: Головчук Н.В\n")

            file.write("Відповідь: Змінна у Python — це іменована область пам'яті, "
                       "у якій зберігається значення, яке може змінюватися. "
                       "Щоб оголосити змінну, достатньо присвоїти їй значення через оператор '='. "
                       "Наприклад: x = 10\n")
            file.write("Питання: Що таке список (list) у Python і як додати до нього елемент?\n")

        print("Дані успішно дописані у файл.")
    except FileNotFoundError:
        print("Помилка: файл students_questions.txt не знайдено.")
    except Exception as e:
        print(f"Сталася помилка під час роботи з файлом: {e}")

if __name__ == "__main__":
    main()
