import dearpygui.dearpygui as dpg
import time
import sys

# --- App state ---
cookies = 0.00
cookiesPerClick = 1.00
cookiesPerSecond = 0.00


#shop
shopItems = [
    #item, price, owned, benefit
    "cursor", 15, 0, 0.1,
    "grandma", 100, 0, 1,
    "farm", 1100, 0, 8,
    "mine", 12000, 0, 47,
    "factory", 130000, 0, 260,
    "bank", 1400000, 0, 1400,
    "temple", 20000000, 0, 7800
    ]



#system variables
sessionRunTime = 0
overallRunTime = 0

shopPrice = 1
shopOwned = 2
shopBenefit = 3


def shutdownGame():
    sys.exit(f"Bye")

def updateScreen():
    dpg.set_value("cookie_count", f"Cookies: {cookies}")
    dpg.set_value("cookies_per_click", f"Cookies Per Click: {cookiesPerClick}")
    dpg.set_value("cookies_per_second", f"Cookies Per Second: {cookiesPerSecond}")

    dpg.set_item_label("shop_cursor", f"Cursor: {shopItems[shopItems.index("cursor") + shopOwned]} Price: {shopItems[shopItems.index("cursor") + shopPrice]}")







def onCookieClick():
    global cookies
    cookies += cookiesPerClick
    updateScreen()




def shop(item):
    print(f"attempt at purchase")
    global cookies
    global cookiesPerSecond
    if item == 1 and cookies >= shopItems[shopItems.index("cursor") + 1]:
        cookies -= shopItems[shopItems.index("cursor") + shopPrice]
        shopItems[shopItems.index("cursor") + shopPrice] = round(shopItems[shopItems.index("cursor") + shopPrice] * 1.15)
        shopItems[shopItems.index("cursor") + shopOwned] += 1
        cookiesPerSecond += shopItems[shopItems.index("cursor") + shopBenefit]
    

    updateScreen()



















# --- Display Setup ---
dpg.create_context()

with dpg.window(label="Cookie Clicker", tag="main_window"):
    dpg.add_text("Cookies: 0", tag="cookie_count")
    dpg.add_text("Cookies Per Click: 1", tag="cookies_per_click")
    dpg.add_text("Cookies Per Second: 0", tag="cookies_per_second")
    dpg.add_button(label="Click the cookie!", callback=onCookieClick, width=200, height=100)

    with dpg.menu_bar():
        dpg.add_button(label="Cookie", callback=onCookieClick)

        with dpg.menu(label="Shop"):
            dpg.add_menu_item(label="Cursor: 0", tag="shop_cursor", callback=lambda: shop(1))
            dpg.add_menu_item(label="Grandma: 0", tag="shop_grandma", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Farm: 0", tag="shop_farm", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Mine: 0", tag="shop_mine", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Factory: 0", tag="shop_factory", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Bank: 0", tag="shop_bank", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Temple: 0", tag="shop_temple", callback={"this is a temp placeholder"})
            
        with dpg.menu(label="Upgrades"):
            dpg.add_menu_item(label="Show Logger")
            dpg.add_menu_item(label="Show About")

        with dpg.menu(label="Oddities"):
            dpg.add_button(label="A Button")
            dpg.add_simple_plot(label="Menu plot", default_value=(0.3, 0.9, 2.5, 8.9), height=80)

        dpg.add_button(label="Leave", callback=shutdownGame)

dpg.create_viewport(title="Cookie Clicker", width=1100, height=850)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_window", True)  # makes the window fill the viewport

#main game loop
last_tick = time.time()

while dpg.is_dearpygui_running():
    now = time.time()
    
    # only increment game-time counters once per real second
    if now - last_tick >= 1.0:
        sessionRunTime += 1
        overallRunTime += 1



        #game variables
        cookies += cookiesPerSecond



        
        
        
        
        
        print(f"Session Run Time: {sessionRunTime}")
        print(f"Precision Time: {overallRunTime}")
        print(f"{last_tick}")



        updateScreen()
        last_tick = now

    dpg.render_dearpygui_frame()  # <-- draws this frame; must run every loop

dpg.destroy_context()