from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Category, Writer, Book, Review, Slider
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import RegistrationForm, ReviewForm

#Trang chủ
def index(request):
    #Trả về sách và các slide theo thứ tự, lấy từ [:b] đầu tới b   
    newpublished = Book.objects.order_by('-created')[:15]
    slide = Slider.objects.order_by('-created')[:3]
    context = {
        "newbooks":newpublished,
        "slide": slide
    }
    #Trả về đối tượng HttpResponse : Trang chủ
    return render(request, 'store/index.html', context)

#Đăng nhập
def signin(request):
    #luôn luôn True,Đây là một cách để biết người dùng đã được xác thực hay chưa
    if request.user.is_authenticated:
        return redirect('store:index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                #Có sẵn của django
                #login()lưu ID của người dùng trong phiên, sử dụng khung phiên của Django.(sau khi đăng ký tc)
                login(request, auth)
                return redirect('store:index')
            else:
                #Sử dụng level erro của messages để báo lỗi nhập sai
            	messages.error(request, 'username and password doesn\'t match')
    #Trả về trang đnăg nhập
    return render(request, "store/login.html")	

#Đăng xuất
def signout(request):
    #Có sẵn của django
    #Khi bạn gọi logout(), dữ liệu phiên cho yêu cầu hiện tại hoàn toàn bị xóa sạch.
    #Tất cả dữ liệu hiện có sẽ bị xóa. 
    #Điều này nhằm ngăn người khác sử dụng cùng một trình duyệt web để đăng nhập 
    #và có quyền truy cập vào dữ liệu phiên của người dùng trước đó
    logout(request)
    #Sau khi logout thì chuyển đến trang chủ
    return redirect('store:index')	

#Đăng ký
def registration(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		form.save()
        #save xong sẽ chuyển đến trang đnăg nhập
		return redirect('store:signin')
    #trả về trangd dăng ký
	return render(request, 'store/signup.html', {"form": form})
#Thanh toán
def payment(request):
    return render(request, 'store/payment.html')

#Sách
def get_book(request, id):
    form = ReviewForm(request.POST or None)
    book = get_object_or_404(Book, id=id)
    rbooks = Book.objects.filter(category_id=book.category.id)
    r_review = Review.objects.filter(book_id=id).order_by('-created')
    #dữ liệu đánh giá của người dùng được chia thành 4 trang
    paginator = Paginator(r_review, 4)
    page = request.GET.get('page')
    rreview = paginator.get_page(page)
    #Đánh giá
    if request.method == 'POST':
        if request.user.is_authenticated: #đã xác thực người dùng
            if form.is_valid():
                temp = form.save(commit=False)
                temp.customer = User.objects.get(id=request.user.id)
                temp.book = book          
                temp = Book.objects.get(id=id)
                temp.totalreview += 1#tăng số đánh giá lên 1 nếu thành công
                temp.totalrating += int(request.POST.get('review_star'))#thay đổi số sao tb
                form.save()  
                temp.save()

            #THông báo mes khi đánh giá
                messages.success(request, "Đánh giá thành công!")
                form = ReviewForm()
        else:
            messages.error(request, "Cần đăng nhập trước khi đnáh giá.")
    context = {
        "book":book,
        "rbooks": rbooks,
        "form": form,
        "rreview": rreview
    }
    return render(request, "store/book.html", context)

#Loại sách
def get_books(request):
    books_ = Book.objects.all().order_by('-created')
    paginator = Paginator(books_, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, "store/category.html", {"book":books})
#Sản phẩm
def get_book_category(request, id):
    book_ = Book.objects.filter(category_id=id)
    paginator = Paginator(book_, 10)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, "store/category.html", {"book":book})
#Tác giả
def get_writer(request, id):
    wrt = get_object_or_404(Writer, id=id)
    book = Book.objects.filter(writer_id=wrt.id)
    context = {
        "wrt": wrt,
        "book": book
    }
    return render(request, "store/writer.html", context)


