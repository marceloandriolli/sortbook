# Sort Book Assessment

The Book Sorting Service API, provide a sort book service by author, title and edition year.

### Dependences:
* Python 3.5+
* Pip 9.0.1
* Gunicorn 19.7
* Django 1.10+
* Django Rest Framework 3.6
* Requests 2.3
* Simplejson 3.10

### Install Dependeces:

To run Book Sorting Service API on linux production server with Ubuntu 16.04 operational system, follow that instruction below:

1) Install Pip:    
    ```sh
    $ sudo apt-get update && sudo apt-get -y upgrade
    $ sudo apt-get install python-pip
    ```

2) Install git:
    ```sh
    $ apt-get install git
    ```

3) Clone project repository:
    ```sh
    $ git clone git@github.com:marceloandriolli/sortbook.git
    ```
4) Install all python modules, libs and framework requirements:
    ```ssh
    $ cd sort_book
    $ pip install -r requirements.txt
    ```

### Run tests:

```ssh
$ python manage.py test
```

### Run Book Sorting Service API:
```ssh
$ gunicorn  -w 6 sort_books.wsgi
```

### Sorting Service API:
It's simple and easy use API, to sort a list of book  just make a POST request on that url. If client wants send a list of four book to sort by title on ascending direction for exemple :

The client must to send a http post request on endpoint(url):
```sh
http://yourserverdomain:8080/api/v1/sort/books/
```

Sending a JSON data format like this:
```json
{   
 "rules":[
        {
        "direction":"ascending",
        "attribute": "title"
        }
    ],
 "books": [
        {
        "title":"Java how to program",
        "author": "Deitel & Deitel",
        "year" : "2007"
        },
        {
        "title":"Patterns of Enterprise Aplication Architeture",
        "author": "Martin Fowler",
        "year" : "2002"
        },
        {
        "title":"Head First Design Patterns",
        "author": "Elisabet Freeman",
        "year" : "2004"
        },
        {
        "title":"Internet & World Wide: How to program",
        "author": "Deitel & Deitel",
        "year" : "2007"
        }       
    ] 
}
});
```

Reply must be a ```HTTP 201``` and ```json``` of sorted book list like this:
```json
[{"title":"Head First Design Patterns","author":"Elisabet Freeman","year":"2004"},{"title":"Internet & World Wide: How to program","author":"Deitel & Deitel","year":"2007"},{"title":"Java how to program","author":"Deitel & Deitel","year":"2007"},{"title":"Patterns of Enterprise Aplication Architeture","author":"Martin Fowler","year":"2002"}]
```

In that example, client sent a list of books in ```books``` and rules of sort in ```rules```. Books must be a list of books and each book must contain the fields: ```title```,```author``` and ```year```. The rules must be a list of rules, each ```rules``` must contain the fields ```direction``` that must be ```ascending``` or ```descending``` and  ``` attribute``` field that must be ```title```, ```author``` or ```year```. It also sort more the one rule, for exemplo sort by title and author:

```json
{   
 "rules":[
        {
        "direction":"ascending",
        "attribute": "author"
        },
        {
        "direction":"descending",
        "attribute": "title"
        }       
        
    ],
 "books": [
        {
        "title":"Java how to program",
        "author": "Deitel & Deitel",
        "year" : "2007"
        },
        {
        "title":"Patterns of Enterprise Aplication Architeture",
        "author": "Martin Fowler",
        "year" : "2002"
        },
        {
        "title":"Head First Design Patterns",
        "author": "Elisabet Freeman",
        "year" : "2004"
        },
        {
        "title":"Internet & World Wide: How to program",
        "author": "Deitel & Deitel",
        "year" : "2007"
        }       
    ] 
}
```

In that example, first it be sort by author and second by title. If client send a request without ```rules``` json field a error will occur and API reply error message:

```json
{"rules": ["This field is required."]}
```
