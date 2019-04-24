parcel:: id:NOT_NULL, max_id:NOT_NULL, sender_id:NOT_NULL,  receiver_id:NOT_NULL,   weight:NOT_NULL, height:NULL , width:NULL , dpth:NULL , dimension_class_id:NULL , parcel_type_id:NULL , status_id:NULL , current_warehouse_id:NULL , worth:NULL , is_cod:NULL , is_insured:NULL 
warehouse_parcel :: parcel_id:NULL , warehouse_id:NULL , entered_warehouse:NULL 

assume:: max_id > 0, id >= 0
assert:: max_id > 0, id >= 0
