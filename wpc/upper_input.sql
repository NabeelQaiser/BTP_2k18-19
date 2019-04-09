PROCEDURE TEST(M IN NUMBER) IS
    MY_MAX NUMBER;
    CURSOR G IS SELECT MAX(A) FROM T
            WHERE A>=M+5 AND C IN (SELECT C2 FROM T2 WHERE B2>=50);
    BEGIN
	ASSUME A>15 AND A3>15 ;

        OPEN G;
        FETCH G INTO MY_MAX;
        CLOSE G;
        SELECT AVG(A2), MAX(B3) INTO X, Y FROM T
                                  JOIN T2 ON B=B2
                                  JOIN T3 ON C2=C3
                    WHERE A2>=M+5 AND C<99;
        IF MY_MAX > Y THEN
            UPDATE T3 SET A3=A3*(X-9), B3=Y-9 WHERE A3>10 AND B3<=(X+Y);
        ELSIF MY_MAX < Y THEN
            UPDATE T SET A=A*(X-9), B=Y-9 WHERE A>10 AND B<=(X+Y);
        ELSE
            INSERT INTO T(A, B, C) VALUES (MY_MAX-X, MY_MAX-Y, Y*(X-2));
        END IF;
    ASSERT A>0 AND A3>10 ;
	END;