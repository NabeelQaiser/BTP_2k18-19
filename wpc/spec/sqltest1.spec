T :: A : not_null, B: null, C :null, D:not_null
T2 :: P:null, Q:not_null, R:not_null

assume :: A+p>=50, c+d=100, q+R<54
assert :: A+p>=50, c+d=100, q+R<54

**** These lines will be ignored, but not above of this
####### Adhere to the STYLE STRICTLY, Attribute info must be EITHER <null> OR <not_null>
------------ '=' means comparison in constraints, don't put '==' for this, if done, will cause parsing ERROR
@@@@@@@@@@@@@@@@@@ Always put EACH and EVERY table info before CONSTRAINTS
%%%%%%%%%%%%%%%%%%%%%%% EVERY table attribute must be present alongside tablename adhering to the STYLE