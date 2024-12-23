from django.shortcuts import render
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class PollListView(LoginRequiredMixin, ListView):
    model = Poll
    template_name = "polling/list.html"


class PollDetailView(LoginRequiredMixin, DetailView):
    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"object": poll}
        return render(request, "polling/detail.html", context)
