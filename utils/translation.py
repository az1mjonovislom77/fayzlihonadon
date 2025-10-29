from modeltranslation.translator import register, TranslationOptions

from .models import HomePage


@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = ('title', 'description')
