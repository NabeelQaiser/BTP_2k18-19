CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR, Y IN VARCHAR)
IS
BEGIN
  A int;
  B varchar;
  CURSOR get_type_id IS
        SELECT A
        FROM T
        WHERE B = 50;
  CURSOR get_max_type_id IS
        SELECT B
        FROM T;

  BEGIN
      OPEN hello;

      FETCH hello INTO B;

      CLOSE hello;

      UPDATE T SET A=A*(X-9*(Y-3)), B=Y-9 WHERE NOT A>10 AND B<=(X+Y)-50;
      ASSERT A>0;
  END;
END;
