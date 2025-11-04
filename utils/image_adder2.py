import os
from django.core.files import File
from home.models import Home, InteriorPhotos


def rooms_photo():
    image_folder = "data/rooms"

    images = [
        f for f in os.listdir(image_folder)
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.svg', '.webp', '.heic', '.heif'))
    ]

    if not images:
        print("❌ Papkada hech qanday rasm topilmadi.")
        return

    homes = list(Home.objects.all())
    if not homes:
        print("❌ Bazada Home obyektlari topilmadi.")
        return

    total_images = len(images)
    total_homes = len(homes)

    print(f"🖼 {total_images} ta rasm topildi.")
    print(f"🏠 {total_homes} ta Home topildi.")
    print("⏳ Yuklanmoqda...")

    created_count = 0

    for home in homes:
        for image_name in images:
            image_path = os.path.join(image_folder, image_name)

            if not os.path.exists(image_path):
                print(f"⚠️ Rasm topilmadi: {image_name}")
                continue

            with open(image_path, "rb") as img_file:
                InteriorPhotos.objects.create(
                    home=home,
                    image=File(img_file, name=image_name)
                )
                created_count += 1

    print(f"✅ {created_count} ta InteriorPhotos muvaffaqiyatli yaratildi!")
