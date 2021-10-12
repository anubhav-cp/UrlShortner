from django.shortcuts import render, redirect
from shortner.models import URL
from .forms import UrlShortner
import random
import string



def homePage(request):
    form = UrlShortner()

    if request.method == 'POST':
        form = UrlShortner(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(5))
            url = form.cleaned_data['full_url']

            new_url = URL(full_url = url, short_url = slug)
            
            new_url.save()
            print(new_url)
            shorty = URL.objects.get(short_url=slug)
            print(shorty)
            return redirect(f'new_url/{shorty.id}' )
            print(new_url)

    else:
        form = UrlShortner()

    data = URL.objects.all()
    context = {'form': form, 'data':data}
    return render(request, 'shortner/homePage.html', context)

def newUrl(request, pk):
    short = URL.objects.all()
    geturl = short.get(id=pk)
    return render(request, 'shortner/new_url.html', {'geturl':geturl})
    
def urlRedirect(request, slugs):
    data = URL.objects.get(short_url=slugs)

    
    return redirect(data.full_url)
    

