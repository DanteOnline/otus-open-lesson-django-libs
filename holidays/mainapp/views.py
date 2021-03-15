from django.shortcuts import render
from .models import Holiday
from django.views.generic import ListView, DetailView


# Create your views here.
class HolidayList(ListView):
    model = Holiday

    def get_queryset(self):
        for _ in range(10):
            holidays = Holiday.objects.all()
            print(holidays)
        return super().get_queryset()


class HolidayDetailView(DetailView):
    model = Holiday
