CREATE OR REPLACE PROCEDURE my_item(x NUMBER)
IS
  BEGIN

          IF x < 0 THEN
              x := -x;
          END IF;
          
  END;
