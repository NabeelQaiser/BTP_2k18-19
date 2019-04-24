car ::license_number: NOT_NULL, brand_id: NOT_NULL, model: NULL, trunk_capacity: NULL, load_capacity: NULL, production_year: NULL, servicing_valid_thru: NULL
car_brand :: max_id: NOT_NULL, id:not_null, brand: NOT_NULL

assume :: id > 0, brand > 0, brand_id > 0, max_id > 0
assert :: id > 0, brand > 0, brand_id > 0, max_id > 0
