from django.db import models
from django.core.validators import FileExtensionValidator

from utils.compressor import optimize_image_to_webp, check_image_size


class CommonHouse(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=500)
    handover = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    house = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class CommonHouseAdvImage(models.Model):
    commonhouse = models.ForeignKey(CommonHouse, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='commonadvimage/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.commonhouse.title


class CommonHouseMainImage(models.Model):
    commonhouse = models.ForeignKey(CommonHouse, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='commonmainimage/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.commonhouse.title


class CommonHouseAbout(models.Model):
    commonhouse = models.ForeignKey(CommonHouse, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    blocks = models.IntegerField(default=0)
    apartments = models.IntegerField(default=0)
    phases = models.IntegerField(default=0)
    projectarea = models.DecimalField(max_digits=100, decimal_places=2, default=0)


class CommonHouseAboutImage(models.Model):
    commonhouseabout = models.ForeignKey(CommonHouseAbout, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='commonaboutimage/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.commonhouseabout.blocks)


class Home(models.Model):
    commonhouse = models.ForeignKey(CommonHouse, on_delete=models.SET_NULL, null=True, blank=True)
    buildingBlock = models.CharField(null=True, blank=True, max_length=200)
    qualities = models.JSONField(null=True, blank=True, max_length=500)
    home_number = models.CharField(null=True, blank=True)
    entrance = models.IntegerField(null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)
    totalarea = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
    pricePerSqm = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
    area = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    totalFloors = models.IntegerField(blank=True, null=True)
    yearBuilt = models.DateField(blank=True, null=True, auto_now_add=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class HomeImage(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.home.name

    class Meta:
        db_table = 'homeimage'
        verbose_name = 'Home image'
        verbose_name_plural = 'Home images'


class FloorPlan(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='floorplan/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.home.name

    class Meta:
        db_table = 'floorplanimage'
        verbose_name = 'FloorPlan image'
        verbose_name_plural = 'FloorPlan images'


class MasterPlan(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='masterplan/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.home.name

    class Meta:
        db_table = 'masterplanimages'
        verbose_name = 'MasterPlan image'
        verbose_name_plural = 'MasterPlan images'


class InteriorPhotos(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='interiorphotos/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.home.name

    class Meta:
        db_table = 'interiorphotos'
        verbose_name = 'InteriorPhotos image'
        verbose_name_plural = 'InteriorPhotos images'


class Basement(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, null=True, blank=True)
    area = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    pricePerSqm = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def __str__(self):
        return self.home.name


class BasementImage(models.Model):
    basement = models.ForeignKey(Basement, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='basement/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']),
        check_image_size])

    def save(self, *args, **kwargs):
        if self.image and not str(self.image.name).endswith('.webp'):
            optimized_image = optimize_image_to_webp(self.image, quality=80)
            self.image.save(optimized_image.name, optimized_image, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.basement.home.name

    class Meta:
        db_table = 'basementimage'
        verbose_name = 'Basement image'
        verbose_name_plural = 'Basement images'
