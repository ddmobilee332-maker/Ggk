# -*- coding: utf-8 -*-
import sys
from เปา import หน้าหลัก

if __name__ == "__main__":
    try:
        หน้าหลัก()
    except KeyboardInterrupt:
        print("\n\x1b[31m[-] ปิดโปรแกรม\x1b[0m")
        sys.exit()
      
