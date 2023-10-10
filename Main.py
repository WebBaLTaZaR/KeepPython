from Notebook import Notebook


def main():
    print("Программа начала работу")
    notebook = Notebook()
    while True:
        print("\nОпции:")
        print("1. Список заметок")
        print("2. Прочитать заметку")
        print("3. Создать новую заметку")
        print("4. Изменить имеющуюся заметку")
        print("5. Удалить заметку")
        print("6. Выйти")
        choice = input("Выберите опцию: ")

        if choice == "1":
            notebook.list_notes()

        elif choice == "2":
            notebook.list_notes()
            index = int(
                input("Введите номер заметки, которую хотите прочитать: "))
            note = notebook.get(index)
            if note:
                print(note)
            else:
                print("Заметка не найдена")

        elif choice == "3":
            title = input("Введите название титула: ")
            content = input("Введите содержимое: ")
            notebook.create(title, content)

        elif choice == "4":
            notebook.list_notes()
            index = int(
                input("Выберите номер заметки, которую хотите удалить: "))
            current_note = notebook.get(index)
            if current_note:
                print(f"Актуальная запись: {current_note.title}")
                title = input(
                    "Напишите новое название титула (оставьте поле пустым, если менять не нужно): ")
                print(f"Актуальная запись: {current_note.content}")
                content = input(
                    "Напишите новое содержимое (оставьте поле пустым, если менять не нужно): ")
                notebook.edit(index, title=title or None, content=content or None)
                print("Заметка обновлена.")

        elif choice == "5":
            notebook.list_notes()  # Добавляем вывод списка заметок перед выбором
            index = int(
                input("Выберите номер заметки, которую хотите удалить: "))
            if notebook.delete(index):
                print("Заметка удалена.")
            else:
                print("Заметка, которую вы хотите удалить, не найдена.")

        elif choice == "6":
            break

        else:
            print("Что-то не так, попробуйте снова.")
    print("Программа завершила работу")


if __name__ == "__main__":
    main()
