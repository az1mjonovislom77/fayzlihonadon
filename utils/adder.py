# app/utils.py
import json
from home.models import Home  # model nomini sizniki bilan almashtiring

def import_homes_from_json(json_path):
    """
    JSON fayldagi ma'lumotlarni o‘qib, Home modeliga yozadi.
    - commonhouse maydonini butunlay e’tiborga olmaydi
    - faqat modelda mavjud bo‘lgan maydonlarni saqlaydi
    - modelda yo‘q maydonlarni tashlab yuboradi
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]  # agar bitta obyekt bo‘lsa, listga o‘giramiz

    # Modeldagi maydonlar nomlarini olish (commonhouse dan tashqari)
    model_fields = {field.name for field in Home._meta.get_fields() if field.name != 'commonhouse'}

    created_count = 0
    for item in data:
        # JSON ichidan faqat modelda borlarini olish
        filtered = {k: v for k, v in item.items() if k in model_fields}
        Home.objects.create(**filtered)
        created_count += 1

    print(f"{created_count} ta yozuv bazaga saqlandi (commonhouse va notanish maydonlar e’tiborga olinmadi).")
