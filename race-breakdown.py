import datetime

# Returns date/time in readable (string) format.
def readable(time):
	return str(datetime.timedelta(hours=time))

class RacePlan:
	def __init__(self, raceName, raceDistance, cutoff, expectedPace):
		
		# Distance of the race in km
		self.raceDistance = raceDistance
		self.expectedPace = expectedPace
		
		# Change to dictionary - use k, v to identify aid stations more clearly.
		aidstations = [12, 29, 36, 53, 57, 63, 66, 83, 99, 117, 125, 128, 149, 160, 174, 182, 193]
		
		# Variation in pace - over/under
		self.over = (expectedPace + 0.5)
		self.under = (expectedPace - 0.5)
		
		# My cal expenditure per km (average)
		averageCalExp = 134

		# Expected race time (race duration / expected average pace)
		raceTime = (raceDistance / expectedPace)
		
		# Nutrition formula ((race distance / expected average pace) / 40 minute nutrition window)
		nutrition = ((raceDistance / expectedPace) / (40/60))
		
		# Hydration requirements
		hydration = (raceTime / 2)
		
		# Average pace required to finish race at cut-off
		avgPaceReq = (raceDistance / cutoff)
		
		# How far ahead of cut-off
		lead = (cutoff - raceTime)
		self.lead = lead
		
		# Calorie requirement (duration of race in hours * average calorie expenditure from similar race)
		calReq = (raceDistance * averageCalExp)
		
		raceTime = readable(raceTime)

		print(f"\n{raceName} Plan")
		
		print(f'\nProjected finish time: {raceTime} hours.')
		
		print(f'\nYou need to maintain an average pace of {avgPaceReq:.3g}km/h to finish before cut-off.')
		
		if lead < 0:
			print(f'\nAt your pace you will not make cut-off. You will fall short by {readable(lead)} hours.')
		else:
			print(f'\nYou will finish {readable(lead)} hours ahead of cut-off.')			
		
			print(f'\nYou will require approx {round(nutrition)} snacks and {hydration:.3g}L of fluid.')

			print(f"\nYou'll burn an estimated {round(calReq)} calories during {raceName}.")
			
			print(f'\nCheckpoint Projections:')
			for station in aidstations:
		
				fast = (station / self.over)
				faster = readable(station / self.over)
				#faster = readable(faster)
				
				slow = (station / self.under)
				slower = readable(station / self.under)
				#slower = readable(slower)
		
				if fast >= 48:
					print(f'\n{station}km:\nOutside of cut-off')
				elif slow >= 48:
					print(f'\n{station}km:\n{faster} - You may not make it in time.')
				else:
					print(f'\n{station}km:\n{faster} - {slower}')

# seawheeze = RacePlan("Sea Wheeze Half", 21.2, 5, 8)

# diezvista = RacePlan("Diez Vista 50k", 50, 9, 6.5)

# runforwater = RacePlan("Run For Water", 50, 11, 6)

#riverrun = RacePlan("River Run", 50, 12, 8.2)

fatdog120 = RacePlan("Fat Dog 120", 192, 48, 5.2)

