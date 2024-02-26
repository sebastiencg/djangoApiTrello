from rest_framework.serializers import ModelSerializer

from api.models import Board, User, List, Card


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'author', 'datetime', 'members']
        extra_kwargs = {'members': {'required': False, 'allow_null': True}}


class ListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'board', 'datetime']

    board = BoardSerializer()


class NewListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'board', 'datetime']


class NewCardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'list', 'datetime', 'importance', 'done']


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'list', 'datetime', 'importance', 'done']

    list = NewListSerializer()
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', ]
