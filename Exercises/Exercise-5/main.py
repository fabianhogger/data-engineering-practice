import csv
import glob
import os
import re
import psycopg2
"""
-- Database: joke

-- DROP DATABASE IF EXISTS joke;

create   table accounts
    (customer_id int not null
    , first_name varchar(50)
    , last_name varchar(50)
    ,   address_1 varchar(50)
    , address_2 varchar(50)
    , city varchar(50)
    , state varchar(50)
    , zip_code int
    , join_date date
    ,    primary key (customer_id)) 
insert into accounts
values(4321, 'john', 'doe', '1532 East Main St.', 'PO BOX 5', 'Middleton', 'Ohio', 50045, '2022/01/16')

select * from products

    create table products(
    product_id int not null
    , product_code varchar(50)
    , product_description varchar(50)
    ,    primary key (product_id))


insert into products
values(345, '01', 'Widget Medium')

create table transactions(
transaction_id varchar(27) not null
    , transaction_date date
    , product_id int 
    , product_code varchar(10)
    , product_description varchar(50)
    , quantity int
    , account_id int
    ,    primary key(transaction_id))


insert into transactions
values('AS345-ASDF-31234-FDAAD-9345', '2022/06/01', 345, '01', 'Widget Medium', 5, 4321)



"""
def main():
    host = "postgres"
    database = "postgres"
    user = "postgres"
    pas = "postgres"
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    cur = conn.cursor()
    #accounts
    cur.execute("""create   table accounts
        (customer_id int not null
        , first_name varchar(50)
        , last_name varchar(50)
        ,   address_1 varchar(50)
        , address_2 varchar(50)
        , city varchar(50)
        , state varchar(50)
        , zip_code int
        , join_date date
        ,    primary key (customer_id));""")
    #products
    cur.execute(""" create table products(
        product_id int not null
        , product_code varchar(50)
        , product_description varchar(50)
        ,    primary key (product_id))""")
    #transactions
    cur.execute("""create table transactions
        (transaction_id varchar(27) not null
        , transaction_date date
        , product_id int 
        , product_code varchar(10)
        , product_description varchar(50)
        , quantity int
        , account_id int
        ,    primary key(transaction_id))""")
    cwd = os.getcwd()
    paths=[]
    # initializing the titles and rows list
    fields = []

    for name in glob.glob(cwd+'\\data\\*?.csv',recursive=True):
        print(name)
        paths.append(name)
        rows = []
        # reading csv file
        with open(name, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            
            # extracting field names through first row
            fields = next(csvreader)
            numfields=len(fields)
            filename=re.sub('.csv','',name.split('\\')[-1])
            print(filename)
            # extracting each data row one by one
            for row in csvreader:
                rows.append(tuple(row))
                print(tuple(row))
            for row in rows:
                cur.execute(f"insert into {filename}   values(%s{(numfields-1)*',%s'})",row)
            conn.commit()
            cur.close()
            conn.close()


if __name__ == "__main__":
    main()
