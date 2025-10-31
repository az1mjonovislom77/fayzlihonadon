from modeltranslation.translator import register, TranslationOptions

from .models import Home, CommonHouse, CommonHouseAbout, InProgress


@register(Home)
class HomeTranslation(TranslationOptions):
    fields = ('name', 'type', 'region', 'description', 'status', 'qualities')


@register(CommonHouse)
class CommonHouseTranslation(TranslationOptions):
    fields = ('title', 'description',)


@register(CommonHouseAbout)
class CommonHouseAboutTranslation(TranslationOptions):
    fields = ('description', 'apartments')


@register(InProgress)
class InProgressTranslation(TranslationOptions):
    fields = ('title', 'stage', 'description')
