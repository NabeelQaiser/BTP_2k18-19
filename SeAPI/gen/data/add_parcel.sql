CREATE OR REPLACE PROCEDURE add_parcel(a_sender_id IN NUMBER,
  a_receiver_id IN NUMBER,
  a_weight IN FLOAT,
  a_height IN FLOAT,
  a_width IN FLOAT,
  a_depth IN FLOAT,
  a_dimension_class_id IN NUMBER,
  a_parcel_type_id IN NUMBER,
  a_status_id IN NUMBER,
  a_current_warehouse_id IN NUMBER,
  a_worth IN NUMBER,
  a_is_cod IN NUMBER,
  a_is_insured IN NUMBER)
IS
BEGIN
 
    DECLARE
         v_parcel_id NUMBER;
         v_entered_timestamp TIMESTAMP;
         CURSOR get_parcel_id IS
          SELECT max_id
          FROM   parcel;
    BEGIN

         OPEN get_parcel_id;
         FETCH get_parcel_id INTO v_parcel_id;
         CLOSE get_parcel_id;

         IF v_parcel_id IS NULL 
         THEN
           v_parcel_id := 1;
         ELSE
           v_parcel_id := v_parcel_id + 1;
        END IF;
        
         v_entered_timestamp := current_date;

         INSERT INTO parcel
                    (id, sender_id,  receiver_id,   weight,  height,  width,  depth1,  dimension_class_id,  parcel_type_id,  status_id,
                    current_warehouse_id,  worth,  is_cod,  is_insured)
        VALUES      (v_parcel_id,                    a_sender_id,
                    a_receiver_id,                    a_weight,
                    a_height,                    a_width,
                    a_depth,                    a_dimension_class_id,
                    a_parcel_type_id,                    a_status_id,
                    a_current_warehouse_id,                    a_worth,
                    a_is_cod,                    a_is_insured);
                    
          
         INSERT INTO warehouse_parcel
                    (parcel_id,
                    warehouse_id,
                    entered_warehouse)
        VALUES      (v_parcel_id,
                    a_current_warehouse_id,
                    v_entered_timestamp);          
    END;
END; 
