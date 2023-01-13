from datetime import datetime
from django import template
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from numerize import numerize

register = template.Library()


DAYS_PER_YEAR = 365
DAYS_PER_MONTH = 30
DAYS_PER_WEEK = 7

""" FILTERS """


@register.filter(is_safe=True)
def date_since(specific_date):
    today = timezone.now()
    # if isinstance(specific_date, datetime):
    #     specific_date = specific_date.date()
    diff = today - specific_date
    diff_years = int(diff.days / DAYS_PER_YEAR)
    diff_months = int(diff.days / DAYS_PER_MONTH)
    diff_weeks = int(diff.days / DAYS_PER_WEEK)
    diff_map = [
        ("year", "years", diff_years),
        ("month", "months", diff_months),
        ("week", "weeks", diff_weeks),
        ("day", "days", diff.days),
    ]
    for parts in diff_map:
        (interval, intervals, count) = parts
        if count > 1:
            return _(f"{count} {intervals} ago")
        elif count == 1:
            return _("yesterday") if interval == "day" else _(f"last {interval}")
    if diff.days == 0:
        seconds = diff.seconds
        minutes = seconds // 60 if seconds and seconds >= 60 else None
        hour = minutes // 60 if minutes and minutes >= 60 else None

        if not minutes:
            return _(f"{seconds} secs ago")
        if not hour:
            return _(
                f"{minutes if minutes > 1 else 'a'} min{'s' if minutes > 1 else ''} ago"
            )

        return _(f"{hour if hour > 1 else 'an'} hr{'s' if hour > 1 else ''} ago")

    else:
        return f"{specific_date: %B %d, %Y}"


@register.filter(is_safe=True)
def get_numerize(numb: int) -> str:
    return numerize.numerize(numb)


""" TAGS """


class ObjectsNode(template.Node):
    def __init__(self, model, manager_method, limit, var_name):
        self.model = model
        self.manager_method = manager_method
        self.limit = template.Variable(limit) if limit else None
        self.var_name = var_name

    def render(self, context):
        if "." in self.manager_method:
            manager, method = self.manager_method.split(".")
        else:
            manager = "_default_manager"
            method = self.manager_method

        model_manager = getattr(self.model, manager)
        fallback_method = self.model._default_manager.none
        qs = getattr(model_manager, method, fallback_method)()
        limit = None
        if self.limit:
            try:
                limit = self.limit.resolve(context)
            except template.VariableDoesNotExist:
                limit = None
        context[self.var_name] = qs[:limit] if limit else qs
        return ""


@register.tag
def load_objects(parser, token):
    """Gets a queryset of objects of the model specified by app and model name

    Usage:
        {% load_objects [<manager.]<method>
                        from <app_name>.<model_name>
                        [limit <amount>]
                        as <var_name>
        %}
    Examples:
        {% load_objects latest_published from people.Person limit 3 as people %}
        {% load_objects objects.all from news.Article as article %}
        {% load_objects my_objects.all from news.Article limit 5 as article %}
    """
    limit_count = None
    try:
        (
            tag_name,
            manager_method,
            str_from,
            app_model,
            str_limit,
            limit_count,
            str_as,
            var_name,
        ) = token.split_contents()
    except ValueError:
        try:
            (
                tag_name,
                manager_method,
                str_from,
                app_model,
                str_as,
                var_name,
            ) = token.split_contents()
        except ValueError:
            tag_name = token.contents.split()[0]
            raise template.TemplateSyntaxError(
                f"{tag_name} tag requires the following syntax: "
                f"{{% {tag_name} [<manager>.]<method> from "
                "<app_name>.<model_name> [limit <amount>] "
                "as <var_name> %}"
            )
    try:
        app_name, model_name = app_model.split(".")
    except ValueError:
        raise template.TemplateSyntaxError(
            "load_objects tag requires application name "
            "and model name, separated by a dot"
        )
    model = apps.get_model(app_name, model_name)
    return ObjectsNode(model, manager_method, limit_count, var_name)
