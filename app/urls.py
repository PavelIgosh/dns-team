from django.urls import path
from .views import (GoodListView, GoodCreateView, GoodDeleteView,
                    GoodUpdateView, GoodDetailView)


urlpatterns = [
    path('main/', GoodListView.as_view(), name='main'),
    path('create/', GoodCreateView.as_view(), name='GoodCreate'),
    path('delete/<int:pk>', GoodDeleteView.as_view(), name='GoodDelete'),
    path('update/<int:pk>', GoodUpdateView.as_view(), name='GoodUpdate'),
    path('detail/<int:pk>', GoodDetailView.as_view(),name='GoodDetail'),
]