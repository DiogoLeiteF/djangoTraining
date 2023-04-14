from django.shortcuts import render
from django.http import HttpResponse
from appTest.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    data = {"index_var": "hello from apptest"}
    return render(request, 'appTest/index.html', context=data)


def home(request):
    if request.method == 'POST':
        topic = request.POST.get('topic').capitalize()
        try:
            topic_id = Topic.objects.filter(top_name=topic)[0]
        except:
            webpages_list = AccessRecord.objects.order_by('date')
            data_dic = {'access_records':webpages_list}
            return render(request, 'appTest/home.html', context=data_dic)

        webpages_list_filter = Webpage.objects.filter(topic=topic_id.pk)
       
        new =[x.pk for x in webpages_list_filter]

        webpages_list = [AccessRecord.objects.filter(name=x)[0] for x in new]
        print(webpages_list)

        data_dic = {'access_records':webpages_list}
        return render(request, 'appTest/home.html', context=data_dic)

    webpages_list = AccessRecord.objects.order_by('date')
    data_dic = {'access_records':webpages_list}

    return render(request, 'appTest/home.html', context=data_dic)
    # return HttpResponse("hello")


