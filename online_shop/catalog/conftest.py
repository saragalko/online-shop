EVERYTHING_EQUALS_NOT_NONE = type('omnieq', (), {"__eq__": lambda x, y: y is not None})()
