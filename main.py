# Написати клас "Книга", який містить властивості: "назва", "автор" та "рік видання".
# Додати метод для виведення інформації про книгу та метод для обчислення віку книги.
# Дане завдання виконуємо в командах по 2-3 (бажано по 2) з повним циклом
# використання GIT-a. Детальний опис ДЗ був в кінці уроку, за потреби перегляньте
# пояснення ще раз, запис є

class Book:

    def __init__(self, name, author, year_of_publication):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication

    def get_info(self):
        print(f'name = {self.name}\n'
              f'author = {self.author}\n'
              f'year_of_publication = {self.year_of_publication}')



