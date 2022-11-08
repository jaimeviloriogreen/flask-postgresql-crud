from psycopg2 import extras

class ModelUser:
    conn = None
    cursor = None

    @classmethod
    def getUsers(self, conn):
        try:
            cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()

            return results
        except Exception as error:
             print(f"Error: {error}")
        finally:
            if conn is not None:
                conn.close()
            if cursor is not None:
                cursor.close()
    @classmethod
    def getUser(self, conn, id):
        try:
            cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
            cursor.execute("SELECT fullname, username FROM users WHERE id = %s", (id, ))
            results = cursor.fetchone()
            return results
        except Exception as error:
             print(f"Error: {error}")
        finally:
            if conn is not None:
                conn.close()
            if cursor is not None:
                cursor.close()
                            
    @classmethod
    def deleteUser(self, conn, id):
        try:
            cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
            sql = """DELETE FROM users WHERE id = %s RETURNING *"""
            cursor.execute(sql, (id,))
            
            conn.commit()
            result = cursor.fetchone()
            
            return result
        except Exception as error:
             print(f"Error: {error}")
        finally:
            if conn is not None:
                conn.close()
            if cursor is not None:
                cursor.close()
                
    @classmethod
    def addUser(self, conn, user):
        try:
            print(user)
            cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
            sql = """
            INSERT INTO 
                users(fullname, username, password)
            VALUES
                (%s, %s, %s)
            """
            value = (user.fullname, user.username, user.password)

            cursor.execute(sql, value)
            result = cursor.rowcount
            conn.commit()
            
            return result
        except Exception as error:
             print(f"Error: {error}")
        finally:
            if conn is not None:
                conn.close()
            if cursor is not None:
                cursor.close()
                
    