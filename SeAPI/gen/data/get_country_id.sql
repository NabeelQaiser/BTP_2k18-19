CREATE OR REPLACE PROCEDURE get_country_id(a_country    IN  VARCHAR,
                                           a_country_id OUT NUMBER)
IS
  BEGIN
    DECLARE
      v_country_id NUMBER;
      CURSOR get_country_id IS
        SELECT id
        FROM country
        WHERE country = a_country;
      CURSOR get_max_country_id IS
        SELECT MAX(id)
        FROM country;
    BEGIN
      OPEN get_country_id;
      FETCH get_country_id INTO v_country_id;
      CLOSE get_country_id;

      IF v_country_id IS NULL
      THEN
        OPEN get_max_country_id;
        FETCH get_max_country_id INTO v_country_id;
        CLOSE get_max_country_id;

        IF v_country_id IS NULL
        THEN
          v_country_id := 1;
        ELSE
          v_country_id := v_country_id + 1;
        END IF;

        INSERT INTO country
        (id,
         country)
        VALUES (v_country_id,
                a_country);
      END IF;

      a_country_id := v_country_id;
    END;
  END;
