import pymysql



def fetch(db, sql: str): 
    """
    fetch from db.

    Arguments:
        db
            hibiki_db = mysql.connector.connect(
                host = "127.0.0.1",
                user = "hibiki",
                passwd = "hi-bi-ki",
                database = "hibiki"
            )

        sql (str)
            SQL query with ';' at the end.

    Returns:
        err
            bool
        resule
            turple (err=False) or str (err=True)
    """
    try:
        db.connect()
        cursor.execute(sql)
        result = cursor.fetchall()
        err = False
    except:
        db.close()
        result = F"""Error: db "{db}" > {sql} > fetch failed."""
        err = True
        quit()

    return err, result

def update(db, sql: str):
    """
    update data.
    
    Arguments:
        db
            hibiki_db = mysql.connector.connect(
                host = "127.0.0.1",
                user = "hibiki",
                passwd = "hi-bi-ki",
                database = "hibiki"
            )

        sql (str)
            SQL query with ';' at the end.
    
    Returns:
        err
            bool
        resule
            "" (err=False) or str (err=True)
    """    
    try:
        db.connect()
        cursor.execute(sql)
        db.commit()
        result = ""
        err = False
    except:
        db.rollback()
        db.close()
        result = F"""Error: db "{db}" > {sql} > update failed."""
        err = True
        quit()

    return err, result
