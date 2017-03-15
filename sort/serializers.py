from rest_framework import serializers


class RulesSerializer(serializers.Serializer):
    direction = serializers.CharField(max_length=20)
    attribute = serializers.CharField(max_length=10)


class BookSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=300, allow_blank=False,
                                  trim_whitespace=True)
    author = serializers.CharField(max_length=150, allow_blank=False,
                                   trim_whitespace=True)
    year = serializers.CharField(max_length=4)
    # direction = serializers.IntegerField(max_value=1, min_value=0)


class BooksSerializer(serializers.Serializer):
    rules = RulesSerializer(many=True)
    books = BookSerializer(many=True)
