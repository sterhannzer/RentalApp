from Store import Store
from dataBase import Base, engine, Session

Base.metadata.create_all(engine)

session = Session()


store = Store('Robotnicza 10B')

session.add(store)
session.commit()
session.close()