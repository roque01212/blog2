from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    View,
    DeleteView
)
from .models import Favorites
from applications.entradas.models import Entry

# Create your views here.


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'

    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)
    


class AddFavoriteView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        # recuperamos el usuario
        usuario = self.request.user
        entrada = Entry.objects.get(id = self.kwargs['pk'])
        # registramos favoritos
        Favorites.objects.create(
            user = usuario,
            entry = entrada
        ).save()
        return HttpResponseRedirect(reverse('favorito_app:Perfil'))
    



class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favorito_app:Perfil')

    