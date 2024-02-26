from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from django.urls import path
app_name = 'api'

urlpatterns = [
    # user
    path('register/', views.register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.user, name='user_info'),

    # end
    # board
    path('boards/', views.all_board, name='all_board'),
    path('board/new/', views.new_board, name='new_board'),
    path('board/<str:id>/', views.board, name='board'),
    path('board/update/<str:id>/', views.board_update, name='board_update'),
    path('board/delete/<str:id>/', views.board_delete, name='board_delete'),
    path('board/add/user/<str:id>/', views.board_add_user, name='board_add_user'),
    path('board/remove/user/<str:id>/', views.board_remove_user, name='board_remove_user'),

    # end
    # list
    path('board/<str:id>/lists/', views.all_list, name='all_list'),
    path('board/<str:id>/list/new/', views.new_list, name='new_list'),
    path('list/<str:id>/', views.list, name='list'),
    path('list/update/<str:id>/', views.list_update, name='list_update'),
    path('list/delete/<str:id>/', views.list_delete, name='list_delete'),
    # end
    # card
    path('list/<str:id>/cards/', views.all_card, name='all_card'),
    path('list/<str:id>/card/new/', views.new_card, name='new_card'),
    path('card/<str:id>/', views.card, name='card'),
    path('card/update/<str:id>/', views.card_update, name='card_update'),
    path('card/delete/<str:id>/', views.card_delete, name='card_delete'),

]
