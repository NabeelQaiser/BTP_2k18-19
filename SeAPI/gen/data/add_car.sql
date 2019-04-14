
-- Specification: NOT NULL Attributes "license_number, brand_id", Properties: id > 0, max(id) > 0, brand_id > 0

CREATE OR REPLACE PROCEDURE add_car(a_license_number       IN VARCHAR,
                                    a_brand                IN VARCHAR,
                                    a_model                IN VARCHAR,
                                    a_trunk_capacity       IN FLOAT,
                                    a_load_capacity        IN FLOAT,
                                    a_production_year      IN NUMBER,
                                    a_servicing_valid_thru IN DATE)
IS
  BEGIN
    DECLARE
      v_car_brand_id NUMBER;
      CURSOR get_car_brand_id IS
        SELECT id
        FROM car_brand
        WHERE brand = a_brand;
      CURSOR get_max_car_brand_id IS
        SELECT MAX(id)
        FROM car_brand;
    BEGIN
      OPEN get_car_brand_id;

      FETCH get_car_brand_id INTO v_car_brand_id;

      CLOSE get_car_brand_id;

      IF v_car_brand_id IS NULL
      THEN
        OPEN get_max_car_brand_id;

        FETCH get_max_car_brand_id INTO v_car_brand_id;

        CLOSE get_max_car_brand_id;

        IF v_car_brand_id IS NULL
        THEN
          v_car_brand_id := 1;
        ELSE
          v_car_brand_id := v_car_brand_id + 1;
        END IF;

        INSERT INTO car_brand
        (id,
         brand)
        VALUES (v_car_brand_id,
                a_brand);
      END IF;

      INSERT INTO car
      (license_number, brand_id, model, trunk_capacity, load_capacity, production_year, servicing_valid_thru)
      VALUES (a_license_number, v_car_brand_id, a_model,  a_trunk_capacity, a_load_capacity, a_production_year,  a_servicing_valid_thru);
    END;
  END;
