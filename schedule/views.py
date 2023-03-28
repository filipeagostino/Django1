from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import ItemForm

from .models import Contacts

@login_required
def home(request):
    return render(request, 'schedule/home.html')

@login_required
def itemsList(request):

    search = request.GET.get('search')
    if search:
        items = Contacts.objects.filter(name__icontains=search, user=request.user)
    else:
        items_list = Contacts.objects.all().order_by('-name').filter(user=request.user)
        paginator = Paginator(items_list, 5)
        page = request.GET.get('page')
        items = paginator.get_page(page)


    return render(request, 'schedule/list.html', {'items': items})

@login_required
def itemView(request, id):
    item = get_object_or_404(Contacts, pk=id)
    form = ItemForm(instance=item)
    
    return render(request, 'schedule/item.html', {'form': form})
    
@login_required
def newItem(request):
    if request.method == 'POST':    
        print('POST')
        current_user = request.user
        print(f'USER ID: {current_user.id}')
        form = ItemForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.user_id = current_user.id
            item = form.save()

            return redirect('/schedule/read_all')

    else:
        form = ItemForm()
        return render(request, 'schedule/additem.html', {'form': form, 'title': 'New Item'})

@login_required
def editItem(request, id):
    item = get_object_or_404(Contacts, pk=id)
    form = ItemForm(instance=item)

    if(request.method == 'POST'):
        form = ItemForm(request.POST, instance=item)

        if(form.is_valid()):
            item.save()
            return redirect('/schedule/read_all')
        else:
            return render(request, 'schedule/edititem.html', {'form': form, 'item': item})

    else:
        return render(request, 'schedule/edititem.html', {'form': form, 'item' : 'item'})

@login_required
def deleteItem(request, id):
    item = get_object_or_404(Contacts, pk=id)
    item.delete()
    return redirect('/schedule/read_all')