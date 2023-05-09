from dataclasses import dataclass


@dataclass(frozen=True)
class CallRequest:
    phone_number: str
    name: str


@dataclass(frozen=True)
class BookingInfo:
    phone_number: str
    item_name: str
    message: str
