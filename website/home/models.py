from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    templates = 'templates/home'

    bannner_title = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("bannner_title")
    ]