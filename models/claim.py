import ormar
from datetime import datetime
from typing import List, Optional

from . import BaseMeta
from .event import Event
from .attendee import Attendee
from .message import RequestMessage

class Claim(ormar.Model):

    class Meta(BaseMeta):
        tablename = "claims"
        constraints = [ormar.UniqueColumns('attendee','event')]

    id: int = ormar.Integer(primary_key=True)
    attendee: Attendee = ormar.ForeignKey(Attendee)
    event: Event = ormar.ForeignKey(Event)
    link: str = ormar.String(max_length=256)
    notified: Optional[bool] = ormar.Boolean(default=False)