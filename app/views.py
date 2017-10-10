from django.http import HttpResponse
from django.views import generic

from .models import Alias

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'alias_list'

    def get_queryset(self):
        return Alias.objects.all


def detail(request, alias_id):
    return HttpResponse("You're looking at alias %s." % alias_id)
