from operator import itemgetter
import pickle
#a = "Mark"
#b = "Dan"
#c = "Paul"
#d = "Glenn"
#e = "Luke"
#f = "Joe"
#g = "Keith"
#h = "Jim"
#i = "Ian" 
#j = "Dave"
#k = "Harry"
def getKey(item):
    return item[0]


# pickle
high_scores = [
    [1800, "Mark"],
    [5000, "Dan"],
    [3200, "Paul"],
    [2000, "Glenn"],
    [3150, "Luke"],
    [7884, "Joe"],
    [2332, "Keith"],
    [77, "Jim"],
    [3259, "Ian"],
    [5748, "Dave"],
    [3758, "Harry"],
    
]

tempArray =[]


#high_scores = [str(x) for x in high_scores]
high_scores.sort(reverse=True)


print high_scores[:5]

def sortHighScores(high_scores):
    high_scores.sort(reverse=True)
    print high_scores[:5]
