from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'iCreate/index.html', {
        # to-be-edited: key-value pairs; django site variables,
    })


