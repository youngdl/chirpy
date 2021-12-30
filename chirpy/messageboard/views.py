from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.template import loader


def index(request):
    template = loader.get_template('messageboard/index.html')
    return HttpResponse(template.render({}, request))


def post_message(request):
    # TODO: Write data into db
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    return HttpResponse('Hello World')
