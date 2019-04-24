courier:: id:NOT_NULL, max_id:NOT_NULL, pesel:NULL, name:NULL, surname:NULL, street:NULL, house_number:NULL, apartment_number:NULL, postal_code:NULL, city:NULL, province:NULL, country_id:NULL, car_license_number:NULL, warehouse_id:NULL, phone_number:NULL, salary:NULL, contract_type:NULL,contract_start:NULL
courier_driving_license_category:: courier_id: NOT_NULL, driving_license_category_id:NOT_NULL

assume:: max_id > 0, id > 0
assert:: max_id > 0, id > 0
