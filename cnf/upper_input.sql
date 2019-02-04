CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN
    X := 60;
    Y := X-100;
    IF X > Y THEN
      X := 2*Y;
      ELSE
        Y := 2*X;
    END IF;
    ASSERT X>0;
  END;
