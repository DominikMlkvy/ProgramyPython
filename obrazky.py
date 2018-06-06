# program ktorý zoberie dva obrázky a "preloží ich dokopy" po riadkoch alebo do šachovnice
from PIL import Image

def output_img (input1, input2, size=50, chessboard=False):
    im1=Image.open (input1)
    im1.convert ("RGB")
    im2=Image.open (input2)
    im2.convert ("RGB")
    width1,height1 = im1.size
    width2, height2 = im2.size
    if width1<=width2:
        width=width1
    else:
        width=width2
    if height1<=height2:
        height=height1
    else:
        height=height2
    out=Image.new ("RGB", (width, height),(255,255,255))
    "out.save(""biela.jpg"")"
    for x in range (width):
        for y in range (height):
            if chessboard is False or (y/size)%2==0:
                r1,g1,b1 = im1.getpixel((x,y))
                r2,g2,b2 = im2.getpixel((x,y))
                if (x/size)%2==1:
                    out.putpixel((x,y), (r1,g1,b1))
                else:
                    out.putpixel((x,y), (r2,g2,b2))
            else:
                r1,g1,b1 = im1.getpixel((x,y))
                r2,g2,b2 = im2.getpixel((x,y))
                if (x/size)%2==0:
                    out.putpixel((x,y), (r1,g1,b1))
                else:
                    out.putpixel((x,y), (r2,g2,b2))
    out.show()
    out.save("vysledok.jpg")


output_img ("o1.jpg", "a.jpg", 30, chessboard=False)
