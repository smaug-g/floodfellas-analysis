import pickle
import matplotlib
import matplotlib.dates
import matplotlib.pyplot
import boto3

client = boto3.client(
    's3',
    aws_access_key_id='AKIA6QRS4LYGJJ3CRMYH',
    aws_secret_access_key='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'
)

def iterate_bucket_items(bucket):
    """
    Generator that iterates over all objects in a given s3 bucket

    for return data format
    :param bucket: name of s3 bucket
    :return: dict of metadata for an object
    """


    paginator = client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket)

    for page in page_iterator:
        if page['KeyCount'] > 0:
            for item in page['Contents']:
                yield item

date_nums = []
sensor_values = []
for i in iterate_bucket_items(bucket='flood-fellas-mmwave'):
    text = client.get_object(Bucket='flood-fellas-mmwave', Key=i['Key'])['Body'].read().decode('utf-8')
    # print(text)
    res = text.split(',')
    # print(len(res))
    if (len(res) < 5):
        continue
    sensor_value = [int(x) for x in res[0:5]]
    date_str = i['Key'].split(' - ', 1)[1][:-4]
    date_num = matplotlib.dates.datestr2num(date_str)
    date_nums.append(date_num)
    sensor_values.append(sensor_value)

# print(date_nums)
# print(sensor_values)

with open('sensor_vals.pkl', 'wb') as f:
    pickle.dump([date_nums, sensor_values], f)
    f.close()

matplotlib.pyplot.plot_date(date_nums, sensor_values)
matplotlib.pyplot.show()
