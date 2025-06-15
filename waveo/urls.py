from django.conf.urls.static import static
from django.urls import path

from api import settings
from . import views

app_name = 'waveo'
urlpatterns = [
    path("", views.home),
    path("create/<str:notes>", views.create),
    path("view/<str:name>", views.recall)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
