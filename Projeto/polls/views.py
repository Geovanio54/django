from django.shortcuts import render
from django.template import loader
from .models import Emprestimo
from django.http import HttpResponse

def index(request):
    emprestimo = Emprestimo.objects.all()
    template = loader.get_template("polls/index.html")
    context = {
        "Emprestimo": emprestimo,
    }
    return HttpResponse(template.render(context, request))