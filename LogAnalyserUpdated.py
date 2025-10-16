import pandas as pd

class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()

    def DiceRead(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        # ✅ >>> ADICIONADO: pular linhas até achar a primeira que começa com "Round"
        for i, line in enumerate(lines):
            if line.strip().startswith("Round"):
                lines = lines[i:]  # mantém só as linhas a partir de "Round"
                break
        for line in lines:
            try:
                round_part, rolls_part = line.strip().split(":", 1)
            except ValueError:
                continue  # pula linhas que não têm o formato esperado

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
        self.df.index += 1  # rounds começam em 1
        self.df.index.name = "Round"


mylog = LogAnalyser()
mylog.DiceRead(r"C:\Users\framb\OneDrive\Área de Trabalho\python\a")
print(mylog.df)
print(mylog.df.head(2))
#print(mylog.df.info())
#print(mylog.df.describe())
#print(mylog.df.shape)