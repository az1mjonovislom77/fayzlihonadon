from modeltranslation.translator import register, TranslationOptions

from .models import HomePage, AdvertisementBanner


@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(AdvertisementBanner)
class AdvertisementBannerTranslation(TranslationOptions):
    fields = ('title', 'description')
