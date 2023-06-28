from django.shortcuts import render

# Create your views here.
# основная логика передачи информации от сервера к клиенту.
#server side rendering- HTML страницы формируются на сервере и отправляются на браузер

def index_view(request):
    return render(request,'index.html')

def article_create_view(request):
    # print(request.GET)
    # print(request.POST)
    if request.method == "GET":
        return render(request,'create_article.html')
    elif request.method == "POST":
        context= {
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
            'body': request.POST.get('body')
        }
        return render(request,'article_detail.html',context)
