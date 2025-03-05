from datetime import datetime

import pytz
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.types import DateTime


class BaseMixin():
    @declared_attr
    def created(cls) -> Column:
        return Column(
            String(15),
            nullable=True,
            comment="作成者",
        )

    @declared_attr
    def created_at(cls) -> Column:
        return Column(
            DateTime,
            nullable=False,
            default=datetime.now(pytz.timezone("Asia/Tokyo")),
            comment="作成日時",
        )

    @declared_attr
    def updated(cls) -> Column:
        return Column(
            String(15),
            nullable=True,
            comment="更新者",
        )

    @declared_attr
    def updated_at(cls) -> Column:
        return Column(
            DateTime,
            nullable=False,
            default=datetime.now(pytz.timezone("Asia/Tokyo")),
            onupdate=datetime.now(pytz.timezone("Asia/Tokyo")),
            comment="更新日時",
        )
