# -*- coding: utf-8 -*-
import yt_dlp

def ดึงข้อมูลคลิป(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'bestaudio/best',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'หัวข้อ': info.get('title', 'ไม่ทราบชื่อ'),
                'ช่อง': info.get('uploader', 'ไม่ทราบช่อง'),
                'ความยาว': info.get('duration', 0),
                'ยอดวิว': f"{info.get('view_count', 0):,}",
                'ลิงก์เสียง': info.get('url')
            }
    except Exception:
        return None
      
