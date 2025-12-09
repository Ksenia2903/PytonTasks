# TODO Найдите количество книг, которое можно разместить на дискете
capacity = 1.44 #Мбайт
pages = 100
lines = 50
symbols = 25
symbol_size = 4 #байт

book_size = symbol_size*symbols*lines*pages/1024**2 #Размер одной книги

amount_of_books = int(capacity//book_size)

print("Количество книг, помещающихся на дискету:", amount_of_books)
