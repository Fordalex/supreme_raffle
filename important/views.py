from django.shortcuts import render

# Create your views here.
def t_and_c_page(request):
    return render(request, 'important/t_and_c.html')