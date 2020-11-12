import sqlite3

con  = sqlite3.connect("empire.db")


c = con.cursor()


def commit():
    con.commit()


def close():
    con.close()


def check_unique(str_key, table_name, table_attribute):
    key_query = """SELECT {} FROM {}""".format(table_attribute, table_name)
    c.execute(key_query)
    keys_fetchall = c.fetchall()
    if(keys_fetchall != None):
        for key_fetchone in keys_fetchall:
            for key in key_fetchone:
                if(key == str_key):
                    return False
    return True


def create_fake_name(fake_name, real_name):
    if(check_unique(fake_name, "FakeName", "FakeName")):
        insert = """INSERT INTO FakeName(FakeName, RealName)
                        VALUES("{}", "{}")""".format(fake_name, real_name)
        c.execute(insert)
        commit()
        return True

def get_fake_names():
    query = """SELECT FakeName FROM FakeName"""
    c.execute(query)
    names_fetchall = c.fetchall()
    names = []
    for name in names_fetchall:
        for n in name:
            names.append(n)
    return names
