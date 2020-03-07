# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import re
import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
matplotlib.rc('font', family='NanumBarunGothic')

from PIL import Image

from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from kopper.group import *
from kopper.train_info import *

class Korail():

    info_current = []
    info_history = []

    info_checkout = None
    info_checkout_seat = None
    """
    [
        {
            "route": "XXXX",
            "seat": {
                "1": {
                    "1": 0,
                    "2": 1,
                    "3": 0,
                    "4": 0,
                    ...
                },
                ...
            }
        },
        {
            "route": "XXXX",
            "seat": {
                ...
            }
        },
        ...
    ]
    """

    def __init__(self):
        self._sess = requests.Session()
        # self._sess.get(URL.MAIN)
        # self._sess.headers.update({
        #     "Content-Type": "application/x-www-form-urlencoded",
        #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"
        # })


    def _search_train_request(self, depart, arrive, date, time, day, train_type):
        _update = {
            "selGoTrain": train_type,
            "selGoTrainRa": train_type,
            "txtGoStart": depart,
            "txtGoEnd": arrive,
            "selGoYear": date[:4],
            "selGoMonth": date[4:6],
            "selGoDay": date[6:],
            "selGoHour": time[:2],
            "txtGoHour": time,
            "txtGoYoil": day,
            "txtGoAbrdDt": date
        }

        data = PARAM.SEARCH
        data.update(_update)

        response = self._sess.post(URL.SEARCH, data=data)

        return response.text


    def search_trains(self, depart="서울", arrive="부산", date=None, time=None, train_type="전체"):
        """
            date : "YYmmdd"
            time : "HHMMSS"
        """
        self.info_history += self.info_current
        self.info_current = []

        now = datetime.now()
        if date is None:
            date = now.strftime("%Y%m%d")
            day_code = now.strftime("%w")
        else:
            day_code = datetime.strptime(date, "%Y%m%d").strftime("%w")

        if time is None:
            time = now.strftime("%H%M%S")

        train_type = TRAIN_TYPE.NAME2CODE[train_type]

        html = self._search_train_request(depart, arrive, date, time, day_code, train_type)
        soup = BeautifulSoup(html, "html.parser")

        scripts = soup.find_all("script", {"type": "text/javascript", "language": "javascripts"})

        for script in scripts:
            script = ''.join(script.text.split())
            info = re.search(PATTERN.SEARCH, script).group(1).replace('"', "").split(",")

            if info not in self.info_history:
                self.info_current.append(TrainInfo(info))

            else:
                idx = self.info_history.index(info)
                self.info_current.append(self.info_history[idx])
                del self.info_history[idx]


    def search_print_current(self):
        for idx, info in enumerate(self.info_current):
            print("%02d %s" % (idx + 1, info))


    def set_checkout(self):
        txtIdx = input("Select number : ")

        if txtIdx is "" or not txtIdx.isdigit():
            print("Canceled.")
            return

        self.info_checkout = self.info_current[int(txtIdx)-1]

        print("=============== SELECTED TRAIN INFO ===============")
        print(self.info_checkout)


    def _seat_train_request_init(self, info_checkout, seat_idx, flag=1):
        """
            flag : 1 (일반실) / 2 (특실)
        """
        info = info_checkout.info
        train_order = info_checkout.train_order

        txtDptRsStnCd = info["h_dpt_rs_stn_cd"]
        txtArvRsStnCd = info["h_arv_rs_stn_cd"]

        txtDptNm = STATION_TYPE.CODE2NAME[txtDptRsStnCd]
        txtArvNm = STATION_TYPE.CODE2NAME[txtArvRsStnCd]

        idxDpt = train_order.index(txtDptNm)
        idxArv = train_order.index(txtArvNm)

        h_dpt_stn_run_ordr = "%06d" % (idxDpt+1)
        h_arv_stn_run_ordr = "%06d" % (idxArv+1)

        params = {
            "txtPsrmClCd": flag, # 일반실 / 2: 특실
            "radJobId": "1",
            "txtRunDt": info["h_run_dt"],
            "txtDptDt": info["h_dpt_dt"],
            "txtTrnClsfCd": info["h_trn_clsf_cd"],
            "txtTrnGpCd": info["h_trn_gp_cd"],
            "txtTrnNo": info["h_trn_no"],
            "txtSrcarNo": seat_idx,
            "txtSeatAttCd": info["h_seat_att_cd"],
            "txtDptRsStnCd": info["h_dpt_rs_stn_cd"],
            "txtArvRsStnCd": info["h_arv_rs_stn_cd"],
            "txtTotPsgCnt": "1",
            "txtDptTm": info["h_dpt_tm"],
            "txtArvTm": info["h_arv_tm"],
            "txtDptStnConsOrdr": info["h_dpt_stn_cons_ordr"],
            "txtArvStnConsOrdr": info["h_arv_stn_cons_ordr"],
            "txtDptStnRunOrdr": h_dpt_stn_run_ordr,
            "txtArvStnRunOrdr": h_arv_stn_run_ordr
        }

        response = self._sess.get(URL.SEAT, params=params)

        return response.text


    def _seat_train_request(self, seat_list, seat_idx, txtDptRsStnCd, txtArvRsStnCd, info_checkout, flag=1):
        """
            flag : 1 (일반실) / 2 (특실)
        """
        info = info_checkout.info
        train_order = info_checkout.train_order

        txtDptNm = STATION_TYPE.CODE2NAME[txtDptRsStnCd]
        txtArvNm = STATION_TYPE.CODE2NAME[txtArvRsStnCd]

        idxDpt = train_order.index(txtDptNm)
        idxArv = train_order.index(txtArvNm)

        h_dpt_stn_run_ordr = "%06d" % (idxDpt+1)
        h_arv_stn_run_ordr = "%06d" % (idxArv+1)

        data = {
            "txtSrcarCnt": len(seat_list),
            "arrSrcarNo": ",".join(str(i) for i in seat_list),
            "txtSrcarNo": seat_idx, #2, 3, 4, 5, 6, 7
            "txtPsrmClCd": flag, # 일반실 / 2: 특실
            "txtRunDt": info["h_run_dt"],
            "txtTrnClsfCd": info["h_trn_clsf_cd"],
            "txtTrnGpCd": info["h_trn_gp_cd"],
            "txtTrnNo": info["h_trn_no"],
            "txtSeatAttCd": info["h_seat_att_cd"],
            "txtDptRsStnCd": txtDptRsStnCd,
            "txtArvRsStnCd": txtArvRsStnCd,
            "txtTotPsgCnt": "1",
            "txtDptStnRunOrdr": h_dpt_stn_run_ordr,
            "txtArvStnRunOrdr": h_arv_stn_run_ordr
        }

        # self._sess.headers.update({
        #     "Accept":                           "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #     "Accept-Encoding":                  "gzip, deflate",
        #     "Accept-Language":                  "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
        #     "Cache-Control":                    "max-age=0",
        #     "Connection":                       "keep-alive",
        #     "Content-Type":                     "application/x-www-form-urlencoded",
        #     "Host":                             "www.letskorail.com",
        #     "Origin":                           "http://www.letskorail.com",
        #     "Referer":                          "http://www.letskorail.com/ebizprd/EbizPrdTicketPr12212_i1.do",
        #     "Upgrade-Insecure-Requests":        "1",
        #     "User-Agent":                       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"
        # })
        # print(data)
        # input()

        response = self._sess.post(URL.SEAT, data=data)

        return response.text


    def search_seat(self):
        """
        DONE:
            - 무궁화호, KTX, KTX-산천
            - 일반실
        """
        assert self.info_checkout is not None
        info_checkout = self.info_checkout

        info = info_checkout.info

        txtTrnClsfCd = info["h_trn_clsf_cd"]
        txtTrnClsfNm = TRAIN_TYPE.CODE2NAME[txtTrnClsfCd]

        txtDptRsStnCd = info["h_dpt_rs_stn_cd"]
        txtArvRsStnCd = info["h_arv_rs_stn_cd"]

        txtDptNm = STATION_TYPE.CODE2NAME[txtDptRsStnCd]
        txtArvNm = STATION_TYPE.CODE2NAME[txtArvRsStnCd]

        train_order = info_checkout.train_order
        idxDpt = train_order.index(txtDptNm)
        idxArv = train_order.index(txtArvNm)


        # 호차번호 구하기
        seat_list = []

        _txtDptRsStnCd = STATION_TYPE.NAME2CODE[train_order[idxDpt]]
        _txtArvRsStnCd = STATION_TYPE.NAME2CODE[train_order[idxDpt+1]]

        for default_seat_idx in range(20):
            default_seat_idx += 1

            default_seat_html = self._seat_train_request_init(info_checkout, default_seat_idx)
            fail_seat_txt = "자세한 문의는 1544-7788(철도고객센터)로 문의하십시오."

            soup = BeautifulSoup(default_seat_html, "html.parser")
            if fail_seat_txt in soup.text:
                continue
            else:
                seat_list.append(default_seat_idx)


        print("=============== Search Seat ===============")
        info_seat = []
        for train_idx in range(idxDpt, idxArv):
            _txtDptRsStnCd = STATION_TYPE.NAME2CODE[train_order[train_idx]]
            _txtArvRsStnCd = STATION_TYPE.NAME2CODE[train_order[train_idx+1]]

            sys.stdout.write("%s - %s" % (train_order[train_idx], train_order[train_idx+1]))
            sys.stdout.flush()

            seat_statuses = {}

            for seat_idx in seat_list:

                sys.stdout.write(".")
                sys.stdout.flush()

                seat_html = self._seat_train_request(seat_list, seat_idx, _txtDptRsStnCd, _txtArvRsStnCd, info_checkout)

                soup = BeautifulSoup(seat_html, "html.parser")

                span_seat_on = soup.find_all("span", {"class": "ck_seat_td1_on"})
                span_seat_on += soup.find_all("span", {"class": "ck_seat_td2_on"})
                span_seat_off = soup.find_all("span", {"class": "ck_seat_td1_off"})
                span_seat_off += soup.find_all("span", {"class": "ck_seat_td2_off"})

                seat_status = {}

                for span_seat in span_seat_on:
                    seat_on = span_seat.text.strip()
                    seat_status[seat_on] = 1    # 자리가 비어있다.

                for span_seat in span_seat_off:
                    seat_off = span_seat.text.strip()
                    seat_status[seat_off] = 0   # 자리가 예약되어있다.

                seat_statuses[seat_idx] = seat_status

            
            sys.stdout.write(" Done!\n")
            sys.stdout.flush()

            info_seat.append({
                "route": "%s-%s" % (train_order[train_idx], train_order[train_idx+1]),
                "seat": seat_statuses
            })

        self.info_checkout_seat = info_seat



    def processing_seat(self):
        # assert self.info_checkout_seat is not None

        """
        sorting setup
        """
        def atoi(text):
            return int(text) if text.isdigit() else text

        def natural_keys(text):
            '''
            alist.sort(key=natural_keys) sorts in human order
            http://nedbatchelder.com/blog/200712/human_sorting.html
            (See Toothy's implementation in the comments)
            '''
            return [ atoi(c) for c in re.split('(\d+)', text) ]


        info_checkout_seat = self.info_checkout_seat

        route_list = []

        hosil_list = []
        is_hosil = False

        seat_list = []
        is_seat = False

        route_matrix = []

        for info_route in info_checkout_seat:
            route_name = info_route["route"]
            hosil = info_route["seat"]

            hosil_keys = sorted(list(hosil.keys()))
            # hosil_keys.sort(key=natural_keys)

            hosil_matrix = []

            for hosil_key in hosil_keys:
                seat = hosil[hosil_key]
                seat_size = len(seat)

                seat_keys = list(seat.keys())
                seat_keys.sort(key=natural_keys)

                seat_matrix = np.zeros((seat_size), dtype=np.int8)

                for seat_idx, seat_key in enumerate(seat_keys):
                    status = seat[seat_key]
                    seat_matrix[seat_idx] = status

                hosil_matrix.append(seat_matrix)

                if is_seat is False:
                    seat_list.append(seat_keys)

            is_seat = True

            if is_hosil is False:
                hosil_list = hosil_keys
                is_hosil = True
            route_list.append(route_name)

            route_matrix.append(hosil_matrix)


        self.info_seat_matrix = np.array(route_matrix)
        self.info_hosil_list = hosil_list
        self.info_route_list = route_list
        self.info_seat_list = seat_list


    def visualization(self, resolution=(19.2, 10.8)):

        def plot_attr(ax, title, seat_matrix, seat_list, route_list, filename):
            cax = ax.matshow(seat_matrix, cmap='winter')
            patch1 = mpatches.Patch(color='green', label='O')
            patch2 = mpatches.Patch(color='blue', label='X')
            plt.legend(handles=[patch1, patch2], bbox_to_anchor=(1, 1), loc=2, borderaxespad=1.)

            ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
            ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

            ax.set_xticklabels([' ']+seat_list)
            ax.set_yticklabels([' ']+route_list)

            plt.text(0.5, 1.25, title,
                horizontalalignment='center',
                fontsize=30,
                transform = ax.transAxes)
            plt.grid(color='gray', linestyle='--')
            fig.set_size_inches((19.20, 10.80), forward=False)
            plt.savefig("img/%s.png" % filename)


        # Save Seperate Image
        info_seat_matrix = self.info_seat_matrix
        info_hosil_list = self.info_hosil_list
        info_seat_list = self.info_seat_list
        info_route_list =  self.info_route_list

        for hosil_idx, hosil_name in enumerate(info_hosil_list):
            fig = plt.figure(hosil_idx+1)

            ax = plt.subplot(1, 1, 1)
            title = "%s호차" % hosil_name
            seat_matrix = np.concatenate([[matrix] for matrix in info_seat_matrix[:, hosil_idx]], axis=0)
            plot_attr(ax, title, seat_matrix, info_seat_list[hosil_idx], info_route_list, hosil_name)



        # Save Merged Image
        new_im_width = 0
        new_im_height = 0

        images = []
        for hosil_idx in info_hosil_list:
            im = Image.open("img/%s.png" % hosil_idx)

            # Cropping Upside, downside
            width = im.size[0]
            height = im.size[1]
            half_the_width = im.size[0] / 2
            half_the_height = im.size[1] / 2

            crop_im = im.crop(
                (
                    0,
                    half_the_height - height/4,
                    width,
                    half_the_height + height/4
                )
            )

            # Set attrs for new image
            new_im_width = max(width, crop_im.size[0])
            new_im_height += crop_im.size[1]

            images.append(crop_im)


        new_im = Image.new('RGB', (new_im_width, new_im_height))

        y_offset = 0
        for im in images:
            new_im.paste(im, (0, y_offset))
            y_offset += im.size[1]

        new_im.save("result.png")
        # new_im.show()




if __name__ == "__main__":
    ko = Korail()
    # ko.search_trains(date="20170922", time="060000")
    # ko.search_print_current()
    # ko.set_checkout()
    # ko.search_seat()
    ko.processing_seat()
    ko.visualization()
