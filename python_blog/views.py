from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("Главная страница")


def catalog_posts(reqest):
    return HttpResponse("Каталог постов")


def post_detail(reqest, slug):
    return HttpResponse(f"Страница поста {slug}")


def catalog_categories(reqest):
    return HttpResponse("Каталог категорий")


def category_detail(reqest, slug):
    return HttpResponse(f"Страница категорий {slug}")


def catalog_tags(reqest):
    return HttpResponse("Каталог тегов")


def tag_detail(reqest, slug):
    return HttpResponse(f"Страница тега {slug}")