#Duck_typing: Duck typing in Python is a programming concept where
#the type or the class of an object is less important than the methods it defines. 
#When you use duck typing, you do not check types at all. 
#Instead, you check for the presence of a given method or attribute.
class Database:
    def connect(self):
        return 'Connected to the database'

class MockDatabase:
    def connect(self):
        return 'Connected to the mock database'
    def load_fixture(self, fixture):
        return f'Loaded {fixture} into the mock database'

def setup_database(db):
    print(db.connect())
    # hasattr(obj,'variable/method' ) => 
    # to check either for attributes(variables) or methods whether present in that object or not
    if hasattr(db, 'load_fixture'):
        print(db.load_fixture('test_data'))

real_db = Database()
test_db = MockDatabase()
setup_database(real_db)
setup_database(test_db)


# In this example, the setup_database function uses duck typing to connect to a database. 
# It doesn’t care whether it’s connecting to a real or mock database; 
# it only cares that the db object has a connect method. Additionally, 
# it checks if the db object has a load_fixture method before calling it. 
# This is a more advanced use of duck typing, where we’re dynamically checking the presence of methods.