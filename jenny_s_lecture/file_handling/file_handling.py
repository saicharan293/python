

# to create a file
f1=open('file_1', 'x')

# to read file
f2=open('file_1')
print(f2.read())

# to write/overwrite something in the file
f3=open('file_1', 'w')
f3.write('this is write mode in file handling')

# to read and write mode in the file: r+
f1=open('file_1', 'r+')
print(f1.read())
print(f1.tell())
f1.write('that ')
f1.write('this is read and write mode in file handling')
f1.write(" this is jenny's lecture ")

#to get the seeker position:
# f.tell()

#to read and write in file: w+

# f4=open('file_2','w+')
# print(f4.tell())
# f4.write('Hi this is second file ')
# print(f4.tell())
#
# f4.write('second line')
# print(f4.tell())
#
# f4.write(' this is python course')
# print(f4.tell())
# f4.seek(0)
# print(f4.tell())
# print(f4.read())
# print(f4.tell())
# f4.close()

#to append: add something in the existing file at the end of the file
# f1=open('file_1','a')
# f1.write(' Hello python files')
# print(f1.tell())
# f1.seek(0)
# print(f1.tell())

#to append and read: a+=> it will not erase the previous content
# f1=open('file_1','a+')
# f1.write('this is append and read added at the end ')
# print(f1.tell())
# f1.seek(0)
# print(f1.read())
# f1.write(' \njenny\'s lecture ')
# f1.seek(0)
# print(f1.read())

#to read an image: : rb
# img=open('image.png','rb')
# img2=open('image2.png','wb')
# for i in img:
#     img2.write(i)
# print(img.read())
