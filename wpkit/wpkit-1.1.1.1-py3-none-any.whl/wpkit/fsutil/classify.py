from wpkit.fsutil import Folder
import re,os,shutil,glob
class ClassifyFolder(Folder):
    def __init__(self,path,keywords=[],except_keywords=[]):
        super().__init__(path)
        self.keywords=keywords
        self.except_keywords=except_keywords
        # self.classifiers=classifiers
        self.classifiers=[]
    def make_classifier(self,name,keywords=[]):
        folder=self.openFolder(name)
        classifier=ClassifyFolder(folder.path,keywords)
        self.classifiers.append(classifier)

    def recognize(self,s):
        for key in self.except_keywords:
            if re.findall(key,s):
                return False
        for key in self.keywords:
            if re.findall(key,s):
               return True
        return False
    def classify(self):
        pathes=self.iterfiles()
        # print(pathes)
        for classifier in self.classifiers:
            tmppathes=pathes.copy()
            for path in tmppathes:
                if classifier.recognize(path):
                    print(path)
                    classifier.eat(path)
                    os.remove(path)
                    pathes.remove(path)
        for classifier in self.classifiers:
            # print(self.path)
            classifier.classify()



def demo():
    '''
    ['其他', '学习方法', '', '英语作文', '英语发音', '英语语法', '英语题目', '词汇短语', '语法填空', '阅读理解']
    '''
    path=r'E:\LearningResources\英语_测试'
    root=ClassifyFolder(path)

    root.make_classifier(name='学习方法',keywords=['学习方法','学好','秘籍','规划','学习英语'])
    root.make_classifier(name='英语听力',keywords=['听力'])
    root.make_classifier(name='知识汇总',keywords=['知识汇总','导图','知识点','状元笔记'])
    root.make_classifier(name='英语发音',keywords=['发音','音标'])
    root.make_classifier(name='英语语法',keywords=['语法','时态','语态','从句','倒转','情态动词',
                                              '句型','虚拟语气','句子成分','词性'])

    root.make_classifier(name='语法填空',keywords=['语法填空'])
    root.make_classifier(name='完形填空',keywords=['完型','完形'])
    root.make_classifier(name='阅读理解',keywords=['阅读'])
    root.make_classifier(name='短文改错',keywords=['改错'])
    root.make_classifier(name='英语作文',keywords=['作文','范文','写作'])
    root.make_classifier(name='词汇短语', keywords=['词汇', '短语', '单词', '固定搭配', '熟词', '3500', '词组', '动词'])
    

    root.classify()



if __name__ == '__main__':
    demo()

