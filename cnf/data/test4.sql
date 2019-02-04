CREATE OR REPLACE PROCEDURE test(x IN VARCHAR, y IN VARCHAR)
IS
  BEGIN
    x := y-60;
    y := x-100;
    x := (y*x)/4-2;
    y := x-50;
    assert x>0;
  END;
