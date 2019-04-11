
// Source : https://github.com/Esentrobn/SQL-University-DB

CREATE PROCEDURE remainingSeats (crs IN integer) AS 
seats pls_integer;
taken pls_integer;
result integer;
BEGIN
SELECT DISTINCT C.csize INTO seats FROM Course C WHERE C.cid = crs;
SELECT COUNT(R.cid) INTO taken FROM Registers R WHERE R.cid = crs;
result:=seats-taken;
DBMS_OUTPUT.PUT_LINE('Remaining Seats = ' || result);
END;
.
Run

Exec remainingSeats(1);

Exec remainingSeats(5);

Exec remainingSeats(8);



CREATE OR REPLACE PROCEDURE STUDENT_COURSE_SEARCH(SPID IN 
INTEGER, SCID IN INTEGER)
AS
PFNAME CHAR(26);
PLNAME CHAR(26);
PGRADE CHAR(1);
PSEM CHAR(6);
PYR INTEGER;
CURSOR STUS
IS 
SELECT PP.FNAME, PP.LNAME, FG.GRADE, FG.SEM, FG.YR
FROM PERSON PP, STUDENT S, FINALGRADE FG
WHERE PP.PID = S.PID AND
S.PID = FG.PID AND
PP.PID = SPID  AND
FG.CID = SCID;
BEGIN
DBMS_OUTPUT.PUT_LINE('FNAME                      LNAME                      G SEM    YR  ');
DBMS_OUTPUT.PUT_LINE('-------------------------- -------------------------- - ------ ----');
OPEN STUS;
LOOP
FETCH STUS INTO PFNAME, PLNAME, PGRADE, PSEM, PYR;
IF (PFNAME IS NULL)
THEN 
DBMS_OUTPUT.PUT_LINE('Student has not taken this course!');
END IF;
IF STUS%NOTFOUND
THEN 
EXIT;
END IF;
DBMS_OUTPUT.PUT_LINE(PFNAME || ' ' || PLNAME || ' ' || PGRADE || ' ' || PSEM || ' ' || PYR);
END LOOP;
CLOSE STUS;
END;


Exec STUDENT_COURSE_SEARCH(0, 0);

Exec STUDENT_COURSE_SEARCH(1, 1);

Exec STUDENT_COURSE_SEARCH(29, 8);


CREATE OR REPLACE PROCEDURE STUDENT_TRANSCRIPT(SPID IN INTEGER)
AS
FGCID INTEGER;
FGTITLE CHAR(26);
FGSEM CHAR(6);
FGYR INTEGER;
FGGRADE CHAR(1);
CURSOR GRADES
IS 
SELECT C.CID, C.TITLE, FG.SEM, FG.YR, FG.GRADE
FROM COURSE C, FINALGRADE FG
WHERE FG.CID = C.CID AND
FG.SEM = C.SEM AND
FG.YR = C.YR AND
FG.PID = SPID AND
FG.YR > ((SELECT MIN(FG.YR)
FROM FINALGRADE FG)-1)
ORDER BY FG.YR;
BEGIN
DBMS_OUTPUT.PUT_LINE('CID TITLE                      SEM    YR   G');
DBMS_OUTPUT.PUT_LINE('--- -------------------------- ------ ---- -');
OPEN GRADES;
LOOP
FETCH GRADES INTO FGCID, FGTITLE, FGSEM, FGYR, FGGRADE;
IF (FGCID IS NULL)
THEN 
DBMS_OUTPUT.PUT_LINE('Student has not taken any courses!');
END IF;
IF GRADES%NOTFOUND
THEN 
EXIT;
END IF;
DBMS_OUTPUT.PUT_LINE('00' || FGCID || ' ' || FGTITLE || ' ' || FGSEM || ' ' || FGYR || ' ' || FGGRADE);
END LOOP;
CLOSE GRADES;
END;

Exec STUDENT_TRANSCRIPT(1);

Exec STUDENT_TRANSCRIPT(20);

Exec STUDENT_TRANSCRIPT(27);


