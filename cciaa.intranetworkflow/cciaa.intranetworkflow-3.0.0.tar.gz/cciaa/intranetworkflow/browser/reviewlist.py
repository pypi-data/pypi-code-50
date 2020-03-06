# -*- coding: utf-8 -*-
from plone.app.content.browser.tableview import Table
from plone.app.content.browser.reviewlist import (
    FullReviewListView as BaseFullReviewListView,
)
from plone.app.content.browser.reviewlist import (
    ReviewListTable as BaseReviewListTable,
)
from plone import api


class FullReviewListView(BaseFullReviewListView):
    def revlist(self):
        my_camcom_worklist = api.content.get_view(
            name='my_camcom_worklist',
            context=api.portal.get(),
            request=self.request,
        )
        results = my_camcom_worklist.get_worklist()
        return results[0]

    def url(self):
        return self.context.absolute_url() + '/full_cciaa_review_list'

    def review_table(self):
        table = ReviewListTable(self.context, self.request)
        return table.render()


class ReviewListTable(BaseReviewListTable):
    """   
    The review list table renders the table and its actions.
    """

    def __init__(self, context, request, **kwargs):
        self.context = context
        self.request = request

        url = self.context.absolute_url()
        view_url = url + '/full_cciaa_review_list'
        self.table = Table(
            request, url, view_url, self.items, buttons=self.buttons
        )

