"""Example for exploring SQLAlchemy

This project provide code how to use AQLAlchemy.  This idea is to build an
example sequentially in steps to give new users the idea on where to start
and how to progress.  Along the way some principles will be exhibited.  The
code should be self-explanatory without as little as possible documentation,
else the project is failing.

This example illustrate the following:
--------------------------------------

1. Establis a link to a MySQL or SQLite database

2. Create tables

3. Populate the tables

4. Configure a many--to-may relationship

5. Query the tables

References
----------

- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_many_to_many_relationships.htm
- https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship
- https://cyruslab.net/2020/07/16/pythoncreate-database-if-not-exists-with-sqlalchemy/
"""


from beetools import msg_info, msg_milestone
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, create_engine, ForeignKey, Integer, String
from sqlalchemy_utils import database_exists, create_database, drop_database


Base = declarative_base()


class CountryCurrency(Base):
    __tablename__ = 'country_currency'

    country_id = Column(Integer, ForeignKey('country.id'), primary_key=True)
    currency_id = Column(Integer, ForeignKey('currency.id'), primary_key=True)


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    cca2 = Column(String(2), unique=True)
    cca3 = Column(String(3), unique=True)
    name_common = Column(String(100))

    # many to many Country<->Currency
    currencies = relationship(
        'Currency',
        secondary="country_currency",
        viewonly=True,
        # cascade="all, delete, delete-orphan"
    )

    def __init__(self, cca2, cca3, name_common):
        self.cca2 = cca2
        self.cca3 = cca3
        self.name_common = name_common

    def __str__(self):
        return (
            f"<Country(id = {self.id}, cca3 = {self.cca3}, "
            f"cca2 = {self.cca2}, name_common = {self.name_common}, "
            f"curr_iso = {self.curr_iso}"
        )

    def __repr__(self):
        return f"Country({self.cca2}, {self.cca3}, {self.name_common})"


class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True)
    curr_iso = Column(String(3), unique=True)
    name = Column(String(50))
    symbol = Column(String(25))
    # many to many Country<->Currency
    countries = relationship(
        'Country', secondary='country_currency', viewonly=True
    )  # , overlaps="currencies")

    def __init__(self, curr_iso, name, symbol):
        self.curr_iso = curr_iso
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return f"<Currency(curr_iso = {self.curr_iso}, name = {self.name}"

    def __repr__(self):
        return f"Country({self.curr_iso}, {self.name}, {self.symbol})"


class SQLAlchemyExample:
    """Class description"""

    def __init__(self, p_ini_pth, p_logger=False):
        """Method description"""
        print(msg_info('Instantiating the class (example)...'))
        self.success = True
        self.ini_pth = p_ini_pth
        self.logger_name = None
        self.logger = None
        self.verbose = False

        self.url = 'sqlite:///CountryData.sqlite'

        # self.base = None
        self.engine = None
        self.meta_data = None
        self.conn = None
        self.Session = None
        self.sess = None

        self.country_tab = None
        self.currency_tab = None
        self.ass_country_currency_tab = None

    def step_01_assign_attributes(self):
        """Method description"""
        print(msg_info('Step 1: Assign the attributes...'))
        self.engine = create_engine(self.url)
        self.conn = self.engine.connect()
        self.Session = sessionmaker(bind=self.engine)
        self.sess = self.Session()
        return True

    def step_02_create_the_db(self):
        print(msg_info('Step 2: Create the database...'))
        if database_exists(self.url):
            drop_database(self.url)
        create_database(self.url)
        Base.metadata.create_all(self.engine)
        pass

    def step_03_populate_the_db(self):
        print(msg_info('Step 3: Add data to the tables...'))
        PopulateCountry(self.sess).add_test_data()
        PopulateCurrency(self.sess).add_test_data()
        PopulateCountryCurrency(self.sess).add_test_data()
        pass

    def step_04_display_data(self):
        print(msg_info('Step 4: Read data from the tables...'))
        print(msg_milestone('- Country table'))
        for country in self.sess.query(Country).order_by(Country.cca2):
            print(country.cca2, country.cca3, country.name_common)
        print()

        print(msg_milestone('- Currency table'))
        for currency in self.sess.query(Currency).order_by(Currency.curr_iso):
            print(currency.curr_iso, currency.name, currency.symbol)
        print()

        print(msg_milestone('- Country <-> Currency table'))
        for x in (
            self.sess.query(Country, Currency)
            .filter(
                CountryCurrency.country_id == Country.id,
                CountryCurrency.currency_id == Currency.id,
            )
            .order_by(Country.name_common)
            .all()
        ):
            print(f"Country: {x.Country.name_common} Currency: {x.Currency.curr_iso}")
            pass

    def step_05_delete_records(self):
        print(msg_info('Step 5: Delete records...'))
        pass

    def step_06(self):
        pass

    def run(self):
        """Method description"""
        self.step_01_assign_attributes()
        self.step_02_create_the_db()
        self.step_03_populate_the_db()
        self.step_04_display_data()
        self.step_05_delete_records()
        self.step_06()
        pass


