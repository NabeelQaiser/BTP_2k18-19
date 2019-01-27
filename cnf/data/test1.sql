CREATE OR REPLACE PROCEDURE test(x IN VARCHAR, y IN VARCHAR)
IS
  BEGIN
    x := 60;
    y := x-100;
    if x > y then
      x := 2*y;
      y := y + 2;
      else
        y := 2*x;
    end if;
    assert x>0;
  END;
