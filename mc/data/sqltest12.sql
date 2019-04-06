
PROCEDURE test(M IN NUMBER) IS
    my_max NUMBER;
    CURSOR G IS SELECT max(A) FROM T
            WHERE A>=M+5 AND C in (SELECT C2 FROM T2 WHERE B2>=50);
    BEGIN
        open G;
        fetch G into my_max;
        close G;
        SELECT avg(A2), max(B3) INTO X, Y FROM T
                                  JOIN T2 ON B=B2
                                  JOIN T3 ON C2=C3
                    WHERE A2>=M+5 AND C<99;
        if my_max > Y THEN
            UPDATE T3 SET A3=A3*(X-9), B3=Y-9 WHERE A3>10 AND B3<=(X+Y);
        elsif my_max < Y THEN
            UPDATE T SET A=A*(X-9), B=Y-9 WHERE A>10 AND B<=(X+Y);
        else
            INSERT INTO T(A, B, C) VALUES (my_max-X, my_max-Y, Y*(X-2));
        END if;
    END;
