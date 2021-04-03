from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            # img_obj = form.instance
            # return render(request, 'ytest1.html', {'form': form, 'img_obj': img_obj})
            return redirect('../check/')
    else:
        form = ImageForm()
    return render(request, 'ytest1.html', {'form': form})


def image_check(request):
	data = Image.objects.all()
	return render(request, 'ytest2.html', {'data': data})