 CREATE OR REPLACE PROCEDURE Proc_Budget_Adjust (Department_Id int, Avail_Amt int) 
 IS 
 	Proposed_Amt int;
 	Extra int;
 	Decrs int;
 	No_Attr int;
 	
 	BEGIN
 	--assume Manpower > 0 and Contingency > 0 and Proposed_Amt > 0 and Avail_Amt > 0;
 		No_Attr := 4;
 		
 		
 		SELECT Total_Amt INTO Proposed_Amt
		FROM Budget_Tab WHERE Dept_ID = Department_Id;
 		IF Proposed_Amt >= Avail_Amt THEN
   			Extra := Proposed_Amt - Avail_Amt;
  			Decrs := Extra/No_Attr;
  		UPDATE Budget_Tab SET Manpower = Manpower - Decrs, Equipment = Equipment - Decrs, Contingency = Contingency - Decrs, Consumable = Consumable - Decrs
 		WHERE Dept_ID = Department_Id;
 		END IF;
 	--assert Manpower > 0 and Contingency > 0;
 END;
