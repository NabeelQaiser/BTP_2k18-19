CREATE OR REPLACE PROCEDURE EMP_SALARY_INCREASE (EMP_ID IN EMPTBL.EMPID%TYPE, SALARY_INC IN OUT EMPTBL.SALARY%TYPE) 

 IS 
 
 DECLARE
   TMP_SAL NUMBER;
   SALARY_INOUT NUMBER; 

 BEGIN
	ASSUME TO_CORRECT_PROBLEMS_IN_SE_API > 0 ;
 

   SELECT SALARY INTO TMP_SAL 
    FROM EMP_TBL
    WHERE EMPID = EMP_ID; 

   IF TMP_SAL BETWEEN 10000 AND 20000 THEN 

      SALARY_INOUT := TMP_SAL * 1.2; 

   ELSIF TMP_SAL BETWEEN 20000 AND 30000 THEN 

      SALARY_INOUT := TMP_SAL * 1.3; 

   ELSIF TMP_SAL > 30000 THEN 
        SALARY_INOUT := TMP_SAL * 1.4; 
   

   END IF; 

 ASSERT TO_CORRECT_PROBLEMS_IN_SE_API > 0 ;
	END;