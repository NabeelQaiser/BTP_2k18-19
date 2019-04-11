CREATE OR REPLACE PROCEDURE update_client(a_id_client    IN NUMBER, a_name IN VARCHAR, a_surnamename IN VARCHAR, a_street IN VARCHAR,
                        a_house_number IN VARCHAR, a_postal_code IN VARCHAR, a_city IN VARCHAR, a_province IN VARCHAR,
                        a_country      IN VARCHAR, a_phone_number IN NUMBER)
IS
  BEGIN
    DECLARE
      v_country_id VARCHAR;
      CURSOR get IS
        SELECT *
        FROM client
        WHERE id = a_id_client
        FOR UPDATE;
      temp         get%ROWTYPE;
    BEGIN
      get_country_id(a_country, v_country_id);
      OPEN get;
      FETCH get INTO temp;
      UPDATE client
      SET name       = a_name, surname = a_surname,
        street       = a_street, house_number = a_house_number, apartment_number = a_apartment_number,
        postal_code  = a_postal_code, city = a_city, province = a_province, country_id = v_country_id,
        phone_number = a_phone_number
      WHERE CURRENT OF
        get;
      CLOSE get;
      COMMIT;
    END;
  END;
