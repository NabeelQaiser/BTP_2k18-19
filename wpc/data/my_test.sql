CREATE OR REPLACE PROCEDURE my_item(id IN VARCHAR, num_item NUMBER)
IS
  BEGIN
    DECLARE
      price NUMBER;
    BEGIN
      SELECT item_price INTO price FROM item_table WHERE item_id = id;
      IF num_item >= 1000 THEN
        price := price - 0.1*num_item;

      ELSIF num_item >= 500 THEN
        price := price - 0.2*num_item;
        
      ELSIF num_item > 99 AND price > 5000 THEN
        price := price - 0.2*num_item;
      ELSE
        price := price + 0.05*num_item;
      
      END IF;


      INSERT INTO item_table(item_id, item_price, item_count)
      VALUES (id, price, num_item);

    END;
  
  END;