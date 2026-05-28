from dataclasses import dataclass

from trading_ig.rest_api.api_enums import IGRestAPIVersion, RequestType
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData


class FetchTopLevelNavigationNodes(RestApiCall):

    def __init__(self):
        self.base_endpoint = "/marketnavigation"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = RequestData()


@dataclass
class FetchSubNodesByNodeArguments(Arguments):
    node: str

    def as_string(self):
        return f"/{self.node}"


class FetchSubNodesByNode(RestApiCall):

    def __init__(self, node: str):
        self.base_endpoint = "/marketnavigation"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchSubNodesByNodeArguments(node=node)
        self.request_data = RequestData()


@dataclass
class FetchMarketByEpicArguments(Arguments):
    epic: str

    def as_string(self):
        return f"/{self.epic}"


class FetchMarketByEpic(RestApiCall):

    def __init__(self, epic: str):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.THREE
        self.arguments = FetchMarketByEpicArguments(epic=epic)
        self.request_data = RequestData()


@dataclass
class FetchMarketsByEpicsData(RequestData):
    epics: str
    filter: str | None = None


class FetchMarketsByEpics(RestApiCall):

    def __init__(self, epics: str, detailed: bool = True):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.request_data = FetchMarketsByEpicsData(
            epics=epics,
            filter="ALL" if detailed else "SNAPSHOT_ONLY",
        )


@dataclass
class SearchMarketsData(RequestData):
    searchTerm: str


class SearchMarkets(RestApiCall):

    def __init__(self, search_term: str):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = SearchMarketsData(searchTerm=search_term)


@dataclass
class SearchMarketsV2Data(RequestData):
    epics: str


class SearchMarketsV2(RestApiCall):

    def __init__(self, epics: str):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.request_data = SearchMarketsV2Data(epics=epics)

