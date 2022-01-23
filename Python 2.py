from turtle import *

bgcolor('black') #untuk mengganti background color
speed(0.5) #speed berfungsi untuk mengatur kecepatan keluarnya lingkaran
        #Defaultnya 0, semakin kecil maka semakin cepat keluarnya lingkaran
hideturtle()
for i in range (400): #semakin gede range maka semakin besar lingkaran tersebut dan semakin banyak
    color('yellow') #untuk mengatur warna pada lingkaran
    circle(i*0.6)   #untuk mengartur ukuran lingkaran
    color('green')
    circle(i*0.4)
    color('yellow')
    circle(i*0.6)
    color('green')
    circle(i*0.4)
    right(3) #untuk mengatur arah lingkaran keluar kalo LEFT maka arahnya ke kiri
    forward(3) #untuk mengatur keluarnya lingkaran kalo backward maka lingkaran akan kebelakang
done()