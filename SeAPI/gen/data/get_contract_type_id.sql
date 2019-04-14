CREATE OR REPLACE PROCEDURE get_contract_type_id(a_contract_type    IN  VARCHAR,
                                                 a_contract_type_id OUT NUMBER)
IS
  BEGIN
    DECLARE
      v_contract_type_id NUMBER;
      CURSOR get_contract_type_id IS
        SELECT id
        FROM contract_type
        WHERE TYPE = a_contract_type;
      CURSOR get_max_contract_type_id IS
        SELECT MAX(id)
        FROM contract_type;
    BEGIN
      OPEN get_contract_type_id;
      FETCH get_contract_type_id INTO v_contract_type_id;
      CLOSE get_contract_type_id;

      IF v_contract_type_id IS NULL
      THEN
        OPEN get_max_contract_type_id;
        FETCH get_max_contract_type_id INTO v_contract_type_id;
        CLOSE get_max_contract_type_id;

        IF v_contract_type_id IS NULL
        THEN
          v_contract_type_id := 1;
        ELSE
          v_contract_type_id := v_contract_type_id + 1;
        END IF;

        INSERT INTO contract_type
        (id,
         type)
        VALUES (v_contract_type_id,
                a_contract_type);
      END IF;

      a_contract_type_id := v_contract_type_id;
    END;
  END;
