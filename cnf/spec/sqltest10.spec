ROUTES :: PRICE:NOT_NULL
LOADS:: load_id:NULL, CUSTOMER_ID:NOT_NULL, WEIGHT:NOT_NULL, START_TIME:NULL


assume:: price > 0, SYSDATE > 0
assert:: price > 0, SYSDATE > 0


**** These lines will be ignored, but not above of this
**** individual predicates MUST be separated by COMMA(,)

**** a predicate must be written in PlSQL accepting Format (i.e. may contain AND, OR, NOT & BETWEEN)

####### Adhere to the STYLE STRICTLY, Attribute info must be EITHER <null> OR <not_null>

------------ '=' means comparison in constraints, don't put '==' for this, if done, will cause parsing ERROR

@@@@@@@@@@@@@@@@@@ Always put EACH and EVERY table info before CONSTRAINTS (i.e., assume and assert)
%%%%%%%%%%%%%%%%%%%%%%% EVERY table attribute must be present alongside tablename adhering to the STYLE

//////////// this is indicator spec file for cnf, don't delete it. (will contain both ASSUME & ASSERT)