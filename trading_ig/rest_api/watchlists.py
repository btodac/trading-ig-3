from dataclasses import dataclass
from typing import Any

from trading_ig.rest_api.api_enums import IGRestAPIVersion, RequestType
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData


class FetchAllWatchlists(RestApiCall):

    def __init__(self):
        self.base_endpoint = "/watchlists"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = RequestData()


@dataclass
class CreateWatchlistData(RequestData):
    name: str
    epics: str


class CreateWatchlist(RestApiCall):

    def __init__(self, name: str, epics: str):
        self.base_endpoint = "/watchlists"
        self.request_type = RequestType.POST
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = CreateWatchlistData(name=name, epics=epics)


@dataclass
class DeleteWatchlistArguments(Arguments):
    watchlist_id: str

    def as_string(self):
        return f"/{self.watchlist_id}"


class DeleteWatchlist(RestApiCall):

    def __init__(self, watchlist_id: str):
        self.base_endpoint = "/watchlists"
        self.request_type = RequestType.DELETE
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = DeleteWatchlistArguments(watchlist_id=watchlist_id)
        self.request_data = RequestData()


@dataclass
class FetchWatchlistMarketsArguments(Arguments):
    watchlist_id: str

    def as_string(self):
        return f"/{self.watchlist_id}"


class FetchWatchlistMarkets(RestApiCall):

    def __init__(self, watchlist_id: str):
        self.base_endpoint = "/watchlists"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchWatchlistMarketsArguments(watchlist_id=watchlist_id)
        self.request_data = RequestData()


@dataclass
class AddMarketToWatchlistData(RequestData):
    epic: str


@dataclass
class AddMarketToWatchlistArguments(Arguments):
    watchlist_id: str

    def as_string(self):
        return f"/{self.watchlist_id}"


class AddMarketToWatchlist(RestApiCall):

    def __init__(self, watchlist_id: str, epic: str):
        self.base_endpoint = "/watchlists"
        self.request_type = RequestType.PUT
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = AddMarketToWatchlistArguments(watchlist_id=watchlist_id)
        self.request_data = AddMarketToWatchlistData(epic=epic)


@dataclass
class RemoveMarketFromWatchlistArguments(Arguments):
    watchlist_id: str
    epic: str

    def as_string(self):
        return f"/{self.watchlist_id}/{self.epic}"


class RemoveMarketFromWatchlist(RestApiCall):

    def __init__(self, watchlist_id: str, epic: str):
        self.base_endpoint = "/watchlists"
        self.request_type = RequestType.DELETE
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = RemoveMarketFromWatchlistArguments(
            watchlist_id=watchlist_id,
            epic=epic,
        )
        self.request_data = RequestData()
