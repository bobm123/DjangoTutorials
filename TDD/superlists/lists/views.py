from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    # Hack gets the test to pass, but we actually want a value from the form
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    # End Hack
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })