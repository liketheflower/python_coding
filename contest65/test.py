class Test(object):
    def __init__(self):
        print "hello"
    def test(self):
        x=2
       # a = [1,2,3]
        a={1:2,2:3}
        print x
        def test1():
            print "within",a
            a[4]=5
            print "within 2",a
        test1()

a = Test()
a.test()
