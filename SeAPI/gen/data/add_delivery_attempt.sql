CREATE OR REPLACE PROCEDURE add_delivery_attempt(a_parcel_id IN NUMBER,
												 a_courier_id IN NUMBER,
												 a_attempt_timestamp IN TIMESTAMP,
												 a_delivery_status IN VARCHAR)
IS
BEGIN

    DECLARE
         v_delivery_status_id NUMBER;
         CURSOR get_delivery_status_id IS
          SELECT id
          FROM   delivery_status
          WHERE  status = a_delivery_status;
    BEGIN
    	
        OPEN get_delivery_status_id;

         FETCH get_delivery_status_id INTO v_delivery_status_id;

         CLOSE get_delivery_status_id;

         IF v_delivery_status_id IS NULL THEN
		 v_delivery_status_id := a_delivery_status;
        END IF;

         INSERT INTO delivery_attempt
                    (parcel_id,
					courier_id,
					attempt_timestamp,
					delivery_status_id)
        VALUES      (a_parcel_id,
                     a_courier_id,
					 a_attempt_timestamp,
					 v_delivery_status_id);
    END;

END; 
