from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>hello world!</h1>")


from bookmarks.models import Bookmark
def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()
    context = {'bookmark_list':bookmark_list}
    return render(request, 'templates/bookmark_list.html', context)
