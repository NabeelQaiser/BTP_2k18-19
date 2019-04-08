T :: A : not_null, B: null, C :null, D:not_null
T2 :: P:null, Q:not_null, R:not_null

PREDICATES :: A+p>=50, c+d=100

**** These lines will be ignored, but not above of this
**** individual predicates MUST be separated by COMMA(,)
**** a predicate must be written in PlSQL accepting Format (i.e. may contain AND, OR, NOT & BETWEEN)
####### Adhere to the STYLE STRICTLY, Attribute info must be EITHER <null> OR <not_null>
------------ '=' means comparison in constraints, don't put '==' for this, if done, will cause parsing ERROR
@@@@@@@@@@@@@@@@@@ Always put EACH and EVERY table info before predicates
%%%%%%%%%%%%%%%%%%%%%%% EVERY table attribute must be present alongside tablename adhering to the STYLE