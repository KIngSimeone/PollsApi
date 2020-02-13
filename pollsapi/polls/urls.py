from django.urls import path
from .views import polls_list, polls_detail
#alternative with apiviews
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, basename= 'polls')



urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    #Using normal Views
    #path('polls/<int:pk>/', polls_detail,name = 'polls_detail'),
    #Using ApiViews
    path('polls/<int:pk>/', PollDetail.as_view(), name="polls_detail"),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk/vote/', CreateVote.as_view(), name = "create_vote"),
    path('users/', UserCreate.as_view(), name="user_create"),
    path('login/',LoginView.as_view(), name="login")
]

urlpatterns += router.urls


