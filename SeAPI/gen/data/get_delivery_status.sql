CREATE OR REPLACE PROCEDURE get_delivery_status(a_status    IN  VARCHAR,
                                                a_status_id OUT NUMBER)
IS
  BEGIN
    DECLARE
      v_status_id NUMBER;
      CURSOR get_status_id IS
        SELECT id
        FROM delivery_status
        WHERE status = a_status;
      CURSOR get_max_status_id IS
        SELECT max_id
        FROM delivery_status;
    BEGIN
      OPEN get_status_id;

      FETCH get_status_id INTO v_status_id;

      CLOSE get_status_id;

      IF v_status_id IS NULL
      THEN
        OPEN get_max_status_id;

        FETCH get_max_status_id INTO v_status_id;

        CLOSE get_max_status_id;

        IF v_status_id IS NULL
        THEN
          v_status_id := 1;
        ELSE
          v_status_id := v_status_id + 1;
        END IF;
      END IF;

      INSERT INTO delivery_status
      (id,
       status)
      VALUES (v_status_id,
              a_status);

      a_status_id := v_status_id;
    END;
  END;
