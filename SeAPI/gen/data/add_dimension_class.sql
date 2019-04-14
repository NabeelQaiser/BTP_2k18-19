CREATE OR REPLACE PROCEDURE add_dimension_class(a_class IN VARCHAR)
IS
  BEGIN
    DECLARE
      v_class_id NUMBER;
      CURSOR get_class_id IS
        SELECT id
        FROM dimension_class
        WHERE class = a_class;
      CURSOR get_max_class_id IS
        SELECT MAX(id)
        FROM dimension_class;
    BEGIN
      OPEN get_class_id;

      FETCH get_class_id INTO v_class_id;

      CLOSE get_class_id;

      IF v_class_id IS NULL
      THEN
        OPEN get_max_class_id;
        FETCH get_max_class_id INTO v_class_id;
        CLOSE get_max_class_id;

        IF v_class_id IS NULL
        THEN
          v_class_id := 1;
        ELSE
          v_class_id := v_class_id + 1;
        END IF;

        INSERT INTO dimension_class
        (id, class)
        VALUES (v_class_id,
                a_class);
      END IF;
    END;
  END;