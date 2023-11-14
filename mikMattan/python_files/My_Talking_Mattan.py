import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import snake
import starfighters_battle
import starfighters_battle_bot

lst_of_games = ["Snake", "Star-fighters battle"]
lst_of_food = ['Acorn squash', 'Alfalfa sprouts', 'Almond milk', 'Almonds', 'Amaretto', 'Anchovies', 'Apples',
               'Apricots', 'Artichokes', 'Asparagus', 'Avocado', 'Bacon', 'Bagels', 'Baked beans', 'Baked potato',
               'Baklava', 'Banana bread', 'Bananas', 'Barbecue sauce', 'Basil', 'Bay leaves', 'Beans', 'Beef', 'Beer',
               'Beets', 'Bell peppers', 'Berries', 'Biscuits', 'Black beans', 'Black-eyed peas', 'Blackberries',
               'Blue cheese', 'Blueberries', 'Bok choy', 'Bologna', 'Boston lettuce', 'Bourbon', 'Bran', 'Bread',
               'Breadfruit', 'Breakfast sausage', 'burger', 'hamburger', 'schnizel', 'shawarma', 'Brie cheese',
               'Broccoli', 'Broccoli rabe', 'Brown rice', 'Brussels sprouts', 'Buckwheat', 'Buffalo', 'Bulgur',
               'Burrito', 'Butter', 'Buttermilk', 'Butternut squash', 'Cabbage', 'Cactus pear', 'Caesar dressing',
               'Calamari', 'Camembert cheese', 'Candied yams', 'Canned fruit', 'Cannellini beans', 'Capers', 'Caramel',
               'Caraway seeds', 'Cardamom', 'Carrots', 'Cashews', 'Cassava', 'Catfish', 'Cauliflower', 'Caviar',
               'Celery', 'Chai tea', 'Chard', 'Cheddar cheese', 'Cheese', 'Cherimoya', 'Cherries', 'Chervil',
               'Chestnuts', 'Chicken', 'Chicken breast', 'Chicken salad', 'Chickpeas', 'Chives', 'Chocolate',
               'Chocolate chips', 'Chorizo', 'Chutney', 'Cilantro', 'Cinnamon', 'Clams', 'Coconut', 'Coconut milk',
               'Cod', 'Coffee', 'Cognac', 'Collard greens', 'Concord grapes', 'Cookies', 'Coriander', 'Corn',
               'Corn syrup', 'Corned beef', 'Cottage cheese', 'Couscous', 'Crab', 'Cranberries', 'Cranberry sauce',
               'Cream', 'Cream cheese', 'Creamed spinach', 'Creme brulee', 'Cucumbers', 'Cumin', 'Curry',
               'Curry powder', 'Custard', 'Daikon', 'Dates', 'Deli meat', 'Dill', 'Doughnuts', 'Dragonfruit', 'Duck',
               'Dumplings', 'Edam cheese', 'Edamame', 'Egg noodles', 'Eggplant', 'Eggs', 'Endive', 'English muffin',
               'Enoki mushrooms', 'Espresso', 'Falafel', 'Farfalle', 'Farro', 'Fava beans', 'Fennel', 'Feta cheese',
               'Fettuccine', 'Figs', 'Filet mignon', 'Fish', 'Flank steak', 'Flaxseed', 'Flatbread', 'Flour', 'Fondue',
               'French beans', 'French bread', 'French fries', 'French onion soup', 'French toast', 'Fresh herbs',
               'Fried chicken', 'Fried rice', 'Frittata', "Frogs' legs", 'Fudge', 'Garam masala', 'Garlic',
               'Garlic bread', 'Gazpacho', 'Gelato', 'Ghee', 'Ginger', 'Gnocchi', 'Goat cheese', 'Goat meat',
               'Gouda cheese', 'Graham crackers', 'Granola', 'Grapefruit', 'Grapes', 'Gravy', 'Greek yogurt',
               'Green beans', 'Green onions', 'Green tea', 'Grits', 'Ground beef', 'Ground turkey', 'Guacamole',
               'Gumbo', 'Halibut', 'Ham', 'Hamburger', 'Haricot verts', 'Hazelnuts', 'Herbs de Provence',
               'Hoisin sauce', 'Honey', 'Honeydew', 'Horseradish', 'Hot chocolate', 'Hot dogs', 'Hot sauce', 'Hummus',
               'Ice cream', 'Irish cream', 'Italian dressing', 'Jalapenos', 'Jam', 'Jambalaya', 'Jasmine rice',
               'Jerk chicken', 'Kale', 'Ketchup', 'Key lime pie', 'Kiwi', 'Kohlrabi', 'Kombucha', 'Korean barbecue',
               'Lamb', 'Lamb chops', 'Lasagna', 'Leeks', 'Lemon', 'Lemonade', 'Lentils', 'Lettuce', 'Licorice',
               'Lima beans', 'Lobster', 'Lox', 'Mackerel', 'Mac', 'adamia nuts', 'Macaroni', 'Macarons', 'Malt vinegar',
               'Mango', 'Maple syrup', 'Margarine', 'Marinara sauce', 'Marjoram', 'Marshmallows', 'Mascarpone cheese',
               'Matzo', 'Meatballs', 'Meatloaf', 'Melon', 'Meringue', 'Mesclun', 'Milk', 'Mint', 'Miso', 'Molasses',
               'Monkey bread', 'Mozzarella cheese', 'Muesli', 'Muffins', 'Mulberries', 'Mussels', 'Mustard',
               'Nectarines', 'Neuchatel cheese', 'Noodles', 'Nutella', 'Oatmeal', 'Oats', 'Omelet', 'Onion rings',
               'Onions', 'Orange juice', 'Oranges', 'Oregano', 'Oysters', 'Pad Thai', 'Paella', 'Pancakes', 'Panini',
               'Papaya', 'Paprika', 'Parmesan cheese', 'Parsley', 'Parsnips', 'Passionfruit', 'Pasta', 'Pastrami',
               'Pate', 'Pavlova', 'Peaches', 'Peanut butter', 'Peanuts', 'Pears', 'Peas', 'Pecans', 'Peking duck',
               'Penne', 'Pepper', 'Pepper jack cheese', 'Peppermint', 'Pepsi', 'Pesto', 'Pickles', 'Pico de gallo',
               'Pies', 'Pigs in a blanket', 'Pine nuts', 'Pineapple', 'Pistachios', 'Pizza', 'Plantains', 'Plum sauce',
               'Plums', 'Poached eggs', 'Pomegranates', 'Popcorn', 'Poppy seeds', 'Pork', 'Pork belly', 'Pork chops',
               'Pork ribs', 'Potato chips', 'Potatoes', 'Poutine', 'Pretzels', 'Prosciutto', 'Prunes', 'Pudding',
               'Pulled pork', 'Pumpkin', 'Pumpkin pie', 'Quiche', 'Quinoa', 'Radicchio', 'Radishes', 'Raisins',
               'Raspberries', 'Ravioli', 'Red cabbage', 'Red peppers', 'Red wine', 'Refried beans', 'Rhubarb', 'Rice',
               'Rice cakes', 'Ricotta cheese', 'Romaine lettuce', 'Rosemary', 'Rotisserie chicken', 'Rum', 'Rye bread',
               'Saffron', 'Sage', 'Sake', 'Salmon', 'Salsa', 'Salt', 'Saltine crackers', 'Sausages', 'Scallops',
               'Scrambled eggs', 'Seaweed', 'Sesame seeds', 'Shrimp', 'Smoked salmon', 'Smoothies', 'Snickers',
               'Snow peas', 'Sorbet', 'Sourdough bread', 'Soy milk', 'Soy sauce', 'Spaghetti', 'Spam', 'Spanish rice',
               'Sparkling water', 'Spicy chicken sandwich', 'Spinach', 'Split pea soup', 'Squash', 'Squid',
               'Sriracha sauce', 'Steak', 'Steamed vegetables', 'Strawberries', 'String beans', 'Stuffing',
               'Submarine sandwiches', 'Suckling pig', 'Sugar', 'Sunflower seeds', 'Sushi', 'Sweet and sour sauce',
               'Sweet potatoes', 'Swiss cheese', 'Swordfish', 'Syrup', 'Tabasco sauce', 'Tacos', 'Tangerines',
               'Tapioca pudding', 'Tartar sauce', 'Tater tots', 'Tea', 'Tempeh', 'Teriyaki sauce', 'Thai basil',
               'Thyme', 'Tilapia', 'Tiramisu', 'Tofu', 'Tomatoes', 'Tortellini', 'Tortilla chips', 'Truffles', 'Tuna',
               'Turkey', 'Turmeric', 'Turnips', 'Tzatziki sauce', 'Udon noodles', 'Vanilla', 'Veal', 'Vegan cheese',
               'Vegan ice cream', 'Vegetable juice', 'Vegetable soup', 'Veggie burgers', 'Vermicelli noodles',
               'Vermouth', 'Vinegar', 'Vodka', 'Waffles', 'Walnuts', 'Wasabi', 'Water chestnuts', 'Watermelon',
               'Wheat bread', 'Whipped cream', 'Whiskey', 'White chocolate', 'White wine', 'Whole grain bread',
               'Whole milk', 'Worcestershire sauce', 'Yakitori', 'Yellow squash', 'Yellowfin tuna', 'Yogurt', 'Ziti',
               'Zucchini']
