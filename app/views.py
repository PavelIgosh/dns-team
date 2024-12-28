from django.shortcuts import render
from .models import Goods
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# CRUD

class GoodListView(ListView):
    model = Goods
    template_name = 'good_list.html'
    context_object_name = 'goods'


class GoodCreateView(CreateView):
    model = Goods
    template_name = 'create_goods.html'
    fields = "__all__"
    success_url = reverse_lazy('main')


class GoodDeleteView(DeleteView):
    model = Goods
    template_name = "delete_goods.html"
    success_url = reverse_lazy('main')


class GoodUpdateView(UpdateView):
    model = Goods
    template_name = 'update_goods.html'
    fields = "__all__"
    success_url = reverse_lazy('BookList')


class GoodDetailView(DeleteView):
    model = Goods
    template_name = "read_goods.html"
    context_object_name = 'goods'
