from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def footer(request):
    template = loader.get_template('footer.html')
    return HttpResponse(template.render())

def heading(request):
    template = loader.get_template('heading.html')
    return HttpResponse(template.render())