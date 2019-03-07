CREATE OR REPLACE PROCEDURE test(x IN VARCHAR, y IN VARCHAR)
IS
  BEGIN

      x := x-50;
      select max(A) into K from T where A=x+3 and B=x-3;

  END;
