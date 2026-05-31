@echo off
title PAO PYTHON EXE BUILDER
echo [+] กำลังติดตั้งเครื่องมือ Python ที่จำเป็น...
pip install yt-dlp requests pygame pyinstaller
echo [+] กำลังมัดรวมโค้ดสร้างไฟล์ เปา.exe ตัวเทพ...
pyinstaller --onefile --name=เปา main.py
echo [✓] บิ้วด์เสร็จแล้วพี่!
echo [*] ไฟล์ เปา.exe ตัวเดี่ยว ๆ จะอยู่ในโฟลเดอร์ชื่อ dist นะครับ
pause
