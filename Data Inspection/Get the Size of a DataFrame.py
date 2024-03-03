import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    number_of_rows = players.shape[0]
    number_of_columns = players.shape[1]
    return [number_of_rows, number_of_columns]
