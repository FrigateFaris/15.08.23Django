from django.shortcuts import render


# Create your views here.
from taskApp.models import Objective


def show_start_page(request):
    objective = Objective.objects.all()
    context = {'objective': objective}
    return render(request, 'main.html', context=context)


def show_create_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('name')
        date = request.POST.get('name')
        level = request.POST.get('name')
        status = request.POST.get('name')

        tasks = Objective.objects.create(name=name,
                                         description=description,
                                         date=date,
                                         level=level,
                                         status=status)

    return render(request, 'createTask')
