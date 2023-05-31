from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = "hanchang"
password = "3edc#EDC"
hostname = "test0527.database.windows.net"
port = 1433
database = "test0527"

# Define the database URL
DATABASE_URL = f"mssql+pyodbc://{username}:{password}@{hostname}:{port}/{database}?driver=ODBC+Driver+18+for+SQL+Server"

# Create the engine and base
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the CalculationHistory table
class CalculationHistory(Base):
    __tablename__ = "calculation_history"

    id = Column(Integer, primary_key=True)
    num1 = Column(Integer)
    num2 = Column(Integer)

    def __repr__(self):
        return f"<CalculationHistory(id={self.id}, num1={self.num1}, num2={self.num2})>"

# Create the table
Base.metadata.create_all(engine)

# Create a session factory and a session
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

# Insert data into the table
new_calculation = CalculationHistory(num1=5, num2=10)
session.add(new_calculation)
session.commit()

# Query the table
calculations = session.query(CalculationHistory).all()
for calculation in calculations:
    print(calculation)

# Close the session
session.close()