# -*- coding: utf-8 -*-
from redminelib import Redmine
from io import BytesIO

class psc(object):
    def __init__(self, user, password, debug = True):
        self.user = user
        self.password = password
        if (debug == True):
            self.host = "172.16.121.17" #THIS IS TEST EASYREDMINE
        else:
            self.host = "192.168.130.45" 
            
        self.webhost = "http://{host}".format(host = self.host)
        self.ezpsc = Redmine(self.webhost, username = self.user, password = self.password)
        
        
    def get_project_id(self, sProject):
        projects = self.ezpsc.project.all()
        for aProject in projects:
            ixProject = aProject.id
            if (sProject == aProject.name):
                return ixProject
        return ""
    
    def Get_tracker(self, sTrack):
        #trackers = self.ezpsc.tracker.all()
        trackers = {u'BOX': 31, u'Category': 58, u'Story': 51, u'Documents': 34, u'Epic': 48, u'ADM-Hanser': 75, u'TEC-Shell': 79, u'DOC': 55, u'Support': 8, u'SUP': 56, u'Feature': 7, u'RD3_Feature': 86, u'TS-Demand': 53, u'Other': 22, u'ADM-eLearning': 73, u'ACT': 54, u'Meeting Record': 26, u'Others': 61, u'Document': 5, u'By PM': 39, u'EXAM': 81, u'Case Service': 3, u'Build Issue': 88, u'Major_Improvement_Theme': 80, u'Personal Project': 46, u'Internal Manual': 25, u'Benchmark': 19, u'TS': 42, u'RD': 41, u'Job': 6, u'Daily Report': 45, u'TECH': 83, u'\u8a08\u7b97\u7570\u5e38\u6216\u767c\u6563(\u5206\u6790\u5931\u6557)': 62, u'Demand': 36, u'Official Release': 24, u'\u7d50\u679c\u4e0d\u5408\u7406\u6216\u8207\u73fe\u5834\u4e0d\u7b26': 68, u'\u8a55\u5b9a\u6e2c\u8a66(BMT)\u6216\u6536\u8cbb\u6848\u4f8b': 70, u'Bug': 1, u'PM': 43, u'XX\u66ab\u6642\u4e0d\u7528-\u7d50\u679c\u8207\u73fe\u5834\u4e0d\u7b26(\u5be6\u9a57\u6bd4\u8f03)': 67, u'\u6280\u8853\u5354\u52a9\u6216\u5176\u4ed6': 71, u'Training': 21, u'Improvement_Theme': 50, u'ACDM': 82, u'To RD': 38, u'To TS': 37, u'Request': 2, u'ELSE': 84, u'Inquery': 16, u'\u9031\u6703': 52, u'Material Testing': 13, u'Research Project': 20, u'Release_Theme': 49, u'TEC-eDesign': 76, u'Release Plan': 29, u'ADM-Paulson': 74, u'Conference Papers': 33, u'\u7814\u7a76\u958b\u767c\u578b\u5c08\u6848': 72, u'Cross-Team': 44, u'All': 47, u'QA story': 59, u'\u7a0b\u5f0f\u9650\u5236(\u5099\u6848\u6027\u8cea)': 69, u'TEC-Solid': 78, u'Sub story': 87, u'Internal Information': 23, u'Change Request': 57, u'Tech Document': 85, u'QA': 40, u'Case Study': 18, u'TEC-BLM': 77, u'DataApplication': 35, u'Alliance Partner Licenses': 32}
        ixTracker = trackers[sTrack]
        return ixTracker
        
    def Get_status(self, sStatus):
        status = self.ezpsc.issue_statuses.all()
        for aStatus in status:
            if (sStatus not in aStatus.name): continue
            return aStatus.id
        
    def Get_User_id(self, sUserName):
        #users = self.ezpsc.user.all()
        dicUser = {'root': 1, 'admin': 5, 'JimmyChien': 7, 'GoranLiu': 9, 'SusanLin': 12, 'BartonLin': 16, 'AlexLu': 19, 
                   'JasmineHo': 21, 'RitzChang': 22, 'JoeWang': 23, 'EthanChiu': 25, 'ThomasChiu': 27, 'JimHsu': 28, 'KentWang': 29, 
                   'fredyang': 31, 'EnzoChen': 36, 'PeterPeng': 37, 'LouisLiu': 38, 'JordanLin': 39, 'CookChen': 40, 'ArvidChang': 42, 'ChrisJwo': 43, 
                   'EdricCheng': 44, 'JoanneHu': 46, 'JingWei': 48, 'ShalomChang': 50, 'AlbertHu': 53, 'TaylorYang': 54, 'WalkerChen': 55, 'JoeTseng': 56, 
                   'KimiFan': 57, 'SeiferLin': 60, 'ScottLim': 61, 'IvorTseng': 62, 'JyeWang': 63, 'DanChang': 64, 'RobertChang': 66, 'EllenHu': 68, 'RogerLee': 69, 
                   'CloudTsai': 71, 'WillieChuang': 72, 'AllenLin': 73, 'SkyeChen': 74, 'VakerLee': 75, 'LawrenceYu': 76, 'RexHuang': 77, 'ChiaoLiu': 78, 'SandyWu': 79,
                   'DemiHo': 80, 'JanikaTsai': 81, 'MayTsai': 83, 'DavidHsu': 84, 'AlarmChang': 85, 'StephenChung': 86, 'SamHsieh': 90, 'VennyYang': 92, 'BillieWang': 93, 
                   'dannickdeng': 94, 'zoehuang': 95, 'cedricliu': 96, 'larryren': 97, 'williamwu': 99, 'vincenthung': 101, 'MarcusSu': 102, 'JoshHsieh': 103, 'OliverTsai': 105, 
                   'KaiWang': 107, 'RubyCheng': 108, 'NickChang': 109, 'YijiLin': 110, 'DanielChen': 112, 'vivaldilee': 114, 'sales.jp': 130, 'sfdc': 131, 'Support.PM': 134, 'Agent': 135, 
                   'ABC': 137, 'AnthonyYang': 149, 'JessicaLin': 151, 'LeoWu': 154, 'Suresh_P': 155, 'KenCheng': 157, 'SrikarVallury': 158, 'JohnSnawerdt': 160, 'JoyLin': 162, 'AliceLin': 163, 
                   'MarvinWang': 164, 'TedLee': 169, 'DonaldChang': 170, 'MaxChang': 171, 'SammiLee': 173, 'EmmaTracz': 174, 'SylviaPan': 178, 'RYChang': 180, 'MartinChang': 182, 'GavinHuang': 183, 
                   'PhilipChang': 184, 'GeorgeLin': 187, 'JohnLin': 189, 'WinnieHung': 191, 'Support.PSC': 192, 'yorkerchang': 197, 'VicGuo': 200, 'DunkHuang': 201, 'PorscheWen': 202, 
                   'HanssonHsu': 207, 'VictorSun': 209, 'CMWong': 211, 'JasonChen': 212, 'NervLee': 214, 'HJChen': 215, 'PaulTsai': 217, 'IanPeng': 218, 'LilyYang': 219, 
                   'AlexChang': 223, 'WilsonHung': 225, 'DebbieWeng': 226, 'AshleyChang': 227, 'EdwardWu': 228, 'BlueLan': 230, 'AlanLiao': 232, 'AllenPeng': 235, 'CarolLee': 236, 
                   'ineschan': 237, 'FrankChen': 238, 'JonHsu': 239, 'FirzenChan': 240, 'DennyQin': 242, 'RitaLi': 243, 'BonnieYe': 245, 'TRSS': 247, 'LeoShen': 248, 'KavyChou': 250, 
                   'JaneChiang': 251, 'MaxKong': 252, 'CarolyhnRen': 254, 'AnnyMa': 255, 'IreneChen': 256, 'MiniKao': 257, 'MiyaHuang': 258, 'VeraYeh': 259, 'WennyTsai': 260, 'AlexBaker': 263, 
                   'AlvinHsu': 265, 'claudeliu': 267, 'KyleHuang': 270, 'MarsLai': 272, 'StevenLee': 273, 'SusanVaaler': 275, 'KikiKratzer': 276, 'JasonZhang': 277, 'RayWu': 278, 'TreeFan': 279, 
                   'AceChen': 281, 'support.us@moldex3d.com': 282, 'kmadmin': 283, 'shenghung': 284, 'tinachang': 285, 'ErinChen': 286, 'JeffChen': 287, 'DarrenShen': 288, 'PierreYeh': 289, 
                   'MarvinLin': 290, 'JackChang': 291, 'russellhsu': 292, 'MichaelChien': 293, 'MishaiHsu': 295, 'AndyChiu': 296, 'JayVang': 297, 'TimCheng': 298, 'MorganChang': 299, 'cases.us': 300, 
                   'AtticusChou': 301, 'JetingWu': 302, 'SonicLin': 303, 'OwenLin': 306, 'support.ts': 307, 'jacklin': 309, 'MandyWang': 310, 'RinnaLiao': 311, 'MarshallWang': 312, 'JosephWang': 321, 
                   'RyanHsu': 326, 'EricYang': 328, 'KellyChen': 329, 'AnitaChen': 330, 'KateChan': 331, 'jennywei': 332, 'RoyLiu': 333, 'EyupmH': 334, 'LingoShih': 335, 'JennanWang': 336, 
                   'LeonLin': 337, 'nobody': 338, 'alarm_t1': 339, 'DonYang': 340, 'eddiewang': 341, 'carriechang': 343, 'hardybai': 345, 'ChoChen': 347, 'LauraPei': 349, 'ZekeChang': 350, 
                   'DoraChen': 351, 'TeresaSun': 352, 'TimChou': 353, 'EarlWang': 356, 'EvanChen': 357, 'SoraLee': 358, 'HenryCyue': 359, 'shellylee': 360, 'OwenChen': 361, 
                   'yoganantham.natrayan': 362, 'PatrickChen': 364, 'YoungHuang': 365, 'sandychang': 366, 'Pankaj_K': 367, 'Abhishek.T': 368, 'KerwinChu': 369, 'oliveryin': 370, 
                   'josephlin': 371, 'IsaacSun': 372, 'scottsazin': 373, 'FrankChi': 375, 'JudyWang': 376, 'JuliaCai': 377, 'PeterXiong': 378, 'KaminLi': 379, 'RyanLi': 380, 'TracyGu': 381, 
                   'LindaZhang': 382, 'HankNiu': 383, 'BillYang': 384, 'OwenZhang': 385, 'ElinChen': 386, 'DawsonHsu': 387, 'SeanYang': 388, 'SawyeZhang': 389, 'KevinLin': 390, 'SimonWei': 391, 
                   'BarryPai':432, 'LynnChang': 442}
        for aKey in dicUser:
            if sUserName.upper() not in aKey.upper(): continue
            sUserName = aKey
        return dicUser[sUserName]
        
    def Get_Project_id(self, sProject):
        projects = self.ezpsc.project.all()
        for aProject in projects:
            if (sProject != aProject.name): continue
            return aProject.id
        
    def Get_Tracker_id_fast(self, sTracker):
        tracker = {"Bug" : 1, "Request" : 2, "Job" : 6}
        return tracker["Bug"]
    
    def Get_Project_id_fast(self, sProject):
        projects = {"IT 2019 基礎建設" : 241}
        return projects[sProject]
        
    def Get_Priority(self, sPriority):
        priority = {"Low" : 1, "Normal" : 2, "High" : 3, "War Room" : 4, "Immediate" : 5}
        return priority[sPriority]
    
    def update_notes(self, ixPSC, notes):
        oPSC = self.ezpsc.issue.get(ixPSC)
        oPSC.notes = notes
        oPSC.save()
        #oPSC.save()
        
    
    def New_Issue(self, project_id, subject, description, sTracker, priority, assigned_to, attached_files = None):
        issue = self.ezpsc.issue.new()
        issue.project_id = project_id
        issue.subject = subject
        issue.tracker_id = self.Get_tracker(sTracker)
        issue.description = description
        issue.status_id = 1
        issue.priority_id = self.Get_Priority(priority)
        issue.assigned_to_id = self.Get_User_id(assigned_to)
        issue.activity_id = 9
        #issue.watcher_user_ids = [123]
        #issue.parent_issue_id = 345
        #issue.start_date = datetime.date(2014, 1, 1)
        #issue.due_date = datetime.date(2014, 2, 1)
        #issue.estimated_hours = 4
        #issue.done_ratio = 40
        #issue.custom_fields = [{'id': 31, 'value': 'alarm'}]
        if (attached_files != None):
            issue.uploads = attached_files
        issue.save()
        return issue.id
    


def test_New_Issue():
    opsc = psc(user = "Agent", password = "moldex3d!")
    ixProject = 679
    subject = u"中文測試"
    description = "description <br/> abc <br/>def <br/>attachment:Snap2604.png<br/>attachment:Snap2603.png<br/>"
    sTracker    = "Bug"
    assigned_to = "admin"
    priority    = "Low"
    attached_files = [{'path': 'G:\\work\\psc_api\\Snap2604.png', 'filename': 'Snap2604.png'}, {'path': 'G:\\work\\psc_api\\Snap2603.png', 'filename': 'Snap2603.png'}]
    ixPSC = opsc.New_Issue(ixProject, subject, description, sTracker, priority, assigned_to)
    print("ixPSC = ", ixPSC)


def main():
    test_New_Issue()


if __name__ == "__main__":
    main()