from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length = 100)
	 #ĐƯờng dẫn URL
	slug = models.SlugField(max_length = 150, unique=True ,db_index=True)#unique : đường dẫn duy nhất, db_index : tạo chỉ mục csdl
	create_at = models.DateTimeField(auto_now_add = True)#ngày khởi tạo  sp
	updated_at = models.DateTimeField(auto_now_add = True) #ngày cập nhập, chỉnh sửa
	#trả về tên sp dưới dạng chuỗi
	def __str__(self):
		return self.name
#Tác giả
class Writer(models.Model):
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length=150, unique=True ,db_index=True)
	bio = models.TextField()
	pic = models.FileField(upload_to = "writer/") #up load ảnh vào file tacgia
	create_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

#Sách
class Book(models.Model):
	#Khóa ngoại TacGia-SanPham(loại sách)
	writer = models.ForeignKey(Writer, on_delete = models.CASCADE)#on_delete : làm việc với khóa ngoại
	# models.CASCADE : Khi đối tượng được tham chiếu bị xóa thì sẽ xóa luôn các đối tượng tham chiếu
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length=100, db_index=True)
	price = models.IntegerField() #Giá của sp
	stock = models.IntegerField() #Giảm giá
	coverpage = models.FileField(upload_to = "coverpage/") #Up load file ảnh vào coverpage
	bookpage = models.FileField(upload_to = "bookpage/") #-----------------------bookpage
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	totalreview = models.IntegerField(default=1) #Đánh giá = text
	totalrating = models.FloatField(default=5) #đnáh giá = sao
	status = models.IntegerField(default=0) #Trạng thái trong kho
	description = models.TextField() #Phần giưới thiệu sách

	def __str__(self):
	    return self.name
#Đánh giá
class Review(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	review_star = models.IntegerField()
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
#Slide ử trang chủ
class Slider(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slideimg = models.FileField(upload_to = "slide/")

	def __str__(self):
		return self.title

class Book_New(models.Model):
	writer = models.ForeignKey(Writer, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length=100, db_index=True)
	price = models.IntegerField()
	stock = models.IntegerField()
	coverpage = models.FileField(upload_to = "coverpage/")
	bookpage = models.FileField(upload_to = "bookpage/")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	totalreview = models.IntegerField(default=1)
	totalrating = models.FloatField(default=5)
	status = models.IntegerField(default=0)
	description = models.TextField()

	def __str__(self):
	    return self.name