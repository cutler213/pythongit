f=open('mydata','r')

pic=open('matrix.jpg','rb')

new=open('new_matrix.jpg','wb')


for i in pic:
    new.write(i)