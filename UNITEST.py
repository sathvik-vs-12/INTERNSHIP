import unittest

class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name

class PerformanceData:
    def __init__(self):
        self.data = {}

    def create_performance(self, player_id, performance):
        if player_id not in self.data:
            self.data[player_id] = []
        self.data[player_id].append(performance)

    def read_performance(self, player_id):
        return self.data.get(player_id, [])

    def update_performance(self, player_id, index, new_performance):
        if player_id in self.data and 0 <= index < len(self.data[player_id]):
            self.data[player_id][index] = new_performance
        else:
            raise ValueError("Invalid player_id or index")

    def delete_performance(self, player_id, index):
        if player_id in self.data and 0 <= index < len(self.data[player_id]):
            del self.data[player_id][index]
        else: 
            raise ValueError("Invalid player_id or index")

class PerformanceAnalysis:
    @staticmethod
    def monitor_player_stats(player_id, performance_data):
        performances = performance_data.read_performance(player_id)
        return performances

    @staticmethod
    def provide_performance_feedback(feedback_id):
        return f"Feedback for performance {feedback_id}"

class TestPerformanceAnalysis(unittest.TestCase):
    def setUp(self): 
        self.player1 = Player(1, "John Doe")
        self.performance_data = PerformanceData()  

    def test_create_performance(self):
        self.performance_data.create_performance(self.player1.player_id, {"score": 10})
        self.assertEqual(len(self.performance_data.read_performance(self.player1.player_id)), 1)

    def test_update_performance(self):
        self.performance_data.create_performance(self.player1.player_id, {"score": 10})
        self.performance_data.update_performance(self.player1.player_id, 0, {"score": 20})
        self.assertEqual(self.performance_data.read_performance(self.player1.player_id)[0]["score"], 20)

    def test_delete_performance(self):
        self.performance_data.create_performance(self.player1.player_id, {"score": 10})
        self.performance_data.delete_performance(self.player1.player_id, 0)
        self.assertEqual(len(self.performance_data.read_performance(self.player1.player_id)), 0)

    def test_monitor_player_stats(self):
        self.performance_data.create_performance(self.player1.player_id, {"score": 10})
        self.performance_data.create_performance(self.player1.player_id, {"score": 20})
        performances = PerformanceAnalysis.monitor_player_stats(self.player1.player_id, self.performance_data)
        self.assertEqual(len(performances), 2)

    def test_provide_performance_feedback(self):
        feedback = PerformanceAnalysis.provide_performance_feedback(400)
        self.assertEqual(feedback, "Feedback for performance 400")

if __name__ == '__main__':
    unittest.main(verbosity=2)
