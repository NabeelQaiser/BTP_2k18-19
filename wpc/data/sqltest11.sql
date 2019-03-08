
PROCEDURE test(M IN NUMBER) IS
        n_o_visits   NUMBER;
        CURSOR G IS
        SELECT A
            FROM T
                JOIN T2 ON B=B2
                JOIN T3 ON C2=C3
            WHERE A2>=M+5 AND C<99;
    BEGIN

        SELECT A, B3 INTO X, Y
            FROM T
                JOIN T2 ON B=B2
                JOIN T3 ON C2=C3
            WHERE A2>=M+5 AND C<99;

        nothing := 6;


    END;
