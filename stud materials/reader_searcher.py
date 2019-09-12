#программа перебирает текстовые документы - книги в библиотеке и ищет совпадения по словам
from os import listdir
books = listdir('HW_dict/HW_dict/books')

response = {}
for book in books:
    with open('HW_dict/HW_dict/books/' + book) as b:
        try:
            content = set(b.read().lower().replace(',',' ').replace('.',' ').split())
        except:
            print('error')
        else:
            for word in content:
                if word in response:
                    response[word].add(book)
                else:
                    response[word] = {book}

response['привет'] & response['гусь']