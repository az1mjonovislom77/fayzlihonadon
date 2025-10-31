from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from utils.models import HomePage, HomePageImage, AdvertisementBannerImage, AdvertisementBanner, Reviews, WaitList


class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    extra = 1


class AdvertisementBannerImageInline(admin.TabularInline):
    model = AdvertisementBannerImage
    extra = 1


@admin.register(HomePage)
class HomePageAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
    inlines = [HomePageImageInline]


@admin.register(AdvertisementBanner)
class AdvertisementBannerAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
    inlines = [AdvertisementBannerImageInline]


@admin.register(Reviews)
class ReviewsAdmin(TranslationAdmin):
    list_display = ('id', 'rating', 'text', 'full_name', 'address')


@admin.register(WaitList)
class WaitListAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'theme')