CREATE PROCEDURE teachesCourses(pr IN integer)
AS
courseID integer;
courseName char(26);
CURSOR teach 
IS
SELECT DISTINCT C.cid, C.title 
FROM Course C, Person P, Teaches T 
WHERE P.pid = pr 
AND P.pid = T.pid 
AND T.cid = C.cid;
BEGIN
DBMS_OUTPUT.PUT_LINE('CID TITLE');
DBMS_OUTPUT.PUT_LINE('--- --------------------------');
OPEN teach;
LOOP
FETCH teach INTO courseID, courseName;
IF teach%NOTFOUND THEN EXIT; END IF;
DBMS_OUTPUT.PUT_LINE(courseID || '   ' || courseName);
END LOOP;
CLOSE teach;
END;
.
run

Exec teachesCourses(9);

Exec teachesCourses(18);

Exec teachesCourses(24);

CREATE PROCEDURE studentRecords (s IN integer, y IN integer) AS 
courseID integer;
sGrade char(1);
sSemester char(10);
sYr integer;
CURSOR records IS SELECT F.cid, F.grade, F.sem, F.yr FROM FinalGrade F WHERE 
F.pid = s AND F.yr = y;
BEGIN
DBMS_OUTPUT.PUT_LINE('CID G SEM        YR');
DBMS_OUTPUT.PUT_LINE('--- - ------     ----');
OPEN records;
LOOP
FETCH records INTO courseID, sGrade, sSemester, sYr;
IF records%NOTFOUND THEN EXIT; END IF;
DBMS_OUTPUT.PUT_LINE(courseID ||'   '|| sGrade ||' '|| sSemester ||' '||	sYr);
END LOOP;
CLOSE records;
END;
.
run

Exec studentRecords(1, 2017);

Exec studentRecords(3, 2016);

Exec studentRecords(19, 2015);

Exec studentRecords(19, 2014);


CREATE OR REPLACE PROCEDURE SEMESTER_GRADES(SPID IN INTEGER, SYR IN INTEGER, SSEM IN CHAR)
AS
FGCID INTEGER;
FGTITLE CHAR(26);
FGGRADE CHAR(1);
CURSOR GRADES
IS 
SELECT C.CID, C.TITLE, FG.GRADE
FROM COURSE C, FINALGRADE FG
WHERE FG.CID = C.CID AND
	  FG.SEM = C.SEM AND
	  FG.YR = C.YR AND
	  FG.PID = SPID AND
	  FG.YR = SYR AND
	  FG.SEM = SSEM;
BEGIN
DBMS_OUTPUT.PUT_LINE('CID TITLE                      SEM    YR   G');
DBMS_OUTPUT.PUT_LINE('--- -------------------------- ------ ---- -');
OPEN GRADES;
LOOP
	FETCH GRADES INTO FGCID, FGTITLE, FGGRADE;
	IF (FGCID IS NULL)
	THEN 
	DBMS_OUTPUT.PUT_LINE('Student did not take any courses this semester!');
	END IF;
	IF GRADES%NOTFOUND
	THEN 
	EXIT;
	END IF;
	DBMS_OUTPUT.PUT_LINE('00' || FGCID || ' ' || FGTITLE || ' ' || SSEM || ' ' || SYR || ' ' || FGGRADE);
END LOOP;
CLOSE GRADES;
END;
/

exec semester_grades(1,2017,'Spring');

exec semester_grades(3,2016,'Fall');

exec semester_grades(3,2015,'Fall');

CREATE OR REPLACE PROCEDURE createcourse(

	   CourseId IN COURSE.CID%TYPE,
	   CourseDays IN COURSE.CDAYS%TYPE ,
	   Coursetitle IN COURSE.TITLE%TYPE,
	   Coursesize IN COURSE.CSIZE%TYPE,
               CourseFinal IN COURSE.FINALEXAM%TYPE,
	   CouseSem IN COURSE.SEM%TYPE,
	   CouseYr IN COURSE.YR%TYPE)
  IS
  BEGIN

  INSERT INTO COURSE ("CID", "CDAYS", "TITLE", "CSIZE", "FINALEXAM", "SEM", "YR")
  VALUES (CourseId, CourseDays,Coursetitle, Coursesize,CourseFinal,CouseSem,CouseYr);

  COMMIT;

  EXCEPTION
		WHEN NO_DATA_FOUND THEN
                       NULL;
		WHEN OTHERS THEN
			NULL;
      
