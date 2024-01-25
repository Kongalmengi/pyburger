# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def main(request):
    #return HttpResponse("안녕하세요, pyburger입니다.")
    return render(request, "main.html")

# 교재 p.48
def burger_list(request):
    # burgers = Burger.objects.all() # 데이터 베이스(DB)에서 정보를 가져옴
    burgers = Burger.objects.all().values()
    print("전체 햄버거 목록:", burgers)
    # print("전체 햄버거 목록:", burgers)
    # Template
    context = {
        "burgers" : burgers,
    }

    return render(request, "burger_list.html", context)

def burger_search(request):
    # print(request.GET)
    keyword = request.GET.get("keyword")
    # print(keyword)

    # keyword가 주어졌을 때와 그렇지 않을 때 조건문
    if keyword is not None: # 키워드가 주어지면,
        burgers = Burger.objects.filter(name__contains=keyword)
    # print(burgers)
        
    else: # 키워드가 주어지지 않으면
        burgers = Burger.objects.none()

    # 결과값을 html로 보내주기 : 데이터 전달
    context = {
        "burgers" : burgers
    }

    return render(request, "burger_search.html", context = context)