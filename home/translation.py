from modeltranslation.translator import register, TranslationOptions

from .models import Home


@register(Home)
class HomeTranslation(TranslationOptions):
    fields = ('name', 'type', 'region', 'description', 'status', 'qualities')
