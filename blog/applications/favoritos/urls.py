#
from django.urls import path
from . import views

app_name = "favorito_app"

urlpatterns = [
    path(
        'perfil/', 
        views.UserPageView.as_view(),
        name='Perfil',
    ),
    path(
        'favoritos/<pk>/', 
        views.AddFavoriteView.as_view(),
        name='Favoritos',
    ),
    path(
        'delete-favoritos/<pk>/', 
        views.FavoritesDeleteView.as_view(),
        name='Delete_Favoritos',
    ),
   
]