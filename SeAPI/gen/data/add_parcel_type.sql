CREATE OR REPLACE PROCEDURE add_parcel_type(a_type IN VARCHAR)
IS
  BEGIN
    DECLARE
      v_type_id NUMBER;
      CURSOR get_type_id IS
        SELECT id
        FROM parcel_type
        WHERE TYPE = a_type;
      CURSOR get_max_type_id IS
        SELECT MAX(id)
        FROM parcel_type;
    BEGIN
      OPEN get_type_id;

      FETCH get_type_id INTO v_type_id;

      CLOSE get_type_id;

      IF v_type_id IS NULL
      THEN
        OPEN get_max_type_id;

        FETCH get_max_type_id INTO v_type_id;

        CLOSE get_max_type_id;

        IF v_type_id IS NULL
        THEN
          v_type_id := 1;
        ELSE
          v_type_id := v_type_id + 1;
        END IF;
      END IF;

      INSERT INTO parcel_type
      (id,
       type)
      VALUES (v_type_id,
              a_type);
    END;
  END;