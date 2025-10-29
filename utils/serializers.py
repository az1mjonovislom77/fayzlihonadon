from rest_framework import serializers

from .models import HomePageImage, HomePage, AdvertisementBannerImage, AdvertisementBanner


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
