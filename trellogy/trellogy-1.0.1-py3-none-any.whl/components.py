from .error import (TrellogyError,
                    NotEnoughParamsError, InvalidParamError)
from urllib.request import unquote
import requests


class Attachment:
    def __init__(self, **kwargs):
        try:
            self._id = kwargs['id']
            self._bytes = kwargs['bytes']
            self._date = kwargs['date']
            self._edgeColor = kwargs['edgeColor']
            self._idMember = kwargs['idMember']
            self._isUpload = kwargs['isUpload']
            self._mimeType = kwargs['mimeType']
            self._name = kwargs['name']
            self._previews = kwargs['previews']
            self._url = kwargs['url']
            self._pos = kwargs['pos']
        except KeyError as error:
            raise NotEnoughParamsError(error.__str__())

    @property
    def id(self):
        return self._id

    @property
    def bytes(self):
        return self._bytes

    @property
    def date(self):
        return self._date

    @property
    def edgeColor(self):
        return self._edgeColor

    @property
    def idMember(self):
        return self._idMember

    @property
    def isUpload(self):
        return self._isUpload

    @property
    def mimeType(self):
        return self._mimeType

    @property
    def name(self):
        return self._name

    @property
    def previews(self):
        return self._previews

    @property
    def url(self):
        return self._url

    @property
    def pos(self):
        return self._pos


class List:
    def __init__(self, **kwargs):
        try:
            self._key = kwargs['key']
            self._token = kwargs['token']
            self._idTrash = kwargs['idTrash']
            self._id = kwargs['id']
            self._name = kwargs['name']
            self._closed = kwargs['closed']
            self._idBoard = kwargs['idBoard']
            self._pos = kwargs['pos']

        except KeyError as error:
            raise NotEnoughParamsError(error.__str__())

        self._cards = None

    @property
    def idTrash(self):
        return self._idTrash

    @property
    def idBoard(self):
        return self._idBoard

    @property
    def closed(self):
        return self._closed

    @property
    def pos(self):
        return self._pos

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        if self._cards is None:
            self.read()

        return self._cards

    def delete(self):
        self.update(idBoard=self._idTrash)

    def archive(self):
        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}/closed?value=true&key={KEY}&token={TOKEN}'
        response = requests.put(url.format(
            LIST_ID=self._id,
            KEY=self._key,
            TOKEN=self._token
        ))
        if response.status_code != 200:
            raise TrellogyError(response.text)

    def read(self):
        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}/cards?fields=all&key={KEY}&token={TOKEN}'
        response = requests.get(url.format(
            LIST_ID=self._id, KEY=self._key, TOKEN=self._token
        ))
        if response.status_code != 200:
            raise TrellogyError(response.text)

        cards = response.json()
        self._cards = []
        for card in cards:
            self._cards.append(Card(key=self._key, token=self._token,
                                    idTrash=self._idTrash, **card))

    def update(self, **kwargs):
        VALID_KEYS = ['name', 'closed', 'idBoard', 'pos', 'subscribed']
        for key in kwargs.keys():
            if key not in VALID_KEYS:
                raise InvalidParamError(key)

        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}?key={KEY}&token={TOKEN}'.format(
                LIST_ID=self._id, KEY=self._key, TOKEN=self._token
            )

        params = map(lambda key: "{}={}".format(
            key, kwargs[key]), kwargs.keys())

        response = requests.put("&".join([url]+list(params)))

        if response.status_code != 200:
            raise TrellogyError(response.textt)

    def __repr__(self):
        return "<class 'trellogy.List'>"

    def __str__(self):
        return self._name


