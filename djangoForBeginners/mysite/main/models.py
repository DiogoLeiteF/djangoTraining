from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text


# python manage.py shell
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)

# >>> from main.models import Item, ToDoList

# >>> t = ToDoList(name = 'Tom\'s list')
# >>> t.save()

# >>> ToDoList.objects.all()
# <QuerySet [<ToDoList: Tom's list>]>
# >>> ToDoList.objects.all()[0]
# <ToDoList: Tom's list>
# >>> ToDoList.objects.all()[0].name
# "Tom's list"

# >>> ToDoList.objects.get(id=1)    
# <ToDoList: Tom's list>

# >>> t
# <ToDoList: Tom's list>

# >>> t.item_set.all()
# <QuerySet []>

# >>> t.item_set.create(text="Go to the mall", complete = "False")
# <Item: Go to the mall>

# >>> Item.objects.all()
# <QuerySet [<Item: Go to the mall>]>

# >>> t.item_set.get(id=1)
# <Item: Go to the mall>

# >>> t=ToDoList.objects
# >>> t.all()
# <QuerySet [<ToDoList: Tom's list>]>
# >>> 

# >>> t.filter(name__startswith='T')
# <QuerySet [<ToDoList: Tom's list>]>
# >>> t.filter(id=2)
# <QuerySet []>

# >>> 
# >>> del_obj = t.filter(id=1)
# >>> del_obj.delete()
# (2, {'main.Item': 1, 'main.ToDoList': 1})
# >>> t.all()
# <QuerySet []>

# >>> t1 =ToDoList(name="First List")
# >>> t1.save()
# >>> t2 = ToDoList(name="Second List")
# >>> t2.save()

# >>> t1.item_set.all()
# <QuerySet []>

# >>> t1.item_set.create(text="do something", complete='False')
# <Item: do something>
# >>>