import pandas as pd

class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()

    def DiceRead(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        #skip lines to get to the "Round" word
        for i, line in enumerate(lines):
            if line.strip().startswith("Round"):
                lines = lines[i:]  #maintain only lines after "Round"
                break
        for line in lines:
            try:
                round_part, rolls_part = line.strip().split(":", 1)
            except ValueError:
                continue  # skip lines that doesn't have the expected format

            rolls_dict = {}
            for part in rolls_part.split(","):
                part = part.strip()
                if " rolled " in part:
                    name, _, roll = part.partition(" rolled ")
                    rolls_dict[name] = int(roll)
                    if name not in self.player_names:
                        self.player_names.append(name)

            self.data.append(rolls_dict)

        self.df = pd.DataFrame(self.data, columns=self.player_names)
        self.df.index += 1  # rounds start in 1
        self.df.index.name = "Round"


mylog = LogAnalyser()
# place to write the analyzed file
url = input("Insert the name to the file you want to analyse: ")
mylog.DiceRead(url)
print(mylog.df)

# This ones can be used to show different informations about the data
# print(mylog.df.head(2))
# print(mylog.df.info())
# print(mylog.df.describe()) 
# print(mylog.df.shape)