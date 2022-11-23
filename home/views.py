from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.feature_extraction.text import _make_int_array

from .form import InputForm
from .XuLy import *
from .createLink import*
from .createCmp import*
#from .key import *

# Create your views here.

input = ""
contents = []
links = []
def index(request):
   return render(request, 'pages/home.html')

def get_input (request):
    global input ,links
    if request.method == 'POST':
        form = InputForm (request.POST) # tạo một thể hiện biểu mẫu và điền nó với dữ liệu từ yêu cầu:
        if(form.is_valid()):
            input = form.getInput()
            print("---input: ",input)
            input = Tien_xu_ly(input)
            print("---input sau khi xử lý: ",input)
            links= get_Link(input)
            createLink(links)

            return  HttpResponseRedirect('chooseWeb/')
    #if a GET (hoặc bất kỳ phương thức nào khác), chúng ta sẽ tạo một biểu mẫu trống
    else: 
        form = InputForm()        
    return render (request, 'pages/home.html', {'form': form})
def chooseWeb(request):
    return render(request, 'pages/links.html')
   
def cmp1(request):
    content = Scraping(links[0])
    ketqua = ThucThi(input,content)
    createCmp(input,content,ketqua)
    return render(request, 'pages/cmp.html')

def cmp2(request):
    content = Scraping(links[1])
    ketqua = ThucThi(input,content)
    createCmp(input,content,ketqua)
    return render(request, 'pages/cmp.html')

def cmp3(request):
    content = Scraping(links[2])
    ketqua = ThucThi(input,content)
    createCmp(input,content,ketqua)
    return render(request, 'pages/cmp.html')

def cmp4(request):
    content = Scraping(links[3])
    ketqua = ThucThi(input,content)
    createCmp(input,content,ketqua)
    return render(request, 'pages/cmp.html')

def cmp5(request):
    content = Scraping(links[4])
    ketqua = ThucThi(input,content)
    createCmp(input,content,ketqua)
    return render(request, 'pages/cmp.html')

  