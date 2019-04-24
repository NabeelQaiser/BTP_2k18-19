CREATE OR REPLACE PROCEDURE test(x IN VARCHAR, y IN VARCHAR)
IS
   BEGIN
       x := 5;
       if  x > 3  then
           
             update t set b = b - 10 where a = y;
            
       end if;
       
       if x < 10 then
       y := x + 3;
       x := y;
       end if;
       
    end;
end;
