
class MyCalendar(object):

    def __init__(self):
        self.cal = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for a, b in self.cal:
            if a <= start < b or start <= a < end:
                return False
        self.cal.append((start,end))
        return True


obj = MyCalendar()
#["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
resu = []
for [s,e] in [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]:
    resu+=[obj.book(s,e)]
print resu
# expected      [true,true,false,false,true,false,true,true,true,false]
#our output [True, True, False, False, True, False, False, True, False, False]
#print obj.book(10,20)
#print obj.book(15,25)
#print obj.book(20,30)
