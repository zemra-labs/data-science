from bs4 import BeautifulSoup
import pandas as pd
import requests
import sys
import traceback
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# import seaborn as sns
bucket = {}
table_header = []
table_data = {}
tb_data = []
tb_d = []
tr_data = []

# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

def get_data(stock):
    stock = stock.lower()
    stock_data = 'http://finance.yahoo.com/q/hp?s=' + stock + '&a=04&b=10&c=2011&d=04&e=5&f=2016&g=d'
    cmc = requests.get(stock_data)
    bucket['content'] = cmc.content

def parse_data(content):
    soup = BeautifulSoup(content, 'lxml')
    for th in soup.find_all('th', class_='yfnc_tablehead1'):
        table_header.append(str(th.get_text()).strip())

    for row in soup.find_all('tr'):
        for value in row.find_all('td', class_='yfnc_tabledata1'):
            if value.has_attr('nowrap'):
                new_list = []
                table_data[str(value.get_text())] = str(value.get_text())
                first = value.findNext('td')
                second = first.findNext('td')
                third = second.findNext('td')
                fourth = third.findNext('td')
                fifth = fourth.findNext('td')
                sixth = fifth.findNext('td')
                new_list.append(str(first.get_text()))
                new_list.append(str(second.get_text()))
                new_list.append(str(third.get_text()))
                new_list.append(str(fourth.get_text()))
                new_list.append(str(fifth.get_text()).replace(',', ''))
                new_list.append(str(sixth.get_text()))
                table_data[str(value.get_text())] = new_list

def data_cleansing(df):
    df = df
    df.set_index(0)
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    df2 = df[['Open','Close', 'Volume']]
    df3 = df2.apply(pd.to_numeric, errors='coerce')
    df3['Mean Price'] = (df3['Open'] + df3['Close'])/2
    print df3
    return df3

def linear_model(df):
    dff = df
    print dff.isnull().values.any()
    df2 = dff.fillna(0)
    print df2.isnull().values.any()
    # print dff
    linreg = LinearRegression()

    x = df2[['Mean Price']]
    y = df2[['Volume']]

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    # linreg.fit(x, y)
    linreg.fit(x_train, y_train)

    # intercept = linreg.intercept_
    # coef = linreg.coef_
    #
    # # make prediction on testing set
    # prediction = linreg.predict(x_test)
    #
    # # compute root mean squared error
    # print np.sqrt(metrics.mean_squared_error(y_test, prediction))

def create_df(table_header, table_data):
    df = pd.DataFrame.from_dict(table_data, orient='index')
    return df

def main():
    if len(sys.argv) >= 2:
        stock = sys.argv[1]
        get_data(stock)
        parse_data(bucket['content'])
        df = create_df(table_header, table_data)
        dff = data_cleansing(df)
        linear_model(dff)
    else:
        traceback.print_tb()

if __name__ == '__main__':
    main()
