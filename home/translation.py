from modeltranslation.translator import register, TranslationOptions

from .models import Home, Qualities


@register(Home)
class HomeTranslation(TranslationOptions):
    fields = ('name', 'type', 'region', 'description')


@register(Qualities)
class QualitiesTranslation(TranslationOptions):
    fields = ('title',)
