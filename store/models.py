from django.db import models


class WinStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.WinUser", models.CASCADE)  #
    store_address = models.CharField(max_length=200)
    store_name = models.CharField(max_length=100)
    store_reg_num = models.CharField(max_length=20)
    store_email = models.CharField(max_length=50)
    store_state = models.IntegerField(default=0)

    class Meta:
        # managed = False
        db_table = "win_store"


class WinStoreExcel(models.Model):
    store_excel_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(WinStore, models.CASCADE)  #
    store_excel = models.CharField(max_length=300)  #

    class Meta:
        # managed = False
        db_table = "win_store_excel"


class WinStoreUrl(models.Model):
    store_url_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(WinStore, models.CASCADE, related_name="storeUrl")  #
    store_map_url = models.CharField(max_length=300)

    class Meta:
        # managed = False
        db_table = "win_store_url"


class WinRevenue(models.Model):
    revenue_id = models.AutoField(primary_key=True)
    store = models.ForeignKey("WinStore", models.CASCADE, related_name="revenue")  #
    revenue_value = models.IntegerField()
    revenue_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = "win_revenue"


class WinSell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    store = models.ForeignKey("WinStore", models.CASCADE, related_name="storeSell")  #
    wine = models.ForeignKey("detail.WinWine", models.CASCADE)  #
    sell_reg_time = models.DateTimeField()
    sell_price = models.IntegerField()
    sell_promot = models.TextField()
    sell_state = models.IntegerField()

    class Meta:
        # managed = False
        db_table = "win_sell"