class Card:
    def __init__(self, **kwargs):
        self._key = kwargs['key']
        self._token = kwargs['token']
        self._attachments = None
        self._idTrash = kwargs['idTrash']
        self._id = kwargs["id"]
        self._address = kwargs["address"]
        self._checkItemStates = kwargs["checkItemStates"]
        self._closed = kwargs["closed"]
        self._coordinates = kwargs["coordinates"]
        self._creationMethod = kwargs["creationMethod"]
        self._dateLastActivity = kwargs["dateLastActivity"]
        self._desc = kwargs["desc"]
        self._descData = kwargs["descData"]
        self._dueReminder = kwargs["dueReminder"]
        self._idBoard = kwargs["idBoard"]
        self._idLabels = kwargs["idLabels"]
        self._idList = kwargs["idList"]
        self._idMembersVoted = kwargs["idMembersVoted"]
        self._idShort = kwargs["idShort"]
        self._idAttachmentCover = kwargs["idAttachmentCover"]
        self._limits = kwargs["limits"]
        self._locationName = kwargs["locationName"]
        self._manualCoverAttachment = kwargs["manualCoverAttachment"]
        self._name = kwargs["name"]
        self._pos = kwargs["pos"]
        self._shortLink = kwargs["shortLink"]
        self._isTemplate = kwargs["isTemplate"]
        self._badges = kwargs["badges"]
        self._dueComplete = kwargs["dueComplete"]
        self._due = kwargs["due"]
        self._idChecklists = kwargs["idChecklists"]
        self._idMembers = kwargs["idMembers"]
        self._labels = kwargs["labels"]
        self._shortUrl = kwargs["shortUrl"]
        self._subscribed = kwargs["subscribed"]
        self._url = kwargs["url"]
        self._cover = kwargs["cover"]

    def update(self, **kwargs):
        """
        Update attributes according to kwargs:
        """
        VALID_KEYS = ['desc', 'closed', 'idMembers',
                      'idAttachmentCover', 'idList', 'idLabels',
                      'idBoard', 'pos', 'due', 'dueComplete',
                      'subscribed', 'address', 'locationName', 'coordinates']

        for key in kwargs.keys():
            if key not in VALID_KEYS:
                raise InvalidParamError(key)

        url = 'https://api.trello.com/1/cards/' + \
            '{CARD_ID}?key={KEY}&token={TOKEN}'.format(
                CARD_ID=self._id, KEY=self._key, TOKEN=self._token
            )

        params = map(lambda key: "{}={}".format(
            key, kwargs[key]), kwargs.keys())

        response = requests.put("&".join([url]+list(params)))

        if response.status_code != 200:
            raise TrellogyError(response.textt)

    def archive(self):
        """
        Archive this card:
        """
        pass

    def delete(self):
        """
        Move this card to the trash_board:
        """
        pass

    @property
    def id(self):
        return self._id

    @property
    def address(self):
        return self._address

    @property
    def checkItemStates(self):
        return self._checkItemStates

    @property
    def closed(self):
        return self._closed

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def creationMethod(self):
        return self._creationMethod

    @property
    def dateLastActivity(self):
        return self._dateLastActivity

    @property
    def desc(self):
        return self._desc

    @property
    def descData(self):
        return self._descData

    @property
    def dueReminder(self):
        return self._dueReminder

    @property
    def idBoard(self):
        return self._idBoard

    @property
    def idLabels(self):
        return self._idLabels

    @property
    def idList(self):
        return self._idList

    @property
    def idMembersVoted(self):
        return self._idMembersVoted

    @property
    def idShort(self):
        return self._idShort

    @property
    def idAttachmentCover(self):
        return self._idAttachmentCover

    @property
    def limits(self):
        return self._limits

    @property
    def locationName(self):
        return self._locationName

    @property
    def manualCoverAttachment(self):
        return self._manualCoverAttachment

    @property
    def name(self):
        return self._name

    @property
    def pos(self):
        return self._pos

    @property
    def shortLink(self):
        return self._shortLink

    @property
    def isTemplate(self):
        return self._isTemplate

    @property
    def badges(self):
        return self._badges

    @property
    def dueComplete(self):
        return self._dueComplete

    @property
    def due(self):
        return self._due

    @property
    def idChecklists(self):
        return self._idChecklists

    @property
    def idMembers(self):
        return self._idMembers

    @property
    def labels(self):
        return self._labels

    @property
    def shortUrl(self):
        return self._shortUrl

    @property
    def subscribed(self):
        return self._subscribed

    @property
    def url(self):
        return self._url

    @property
    def cover(self):
        return self._cover

    @property
    def attachments(self):
        if not self._attachments:
            self.read_attachments()

        return self._attachments

    def read_attachments(self):
        url = 'https://api.trello.com/1/cards/' + \
            '{CARD_ID}/attachments?key={KEY}&token={TOKEN}'
        response = requests.get(url.format(
            CARD_ID=self._id, KEY=self._key, TOKEN=self._token
        ))
        if response.status_code != 200:
            raise TrellogyError(response.text)

        attachments = []
        for attachment in response.json():
            attachments.append(Attachment(**attachment))
        self._attachments = attachments

    def __repr__(self):
        return "<class 'trellogy.Card'>"

    def __str__(self):
        return self._name
