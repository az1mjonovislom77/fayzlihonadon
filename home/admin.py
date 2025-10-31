from django.contrib import admin
from decimal import Decimal
from .models import (Home, HomeImage, FloorPlan, MasterPlan, InteriorPhotos, Basement, CommonHouseAdvImage,
                     CommonHouseMainImage, CommonHouse, CommonHouseAboutImage, CommonHouseAbout, InProgressImage,
                     InProgress)
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


class InProgressImageInline(admin.TabularInline):
    model = InProgressImage
    extra = 1


@admin.register(CommonHouse)
class CommonHouseAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'handover')
    list_filter = ('title',)
    inlines = [CommonHouseAdvInline, CommonHouseMainInline]


@admin.register(CommonHouseAbout)
class CommonHouseAboutAdmin(TranslationAdmin):
    list_display = ('id', 'projectarea', 'blocks', 'apartments', 'phases')
    list_filter = ('blocks',)
    inlines = [CommonHouseAboutInline]


@admin.register(InProgress)
class InProgressAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'progress', 'stage')
    inlines = [InProgressImageInline, ]


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'area', 'price', 'totalarea', 'totalprice', 'buildingBlock', 'home_number', 'status')
    list_filter = ('region', 'floor', 'buildingBlock', 'status')
    search_fields = ('name', 'region', 'description', 'floor', 'buildingBlock')
    inlines = [HomeImageInline, FloorPlanInline, MasterPlanInline, InteriorPhotosInline]

    def save_model(self, request, obj, form, change):
        from .models import Basement

        if obj.area and obj.pricePerSqm:
            obj.price = Decimal(obj.area) * Decimal(obj.pricePerSqm)

        basements = Basement.objects.filter(home=obj)

        if basements.exists():
            basement_total_price = sum(b.price or Decimal(0) for b in basements)
            basement_total_area = sum(b.area or Decimal(0) for b in basements)

            home_price = obj.price or Decimal(0)
            home_area = obj.area or Decimal(0)

            obj.totalprice = home_price + basement_total_price
            obj.totalarea = home_area + basement_total_area
        else:
            obj.totalprice = Decimal(0)
            obj.totalarea = Decimal(0)

        super().save_model(request, obj, form, change)


@admin.register(Basement)
class BasementAdmin(admin.ModelAdmin):
    list_display = ('id', 'home', 'area', 'pricePerSqm', 'price')

    def save_model(self, request, obj, form, change):
        if obj.area and obj.pricePerSqm:
            obj.price = Decimal(obj.area) * Decimal(obj.pricePerSqm)

        super().save_model(request, obj, form, change)

        if obj.home:
            obj.home.save()

    def delete_model(self, request, obj):
        home = obj.home
        super().delete_model(request, obj)

        if home:
            from .models import Basement
            basements = Basement.objects.filter(home=home)

            if basements.exists():
                total_price = sum(b.price or Decimal(0) for b in basements)
                total_area = sum(b.area or Decimal(0) for b in basements)
                home.price = (home.area or Decimal(0)) * (home.pricePerSqm or Decimal(0))
                home.totalprice = (home.price or Decimal(0)) + total_price
                home.totalarea = (home.area or Decimal(0)) + total_area
            else:
                home.totalprice = Decimal(0)
                home.totalarea = Decimal(0)

            home.save()


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
