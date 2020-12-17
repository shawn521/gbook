from django,urls import
form .views import *

urlpatterns =[
    path('',MessageList.as_veiw(),name='msg_view'),
    path('<ink:pk>/',MessgeDetail.as_veiw(),name='msg_view'),
    path('create/',MessageCreate.as_view(),name=msg_create),
]