from django.contrib import admin
from django.urls import path
from python_blog.views import main
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<str:name>/", main),
    # Подключение python_blog.urls
    path("posts/", include("python_blog.urls")),
]
