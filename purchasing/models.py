from django.db import models


class WinPurchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.WinUser", models.CASCADE)  #
    purchase_time = models.DateTimeField()
    purchase_number = models.IntegerField()
    purchase_price = models.IntegerField()

    class Meta:
        # managed = False
        db_table = "win_purchase"


class WinPurchaseDetail(models.Model):
    purchase_detail_id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(
        WinPurchase, models.CASCADE, related_name="purchasePurchaseDetail"
    )  #
    sell = models.ForeignKey(
        "store.WinSell", models.CASCADE, related_name="sellPurchaseDetail"
    )  #
    purchase_det_number = models.IntegerField()
    purchase_det_price = models.IntegerField()
    purchase_det_state = models.IntegerField()

    class Meta:
        #      managed = False
        db_table = "win_purchase_detail"


class WinCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.WinUser", models.CASCADE)  #
    cart_time = models.DateTimeField()
    cart_state = models.IntegerField()

    class Meta:
        #       managed = False
        db_table = "win_cart"


class WinCartDetail(models.Model):
    cart_det_id = models.AutoField(primary_key=True)
    sell = models.ForeignKey("store.WinSell", models.CASCADE)  #
    cart = models.ForeignKey("WinCart", models.CASCADE)  #
    cart_det_qnty = models.IntegerField()

    class Meta:
        #     managed = False
        db_table = "win_cart_detail"


class WinReceiveCode(models.Model):
    receive_code_id = models.AutoField(primary_key=True)
    purchase_detail = models.ForeignKey("WinPurchaseDetail", models.CASCADE)
    receive_code = models.BinaryField(max_length=500)

    class Meta:
        #     managed = False
        db_table = "win_receive_code"
