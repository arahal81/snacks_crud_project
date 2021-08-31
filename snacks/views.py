from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Snack

# Create your views here.
def home(request):
    return render(request,'home.html')


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "purchaser", "description"]


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title", "purchaser", "description"]
    # reverse_lazy("snack_list")


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")