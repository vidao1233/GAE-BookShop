from django import forms
#Cài đặt crispy_form : pip install django-crispy-forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review
#Giao diện - DangKy.html(Store\templates\Store\DangKy.html)
#tạo form Đăng ký và form viết đánh giá
#UserCreationForm : được sử dụng để tạo người dùng mới 
#Bao gồm tên user, mật khẩu 1 và 2 (nhập lại mật khẩu)
class RegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            #Hiển thị :
            'name',
            'email',
            'username',
            'password1',
            'password2'
        ]
    #lỗi email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('name')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(("Email này đã được sử dụng, vui lòng sử dụng email khác!"))
        return email
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.user_name = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ReviewForm(forms.ModelForm):
    review_star = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    review_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Viết đánh giá của bạn!'}))

    class Meta:
        model = Review
        fields = [
            'review_star',
            'review_text'
        ]
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    