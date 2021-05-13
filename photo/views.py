from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    title = "Home"

    return render(request, 'index.html',{'images': images[::-1], 'locations': locations, "title":title})


def search(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        title = "Searched Images"
        return render(request, 'search.html', {"message": message, "images": searched_images, "title":title})
    else:
        message = "You haven't searched for any image category"
        title = "Searched Images"

        return render(request, 'search.html', {"message": message, "title":title})


def location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    title = "Location"
    return render(request, 'location.html', {'location_images': images, "title":title})