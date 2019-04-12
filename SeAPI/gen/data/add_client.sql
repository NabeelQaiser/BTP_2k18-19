-- requires get_country_id procedure
CREATE OR REPLACE PROCEDURE add_client(a_name             IN VARCHAR,
                                       a_surname          IN VARCHAR,
                                       a_street           IN VARCHAR,
                                       a_house_number     IN NUMBER,
                                       a_apartment_number IN NUMBER,
                                       a_postal_code      IN VARCHAR,
                                       a_city             IN VARCHAR,
                                       a_province         IN VARCHAR,
                                       a_country          IN VARCHAR,
                                       a_phone_number     IN NUMBER)
IS
  BEGIN
    DECLARE
      v_country_id NUMBER;
      v_client_id  NUMBER;
      CURSOR get_max_client_id IS
        SELECT MAX(id)
        FROM client;
    BEGIN
      OPEN get_max_client_id;
      FETCH get_max_client_id INTO v_client_id;
      CLOSE get_max_client_id;

      IF v_client_id IS NULL
      THEN
        v_client_id := 1;
      ELSE
        v_client_id := v_client_id + 1;
      END IF;

      --get_country_id(a_country, v_country_id);
      NOTHING := -1;

      INSERT INTO client
      (id,
       name,
       surname,
       street,
       house_number,
       apartment_number,
       postal_code,
       city,
       province,
       country_id,
       phone_number)
      VALUES (v_client_id,
        a_name,
        a_surname,
        a_street,
        a_house_number,
        a_apartment_number,
        a_postal_code,
        a_city,
        a_province,
        v_country_id,
        a_phone_number);
    END;
  END;
