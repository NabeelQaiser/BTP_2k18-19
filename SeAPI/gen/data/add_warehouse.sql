CREATE OR REPLACE PROCEDURE add_warehouse(a_street           IN VARCHAR,
                                          a_house_number     IN NUMBER,
                                          a_apartment_number IN NUMBER,
                                          a_postal_code      IN VARCHAR,
                                          a_city             IN VARCHAR,
                                          a_province         IN VARCHAR,
                                          a_country          IN VARCHAR,
                                          a_area             IN FLOAT)
IS
  BEGIN
 
    DECLARE
       v_warehouse_id NUMBER;
       v_country_id   NUMBER;
       CURSOR get_max_warehouse_id IS
        SELECT max_id
        FROM warehouse;
    BEGIN
       v_country_id := a_country ;

       OPEN get_max_warehouse_id;
       FETCH get_max_warehouse_id INTO v_warehouse_id;
       CLOSE get_max_warehouse_id;

       IF v_warehouse_id IS NULL
      THEN
         v_warehouse_id := 1;
       ELSE
         v_warehouse_id := v_warehouse_id + 1;
      END IF;

       INSERT INTO warehouse  (id,  street,  house_number, apartment_number, postal_code,  city, province, country_id, area)
      VALUES (v_warehouse_id,
              a_street,
              a_house_number,
              a_apartment_number,
              a_postal_code,
              a_city,
              a_province,
              v_country_id,
              a_area);
    END;
  END;
