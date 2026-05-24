from enum import IntEnum, StrEnum

class IGRestAPIVersion(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class RequestType(StrEnum):
    PUT = "put"
    POST = "post"
    GET = "get"
    DELETE = "delete"


class Direction(StrEnum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(StrEnum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    QUOTE = "QUOTE"


class TimeInForce(StrEnum):
    EXECUTE_AND_ELIMINATE = "EXECUTE_AND_ELIMINATE"
    FILL_OR_KILL = "FILL_OR_KILL"
    
