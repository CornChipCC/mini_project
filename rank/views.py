from django.shortcuts import render
from django.http import HttpResponse
from .models import rank_data
from django.db import connection
# Create your views here.
def rank1_100(request):
    rank_list = rank_data.objects.all()
    return render(
        request,
        'rank/rank1_100.html',
        {'rank_list': rank_list}
    )

def insert(request):
    rank_data(user_id='a1', user_rank = 25, user_score = 100, user_name = '김동민').save()
    return HttpResponse('데이터 입력 완료')