CREATE OR REPLACE PROCEDURE test(x IN VARCHAR, y IN VARCHAR)
IS
  BEGIN

      x := x-50;
      select A into K from T where A=x+3 and B=x-3;
      insert into T (A, B) values (x+5, y-5);
      delete from T where A=x+8 and B=y-8;
      update T set A=x-9 where A>10;

  END;
