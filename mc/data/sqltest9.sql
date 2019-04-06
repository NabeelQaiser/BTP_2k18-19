CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN

    DECLARE
      v_type_id NUMBER;

      CURSOR Y IS
              SELECT A
              FROM T
              WHERE B = 50;
      CURSOR id IS
              SELECT B
              FROM T;
      BEGIN
          OPEN id;
          FETCH id INTO X;
          CLOSE id;
          INSERT INTO T(A, B, C) VALUES (X+5, X-5, Y*(Z-2));
          if x>y then
              x := x-50;
              x := x*9;
              delete from T where A=x+8 and B=y-8;
          elsif x<y then
              y := x-5;
              select A, B into X, Y from T where A=x+3 and B=x-3;
          else
              x := x+40;
              UPDATE T SET A=A*(X-9*(Y-3)), B=Y-9 WHERE (A>10 AND B<=(X+Y)-50);
          end if;

          IF K+L<55 OR (J>=66 AND A+B BETWEEN (X+10) AND Y+20) OR U>=60
          THEN
              SELECT A INTO GG FROM T WHERE A+C<55 AND (A+B BETWEEN (X+10) AND Y+20) OR Z>=60;
          END IF;

      END;

  END;
