import os
import json
import requests

from datetime import datetime, timedelta
from bs4 import BeautifulSoup

from kopper.group import *

class TrainSchedule:
    """
    train_order = ["station1", "station2", ...]
    train_schedule = {
        "station1": {
            "depart": "MMSS",
            "arrive": "MMSS"
        },
        "station2": {
            "depart": "MMSS",
            "arrive": "MMSS"
        },
        ...
    ]
    """

    def __init__(self, info):
        self.train_order    = []
        self.train_schedule = {}

        txtRunDt = info["h_run_dt"]
        txtDptDt = info["h_dpt_dt"]
        txtTrnGpCd = info["h_trn_gp_cd"]
        txtTrnNo = info["h_trn_no"]
        self.get_schedule(txtRunDt, txtDptDt, txtTrnGpCd, txtTrnNo)


    def get_schedule(self, txtRunDt, txtDptDt, txtTrnGpCd, txtTrnNo):

        params = {
            "txtRunDt": txtRunDt,
            "txtDptDt": txtDptDt,
            "txtTrnGpCd": txtTrnGpCd,
            "txtTrnNo": txtTrnNo
        }

        response = requests.get(URL.SCHEDULE, params=params)

        soup = BeautifulSoup(response.text, "html.parser")

        tbody = soup.find("tbody")
        trs = tbody.find_all("tr")

        info = []
        for tr in trs:
            tds = tr.find_all("td")
            txtStation  = tds[0].text.strip()
            txtArrive   = tds[1].text.strip()
            txtDepart   = tds[2].text.strip()
            txtDelay    = tds[3].text.strip()

            if txtArrive == "-":
                tm_arrive = datetime.strptime("0", "%S")
            else:
                tm_arrive = datetime.strptime(txtArrive, "%H:%M")

            if txtDepart == "-":
                tm_depart = datetime.strptime("0", "%S")
            else:
                tm_depart = datetime.strptime(txtDepart, "%H:%M")

            if txtDelay == "-":
                tm_delay = timedelta(minutes=0)
            else:
                tm_delay = datetime.strptime(txtDelay, "%m")
                tm_delay = timedelta(minutes=tm_delay.minutes)
            tm_arrive += tm_delay

            self.train_order.append(txtStation)
            self.train_schedule.update({
                txtStation : {
                    "arrive": tm_arrive,
                    "depart": tm_depart
                }
            })

    def _backup(self):
        with open("schedule.json", "w") as f:
            f.write(json.dumps(self.train_schedule))



class TrainInfo(TrainSchedule):

    def __init__(self, info):
        self.info = dict(zip(HEADER.SEARCH, info))

        TrainSchedule.__init__(self, self.info)

    def __str__(self):
        # "KTX : 서울(HH:MM) - 부산(HH:MM)"

        txtTrnClsfCd = self.info["h_trn_clsf_cd"]
        txtTrnClsfNm = TRAIN_TYPE.CODE2NAME[txtTrnClsfCd]
        txtDepartStation = self.info["h_dpt_rs_stn_cd_nm"]
        txtArriveStation = self.info["h_arv_rs_stn_cd_nm"]

        schedule_info = self.train_schedule

        txtOut = "%s(%s) - %s(%s)" % (
            txtDepartStation, schedule_info[txtDepartStation]["depart"].strftime("%H:%M"),
            txtArriveStation, schedule_info[txtArriveStation]["arrive"].strftime("%H:%M")
        )

        if txtTrnClsfNm == "KTX":
            txtTrnClsfNm += "\t"
        return "%s\t%s" % (txtTrnClsfNm, txtOut)


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == "__main__":
    print(TrainInfo("A") in [TrainInfo("A"), TrainInfo("B")])
    t = TrainInfo("A")
    print(t)
