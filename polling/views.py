from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

# def list_view(request):
#     context = {'polls': Poll.objects.all()}
#     return render(request, 'polling/list.html', context)

class PollListView(ListView): # This "subclasses down" the ListView that django provides
    model = Poll
    template_name = 'polling/list.html' # not necessary, django will try to infer it and find it

class PollDetailView(DetailView):
    model = Poll
    template_name = 'polling/detail.html'
    # these parameters are enough to find a specific poll and inject it into the view we've created
    # But, we need to be able to accept post request also - receive the yes or no vote.
    # overriding - provide a post method in the class

    def post(self, request, *args, **kwargs):
        poll = self.get_object() # will see id number and retrieve indicated polll
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
        
        context = {'object': poll} # context variable name is object...?
        return render(request, 'polling/detail.html', context)

# def detail_view(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404

#     if request.method == "POST":
#         if request.POST.get("vote") == "Yes":
#             poll.score += 1
#         else:
#             poll.score -= 1
#         poll.save()

#     context = {'poll': poll}
#     return render(request, 'polling/detail.html', context)