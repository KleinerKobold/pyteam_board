from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader

from .models import Person

# Create your views here.
def index(request):
    person_list = Person.objects.order_by("name_text")[:5]
    context = {'person_list': person_list}
    return render(request, 'team_member/index.html', context)

    
def detail(request, person_id):
    person = get_object_or_404(Person,pk=person_id)
    return render(request, "team_member/detail.html", {'person': person})

def experience(request, person_id):
    response = "You're looking at the experiences of person %s."
    return HttpResponse(response % person_id)

