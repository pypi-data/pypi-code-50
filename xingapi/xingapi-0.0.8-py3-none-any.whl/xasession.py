# -*- coding: utf-8 -*-
__all__ = ['Session']

import pythoncom
import win32com.client

class _XASession:
    def __init__(self):
        self.reset()

    def reset(self):
        self.code = None
        self.msg = None

    def OnLogin(self, code, msg):
        self.code = str(code)
        self.msg = str(msg)

    def OnLogout(self):
        pass # 사용하지 않는 기능

    def OnDisconnect(self):
        pass # 사용하지 않는 기능

class Session:
    def __init__(self):
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", _XASession)
    
    def login(self, id, pwd, cert):
        """서버에 로그인한다
        
        :param id: 아이디
        :param pwd: 패스워드
        :param cert: 공인인증패스워드
        
        :returns bool: 로그인 성공여를 반환한다 
        
        """
        self.session.reset()
        connected = self.session.ConnectServer("hts.ebestsec.co.kr", 20001)
        if connected:
            self.session.Login(id, pwd, cert, 0, False)
            while self.session.code is None:
                pythoncom.PumpWaitingMessages()
            print('로그인 성공')
            return self.is_connected()
        else:
            print('로그인 실패')
            return self.is_connected()

    @property
    def accounts(self):
        """모든 계좌목록을 조회한다

        :returns dict(index:int=acct:str): 계좌목록을 딕셔너리로 반환한다

            ::
                session = xa.Session()
                session.login(id='myid', pwd='mypwd', cert='mycert')
                accounts = session.accounts
                accounts[0][number] = 12345678

                # 0은 첫번째 계좌 index, number은 계좌번호. name/nickname/detail_nickname조회가능
        """
        num_acc = self.get_account_list_count()
        accounts = {}
        for index in range(num_acc):
            account = {}
            account['number'] = self.get_account_list(index)
            account['name'] = self.get_account_name(index)
            account['nickname'] = self.get_acct_nickname(index)
            account['detail_name'] = self.get_acct_detail_name(index)
            accounts[index] = account
        return accounts


    def logout(self):
        return self.session.Logout()

    @property
    def send_packet_size(self):
        return self.session.SendPacketSize

    @property
    def connect_time_out(self):
        return self.session.ConnectTimeOut

    def disconnect_server(self):
        return self.session.DisconnectServer()

    def is_connected(self):
        return self.session.IsConnected()

    def get_account_list_count(self):
        return self.session.GetAccountListCount()

    def get_account_list(self, index):
        return self.session.GetAccountList(index)

    def get_account_name(self, index):
        return self.session.GetAccountName(index)

    def get_acct_nickname(self, index):
        return self.session.GetAcctNickname(index)

    def get_acct_detail_name(self, index):
        return self.session.GetAcctDetailName(index)

    def get_last_error(self):
        return self.session.GetLastError()

    def get_error_message(self, error_code):
        return self.session.GetErrorMessage(error_code)

    def is_load_api(self):
        return self.session.IsLoadAPI()

    def get_server_name(self):
        return self.session.GetServerName()