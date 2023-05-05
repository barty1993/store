import requests
from hardware_store.celery import app
from hardware_store.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from repair_and_sale.services.data_classes import BookingInfo
from repair_and_sale.services.utils import create_booking_message


@app.task()
def send_message_to_telegram_task(data):
    token = TELEGRAM_BOT_TOKEN
    chat_id = TELEGRAM_CHAT_ID
    booking_info = BookingInfo(data['phone_number'],
                               data['item_name'],
                               data['message'])
    message = create_booking_message(booking_info)
    data = {'chat_id': chat_id, 'text': message}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data=data)
