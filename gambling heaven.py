import tkinter as tk
from PIL import Image, ImageTk
import random
import sys
import os

window = tk.Tk()
window.title('version 0.75')
window.geometry("1200x800")
window.resizable(False, False)

def resource_path(relativePath):
    try:
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath('.')

    return os.path.join(basePath, relativePath)

numList = [0,0,0]
points = 1000
counts = {'menuOpen':False,'aniCount': 0,'winCount':0,'shopOpen':False,'leverPulled':False,'chip':0,'buyAni':False,'round':1,'spins':0,'textStart':False,'speaker':True,'nextText':0}
winType = ['small win','normal win','big win','you lost']
names = ['@gaia_gallifrey - Voice Actor','@mediumenemyspider - Voice Actor','@imagiknight - Artist','@endless_g - Play Tester','@a_31_minutos_fan - Play Tester','@Kiernbr - GamePlay Programmer / Director']

inventory = []
stats= {'goodLuck':1,'badLuck':1}


startMenu = tk.Frame(window, bg = 'teal', bd =4)
startMenu.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.6,relheight=0.6)

startBTN = tk.Button(startMenu, text= 'start', command = lambda: main_menu('start'))
startBTN.pack()

creditBTN = tk.Button(startMenu, text= 'credits', command = lambda: main_menu('credits'))
creditBTN.pack()

creditsMenu = tk.Frame(window, bg = 'teal', bd =4)
for i in range(6):
    c = tk.Label(creditsMenu,text = names[i],font= ('Arial',15))
    c.pack(side='top')
    
credBack = tk.Button(creditsMenu,text='back',command= lambda: main_menu('back'))
credBack.pack()

def main_menu(btn):
    if btn == 'start':
        startMenu.place_forget()
        opening_cinematic()
        
    elif btn == 'credits':
        startMenu.place_forget()
        creditsMenu.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.6,relheight=0.6)
        
    elif btn == 'back':
        creditsMenu.place_forget()
        startMenu.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.6,relheight=0.6)


def opening_cinematic():
    MC_sprite = Image.open(resource_path('assets/playersilhouette000.png'))
    uknown_sprite = Image.open(resource_path('assets/trustworthyman000.png'))

    diolauges = {'diolauge1':['Man this place sucks,','not even a spike in my heart rate',f'I need something to really get the blood pumping'],
                 'diolauge2':['Hey friend! Bored?','I can help with that….',f"As long as you don't mind handing your life over to fate."],
                 'diolauge3':["What's the game?"],
                 'diolauge4':['Oh nothing crazy, just slots.'],
                 'diolauge5':['Really? Just slots?','That sounds boring as hell'],
                 'diolauge6':["Oh don't worry out of everything you will feel while playing….","I guarantee boredom isn't one of them."],
                 'diolauge7':['You know what you sound like, a trustworthy distant voice!','How do I play?'],
                 'diolauge8':['Great! All you must do is enter the back room','Use the black door by the managers office'],
                 'diolauge9':['Great…']}

    cinematicBG = tk.Frame(window,bg = 'yellow',bd = 4)
    cinematicBG.place(width = 1200,height=800)
    
    MC_sprite = MC_sprite.resize((200,300))
    MC_sprite = ImageTk.PhotoImage(MC_sprite)

    uknown_sprite = uknown_sprite.resize((200,300))
    uknown_sprite = ImageTk.PhotoImage(uknown_sprite)

    textBox = tk.Frame(cinematicBG, bg='grey',bd=4)
    textBox.place(relx=0.2,rely=0.8,anchor='nw',relwidth=0.6,relheight=0.15)

    textDisplay = tk.Label(textBox,font = ('Arial',25),wraplength=700,justify='left')
    textDisplay.pack(side= 'left',anchor='nw')

    MC = tk.Label(cinematicBG, image = MC_sprite,bg='yellow')
    MC.image = MC_sprite
    MC.place(relx=0,rely=1.05,anchor='sw')

    uknown = tk.Label(cinematicBG, image = uknown_sprite, bg='yellow')
    uknown.image = uknown_sprite
    
    skip = tk.Button(cinematicBG,text='skip',command=lambda: skip_btn())
    skip.pack(side='top',anchor='ne')

    def skip_btn():
        cinematicBG.place_forget()
        game()
    
    global temp,textCount,currentIndex 
    
    temp = ''
    textCount = 0

    counts['nextText'] = list(diolauges.keys())
    currentIndex = 0
    
    def opening_text(text,count = 0):
        global temp,textCount,speaker,currentIndex

        if currentIndex >= len(counts['nextText']):
            cinematicBG.place_forget()
            game()
            return
        
        if count == 0:
            if counts['textStart'] == True:
                return
            
        currentKey = counts['nextText'][currentIndex]
        
        if textCount  >= len(diolauges[currentKey]):
            return

        if counts['speaker'] == True:
           textDisplay.config(fg = 'blue')

        elif counts['speaker'] == False:
            textDisplay.config(fg = 'red')
            uknown.place(relx=0.01*101,rely=1.05,anchor='se')

        counts['textStart'] = True

        currentLine = diolauges[currentKey][textCount]

        if count < len(currentLine):
            temp += currentLine[count]
            textDisplay.config(text = temp)
            window.after(50,opening_text,text,count + 1)

        else:
            temp = ''
            textCount += 1
            counts['textStart'] = False
            
            if textCount >= len(diolauges[currentKey]):
                textCount = 0
                currentIndex += 1
                if counts['speaker'] == True:
                    counts['speaker'] = False

                elif counts['speaker'] == False:
                    counts['speaker'] = True
                
                if currentIndex >= len(counts['nextText']):
                  return


    textDisplay.bind('<Button-1>',lambda e:opening_text(counts['nextText']))
    textBox.bind('<Button-1>',lambda e:opening_text(counts['nextText']))
    
    opening_text(counts['nextText'])
        

