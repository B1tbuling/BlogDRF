from django.urls import path
from .views import *

urlpatterns = [
    path('list/', PostAPIList.as_view()),
    path('create/', PostApiCreate.as_view()),
    #or you can do this
    #path('create/<int:pk>', PostAPIUpdate.as_view()),
    path('update/<int:pk>', PostAPIUpdate.as_view()),
    path('delete/<int:pk>', PostAPIDelete.as_view()),
    path('<int:pk>/', PostAPIDitail.as_view()),

    path('tag/list/', TagAPIListCreate.as_view()),
    path('tag/create/', TagAPIListCreate.as_view()),
]
