newtable :: t_id : not_null, t_price : not_null, t_amount : not_null
oldtable :: t_id : not_null, t_price : not_null

assume :: amount > 0 and t_price > 0 and price > 0
assert :: price > 0
