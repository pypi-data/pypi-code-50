# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django_szuprefix_saas.saas.models import Party
from django_szuprefix.utils import modelutils


class Survey(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "问卷"
        ordering = ("-is_active", "title")

    party = models.ForeignKey(Party, verbose_name=Party._meta.verbose_name, related_name="surveys")
    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="surveys")
    title = models.CharField("标题", max_length=255)
    content = models.TextField("内容", blank=True, null=True,
                               help_text="编辑指南:\n首行为标题.\n题目用阿拉伯数字加点号开头.\n选项用英文字母加点号开头.")
    content_object = modelutils.JSONField("内容对象", blank=True, null=True, help_text="")
    is_active = models.BooleanField('有效', default=False)
    questions_count = models.PositiveSmallIntegerField("题数", blank=True, default=0)
    target_user_tags = models.CharField('目标人群标签', max_length=255, null=True, blank=True,
                                        help_text=u"符合标签的人才能填写问卷,留空则所有人均可填写,多个并列标签使用逗号分隔")
    target_user_count = models.PositiveIntegerField('目标参与人数', default=0, blank=True)
    actual_user_count = models.PositiveIntegerField('实际参与人数', default=0, blank=True)
    begin_time = models.DateTimeField("开始时间", help_text="开始时间一到问卷会被自动上线")
    end_time = models.DateTimeField("结束时间", help_text="结束时间一到问卷会被自动下线")

    def __unicode__(self):
        return self.title

    def stat_detail(self, extattr_filter=None):
        from . import helper
        return helper.stat_detail(self, extattr_filter)

    def get_target_user_ids(self):
        us = set()
        tags = self.target_user_tags
        if tags:
            qset = self.corporation.tags.all()
            for t in tags.split(","):
                ws = reduce(set.intersection,
                            [qset.get(name=tag).get_workers(wx_userid_only=True) for tag in t.split("+")])
                us.update(ws)
        return us

    def get_actual_user_ids(self):
        return list(self.answers.values_list("user_id", flat=True))

    def get_not_answer_user_ids(self):
        return set(self.get_target_user_ids()).difference(set(self.get_actual_user_ids()))

    def save(self, **kwargs):
        # if self.target_user_count == None:
        self.target_user_count = len(self.get_target_user_ids())
        return super(Survey, self).save(**kwargs)


class Answer(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "答案"
        unique_together = ("survey", "user")

    party = models.ForeignKey(Party, verbose_name=Party._meta.verbose_name, related_name="survey_answers")
    survey = models.ForeignKey(Survey, related_name="answers")
    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="survey_answers", blank=True)
    detail = modelutils.JSONField("详情", help_text="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True, blank=True)

    def user_name(self):
        return self.user and self.user.get_full_name()

    user_name.short_description = '用户姓名'

    def show_content(self):
        return "\n".join(["%s : %s" % (d.get("name"), d.get("value")) for d in self.detail])

    show_content.short_description = '答卷展示'
