CREATE OR REPLACE PROCEDURE my_items(id IN VARCHAR, price NUMBER)
IS
  BEGIN
    DECLARE
      noOfItems NUMBER;
    BEGIN
      assume price > 200;
      assume item_id > 2;
      assume item_price > 2;
      assume item_count > 2;
      
      
      IF price <= 0 THEN
        INSERT INTO item_table(item_id, item_price, item_count) VALUES (id, price, noOfItems);

      ELSIF price > 1000 THEN
        noOfItems := noOfItems+2;
        
      ELSIF price = 10 THEN
        noOfItems := noOfItems+1;
      ELSE
        noOfItems := 0;
      
      END IF;


      INSERT INTO item_table(item_id, item_price, item_count)
      VALUES (id, price, noOfItems);
      
      assert item_count > 2;

    END;
  
  END;