END;

BEGIN

   createcourse(10,'MWF','SQL DB IN ORACLE',25,to_date('5/2/2017', 'MM/DD/YYYY'),'SPRING',2017);

   createcourse(11,'MTW','NOSQL WITH MONGODB',25,to_date('12/19/2017', 'MM/DD/YYYY'),'FALL',2017);
       
 END;


create or replace PROCEDURE UpdateCourse
 (
  COURSEID IN integer,
  COURSEDAYS  IN char,
  COURSETITLE IN char,
  COURSESIZE IN CHAR,
  COURSEFINALEXAM IN VARCHAR2,
  COURSESEM IN char,
  COURSEYEAR IN char
  )

    AS
  BEGIN
      UPDATE COURSE C
        SET C.CDAYS = COURSEDAYS,
            C.TITLE = COURSETITLE,
            C.CSIZE = COURSESIZE,
            C.FINALEXAM = COURSEFINALEXAM,
            C.SEM = COURSESEM,
            C.YR = COURSEYEAR
            
      WHERE COURSEID = C.CID;
      
      END;

EXEC UPDATECOURSE(11,'MWTHF','NOSQL DB WITH MONGO',35,to_date('12/15/2018', 'MM/DD/YYYY'),'FALL',2018);


            /*  ADD AN ORGANIZATION */
set SERVEROUTPUT ON;
 
CREATE OR REPLACE PROCEDURE ADDORG
(
            ORG_ID IN ORGANIZATIONS.ORID%TYPE,
 	ORG_NAME IN ORGANIZATIONS.ONAME%TYPE
 )
            	  
            	  
IS
BEGIN

  INSERT INTO ORGANIZATIONS ("ORID", "ONAME")
  VALUES (ORG_ID, ORG_NAME);
 
  COMMIT;
 
                            	EXCEPTION
                            	WHEN NO_DATA_FOUND THEN
                                            	NULL;
                            	WHEN OTHERS THEN
                                            	NULL;
 
END;


Exec ADDORG(9,'DIGITAL CARE');

 /* ADD A NEW STUDENT */


CREATE OR REPLACE PROCEDURE ADDSTUDENT
(
	   STUDID IN PERSON.PID%TYPE,
	   STUDFNAME IN PERSON.FNAME %TYPE ,
	   STUDLNAME IN PERSON.LNAME%TYPE,
               STUDPID IN STUDENT.PID%TYPE,
               STUDMAJOR IN STUDENT.MAJOR%TYPE,
	   STUDEMAIL IN STUDENT.EMAIL%TYPE)
     
	   
	   
IS
BEGIN

  INSERT INTO PERSON ("PID", "FNAME", "LNAME")
  VALUES (STUDID,STUDFNAME,STUDLNAME);
  
  INSERT INTO STUDENT ("PID", "MAJOR", "EMAIL" )
  VALUES ( STUDPID, STUDMAJOR,STUDEMAIL);
  COMMIT;

  EXCEPTION
		WHEN NO_DATA_FOUND THEN
			NULL;
		WHEN OTHERS THEN
			NULL;

END;


BEGIN
  ADDSTUDENT(37,'NELSON','KANYE',37,'DATAANALYTICS','KNELSON@STCLOUDSTATE.EDU');
  ADDSTUDENT(73,'ZACKERY','GATES',73,'DATAANALYTICS','ZGATES@STCLOUDSTATE.EDU');

END;


CREATE OR REPLACE PROCEDURE removecourse
          (
          coursId IN course.cid%TYPE,
          coursename in course.title%TYPE
          )
          IS
            BEGIN

              DELETE course where cid = coursId and
                       title = coursename ;
                
           COMMIT;
           
            EXCEPTION
		          WHEN NO_DATA_FOUND THEN
			          NULL;
		          WHEN OTHERS THEN
		             	NULL;

          END;

BEGIN

   REMOVECOURSE(10,'SQL DB IN ORACLE');
   REMOVECOURSE(11,'NOSQL DB WITH MONGO');

END;



