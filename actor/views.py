from django.shortcuts import render, get_object_or_404, redirect
from actor.models import Actor
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .forms import ActorForm
from django.core.paginator import Paginator
# Create your views here.


def index(request):

    actors = Actor.objects.all()
    paginator = Paginator(actors, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/actor/actors.html', {'actors': page_obj})


def actor(request, pk):
    actor1 = get_object_or_404(Actor, pk=pk)
    return render(request, '../templates/actor/detail.html', {'actor': actor1})


class SearchActor(ListView):
    model = Actor
    template_name = "actor_search.html"

    def get_actor(self):
        query = self.request.GET.get("A")
        object_list = Actor.objects.filter(
            Q(name__icontains=query) | Q(last_name__icontains=query)
        )
        return object_list


def add_actor(request):

    actor_form = ActorForm()
    if request.method == "POST":
        actor_form = ActorForm(request.POST, request.FILES)
        if actor_form.is_valid():
            actors = actor_form.save()
            return redirect(index)
    context = {"actor_form": actor_form}
    return render(request, '../templates/actor/add_actor.html', context=context)