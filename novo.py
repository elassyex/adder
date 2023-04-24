import os, itertools, time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import telebot
from telebot import types
import requests
#chromedriver = f"/usr/bin/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# Set up bot
bot = telebot.TeleBot("6114172148:AAFUoZs9LFEIvAMhlNe570THBiUIRjHBBOM")

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True , one_time_keyboard = True)
    markup.row(telebot.types.KeyboardButton('Добавить новый номер'))
    # Send welcome message and instructions
    bot.reply_to(message, "Добро пожаловать в бота Adder Numbers! Нажмите «Добавить новый номер», чтобы начать.", reply_markup=markup)
    
# Handler for text messages
@bot.message_handler(func=lambda message: message.text == 'Добавить новый номер')
def start_search(message):
    # Remove the reply markup after the search is initiated
    markup = telebot.types.ReplyKeyboardRemove()
    # Ask the user to enter their search query
    bot.reply_to(message, "Введите номер, который хотите добавить:")
    # Register the next message as the search query
    bot.register_next_step_handler(message, add, markup)
def add(message, markup):
    # Get search query from message text
    bot.send_chat_action(message.chat.id, 'typing')
    query = message.text
    if '+7' not in query:
        bot.send_message(message.chat.id,f"пожалуйста, добавьте номер правильно +7xxxxxxxxxx")
    else:
        bot.send_message(message.chat.id,f"Добавление номера {query}")

        def delay(waiting_time=5):
            driver.implicitly_wait(waiting_time)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        xc =1
        driver.get(f"https://my.novofon.com/auth")
        number='+79649090038'
        
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/button').click()
            driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('k9587568143@yandex.ru')
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('ZPU5mbzbJNtaei1')

            driver.find_element(By.XPATH, '//*[@id="submit_button"]').click()
            time.sleep(1)
            driver.get(f"https://my.novofon.com/mypbx/in_calls/edit")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/main/div[1]/div/div[1]/div/div[1]/div/div[3]/div[2]/div[1]/div').click()
            delay(3)
            driver.find_element(By.XPATH, '//*[@id="telInputID"]').send_keys(int(query))
            delay(3)
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/main/div[1]/div/div[1]/div/div[7]/div[3]/section/div[1]/div[1]/div[2]').click()

            delay(3)
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/main/div[1]/div/div[1]/div/div[7]/div[4]/div/button[1]').click()
            time.sleep(2)
            print('done')
            bot.send_message(message.chat.id, f"номер {query} Добавлен .", reply_markup=markup)
        except:
            bot.reply_to(message, 'oooops')
        


    # Send search results as message

# Start bot
try:
    bot.polling()
except:
    pass
    bot.polling()
# xla = open("wilds.xlsx", "a")

    
