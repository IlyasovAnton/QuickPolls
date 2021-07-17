from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models.polls_models import Option
from .models.polls_models import Poll


@admin.register(Poll)
class PollsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'duration_in_minutes', 'state', 'minutes_remain', 'seconds_remain',)
    readonly_fields = ('id', 'question', 'duration_in_minutes', 'minutes_remain', 'seconds_remain',)
    exclude = ('timezone_override', 'start_date_offset_in_minutes',)
    fields = ('id', 'question', 'duration_in_minutes', 'state', 'minutes_remain', 'seconds_remain',)
    list_per_page = 15


@admin.register(Option)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll_link', 'option', 'votes')
    readonly_fields = ('id', 'poll_link', 'option', 'votes')
    exclude = ('poll',)
    list_per_page = 15

    def poll_link(self, obj):
        url = (
            # reverse('admin:polls_poll_change', kwargs={'object_id': obj.poll_id})
            reverse('admin:polls_poll_changelist')
            + '?'
            + urlencode({'id': f'{obj.poll_id}'})
        )
        return format_html('<a href="{}">{}</a>', url, obj.poll_id)
    poll_link.short_description = 'poll'
