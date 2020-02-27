from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify


from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock


# Models


class PersonTag(TaggedItemBase):
    """A tag, related to a person"""
    content_object = ParentalKey(
        'Person',
        related_name='tagged_items',
        on_delete=models.CASCADE,
        null=True,
    )


class PersonExtrernalLink(Orderable, models.Model):
    """A person's external link"""
    person = ParentalKey(
        'Person',
        on_delete=models.CASCADE,
        verbose_name=_('Person'),
        related_name='external_links'
    )
    label = models.CharField(
        verbose_name=_('Label'),
        max_length=255,
    )
    url = models.URLField(
        verbose_name=_('URL'),
        max_length=255,
    )

    panels = [
        FieldPanel('label'),
        FieldPanel('url'),
    ]

    class Meta:
        verbose_name = _("Person's extrernal link")
        verbose_name_plural = _("Person's extrernal links")

    def __str__(self):
        return self.label


class Person(ClusterableModel):
    """A person"""
    picture = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Picture'),
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=250,
    )
    tags = TaggableManager(through=PersonTag, blank=True)
    intro = models.CharField(
        verbose_name=_('Introduction'),
        max_length=250,
        blank=True,
        help_text=_('Shown on the short descriptions'),
    )
    abstract = RichTextField(
        blank=True,
        verbose_name=_('Abstract'),
    )

    panels = [
        ImageChooserPanel('picture'),
        FieldPanel('name'),
        FieldPanel('tags'),
        FieldPanel('intro'),
        FieldPanel('abstract'),
        InlinePanel('external_links', label=_('link')),
    ]

    class Meta:
        verbose_name = _('Person or author')
        verbose_name_plural = _('Persons or authors')
        ordering = ['name']

    def __str__(self):
        return self.name


# Models


class PersonPage(Page):
    """A person"""
    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name=_('Person'),
        null=True,
    )

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('person'),
    ]

    class Meta:
        verbose_name = _('Person or author page')
        verbose_name_plural = _('Person or author pages')
        ordering = ['title']

    def __str__(self):
        return self.title


class PersonIndexPage(Page):
    """An index page of person children pages"""
    intro = RichTextField(
        blank=True,
        verbose_name=_('Intro'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]

    subpage_types = ['wagtailperson.PersonPage']

    class Meta:
        verbose_name = _('Persons or authors Index Page')
        verbose_name_plural = _('Persons or authors Index Pages')

    def __str__(self):
        return self.title

    def get_context(self, request):
        """Overloud the context with published person pages, ordered by
        name"""
        context = super(PersonIndexPage, self).get_context(request)
        person_pages = sorted(
            (
                page.specific
                for page
                in self.get_children().live()
            ),
            key=lambda person_page: person_page.person.name
        )
        context['person_pages'] = person_pages
        return context
