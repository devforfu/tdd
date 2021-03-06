from django.shortcuts import redirect, render

from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)

    if form.is_valid():
        ls = List.objects.create()
        form.save(for_list=ls)
        return redirect(ls)

    return render(request, "home.html", {'form': form})


def view_list(request, list_id):
    ls = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=ls)

    if request.method == "POST":
        form = ExistingListItemForm(for_list=ls, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(ls)

    return render(request, "list.html", {"list": ls, "form": form})
