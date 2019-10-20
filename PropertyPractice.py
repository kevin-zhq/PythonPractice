class Screen(object):

    # __slots__ = ('width','height') 好像不能再定义
   
    #用property装饰器来定义 setter函数，等同于建立一个获取属性的方法
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,w):
        self._width = w

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,h):
        self._height = h

    @property
    def resolution(self):
        return 'assert s.resolution = %d * %d = %d' % (self._width,self._height,self._width*self._height)

      #用__slots__来限制类的额外属性名称选项
     # __slots__ = ('width','height') 好像不能和@property一起用

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)