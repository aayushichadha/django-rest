from django.shortcuts import render
from .forms import PostForm
from snippets.models import Number
from django.db.models import Max


def check(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            num = request.POST.get('num', '')
            object = Number(value=num)
            object.save()
            return render(request, 'postform.html', {'obj': object})
    else:
        form = PostForm()

    return render(request, 'postform.html', {'form': form})

def max(request):
        maxnum = Number.objects.all().aggregate(Max('value'))
        return render(request, 'showmax.html', {'num_max': maxnum})
