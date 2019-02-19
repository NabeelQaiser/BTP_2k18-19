CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN
  ASSUME v_type_id+Y > 10;
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
      END;
      ASSERT A-B+C>0;
  END;
