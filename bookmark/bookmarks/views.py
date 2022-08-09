from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>hello world!</h1>")


from bookmarks.models import Bookmark
def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()
    context = {'bookmark_list':bookmark_list}
    return render(request, 'bookmark_list.html', context)

from django.shortcuts import get_object_or_404
def bookmark_detail(request,pk):
    #bookmark = Bookmark.objects.get(id=pk)
    bookmark = get_object_or_404(Bookmark, id=pk)
    context = {'bookmark':bookmark}
    return render(request, 'bookmark_detail.html', context)

from .forms import BookmarkForm
def bookmark_create(request):
    #     context = {'text':'POST METHOD!!!'}
    #     return render(request, 'templates/bookmark_create.html',context)
    # context={'text':'GET METHOD'}
    # return render(request, 'templates/bookmark_create.html', context)
    # bookmark = Bookmark()
    # if request.method=='POST':
    #     bookmark.title = request.POST['title']
    #     bookmark.url = request.POST['url']
    #     bookmark.memo = request.POST['memo']

    #     bookmark.save()

    #     return redirect(f'/bookmark/{bookmark.id}/')

    # return render(request, 'bookmark_create.html')
    context = {}


    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save()
            return redirect(f'bookmarks:detail', bookmark.id)
    else:
        form = BookmarkForm()
        context['form'] = form
    return render(request, 'bookmark_create.html', context)




def bookmark_update(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    # context={'bookmark':bookmark}
    # if request.method=='POST':
    #     bookmark.title = request.POST['title']
    #     bookmark.url = request.POST['url']
    #     bookmark.memo = request.POST['memo']

    #     bookmark.save()

    #     return redirect(f'/bookmark/{bookmark.id}/')

    # return render(request, 'bookmark_update.html', context)
    context = {}


    if request.method == "POST":
        form = BookmarkForm(request.POST, instance = bookmark)
        if form.is_valid():
            bookmark = form.save()
            return redirect(f'bookmarks:detail', bookmark.id)
    else:
        form = BookmarkForm()
        context['form'] = form
    return render(request, 'bookmark_update.html', context)   


def bookmark_delete(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    context = {'haha':bookmark}

    if request.method == 'POST':
        bookmark.delete()
        return redirect('/bookmark/')

    return render(request, 'bookmark_delete.html', context)





   
