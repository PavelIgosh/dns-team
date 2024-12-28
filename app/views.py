from django.shortcuts import render
from .models import Manufacturer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# CRUD

class GoodListView(ListView):
    model = Manufacturer
    template_name = '.html'
    context_object_name = 'books'


class GoodCreateView(CreateView):
    model = Manufacturer
    template_name = '-.html'
    fields = "__all__"
    success_url = reverse_lazy('BookList')


class GoodDeleteView(DeleteView):
    model = Manufacturer
    template_name = "-.html"
    success_url = reverse_lazy('BookList')


class GoodUpdateView(UpdateView):
    model = Manufacturer
    template_name = '-.html'
    fields = "__all__"
    success_url = reverse_lazy('BookList')


class GoodDetailView(DeleteView):
    model = Manufacturer
    template_name = "-.html"
    context_object_name = 'book'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['smile'] = "`(*>﹏<*)′  ||||  (❁´◡`❁)"
    #     return context