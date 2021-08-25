#Dilay Sapmaz
#Object counting

from tkinter.filedialog import *
from PIL import Image, ImageTk
from copy import deepcopy
#import tkinter as tk
import numpy as np
#import csv
#import time
global nrows, ncols

'''
global tsfCanvas

#Global Variables
openedImage=None
binaryImage=None
framedImage=None
nCol, nRow, orNRow, orNCol = 0,0,0,0
pixelMapAsString=""

#GUI Creation
root = tk.Tk()
xSize,ySize = 900,600
size = str(xSize)+"x"+str(ySize)
root.geometry(size)
root.title("Programing Studio")
root.geometry("800x500")
root.configure(bg='white')
root.resizable(True,True)

for r in range(3):
    for c in range(3):
        if r == 0:
            Label(root, bg='white').grid(row=r, column=c, padx=150, pady=20)
        if c == 0:
            Label(root, bg='white', text="test1").grid(row = r, column = c, padx = 150, pady = 20)
        else:
            Label(root, bg='white', text="test2").grid(row = r, column = c, padx = 150, pady = 20)

#Opening an image
def openImage():
    try:
        openFileFormats = (("all files", "*.*"), ("png files", "*.png"))  # File formats for easy search
        path = askopenfilename(parent=root, filetypes=openFileFormats)  # Basic file pick gui
        fp = open(path, "rb")  # Read file as a byte map

        global openedImage
        openedImage = Image.open(fp).convert('1', dither=Image.NONE)  # Convert byte map to Image then grayscaling of the image
    except:
        reset()

    imageProcess()


def imageProcess():
    global openedImage
    nCol, nRow = openedImage.size
    print("-------------------------------------------")
    print("Image size : \nHorizontal : ",nCol,"\nVertical : ", nRow)
    print("-------------------------------------------")

    colorMap = openedImage.load() # Images to pixel map because of converting return average of RGB

    global framedImage
    # Creates an image with 2 additional columns and rows for framing edges
    framedImage = Image.new('RGB', ((nCol+2), (nRow+2)), color='black').convert('1', dither=Image.NONE)
    #convert 1 : black white image
    #convert L : gray scaled image

    for r in range(1,nRow+1):
        for c in range(1,nCol+1):
            framedImage.putpixel((c,r), colorMap[c-1,r-1]) #Coloring framed image

    colorMap = framedImage.load() # Images to pixel map
    orNCol,orNRow=nCol,nRow

    nCol, nRow = framedImage.size
    print("-------------------------------------------")
    print("Framed Image size : \nHorizontal : ", nCol, "\nVertical : ", nRow)
    print("-------------------------------------------")

    global binaryImage
    binaryImage = [[0 for x in range(nCol)] for y in range(nRow)]  # Set pixelValue sizes

    global pixelMapAsString

    #Create binary image according to pixel map
    for r in range(nRow):
        for c in range(nCol):
            if colorMap[c,r] > 200:
                binaryImage[r][c] = 1
            else:
                binaryImage[r][c] = 0
            pixelMapAsString +=  str(binaryImage[r][c])
        pixelMapAsString += "\n"

    print(pixelMapAsString)

    # Putting image to screen
    global img1
    defImg = ImageTk.PhotoImage(framedImage)
    img1.config(image=defImg)
    img1.image = defImg
    img1.update()


def reset():
    print("")


def writeBinaryToScreen():
    global binaryCanvas
    global pixelMapAsString
    fontSize = 3

    binaryCanvas.create_text(0,0, text=pixelMapAsString, font=("Ariel", fontSize, "bold"), tag="lvTag", anchor=NW)
    # anchor North West is used to position the image to top left corner
    # 0,0 gives relative position to anchor

    # for remove text from canvas use tag
    binaryCanvas.select_clear()
    #binaryCanvas.delete("lvTag")

    #for update you can remove and write text for every iteration
    binaryCanvas.update()
    reset()

def tsfgui(text):
    global tsfCanvas,nrows,ncols,binaryImage

    arrText = ""
    for r in range(nrows):
        for s in range(cols):
            arrText += str(arr[r][s])
            print(arr[r][s], end="")
        print("")
        arrText += "\n"
    tsfCanvas.select_clear()
    tsfCanvas.delete("tsf")
    tsfCanvas.create_text(200,200,text=arrText,font=("Ariel",3),tag="tsf")
    tsfCanvas.update()

def updateLevCanvas(text):

    tsfCanvas.select_clear()
    tsfCanvas.delete("tsf")
    tsfCanvas.create_text(200,200,text=arrText,font=("Ariel",3),tag="tsf")


writeBinaryButton = Button(root, text='Binary', borderwidth=10, command=writeBinaryToScreen, relief=RAISED)
writeBinaryButton.grid(row=0, column=1, sticky=NE, padx=20, pady=20)

selectButton = Button(root, text='Open', borderwidth=1, command=openImage, relief=RAISED)
selectButton.grid(row=0, column=0, sticky=NW, padx=20, pady=20)

writeBinary = Button(root, text='levialdi', borderwidth=10, command=levialdi, relief=RAISED)
writeBinary.grid(row=0, column=1, sticky=NE, padx=20, pady=20)

writeBinaryB = Button(root, text='tsf', borderwidth=10, command=tsf, relief=RAISED)
writeBinaryB.grid(row=0, column=1, sticky=NE, padx=20, pady=20)

# You should use canvas to edit text in label
binaryCanvas = Canvas(root, borderwidth=2, bg="white", bd=3, relief="groove")
binaryCanvas.grid(row=1, column=1, sticky=W + E + N + S)

img1 = Label(root, borderwidth=2, bg="white", fg="black", bd=3, relief="groove")
img1.grid(row=1, column=0, sticky=W + E + N + S)

root.mainloop()
'''

