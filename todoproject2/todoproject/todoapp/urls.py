from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .import views

import todoapp

urlpatterns = [

   path('',views.demo,name='demo'),
   path('delete/<int:task_id>/',views.delete,name='delete'),
   path('update/<int:id>/',views.update,name='update')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)