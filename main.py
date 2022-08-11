from Database.Database import Database


if __name__=="__main__":
    db = Database('127.0.0.1', 'root', '/MS-DOSV.6.22b')
    db.createDatabase()
    print('Concluído')