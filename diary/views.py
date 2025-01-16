from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from diary.forms import DiaryForm
from diary.models import Diary
from diary.services import get_articles_from_cache
from users.permissions import IsOwner
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated


def index(request):
    context = {'title': '"Мой дневник" личный электронный дневник'}
    return render(request, 'diary/index.html', context)


class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q', '')
        queryset = get_articles_from_cache().filter(owner=user)
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Архив записей'
        context
        return context


class DiaryCreateView(CreateView):
    model = Diary
    form_class = DiaryForm
    permission_classes = [IsAuthenticated]

    def form_valid(self, form):
        diary = form.save(commit=False)
        user = self.request.user
        diary.owner = user
        diary.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('diary:detail', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание записи'
        return context


class DiaryDetailsView(DetailView):
    model = Diary
    permission_classes = [IsOwner]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подробная информация записи'
        return context

    def get_queryset(self):
        return get_articles_from_cache()


class DiaryUpdateView(UpdateView):
    model = Diary
    form_class = DiaryForm

    def get_success_url(self):
        return reverse_lazy('diary:detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование записи'
        return context


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:list')
    permission_classes = [IsOwner]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление записи'
        return context