def main():
    global nrows, ncols
    img = Image.open('/Users/sapma/Desktop/NCC4_ITER128.png')
    img = readPILimg()
    arr = PIL2np(img)
    arr = frame(arr)

    #image's pixels to binary
    for i in range(0, len(arr)):
        for j in range(0, len(arr[1])):
            if arr[i][j] < 200:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
            print(arr[i][j], end = " ")
        print("")

    levialdi(arr)
    tsf(arr)


def levialdi(arr):
    global nrows, ncols
    #frame
    nrows = len(arr)
    ncols = len(arr[1])

    LevialdiIteration = 0 #ncc for levialdi
    counterlev = 0
    copy1 = deepcopy(arr)
    frame(copy1)
    flaglevi = True #control flag

    while flaglevi == True:
        LevialdiIteration += 1 #it checks the quantity of iteration
        arr = deepcopy(copy1)
        flaglevi = False
        for i in range(1, nrows-1):
            for j in range(1, ncols-1):
                #checked array,but changed on copy of an array
                if arr[i][j] == 0: #augmentation
                    if arr[i][j-1] == 1 and arr[i+1][j] == 1:
                        copy1[i][j] = 1
                        flaglevi = True
                elif arr[i][j] == 1:#delition
                    if arr[i][j-1] == 0 and arr[i+1][j-1] == 0 and arr[i+1][j] == 0:
                        copy1[i][j] = 0
                        flaglevi = True
                        if arr[i-1][j-1] == 0 and arr[i-1][j] == 0 and \
                                arr[i-1][j+1] == 0 and arr[i][j+1] == 0 and arr[i+1][j+1] == 0:
                            copy1[i][j] == 0
                            counterlev += 1
                            flaglevi = True
                else: #isolated
                    arr[i-1][j-1]==0 and arr[i-1][j]==0 and arr[i-1][j+1]==0 and arr[i][j+1]==0 and \
                            arr[i+1][j+1]==0 and arr[i+1][j]==0 and arr[i+1][j-1]==0 and arr[i][j-1]==0
                    counterlev +=1
                    copy1[i][j] == 0
                    flag= True



    print('Levialdi Counter: ' + str(counterlev))
    print('Levialdi Iterations: ' + str(LevialdiIteration))


