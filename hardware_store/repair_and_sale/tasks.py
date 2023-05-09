import requests
from hardware_store.celery import app
from hardware_store.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from repair_and_sale.services.data_classes import BookingInfo, CallRequest
from repair_and_sale.services.utils import create_booking_message, create_call_request_message


@app.task()
def book_a_product_telegram_task(data):
    token = TELEGRAM_BOT_TOKEN
    chat_id = TELEGRAM_CHAT_ID
    booking_info = BookingInfo(data['phone_number'],
                               data['item_name'],
                               data['message'])
    message = create_booking_message(booking_info)
    data = {'chat_id': chat_id, 'text': message}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data=data)


@app.task()
def call_request_telegram_task(data):
    token = TELEGRAM_BOT_TOKEN
    chat_id = TELEGRAM_CHAT_ID
    call_request_data = CallRequest(data['phone_number'],
                                    data['name'])
    message = create_call_request_message(call_request_data)
    data = {'chat_id': chat_id, 'text': message}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data=data)
