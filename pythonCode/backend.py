from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import datetime
import json
import numpy as np
from sklearn.linear_model import LinearRegression
import pytz

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['MONGO_URI'] = 'mongodb://exceed_group08:r63tbmyq@158.108.182.0:2255/exceed_group08'
mongo = PyMongo(app)

myCollection = mongo.db.nubwuttagum_store


@app.route('/update_customer/<storeId>', methods=['POST'])
@cross_origin()
def update_customer(storeId):
    # get status (0/1) for (in/out)
    data = request.json
    storeId = int(storeId)
    statusId = int(data['statusId'])
    filt = {'storeId': int(storeId)}

    query = myCollection.find_one(filt)
    currentCustomer = query['currentCustomer']


    unconverted_now = datetime.datetime.now()
    timezone = pytz.timezone("Asia/Bangkok")
    now = unconverted_now.astimezone(timezone)
    minute = now.minute  # Too tell minute for now
    five_minutes_current_interval = minute // 5  # Current interval for data Array(size(12))
    currentMinuteCumulativeCustomer = query['thisHourCumulativeCustomerEveryFiveMinutes'][five_minutes_current_interval]

    hour = now.hour
    if hour != query['lastHourChecked']:
        myCollection.update_one(filt, {'$set': {
        'thisHourCumulativeCustomerEveryFiveMinutes': [0,0,0,0,0,0,0,0,0,0,0,0],
        'lastHourChecked': hour
        }})

    if now.strftime("%x") != query['cumulativeCustomer'][-1]['timeStamp']:
        added_day = {'$push': {'cumulativeCustomer': {'timeStamp': now.strftime("%x"), 'cumulativeCustomerPerHour': [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}}
        myCollection.update_one(filt, added_day)

    if hour == 25:
        hour = 0

    currentHourCumulativeCustomer = query['cumulativeCustomer'][-1]["cumulativeCustomerPerHour"][hour]

    if statusId == 0:
        currentCustomer -= 1
    else:
        currentCustomer += 1
        currentMinuteCumulativeCustomer += 1
        currentHourCumulativeCustomer += 1
        if hour < 24:
            query['cumulativeCustomer'][-1]["cumulativeCustomerPerHour"][hour + 1] = currentHourCumulativeCustomer
        if five_minutes_current_interval + 1 < 11:
            query['thisHourCumulativeCustomerEveryFiveMinutes'][five_minutes_current_interval + 1] = currentMinuteCumulativeCustomer

    updated_content = {'$set': {
        'currentCustomer': currentCustomer,
        'thisHourCumulativeCustomerEveryFiveMinutes.' + str(five_minutes_current_interval): currentMinuteCumulativeCustomer,
    }}

    length = len(myCollection.find({'storeId': 0})[0]['cumulativeCustomer'])
    myCollection.update_one(filt, updated_content)
    if hour == 0:
        hour = 1
    myCollection.update_one(
        filt,
        {"$set": {'cumulativeCustomer.' +
                  str(length-1) + '.cumulativeCustomerPerHour.' + str(hour-1): currentHourCumulativeCustomer}}
    )

    return {'result': 'Updated successfully'}


@app.route('/max', methods=['GET'])
@cross_origin()
def get_max():
    query = myCollection.find_one()
    max_customer = {
        "maxCustomer": query["maxCustomer"],
    }
    return max_customer


@app.route('/current', methods=['GET'])
@cross_origin()
def get_current():
    query = myCollection.find_one()
    current = {
        "currentCustomer": query["currentCustomer"],
    }
    return current


@app.route('/minute', methods=['GET'])
@cross_origin()
def get_per_minute_this_hour():
    query = myCollection.find_one()
    five_minute = query["thisHourCumulativeCustomerEveryFiveMinutes"]
    list_five = []
    for i in five_minute:
        list_five.append(i)
    return json.dumps(list_five)


@app.route('/hour', methods=['GET'])
@cross_origin()
def get_per_hour():
    query = myCollection.find_one()
    data = query['cumulativeCustomer']
    list_day = []
    list_hour = []
    for i in data:
        list_day.append(i)
    latest_date = list_day[-1]
    del latest_date["timeStamp"]
    for i in latest_date.values():
        list_hour.append(i)
    return json.dumps(list_hour[0])


@app.route('/day', methods=['GET'])
@cross_origin()
def get_per_day():
    query = myCollection.find_one()
    data = query['cumulativeCustomer']
    list_day = []
    list_hour = []
    for i in data:
        list_day.append(i)
    latest_date = list_day[-1]
    del latest_date["timeStamp"]
    for i in latest_date.values():
        list_hour.append(i)
    return json.dumps(max(list_hour[0]))  # However the cumulative is always a max value in that day

@app.route('/get_predict', methods=['GET'])
@cross_origin()
def get_predict():
    query = myCollection.find_one()
    data = query['predictResult']
    return json.dumps(data)

@app.route('/predict_customer/<storeId>', methods=['GET'])
@cross_origin()
def predict_customer(storeId):
    # get store id
    storeId = int(storeId)
    filt = {'storeId': int(storeId)}

    # query data from database
    query = myCollection.find_one(filt)
    cumulative = query['cumulativeCustomer']
    maxCustomer = query['maxCustomer']

    # initial value
    x = np.array([[0, 0]])  # dayId 0-6, dayHour 0-23
    y = np.array([0])  # expected cumulative number
    firstDayInDatabase = -1

    # indicate test data
    x_test = np.array([[0, 0]])
    for i in range(24):
        for j in range(7):
            x_test = np.append(x_test, [[i, j]], axis=0)
    x_test = x_test[1:]

    # put the database's data into our dataset
    for data in cumulative:
        month, day, year = [int(i) for i in data['timeStamp'].split('/')]
        d = datetime.datetime(year, month, day)
        weekday = int(d.strftime('%w'))
        if (firstDayInDatabase == -1):
            firstDayInDatabase = weekday

        for i in range(24):
            x = np.append(x, [[weekday, i]], axis=0)
            cumulative = data['cumulativeCustomerPerHour'][i]
            y = np.append(y, [cumulative], axis=0)

    x = x[1:]
    y = y[1:]

    # create model
    model = LinearRegression()
    model.fit(x, y)

    # validate model
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)

    # prediction
    y_pred = [i if i > 0 else 0 for i in model.predict(x_test)]
    print('predicted response:', y_pred, sep='\n')

    # get average customer in each day a week
    dayAverage = []
    for i in range(0, len(y_pred), 24):
        sumValue = sum(y_pred[i:i+24])
        dayAverage.append(sumValue/24)
    dayAverage = shift(dayAverage, firstDayInDatabase)

    # get customer density in each day a week
    customerDensity = []
    for elem in dayAverage:
        customerDensity.append(elem/maxCustomer)

    # get customer density today
    day = int(datetime.datetime.today().strftime('%w'))
    customerDensityToday = customerDensity[day]

    return {'predictResult': json.dumps(dayAverage), 'customerDensity': json.dumps(customerDensity), 'customerDensityToday': customerDensityToday}


def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)
