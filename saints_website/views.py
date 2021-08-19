from django.shortcuts import render

from .models import Saint

def index(request):
    return render(request, 'saints_website/index.html')

def saints(request):
    topics = Saint.objects.order_by('date_added')
    context = {'saints': saints}
    return render(request, 'saints_website/saints.html', context)

def saint(request, text):
    topic = Saint.objects.get(id=text)
    entries = saint.entry_set.order_by('-date_added')
    context = {'saint':saint, 'entries':entries}
    return render(request, 'saints_website/saint.html', context)
