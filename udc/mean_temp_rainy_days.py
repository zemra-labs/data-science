import pandas
import pandasql

def avg_min_temperature(filename):

    weather_data = pandas.read_csv(filename)

    q = """
        select avg(mintempi) from weather_data where rain=1 and mintempi > 55
    """

    #Execute your SQL command against the pandas frame
    avg_min_temp_rainy = pandasql.sqldf(q.lower(), locals())
    return avg_min_temp_rainy
