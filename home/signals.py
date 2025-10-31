from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from decimal import Decimal
from .models import Basement, Home

def update_home_totals(home):
    if not home:
        return

    basements = Basement.objects.filter(home=home)
    if basements.exists():
        basement_total_price = sum(b.price or Decimal(0) for b in basements)
        basement_total_area = sum(b.area or Decimal(0) for b in basements)
        home.price = (home.area or Decimal(0)) * (home.pricePerSqm or Decimal(0))
        home.totalprice = (home.price or Decimal(0)) + basement_total_price
        home.totalarea = (home.area or Decimal(0)) + basement_total_area
    else:
        home.totalprice = Decimal(0)
        home.totalarea = Decimal(0)
    home.save(update_fields=["price", "totalprice", "totalarea"])


@receiver(post_save, sender=Basement)
def update_home_after_basement_save(sender, instance, **kwargs):
    update_home_totals(instance.home)


@receiver(post_delete, sender=Basement)
def update_home_after_basement_delete(sender, instance, **kwargs):
    update_home_totals(instance.home)
