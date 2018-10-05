from string import digits

def print_list(list):
	print "\n".join(map(str,list))
	return

def sample_text():
	text = "A refrigerator (colloquially fridge, or fridge-freezer in the UK) is a popular household appliance that consists of a thermally insulated compartment and a heat pump (mechanical, electronic or chemical) that transfers heat from the inside of the fridge to its external environment so that the inside of the fridge is cooled to a temperature below the ambient temperature of the room. Refrigeration is an essential food storage technique in developed countries. The lower temperature lowers the reproduction rate of bacteria, so the refrigerator reduces the rate of spoilage. A refrigerator maintains a temperature a few degrees above the freezing point of water. Optimum temperature range for perishable food storage is 3 to 5 C (37 to 41 F).[1] A similar device that maintains a temperature below the freezing point of water is called a freezer. The refrigerator replaced the icebox, which had been a common household appliance for almost a century and a half. For this reason, a refrigerator is sometimes referred to as an icebox in American usage."
	return text.translate(None, digits)