def fourtime(d):
    print d,
    print d,
    print d,
    print d,
    
def across():
    print '+',    
    fourtime("-")
    
def mid3():
    print '|',
    fourtime(' ')
    print '|',
    fourtime(' ')
    print '|'

def mid4():
    print '|',
    fourtime(' ')    
    print '|',
    fourtime(' ')
    print '|',
    fourtime(' ')
    print '|'

def grid3x3():
    across()
    across()
    print '+'
    mid3()
    mid3()
    mid3()
    mid3()
    across()
    across()
    print '+'
    mid3()
    mid3()
    mid3()
    mid3()
    across()
    across()
    print '+'
    
def grid4x4():
    across()
    across()
    across()    
    print '+'
    mid4()
    mid4()
    mid4()
    mid4()
    across()
    across()
    across()    
    print '+'
    mid4()
    mid4()
    mid4()
    mid4()
    across()
    across()
    across()    
    print '+'
    mid4()
    mid4()
    mid4()
    mid4()   
    across()
    across()
    across()    
    print '+'
       
grid3x3()
grid4x4()


