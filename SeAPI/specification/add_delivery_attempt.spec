delivery_status:: id: NOT_NULL, status:NULL
delivery_attempt:: parcel_id:NOT_NULL, courier_id:NOT_NULL, attempt_timestamp:NULL, delivery_status_id:NULL


assume:: id > 0, delivery_status_id > 0
assert:: id > 0, delivery_status_id > 0
