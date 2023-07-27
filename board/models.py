from django.db import models

# from .models import Post


class WinBoard(models.Model):
    board_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.WinUser", models.CASCADE)  #
    board_title = models.CharField(max_length=150)
    board_reg_time = models.DateTimeField()
    board_content = models.TextField()
    board_read_count = models.IntegerField()
    board_ip = models.CharField(max_length=20)

    class Meta:
        #    managed = False
        db_table = "win_board"


class WinBoardImg(models.Model):
    board_img_id = models.AutoField(primary_key=True)
    board = models.ForeignKey(WinBoard, models.CASCADE)  #
    board_image = models.ImageField(max_length=150)

    class Meta:
        #   managed = False
        db_table = "win_board_img"


class WinComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    board = models.ForeignKey(WinBoard, models.CASCADE)
    user = models.ForeignKey("user.WinUser", models.CASCADE)  #
    comment_content = models.ImageField(max_length=500)
    comment_reg_time = models.DateTimeField()
    content_ip = models.CharField(max_length=20)

    class Meta:
        #    managed = False
        db_table = "win_comment"


class WinBoardLike(models.Model):
    board_like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.WinUser", models.CASCADE)
    board = models.ForeignKey(WinBoard, models.CASCADE)
    board_like_time = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = "win_board_like"
