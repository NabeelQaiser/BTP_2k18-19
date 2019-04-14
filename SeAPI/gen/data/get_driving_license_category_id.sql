CREATE OR REPLACE PROCEDURE get_driving_license_category_id(a_category IN VARCHAR,
                                      a_category_id OUT NUMBER)
IS
BEGIN
    DECLARE
        v_category_id NUMBER;
        CURSOR get_category_id IS
          SELECT id
          FROM   driving_license_category
          WHERE  category = a_category;
        CURSOR get_max_category_id IS
          SELECT MAX(id)
          FROM   driving_license_category;
    BEGIN
        OPEN get_category_id;
        FETCH get_category_id INTO v_category_id;
        CLOSE get_category_id;

        IF v_category_id IS NULL THEN
          OPEN get_max_category_id;
          FETCH get_max_category_id INTO v_category_id;
          CLOSE get_max_category_id;

          IF v_category_id IS NULL THEN
            v_category_id := 1;
          ELSE
            v_category_id := v_category_id + 1;
          END IF;

          INSERT INTO driving_license_category
                      (id,
                       category)
          VALUES      ( v_category_id,
                       a_category );
        END IF;

        a_category_id := v_category_id;
    END;
END;
