import pandas as pd
import numpy as np
import datetime
from catchment.models import Site, Location

print(Site.version)

FP35 = Site('FP35')


rainfall_data = pd.Series(
    [0.0,2.0,1.0],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3)
        ]
    )
waterpH_data = pd.Series(
    [7.8,8.0,7.9],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3)
        ]
    )

FP35.add_measurement('Rainfall', rainfall_data, 'mm')
FP35.add_measurement('Water pH', waterpH_data)

print(FP35.measurements['Rainfall'].series)
print(FP35.measurements.keys())
print(FP35.measurements['Rainfall'])

default_site = Site.create_sample_site()
print(default_site.name)

print(FP35)

lastdata = FP35.last_measurements
#print(lastdata)

PL12 = Location('PL12')
print(PL12)

PL12.add_measurement('Rainfall', rainfall_data)

#data = pd.DataFrame([[1., 2., 3.], [4., 5., 6.]],
                     #index=['FP35','FP56'])

#location_measurement = [
   # ("FP", "FP35", "Rainfall"),
   # ("FP", "FP56", "River Level"),
   # ("PL", "PL23", "River Level"),
   # ("PL", "PL23", "Water pH")
# ]
# index_names = ["Catchment", "Site", "Measurement"]
# index = pd.MultiIndex.from_tuples(location_measurement,names=index_names)
#
# data = [
#     [0., 2., 1.],
#     [30., 29., 34.],
#     [34., 32., 33.],
#     [7.8, 8., 7.9]
# ]
#
# data2 = pd.DataFrame(data,index=index)
#
# print(data2)
#
# measurement_data = [
#     {
#         'site': 'FP35',
#         'measurement': 'Rainfall',
#         'data': [0.0, 2.0, 1.0]
#     },
#     {
#         'site': 'FP56',
#         'measurement': 'River level',
#         'data': [30.0, 29.0, 34.0]
#     },
# ]
#
# print(measurement_data)
#
# def attach_names(data, site, measurement):
#     """Create datastructure containing measurement data from a range of sites."""
#     assert len(data) == len(names)
#     assert len(data) == len(measurements)
#     output = []
#
#     for data_row, measurement, site in zip(data, measurement, site):
#         output.append({'site': site,
#                        'measurement': measurement,
#                        'data': data_row})
#
#     return output
#
# data = np.array([[34., 32., 33.],
#                  [7.8, 8.0, 7.9]])
#
# output = attach_names(data, ['PL23', 'PL23'], ['River level', 'pH'])
# print(output)
#



