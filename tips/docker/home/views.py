from email.utils import format_datetime
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Image
from .forms import ImageForm


# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})


def AddImageView(request):
    context = {"form": ImageForm}
    if request.method == "POST":
        form_image = ImageForm(request.POST, request.FILES)
        if form_image.is_valid():
            form_image.save()
            context["message"] = "your image has been ingested"
    return render(request, 'home/add_image.html', context=context)


class ImageDetailView(DetailView):
    model = Image
    template_name = 'home/images_details.html'
    context_object_name = "image"




"""
class AddImageView(CreateView):
	model = Image
	form_class = ImageForm
	template_name = 'home/add_image.html'
"""