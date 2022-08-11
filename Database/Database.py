import pymysql

class Database(object):
    def __init__(self, host, user, password):
        self.dbConnection = pymysql.connect(
            host = host,
            user = user,
            password = password,
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor
        )
    
    def createDatabase(self):
        try:
            with self.dbConnection.cursor() as db:
                db.execute('CREATE DATABASE AG002')
                self.dbConnection.commit()

                db.execute('USE AG002')
                self.dbConnection.commit()

                sql = '''CREATE TABLE Credit (
                            Id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            Laufkont INT,
                            Llaufzeit INT,
                            Moral INT,
                            Verw INT,
                            Hoehe INT,
                            Sparkont INT,
                            Beszeit INT,
                            Rate INT,
                            Famges INT,
                            Buerge INT,
                            Wohnzeit INT,
                            Verm INT,
                            `Alter` INT,
                            Weitkred INT,
                            Wohn INT,
                            Bishkred INT,
                            Beruf INT,
                            Pers INT,
                            Telef INT,
                            Gastarb INT,
                            Kredit INT
                        );'''

                db.execute(sql)
                self.dbConnection.commit()
                
        except self.dbConnection.Error as ex:
            print(ex)
            pass
