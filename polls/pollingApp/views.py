from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PollsSerializer, VotersListSerializer
from .models import VoterDetail
from rest_framework.decorators import api_view
from django.shortcuts import render
from . import parties
from django.views.generic import TemplateView

panels = parties.panels


class BaseTemplate(TemplateView):
    template_name = 'base.html'


class HomeView(viewsets.ModelViewSet):
    queryset = VoterDetail.objects.all()
    serializer_class = PollsSerializer
   

def voter_list(request):
    if request.method == 'GET':
        data = VoterDetail.objects.all().values()
        total = VoterDetail.objects.count()
        return render(request, 'voters_list.html', {'data': data, 'total': total})


@api_view(['GET'])
def voter_list_api(request):
    data = VoterDetail.objects.all()
    serialized = VotersListSerializer(data, many=True)
    return Response(serialized.data)


def voting_stat(request):
    data = VoterDetail.objects.all().values()
    result = []
    for eachPanel in panels:
        temp_dict = {'count': 0}
        temp_dict['party'] = eachPanel[1]
        for eachVote in data:
            if eachPanel[0] == eachVote.get('voted_to'):
                temp_dict['count'] += 1
        result.append(temp_dict)
    return render(request, 'voting_stat.html', {'data': result, 'total': VoterDetail.objects.count()})