def game():
    #slot screen stuff
    slotM_sprite = Image.open(resource_path('assets/Slot_Machine000.png'))

    slotScreen = tk.Canvas(window)
    slotScreen.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.6,relheight=0.6)

    window.update()
        
    resized = slotM_sprite.resize((slotScreen.winfo_width(), slotScreen.winfo_height()),Image.NEAREST)
    slotScreen.img = ImageTk.PhotoImage(resized)
    
    slotScreen.place_configure(relwidth = 0.9)
    window.update()
    
    slotScreen.create_image(slotScreen.winfo_width()//2,slotScreen.winfo_height()//2,image = slotScreen.img,anchor='center')

    def show_slot_screen():
        winScreen.place_forget()
        slotScreen.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.9,relheight=0.6)
        bottomStuff.place(relx=0.2,rely=0.8,anchor='nw',relwidth=0.6,relheight=0.15)


    #make slot numbers
    numberSheet = Image.open(resource_path('assets/Slot_Numbers000.png'))

    digitWidth = numberSheet.width
    digitHeight = numberSheet.height // 12

    numberImages = []
    
    slotScreen.place_configure(relwidth = 0.9)
    window.update()
    
    canvasWidth = slotScreen.winfo_width()
    canvasHeight = slotScreen.winfo_height()

    displayWidth = max(1,canvasWidth // 6)
    displayHeight = max(1,canvasHeight // 4)


    
    for i in range(12):#reads the sprite sheet and creats the images
        top = i * digitHeight
        bottom = (i+1)* digitHeight

        digit = numberSheet.crop((0,top,digitWidth,bottom))
        digit = digit.resize((displayWidth-50, displayHeight-50),Image.NEAREST)

        numberImages.append(ImageTk.PhotoImage(digit))
        
    slotScreen.place_configure(relwidth = 0.6)
    window.update()
        
    #display numbers
    reels = []
    spacing = canvasWidth // 6
    positions = [spacing*1.05, spacing*2.01, spacing*2.95]#locations in the canvas
    
    for x in positions:
        img = slotScreen.create_image(x + 180,canvasHeight // 2,image=numberImages[0])
        reels.append(img)
        
    
    #win screen
    winScreen = tk.Frame(window,bg = 'red', bd=4)
    winText = tk.Label(winScreen, text  = '',font= ('Arial',100))
    winText.pack(expand=True)

    #display info
    pointDisplay = tk.Label(window, text = f'{points}',font= ('Arial',50),bg='red')
    pointDisplay.place(anchor= 'nw')

    displayRound = tk.Label(window, text = f'round [{counts["round"]}]',font= ('Arial',50),bg='red')
    displayRound.place(y = 80)

     #make the lever
    leverSheet = Image.open(resource_path('assets/lever000.png'))
    leverFrames = []

    frameWidth = leverSheet.width // 4
    frameHeight = leverSheet.height

    leverWidth = canvasWidth // 8
    leverHeight = canvasHeight // 2

    scale = 3

    newWidth = int(frameWidth * scale)
    newHeight = int(frameHeight * scale)
    
    for i in range(5):
        left = i * frameWidth 
        right = (i + 1) * frameWidth

        frame = leverSheet.crop((left, 0, right, frameHeight))
        frame = frame.resize((newWidth, newHeight),Image.NEAREST)
        
        leverFrames.append(ImageTk.PhotoImage(frame))

    lever = slotScreen.create_image(canvasWidth -leverWidth // 2*2.85 , canvasHeight //2.18, image = leverFrames[0])
    slotScreen.tag_raise(lever)
    def lever_animation(frame = 0):

        if frame == 0:
            if counts['leverPulled']:
                return
        
        counts['leverPulled'] = True
            
        if frame < 5:
            slotScreen.itemconfig(lever, image = leverFrames[frame])
            window.after(100,lever_animation, frame+1)
        else:
            roll_animation()
            slotScreen.itemconfig(lever, image = leverFrames[0])
            
    slotScreen.tag_bind(lever, '<Button-1>', lambda e: lever_animation(0))
    slotScreen.place_configure(relwidth = 0.9)
    window.update()
    #bottom stuff
    bottomStuff = tk.Frame(window,bg= 'green',bd=4)
    bottomStuff.place(relx=0.2,rely=0.8,anchor='nw',relwidth=0.6,relheight=0.15)

    shopButton = tk.Button(bottomStuff, text = 'shop',command=lambda: open_shop())
    shopButton.place(anchor = 'nw')
    
    #shop
    shopBG_sprite = Image.open(resource_path('assets/Circuit_shop000.png'))

    
    shopScreen = tk.Canvas(window)

    def draw_shop_bg(event=None):
        spriteResize_shop = shopBG_sprite.resize((shopScreen.winfo_width(),shopScreen.winfo_height()),Image.NEAREST)
        shopScreen.bg_img = ImageTk.PhotoImage(spriteResize_shop)
        shopScreen.delete('bg')
        shopScreen.create_image(shopScreen.winfo_width()//2,shopScreen.winfo_height()//2,image=shopScreen.bg_img)
        shopScreen.tag_lower('bg')
        shopScreen.tag_raise('chip')

    shopScreen.bind('<Configure>',draw_shop_bg)
    
    #make chips 
    chips = []
    luckChip_sprite = Image.open(resource_path('assets/luckychip000.png'))
    luckChip = ImageTk.PhotoImage(luckChip_sprite)

    badLuckChip_sprite = Image.open(resource_path('assets/unluckychip001.png'))
    badLuckChip = ImageTk.PhotoImage(badLuckChip_sprite)

    chips.append(luckChip_sprite)
    chips.append(badLuckChip_sprite)

    shopImages = [ImageTk.PhotoImage(luckChip_sprite),ImageTk.PhotoImage(badLuckChip_sprite)]
    
    
    chipDisplay = shopScreen.create_image(300,200,image= shopImages[0], anchor='center',tags='chip')
    shopScreen.itemconfig(chipDisplay, state='hidden')

    buyBTN = tk.Button(shopScreen, text = 'buy random item', command = lambda: buy_animation())
    buyBTN.place(anchor='nw')
    def buy_animation(count = 0):
        global points
        
        if count == 0:
            if points > 500:
                if counts['buyAni']:
                    return

        counts['buyAni'] = True
                
        
        if count < 10:
            counts['chip'] = random.randint(0,1)
            shopScreen.itemconfig(chipDisplay, image = shopImages[counts['chip']],state='normal')
            window.after(100,buy_animation,count + 1)
        else:
            count = 0
            buy_item(chips[counts['chip']])
            shopScreen.itemconfig(chipDisplay,state='hidden')

    def open_shop():
        if counts['shopOpen'] == False:
            slotScreen.place_forget()
            shopScreen.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.6,relheight=0.6)
            counts['shopOpen'] = True
        else:
            counts['shopOpen'] = False
            shopScreen.place_forget()
            slotScreen.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.9,relheight=0.6)

    def buy_item(item):
        global points
        itemType = ''
        if item == chips[0]:
            stats['goodLuck'] += 5
            itemType = 'good'
        elif item == chips[1]:
            stats['badLuck'] += 5
            itemType= 'bad'
            
        points -= 500
        pointDisplay.config(text= f'{points}')
        counts['buyAni'] = False
        inventory.append(item)
        new_item(itemType)
        
    #inventory
    inventoryMenu = tk.Canvas(window,bg='blue',bd=4)
    inventoryMenu.place(relx=0.0,rely=0.5,anchor='w',relwidth=0.2,relheight=0.6)
    
    inventoryImages =[]
    inventoryText = {}
    
    global inventory_index
    inventory_index = 0
    
    global currentItem
    currentItem = None
    
    def boost_text(event):
        global currentItem

        items = inventoryMenu.find_withtag('current')

        if currentItem and currentItem in inventoryText:
            inventoryMenu.itemconfig(inventoryText[currentItem], state = 'hidden')
            currentItem = None
        if not items:
            return

        item = items[0]

        if item in inventoryText:
            inventoryMenu.itemconfig(inventoryText[item], state = 'normal')
            currentItem = item
            
    inventoryMenu.bind('<Motion>',boost_text)
    
    def new_item(itemType):
        global inventory_index
        window.update()

        cols = 3

        row = inventory_index // cols
        col = inventory_index % cols
        
        w = inventoryMenu.winfo_width() // 4
        h = inventoryMenu.winfo_height() // 6

        x = 45 + col * 70
        y = 70 + row * 90

        resized = inventory[-1].resize((w,h),Image.NEAREST)
        img = ImageTk.PhotoImage(resized)
        inventoryImages.append(img)
        
        item = inventoryMenu.create_image(x,y,image = img)
        
        if itemType == 'good':
            boostText = inventoryMenu.create_text(x,y-40, text = '+5 good luck',state='hidden')

        elif itemType == 'bad':
            boostText = inventoryMenu.create_text(x,y-40, text = '+5 bad luck',state='hidden')

        inventoryMenu.itemconfig(boostText, tags=('tooltip',))            
        inventoryText[item] = boostText
        
        inventory_index += 1

    def lose_screen():
        slotScreen.place_forget()
        displayRound.place_forget()
        pointDisplay.place_forget()
        winScreen.place_forget()
        inventoryMenu.place_forget()
        
        loseScreen = tk.Frame(window,bg = 'teal', bd =4)
        
        loseText = tk.Label(loseScreen, text = 'your soul is no longer yours, the machine owns you now',font= ('Arial',40), wraplength=1000, justify='center')
        loseText.pack(expand=True)

        loseScreen.place(relx=0.5, rely=0.5, anchor='center', relwidth=1, relheight=1)
           
    #roll animation--slot Screen
    def roll_animation(count = 0):
        if count == 3:
            count = 0
        weights = [1] * 12
        for i in range(1,6):
            weights[i] = stats['badLuck']
            
        for i in range(6,12):
            weights[i] = stats['goodLuck']
            
        newNumbers = []
        bottomStuff.place_forget()
        winScreen.place_forget()
        slotScreen.place(relx=0.5,rely=0.5,anchor='center',relwidth=0.9,relheight=0.6)
        counts['aniCount'] += 1
        if counts['aniCount'] < 10:
            for i in range(3):
                numList[i] = random.choices(list(range(12)), weights=weights)[0]
                slotScreen.itemconfig(reels[i],image= numberImages[numList[i]])
            window.after(100,roll_animation,(count + 1)%3)
        else:
            counts['aniCount'] = 0
            window.after(1000,calc_win)

    #calculates how many points the player gets        
    def calc_win():
        global points
            
        slotScreen.place_forget()
        
        if all(num == numList[0] for num in numList) == True:
                points = points + (100*numList[0])
                
                if (100*numList[0]) == 100:
                    counts['winCount'] = 0
                    
                elif (100*numList[0]) == 300:
                    counts['winCount'] = 1

                elif (100*numList[0]) >= 300:
                    counts['winCount'] = 2
        else:
            counts['winCount'] = 3
            points -= 100
            
        winText.config(text = f'{winType[counts["winCount"]]}',bg= 'red')
        pointDisplay.config(text=f'{points}')
        winScreen.place(relx=0.5,rely=0.5,anchor='center')
        
        counts['leverPulled'] = False
        counts['spins'] += 1
        
        if counts['spins'] == 5:
            counts['round'] += 1
            displayRound.config(text=f'round [{counts["round"]}]')
        if points <= 0:
            lose_screen()
        else:    
            window.after(700,show_slot_screen)
        
    
window.mainloop()
