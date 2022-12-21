#Tạo các thẻ và bộ mẫu
#Khi template sử dụng : {% load customerfunction %}
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Sum
from django.utils.safestring import mark_safe
from django import template
#template.Library, trong đó tất cả các thẻ và bộ lọc được đăng ký
register = template.Library()
#Phí ship cố định
shippingConst = 28000

#số lượng liện thị của text (tiểu sử, review,..)
@register.filter(name='text_short')
def text_short(value):
	temp = value[0:50]
	return temp
#Phí ship
@register.filter(name='shipping')
def shipping(value):
	return shippingConst
#Tổng tiền thanh toán
@register.filter(name='payabletotal')
def  payabletotal(value):
	return value+shippingConst
#Tính trung bình đánh giá sao
@register.filter(name='averagerating')
def averagerating(value, args):
	temp = value / args
	if int(temp + 0.5) > int(temp):
		temp = int(temp + 0.5)
	else:
		temp = int(temp)

	if temp > 5:
		temp = 5
		
	if temp == 1:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span>"
	elif temp == 2:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span>"
	elif temp == 3:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span>"
	elif temp == 4:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star'></span>"
	else:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span>"

	return mark_safe(temp1)

@register.filter(name='subtotal')
def subtotal(value, args):
	return value*args
