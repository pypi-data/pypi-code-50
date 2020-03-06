# -*- coding: utf-8 -*-
from plone import api
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer


class IWorklistPortlet(IPortletDataProvider):
    """Marker interface for CCIAA Worklist portlets"""


@implementer(IWorklistPortlet)
class Assignment(base.Assignment):
    @property
    def title(self):
        return u"Lista di revisione CCIAA"


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('camcom_portlet_review.pt')

    def getMember(self):
        return api.user.get_current()

    def getMemberNameOrId(self, member_id):
        """Return the name of the member, or its id if no name available"""
        member = api.user.get_current()
        return member.getProperty('fullname', None) or member.getId()

    @property
    def full_review_link(self):
        portal_url = getToolByName(self.context, 'portal_url')
        return "%s/full_cciaa_review_list" % portal_url()


class AddForm(base.NullAddForm):
    label = u"Aggiungi lista di revisione camerale"
    description = "Aggiunge la lista di revisione che usa i ruoli camerali"

    def create(self):
        assignment = Assignment()
        return assignment
