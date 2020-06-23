from django.shortcuts import render, redirect
from .models import Medicine, DoseVariant, ScheduleRow
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def registration(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegistrationForm()

    return render(response, "registration/register.html", {"form": form})


@login_required
def schedule(request):
    user_medicines = request.user.medicine_set().all()
    schedule_rows = request.user.schedulerow_set().all()
    return render(request, 'schedule.html')


@login_required
def medicine_schedule(request):
    return render(request, 'medicine_schedule.html')
