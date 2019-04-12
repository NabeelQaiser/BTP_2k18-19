-- requires add_car procedure 
-- requires get_country_id procedure 
-- requires get_driving_license_category_id procedure 
CREATE OR REPLACE PROCEDURE add_courier(a_pesel                    IN NUMBER,
                                        a_name                     IN VARCHAR,
                                        a_surname                  IN VARCHAR,
                                        a_street                   IN VARCHAR,
                                        a_house_number             IN NUMBER,
                                        a_apartment_number         IN NUMBER,
                                        a_postal_code              IN VARCHAR,
                                        a_city                     IN VARCHAR,
                                        a_province                 IN VARCHAR,
                                        a_country                  IN VARCHAR,
                                        a_phone_number             IN NUMBER,
                                        a_warehouse_id             IN NUMBER,
                                        a_salary                   IN NUMBER,
                                        a_contract_type               VARCHAR,
                                        a_driving_license_category IN VARCHAR,
  -- car -- note every courier has it's own car
                                        a_car_license_number       IN VARCHAR,
                                        a_brand                    IN VARCHAR,
                                        a_model                    IN VARCHAR,
                                        a_trunk_capacity           IN FLOAT,
                                        a_load_capacity            IN FLOAT,
                                        a_production_year          IN NUMBER,
                                        a_servicing_valid_thru     IN DATE)
IS
  BEGIN
    DECLARE
      v_courier_id                  NUMBER;
      v_country_id                  NUMBER;
      v_driving_license_category_id NUMBER;
      v_contract_type_id            NUMBER;
      v_contract_start              DATE;
      CURSOR get_max_courier_id IS
        SELECT Max(id)
        FROM courier;
    BEGIN
      OPEN get_max_courier_id;

      FETCH get_max_courier_id INTO v_courier_id;

      CLOSE get_max_courier_id;

      IF v_courier_id IS NULL
      THEN
        v_courier_id := 1;
      ELSE
        v_courier_id := v_courier_id + 1;
      END IF;

      --get_country_id(a_country, v_country_id);

      --get_driving_license_category_id(a_driving_license_category, v_driving_license_category_id);

      --get_contract_type_id(a_contract_type, v_contract_type_id);

      --add_car(a_car_license_number, a_brand, a_model, a_trunk_capacity, a_load_capacity, a_production_year, a_servicing_valid_thru);

      v_contract_start := Current_date();

      INSERT INTO courier
      (id,
       pesel,
       name,
       surname,
       street,
       house_number,
       apartment_number,
       postal_code,
       city,
       province,
       country_id,
       car_license_number,
       warehouse_id,
       phone_number,
       salary,
       contract_type,
       contract_start)
      VALUES (v_courier_id,
        a_pesel,
        a_name,
        a_surname,
        a_street,
        a_house_number,
        a_apartment_number,
        a_postal_code,
        a_city,
        a_province,
        v_country_id,
              a_car_license_number,
              a_warehouse_id,
              a_phone_number,
              a_salary,
              v_contract_type_id,
              v_contract_start);

      INSERT INTO courier_driving_license_category
      (courier_id,
       driving_license_category_id)
      VALUES (v_courier_id,
              v_driving_license_category_id);
    END;
  END;
