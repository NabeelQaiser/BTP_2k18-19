CREATE OR REPLACE PROCEDURE test(x IN VARCHAR, y IN VARCHAR)
IS
  BEGIN
    assume x>15;
    y := x-100;
    if x>y then
      x := x-50;
      x := x*9;
    elsif x<y then
      y := x-5;
    else
      x := x+40;
    end if;
    x := x-2;
    assert x>0;
  END;
