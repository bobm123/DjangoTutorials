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
    
    return render(request, 'home.html')

    # All this can go away since we're redirectin after a post
    # alseo removed, adding a dummy value to new_item_text
    #return render(request, 'home.html', {
    #    'new_item_text': request.POST.get('item_text', '')
    #})