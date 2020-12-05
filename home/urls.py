from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from home import views
urlpatterns = [
    path('', views.Index.as_view()),
    ]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)