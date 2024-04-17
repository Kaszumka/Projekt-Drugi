import pandas as pd
dane = pd.read_csv(r"C:\Users\julia\Downloads\gesty.csv")
print(dane)

del dane["gesture_id"]

dane["gesture_id"] = 0
dane.loc[0:74, "gesture_id"] = 1
for i in range(1, int(dane.shape[0]/75)+1):
    dane.loc[i*75:(i+1)*75-1, "gesture_id"] = dane.loc[(i-1)*75, "gesture_id"]+1

dane = dane.drop(labels = range(375525, 375580), axis = 0)
print(dane)
#dane.to_csv(r"C:\Users\julia\Desktop\gesty_v3.csv")