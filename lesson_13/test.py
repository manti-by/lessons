from faker import Faker

fake = Faker()

# name() -> str
fake.name()  # Jorge Sullivan

# city() -> str
fake.city()  # New-York

# pyint(min_value: int = 0, max_value: int = 9999, step: int = 1) -> int
fake.pyint()  # 6311
