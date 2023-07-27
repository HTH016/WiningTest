from django.db import models

class WinUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30 )
    user_grade = models.ForeignKey('WinUserGrade', models.DO_NOTHING, db_column='user_grade' )
    user_passwd = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    user_tel = models.CharField(max_length=20)
    user_reg_date = models.DateTimeField()
    user_point = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'win_user'

class WinUserGrade(models.Model):
    user_grade = models.IntegerField(primary_key=True )
    user_grade_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'win_user_grade'