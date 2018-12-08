from django.shortcuts import render
#views here
def index(request):
    return render(request, 'index.html')

def styles(request):
    return render(request, 'styles.css')