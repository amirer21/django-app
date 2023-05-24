# django-app

## 1. Web Server와 Web Application의 차이

(django 프레임워크로 들어가기에 앞서...)

- Web Server(apache, nginx)는 미리 만들어둔 화면을 정적으로 응답한다.

- Web Application Server(django, flask, php, jsp)은 화면을 동적으로 생성하는 프로그램을 만들어도 가능하다.

동적으로 만들 웹 페이지의 경우에는 유지보수에 유리하다.
(하나만 바꾸어도 전체가 바뀌기 때문임)

## 2. 구조

- url.py : URL 라우팅

- manange.py : 유틸리티 파일

## 3. 실행 방법

> python manage.py runserver

또는 

> python3 manage.py runserver

## 4. 다른 포트로 실행하는 방법

뒤에 포트번호를 넣어서 실행한다.
> python manage.py runserver:8888


## 5. Including another URLconf
http://127.0.0.1/create 와 같이 URL의 path를 설정할 수 있다.

```python
urlpatterns = [  
    path('', views.index), #path없이, home(127.0.0.1) 접근했을때 views.py에 있는 함수 index로 위임
    path('create/', views.create), #create/로 접근했을때 views.py의 create 함수 호출
    path('read/<id>/', views.read) #read/1/로 접근 read/<id>/ <> 가변하는 값을 담을 수 있다
]
```