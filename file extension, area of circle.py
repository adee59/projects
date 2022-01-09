'''
1 : extracting flie extenson and identifying the type
(----------------sample-----------------) 
'''
print('----------Know Your File Type------------')
print('1.) .py')
print('2.) .docx')
print('3.) .ppt')
print('4.) .pdf')
print('5.) .html')
txt = input("Enter the file name : ")

x = txt.rsplit(".")

n=x[1]
print('your file extension is : ',".",n)

ext={
    "py":"python file",
    "docx":"word file",
    "ppt":"presentation file",
    "pdf":"PDF file",
    "html":"HTML file"
    }

if n=="py":
    m=ext.get("py")
    print('your file type is : ',m)
elif n=='docx':
    m=ext.get("docx")
    print('your file type is : ',m)
elif n=='ppt':
    m=ext.get("ppt")
    print('your file type is : ',m)
elif n=='pdf':
    m=ext.get("pdf")
    print('your file type is : ',m)
elif n=='html':
    m=ext.get("html")
    print('your file type is : ',m)
else:
    print('file type not identified. \n \n')


#2 : area of the circle

print('______________AREA OF CIRCLE_______________\n \n')
r= float(input("enter the radius ofthe circle (in cm):"))
ar=3.14*(r**2)
print("the area is : ",ar,'sq.cm')