def frame(arr):
    nrows = len(arr[0])
    ncols = len(arr[1])
    fram = np.zeros(shape=(nrows+2, ncols+2))

    for i in range(0, nrows):
        for j in range(0, ncols):
            fram[i+1][j+1] = arr[i][j]
    return fram


def tsf(arr):
    counterTSF = 0
    nrows = len(arr)
    ncols = len(arr[1])
    copy2 = deepcopy(arr)
    copy3 = deepcopy(copy2)
    flag = True
    TSFIteration = 0

    while flag == True:
        TSFIteration += 1
        flag = False
        bcheck = False #checking b for true or false. It is needed, unless code willnot run..

        for i in range(1, nrows-1, 2):
            for j in range(1, ncols-1, 2):
                b = bpequality(i, j, copy2)
                c = cpequality(i, j, copy2)
                z = zero(i, j, copy2)
                if copy2[i][j] == 0: #augmentation
                    if c == 1 and ((copy2[i][j-1] == 1 and copy2[i-1][j] == 1) or
                                   (copy2[i][j-1] == 1 and copy2[i+1][j] == 1)):
                        copy3[i][j] = 1
                        flag = True
                else: #deletion
                    if b == 0: #isolated
                        copy3[i][j] = 0 #changes ij 1 to 0(ortadakini sıfır yapıyor)
                        counterTSF += 1
                        flag = True
                    bcheck = False

                    if b != 1: #not isolated
                        bcheck = True
                    else: #when bp!=0
                        if copy2[i-1][j-1] == 0 and copy2[i-1][j+1] == 0: #p1=p3=0
                            bcheck = True

                    if bcheck == True:
                        if c == 1 and z:
                            copy3[i][j] = 0
                            flag = True

        for i in range(2, nrows-1, 2):
            for j in range(2, ncols-1, 2):
                b = bpequality(i, j, copy2)
                c = cpequality(i, j, copy2)
                z = zero(i, j, copy2)
                if copy2[i][j] == 0:
                    if c == 1 and ((copy2[i][j - 1] == 1 and copy2[i - 1][j] == 1) or
                                   (copy2[i][j - 1] == 1 and copy2[i + 1][j] == 1)):
                        copy3[i][j] = 1
                        flag = True
                else:
                    if b == 0:
                        copy3[i][j] = 0
                        counterTSF += 1
                        flag = True
                    bcheck = False
                    if b != 1:
                        bcheck = True
                    else:
                        if copy2[i-1][j-1] == 0 and copy2[i-1][j+1] == 0:
                            bcheck = True

                    if bcheck == True:
                        if c == 1 and z:
                            copy3[i][j] = 0
                            flag = True
        copy2 = deepcopy(copy3)

        for i in range(1, nrows-1, 2):
            for j in range(2, ncols-1, 2):
                b = bpequality(i, j, copy2)
                c = cpequality(i, j, copy2)
                z = zero(i, j, copy2)
                if copy2[i][j] == 0:
                    if c == 1 and ((copy2[i][j - 1] == 1 and copy2[i - 1][j] == 1) or
                                   (copy2[i][j - 1] == 1 and copy2[i + 1][j] == 1)):
                        copy3[i][j] = 1
                        flag = True
                else:
                    if b == 0:
                        copy3[i][j] = 0
                        counterTSF += 1
                        flag = True
                    bcheck = False
                    if b != 1:
                        bcheck = True
                    else:
                        if copy2[i-1][j-1] == 0 and copy2[i-1][j+1] == 0:
                            bcheck = True

                    if bcheck == True:
                        if c == 1 and z:
                            copy3[i][j] = 0
                            flag = True
        for i in range(2, nrows - 1, 2):
            for j in range(1, ncols - 1, 2):
                b = bpequality(i, j, copy2)
                c = cpequality(i, j, copy2)
                z = zero(i, j, copy2)
                if copy2[i][j] == 0:
                    if c == 1 and ((copy2[i][j-1] == 1 and copy2[i-1][j] == 1) or
                                   (copy2[i][j-1] == 1 and copy2[i+1][j] == 1)):
                        copy3[i][j] = 1
                        flag = True
                else:
                    if b == 0:
                        copy3[i][j] = 0
                        counterTSF += 1
                        flag = True
                    bcheck = False
                    if b != 1:
                        bcheck = True
                    else:
                        if copy2[i-1][j-1] == 0 and copy2[i-1][j+1] == 0:
                            bcheck = True

                    if bcheck == True:
                        if c == 1 and z:
                            copy3[i][j] = 0
                            flag = True
        copy2 = deepcopy(copy3)

    print("TSF counter: " + str(counterTSF))
    print("TSF iterations: " + str(TSFIteration))


