CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN
      x := x-36;
      SELECT A, B INTO X, Z FROM T WHERE A=X+3;
      insert into T (A, B) values (x+5, y-5);
      delete from T where A=x+8 and B=y-8;
      UPDATE T SET A=A*(X-9*(Y-3)), B=Y-9 WHERE (A>10 AND B<=(X+Y)-50);
  END;
