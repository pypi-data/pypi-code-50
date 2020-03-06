# -*- coding: utf-8 -*-

from collective.smartlink import _
from plone import api
from plone.app.contenttypes.browser.link_redirect_view import LinkRedirectView as Base  # noqa
from plone.app.contenttypes.browser.link_redirect_view import NON_RESOLVABLE_URL_SCHEMES  # noqa
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LinkRedirectView(Base):
    index = ViewPageTemplateFile('templates/link.pt')

    def absolute_target_url(self):
        """Compute the absolute target URL."""
        url = self.url()
        mtool = getToolByName(self.context, 'portal_membership')
        can_edit = mtool.checkPermission('Modify portal content', self.context)

        if self.context.remoteUrl.startswith('$'):
            # searching for the linked object
            obj = api.content.get(UID=url.split('/')[-1])

            if obj:
                return obj.absolute_url()
            else:
                # Broken Link or resource not published
                if can_edit:
                    return None
                else:
                    api.portal.show_message(
                        message=_("link_not_found"),
                        request=self.request,
                        type='warning'
                    )
                    return self.request.response.redirect(
                        api.portal.get().absolute_url()
                    )
        else:
            return super(LinkRedirectView, self).absolute_target_url()
