CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN

      x := x-36;
      y := x-100;
      if x>y then
        x := x-50;
        x := x*9;
      elsif x<y then
        y := x-5;
        select A, B into X, Y from T where A=x+3 and B=x-3;
        insert into T (A, B) values (x+5, y-5);
        delete from T where A=x+8 and B=y-8;
        UPDATE T SET A=A*(X-9*(Y-3)), B=Y-9 WHERE (A>10 AND B<=(X+Y)-50);
      else
        x := x+40;
      end if;


  END;
