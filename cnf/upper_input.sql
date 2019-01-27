CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR)
IS
  BEGIN
      X := X-100;

      IF X>50 THEN
          X := X-50;

          IF X > 10 THEN
              X := X-10;
          ELSIF X>20 THEN
              X := X-20;
          ELSE
              X := X-1;
          END IF;

          X := X*9;
      ELSIF X>100 THEN
          X := X-100;
      ELSIF X>200 THEN
          X := X-150;
      ELSE
          X := X+40;
      END IF;

      X := X-2;
      ASSERT X>0;
  END;
