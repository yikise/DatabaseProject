from django.db import models
from User.models import OrdinaryUser
from User.models import Administrator
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    itemId = models.AutoField(verbose_name='ItemID', primary_key=True)  # Field name made lowercase.
    seller = models.ForeignKey(OrdinaryUser, models.CASCADE, verbose_name='卖家')
    category = models.CharField(verbose_name='Category', max_length=50)
    itemName = models.CharField(verbose_name='ItemName', max_length=50)  # Field name made lowercase.
    purchaseYear = models.DecimalField(verbose_name='PurchaseYear', max_digits=4,
                                       decimal_places=0)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='物品价格')  # Field name made lowercase.
    item_photo = models.ImageField(upload_to='images/item', null=True, blank=True, verbose_name='ItemPhoto')
    itemDesc = models.CharField(max_length=200, blank=True, null=True, verbose_name='ItemDesc')
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name='Location')
    new_old_degree = models.IntegerField(choices=[(0, '旧'), (1, '较旧'), (2, '较新'), (3, '新')],
                                         verbose_name='新旧程度')  # Field name made lowercase.
    itemStatus = models.IntegerField(choices=[(0, '在售'), (1, '已售'), (2, '已被下架')], verbose_name='itemStatus')

    class Meta:
        ordering = ['itemId']
        db_table = 'item'
        verbose_name = "物品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.itemName

    def get_order_url(self):
        return reverse("Market:get_order", kwargs={'item_id': self.itemId})

    def admin_remove_url(self):
        return reverse("Market:admin_remove", kwargs={'item_id': self.itemId})


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='订单编号')
    item = models.ForeignKey(Item, models.CASCADE, verbose_name='物品')
    buyer = models.ForeignKey(OrdinaryUser, models.CASCADE, verbose_name='买家', related_name='buyer_orders')
    seller = models.ForeignKey(OrdinaryUser, models.CASCADE, verbose_name='卖家', related_name='seller_orders')
    order_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单价格')
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    order_status = models.IntegerField(choices=[(0, '未支付'), (1, '已支付'), (2, '已发货'), (3, '已送达')], default=0,
                                       verbose_name='订单状态')

    class Meta:
        ordering = ['-order_time']
        db_table = 'orders'
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name
