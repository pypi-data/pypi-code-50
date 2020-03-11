import time

import pytest

from slim.retcode import RETCODE
from slim.support.peewee import PeeweeView
from peewee import *
from slim import Application, ALL_PERMISSION
from slim.tools.test import make_mocked_view_instance, invoke_interface

pytestmark = [pytest.mark.asyncio]
app = Application(cookies_secret=b'123456', permission=ALL_PERMISSION)
db = SqliteDatabase(":memory:")


class Topic(Model):
    title = CharField(index=True, max_length=255)
    time = BigIntegerField(index=True)
    content = TextField()

    class Meta:
        database = db


db.create_tables([Topic], safe=True)


Topic.create(time=time.time(), title='Hello', content='World')
Topic.create(time=time.time(), title='Hello2', content='World')
Topic.create(time=time.time(), title='Hello3', content='World')
Topic.create(time=time.time(), title='Hello4', content='World')


@app.route('/topic')
class TopicView(PeeweeView):
    model = Topic


app._prepare()


async def test_set_simple():
    view = await invoke_interface(app, TopicView().set, params={'id': 1}, post={"content": "Content changed 3"})
    assert view.ret_val['code'] == RETCODE.SUCCESS


async def test_set_bad_values():
    view = await invoke_interface(app, TopicView().set, params={'id': 1}, post={"asd": "1"})
    assert view.ret_val['code'] == RETCODE.INVALID_POSTDATA
    assert 'Invalid post values' in view.ret_val['data']


async def test_set_bulk():
    view = await invoke_interface(app, TopicView().set, post={"content": "Content changed 3"}, headers={'bulk': 'true'})
    assert view.ret_val['code'] == RETCODE.SUCCESS
    assert view.ret_val['data'] == 4
