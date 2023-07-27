# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WinBoard(models.Model):
    board_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    board_title = models.CharField(max_length=150)
    board_reg_time = models.DateTimeField()
    board_content = models.TextField()
    board_read_count = models.IntegerField()
    board_like = models.IntegerField()
    board_ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "win_board"


class WinBoardImg(models.Model):
    board_img_id = models.AutoField(primary_key=True)
    board = models.ForeignKey(WinBoard, models.DO_NOTHING)
    board_image = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = "win_board_img"


class WinCart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    cart_time = models.DateTimeField()
    cart_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = "win_cart"


class WinCartDetail(models.Model):
    cart_det_id = models.AutoField(primary_key=True)
    sell = models.ForeignKey("WinSell", models.DO_NOTHING)
    cart = models.ForeignKey(WinCart, models.DO_NOTHING)
    cart_det_qnty = models.IntegerField()

    class Meta:
        managed = False
        db_table = "win_cart_detail"


class WinComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    board = models.ForeignKey(WinBoard, models.DO_NOTHING)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    comment_content = models.CharField(max_length=500)
    comment_reg_time = models.DateTimeField()
    content_ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "win_comment"


class WinDetailView(models.Model):
    detail_view_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        blank=True,
        null=True,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    wine = models.ForeignKey("WinWine", models.DO_NOTHING)
    detail_view_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "win_detail_view"


class WinPointHis(models.Model):
    point_his_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    point_reg = models.DateTimeField()
    point_add = models.IntegerField()

    class Meta:
        managed = False
        db_table = "win_point_his"


class WinPurchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    purchase_time = models.DateTimeField()
    purchase_number = models.IntegerField()
    purchase_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = "win_purchase"


class WinPurchaseDetail(models.Model):
    purchase_detail_id = models.IntegerField(primary_key=True)
    purchase = models.ForeignKey(WinPurchase, models.DO_NOTHING)
    sell = models.ForeignKey("WinSell", models.DO_NOTHING)
    purchase_det_number = models.IntegerField()
    purchase_det_price = models.IntegerField()
    purchase_det_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = "win_purchase_detail"


class WinRevenue(models.Model):
    revenue_id = models.AutoField(primary_key=True)
    store = models.ForeignKey("WinStore", models.DO_NOTHING)
    revenue_value = models.IntegerField()
    revenue_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "win_revenue"


class WinReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    sell = models.ForeignKey("WinSell", models.DO_NOTHING)
    review_content = models.CharField(max_length=500)
    review_score = models.DecimalField(max_digits=2, decimal_places=1)
    review_reg_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "win_review"


class WinSearch(models.Model):
    search_id = models.AutoField(primary_key=True)
    user_id = models.CharField(
        max_length=30,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    search_word = models.CharField(max_length=200)
    search_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "win_search"


class WinSell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    store = models.ForeignKey("WinStore", models.DO_NOTHING)
    wine = models.ForeignKey("WinWine", models.DO_NOTHING)
    sell_reg_time = models.DateTimeField()
    sell_price = models.IntegerField()
    sell_promot = models.TextField()
    sell_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = "win_sell"


class WinStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "WinUser",
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    store_address = models.CharField(max_length=200)
    store_name = models.CharField(max_length=100)
    store_reg_num = models.CharField(unique=True, max_length=20)
    store_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "win_store"


class WinStoreExcel(models.Model):
    store_excel_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(WinStore, models.DO_NOTHING)
    store_excel = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = "win_store_excel"


class WinStoreUrl(models.Model):
    store_url_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(WinStore, models.DO_NOTHING)
    store_map_url = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = "win_store_url"


class WinUser(models.Model):
    user_id = models.CharField(
        primary_key=True,
        max_length=30,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    user_grade = models.ForeignKey(
        "WinUserGrade",
        models.DO_NOTHING,
        db_column="user_grade",
        db_comment="-1 / Ż�� ȸ��\r\n1 / �Ϲ� ȸ��\r\n2 / ���� ȸ��(�Ϲ� ȸ�� + ���� �߰� ����)",
    )
    user_passwd = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    user_tel = models.CharField(max_length=20)
    user_reg_date = models.DateTimeField()
    user_point = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "win_user"


class WinUserFavorite(models.Model):
    fav_user_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        WinUser,
        models.DO_NOTHING,
        db_comment="ȸ��-��ȸ�� �����ؼ� �˻� Ű���带 ����-��� �Ͻô� ��� id �÷��� �ܷ�Ű�� �Ǹ� ��ȸ���� ���� row ����� �Ұ����մϴ�",
    )
    fav_wine_color = models.IntegerField()
    fav_alc = models.IntegerField(db_comment="(�ַ� ����)")
    fav_numbwith = models.IntegerField()
    fav_sweet = models.IntegerField()
    fav_bitter = models.IntegerField()
    fav_sour = models.IntegerField()
    fav_season = models.IntegerField()
    fav_food = models.IntegerField()

    class Meta:
        managed = False
        db_table = "win_user_favorite"


class WinUserGrade(models.Model):
    user_grade = models.IntegerField(
        primary_key=True,
        db_comment="-1 / Ż�� ȸ��\r\n1 / �Ϲ� ȸ��\r\n2 / ���� ȸ��(�Ϲ� ȸ�� + ���� �߰� ����)",
    )
    user_grade_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = "win_user_grade"


class WinWine(models.Model):
    wine_id = models.AutoField(primary_key=True)
    wine_name = models.CharField(max_length=150)
    wine_sort = models.IntegerField()
    wine_capacity = models.IntegerField(blank=True, null=True)
    wine_alc = models.DecimalField(max_digits=3, decimal_places=1)
    wine_dangdo = models.IntegerField()
    wind_sando = models.IntegerField()
    wine_tannin = models.IntegerField()
    wine_food = models.IntegerField()
    wine_image = models.CharField(max_length=200)
    wine_region = models.ForeignKey("WinWineRegion", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "win_wine"


class WinWineRegion(models.Model):
    wine_region_id = models.IntegerField(primary_key=True)
    wine_region = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "win_wine_region"
