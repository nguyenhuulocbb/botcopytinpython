from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup

def get_news():
    list_news = []
    r = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})
    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)
    return list_news

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin Chao {update.effective_user.first_name}')

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_news()
    str1 = ""
    for item in data:
        str1 += item["title"]+"\n"
    await update.message.reply_text(f'{str1}')

app = ApplicationBuilder().token("6431697703:AAFbGGSQxRSL4Pjm0Mw6AS2940Uyj3391eE").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("news", news))

app.run_polling()