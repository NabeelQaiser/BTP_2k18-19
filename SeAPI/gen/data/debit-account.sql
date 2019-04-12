 PROCEDURE debit_account (acct  NUMBER, debit NUMBER) IS 

 

        old_balance         NUMBER; 
        new_balance         NUMBER; 
        insufficient_funds  EXCEPTION; 

  BEGIN 
  	--assume minimum_balance > 1000 and balance  >= minimum_balance;
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
       
       
 --assert balance  >= minimum_balance ;
  EXCEPTION 
        WHEN NO_DATA_FOUND THEN 
          new_status := 'Nonexistent account'; 
        WHEN insufficient_funds THEN 
          new_status := 'Insufficient funds';  
        WHEN OTHERS THEN  /* Returns other errors to application */  
          new_status := 'Error: ' || SQLERRM(SQLCODE);  
 
  END debit_account; 
