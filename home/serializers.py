from rest_framework import serializers

from .models import Home, HomeImage, Basement, FloorPlan, MasterPlan, InteriorPhotos, BasementImage, CommonHouse, \
    CommonHouseMainImage, CommonHouseAdvImage, CommonHouseAboutImage, CommonHouseAbout, InProgress, InProgressImage


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


class FloorPlanSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = FloorPlan
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class MasterPlanSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = MasterPlan
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class InteriorPhotosSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = InteriorPhotos
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class BasementImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = BasementImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class BasementSerializer(serializers.ModelSerializer):
    images = BasementImageSerializer(many=True, required=False, source='basementimage_set')

    class Meta:
        model = Basement
        fields = ['id', 'home', 'area', 'price', 'pricePerSqm', 'images']

    def create(self, validated_data):
        request = self.context.get('request')

        image_files = request.FILES.getlist('images')
        validated_data.pop('basementimage_set', None)
        basement = Basement.objects.create(**validated_data)
        for img in image_files:
            BasementImage.objects.create(basement=basement, image=img)

        return basement


class HomeSerializerGet(serializers.ModelSerializer):
    images = HomeImageSerializer(source='homeimage_set', many=True, required=False, read_only=True)
    floorplan = FloorPlanSerializer(source='floorplan_set', many=True, required=False)
    masterplan = MasterPlanSerializer(source='masterplan_set', many=True, required=False)
    interiorphotos = InteriorPhotosSerializer(source='interiorphotos_set', many=True, required=False)

    class Meta:
        model = Home
        fields = ['id', 'commonhouse', 'buildingBlock', 'overDate', 'qualities', 'qualities_uz', 'qualities_en',
                  'qualities_ru', 'qualities_zh_hans', 'qualities_ar', 'home_number', 'entrance', 'totalprice',
                  'totalarea', 'status', 'status_uz', 'status_en', 'status_ru', 'status_zh_hans', 'status_ar', 'name',
                  'name_uz', 'name_en', 'name_ru', 'name_zh_hans', 'name_ar', 'price', 'pricePerSqm', 'area', 'rooms',
                  'floor', 'totalFloors', 'yearBuilt', 'description', 'description_uz', 'description_en',
                  'description_ru', 'description_zh_hans', 'description_ar', 'type', 'type_uz', 'type_en', 'type_ru',
                  'type_zh_hans', 'type_ar', 'region', 'region_uz', 'region_en', 'region_ru', 'region_zh_hans',
                  'region_ar', 'images', 'floorplan', 'masterplan', 'interiorphotos', ]


class HomeSerializerPost(serializers.ModelSerializer):
    images = HomeImageSerializer(source='homeimage_set', many=True, required=False)
    floorplan = FloorPlanSerializer(source='floorplan_set', many=True, required=False)
    masterplan = MasterPlanSerializer(source='masterplan_set', many=True, required=False)
    interiorphotos = InteriorPhotosSerializer(source='interiorphotos_set', many=True, required=False)

    class Meta:
        model = Home
        fields = ['commonhouse', 'buildingBlock', 'overDate', 'qualities', 'qualities_uz', 'qualities_en',
                  'qualities_ru', 'qualities_zh_hans', 'qualities_ar', 'home_number', 'entrance', 'totalprice',
                  'totalarea', 'status', 'status_uz', 'status_en', 'status_ru', 'status_zh_hans', 'status_ar', 'name',
                  'name_uz', 'name_en', 'name_ru', 'name_zh_hans', 'name_ar', 'price', 'pricePerSqm', 'area', 'rooms',
                  'floor', 'totalFloors', 'yearBuilt', 'description', 'description_uz', 'description_en',
                  'description_ru', 'description_zh_hans', 'description_ar', 'type', 'type_uz', 'type_en', 'type_ru',
                  'type_zh_hans', 'type_ar', 'region', 'region_uz', 'region_en', 'region_ru', 'region_zh_hans',
                  'region_ar', 'images', 'floorplan', 'masterplan', 'interiorphotos', ]

    def create(self, validated_data):
        request = self.context.get('request')

        image_files = request.FILES.getlist('images')
        floorplan_files = request.FILES.getlist('floorplan')
        masterplan_files = request.FILES.getlist('masterplan')
        interior_files = request.FILES.getlist('interiorphotos')

        validated_data.pop('homeimage_set', None)
        validated_data.pop('floorplan_set', None)
        validated_data.pop('masterplan_set', None)
        validated_data.pop('interiorphotos_set', None)

        home = Home.objects.create(**validated_data)

        for img in image_files:
            HomeImage.objects.create(home=home, image=img)

        for img in floorplan_files:
            FloorPlan.objects.create(home=home, image=img)

        for img in masterplan_files:
            MasterPlan.objects.create(home=home, image=img)

        for img in interior_files:
            InteriorPhotos.objects.create(home=home, image=img)

        return home


