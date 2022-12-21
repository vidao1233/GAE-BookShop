from django.urls import path
from . import views

app_name = 'store' #khi liên kết link thì đường dẫn sẽ có dạng "store:..."

urlpatterns = [
	path('', views.index, name = "index"), #Đường dẫn đến trang chủ index.html
	path('login', views.signin, name="signin"), #Đường dẫn đến trang đăng nhập sigin.html
	path('logout', views.signout, name="signout"), #Đường dẫn đến đăng xuất ->thoát khỏi tk 
	path('registration', views.registration, name="registration"), #đăng ký sigup.html
	path('book/<int:id>', views.get_book, name="book"), #sách book.html
	path('books', views.get_books, name="books"), #category.html
	path('category/<int:id>', views.get_book_category, name="category"),
	path('writer/<int:id>', views.get_writer, name = "writer"),
]
