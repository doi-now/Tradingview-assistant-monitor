import requests
import time
import random
from PIL import ImageGrab as ig

LINE_TOKEN = "**************************" #Line token for monitor module
url = 'https://notify-api.line.me/api/notify'
data = {'message': "💻 Finished"}
headers = {'Authorization':'Bearer ' + LINE_TOKEN}

def capturebycolor():
    work = 0 # ไว้คำนวน ไม่ให้ไลน์ส่งซ้ำหลังจูนเสร็จ
    im = ig.grab(bbox=(50, 0, 980, 320))
    im.show() #####__________ บริเวณที่ตรวจสอบ ไว้ทดสอบ อาจปิดทีหลัง_______
    w, h = im.size
    x_scan = int(w/2) # tuned for TV tuner, one monitor
    y_scan = random.sample(range(0, h), 20) #static value, for not repeat sent alert!
    time.sleep(1)
    while True:
        im = ig.grab(bbox=(50, 0, 980, 320)) #ปรับคำแน่งตามนกฟ้า  left, top, right, bottom
        rgb_im = im.convert('RGB')
        for x in y_scan:
            r, g, b = rgb_im.getpixel((x_scan, x))
            print(r, g, b) ##### RGB______ที่อ่านได้ ไว้ทดสอบ อาจปิดทีหลัง_____
            if (r, g, b) == (174, 253, 215) and (work==0):
                im.save("img1.png","PNG")
                img = {'imageFile': open('img1.png','rb')} #Local picture File
                session = requests.Session()
                time.sleep(1)
                try:
                    session_post = session.post(url, headers=headers, files=img, data =data)
                except Exception as e:
                    print(e)
                work = 1
                break;
            if (r, g, b) == (174, 253, 215):
                work = 1
                break;
            else:
                work = 0
                break;
        time.sleep(60)  #เช็คทุก 60 วินาที

capturebycolor()
