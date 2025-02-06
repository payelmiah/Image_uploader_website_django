from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    
    # Always load the images and return a response
    img = Image.objects.all()
    return render(request, 'home/home.html', {'form': form, 'img': img})
