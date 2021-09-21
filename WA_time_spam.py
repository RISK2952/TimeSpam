#import pywhatkit as wk
import time
import pyautogui as pgi
from datetime import datetime

#wk.sendwhatmsg("PhoneNo.","Hehehehe",00,00)

Hr = 5

for i in range(Hr*60):
    time.sleep(60)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    pgi.write(current_time)
    pgi.press("enter")