lst_of_subjects = ["mathematics", "madait handasit", "physics", "history", "hebrew", "bible", "english", "literature"]

for i in lst_of_food:
    lst_of_food[lst_of_food.index(i)] = i.lower()


def help_mattan():
    print("Welcome to My Talking Mattan game!")
    print("Here is what you can do with mattan:")
    print("feed\ngym\nplay\nlearn\n")
    print("To get your mattan's data enter: get data")
    print("To exit and save, enter: exit")
    print()


class Mattan:
    def __init__(self, hunger=7, fun=3, pumped=3, iq=90):
        self.hunger = hunger
        self.fun = fun
        self.pumped = pumped
        self.iq = iq

    def __str__(self):
        return f"Hunger: {self.hunger}\nFun: {self.fun}\nPumped: {self.pumped}\nIQ: {self.iq}\n"

    def get_data(self):
        return self.hunger, self.fun, self.pumped, self.iq

    def check_pumped(self):
        if self.pumped < 2:
            print("Mattan wants to work out")
            print()

    def check_fun(self):
        if self.fun < 2:
            print("Mattan is bored")
            print()

    def check_hunger(self):
        if self.hunger > 15:
            print("Mattan is hungry!")
            print()

    def check_iq(self):
        if self.iq < 80:
            print("Mattan needs to learn!")
            print()

    def learn(self):
        subject = input("What subject you want Mattan to learn: ")

        while not (subject in lst_of_subjects):
            print("No such subject as", subject)
            subject = input("What subject you wan Mattan to learn: ")

        self.iq += len(subject)
        self.hunger += 3
        self.fun -= len(subject) // 2
        self.pumped -= 2
        print("Mattan is learning!")
        print("Now Mattan's IQ is", self.iq)
        print()

    def feed(self):
        if self.hunger < 3:
            print("Mattan is not hungry!")
            print()
            return None

        food = input("Enter food to eat: ")

        while not (food in lst_of_food):
            print("Mattan can't it this!")
            food = input("Enter food to eat: ")

        self.hunger -= len(food)
        self.pumped -= 2
        self.fun -= 2
        print("Mattan ate it, now his hunger is", self.hunger)
        print()

    def play(self):
        print("What game do you want to play with your Mattan?")
        for idx, game in enumerate(lst_of_games):
            print(f"{idx + 1}: {game}")

        choice_of_game = input("Enter what game to play: ")

        while (not choice_of_game.isdigit()) or 1 > int(choice_of_game) or int(choice_of_game) > len(lst_of_games):
            print("Invalid input")
            choice_of_game = input("Enter what game to play: ")
        print()
        choice_of_game = int(choice_of_game)
        if choice_of_game == 1:
            print("Move snake with arrows")
            print("Press start button to start the game")
            print()
            self.fun += snake.play() // 2
        else:
            print("Left player moves with w, a, s, d and shoots with left Ctrl")
            print("Right player moves with arrows and shoots with right Ctrl")
            print("Press screen to start game")
            print()
            single_player_choice = input("Do you want to play single player (y for yes, any other key for no): ")

            if single_player_choice == "y":
                bot_health, player_health = starfighters_battle_bot.main()
                self.fun += starfighters_battle.STARTER_HEALTH - bot_health + player_health
            else:
                yellow_player, red_player = starfighters_battle.main()
                self.fun += starfighters_battle.STARTER_HEALTH - yellow_player - red_player

        self.hunger += 3
        self.pumped -= 2
        self.iq -= 2
        print("Mattan is having fun!!!")
        print("Now his fun is", self.fun)
        print()

    def gym(self):
        self.pumped += 4
        self.hunger += 3
        self.fun += 1
        print("Mattan is working out! (also training legs)")
        print("Now his pumped level is", self.pumped)
        print()


