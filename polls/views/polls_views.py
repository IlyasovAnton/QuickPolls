import json

from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone

from polls.forms.polls_forms import CreatePollForm
from polls.models.polls_models import Option
from polls.models.polls_models import Poll


def home(request):
    return render(request, 'main_app/index.html', {'title': 'Quick Polls'})


def create_poll(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            poll = Poll(question=data.pop('question'), duration_in_minutes=data.pop('duration'),
                        state=data.pop('start'))
            poll.save()
            for v in data.values():
                if v != '':
                    option = Option(poll=poll, option=v)
                    option.save()
            return redirect('polls:vote', poll_id=poll.id)

    form = CreatePollForm()

    return render(request, 'main_app/create_poll.html', {'title': 'Create poll',
                                                         'form': form})


def polls(request):
    polls_list = Poll.objects.all()
    paginator = Paginator(object_list=polls_list, per_page=9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main_app/polls.html', {'title': 'Polls',
                                                   'page_obj': page_obj})


def vote(request, poll_id):
    poll = Poll.objects.filter(id=poll_id).first()
    votes = json.loads(request.COOKIES.get('votes', '{}').replace("\'", "\""))
    voted_id = int(votes.get(str(poll_id), 0))

    if request.method == 'POST':
        if str(poll_id) not in votes:
            data = request.POST
            chosen_option, id = data.get('option'), data.get('id')
            votes[str(poll_id)] = id

            option = Option.objects.filter(id=id, option=chosen_option)
            option.update(votes=F('votes') + 1)

            response = HttpResponse(option.first().votes)
            response.set_cookie('votes', votes, expires=timezone.datetime.now() + timezone.timedelta(days=100))
        else:
            response = HttpResponse('-1')
        return response
    elif request.method == 'GET':
        if 'poll' in request.GET.dict():
            options = [option.dict().get('votes') for option in Option.objects.filter(poll=poll)]
            return HttpResponse(json.dumps(options))
        elif 'pause' in request.GET.dict():
            poll.state = Poll.STATE.PAUSED
            poll.save()
        elif 'start' in request.GET.dict():
            poll.state = Poll.STATE.RUNNING
            poll.save()

    options = [option.dict() for option in Option.objects.filter(poll=poll)]
    return render(request, 'main_app/vote.html', {'title': 'Vote',
                                                  'poll': poll,
                                                  'options': options,
                                                  'voted_id': voted_id})
