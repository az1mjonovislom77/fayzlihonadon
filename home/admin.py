from django.contrib import admin
from .models import (Home, HomeImage, FloorPlan, MasterPlan, InteriorPhotos, Basement, CommonHouseAdvImage,
                     CommonHouseMainImage, CommonHouse, CommonHouseAboutImage, CommonHouseAbout, )
from modeltranslation.admin import TranslationAdmin


class HomeImageInline(admin.TabularInline):
    model = HomeImage
    extra = 1


class FloorPlanInline(admin.TabularInline):
    model = FloorPlan
    extra = 1


class MasterPlanInline(admin.TabularInline):
    model = MasterPlan
    extra = 1


class InteriorPhotosInline(admin.TabularInline):
    model = InteriorPhotos
    extra = 1


class CommonHouseAdvInline(admin.TabularInline):
    model = CommonHouseAdvImage
    extra = 1


class CommonHouseMainInline(admin.TabularInline):
    model = CommonHouseMainImage
    extra = 1


class CommonHouseAboutInline(admin.TabularInline):
    model = CommonHouseAboutImage
    extra = 1


@admin.register(CommonHouse)
class CommonHouseAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'handover')
    list_filter = ('title',)
    inlines = [CommonHouseAdvInline, CommonHouseMainInline]


@admin.register(CommonHouseAbout)
class CommonHouseAdmin(TranslationAdmin):
    list_display = ('id', 'projectarea')
    list_filter = ('blocks',)
    inlines = [CommonHouseAboutInline]


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'price', 'area', 'home_number', 'buildingBlock')
    list_filter = ('region', 'floor', 'buildingBlock')
    search_fields = ('name', 'region', 'description', 'floor', 'buildingBlock')
    inlines = [HomeImageInline, FloorPlanInline, MasterPlanInline, InteriorPhotosInline]


@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'home')
    search_fields = ('home__name',)


@admin.register(FloorPlan)
class FloorPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'home')


@admin.register(MasterPlan)
class MasterPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'home')


@admin.register(InteriorPhotos)
class InteriorPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'home')


@admin.register(CommonHouseMainImage)
class CommonHouseMainImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'commonhouse')


@admin.register(CommonHouseAdvImage)
class CommonHouseAdvImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'commonhouse')


@admin.register(Basement)
class BasementAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'price', 'pricePerSqm')
