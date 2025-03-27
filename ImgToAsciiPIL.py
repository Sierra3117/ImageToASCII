import PIL
import PIL.Image
from LookUp import AsciiSetter1

img = PIL.Image.open('Sample1.webp')
#img = PIL.Image.open('Sample1.jpg')
imageData = img.load()
img1 = img.convert("L")
imageDataG = img1.load()

scale = 5

width, height = img.size 
print(imageData[0,0])
print(imageDataG[0,0])
# displaying the dimensions 
print(str(width) + "x" + str(height))
res = width*height
resOut = res/100
resW = 36
resH = 36
lst = [[None]*360] * 360
file1 = open("MyFile2.txt","a")

for y in range(0, height, scale):
    for x in range(0, width, scale):
        #retrieve single colands
        r = imageDataG[x,y]
        #g = imageDataG[x,y]
        #b = imageDataG[x,y]
        #print("R: ", r, "\n", "G: ", g, "\n", "B: ", b)
        
        lst[x][y] = AsciiSetter1(r)

        if x == scale:
            
            file1.write(lst[x][y] + "\n") 
            
        else:
            file1.write(lst[x][y])
#print(lst)

