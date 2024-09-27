from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry, Category
from applications.favoritos.models import Favorites

# Create your views here.



class EntryListView(ListView):
    
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context =  super(EntryListView, self).get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        return context

    def get_queryset(self):
        # queryset = super(EntryListView, self).get_queryset()
        kword = self.request.GET.get('kword', '')
        categoria = self.request.GET.get('categoria', '')
        # connsulta de busqueda
        queryset = Entry.objects.buscar_entrada(kword, categoria)
        return queryset
    


class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['existe'] = Favorites.objects.comprobar_si_existe(self.request.user, self.object.id)
            return context
        return context
