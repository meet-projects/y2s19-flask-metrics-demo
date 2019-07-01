from sqlalchemy import create_engine, MetaData, inspect, Table
from sqlalchemy.orm import sessionmaker
from database import *

if __name__ == '__main__':
    # LOCAL

    metadata = MetaData(engine)
    table = Table('metrics', metadata, autoload=True)
    table_to_print = session.query(table).all()

    metrics = {}

    for row in table_to_print:
        if (row[1],row[2]) in metrics:
            metrics[(row[1],row[2])] += 1
        else:
            metrics[(row[1],row[2])] = 1

    print(metrics)            
