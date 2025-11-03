from home.models import Home, CommonHouse

def connect_kitob_commonhouse(commonhouse_id):
    target_name = "FAYZLI XONADONLAR KITOB"

    try:
        commonhouse = CommonHouse.objects.get(id=commonhouse_id)
    except CommonHouse.DoesNotExist:
        print(f"❌ CommonHouse id={commonhouse_id} topilmadi.")
        return

    homes = Home.objects.filter(
        name_uz=target_name
    ) | Home.objects.filter(
        name_en=target_name
    ) | Home.objects.filter(
        name_ru=target_name
    ) | Home.objects.filter(
        name_zh_hans=target_name
    ) | Home.objects.filter(
        name_ar=target_name
    )

    count = homes.count()
    if count == 0:
        print(f"⚠️ '{target_name}' nomli uylar topilmadi.")
        return

    homes.update(commonhouse=commonhouse)

    print(f"✅ {count} ta uy '{target_name}' nomi bilan CommonHouse(id={commonhouse_id}) ga bog‘landi.")

# python manage.py shell

# from utils.connecter2 import connect_kitob_commonhouse
# connect_kitob_commonhouse(3)
