from main import User, Password
from session import session



username_one = User(username="grndr", username_id=1)
username_two = User(username="mkrn", username_id=2)
username_three = User(username="kmst", username_id=3)
password_one = Password(password="vienasdutrys", user_id=1)
password_two = Password(password="keturipenkis", user_id=2)
password_three = Password(password="sesiseptyni", user_id=3)

session.add(username_one)
session.add(username_two)
session.add(username_three)
session.add(password_one)
session.add(password_two)
session.add(password_three)
session.commit()