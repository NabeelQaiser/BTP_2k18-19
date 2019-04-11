 PROCEDURE debit_account (acct  NUMBER, debit NUMBER) IS 

 

        old_balance         NUMBER; 
        new_balance         NUMBER; 
        insufficient_funds  EXCEPTION; 

  BEGIN 

        SELECT balance INTO old_balance FROM accounts 
          WHERE acct_id = acct 
          FOR UPDATE OF balance; 
          
        new_balance := old_balance - debit; 
        IF new_balance >= minimum_balance  THEN 
          UPDATE accounts SET balance = new_balance 

            WHERE acct_id = acct; 
        ELSE 
          RAISE insufficient_funds; 
        END IF; 
       
       

  EXCEPTION 
        WHEN NO_DATA_FOUND THEN 
          new_status := 'Nonexistent account'; 
        WHEN insufficient_funds THEN 
          new_status := 'Insufficient funds';  
        WHEN OTHERS THEN  /* Returns other errors to application */  
          new_status := 'Error: ' || SQLERRM(SQLCODE);  
 
  END debit_account; 
