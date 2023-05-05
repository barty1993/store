from dataclasses import dataclass


@dataclass(frozen=True)
class BookingInfo:
    phone_number: str
    item_name: str
    message: str