class PopulateCountry:
    def __init__(self, p_session):
        self.sess = p_session
        self.test_data = [
            ('ZAF', 'ZA', 'South Africa', 'ZAR'),
            ('USA', 'US', 'United States of America', 'USD'),
            ('GBR', 'GB', 'United Kingdom', 'GBP'),
            ('DER', 'DE', 'Federal Republic of Germany', 'EUR'),
            ('AUS', 'AU', 'Australia', 'AUD'),
            ('LSO', 'LS', 'Lesotho', 'ZAR'),
            ('SWZ', 'SZ', 'Eswatini', 'ZAR'),
        ]

    pass

    def add_test_data(self):
        for country in self.test_data:
            self.sess.add(
                Country(
                    cca3=country[0],
                    cca2=country[1],
                    name_common=country[2],
                    # curr_iso = country[3]
                )
            )
        self.sess.commit()
        pass


class PopulateCurrency:
    def __init__(self, p_session):
        self.sess = p_session
        self.test_data = [
            ('ZAR', 'South African rand', 'R'),
            ('USD', 'United States dollar', '$'),
            ('GBP', 'Pound sterling', '£'),
            ('EUR', 'Euro', '€'),
            ('AUD', 'Australian dollar', '$'),
            ('LSL', 'Lesotho loti', 'l'),
            ('SZL', 'Swazi lilangeni', 'L'),
        ]

    def add_test_data(self):
        for currency in self.test_data:
            self.sess.add(
                Currency(
                    curr_iso=currency[0],
                    name=currency[1],
                    symbol=currency[2],
                )
            )
        pass
        self.sess.commit()


class PopulateCountryCurrency:
    def __init__(self, p_session):
        self.sess = p_session
        self.test_data = [
            ('ZA', 'ZAR'),
            ('US', 'USD'),
            ('GB', 'GBP'),
            ('DE', 'EUR'),
            ('AU', 'AUD'),
            ('LS', 'ZAR'),
            ('LS', 'LSL'),
            ('SZ', 'ZAR'),
            ('SZ', 'SZL'),
        ]

    def add_test_data(self):
        for cntry, curr in self.test_data:
            cntry_det = self.sess.query(Country).filter(Country.cca2 == cntry).first()
            curr_det = (
                self.sess.query(Currency).filter(Currency.curr_iso == curr).first()
            )
            self.sess.add(
                CountryCurrency(country_id=cntry_det.id, currency_id=curr_det.id)
            )
            pass
        self.sess.commit()
        pass


if __name__ == '__main__':
    t_sqlalchemyexample = SQLAlchemyExample()
    if t_sqlalchemyexample.success:
        t_sqlalchemyexample.run()
# end __main__
