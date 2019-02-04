CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN
      ASSUME A>15;
      X := X-36;
      Y := X-100;
      IF X>Y THEN
        X := X-50;
        X := X*9;
      ELSIF X<Y THEN
        Y := X-5;
        SELECT A INTO K FROM T WHERE A=X+3 AND B=X-3;
        INSERT INTO T (A, B) VALUES (X+5, Y-5);
        DELETE FROM T WHERE A=X+8 AND B=Y-8;
        UPDATE T SET A=A*(X-9*(Y-3)), B=Y-9 WHERE (A>10 AND B<=(X+Y)-50);
      ELSE

        X := X+40;
      END IF;

      ASSERT A>0;
  END;
