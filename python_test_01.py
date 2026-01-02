print("hello python")
print("안녕 파이썬")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"이 레스토랑의 이름은 {self.restaurant_name}이며, 요리는 {self.cuisine_type}입니다.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 레스토랑이 문을 열었습니다!")

Restaurant1 = Restaurant("맛있는 집", "한식")
Restaurant1.describe_restaurant()
Restaurant1.open_restaurant()
Restaurant2 = Restaurant("Delicious Place", "Italian")
Restaurant2.describe_restaurant()
Restaurant2.open_restaurant()

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"사용자 이름: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"안녕하세요, {self.first_name} {self.last_name}님!")           

User1 = User("철수", "김")
user2 = User("John", "Doe")
User1.describe_user()
User1.greet_user()
user2.describe_user()
user2.greet_user()

