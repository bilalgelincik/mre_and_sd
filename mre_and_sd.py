import os
import math

while_sayac=2
list_point=os.listdir(r"C:\Users\bilal\Desktop\test_labels_ham")
sayac=1
sonuc=0
list_mre=[]
while while_sayac<21:
    for i in list_point:

        dosya=open(r"C:\Users\bilal\Desktop\1200_models\cikti_x_model_1200" + "\\" + i ,"r",encoding="utf-8")
        while sayac<while_sayac:
            text_readline=dosya.readline().rstrip().split(",")
            sayac+=1

        sayac=1
        coordinat_x_predict=float(text_readline[0])
        coordinat_y_predict=float(text_readline[1])

        dosya.close()

        dosya=open(r"C:\Users\bilal\Desktop\test_labels_ham" + "\\" + i ,"r",encoding="utf-8")
        while sayac<while_sayac:
            text_readline=dosya.readline().rstrip().split(",")
            sayac+=1
        
        sayac=1
        coordinat_x_test=float(text_readline[0])
        coordinat_y_test=float(text_readline[1])
        dosya.close()

        x_kare=(coordinat_x_predict - coordinat_x_test)
        x_kare=x_kare*x_kare

        y_kare=(coordinat_y_predict-coordinat_y_test)
        y_kare=y_kare*y_kare

        sonuc=sonuc + (math.sqrt(x_kare+y_kare))

    while_sayac+=1
    mm=0.1
    sonuc=((sonuc/100)*mm)
    list_mre.append(sonuc)


while_sayac=2
sayac=1
sonuc=0
list_sayac=0
list_sd=[]
while while_sayac<21:
    for i in list_point:

        dosya=open(r"C:\Users\bilal\Desktop\1200_models\cikti_x_model_1200" + "\\" + i ,"r",encoding="utf-8")
        while sayac<while_sayac:
            text_readline=dosya.readline().rstrip().split(",")
            sayac+=1

        sayac=1
        coordinat_x_predict=float(text_readline[0])
        coordinat_y_predict=float(text_readline[1])

        dosya.close()

        dosya=open(r"C:\Users\bilal\Desktop\test_labels_ham" + "\\" + i ,"r",encoding="utf-8")
        while sayac<while_sayac:
            text_readline=dosya.readline().rstrip().split(",")
            sayac+=1
        
        sayac=1
        coordinat_x_test=float(text_readline[0])
        coordinat_y_test=float(text_readline[1])
        dosya.close()

        x_kare=(coordinat_x_predict - coordinat_x_test)
        x_kare=x_kare*x_kare

        y_kare=(coordinat_y_predict-coordinat_y_test)
        y_kare=y_kare*y_kare

        mm=0.1
        sd_ham=((math.sqrt(x_kare+y_kare))*mm)-float(list_mre[list_sayac])

        sonuc=sonuc + (sd_ham*sd_ham)

    
    while_sayac+=1
    list_sayac+=1
    sonuc=math.sqrt(sonuc/99)
    list_sd.append(sonuc)
    sonuc=0    

print(list_mre)
print(list_sd)
