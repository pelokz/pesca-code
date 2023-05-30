import pyautogui
import random 

X_FISH = 156
Y_FISH = 78
RGB_FISH = (67, 166, 54)
X_AERODACTYL = 685
Y_AERODACTYL = 320
RGB_AERODACTYL= (67, 58, 78)

POKE_DEAD_POSITION = (744, 337) 
BP_LOOT_POSITION = (1233, 536)
LIST_ATACK = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
LIST_OCEAN_POSITION = [(682,154), (738,156), (793,155), (793,200)]
BATTLE_REGION = (1176, 405, 182, 75)
LOOT_POSITIONS = [(1194, 685)]  

USE_POKEBALL = True


def check_battle():
    battle = pyautogui,pyautogui.locateOnScreen('battle.PNG', confidence=0.9, region=BATTLE_REGION)
    if battle is None:
        return True
    return False

def click_fish():
    pyautogui.moveTo(X_FISH, Y_FISH)
    pyautogui.click()

def poke_atack():
    pyautogui.press(LIST_ATACK)

def get_loot():
    pyautogui.moveTo(POKE_DEAD_POSITION)
    pyautogui.click(button='secondary')
    pyautogui.sleep(0.8)
    pyautogui.keyDown('ctrl')
    
    for loot_position in LOOT_POSITIONS:
        pyautogui.moveTo(loot_position)
        pyautogui.click()
        pyautogui.moveTo(loot_position)
        pyautogui.click()
    
    pyautogui.keyUp('ctrl')
    pyautogui.click(clicks=5)


def use_fishing_rod():
    ocean_position = random.choice(LIST_OCEAN_POSITION)
    pyautogui.press('delete')
    pyautogui.moveTo(ocean_position)
    pyautogui.click()


MAX_ATTEMPT = 800
attempt = 0

while True:
    fish = pyautogui.pixelMatchesColor(X_FISH, Y_FISH, RGB_FISH)
    attempt = attempt + 1
    print(attempt)
    if fish:
        click_fish()
        pyautogui.sleep(1.5)
        poke_atack()
        pyautogui.sleep(2)
        get_loot()
        pyautogui.sleep(4)
        if not check_battle():
            poke_atack()
        use_fishing_rod()
        attempt = 0
    if attempt == MAX_ATTEMPT:
        use_fishing_rod()
        attempt = 0
        