class CommonHouseAdvImageSerailizers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CommonHouseAdvImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class CommonHouseMainImageSerailizers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CommonHouseMainImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class CommonHouseSerializer(serializers.ModelSerializer):
    commonadvimage = CommonHouseAdvImageSerailizers(source='commonhouseadvimage_set', many=True, required=False)
    commonmainimage = CommonHouseMainImageSerailizers(source='commonhousemainimage_set', many=True, required=False)

    class Meta:
        model = CommonHouse
        fields = ['title', 'title_en', 'title_uz', 'title_ru', 'title_zh_hans', 'title_ar', 'description',
                  'description_uz', 'description_en', 'description_ru', 'description_zh_hans', 'description_ar',
                  'handover', 'country', 'region', 'district', 'street', 'house', 'latitude', 'longitude',
                  'commonadvimage', 'commonmainimage']

    def create(self, validated_data):
        request = self.context.get('request')

        commonhouseadvimage_files = request.FILES.getlist('commonadvimage')
        commonhousemainimage_files = request.FILES.getlist('commonmainimage')

        validated_data.pop('commonhouseadvimage_set', None)
        validated_data.pop('commonhousemainimage_set', None)

        commonhouse = CommonHouse.objects.create(**validated_data)

        for img in commonhouseadvimage_files:
            CommonHouseAdvImage.objects.create(commonhouse=commonhouse, image=img)

        for img in commonhousemainimage_files:
            CommonHouseMainImage.objects.create(commonhouse=commonhouse, image=img)

        return commonhouse


class CommonHouseAboutImageSerailizers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CommonHouseMainImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class CommonHouseAboutSerializer(serializers.ModelSerializer):
    images = CommonHouseAboutImageSerailizers(source='commonhouseaboutimage_set', many=True, required=False)

    class Meta:
        model = CommonHouseAbout
        fields = [
            'id', 'commonhouse', 'description', 'description_uz', 'description_en', 'description_ru',
            'description_zh_hans', 'description_ar', 'blocks', 'apartments', 'apartments_uz', 'apartments_en',
            'apartments_ru', 'apartments_zh_hans', 'apartments_ar', 'phases', 'projectarea', 'images']

    def create(self, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')

        validated_data.pop('commonhouseaboutimage_set', None)

        commonhouseabout = CommonHouseAbout.objects.create(**validated_data)

        for img in images:
            CommonHouseAboutImage.objects.create(commonhouseabout=commonhouseabout, image=img)

        return commonhouseabout


class InProgressImageSerailizers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CommonHouseMainImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class InProgressSerializer(serializers.ModelSerializer):
    images = InProgressImageSerailizers(source='inprogressimage_set', many=True, required=False)

    class Meta:
        model = InProgress
        fields = ['id', 'title', 'title_en', 'title_uz', 'title_ru', 'title_zh_hans', 'title_ar', 'description',
                  'description_uz', 'description_en', 'description_ru', 'description_zh_hans', 'description_ar',
                  'address', 'progress', 'stage', 'stage_en', 'stage_uz', 'stage_ru', 'stage_zh_hans', 'stage_ar',
                  'overdate', 'latitude', 'longitude', 'images']

    def create(self, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')

        validated_data.pop('inprogressimage_set', None)

        inprogress = InProgress.objects.create(**validated_data)

        for img in images:
            InProgressImage.objects.create(inprogress=inprogress, image=img)

        return inprogress
