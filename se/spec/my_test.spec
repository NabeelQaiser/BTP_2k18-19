newtable :: t_id : not_null, t_price : not_null, t_amount : not_null
oldtable :: t_id : not_null, t_price : not_null

assume :: amount > 0 and t_price > 0 and price > 0
assert :: price > 0


**** These lines will be ignored, but not above of this
**** individual predicates MUST be separated by COMMA(,)

**** a predicate must be written in PlSQL accepting Format (i.e. may contain AND, OR, NOT & BETWEEN)

####### Adhere to the STYLE STRICTLY, Attribute info must be EITHER <null> OR <not_null>

------------ '=' means comparison in constraints, don't put '==' for this, if done, will cause parsing ERROR

@@@@@@@@@@@@@@@@@@ Always put EACH and EVERY table info before CONSTRAINTS (i.e., assume and assert)
%%%%%%%%%%%%%%%%%%%%%%% EVERY table attribute must be present alongside tablename adhering to the STYLE

//////////// this is indicator spec file for "se", don't delete it. (will contain both ASSUME & ASSERT)