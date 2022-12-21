from django.contrib import admin
from encodings import search_function
from .models import Category, Writer, Book, Slider,Book_New

#Hiển thị trên trang admin

#Sản phẩm
class AddCategory(admin.ModelAdmin):
	list_display = ['name', 'slug']#hiển thị tên và slug
	#ánh xạ từ tên sp sang slug
	prepopulated_fields = {'slug': ('name',)}
	#Tìm kiếm
	search_fields = ['name']
#Hiển thị lên trang admin
admin.site.register(Category, AddCategory)

#Tác giả
class AddWriter(admin.ModelAdmin):
	list_display = ['name', 'slug']#hiển thị tên và slug
	 #ánh xạ từ tên sp sang slug
	prepopulated_fields = {'slug': ('name',)}
	#Tìm kiếm
	search_fields = ['name']
#Hiển thị lên trang admin
admin.site.register(Writer, AddWriter)

#SÁCH
class AddBook(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock', 'status', 'created', 'updated']
    #kích hoạt bộ lọc trong thanh bên phải trong phần chỉnh sửa thêm sách của trang admin
	list_filter = ['status', 'created', 'updated']
    #các trường được liệt kê trong list_editable sẽ được hiển thị dưới dạng widget 
    #biểu mẫu trên trang danh sách thay đổi, 
    #cho phép người dùng chỉnh sửa và lưu nhiều hàng cùng một lúc.
	list_editable = ['price', 'stock', 'status']
	prepopulated_fields = {'slug': ('name',)}
	search_fields = ['name', 'price', 'stock', 'status']

admin.site.register(Book, AddBook)

class AddSlider(admin.ModelAdmin):
	list_display = ['title', 'created', 'updated']
	#list_editable = ['title',]

admin.site.register(Slider, AddSlider) 

class AddBooknew(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock', 'status', 'created', 'updated']
	list_filter = ['status', 'created', 'updated']
	list_editable = ['price', 'stock', 'status']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book_New, AddBooknew)