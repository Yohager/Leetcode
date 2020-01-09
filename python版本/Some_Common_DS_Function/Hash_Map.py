'''
实现一种hash结构
初级hash表，时间复杂度是线性时间复杂度，最优有序二分查找logN
'''
class LinearMap(object):
    def __init__(self):
        self.items = []
    
    #向表中添加元素
    def  add(self, k, v):
        self.items.append((k,v))
    
    #使用线性方式查找元素
    def get(self,k):
        for key,value in self.items:
            if key == k:
                return value
        raise KeyError

'''
对于linearmap进行一定的改进
'''
class BetterMap(object):
    '''
    将总查询表分割为若干个较小的列表
    通过hash函数求某个键的hash值，再通过计算添加或查找在哪个子段
    缩短时间
    '''
    def __init__(self,n = 100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())
            
    def find_map(self,k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self,k,v):
        m = self.find_map(k)
        m.add(k,v)

    def get(self,k):
        m = self.find_map(k)
        return m.get(k)

'''
上述的这种bettermap的形式，当n=100时，查找的速度大概是linearmap的100倍
'''

class HashMap(object):
    def __init__(self):
        #初始化总表为容量为2的表格
        self.maps = BetterMap(2)
        self.number = 0 #表中的数据个数
    
    def get(self,k):
        return self.maps.get(k)
    
    def add(self,k,v):
        #若当前元素达到临界值，进行重排操作
        #对总表进行扩张，增加子表的个数为当前元素的两倍
        if self.number == len(self.maps.maps):
            self.resize()
        #对重排之后的self.map添加新的元素
        self.maps.add(k,v)
        self.number += 1
    
    def resize(self):
        #重排操作，添加新表，重排需要线性时间
        #先建立一个新表，子表的个数 = 2*元素个数
        new_maps = BetterMap(self.number * 2)
        for m in self.maps.maps:
            for k,v in m.items:
                new_maps.add(k,v)
        self.maps = new_maps
    
    
