 PROCEDURE debit_account (acct  NUMBER, debit NUMBER) IS
        old_balance         NUMBER; 
        new_balance         NUMBER; 
        insufficient_funds  EXCEPTION; 

  BEGIN 
  	--assume minimum_balance > 1000 and balance  >= minimum_balance;
        SELECT balance INTO old_balance FROM accounts 
          WHERE acct_id = acct; 
          
        new_balance := old_balance - debit; 
        IF new_balance >= minimum_balance  THEN 
          UPDATE accounts SET balance = new_balance WHERE acct_id = acct;
        END IF; 
        
 
  END debit_account; 
