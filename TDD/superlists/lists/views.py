from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item


# Create your views here.
def home_page(request):
    # Hack gets the test to pass, but we actually want a value from the form
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    # End Hack
    
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])  #2
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})