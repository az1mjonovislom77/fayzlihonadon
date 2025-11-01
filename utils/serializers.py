from rest_framework import serializers
from datetime import date
from home.models import Home, CommonHouse
from .models import HomePageImage, HomePage, AdvertisementBannerImage, AdvertisementBanner, Reviews, WaitList, \
    SocialMedia, Contacts, AboutCompany


class HomePageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class HomePageSerializer(serializers.ModelSerializer):
    images = HomePageImageSerializer(many=True, required=False, source='homepageimage_set')

    class Meta:
        model = HomePage
        fields = ['id', 'title', 'title_uz', 'title_en', 'title_ru', 'title_zh_hans', 'title_ar', 'description',
                  'description_uz',
                  'description_en', 'description_ru', 'description_zh_hans', 'description_ar', 'images']

    def create(self, validated_data):
        request = self.context.get('request')

        image_files = request.FILES.getlist('images')
        validated_data.pop('homepageimage_set', None)
        homepage = HomePage.objects.create(**validated_data)
        for img in image_files:
            HomePageImage.objects.create(homepage=homepage, image=img)

        return homepage


class AdvertisementBannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementBannerImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class AdvertisementBannerSerializer(serializers.ModelSerializer):
    images = AdvertisementBannerImageSerializer(many=True, required=False, source='advertisementbannerimage_set')

    class Meta:
        model = AdvertisementBanner
        fields = ['id', 'title', 'title_uz', 'title_en', 'title_ru', 'title_zh_hans', 'title_ar', 'description',
                  'description_uz',
                  'description_en', 'description_ru', 'description_zh_hans', 'description_ar', 'images']

    def create(self, validated_data):
        request = self.context.get('request')

        image_files = request.FILES.getlist('images')
        validated_data.pop('advertisementbannerimage_set', None)
        advertisementbanner = AdvertisementBanner.objects.create(**validated_data)
        for img in image_files:
            AdvertisementBannerImage.objects.create(homepage=advertisementbanner, image=img)

        return advertisementbanner


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'rating', 'text', 'text_uz', 'text_en', 'text_ru', 'text_zh_hans', 'text_ar', 'full_name',
                  'address', 'image']


class WaitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitList
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class HomeFilterSerializer(serializers.Serializer):
    projectName = serializers.CharField(required=False)
    rooms = serializers.IntegerField(required=False)
    floorFrom = serializers.IntegerField(required=False)
    floorTo = serializers.IntegerField(required=False)
    areaFrom = serializers.DecimalField(required=False, max_digits=100, decimal_places=2)
    areaTo = serializers.DecimalField(required=False, max_digits=100, decimal_places=2)
    overDate = serializers.CharField(required=False)

    def filter_queryset(self):
        data = self.validated_data
        homes = Home.objects.all()

        if data.get("projectName"):
            homes = homes.filter(commonhouse__title__icontains=data["projectName"])
        if data.get("rooms"):
            homes = homes.filter(rooms=data["rooms"])
        if data.get("floorFrom") and data.get("floorTo"):
            homes = homes.filter(floor__gte=data["floorFrom"], floor__lte=data["floorTo"])
        elif data.get("floorFrom"):
            homes = homes.filter(floor__gte=data["floorFrom"])
        elif data.get("floorTo"):
            homes = homes.filter(floor__lte=data["floorTo"])
        if data.get("areaFrom") and data.get("areaTo"):
            homes = homes.filter(area__gte=data["areaFrom"], area__lte=data["areaTo"])
        elif data.get("areaFrom"):
            homes = homes.filter(area__gte=data["areaFrom"])
        elif data.get("areaTo"):
            homes = homes.filter(area__lte=data["areaTo"])
        if data.get("overDate"):
            try:
                year = int(data["overDate"])
                start_date = date(year, 1, 1)
                end_date = date(year, 12, 31)
                homes = homes.filter(overDate__range=(start_date, end_date))
            except ValueError:
                pass

        return homes
