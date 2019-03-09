-- HTTPS://GITHUB.COM/LEWAN110/HOTEL-ROOM-RESERVATION-DATABASE/BLOB/MASTER/PROC.SQL


PROCEDURE BILL (P_RESERVATION_ID IN NUMBER) IS
        N_O_VISITS   NUMBER;
        FINAL_COST   NUMBER;
        TO_PAY      NUMBER;
        DISCOUNT     NUMBER;
    BEGIN
	ASSUME TO_PAY > 0 ;

        SELECT
            COUNT(*)
        INTO N_O_VISITS
        FROM
            CLIENTS
            JOIN CLIENT_RESERVATION ON PESEL_C = PESEL
            JOIN RESERVATIONS ON RESERVATION_ID = RESERVATION_ID_R
        WHERE
            STATUS = COMPLETED;

        IF
            ( N_O_VISITS > 10 )
        THEN
            DISCOUNT := 10;
        ELSE
            DISCOUNT := 0;
        END IF;


        SELECT
            SUM(PRICE_PER_DAY)
        INTO FINAL_COST
        FROM
            ROOMS
            JOIN RESERVATIONS ON ROOM_ID = ROOM_ID_R
        WHERE
            RESERVATION_ID_R = P_RESERVATION_ID;

        TO_PAY:=FINAL_COST-FINAL_COST*(DISCOUNT/100);


ASSERT TO_PAY > 0 ;
	END;