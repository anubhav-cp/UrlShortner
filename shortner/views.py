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

    context = {'form': form}
    return render(request, 'shortner/homePage.html', context)


def urlRedirect(request, slugs):
    data = URL.objects.get(short_url=slugs)
    return redirect(data.full_url)
    