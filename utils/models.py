from django.db import models
from django.core.validators import FileExtensionValidator

from utils.compressor import check_image_size, optimize_image_to_webp


class HomePage(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.description}'


class HomePageImage(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='homepage/', validators=[
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
        return f'{self.homepage.title} {self.homepage.description}'


class AdvertisementBanner(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.description}'


class AdvertisementBannerImage(models.Model):
    advertisementbanner = models.ForeignKey(AdvertisementBanner, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='advertisementbanner/', validators=[
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
        return f'{self.advertisementbanner.title} {self.advertisementbanner.description}'


class Reviews(models.Model):
    rating = models.IntegerField(null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    full_name = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='reviews/', validators=[
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
        return str(self.full_name)
