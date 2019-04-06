PROCEDURE TEST(M IN NUMBER) IS
    MY_MAX NUMBER;
    CURSOR G IS SELECT MAX(A) FROM T
            WHERE A>=M+5 AND C IN (SELECT G FROM U WHERE D>=50);
    BEGIN
	ASSUME A>15 AND J>15 ;

        OPEN G;
        FETCH G INTO MY_MAX;
        CLOSE G;
        SELECT AVG(E), MAX(F) INTO X, Y FROM T
                                  JOIN U ON B=D
                                  JOIN V ON G=H
                    WHERE E>=M+5 AND C<99;
        IF MY_MAX > Y THEN
            UPDATE V SET J=J*(X-9), F=Y-9 WHERE J>10 AND F<=(X+Y);
        ELSIF MY_MAX < Y THEN
            UPDATE T SET A=A*(X-9), B=Y-9 WHERE A>10 AND B<=(X+Y);
        ELSE
            INSERT INTO T(A, B, C) VALUES (MY_MAX-X, MY_MAX-Y, Y*(X-2));
        END IF;
    ASSERT A>0 AND J>10 ;
	END;

-- C2--G
-- T2--U
-- B2--D
-- A2--E
-- B3--F
-- T3--V
-- C3--H
-- A3--J
-- D2--K
-- D3--L