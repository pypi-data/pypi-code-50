import sys
sys.setrecursionlimit(150000)


class ListMapperIterator:
    def __init__(self, list_mapper):
        self.current = 0
        self.max = len(list_mapper.maList)
        self.list = list_mapper.maList
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        ret = self.list[self.current]
        self.current += 1
        return ret

class ListMapper:
    
    def __init__(self,maList=list()):
        self.maList = maList
        
    def __str__(self):
        return 'List'+str(self.maList)
    
    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return ListMapperIterator(self)

    def copy(self):
        temp = self.maList.copy()
        return ListMapper(temp)
        
    def mapF(self,function):
        res = self.copy()
        res.maList = list(map(function,self.maList))
        return res

    
    def flatten(self):
        res = self.copy()
        res.maList = sum(self.maList,[])
        return res
        
    def flatMapF(self,function):
        temp = self.mapF(function).maList.copy()
        res = self.copy()
        res.maList = (sum(temp,[]))
        return res

    def reduceF(self,function):
        result =self.maList[0]
        for k in range(1,len(self.maList)):
            result=function(self.maList[k],result)
        return result

    def groupByKey(self):
        toMapList = self.mapF(lambda x:x)
        res = toMapList.mapF(lambda x:x[0]).uniqueF
        res = res.mapF(lambda x:(x,toMapList.mapF(lambda y:y[1] if x==y[0] else None).filterF(lambda x:x!=None)))
        
        return res

            
    def reduceByKeyF(self,function):
        res =self.groupByKey().mapF(lambda x:(x[0],x[1].reduceF(function)))
        return res                       


    def foreach(self,function):
        for k in self:
            function(k)

    @property
    def uniqueF(self):
        res = self.copy()
        res.maList = list(set(self.maList))
        return res
    
    def filterF(self,function):
        res = self.copy()
        res.maList = list(filter(function,self.maList))
        return res
    
    def append(self,value):
        self.maList.append(value)
        return self
    
    def extend(self,listValue):
        self.maList.extend(listValue)
        return self
    
    def insert(self,index,value):
        self.maList.insert(index,value)
        return self
    
    @property
    def head(self):
        return self.maList[0]
    
    @property
    def tail(self):
        return self.maList[-1]
    
    def remove(self,elem):
        self.maList.remove(elem)
        
    def removeAll(self,value):
        self.maList =[val for val in self.maList if val!=value]
        return self
    
    def removeIndex(self,index):
        self.maList =[k for i,k in enumerate(self.maList) if i!=index]
        return self
    
    def removeListIndex(self,listIndex):
        self.maList = [k for i,k in enumerate(self.maList) if i not in listIndex]
        return self
    
    def removeListValue(self,listValue):
        self.maList =[val for val in self.maList if val not in listValue]
        return self
