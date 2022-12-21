from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):


	PAYMENT_METHOD_CHOICES = (
		('Tien Mat', 'Tien Mat'),
		('Momo','')
	)

	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES)

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'note', 'payment_method']
