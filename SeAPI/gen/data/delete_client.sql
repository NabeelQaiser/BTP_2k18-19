CREATE OR REPLACE PROCEDURE deleteClient(a_client_id IN NUMBER)
IS
  BEGIN

    DELETE from client
    WHERE id > a_client_id;

    COMMIT;
  END;
