CREATE OR REPLACE PROCEDURE MY_ITEM(X NUMBER)
IS
  BEGIN
	ASSUME X > -50 ;


          IF X < 0 THEN
              X := -X;
          END IF;
          
  ASSERT X > 0 ;
	END;