import os
from django.core.files import File
from home.models import Home, HomeImage


def home_images_room():
    target_name = "FAYZLI XONADONLAR KITOB"
    base_dir = "data/image"
    img1_path = os.path.join(base_dir, "1xona.jpg")
    img2_path = os.path.join(base_dir, "2xona.jpg")

    if not os.path.exists(img1_path):
        print(f"❌ Rasm topilmadi: {img1_path}")
        return
    if not os.path.exists(img2_path):
        print(f"❌ Rasm topilmadi: {img2_path}")
        return

    homes_1 = Home.objects.filter(name=target_name, rooms=1)
    homes_2 = Home.objects.filter(name=target_name, rooms=2)

    count1, count2 = 0, 0

    for home in homes_1:
        with open(img1_path, "rb") as img_file:
            HomeImage.objects.create(home=home, image=File(img_file, name="1xona.jpg"))
            count1 += 1

    for home in homes_2:
        with open(img2_path, "rb") as img_file:
            HomeImage.objects.create(home=home, image=File(img_file, name="2xona.jpg"))
            count2 += 1

    print(f"✅ {count1} ta (1 xona) uylarga '1xona.jpg' rasmi biriktirildi.")
    print(f"✅ {count2} ta (2 xona) uylarga '2xona.jpg' rasmi biriktirildi.")
