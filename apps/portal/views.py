from django.shortcuts import render

# Create your views here.


def portal(request):
    context ={ 'title': "Main Portal"}
    return render(request, 'portal/portal.html', context=context)