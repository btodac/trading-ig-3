from pydantic.dataclasses import dataclass

from trading_ig_core.rest_api.rest_api_enums import Direction, RejectionReasons
from trading_ig_core.streaming_api.updates import AffectedDealStatus, DealStatus, PositionStatus


@dataclass
class DealConfirmation:
    affectedDeals: list[AffectedDealStatus]
    date: str  # Transaction date
    dealId: str  # Deal identifier
    dealReference: str  # Deal reference
    dealStatus: DealStatus
    direction: Direction
    epic: str  # Instrument epic identifier
    expiry: str  # Instrument expiry
    guaranteedStop: bool  # True if guaranteed stop
    level: float  # Level
    limitDistance: float | None  # Limit distance
    limitLevel: float  # Limit level
    profit: float | None  # Profit
    profitCurrency: str | None  # Profit currency
    reason: RejectionReasons  # Describes the error (or success) condition for the specified trading operation
    size: float  # Size
    status: PositionStatus  # Position status
    stopDistance: float | None  # Stop distance
    stopLevel: float  # Stop level
    trailingStop: bool  # True if trailing stop
