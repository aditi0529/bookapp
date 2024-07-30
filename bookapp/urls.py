from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('add',views.addbook),
    path('list',views.booklist),
    path('savebook',views.savebook),
    path('delete/<rid>',views.deleteBook),
    path ('edit/<rid>',views.editBook)
    
]
