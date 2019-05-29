import logging
from datetime import datetime, date

from django import template
from django.template import defaultfilters
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.utils.translation import pgettext, ugettext as _, ungettext

from app.ext.haystack.highlighting import TitleHighlighter

register = template.Library()
logger = logging.getLogger("django")


@register.filter
def highlight_title(value, query=None):
    value = strip_tags(value)
    if query is None:
        return value
    else:
        highlighter = TitleHighlighter(query)
        return mark_safe(highlighter.highlight(value))


@register.filter
def datetime_aware(value):
    if isinstance(value, date):
        if timezone.is_aware(value):
            return value
        else:
            tz = timezone.make_aware(value, timezone.utc)
            return tz
    else:
        raise TypeError("value must be datetime")


@register.filter
def naturaltime(value):
    if not isinstance(value, date):
        return value
    now = datetime.now(timezone.utc if timezone.is_aware(value) else None)
    if value < now:
        delta = now - value
        if delta.days != 0:
            return value
        elif delta.seconds == 0:
            return _("now")
        elif delta.seconds < 60:
            return ungettext(
                # Translators: please keep a non-breaking space (U+00A0)
                # between count and time unit.
                "a second ago",
                "%(count)s seconds ago",
                delta.seconds,
            ) % {"count": delta.seconds}
        elif delta.seconds // 60 < 60:
            count = delta.seconds // 60
            return ungettext(
                # Translators: please keep a non-breaking space (U+00A0)
                # between count and time unit.
                "a minute ago",
                "%(count)s minutes ago",
                count,
            ) % {"count": count}
        else:
            count = delta.seconds // 60 // 60
            return ungettext(
                # Translators: please keep a non-breaking space (U+00A0)
                # between count and time unit.
                "an hour ago",
                "%(count)s hours ago",
                count,
            ) % {"count": count}
    else:
        return value
