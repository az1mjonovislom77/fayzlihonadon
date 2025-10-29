from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from utils.models import HomePage, HomePageImage


class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    extra = 1


@admin.register(HomePage)
class HomePageAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
    inlines = [HomePageImageInline]
