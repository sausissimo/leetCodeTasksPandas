import pandas as pd
import numpy

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return players.shape

players = [[1,15,2],[2,11,2],[3,11,2],[4,20,2]]
playersDF = pd.DataFrame(players, columns = ["name", "type", "aboba"])
print(playersDF)

print()
print(numpy.array(getDataframeSize(playersDF)))