import smtplib
import requests
from bs4 import BeautifulSoup
import time
import schedule


# Url of the product website
URL = 'https://www.newegg.com/apple-mme73am-a-bluetooth-headset-3rd-generation-white/p/0G6-003J-00162?Description=airpods&cm_re=airpods-_-0G6-003J-00162-_-Product&quicklink=true'

# set the headers and user string
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

# function to check if the price has dropped


def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

# using BS to pull out product name and price from html
    title = soup.find(class_="product-title").get_text()
    price = soup.find(class_="price-current").get_text()
    conv_price = float(price[1:4])

    print(title)
    print("Current Price $", conv_price)

# if statement that send mail if the price goes below
    if(conv_price < 171):
        send_mail()

# function that sends an email if the prices fell down


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('pricetrack2022@gmail.com', 'bxaelgyfhvknajnp') #sender Email credentials

    subject = 'Price fell down!'
    body = "Check the link https: \n www.newegg.com/apple-mme73am-a-bluetooth-headset-3rd-generation-white/p/0G6-003J-00162?Description = airpods & cm_re = airpods-_-0G6-003J-00162-_-Product & quicklink = true"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pricetrack2022@gmail.com',  # Sender Email
        'momip68712@sofrge.com',  # Receiver Email
        msg
    )

    print("hurray!!! price has went down \n Email has been sent")

    server.quit()


# loop that allows the program to regularly check for prices (3 hr)
while(True):
    check_price()
    schedule.run_pending()
    time.sleep(10800)
