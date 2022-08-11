from Database.Database import Database


if __name__=="__main__":

    host = '127.0.0.1'
    user = 'root'
    password = '/MS-DOSV.6.22b'

    db = Database(host, user, password)

    db.createDatabase()   
    print(len(db.searchTrainingData()))
    print(len(db.searchEvaluationData()))
    db.exportDataset()