from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.utils.safestring import mark_safe



from .models import Calendar, Saint, Prayer, Entry
def can_be_coverted(conversion, thing):
    try:
        conversion(thing)
    except:
        return False
    else: 
        return True

def index(request):
    return render(request, 'saints_website/index.html')

def saints(request):
    saints = Saint.objects.order_by('text')
    entries = Entry.objects.order_by('text')
    context = {'saints': saints,'entries':entries}
    return render(request, 'saints_website/saints.html', context)

def saint(request, saint_id):
    saint = Saint.objects.get(id=saint_id)
    entries = saint.entry_set.order_by('-date_added')
    context = {'saint':saint, 'entries':entries}
    return render(request, 'saints_website/saint.html', context)

def search_results(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('q')
        if query == '' or query == None:
            query = 'None'
            results = Saint.objects.filter(Q(text=query))
        elif can_be_coverted(int,query[:4]):
            results = Saint.objects.filter(Q(birth=query) | Q(death=query))
        else:
            results = Saint.objects.filter(Q(text=query))
    return render(request, 'saints_website/search_results.html', {'query': query, 'results': results})

def prayers(request):
    prayers = Prayer.objects.all()
    context = {'prayer':prayers}
    return render(request, 'saints_website/prayers.html', context)

def calendar(request):
    saints = Saint.objects.all()
    year = datetime.now().year
    current_day = str(datetime.now().day)
    
    months = ["","January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    month_days = ["", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    current_month = months[datetime.now().month] 
    month_day = []
    image = True
    first_color = 'secondary'
    second_color = 'primary'
    for i in range(month_days[datetime.now().month]):
        month_day.append(f"{i + 1}")
    if request.method == 'POST' and 'run_script' in request.POST: # link view
        from .viewfunctions import toggle
        image = toggle(image)
        first_color = 'primary'
        second_color = 'secondary'
    elif request.method == 'GET' and 'run_script' in request.GET: # picture view
        from .viewfunctions import toggle
        image = False
        image = toggle(image)
        first_color = 'secondary'
        second_color = 'primary'
   
    context = {'saints':saints,'month':current_month, 'days':month_day, 'year':year, 'image_view':image, 'first_color': first_color, 'second_color': second_color, 'current_day': current_day}
    return render(request, 'saints_website/calendar.html', context)

def switch_view(request):
    if request.method != 'POST':
        image = False
    else:
        image = True
    context = {'image_view':image}
    return render(request, 'saints_website/calendar.html', context)