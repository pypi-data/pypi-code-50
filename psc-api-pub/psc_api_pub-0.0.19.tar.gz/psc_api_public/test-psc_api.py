# -*- coding: utf-8 -*-
import unittest
from psc_api import psc
from psc_mysql import psc_mysql
import warnings

class For_test_psc_api(unittest.TestCase):
    
    def setUp(self):
        self.psc = psc()
        self.mysql = psc_mysql()
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<socket.socket.*>") 
        
    def tearDown(self):
        pass
    """
    def test_get_project_id(self):
        sProject = "> Moldex3D Product Information"
        ixProject = self.psc.get_project_id(sProject)
        self.assertEqual(7, ixProject)
    """
        
    def test_Get_News(self):
        ixNews = 49
        oNews = self.psc.Get_News(ixNews)
        self.assertEqual(oNews.title, "this is alarm news in 2019 project")
        
        
    def test_get_project_id_sql(self):
        sProject = "Bug"
        ixProject = self.mysql.get_project_id_sql(sProject)
        self.assertEqual(ixProject[0][0], 150)
        
    def test_Add_News_in_Project(self):
        ixProject = 241
        project_id = 241
        title = "python unittest"
        description = "Hi <Br/> today is good day<br/>"
        author_id = 5
        ixNews = self.mysql.Add_News_in_Project(project_id, title, description, author_id)
        self.mysql.Add_watchers_for_News(ixNews, author_id)
        
        
    def test_New_Issue(self):
        ixProject = 241
        subject = u"中文測試"
        #description = {"description": "this is apple\n123", "another key": "avlue2"}
        #attachment:"Image20190424185509_1.png"
        description = "description <br/> abc <br/>def <br/>attachment:Snap2604.png<br/>attachment:Snap2603.png<br/>"
        sTracker = "Bug"
        assigned_to = "admin"
        priority = "Low"
        attached_files = [{'path': 'G:\\work\\psc_api\\Snap2604.png', 'filename': 'Snap2604.png'}, {'path': 'G:\\work\\psc_api\\Snap2603.png', 'filename': 'Snap2603.png'}]
        ixPSC = self.psc.New_Issue(ixProject, subject, description, sTracker, priority, assigned_to, attached_files)
        #print("ixPSC = ", ixPSC)
        
    def test_list_tracker(self):
        sTracker = "Bug"
        ixTracker = self.psc.Get_tracker(sTracker)
        self.assertEqual(ixTracker, 1)
        
    def test_Get_User_id(self):
        sUser = "GoranLiu"
        user_id = self.psc.Get_User_id(sUser)
        self.assertEqual(user_id, 9)
        
    def test_Get_Project_id(self):
        sProject = "IT 2019 基礎建設"
        project_id = self.psc.Get_Project_id(sProject)
        self.assertEqual(project_id, 241)
        project_id = self.psc.Get_Project_id_fast(sProject)
        self.assertEqual(project_id, 241)
        
    def test_Issue_Alread_Exists(self):
        sTitle = "中文測試"
        res = self.mysql.Issue_Alread_Exists(sTitle)
        self.assertEqual(21528, res)
        
    #def test_Get_status(self):
        #sStatus = "Active"
        #ixStatus = self.psc.Get_status(sStatus)
        #self.assertEqual(ixStatus, 100)
        
if __name__ == "__main__":
    unittest.main()