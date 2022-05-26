# This writes dataframe with plurality data to excel based on date

import pandas as pd
import psycopg2
import datetime

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn

def get_excel_df(conn,dte):
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from rs_industry_groups where date = %s"
    cursor.execute(postgreSQL_select_Query,(dte,))
    rs_ind_records = cursor.fetchall()

    rs_df = pd.DataFrame(rs_ind_records,
                         columns=['date', 'industry', 'ticker', 'rs1', 'rs2', 'rs3', 'rs4', 'rs'])

    return rs_df



if __name__ == '__main__':

    param_dic = {
        "host": "localhost",
        "database": "Plurality",
        "user": "postgres",
        "password": "root"
    }

    con = connect(param_dic)

    delta_days_from_current_date = 6
    dateTimeObj = datetime.datetime.now()
    run_date = dateTimeObj - datetime.timedelta(days=delta_days_from_current_date)
    run_date = run_date.strftime("%Y-%m-%d")

    print(run_date)

    rss_df = get_excel_df(con, run_date)


    rss_df.to_excel(r"C:\Users\uvdsa\Documents\Trading\Scripts\plurality-input.xlsx", index=False)
















