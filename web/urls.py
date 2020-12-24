from django.urls import path
from .views import *

urlpatterns =[
    path('',MessageList.as_view(),name='msg_view'),
    path('<int:pk>/',MessageDetail.as_view(),name='msg_view'),
    path('create/',MessageCreate.as_view(),name='msg_create'),
]