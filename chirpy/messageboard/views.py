from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('messageboard/index.html')
    return HttpResponse(template.render({}, request))


def post_message(request):
    # TODO: check request is get/post
    # TODO: Write data into db
    return HttpResponse('Hello World')
