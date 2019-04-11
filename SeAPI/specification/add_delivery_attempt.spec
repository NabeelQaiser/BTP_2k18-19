delivery_status:: id: NOT NULL, status:NULL
delivery_attempt:: parcel_id:NOT NULL, courier_id:NOT NULL, attempt_timestamp:NULL, delivery_status_id:NULL


constraints:: id > 0, delivery_status_id > 0
