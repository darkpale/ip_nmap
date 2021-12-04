#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
İllegalplatform.co Özeldir.
EDİTED BY DarkPale

1) Hızlı Tarama
2) Servis ve Versiyon Bilgisi
3) İşletim Sistemi Bilgisi
4) Açık İP Adresilerini Öğrenme
5) Açık Portları Öğrenme
6) TCP Taraması
7) Script Database Güncelleme
8) İşletim Sistemi Keşifleri
""")

islemno = raw_input("İşlem Numarasını Girin: ")



if(islemno=="1"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap " + hedefip)
elif(islemno=="2"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap -O " + hedefip)
elif(islemno=="4"):
	hedefip = raw_input("Hedef İp Girin ")
	os.system("nmap -sn -n -v --open" + hedefip )
elif(islemno=="5"):
	hedefip = raw_input("Hedef İp Girin ")
	os.system("sudo nmap -Pn -sS -n -v --reason --open" + hedefip )
elif(islemno=="6"):
	hedefip = raw_input("Hedef İp Girin ")
	os.system("sudo nmap -sN" + hedefip )
	elif(islemno=="7"):
		os.system("nmap — script-updatedb")
elif(islemno=="8")
    hedefip = raw_input("Hedef İp Girin ")
	os.system("nmap –osscan-guess" + hedefip )



	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
