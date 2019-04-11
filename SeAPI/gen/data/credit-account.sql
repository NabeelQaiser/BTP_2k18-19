

CREATE PROCEDURE credit_account (acct NUMBER, credit NUMBER) AS 


        old_balance  NUMBER; 
        new_balance  NUMBER; 
   BEGIN 
        SELECT balance INTO old_balance FROM accounts 
          WHERE acct_id = acct 
          FOR UPDATE OF balance; 

        new_balance := old_balance + credit; 
        UPDATE accounts SET balance = new_balance 
          WHERE acct_id = acct; 
        COMMIT; 

        EXCEPTION 
          WHEN NO_DATA_FOUND THEN 
            INSERT INTO accounts (acct_id, balance) 
                VALUES(acct, credit); 
          WHEN OTHERS THEN 
        ROLLBACK; 
END credit_account
