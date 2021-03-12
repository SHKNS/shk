from django.db import models


class UnionBoard(models.Model):
    shop_url = models.CharField(primary_key=True, max_length=500)
    url = models.CharField(max_length=200)
    pro_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    delivery_fee = models.CharField(max_length=100, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'union_board'