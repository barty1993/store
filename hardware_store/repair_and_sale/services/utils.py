from repair_and_sale.services.data_classes import BookingInfo, CallRequest


def create_booking_message(booking_info: BookingInfo):
    message = f"Клиент с номером {booking_info.phone_number} " \
              f"заинтересовался товаром:" \
              f"\n-------------\n" \
              f"{booking_info.item_name}" \
              f"\n-------------\n" \
              f"{booking_info.message}"

    return message


def create_call_request_message(call_request_data: CallRequest):
    message = f"Клиент {call_request_data.name}\n" \
              f"с номером {call_request_data.phone_number}\n" \
              f"запросил звонок!"

    return message
