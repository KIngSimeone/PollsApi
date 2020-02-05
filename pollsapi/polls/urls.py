from django.urls import path
from .views import polls_list, polls_detail
#alternative with apiviews
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    #Using normal Views
    #path('polls/<int:pk>/', polls_detail,name = 'polls_detail'),
    #Using ApiViews
    path('polls/<int:pk>/', PollDetail.as_view(), name="polls_detail"),
    path('choices/', ChoiceList.as_view(), name="choice_list"),
    path('vote/', CreateVote.as_view(), name = "create_vote"),
]