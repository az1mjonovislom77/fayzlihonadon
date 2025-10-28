import json

from rest_framework import serializers

from .models import Home, HomeImage, Qualities, Basement


class HomeImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = HomeImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class QualitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualities
        fields = ['id', 'title']


class BasementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basement
        fields = ['id', 'area', 'price', 'pricePerSqm']


class HomeSerializerGet(serializers.ModelSerializer):
    images = HomeImageSerializer(source='homeimage_set', many=True, required=False, read_only=True)
    qualities = QualitiesSerializer(source='qualities_set', many=True, required=False)

    class Meta:
        model = Home
        fields = ['id', 'name', 'price', 'pricePerSqm', 'area', 'rooms', 'floor', 'totalFloors', 'yearBuilt',
                  'description', 'type', 'region', 'images', 'qualities']


class HomeSerializerPost(serializers.ModelSerializer):
    images = HomeImageSerializer(source='homeimage_set', many=True, required=False)
    qualities = QualitiesSerializer(source='qualities_set', many=True, required=False)

    class Meta:
        model = Home
        fields = [
            'id', 'name', 'price', 'pricePerSqm', 'area', 'rooms',
            'floor', 'totalFloors', 'yearBuilt', 'description',
            'type', 'region', 'images', 'qualities'
        ]

    def create(self, validated_data):
        request = self.context.get('request')

        image_files = request.FILES.getlist('images')

        qualities_raw = request.data.get('qualities')

        validated_data.pop('homeimage_set', None)
        validated_data.pop('qualities_set', None)

        home = Home.objects.create(**validated_data)

        if image_files:
            for img in image_files:
                HomeImage.objects.create(home=home, image=img)

        if qualities_raw:
            try:
                qualities_data = json.loads(qualities_raw)
                for q in qualities_data:
                    Qualities.objects.create(home=home, title=q.get('title'))
            except Exception as e:
                print("❌ Qualities JSON parse error:", e)

        return home
