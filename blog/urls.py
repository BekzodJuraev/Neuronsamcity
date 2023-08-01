from django.urls import path
from .views import *
urlpatterns=[

    path('',Home.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('category/<str:slug>',PostsByCategory.as_view(),name='category'),
    #path('teacher/<str:slug>',Teacher.as_view(),name='teacher'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('contact/', Contact.as_view(),name='contact'),
    path('register/', register,name='register'),
]

