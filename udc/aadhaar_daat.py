import pandas
import pandasql

def aggregate_query(filename):

    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = '''select gender, district, sum(aadhaar_generated) from aadhaar_data where age > 50 group by gender, district;'''

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution
