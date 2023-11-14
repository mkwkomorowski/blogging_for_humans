from . import models
from django.shortcuts import render


def render_something_from_model(request):

    a = 'blablabla'
    query_set = models.Model_01.objects.all()
    for model in query_set:
        a = model
    return render(request, 'blogging_for_humans.base.html', {'name': a})
