from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    instock = models.DecimalField(max_digits=10, decimal_places=2)
    sold = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name + ' ' + ('instock: {} sold: {}'.format(self.instock, self.sold))

    
class Staff(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    name = models.CharField(max_length=255, verbose_name='ชื่อ-นามสกุล')
    title = models.CharField(max_length=255, verbose_name='เรื่อง')
    detail = models.TextField(null=True, blank=True, verbose_name='รายละเอียด')
    email = models.CharField(max_length=255, verbose_name='อีเมล')
    done = models.BooleanField(default=False, verbose_name='ดำเนินการแล้ว')
    summary = models.TextField(null=True, blank=True, verbose_name='สรุปผล')

    def __str__(self):
        return self.title