CREATE OR REPLACE PROCEDURE test(x IN VARCHAR, y IN VARCHAR)
IS
  BEGIN
    y := x-100;

    if x>y then
      x := x-50;
      x := x*9;
    end if;
    x := x-2;

  END;
