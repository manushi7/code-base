import sqlite3

conn = sqlite3.connect('mock_user.db')
c = conn.cursor()


commands = [("""
                CREATE TABLE users(
                    id integer PRIMARY KEY
                    username text,
                    email text,
                    password text,
                    address text,
                    phoneno integer
                )"""),
                ("""
                    CREATE TABLE tools(
                       id integer PRIMARY KEY
                       tool_name text,
                       half_day_rate integer,
                       full_day_rate integer,
                       description text,
                       FOREIGN KEY (users_id) REFERENCES users(id)
                    )"""),
                ("""
                    CREATE TABLE invoice(
                        id integer PRIMARY KEY
                        description text,
                        quantity integer,
                        price integer,
                        total integer,
                        FOREIGN KEY (users_id) REFERENCES users(id)
                    )"""),
                ("""
                    CREATE TABLE transaction(
                        id integer PRIMARY KEY,
                        FOREIGN KEY (user_name) REFERENCES users(username),
                        FOREIGN KEY (tool_name_) REFERENCES tools(tool_name),
                        FOREIGN KEY (quantity_) REFERENCES tools(quantity),
                        FOREIGN KEY (half_day_rate) REFERENCES tools(half_day_rate),
                        FOREIGN KEY (full_day_rate) REFERENCES tools(full_day_rate)
                    )""")
                ]
new_user = '''
            INSERT INTO users VALUES('bisesh', 'bisesh@hotmail.com', 'linux123',
            'sallaghari', 323232323)
            )'''

get_one_user = '''
            SELECT * FROM users WHERE username = 'bisesh'
            '''
get_user = '''
            SELECT * FROM users 
            '''
user_id = get_user.fetchall()[0][0]
new_tool = '''
            INSERT INTO tools VALUES ('hammer', 240 , 480 , 'is used
            to hammer things', ?))''',(user_id)


new_transaction = '''
                    INSERT INTO transaction VALUES
                    ('bisesh', 'hammer')
                   '''
get_tool = '''
            SELECT * FROM tools 
            '''

def create_table():
    try:
        for i in commands:
            c.execute(i)
    except Exception as e:
        print(e)
        print('table already exists')

def create_user():
    c.execute(new_user)

def add_tool():
    c.execute(new_tool)
    
def create_transaction():
    c.execute(new_transaction)

def prepare_invoice():
    c.execute(get_user)
    s = c.fetchall()
    for i in s:
        get_user_transaction = '''
                                SELECT * FROM transactions WHERE user_name=?
        
                                ''',(i[1])

        total = get_user_transaction.fetchall()
        if len(total) < 1:
            create_invoice = '''
                            INSERT INTO invoice VALUES(?,?,?,?)
                            '''
            c.execute(create_invoice, (i[2],i[3],i[4],i[3]*i[4]))

        elif len(total) > 1:
            for k in total:
                create_invoice = '''
                                 INSERT INTO invoice VALUES(?,?,?,?)
                                 '''
                c.execute(create_invoice, (k[2], k[3], k[4], k[3]*k[4]))


                
