from django.shortcuts import render
from .forms import *
import datetime
from .models import *
import requests
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def home(request):
    post = Post.objects.all()
    return render(request, 'home.html')

# def post(request):
#     context ={}
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         print(form.instance)
#         url = "https://api.aiforthai.in.th/ssense"
#         text = form.instance
#         data = {'text':text}
#         headers = {
#             'Apikey': "3gCn6fXC0WwqfKGJbS309aWqnXiyyf1M"
#             }
#         response = requests.post(url, data=data, headers=headers)
#         result = (response.json()['sentiment']['polarity'])
#         if (result == 'negative'):
#             print('ลบ')
#             print(response.json())
#             form.save()
#             messages.warning(request,'ลบ')
#         else:
#             print('บวก')
#             print(response.json())
#             form.save()
#             messages.warning(request,'บวก')
#     context['form'] = form
#     return render(request,"post.html")

def contact(request):
    post = Post.objects.all()
    return render(request, 'contact.html')

def about(request):
    post = Post.objects.all()
    return render(request, 'about.html', {
        'post': post
    })

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST ,request.FILES)
        
        context = {}
        if form.is_valid():
            print (form.instance)
            moji_list =[['🙂','😄','😁','😆','😀','😊','😃'],
            ['😢','😥','😰','😓','🙁','😟','😞','😔','😣','😫','😩'],
            ['😡','😠','😤','😖'],
            ['🙄','😒','😑','😕'],
            ['😱'],
            ['😨','😧','😦'],
            ['😮','😲','😯'],
            ['😴','😪'],
            ['😋','😜','😝','😛'],
            ['😍','💕','😘','😚','😙','😗'],
            ['😌'],
            ['😐'],
            ['😷'],
            ['😳'],
            ['😵'],
            ['💔'],
            ['😎','😈'],
            ['🙃','😏','😂','😭'],
            ['😬','😅','😶'],
            ['😉'],
            ['💖','💙','💚','💗','💓','💜','💘','💛'],
            ['😇']]
            url = "https://api.aiforthai.in.th/emoji"
            text = form.instance
            params = {'text':text}
        
            headers = {
                'Apikey': "3gCn6fXC0WwqfKGJbS309aWqnXiyyf1M"
                }
            response = requests.get(url, params=params, headers=headers,)
    
            keys=response.json().keys()
            emoji = [moji_list[int(k)][0] for k in keys]
            print(emoji,keys)
            context['form']= form
            # return super().form_valid(form,)
 
        if form.is_valid():
            print (form.instance)
            url = "https://api.aiforthai.in.th/ssense"
            
            text = form.instance
            
            data = {'text':text}
            
            headers = {
                'Apikey': "3gCn6fXC0WwqfKGJbS309aWqnXiyyf1M"
                }
    
            response = requests.post(url, data=data, headers=headers)
            result = (response.json()['sentiment']['polarity'])
            if (result == 'negative' ):
                print('ลบ')
                print(response.json())
                            
            else:
                print('บวก')
                print(response.json())
        #return super().form_valid(form,)
            form.save()
            print(form)
            messages.success(request, 'เพิ่มสำเร็จ')
            return redirect('/about')
    else:
        form = PostForm()
    return render(request, 'post.html',
                  {
                      'form': form,
                  })

def login(request):
    return render(request, 'login.html')