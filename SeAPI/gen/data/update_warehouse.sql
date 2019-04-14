CREATE OR REPLACE PROCEDURE update_warehouse(a_parcel_id        IN NUMBER,
                                             a_old_warehouse_id IN VARCHAR,
                                             a_new_warehouse_id IN NUMBER)
IS
  BEGIN
    DECLARE
      v_time TIMESTAMP;
    BEGIN
      v_time := Current_date();

      UPDATE warehouse_parcel
      SET left_warehouse = v_time
      WHERE WAREHOUSE_ID = a_old_warehouse_id;
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
      END IF;
    END;
  END;
