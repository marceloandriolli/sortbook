import unittest
import requests
import json


class SortBooksAPI(unittest.TestCase):
    def setUp(self):
        self.API_VERSION = 'v1'
        self.API_URL = 'http://localhost:8000/api/{}'.format(
            self.API_VERSION
        )
        self.headers = {'Content-Type': 'application/json',
                        'Accept-Encoding': None}

    # Sort Books with title ascending
    def test_case_one(self):
        post_data = {
            "rules": [
                    {
                        'direction': "ascending",
                        'attribute': "title"
                    }
            ],
            'books': [
                    {
                        'title': "Java how to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    },
                    {
                        'title': "Patterns of Enterprise Aplication Architeture",
                        'author': "Martin Fowler",
                        'year': "2002"
                    },
                    {
                        'title': "Head First Design Patterns",
                        'author': "Elisabet Freeman",
                        'year': "2004"
                    },
                    {
                        'title': "Internet & World Wide: How to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    }
            ]
        }

        response = requests.post(
            '{url}/sort/books/'.format(url=self.API_URL),
            data=json.dumps(post_data), headers=self.headers, verify=False
        )

        data = response.json()

        test_data = [{
                     'title': "Head First Design Patterns",
                     'author': "Elisabet Freeman",
                     'year': "2004"
                     },
                     {
                     'title': "Internet & World Wide: How to program",
                     'author': "Deitel & Deitel",
                     'year': "2007"
                     },
                     {
                     'title': 'Java how to program',
                     'author': "Deitel & Deitel",
                     'year': "2007"
                     },
                     {
                     'title': "Patterns of Enterprise Aplication Architeture",
                     'author': "Martin Fowler",
                     'year': "2002"
                     }]

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, test_data)

    # Sort Books with author ascending and title descending
    def test_case_two(self):
        post_data = {
            "rules": [
                    {
                        'direction': "ascending",
                        'attribute': "author"
                    },
                    {
                        'direction': "descending",
                        'attribute': "title"
                    }
            ],
            'books': [
                    {
                        'title': "Java how to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    },
                    {
                        'title': "Patterns of Enterprise Aplication Architeture",
                        'author': "Martin Fowler",
                        'year': "2002"
                    },
                    {
                        'title': "Head First Design Patterns",
                        'author': "Elisabet Freeman",
                        'year': "2004"
                    },
                    {
                        'title': "Internet & World Wide: How to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    }
            ]
        }

        response = requests.post(
            '{url}/sort/books/'.format(url=self.API_URL),
            data=json.dumps(post_data), headers=self.headers, verify=False
        )

        data = response.json()

        test_data = [{
                     'title': "Patterns of Enterprise Aplication Architeture",
                     'author': "Martin Fowler",
                     'year': "2002"
                     },
                     {
                     'title': "Java how to program",
                     'author': "Deitel & Deitel",
                     'year': "2007"
                     },
                     {
                     'title': "Internet & World Wide: How to program",
                     'author': "Deitel & Deitel",
                     'year': "2007"
                     },
                     {
                     'title': "Head First Design Patterns",
                     'author': "Elisabet Freeman",
                     'year': "2004"
                     }]

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, test_data)

    # Sort Books with Year edition descending, author descending and
    # title ascending
    def test_case_three(self):
        post_data = {
            "rules": [
                    {
                        'direction': "descending",
                        'attribute': "year"
                    },
                    {
                        'direction': "descending",
                        'attribute': "author"
                    },
                    {
                        'direction': "ascending",
                        'attribute': "title"
                    }
            ],
            'books': [
                    {
                        'title': "Java how to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    },
                    {
                        'title': "Patterns of Enterprise Aplication Architeture",
                        'author': "Martin Fowler",
                        'year': "2002"
                    },
                    {
                        'title': "Head First Design Patterns",
                        'author': "Elisabet Freeman",
                        'year': "2004"
                    },
                    {
                        'title': "Internet & World Wide: How to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    }
            ]
        }

        response = requests.post(
            '{url}/sort/books/'.format(url=self.API_URL),
            data=json.dumps(post_data), headers=self.headers, verify=False
        )

        data = response.json()

        test_data = [{
                     'title': "Head First Design Patterns",
                     'author': "Elisabet Freeman",
                     'year': "2004"
                     },
                     {
                     'title': "Internet & World Wide: How to program",
                     'author': "Deitel & Deitel",
                     'year': "2007"
                     },
                     {
                     'title': "Java how to program",
                     'author': "Deitel & Deitel",
                     'year': "2007"
                     },
                     {
                     'title': "Patterns of Enterprise Aplication Architeture",
                     'author': "Martin Fowler",
                     'year': "2002"
                     }]

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, test_data)

    # Sort Books without any rules
    def test_case_four(self):
        post_data = {
            'books': [
                    {
                        'title': "Java how to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    },
                    {
                        'title': "Patterns of Enterprise Aplication Architeture",
                        'author': "Martin Fowler",
                        'year': "2002"
                    },
                    {
                        'title': "Head First Design Patterns",
                        'author': "Elisabet Freeman",
                        'year': "2004"
                    },
                    {
                        'title': "Internet & World Wide: How to program",
                        'author': "Deitel & Deitel",
                        'year': "2007"
                    }
            ]
        }

        response = requests.post(
            '{url}/sort/books/'.format(url=self.API_URL),
            data=json.dumps(post_data), headers=self.headers, verify=False
        )

        data = response.json()

        test_data = {'rules': ["This field is required."]}

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data, test_data)
