from django.template import Template, RequestContext
from django.http import HttpResponse

def index(request):
    return HttpResponse(Template("").render(RequestContext(request, {'a': 1000})))
