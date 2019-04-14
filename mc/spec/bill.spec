clients:: pesel_c:NOT_NULL, first_name:NULL, last_name:NULL, telephone: NOT_NULL
client_reservation:: pesel:NOT_NULL, reservation_id:NOT_NULL
reservations:: reservation_id_r:NOT_NULL, status:NULL, date_of_purchase:NOT_NULL, beginning:NOT_NULL, ending:NOT_NULL, date_of_reservation:NOT_NULL, room_id_r:NOT_NULL
rooms:: room_id:NOT_NULL, capacity:NOT_NULL, price_per_day:NOT_NULL

PREDICATES:: to_pay > 0

