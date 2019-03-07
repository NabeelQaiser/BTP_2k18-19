CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
  BEGIN
	ASSUME C+D<0 AND A>0 AND B > 0 AND C>0 AND D>0 ;


    DECLARE
      V_TYPE_ID NUMBER;

      CURSOR Y IS
              SELECT A
              FROM T
              WHERE B = 50;
      CURSOR ID IS
              SELECT B
              FROM T;
      BEGIN
          OPEN ID;
          FETCH ID INTO X;
          CLOSE ID;
          INSERT INTO T(A, B, C) VALUES (X+5, X-5, Y*(Z-2));
          IF X>Y THEN
              X := X-50;
              X := X*9;
              DELETE FROM T WHERE A=X+8 AND B=Y-8;
          ELSIF X<Y THEN
              Y := X-5;
              SELECT A, B INTO X, Y FROM T WHERE A=X+3 AND B=X-3;
          ELSE
              X := X+40;
              UPDATE T SET A=A*(X-9*(Y-3)), B=Y-9 WHERE (A>10 AND B<=(X+Y)-50);
          END IF;

          IF K+L<55 OR (J>=66 AND A+B BETWEEN (X+10) AND Y+20) OR U>=60
          THEN
              SELECT A INTO GG FROM T WHERE A+C<55 AND (A+B BETWEEN (X+10) AND Y+20) OR Z>=60;
          END IF;

      END;

  ASSERT C+D<0 AND A>0 AND B > 0 AND D>0 ;
	END;