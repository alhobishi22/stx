import ccxt
import time
import asyncio
from telegram import Bot

# بيانات الاعتماد لبوت Telegram
bot_token = "7022214159:AAEuEYEw8r6I4EKB81dHixHBIlkrn7-6jX8"
  # استبدلها بالتوكن الخاص بك
chat_id = "1406072915" # استبدلها بمعرف الدردشة الخاص بك

# إعداد منصة التداول
exchange = ccxt.mexc()

# إعداد زوج العملات الرقمية
symbol = 'CTK/USDT'

# تحديد نسبة التغير المطلوبة والفترة الزمنية
change_percentage = 0.001  # نسبة التغير المطلوبة (0.1% كمثال)
time_interval = 2  # ساعتين بالثواني

# الحصول على السعر الأولي
initial_ticker = exchange.fetch_ticker(symbol)
initial_price = initial_ticker['last']

# إنشاء بوت Telegram
bot = Bot(token=bot_token)

async def main():
    global initial_price

    while True:
        # الانتظار للفترة المحددة
        time.sleep(time_interval)

        # الحصول على السعر الحالي
        current_ticker = exchange.fetch_ticker(symbol)
        current_price = current_ticker['last']

        # حساب نسبة التغير
        price_change = ((current_price - initial_price) / initial_price) * 100

        # التحقق من التغير في السعر
        if abs(price_change) >= change_percentage:
            message = f"تنبيه: تغير السعر بنسبة {price_change:.2f}% لـ {symbol}. السعر الحالي: {current_price}"
            print(message)

            # إرسال التنبيه عبر Telegram
            await bot.send_message(chat_id=chat_id, text=message)

        # تحديث السعر الأولي
        initial_price = current_price

# تشغيل الحلقة الرئيسية
asyncio.run(main())
