from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from utils.compressor import optimize_image_to_webp


def check_image_size(image):
    if image.size > 10 * 1024 * 1024:
        raise ValidationError("The image is too long")


class Home(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    pricePerSqm = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    area = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    totalFloors = models.IntegerField(blank=True, null=True)
    yearBuilt = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


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


class Qualities(models.Model):
    title = models.CharField(max_length=200)
    home = models.ForeignKey(Home, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


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
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    area = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    pricePerSqm = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def __str__(self):
        return f'{self.area} {self.price} {self.pricePerSqm}'
