 CREATE OR REPLACE PROCEDURE T_Update( x IN NUMBER, y IN NUMBER) As
 BEGIN

 if x >= 3 then
   update t set b = b - 10 where a = y;
 END if;

 END;
