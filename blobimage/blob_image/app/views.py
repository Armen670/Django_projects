from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = Image(
                name=form.cleaned_data['name'],
                image_data=form.cleaned_data['image'].read()
            )
            image_instance.save()
            return redirect('app:image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})