print("Hello and welcome to the My Talking Mattan game!")
print()
print("""  
  __  __         _______    _ _    _               __  __       _   _              
 |  \/  |       |__   __|  | | |  (_)             |  \/  |     | | | |             
 | \  / |_   _     | | __ _| | | ___ _ __   __ _  | \  / | __ _| |_| |_ __ _ _ __  
 | |\/| | | | |    | |/ _` | | |/ / | '_ \ / _` | | |\/| |/ _` | __| __/ _` | '_ \ 
 | |  | | |_| |    | | (_| | |   <| | | | | (_| | | |  | | (_| | |_| || (_| | | | |
 |_|  |_|\__, |    |_|\__,_|_|_|\_\_|_| |_|\__, | |_|  |_|\__,_|\__|\__\__,_|_| |_|
          __/ |                             __/ |                                  
         |___/                             |___/ """)
print()
try:
    with open(r"C:\Talking Mattan\data_file.txt", "r") as data_file:
        lst_of_data = [int(i.split(',')[1]) for i in data_file.readlines()]
        my_mattan = Mattan(lst_of_data[0], lst_of_data[1], lst_of_data[2], lst_of_data[3])
    save = True

    print("Synced data successfully")
    print()
except FileNotFoundError:
    print("Hello new player")
    create_folder = input(
        r"Do you allow creating a folder for holding info about your progress (y, n)? (the folder will be located in C:\ dir) ")
    is_valid = create_folder in ('y', 'n')

    while not is_valid:
        create_folder = input("y or n: ")
        is_valid = create_folder in ('y', 'n')

    if create_folder == 'y':
        os.mkdir(r"C:\Talking Mattan")
        with open(r"C:\Talking Mattan\data_file.txt", 'w') as data_file:
            data_file.write("hunger,7\nfun,3\npumped,3\niq,90")

        save = True
    else:
        print("Ok, your progress won't be saved")
        save = False

    my_mattan = Mattan()

while True:
    did_something = False
    choice = input("What do you want to do with Mattan (for help enter: help): ")
    print()
    if choice == "play":
        my_mattan.play()
        did_something = True
    elif choice == "feed":
        my_mattan.feed()
        did_something = True
    elif choice == "gym":
        my_mattan.gym()
        did_something = True
    elif choice == "learn":
        my_mattan.learn()
        did_something = True
    elif choice == "exit":
        break
    elif choice == "help":
        help_mattan()
    elif choice == "get data":
        print(my_mattan)
    else:
        print("Mattan can't do that")
    if did_something:
        my_mattan.check_hunger()
        my_mattan.check_fun()
        my_mattan.check_pumped()
        my_mattan.check_iq()

if save:
    with open(r"C:\Talking Mattan\data_file.txt", 'w') as data_file:
        data_file.write("hunger,%d\nfun,%d\npumped,%d\niq,%d" % my_mattan.get_data())
