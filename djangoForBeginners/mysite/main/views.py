from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import ToDoList, Item
from main.forms import CreateNewList
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login")
def index(response, d):
    ls = ToDoList.objects.get(id=d)

    if response.method == 'POST':
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, 'main/list.html', {"list": ls})


@login_required(login_url="/login")
def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = response.user.todolist_set.create(name=n)
            return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()

    return render(response, 'main/create.html', {'form': form})


@login_required(login_url="/login")
def view(response):

    data = response.user.todolist_set.all()

    return render(response, "main/view.html", context={"list": data, "user": response.user})


@login_required(login_url="/login")
def delete(response, id):
    try:
        lst = response.user.todolist_set.get(id=id)
        
        lst.delete()
    except:
        pass
    return redirect("/view")
