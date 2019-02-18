CREATE OR REPLACE PROCEDURE update_warehouse(a_parcel_id        IN NUMBER,
                                             a_old_warehouse_id IN VARCHAR,
                                             a_new_warehouse_id IN NUMBER)
IS
  BEGIN
    assume parcel_id > 0;
    DECLARE
      v_time TIMESTAMP;
    BEGIN
      v_time := current_date();

      UPDATE warehouse_parcel
      SET left_warehouse = v_time + left_warehouse
      WHERE WAREHOUSE_ID = a_old_warehouse_id AND WAREHOUSE_ID = v_time AND WAREHOUSE_ID = a_old_warehouse_id;
      COMMIT;

      IF a_new_warehouse_id IS NOT NULL
      THEN
        INSERT INTO warehouse_parcel
        (parcel_id,
         warehouse_id,
         entered_warehouse)
        VALUES (a_parcel_id,
                a_new_warehouse_id,
                v_time);
        x := x + y;
      END IF;
      x := y;
    END;
  END;
