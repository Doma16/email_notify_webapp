from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tap, Day
from .forms import TapForm, DayForm

def home(request):
    return render(request, template_name='tapa/home.html')

class TapList(LoginRequiredMixin, ListView):
    model = Tap
    context_object_name = 'taps'
    template_name = 'tapa/home.html'

    paginate_by = 5

    def get_queryset(self):
        taps = Tap.objects.filter(user=self.request.user)
        taps = [ (x, list(Day.objects.filter(tap=x.pk))) for x in taps]
        return taps

def new_tap(request):
    if request.method == 'POST':
        form = TapForm(request.POST, instance=request.user)

        day_form = DayForm(request.POST)

        if form.is_valid() and day_form.is_valid():
            #form.save()

            send_date = request.POST['send_date'] if request.POST['send_date'] != '' else None
            t = Tap(title=request.POST['title'],
                    message=request.POST['message'],
                    send_date=send_date,
                    email_to=request.POST['email_to'],
                    user=request.user)
            
            t.save()

            day = request.POST['day']
            time = request.POST['time'] if request.POST['time'] != '' else None
            if time is not None and day != '':
                d = Day(day=day,
                        time=time,
                        tap=t)
                d.save()

            messages.success(request, f'Tap Tap!')
            return redirect('home')
    else:
        form = TapForm(instance=request.user)
        day_form = DayForm(request.POST)

    context = {
        'form': form,
        'day_form': day_form
    }

    return render(request, 'tapa/create_tap.html', context)
