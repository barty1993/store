from repair_and_sale.services.data_classes import BookingInfo


def create_booking_message(booking_info: BookingInfo):
    message = f"Клиент с номером {booking_info.phone_number} " \
              f"заинтересовался товаром:" \
              f"\n-------------\n" \
              f"{booking_info.item_name}" \
              f"\n-------------\n" \
              f"{booking_info.message}"

    return message