def bpequality(a, b, arr):
    counterbp = 0
    neig8=[arr[a-1][b-1],arr[a-1][b],arr[a-1][b+1],arr[a][b+1], arr[a+1][b+1], arr[a+1][b], arr[a+1][b-1], arr[a][b-1]]

    for m in range (0,8):
        if neig8[m] == 1:
            counterbp += 1
    return counterbp


def cpequality(i, j, arr):
    neig8 = [arr[i-1][j-1],arr[i-1][j],arr[i-1][j+1],arr[i][j+1],arr[i+1][j+1],arr[i+1][j],arr[i+1][j-1],arr[i][j-1]]
    countercp = 0
    cevre = 0

    if neig8[1] == 1 and neig8[3] == 1 and neig8[2] == 0:
        neig8[2] = 1
    if neig8[3] == 1 and neig8[5] == 1 and neig8[4] == 0:
        neig8[4] = 1
    if neig8[5] == 1 and neig8[7] == 1 and neig8[6] == 0:
        neig8[6] = 1
    if neig8[7] == 1 and neig8[1] == 1 and neig8[0] == 0:
        neig8[0] = 1
    if(neig8[0] + neig8[1] + neig8[2] + neig8[3] + neig8[4] + neig8[5] + neig8[6] + neig8[7]) == 8:
        cevre = 1
        #tp
    for i in range(0,7):
        if neig8[i] == 0 and neig8[i+1] == 1:
            countercp += 1
    if neig8[7] == 0 and neig8[0] == 1:
            countercp += 1

    if cevre == 1:
        return 1
    else:
        return countercp


def zero(a, b, arr):
    zeros = 0
    neig8=[arr[a-1][b-1],arr[a-1][b],arr[a-1][b+1],arr[a][b+1],arr[a+1][b+1],arr[a+1][b],arr[a+1][b-1],arr[a][b-1]]

    if neig8[6] == 0 and neig8[7] == 0 and neig8[0] == 0:
        zeros += 1
    elif neig8[7] == 0 and neig8[0] == 0 and neig8[1] == 0:
        zeros += 1

    for i in range(0, 5):
        if neig8[i] == 0 and neig8[i+1] == 0 and neig8[i+2] == 0:
            zeros += 1
        else:
            continue
    return zeros


def readPILimg():
    img = Image.open('/Users/sapma/Desktop/NCC4_ITER128.png')
    img.show()
    img_gray = color2gray(img)
    img_gray.show()
    img_gray.save('/Users/sapma/Desktop/NCC4_ITER128.png')
    #new_img = img.resize((256,256))
    #new_img.show()
    return img_gray


#it makes the image gray
def color2gray(img):
    img_gray = img.convert('L')
    return img_gray


#it makes image to array
def PIL2np(img):
    global nrows, ncols
    ncols = img.size[0]
    nrows = img.size[1]
    print("nrows, ncols : ", nrows,ncols)
    imgarray = np.array(img.convert("L"))
    return imgarray


def np2PIL(im):
    print("size of arr: ",im.shape)
    img = Image.fromarray(np.uint8(im))
    return img


if __name__=='__main__':
    main()
