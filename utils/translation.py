from modeltranslation.translator import register, TranslationOptions

from .models import HomePage, AdvertisementBanner, Reviews


@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(AdvertisementBanner)
class AdvertisementBannerTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(Reviews)
class ReviewsTranslation(TranslationOptions):
    fields = ('text',)
