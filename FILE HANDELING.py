class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name

class PerformanceData:
    def __init__(self, player, runs, wickets, catches):
        self.player = player
        self.runs = runs
        self.wickets = wickets
        self.catches = catches

class PerformanceAnalysis:
    def __init__(self):
        self.data = {}  
        try:
            with open('performance_data.txt', 'r') as file:
                for line in file:
                    data_values = line.strip().split(',')
                    if len(data_values) == 5:
                        player_id, name, runs, wickets, catches = map(str.strip, data_values)
                        player_id, runs, wickets, catches = int(player_id), int(runs), int(wickets), int(catches)
                        player = Player(player_id, name)
                        data = PerformanceData(player, runs, wickets, catches)
                        self.data[player_id] = data
                    else:
                        print("Invalid data format. Skipping line.")
        except FileNotFoundError:
            print("Performance data file not found. It will be created when performance data is added.")

    def create_data(self, player_id, name, runs, wickets, catches):
        if player_id in self.data:
            print(f"Player ID {player_id} already exists. Use another player ID.")
            return
        else:
            player = Player(player_id, name)
            data = PerformanceData(player, runs, wickets, catches)
            self.data[player_id] = data
            with open('performance_data.txt', 'a') as file:
                file.write(f"{player_id},{name},{runs},{wickets},{catches}\n")
            print(f"Performance data created for player {player_id} - {name}")

    def read_data(self, player_id):
        if player_id in self.data:
            data = self.data[player_id]
            print(f"Player ID: {data.player.player_id}, Name: {data.player.name}, Runs: {data.runs}, Wickets: {data.wickets}, Catches: {data.catches}")
        else:
            print(f"No performance data found for player {player_id}")

    def update_data(self, player_id, runs=None, wickets=None, catches=None):
        if player_id in self.data:
            data = self.data[player_id]
            if runs is not None:
                data.runs = runs
            if wickets is not None:
                data.wickets = wickets
            if catches is not None:
                data.catches = catches
            with open('performance_data.txt', 'r') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if str(player_id) in line:
                        line = f"{player_id},{data.player.name},{data.runs},{data.wickets},{data.catches}\n"
                    file.write(line)
                file.truncate()
            print(f"Performance data updated for player {player_id}")
        else:
            print(f"Player {player_id} not found.")

    def delete_data(self, player_id):
        if player_id in self.data:
            del self.data[player_id]
            with open('performance_data.txt', 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if str(player_id) not in line:
                        file.write(line)
                file.truncate()
            print(f"Performance data deleted for player {player_id}")
        else:
            print(f"Player {player_id} not found. Deletion failed.")

    def provide_performance_feedback(self, player_id):
        if player_id in self.data:
            data = self.data[player_id]
            print(f"**Feedback for Player {player_id}:**")
            if data.runs > 50:
                print("Excellent batting performance!")
            if data.wickets > 2:
                print("Impressive bowling!")
            if data.catches > 2:
                print("Outstanding fielding!")
        else:
            print(f"No performance data found for player {player_id}. Feedback unavailable.")

performance_analysis = PerformanceAnalysis()

while True:
    print("\nCricket Team Performance Analysis")
    print("1. Create Performance Data")
    print("2. Read Performance Data")
    print("3. Update Performance Data")
    print("4. Delete Performance Data")
    print("5. Provide Performance Feedback")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        player_id = int(input("Enter player ID: "))
        name = input("Enter player name: ")
        runs = int(input("Enter runs scored: "))
        wickets = int(input("Enter wickets taken: "))
        catches = int(input("Enter catches taken: "))
        performance_analysis.create_data(player_id, name, runs, wickets, catches)
    elif choice == '2':
        player_id = int(input("Enter player ID: "))
        performance_analysis.read_data(player_id)
    elif choice == '3':
        player_id = int(input("Enter player ID to update: "))
        update_choice = input("Update (runs/wickets/catches) or all (a)? ")
        if update_choice.lower() == 'a':
            runs = int(input("Enter new runs: "))
            wickets = int(input("Enter new wickets: "))
            catches = int(input("Enter new catches: "))
            performance_analysis.update_data(player_id, runs, wickets, catches)
        else:
            if update_choice.lower() == 'runs':
                runs = int(input("Enter new runs: "))
                performance_analysis.update_data(player_id, runs=runs)
            elif update_choice.lower() == 'wickets':
                wickets = int(input("Enter new wickets: "))
                performance_analysis.update_data(player_id, wickets=wickets)
            elif update_choice.lower() == 'catches':
                catches = int(input("Enter new catches: "))
                performance_analysis.update_data(player_id, catches=catches)
            else:
                print("Invalid update choice. Please try again.")
    elif choice == '4':
        player_id = int(input("Enter player ID to delete:"))
        performance_analysis.delete_data(player_id)
    elif choice == '5':
        player_id = int(input("Enter player ID for feedback: "))
        performance_analysis.provide_performance_feedback(player_id)
    elif choice == '6':
        print("Exiting Cricket Team Performance Analysis.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
