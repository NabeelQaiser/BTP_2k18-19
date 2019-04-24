
PROCEDURE bill (p_reservation_id IN NUMBER) IS
        n_o_visits   NUMBER;
        final_cost   NUMBER;
        to_pay      number;
        discount     NUMBER;
    BEGIN
        SELECT
            COUNT_star
        INTO n_o_visits
        FROM
            clients
            JOIN client_reservation ON pesel_c = pesel
            JOIN reservations ON reservation_id = reservation_id_r
        WHERE
            status = completed;

        IF n_o_visits > 10
        THEN
            discount := 10;
        ELSE
            discount := 0;
        END IF;


        SELECT
            SUM_price_per_day
        INTO final_cost
        FROM
            rooms
            JOIN reservations ON room_id = room_id_r
        WHERE
            reservation_id_r = p_reservation_id;

        to_pay:=final_cost-final_cost*(discount/100);


END;
