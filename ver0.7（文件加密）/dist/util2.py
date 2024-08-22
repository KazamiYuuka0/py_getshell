f=open('temp.exe','rb')
d=f.read()
f.close()

#
size=6417813
#
a=open('a-.exe','wb')
a.write(d[:size])
a.close()
b=open('b-.exe','wb')
b.write(d[size:size+3223880])
b.close()
c=open('c-.exe','wb')
c.write(d[size+3223880:])
c.close()

