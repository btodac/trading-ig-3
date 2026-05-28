from dataclasses import dataclass
from typing import Any

from trading_ig.rest_api.api_enums import IGRestAPIVersion, RequestType
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData


@dataclass
class FetchClientSentimentByInstrumentArguments(Arguments):
    market_id: str | list[str]

    def as_string(self):
        if isinstance(self.market_id, (list, tuple)):
            market_ids = ",".join(self.market_id)
            return f"/?marketIds={market_ids}"
        return f"/{self.market_id}"


class FetchClientSentimentByInstrument(RestApiCall):

    def __init__(self, market_id: str | list[str]):
        self.base_endpoint = "/clientsentiment"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchClientSentimentByInstrumentArguments(market_id=market_id)
        self.request_data = RequestData()


@dataclass
class FetchRelatedClientSentimentByInstrumentArguments(Arguments):
    market_id: str

    def as_string(self):
        return f"/related/{self.market_id}"


class FetchRelatedClientSentimentByInstrument(RestApiCall):

    def __init__(self, market_id: str):
        self.base_endpoint = "/clientsentiment"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchRelatedClientSentimentByInstrumentArguments(market_id=market_id)
        self.request_data = RequestData()


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


@dataclass
class FetchHistoricalPricesByEpicArguments(Arguments):
    epic: str

    def as_string(self):
        return f"/{self.epic}"


@dataclass
class FetchHistoricalPricesByEpicData(RequestData):
    resolution: str | None = None
    from_: str | None = None
    to: str | None = None
    max: int | None = None
    pageSize: int = 20
    pageNumber: int | None = None

    def to_json(self):
        payload = super().to_json()
        if "from_" in payload:
            payload["from"] = payload.pop("from_")
        return payload


class FetchHistoricalPricesByEpic(RestApiCall):

    def __init__(
        self,
        epic: str,
        resolution: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        numpoints: int | None = None,
        pagesize: int = 20,
        page_number: int | None = None,
    ):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.THREE
        self.arguments = FetchHistoricalPricesByEpicArguments(epic=epic)
        self.request_data = FetchHistoricalPricesByEpicData(
            resolution=resolution,
            from_=start_date,
            to=end_date,
            max=numpoints,
            pageSize=pagesize,
            pageNumber=page_number,
        )


@dataclass
class FetchHistoricalPricesByEpicAndNumPointsArguments(Arguments):
    epic: str
    resolution: str
    numpoints: int

    def as_string(self):
        return f"/{self.epic}/{self.resolution}/{self.numpoints}"


class FetchHistoricalPricesByEpicAndNumPoints(RestApiCall):

    def __init__(self, epic: str, resolution: str, numpoints: int):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = FetchHistoricalPricesByEpicAndNumPointsArguments(
            epic=epic,
            resolution=resolution,
            numpoints=numpoints,
        )
        self.request_data = RequestData()


@dataclass
class FetchHistoricalPricesByEpicAndDateRangeV1Data(RequestData):
    startdate: str
    enddate: str


@dataclass
class FetchHistoricalPricesByEpicAndDateRangeV1Arguments(Arguments):
    epic: str
    resolution: str

    def as_string(self):
        return f"/{self.epic}/{self.resolution}"


class FetchHistoricalPricesByEpicAndDateRangeV1(RestApiCall):

    def __init__(
        self,
        epic: str,
        resolution: str,
        start_date: str,
        end_date: str,
    ):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchHistoricalPricesByEpicAndDateRangeV1Arguments(
            epic=epic,
            resolution=resolution,
        )
        self.request_data = FetchHistoricalPricesByEpicAndDateRangeV1Data(
            startdate=start_date,
            enddate=end_date,
        )


@dataclass
class FetchHistoricalPricesByEpicAndDateRangeV2Arguments(Arguments):
    epic: str
    resolution: str
    start_date: str
    end_date: str

    def as_string(self):
        return f"/{self.epic}/{self.resolution}/{self.start_date}/{self.end_date}"


class FetchHistoricalPricesByEpicAndDateRangeV2(RestApiCall):

    def __init__(
        self,
        epic: str,
        resolution: str,
        start_date: str,
        end_date: str,
    ):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = FetchHistoricalPricesByEpicAndDateRangeV2Arguments(
            epic=epic,
            resolution=resolution,
            start_date=start_date,
            end_date=end_date,
        )
        self.request_data = RequestData()
