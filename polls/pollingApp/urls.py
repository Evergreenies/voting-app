from django.urls import path, include
from rest_framework import routers
from .views import HomeView, voter_list, voting_stat, BaseTemplate, voter_list_api
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'voting', HomeView)

# app_name = 'pollingApp'
urlpatterns = [
    path('', BaseTemplate.as_view(), name='home'),
    path('', include(router.urls), name='voting'),
    path('voter-list/', voter_list, name='voter-list'),
    path('voter-list-api/', voter_list_api, name='voter-list-api'),
    path('voting-detail/', voting_stat, name='voting-detail'),
    path('docs/', include_docs_urls(title='Voting App'))
]
