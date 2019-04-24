CREATE OR REPLACE PROCEDURE Sal_raise (Emp_id IN NUMBER, Sal_incr IN NUMBER) AS

BEGIN
      UPDATE Emp_tab
         SET Sal = Sal + Sal_incr
         WHERE Empno = Emp_id;
END Sal_raise;

