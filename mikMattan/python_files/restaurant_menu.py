import tkinter as tk
import pop_allert

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

for i in lst_of_food:
    lst_of_food[lst_of_food.index(i)] = i.lower()

TITLE_FONT_SIZE = 23
BTN_FONT_SIZE = 18
ENT_FONT_SIZE = 20

TITLE_FONT = ("Comic Sans MS", TITLE_FONT_SIZE)
ENT_FONT = ("David", ENT_FONT_SIZE)
BTN_FONT = ("Times New Roman", BTN_FONT_SIZE)

BC = "#61b52a"
BORDER_WIDTH = 7

ENT_WIDTH = 30
PAD_WIDGET = 20

DEFAULT_ENTRY_VALUE = "What would you like to order"


name = None


def execute_command(window, entry):
    global name

    name = entry.get()
    window.destroy()


def main():
    ##  window  ##
    window = tk.Tk()
    window.title("Restaurant menu")
    window.resizable(False, False)
    window.configure(background=BC)

    ##  url frame  ##
    url_frm = tk.Frame()
    url_frm.configure(background=BC)

    url_lbl = tk.Label(master=url_frm, text="Menu", font=TITLE_FONT, background=BC)
    name_ent = tk.Entry(master=url_frm, font=ENT_FONT, width=ENT_WIDTH)

    name_ent.insert(0, DEFAULT_ENTRY_VALUE)

    name_ent.bind("<FocusIn>", lambda event: name_ent.delete(0, tk.END))  # Bind event handler for clicking on the Entry

    url_lbl.pack(pady=PAD_WIDGET, padx=PAD_WIDGET)
    name_ent.pack(pady=PAD_WIDGET, padx=PAD_WIDGET)

    ## buttons frame ##
    btn_frm = tk.Frame()
    btn_frm.configure(background=BC)

    activate = tk.Button(master=btn_frm, text="Order", font=BTN_FONT, borderwidth=BORDER_WIDTH, command=lambda: execute_command(window, name_ent))

    activate.grid(padx=PAD_WIDGET, pady=PAD_WIDGET, row=0, column=0)

    ## place frames ##
    url_frm.pack()
    btn_frm.pack()

    window.bind("<Return>", lambda event=None: execute_command(window, name_ent))
    window.mainloop()

    if name == DEFAULT_ENTRY_VALUE:
        return None
    elif name in lst_of_food:
        return name

    pop_allert.pop_msg("Wtf", f"There is not food named {name}")
    return "error"


if __name__ == "__main__":
    main()
