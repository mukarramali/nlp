from string import digits
from IPython import embed
import matplotlib.pyplot as plt
from beautifultable import BeautifulTable

def list_s(list, delim = "\n"):
	return delim.join(map(str,list))

def max_freq(list):
    return list.count(max(list,key=list.count))

def sample_text():
	text = "Journalist Eddie Brock is trying to take down Carlton Drake, the notorious and brilliant founder of the Life Foundation. While investigating one of Drake's experiments, Eddie's body merges with the alien Venom -- leaving him with superhuman strength and power. Twisted, dark and fueled by rage, Venom tries to control the new and dangerous abilities that Eddie finds so intoxicating."
	return text.translate(digits).decode("utf-8")

def breakpoint():
	embed()

def draw_table(column2, column3):
	table = BeautifulTable()
	table.column_headers = ["key", "dataset", "article"]
	for key in column3:
		table.append_row([key, column2.get(key), column3.get(key)])
	print(table)


def draw_hash(pairs, title):
	plt.bar(range(len(pairs)), list(pairs.values()), align='center')
	plt.xticks(range(len(pairs)), list(pairs.keys()))
	plt.title(title)
	plt.show()
