-- REQUIRES ADD_CAR PROCEDURE 
-- REQUIRES GET_COUNTRY_ID PROCEDURE 
-- REQUIRES GET_DRIVING_LICENSE_CATEGORY_ID PROCEDURE 
CREATE OR REPLACE PROCEDURE ADD_COURIER(A_PESEL                    IN NUMBER,
                                        A_NAME                     IN VARCHAR,
                                        A_SURNAME                  IN VARCHAR,
                                        A_STREET                   IN VARCHAR,
                                        A_HOUSE_NUMBER             IN NUMBER,
                                        A_APARTMENT_NUMBER         IN NUMBER,
                                        A_POSTAL_CODE              IN VARCHAR,
                                        A_CITY                     IN VARCHAR,
                                        A_PROVINCE                 IN VARCHAR,
                                        A_COUNTRY                  IN VARCHAR,
                                        A_PHONE_NUMBER             IN NUMBER,
                                        A_WAREHOUSE_ID             IN NUMBER,
                                        A_SALARY                   IN NUMBER,
                                        A_CONTRACT_TYPE               VARCHAR,
                                        A_DRIVING_LICENSE_CATEGORY IN VARCHAR,
  -- CAR -- NOTE EVERY COURIER HAS IT'S OWN CAR
                                        A_CAR_LICENSE_NUMBER       IN VARCHAR,
                                        A_BRAND                    IN VARCHAR,
                                        A_MODEL                    IN VARCHAR,
                                        A_TRUNK_CAPACITY           IN FLOAT,
                                        A_LOAD_CAPACITY            IN FLOAT,
                                        A_PRODUCTION_YEAR          IN NUMBER,
                                        A_SERVICING_VALID_THRU     IN DATE)
IS
  BEGIN
	ASSUME MAX_ID > 0 AND ID > 0 ;

    DECLARE
      V_COURIER_ID                  NUMBER;
      V_COUNTRY_ID                  NUMBER;
      V_DRIVING_LICENSE_CATEGORY_ID NUMBER;
      V_CONTRACT_TYPE_ID            NUMBER;
      V_CONTRACT_START              DATE;
      CURSOR GET_MAX_COURIER_ID IS
        SELECT MAX(ID)
        FROM COURIER;
    BEGIN
      OPEN GET_MAX_COURIER_ID;

      FETCH GET_MAX_COURIER_ID INTO V_COURIER_ID;

      CLOSE GET_MAX_COURIER_ID;

      IF V_COURIER_ID IS NULL
      THEN
        V_COURIER_ID := 1;
      ELSE
        V_COURIER_ID := V_COURIER_ID + 1;
      END IF;

      --GET_COUNTRY_ID(A_COUNTRY, V_COUNTRY_ID);

      --GET_DRIVING_LICENSE_CATEGORY_ID(A_DRIVING_LICENSE_CATEGORY, V_DRIVING_LICENSE_CATEGORY_ID);

      --GET_CONTRACT_TYPE_ID(A_CONTRACT_TYPE, V_CONTRACT_TYPE_ID);

      --ADD_CAR(A_CAR_LICENSE_NUMBER, A_BRAND, A_MODEL, A_TRUNK_CAPACITY, A_LOAD_CAPACITY, A_PRODUCTION_YEAR, A_SERVICING_VALID_THRU);

      V_CONTRACT_START := CURRENT_DATE();

      INSERT INTO COURIER
      (ID,
       PESEL,
       NAME,
       SURNAME,
       STREET,
       HOUSE_NUMBER,
       APARTMENT_NUMBER,
       POSTAL_CODE,
       CITY,
       PROVINCE,
       COUNTRY_ID,
       CAR_LICENSE_NUMBER,
       WAREHOUSE_ID,
       PHONE_NUMBER,
       SALARY,
       CONTRACT_TYPE,
       CONTRACT_START)
      VALUES (V_COURIER_ID,
        A_PESEL,
        A_NAME,
        A_SURNAME,
        A_STREET,
        A_HOUSE_NUMBER,
        A_APARTMENT_NUMBER,
        A_POSTAL_CODE,
        A_CITY,
        A_PROVINCE,
        V_COUNTRY_ID,
              A_CAR_LICENSE_NUMBER,
              A_WAREHOUSE_ID,
              A_PHONE_NUMBER,
              A_SALARY,
              V_CONTRACT_TYPE_ID,
              V_CONTRACT_START);

      INSERT INTO COURIER_DRIVING_LICENSE_CATEGORY
      (COURIER_ID,
       DRIVING_LICENSE_CATEGORY_ID)
      VALUES (V_COURIER_ID,
              V_DRIVING_LICENSE_CATEGORY_ID);
    END;
  ASSERT MAX_ID > 0 AND ID > 0 ;
	END;