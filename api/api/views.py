import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.api.serialzers import BoardSerializer, UserSerializer, ListSerializer, NewListSerializer, NewCardSerializer, \
    CardSerializer
from api.models import Board, models, User, List, Card


@api_view(['Post'])
def register(request):
    if request.method == 'POST':
        new_User = User(username=request.data['username'], password=request.data['password'])
        new_User.password = make_password(new_User.password)
        serializer = UserSerializer(instance=new_User, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# User end
# -----------------------------------------------------------------------------------------------------------
# board start
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def all_board(request):
    board = Board.objects.all()
    serialized_board = BoardSerializer(board, many=True)
    return Response(serialized_board.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def board(request, id):
    try:
        board = Board.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)
    serialized_board = BoardSerializer(board, many=False)
    return Response(serialized_board.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def new_board(request):
    if request.method == 'POST':
        if 'name' in request.data and 'description' in request.data:
            new_board_data = {
                'name': request.data['name'],
                'description': request.data['description'],
                'author': request.user.id,
            }
            new_board_serializer = BoardSerializer(data=new_board_data)
            if new_board_serializer.is_valid():
                new_board_instance = new_board_serializer.save()
                new_board_instance.members.set([request.user])
                return Response(new_board_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(new_board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def board_add_user(request, id):
    try:
        board = Board.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)
    try:
        user_id = request.data.get('id')
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        if board.author == request.user:
            board.members.add(user_id)
            return Response({"detail": "User added to the board successfully."}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def board_remove_user(request, id):
    try:
        board = Board.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)
    try:
        user_id = request.data.get('id')
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if board.author == request.user:
            board.members.remove(user_id)
            return Response({"detail": "User remove to the board successfully."}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def board_update(request, id):
    try:
        board = Board.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        if board.author == request.user:
            new_board_data = {
                'name': request.data.get('name', board.name),
                'description': request.data.get('description', board.description),
            }
            board_serializer = BoardSerializer(board, data=new_board_data, partial=True)
            if board_serializer.is_valid():
                board_serializer.save()
                return Response(board_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def board_delete(request, id):
    try:
        board = Board.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if board.author == request.user:
            board.delete()
            return Response({"detail": "Board delete."}, status=status.HTTP_200_OK)
        return Response({"detail": "No good author."}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# board end
# -----------------------------------------------------------------------------------------------------------
# List start

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def all_list(request, id):
    try:
        lists = List.objects.filter(board=id)
    except List.DoesNotExist:
        return Response({"detail": "Lists not found."}, status=status.HTTP_404_NOT_FOUND)

    serialized_lists = NewListSerializer(lists, many=True)
    return Response(serialized_lists.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def new_list(request, id):
    if request.method == 'POST':
        try:
            board = Board.objects.get(id=id)
        except Board.DoesNotExist:
            return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)

        if not request.user in board.members.all():
            return Response({"detail": "You are no member"}, status=status.HTTP_404_NOT_FOUND)
        if 'name' in request.data:
            new_list_data = {
                'name': request.data['name'],
                'board': board.id
            }
            new_list_serializer = NewListSerializer(data=new_list_data)
            if new_list_serializer.is_valid():
                new_list_serializer.save()
                return Response(new_list_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(new_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list(request, id):
    try:
        list = List.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "List not found."}, status=status.HTTP_404_NOT_FOUND)
    serialized_list = ListSerializer(list, many=False)
    return Response(serialized_list.data)


@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def list_update(request, id):
    try:
        list = List.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "list not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        if request.user in list.board.members.all():
            new_list_data = {
                'name': request.data.get('name', list.name),
            }
            list_serializer = ListSerializer(list, data=new_list_data, partial=True)
            if list_serializer.is_valid():
                list_serializer.save()
                return Response(list_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def list_delete(request, id):
    try:
        list = List.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "list not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if request.user in list.board.members.all():
            list.delete()
            return Response({"detail": "list delete."}, status=status.HTTP_200_OK)
        return Response({"detail": "you are no member."}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# list end
# -----------------------------------------------------------------------------------------------------------
# Card start

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def all_card(request, id):
    try:
        cards = Card.objects.filter(list=id)
    except Card.DoesNotExist:
        return Response({"detail": "cards not found."}, status=status.HTTP_404_NOT_FOUND)

    serialized_cards = NewCardSerializer(cards, many=True)
    return Response(serialized_cards.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def new_card(request, id):
    if request.method == 'POST':
        try:
            list = List.objects.get(id=id)
        except List.DoesNotExist:
            return Response({"detail": "list not found."}, status=status.HTTP_404_NOT_FOUND)

        if not request.user in list.board.members.all():
            return Response({"detail": "You are no member"}, status=status.HTTP_404_NOT_FOUND)
        if 'name' in request.data and 'description' in request.data and 'importance' in request.data:
            new_card_data = {
                'name': request.data['name'],
                'description': request.data['description'],
                'importance': request.data['importance'],
                'list': list.id
            }
            new_card_serializer = NewCardSerializer(data=new_card_data)
            if new_card_serializer.is_valid():
                new_card_serializer.save()
                return Response(new_card_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(new_card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def card(request, id):
    try:
        card = Card.objects.get(id=id)
    except Card.DoesNotExist:
        return Response({"detail": "Card not found."}, status=status.HTTP_404_NOT_FOUND)
    serialized_card = CardSerializer(card, many=False)
    return Response(serialized_card.data)


@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def card_update(request, id):
    try:
        card = Card.objects.get(id=id)
    except Card.DoesNotExist:
        return Response({"detail": "card not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        if request.user in card.list.board.members.all():
            new_card_data = {
                'name': request.data.get('name', card.name),
                'description': request.data.get('description', card.description),
                'importance': request.data.get('importance', card.importance),
                'done': request.data.get('done', card.done),
            }
            card_serializer = NewCardSerializer(card, data=new_card_data, partial=True)
            if card_serializer.is_valid():
                card_serializer.save()
                return Response(card_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def card_delete(request, id):
    try:
        card = Card.objects.get(id=id)
    except Card.DoesNotExist:
        return Response({"detail": "Card not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if request.user in card.list.board.members.all():
            card.delete()
            return Response({"detail": "card delete."}, status=status.HTTP_200_OK)
        return Response({"detail": "you are no member."}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
