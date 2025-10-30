import json
from home.models import Home


def import_homes_from_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    model_fields = {field.name for field in Home._meta.get_fields()}
    created_count = 0

    for item in data:
        item.pop('id', None)

        if 'pricePerArea' in item:
            item['pricePerSqm'] = item.pop('pricePerArea')

        descriptions = {
            'description_uz': "Yorug‘, ekologik hududda joylashgan yaxshi rejalashtirilgan kvartira",
            'description_en': "Bright apartment with a good layout in an eco-friendly area",
            'description_ru': "Светлая квартира с хорошей планировкой в экологичном районе",
            'description_zh_hans': "明亮的公寓，布局合理，位于环保区域",
            'description_ar': "شقة مشرقة ذات تخطيط جيد في منطقة صديقة للبيئة",
        }
        item.update(descriptions)

        filtered = {k: v for k, v in item.items() if k in model_fields}

        Home.objects.create(**filtered)
        created_count += 1

    print(
        f"✅ {created_count} ta yozuv bazaga saqlandi (id e’tiborga olinmadi, 5 tildagi description maydonlari to‘ldirildi).")
