PROCEDURE TEST(M IN NUMBER) IS
        N_O_VISITS   NUMBER;
        CURSOR G IS
        SELECT A
            FROM T
                JOIN T2 ON B=B2
                JOIN T3 ON C2=C3
            WHERE A2>=M+5 AND C<99;
    BEGIN
	ASSUME A>0 ;


        SELECT A, B3 INTO X, Y
            FROM T
                JOIN T2 ON B=B2
                JOIN T3 ON C2=C3
            WHERE A2>=M+5 AND C<99;

        NOTHING := 6;


    ASSERT A>0 ;
	END;