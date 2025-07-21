from django.db import models

class PaintProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class FootwearProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='footwear_images/')

    def __str__(self):
        return self.name

class FurnitureProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='furniture_images/')

    def __str__(self):
        return self.name

# Buyurtma statuslari
ORDER_STATUS_CHOICES = [
    ('yangi', 'Yangi'),
    ('qabul_qilingan', 'Qabul qilingan'),
    ('bekor_qilingan', 'Bekor qilingan'),
    # ('jarayonda', 'Jarayonda'),
    # ('tayyor', 'Tayyor'),
]
    
class OrderRequest(models.Model):
    product = models.ForeignKey('PaintProduct', on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='yangi')

    def __str__(self):
        return f"{self.full_name} - {self.product.name} x{self.quantity}"

class FootwearOrderRequest(models.Model):
    product = models.ForeignKey('FootwearProduct', on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='yangi')

    def __str__(self):
        return f"{self.full_name} - {self.product.name} x{self.quantity}"

class FurnitureOrderRequest(models.Model):
    product = models.ForeignKey('FurnitureProduct', on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='yangi')

    def __str__(self):
        return f"{self.full_name} - {self.product.name} x{self.quantity}"
