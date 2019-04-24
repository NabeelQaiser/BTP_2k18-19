ROUTES :: PRICE:NOT_NULL, SUM_WEIGHT:NOT_NULL
LOADS:: load_id:NULL, CUSTOMER_ID:NOT_NULL, WEIGHT:NOT_NULL, START_TIME:NULL, SUM_WEIGHT:NOT_NULL


assume:: big_discount >= 0 , low_discount >= 0 , wrong_discount >= 0 , price > 0, SYSDATE > 0
assert:: big_discount >= 0 , low_discount >= 0 , wrong_discount >= 0 , price > 0, SYSDATE > 0
