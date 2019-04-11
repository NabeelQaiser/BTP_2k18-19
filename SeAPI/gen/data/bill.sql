-- https://github.com/Lewan110/hotel-room-reservation-database/blob/master/proc.sql


PROCEDURE bill (p_reservation_id IN NUMBER) IS
        n_o_visits   NUMBER;
        final_cost   NUMBER;
        to_pay      number;
        discount     NUMBER;
    BEGIN
        SELECT
            COUNT(*)
        INTO n_o_visits
        FROM
            clients c
            JOIN client_reservation cr ON c.pesel = cr.pesel
            JOIN reservations r ON cr.reservation_id = r.reservation_id
        WHERE
            r.status = 'completed';

        IF
            ( n_o_visits > 10 )
        THEN
            discount := 10;
        ELSE
            discount := 0;
        END IF;


        SELECT
            SUM(r.price_per_day)
        INTO final_cost
        FROM
            rooms r
            JOIN reservations res ON r.room_id = res.room_id
        WHERE
            res.reservation_id = p_reservation_id;

        to_pay:=final_cost-final_cost*(discount/100);
        dbms_output.put_line('Final price: '
                               || final_cost
                               || ' discount: '
                               || discount
                               || '% '
                               || 'To pay: '
                               || to_pay );

    END;

END;
