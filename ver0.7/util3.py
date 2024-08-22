fr=open('r.exe','ab')

fa=open('a.exe','rb')
fb=open('b.exe','rb')
fc=open('c.exe','rb')
da=fa.read()
db=fb.read()
dc=fc.read()
fa.close()
fb.close()
fc.close()

fr.write(da)
fr.write(db)
fr.write(dc)

fr.close()
