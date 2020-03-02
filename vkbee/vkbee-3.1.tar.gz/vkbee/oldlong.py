import time
import asyncio
import json
class BotLongpoll:
    def __init__(self,vk, group_id, wait=10):
        self.group_id = group_id
        self.wait = wait
        self.vk = vk

        self.method_url = "https://api.vk.com/method/groups.getLongPollServer"

        self.url = None
        self.key = None
        self.server = None
        self.ts = None
        self.start_time = time.time()
        self.request_count = 0

    async def update_server(self,update_ts=True):
        data = {"group_id": self.group_id}
        # r = await self.s.post(self.method_url, data=data)
        r = await self.vk.call("groups.getLongPollServer", data=data)
        print(r)
        self.key = r["response"]["key"]
        self.server = r["response"]["server"]
        self.url = self.server

        if update_ts:
            print(r)
            self.ts = r["response"]["ts"]

    async def get_events(self):
        params = {
            "act": "a_check",
            "key": self.key,
            "ts": self.ts,
            "wait": self.wait,
        }
        response = await self.vk.s.get(self.url, params=params)

        self.request_count += 1
        # work_time = time.time() - self.start_time
        # avr_time = work_time / self.request_count
        # speed = self.request_count / work_time
        print(f'All Get Events - {self.request_count}')
        # print(f'Work Time - {work_time}')
        # print(f'Requests in Second - {speed}')
        # print(f'Average Time - {avr_time}')

        response = await response.json()

        if "failed" not in response:
            return response["updates"]

        elif response["failed"] == 1:
            self.ts = response["ts"]

        elif response["failed"] == 2:
            self.update_server()(update_ts=False)

        elif response["failed"] == 3:
            self.update_server()

        return []

    async def events(self):
        await self.update_server(self)
        while True:
            for event in await self.get_events():
                await self.update_server()
                yield event
