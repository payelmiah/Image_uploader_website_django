from django.shortcuts import render

# Create your views here.

def profile_settings(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()

    # Always load the images and return a response
    img = Profile.objects.all()
    