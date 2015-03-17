import csv

class FlightSchedule:
	def __init__(self):
		self.flights = []
		self.plane_identifiers = []

	def read_data_from_file(self):
		with open("flight_data.csv", encoding='utf-8') as file:
			reader = csv.reader(file)
			for row in reader:
				self.flights.append(row[0])
				if row[1] not in self.plane_identifiers:
					self.plane_identifiers.append(row[1])
				
	def determine_longest_flight(self):
		highestValue = 100
		longestFlight = None
		with open("flight_data.csv", encoding='utf-8') as file:
			reader = csv.reader(file)
			for row in reader:
				if int(row[4]) > highestValue:
					longestFlight = row
					highestValue = int(longestFlight[4])
		return longestFlight[0]


		# make sure to assign .flights attribute
