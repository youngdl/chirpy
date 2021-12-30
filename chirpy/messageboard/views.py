from django.http import HttpResponse, HttpRequest
from django.http.response import HttpResponseNotAllowed
from django.template import loader
from chirpy.messageboard import models
from django.utils import timezone

def index(request):
    template = loader.get_template('messageboard/index.html')
    return HttpResponse(template.render({}, request))


def post_message(request: HttpRequest):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    post_text = request.POST.get('message')
    post_user_name = request.POST.get('user_name')
    entry = models.Entry(message=post_text, user_name=post_user_name, pub_date=timezone.now())
    entry.save()
    return HttpResponse('Hello World')
