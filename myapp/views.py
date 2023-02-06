from django.shortcuts import render, HttpResponse

# Create your views here.
#클라이언트로 정보를 전달하기 위함 함수
#파라미터 : 요청
def index(requset):
    return HttpResponse('Welcome!')

def create(requset):
    return HttpResponse('Create!')

def read(requset, id):
    return HttpResponse('Read!'+ id)

#test