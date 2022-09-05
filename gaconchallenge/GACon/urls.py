from django.urls import path
from .views import TalkList, EventList

urlpatterns = [
    path('', EventList.as_view()),
    path('talks', TalkList.as_view())
]