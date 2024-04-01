from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
    path('todos/', include('todo.urls')),
    path("accounts/", include('allauth.urls')),
]
