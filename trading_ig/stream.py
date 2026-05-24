import logging

from lightstreamer.client import LightstreamerClient, Subscription, ClientListener

from trading_ig.rest import IGService, IGRestAPIVersion

logger = logging.getLogger(__name__)


class IGStreamService:
    def __init__(self, ig_service: IGService):
        self.ig_service = ig_service

        self.lightstreamerEndpoint = None
        self.acc_number = None
        self.ls_client = None

    def create_session(self, encryption: bool=False, version: IGRestAPIVersion=IGRestAPIVersion.TWO):
        ig_session = self.ig_service.create_session(
            encryption=encryption, version=str(version)
        )
        # if we have created a v3 session, we also need the session tokens
        if version == IGRestAPIVersion.THREE:
            self.ig_service.read_session(fetch_session_tokens="true")
        self.lightstreamerEndpoint = ig_session["lightstreamerEndpoint"]
        cst = self.ig_service.session.headers["CST"]
        xsecuritytoken = self.ig_service.session.headers["X-SECURITY-TOKEN"]
        ls_password = f"CST-{cst}|XST-{xsecuritytoken}" 

        # Establishing a new connection to Lightstreamer Server
        logger.info("Starting connection with %s", self.lightstreamerEndpoint)
        self.ls_client = LightstreamerClient(self.lightstreamerEndpoint)
        self.ls_client.connectionDetails.setUser(self.acc_number)
        self.ls_client.connectionDetails.setPassword(ls_password)
        try:
            self.ls_client.connect()
        except Exception as e:
            logger.error("Unable to connect to Lightstreamer Server")
            raise e

    def subscribe(self, subscription: Subscription):
        self.ls_client.subscribe(subscription)

    def unsubscribe(self, subscription: Subscription):
        self.ls_client.unsubscribe(subscription)

    def unsubscribe_all(self):
        for sub in self.ls_client.getSubscriptions():
            self.ls_client.unsubscribe(sub)

    def add_client_listener(self, listener: ClientListener):
        self.ls_client.addListener(listener)

    def remove_client_listener(self, listener: ClientListener):
        self.ls_client.removeListener(listener)

    def disconnect(self):
        self.unsubscribe_all()
        self.ls_client.disconnect()
