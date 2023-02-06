from django.shortcuts import render, HttpResponse

#dictionary data type
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ...'},
    {'id':2, 'title':'view', 'body':'View is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'}
]


# Create your views here.
#클라이언트로 정보를 전달하기 위함 함수
#파라미터 : 요청
def index(requset):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        #다음과 같이 반복하여 html 작성
        #<li>routing</li>
        #<li>view</li>
        #<li>model</li>
    return HttpResponse(f'''
    <html> 
    <body>
        <h1>Django</h1>
        <ol>
            {ol}            
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>                   
    </html>
    ''')

def create(requset):
    return HttpResponse('Create!')

def read(requset, id):
    return HttpResponse('Read!'+ id)

#test