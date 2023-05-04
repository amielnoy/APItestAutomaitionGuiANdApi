from enum import Enum


class Detection(Enum):
    IP_BLACK_LIST = 1
    IP_WHITE_LIST = 2
    RECIPTENT_WHITE_LIST = 3
    SENDER_BLACK_LIST = 4
    SENDER_MAIL_WHITE_LIST = 5
    URL_BLACK_LIST = 6
    URL_WHITE_LIST = 7
    HASH_WHITE_LIST = 8
