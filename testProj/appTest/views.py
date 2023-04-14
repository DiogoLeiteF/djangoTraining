from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from appTest.models import Topic, Webpage, AccessRecord
from datetime import datetime

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
            data_dic = {'access_records': webpages_list}
            return render(request, 'appTest/home.html', context=data_dic)

        webpages_list_filter = Webpage.objects.filter(topic=topic_id.pk)

        new = [x.pk for x in webpages_list_filter]

        webpages_list = [AccessRecord.objects.filter(name=x)[0] for x in new]
        # print(webpages_list)

        data_dic = {'access_records': webpages_list}
        return render(request, 'appTest/home.html', context=data_dic)

    webpages_list = AccessRecord.objects.order_by('date')
    data_dic = {'access_records': webpages_list}

    return render(request, 'appTest/home.html', context=data_dic)
    # return HttpResponse("hello")


def add(request):
    if request.method == 'POST':
        topic_html = request.POST.get('topic').capitalize()
        name_html = request.POST.get('name')
        url_html = request.POST.get('url')


        if topic_html and name_html and url_html:
            topic = Topic.objects.filter(top_name=topic_html)
            webpage_name = Webpage.objects.filter(name=name_html)
            webpage_url = Webpage.objects.filter(url=url_html)

            # print(topic)
            # print(webpage)

            if not topic:
                topic = Topic(top_name=topic_html)
                topic.save()
            else:
                topic = topic[0]
            
            if not webpage_name and not webpage_url:
                webpg = Webpage(topic=topic, name=name_html, url=url_html)
                webpg.save()

                accRec = AccessRecord(name=webpg, date=datetime.now())
                accRec.save()
                print("   ADDED   ")
                return HttpResponseRedirect('../')
            
        return render(request, 'appTest/add.html', context={"msg": 'incorect data'})  


    return render(request, 'appTest/add.html')



