def dodict(*args, **kwds):
    d = {}
    for k, v in args:
        d[k] = v
    d.update(kwds)

    return d
def makedict(**kwds):
    return kwds
item = (('new' ,1),('old',2))
tada = {}
for i in item:
    tada.update(dodict(i))
data = makedict(xx = 1,yy = 2)
print   tada
print data