from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # устанавливаем книге жанр
    def test_set_book_genre_creating_a_genre_for_a_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.set_book_genre('Дон Кихот', 'Комедии')
        assert collector.books_genre['Дон Кихот'] == 'Комедии'

    # получаем жанр книги по её имени
    def test_get_book_genre_identify_the_genre_of_a_book_by_its_title(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.set_book_genre('Дон Кихот', 'Комедии')
        assert collector.get_book_genre('Дон Кихот') == 'Комедии'

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_display_a_list_of_books_with_the_comedy_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.add_new_book('Двенадцать стульев')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Дон Кихот', 'Комедии')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_with_specific_genre('Комедии') == ['Дон Кихот', 'Двенадцать стульев']

    # получаем словарь books_genre
    def test_get_books_genre_output_a_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Дон Кихот', 'Комедии')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        expected_result = {
            'Дон Кихот': 'Комедии',
            'Шерлок Холмс': 'Детективы'
        }
        assert collector.get_books_genre() == expected_result

    # книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_get_books_for_children_books_with_age_ratings_are_not_included_in_the_list_of_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Дон Кихот', 'Комедии')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.genre_age_rating = {
           'Детективы': '16+'
        }
        result = collector.get_books_for_children()
        assert result == ['Дон Кихот']
        assert 'Шерлок Холмс' not in result

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_adding_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.add_book_in_favorites('Дон Кихот')
        assert 'Дон Кихот' in collector.favorites
        assert len(collector.favorites) == 1

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.add_book_in_favorites('Дон Кихот')
        collector.delete_book_from_favorites('Дон Кихот')
        assert 'Дон Кихот' not in collector.favorites

     # получаем список Избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.set_book_genre('Дон Кихот', 'Комедии')
        collector.add_book_in_favorites('Дон Кихот')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Дон Кихот']
        assert len(collector.favorites) == 1
        assert 'Дон Кихот' in favorites

    # у добавленной книги нет жанра
    def test_add_new_book_adding_a_book_without_a_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        assert len(collector.get_books_genre()) == 1
        assert 'Дон Кихот' in collector.get_books_genre()
        assert collector.get_book_genre('Дон Кихот') == ''