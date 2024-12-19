import pandas as pd

data = {
    'store': [1, 2, 3, 4]
}
DataFrame = pd.DataFrame(data)
DataFrame['kopilka'] = DataFrame['store'].cumsum()
print(DataFrame)
