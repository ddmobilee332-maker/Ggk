# -*- coding: utf-8 -*-
import os
import requests
from pygame import mixer
import time

def เล่นเสียงคลิป(url):
    if not url:
        print('\x1b[31m[!] ไม่พบไฟล์เสียงของคลิปนี้\x1b[0m')
        return

    ไฟล์ชั่วคราว = "temp_pao_audio.mp3"
    
    try:
        # ดาวน์โหลดไฟล์เสียงมาลงเครื่อง
        ตอบกลับ = requests.get(url, stream=True)
        with open(ไฟล์ชั่วคราว, 'wb') as f:
            for ก้อนข้อมูล in ตอบกลับ.iter_content(chunk_size=1024):
                if ก้อนข้อมูล:
                    f.write(ก้อนข้อมูล)
        
        # สั่งเปิดเสียงในเครื่องคอมพิวเตอร์
        mixer.init()
        mixer.music.load(ไฟล์ชั่วคราว)
        mixer.music.play()
        
        # รอให้เพลงเล่นจนจบ หรือกด Ctrl+C เพื่อข้าม
        while mixer.music.get_busy():
            time.sleep(1)
            
        mixer.music.unload()
        mixer.quit()
    except Exception as e:
        print(f'\x1b[31m[!] การเล่นเสียงขัดข้อง: {e}\x1b[0m')
    finally:
        # ลบไฟล์ขยะ
        if os.path.exists(ไฟล์ชั่วคราว):
            try:
                os.remove(ไฟล์ชั่วคราว)
            except:
                pass
              
