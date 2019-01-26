CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN
    ASSUME X>15;
    Y := X-100;
    IF X>Y THEN
      X := X-50;
      X := X*9;
    ELSIF X<Y THEN
      Y := X-5;
    ELSE
      X := X+40;
    END IF;
    X := X-2;
    ASSERT X>0;
  END;
