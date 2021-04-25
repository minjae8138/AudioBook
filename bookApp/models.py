from django.db import models


# Create your models here.

from django.db import models


class BookTb(models.Model):
    book_id = models.AutoField(db_column='BOOK_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('UserTb', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    book_name = models.CharField(db_column='BOOK_NAME', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOOK_TB'


class ContentTb(models.Model):
    content_id = models.AutoField(db_column='CONTENT_ID', primary_key=True)  # Field name made lowercase.
    sentence_id = models.IntegerField(db_column='SENTENCE_ID')  # Field name made lowercase.
    text = models.TextField(db_column='TEXT')  # Field name made lowercase.
    feeling = models.IntegerField(db_column='FEELING', blank=True, null=True)  # Field name made lowercase.
    book = models.ForeignKey(BookTb, models.DO_NOTHING, db_column='BOOK_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTENT_TB'


class UserTb(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=30, verbose_name="사용자 아이디")  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=30, verbose_name="비밀번호")  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=30, verbose_name="별명")  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50, verbose_name="이메일")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_TB'




