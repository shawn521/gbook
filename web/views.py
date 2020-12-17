form django.shortcuts import render
form django.view.generic import ListVeiw, DetailView, CreateView
form django.urls import reverse_lazy
form .models import Message

class MwssageList(ListView):
    model=Message

class MessageDetail(DetailView):
    model=Message

class MessageCreate(CreateView):
    model=Message
    fields='__all__'
    success_url=reverse_lazy('msg_list')