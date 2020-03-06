# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from plone import api


class View(BrowserView):
    """
    support view
    """

    def get_worklist(self, limitAt=0, showcuff=False):
        if api.user.is_anonymous():
            return ([], False)
        portal_workflow = api.portal.get_tool(name='portal_workflow')
        wf_results = list(portal_workflow.getWorklistsResults())
        if not wf_results:
            return ([], False)

        wf_results.sort(lambda x, y: cmp(x.modified(), y.modified()))
        member = api.user.get_current()

        hasReviewLev2 = False

        elem_count = 0

        # Ulteriore filtro, se sono un caposervizio vedo quelli del
        # capoufficio SOLO se ho un parametro particolare.
        # Altrimenti ricontrollo tutti gli elementi ed elimino quelli
        # non nello stato giusto.

        tmpList = []
        for item in wf_results:
            if (
                portal_workflow.getInfoFor(item, 'review_state', '???')
                == 'attesa'
            ):
                if (
                    member.has_permission(
                        'CamCom: Approvazione livello 1', item
                    )
                    and not member.has_permission(
                        'CamCom: Approvazione livello 2', item
                    )
                ) or (
                    member.has_permission(
                        'CamCom: Approvazione livello 2', item
                    )
                    and showcuff
                ):
                    tmpList.append(item)
                    elem_count += 1
                    if limitAt and elem_count >= limitAt:
                        break

            elif (
                portal_workflow.getInfoFor(item, 'review_state', '???')
                == 'attesa_cser'
                and not showcuff
            ):
                if member.has_permission(
                    'CamCom: Approvazione livello 2', item
                ):
                    hasReviewLev2 = True
                    tmpList.append(item)
                    elem_count += 1
                    if limitAt and elem_count >= limitAt:
                        break

        wf_results = tmpList
        return (wf_results, hasReviewLev2)
