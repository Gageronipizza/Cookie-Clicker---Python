import dearpygui.dearpygui as dpg
import time
import sys

# --- App state ---
cookies = 0
cookiesPerClick = 1
cookiesPerSecond = 0


#shop
shopItems = [
    #item, price, owned, benefit
    "cursor", 0, 15, 0,
    "farm", 0, 0, 0]



#system variables
sessionRunTime = 0
overallRunTime = 0


def shutdown_game():
    sys.exit(f"Bye")

def update_screen():
    dpg.set_value("cookie_count", f"Cookies: {cookies}")
    dpg.set_item_label("shop_cursor", f"Cursor: {shopItems[shopItems.index("cursor") + 2]}")






def on_cookie_click():
    global cookies
    cookies += cookiesPerClick
    update_screen()




def shop(item):
    print(f"attempt at purchase")
    global cookies
    global cookiesPerSecond
    if item == 1 and cookies >= 15:
        cookiesPerSecond += 0.1
        cookies -= 15



















# --- Display Setup ---
dpg.create_context()

with dpg.window(label="Cookie Clicker", tag="main_window"):
    dpg.add_text("Cookies: 0", tag="cookie_count")
    dpg.add_text("Cookies Per Click: 1", tag="cookies_per_click")
    dpg.add_text("Cookies Per Second: 0", tag="cookies_per_second")
    dpg.add_button(label="Click the cookie!", callback=on_cookie_click, width=200, height=100)

    with dpg.menu_bar():
        dpg.add_button(label="Cookie", callback=on_cookie_click)

        with dpg.menu(label="Shop"):
            dpg.add_menu_item(label="Cursor: 0", tag="shop_cursor", callback=lambda: shop(1))
            dpg.add_menu_item(label="Grandma: 0", tag="shop_grandma", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Farm: 0", tag="shop_farm", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Mine: 0", tag="shop_mine", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Factory: 0", tag="shop_factory", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Bank: 0", tag="shop_bank", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Temple: 0", tag="shop_temple", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Wizard Tower: 0", tag="shop_wizard_tower", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Shipment: 0", tag="shop_shipment", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Alchemy Lab: 0", tag="shop_alchemy_lab", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Portal: 0", tag="shop_portal", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Time Machine: 0", tag="shop_time_machine", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Antim. Condenser: 0", tag="shop_antim_condenser", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Prism: 0", tag="shop_prism", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Chancemaker: 0", tag="shop_chancemaker", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Fractal Engine: 0", tag="shop_fractal_engine", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Javascript Console: 0", tag="shop_javascript_console", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Idleverse: 0", tag="shop_idleverse", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="Cortex Baker: 0", tag="shop_cortex_baker", callback={"this is a temp placeholder"})
            dpg.add_menu_item(label="You: 0", tag="shop_you", callback={"this is a temp placeholder"})
            
        with dpg.menu(label="Upgrades"):
            dpg.add_menu_item(label="Show Logger")
            dpg.add_menu_item(label="Show About")

        with dpg.menu(label="Oddities"):
            dpg.add_button(label="A Button")
            dpg.add_simple_plot(label="Menu plot", default_value=(0.3, 0.9, 2.5, 8.9), height=80)

        dpg.add_button(label="Leave", callback=shutdown_game)

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



        
        
        
        
        
        print(f"Session Run Time: {sessionRunTime}")
        print(f"Precision Time: {overallRunTime}")
        print(f"{last_tick}")



        update_screen()
        last_tick = now

    dpg.render_dearpygui_frame()  # <-- draws this frame; must run every loop

dpg.destroy_context()