from newsboard import models


class BaseBackend:
    existing = models.Tag.objects.all()
    displayed = existing.exclude(is_hidden=True)

    def guess(self, post):
        return []


class TitleBackendMixin:
    def guess(self, post):
        tags = super().guess(post)
        new_tags = []
        for title_word in post.title.split():
            new_tags += list(self.displayed
                .filter(name__icontains=title_word)
                .values_list('name', flat=True))
        tags += new_tags
        return tags


class Backend(TitleBackendMixin, BaseBackend):
    pass
