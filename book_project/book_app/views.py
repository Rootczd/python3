from django.shortcuts import render
from .models import *
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
# Create your views here.

def index(request):
# 接收到请求后，返回的内容就是book_app/index.html
    raise Exception('自定义异常')
    return render(request,'book_app/index.html')


def book(request):
    # 定义一个变量名，它的内容就是获取BookInfo类名所对应数据库表中的所有数据
    booklist = BookInfo.objects.all()    # 定义上下文，这个上下文是一个字典类型，里面有两个键值对
    context = {'Tem_title':'图书信息','Tem_booklist':booklist}
    # 给用户返回一个模板文件，同时给模板文件传入上下文中定义的内容，供模板文件中的模板标签使用
    return render(request,'book_app/book.html',context)

def renwu(request,bid):
 	# 接收到用户的 /renwu1/请求后，返回给用户一个模板文件：book_app/renwu1.html

    book = BookInfo.objects.get(id=int(bid))
    herolist = book.heroinfo_set.all()
    context = {'Tem_title':'人物信息','Tem_book':book.btitle,'Tem_herolist':herolist}
    return render(request, 'book_app/renwu.html',context)

def cookie_set(request):
#     创建HttpResponse对象
    Response = HttpResponse("<h1>设置Cook，请查看响应报文头</h1>")
    # 设置一个cookie
    Response.set_cookie("CookieKey","CookieValue")
    # 返回应答内容
    return Response

def cookie_get(request):
    if "CookieKey" in request.COOKIES:
        val = request.COOKIES["CookieKey"]
    else:
        val = "Cookie不存在"
    return HttpResponse(val)

def bianliang(request):
    dict = {'title':'字典键值'}
    book = BookInfo()
    book.btitle = '对象属性'
    context = {'dict':dict,'book':book}
    return render(request,'book_app/bianliang.html',context)


# 定义一个函数，它接收请求两个参数
def weizhi_url(request, value1, value2):
	# 构造上下文
      context = {'Tem_pos1':value1, 'Tem_pos2':value2}
      return render(request, 'book_app/weizhi_url.html', context)

def static_file(request):
    return render(request,'book_app/static-file.html')


def zhuanyi(request):
    context = ({'Tem_context':'<h1>hello world</h1>'})
    return render(request,"book_app/zhuanyi.html",context)


def page_test(request,Pnum):
    hero = HeroInfo.objects.all()
    danye = Paginator(hero,4)
    if Pnum == '':
        Pnum = 1
    page_renwu = danye.page(int(Pnum))
    # 获取所有的页码
    page_num = danye.page_range
    context = {"Tem_title":'人物详情页',"Tem_renwu":page_renwu,"Tem_pnum":page_num}
    return render(request,"book_app/page_renwu.html",context)


