import unittest\nfrom ml_model import create_model\n\nclass TestMLModel(unittest.TestCase):\n    def test_create_model(self):\n        model = create_model()\n        self.assertIsNotNone(model)\n    def test_train_model(self):\n        model = create_model()\n        self.assertIsNotNone(model)\n\nif __name__ == '__main__':\n    unittest.main()
\n    def test_train_model(self):\n        model = create_model()\n        self.assertIsNotNone(model)
