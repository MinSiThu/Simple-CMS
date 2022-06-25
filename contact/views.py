from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact/success.html')
    form = ContactForm()
    context = {'form':form}
    return render(request,'contact/contact.html',context)
