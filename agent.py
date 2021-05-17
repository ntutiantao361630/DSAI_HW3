import pandas as pd
import datetime


class Agent:
    def __init__(self):
        self.gen = None
        self.use = None
        self.bid = None

    def load_data(self, gen_path, use_path, bid_path):
        self.gen = pd.read_csv(gen_path)
        self.use = pd.read_csv(use_path)

    def predict(self):
        print(self.gen)
        print(self.use)
        pass

    def output(self, output_path):
        day = self.gen['time'].values.tolist()
        col = ["time", "action", "target_price", "target_volume"]
        df = pd.DataFrame(columns=col)
        current_date_and_time = datetime.datetime.strptime(day[-1], '%Y-%m-%d %H:%M:%S')
        # print(current_date_and_time)
        ind = 0
        for i in range(1, 25):
            hours_added = datetime.timedelta(hours=i)
            future_date_and_time = current_date_and_time + hours_added
            # print(future_date_and_time)
            for j in range(4):
                if (j%2) == 0:
                    df.loc[ind] = [future_date_and_time, "buy", 3, 1]
                else:
                    df.loc[ind] = [future_date_and_time, "sell", 1, 1]

                ind += 1


        df.to_csv(output_path, index=False)
