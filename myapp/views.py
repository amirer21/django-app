from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect #https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/

#dictionary data type
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ...'},
    {'id':2, 'title':'view', 'body':'View is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'}
]
#id 마지막이 3이므로 다음은 4
nextId = 4

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
        <ul>
            <li><a href="/create/">cheate</a></li>
        </ul>
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

def read(requset, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id): #들어오는값은 string이므로 int로 변환
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
    #return HttpResponse('Read!'+ id)

@csrf_exempt
#django csrf skip
#https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
def create(request):
    global nextId #global 함수 밖에서 이미 선언된 전역 변수를 가리킨다
    #print('request.method', request.method)
    if request.method == 'GET':
    #return HttpResponse('Create!')
    #submit을 눌렀을때 보내려는 주소는 action으로
    #method를 넣어주면 post방식으로 된다. 없다면 기본값은 get방식
        article = '''
        <form action action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        #print(request.POST['title'])
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}        
        topics.append(newTopic)
        url = '/read/'+str(nextId) #redirect
        nextId = nextId + 1
        #return HttpResponse(request.POST['title'])
        #return HttpResponse(HTMLTemplate('AAA'))
        return redirect(url)