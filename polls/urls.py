from django.urls import path

from polls.views import polls_views

urlpatterns = [
    path('', polls_views.home, name='home'),
    path('create_poll/', polls_views.create_poll, name='create_poll'),
    path('vote/<int:poll_id>', polls_views.vote, name='vote'),
    path('polls', polls_views.polls, name='polls'),
]
