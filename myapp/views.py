from django.shortcuts import render, HttpResponse

#dictionary data type
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ...'},
    {'id':2, 'title':'view', 'body':'View is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        #다음과 같이 반복하여 html 작성
        #<li>routing</li>
        #<li>view</li>
        #<li>model</li>
    return  f'''
    <html> 
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}            
        </ol>
        {articleTag}    
    </body>                   
    </html>
    '''

# Create your views here.
#클라이언트로 정보를 전달하기 위함 함수
#파라미터 : 요청
def index(requset):
    article = '''
    <h2>Welcome</h2>
        Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def create(requset):
    return HttpResponse('Create!')

def read(requset, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id): #들어오는값은 string이므로 int로 변환
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
    #return HttpResponse('Read!'+ id)