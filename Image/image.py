'''
图片文件一定是jpg格式
在Excel表格里面的宏代码如下：
    Sub set_colour()
    Dim r As Range, arr
    For Each r In Range("A:ATE")
        arr = Split(r, ",")
        r.Interior.Color = RGB(CInt(arr(0)), CInt(arr(1)), CInt(arr(2)))
    Next
    End Sub

'''
from PIL import Image
imload = Image.open('1.jpg')
im = imload.convert("RGB")
width,height = im.size
demo = open('rbg.txt','a')

for y in range(height):
    for x in range(width):
        rgb = im.getpixel((x,y))
        rgb = str(rgb)
        demo.write(rgb[1:-1]+"\t")
    demo.write('\n')
demo.close()