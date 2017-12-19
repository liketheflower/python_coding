class Test(object):
    def test_a(self):
        def test_b(s,e):
            check[(s,e)] =s+e
            print check
            return check[(s,e)]
        check = {}
        for s in range(2):
           test_b(s,s+4)
        print check


a = Test()
a.test_a()
