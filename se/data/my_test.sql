CREATE OR REPLACE PROCEDURE my_item(id NUMBER, amount FLOAT)
IS
  BEGIN
      DECLARE
          price FLOAT;
      BEGIN
          SELECT t_price INTO price FROM oldtable
                                        WHERE t_id = id;
          IF amount >= 200 AND price > 5000 THEN
              price := price - 0.2*amount;
          ELSE
              price := price + 0.05*amount;
          END IF;
          INSERT INTO newtable(t_id, t_price, t_amount)
                          VALUES (id, price, amount);
      END;
  END;