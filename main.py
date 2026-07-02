import dearpygui.dearpygui as dpg

# --- App state ---
cookies = 0
cookies_per_click = 1

def on_cookie_click():
    global cookies
    cookies += cookies_per_click
    dpg.set_value("cookie_count", f"Cookies: {cookies}")

# --- Setup ---
dpg.create_context()

with dpg.window(label="Cookie Clicker", tag="main_window"):
    dpg.add_text("Cookies: 0", tag="cookie_count")
    dpg.add_button(label="Click the cookie!", callback=on_cookie_click, width=200, height=100)

dpg.create_viewport(title="Cookie Clicker", width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_window", True)  # makes the window fill the viewport
dpg.start_dearpygui()
dpg.destroy_context()