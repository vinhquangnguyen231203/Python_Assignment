class rwFile:
    @staticmethod
    def read_data():
        data = []
        try:
            with open("DuLieu.txt", "r", encoding="utf-8") as file:
                for line in file:
                    data.append(line.strip().split(","))
        except FileNotFoundError:
            pass
        return data

    @staticmethod
    def write_data(data):
        with open("DuLieu.txt", "w") as file:
            for record in data:
                file.write(",".join(record) + "\n")
