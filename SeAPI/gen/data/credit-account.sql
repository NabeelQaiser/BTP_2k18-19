--https://www.bnl.gov/phobos/detectors/computing/orant/doc/database.804/a58227/ch14.htm

CREATE PROCEDURE credit_account (acct NUMBER, credit NUMBER) AS 
        old_balance  NUMBER; 
        new_balance  NUMBER; 
   BEGIN 
        SELECT balance INTO old_balance FROM accounts 
          WHERE acct_id = acct; 

        new_balance := old_balance + credit; 
        UPDATE accounts SET balance = new_balance 
          WHERE acct_id = acct; 
        COMMIT;
END credit_account
