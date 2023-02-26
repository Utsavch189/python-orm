from oracle_config import ENGINE_PATH_WIN_AUTH
from sqlalchemy import *
from sqlalchemy.orm import declarative_base


ENGINE = create_engine(ENGINE_PATH_WIN_AUTH,echo=True)

Base=declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   
   id = Column(Integer, primary_key=True)
   name = Column(String)
   address=Column(String)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=ENGINE)
session = Session()

c1 = Customers(id=1,name = 'Utsav',address='Guptipara')

try:
    #session.add(c1)
    c=session.query(Customers).filter(Customers.address=='Guptipara').all()

    for i in c:
        print('\n',i.name ,'  ',i.address,'\n')
    session.commit()
except Exception as e:
    print(e)