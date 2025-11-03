from home.models import Home, CommonHouse

def conn_commonhouse_by_id(commonhouse_id):
    try:
        commonhouse = CommonHouse.objects.get(id=commonhouse_id)
    except CommonHouse.DoesNotExist:
        print(f"❌ CommonHouse id={commonhouse_id} topilmadi.")
        return

    homes = list(Home.objects.all())
    for h in homes:
        h.commonhouse = commonhouse
    Home.objects.bulk_update(homes, ["commonhouse"])

    print(f"✅ {len(homes)} ta Home '{commonhouse.title}' (id={commonhouse_id}) bilan bog‘landi.")


#python manage.py shell

# from utils.connecter import conn_commonhouse_by_id
# conn_commonhouse_by_id(3)
