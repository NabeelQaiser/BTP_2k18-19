car :: id: NOT_NULL, brand: NOT_NULL
car_brand :: license_number: NOT_NULL, brand_id: NOT_NULL, model: NULL, trunk_capacity: NULL, load_capacity: NULL, production_year: NULL, servicing_valid_thru: NULL

assume :: id > 0, brand > 0, brand_id > 0, max_id > 0
assert :: id > 0, brand > 0, brand_id > 0, max_id > 0
