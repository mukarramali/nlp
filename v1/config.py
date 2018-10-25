from string import digits
from IPython import embed

def to_s(list, delim = "\n"):
	return delim.join(map(str,list))

def sample_text():
	text = "Journalist Eddie Brock is trying to take down Carlton Drake, the notorious and brilliant founder of the Life Foundation. While investigating one of Drake's experiments, Eddie's body merges with the alien Venom -- leaving him with superhuman strength and power. Twisted, dark and fueled by rage, Venom tries to control the new and dangerous abilities that Eddie finds so intoxicating."
	return text.translate(digits).decode("utf-8")

def breakpoint():
	embed()

