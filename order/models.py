from django.db import models
from store.models import Book
from django.contrib.auth.models import User


class Order(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE) #khách hàng
	name = models.CharField(max_length=30) #tên
	email = models.EmailField() 
	phone = models.CharField(max_length=16) 
	address = models.CharField(max_length=150)
	note = models.TextField(null = True, blank=True)  #Ghi chú
	payment_method = models.CharField(max_length = 20) #phương thức thanh toán
	payable = models.IntegerField() #tiền sách
	totalbook = models.IntegerField() #số lượng
	created = models.DateTimeField(auto_now_add=True) 
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False) #trạng thái

	class Meta:
		ordering = ('-created', )

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
