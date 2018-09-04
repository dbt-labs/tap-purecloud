
from singer.catalog import Catalog, Schema, CatalogEntry
from . import schemas


def load_schema(ctx, tap_stream_id):
    schema = getattr(schemas, tap_stream_id)
    return schema


def discover(ctx):
    catalog = Catalog([])
    for stream in all_streams:
        schema = Schema.from_dict(load_schema(ctx, stream.tap_stream_id), inclusion="automatic")
        catalog.streams.append(CatalogEntry(
            stream=stream.tap_stream_id,
            tap_stream_id=stream.tap_stream_id,
            key_properties=stream.pk_fields,
            schema=schema,
        ))
    return catalog


class Stream(object):
    def __init__(self, tap_stream_id, pk_fields):
        self.tap_stream_id = tap_stream_id
        self.pk_fields = pk_fields


all_streams = [
    Stream("historical_adherence", ['userId', 'management_unit_id', 'startDate']),
    Stream("users", ['id']),
    Stream("groups", ['id']),
    Stream("location", ['id']),
    Stream("conversation", ['conversation_id']),
    Stream("user_state", ['id']),
    Stream("management_unit", ['id']),
    Stream("activity_codes", ['id', 'management_unit_id']),
    Stream("management_unit_users", ['user_id', 'management_unit_id']),
    Stream("user_schedule", ['start_date', 'user_id']),
    Stream("presence", ['id']),
    Stream("queues", ['id']),
    Stream("queue_membership", ['id']),
    Stream("queue_wrapup_code", ['id']),
]
