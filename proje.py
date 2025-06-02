
import cv2
from PIL import Image ,ImageChops,ImageOps
resim1=Image.open("ilkhali.jpg")
resim2=Image.open("sonhali.jpg")


fark = ImageChops.difference(resim1, resim2)
resim1.show()
resim2.show()
#fark.show()
im3=fark.save("im3.jpg")
img=Image.open("im3.jpg").convert("L")
img1=ImageOps.colorize(img,black="black",white="white")
img1.show()
im4=img1.save("im4.jpg")
image = cv2.imread("im4.jpg")

height= image.shape[0]
width = image.shape[1]
size = height*width

white = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
white = cv2.GaussianBlur(white, (7, 7), 0)

_,thresh = cv2.threshold(white,60,255,cv2.THRESH_BINARY)

cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
size_elements = 0
for cnt in cnts:
    cv2.drawContours(image,cnts, -1, (0, 0, 255), 3)
    size_elements += cv2.contourArea(cnt)

imS = cv2.resize(image, (1024, 768))
cv2.imshow("Image", imS)
print("toplam piksel alanı : ", size_elements)
print("resim boyutu : ", size)
eriyenalan=2.500*size_elements
print("eriyen alan:",eriyenalan)
gunluk_eriyen=eriyenalan/12
print("gunluk eriyen alan: ",gunluk_eriyen)
giris=int(input("hesaplanacak yılı giriniz:"))
x=giris*gunluk_eriyen*365
print("girilen yıldaki değişim",x)
cv2.waitKey(0)

