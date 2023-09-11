import pytchat
import datetime
from openpyxl import Workbook

def ioxl(wb, inp, inp_v, inp_c):

    ws = wb.active
    ws.append([inp, inp_v, inp_c])

def stop_scraping():
    print("Stopping the chat scraping process...")
    chat.stop()

wb = Workbook()

chat = pytchat.create(video_id="")

i = 0
while ((i<1000) and chat.is_alive()):
    for c in chat.get().sync_items():
        print(f"{c.datetime} \n[{c.author.name}] \n{c.message}")
        ioxl(wb, c.datetime, c.author.name, c.message)
        i+=1
        wb.save("scrape.xlsx")
    
    wb.save("some_random_test.xlsx")

