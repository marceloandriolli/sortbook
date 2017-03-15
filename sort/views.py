# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sort import serializers

from operator import itemgetter


class SortBooks(APIView):
    """
    Sort Books by title, author or edition year
    """

    def post(self, request, format=None):
        serializer = serializers.BooksSerializer(data=request.data)
        if serializer.is_valid():
            # Get sended data
            data = serializer.validated_data
            # Get rules
            rules = data['rules']
            # Get list of sended books
            books = data['books']
            # Apply sort methedo by direction and attribute
            for _, rule in enumerate(rules):
                if rule.get('direction') == 'ascending':
                    direction = False
                elif rule.get('direction') == 'descending':
                    direction = True
                attr_key = rule.get('attribute')
                books = sorted(books, key=itemgetter(attr_key),
                               reverse=direction)
            return Response(books,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
