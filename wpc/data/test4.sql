CREATE OR REPLACE PROCEDURE test(x IN VARCHAR)
IS
  BEGIN
      x := x-100;

      if x>50 then
          x := x-50;
          x := x*9;
      elsif x>100 then
          x := x-100;

          if x > 10 then
              x := x-10;
          elsif x>20 then
              x := x-20;
          else
              x := x-1;
          end if;
      elsif x>200 then
          x := x-150;
      else
          x := x+40;
      end if;

      x := x-2;
      assert x>0;
  END;
