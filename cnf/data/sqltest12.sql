
PROCEDURE test(M IN NUMBER) IS
    my_max NUMBER;
    CURSOR G IS SELECT max(A) FROM T
            WHERE A>=M+5 AND C in (SELECT G FROM U WHERE D>=50);
    BEGIN
        open G;
        fetch G into my_max;
        close G;
        SELECT avg(E), max(F) INTO X, Y FROM T
                                  JOIN U ON B=D
                                  JOIN V ON G=H
                    WHERE E>=M+5 AND C<99;
        if my_max > Y THEN
            UPDATE V SET J=J*(X-9), F=Y-9 WHERE J>10 AND F<=(X+Y);
        elsif my_max < Y THEN
            UPDATE T SET A=A*(X-9), B=Y-9 WHERE A>10 AND B<=(X+Y);
        else
            INSERT INTO T(A, B, C) VALUES (my_max-X, my_max-Y, Y*(X-2));
        END if;
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