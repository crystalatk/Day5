# This allows me to use different # of nights stayed at the hotel for the checkout:)
import random

# Artwork for initializing the game
hotel_front = '''
                ****Welcome to hotel DC****
 Where the beds are hard-coded and the cookies are always warm!



 888             888           888      88888888         888888
 888             888           888      888    888     888    888
 888             888           888      888     888   888      """
 88888b.  .d88b. 888888 .d88b. 888      888      888 888
 888 "88bd88""88b888   d8P  Y8b888      888       888888
 888  888888  888888   88888888888      888       888888
 888  888Y88..88PY88b. Y8b.    888      888       888 888      nnn
 888  888 "Y88P"  "Y888 "Y8888 888      88888888888P    888888888
 ||                             ||      ||                     ||
|-----------------------------------------------------------------|
|=================================================================|
|U-U-U-U-U-U-U-U-U-U-U-U-U-U->>ooOoo<<-U-U-U-U-U-U-U-U-U-U-U-U-U-U|
---|                                                           |---
    |    ========             =======             ========    |
    |   ||      ||         //   ||    \\\         ||      ||   |
    |   ||      ||       //     ||     \\\        ||      ||   |
    |   ||      ||      ||      ||      ||       ||      ||   |
    |   ||      ||      ||      ||      ||       ||      ||   |
    |   ==========      ||     o||o     ||       ==========   |
    |     88888         ||      ||      ||          88888     |
    |     88  88        ||      ||      ||         88   ""    |
    |     88   88       ||      ||      ||         88   __    |
    ------888888------------------------------------88888---------
                         \                \\
                          \                \\
                           \                \\
                            \                \\


'''

# Artwork for room assigned message upon check-in
hotel_room = '''


o(=(=(=(=)=)=)=)o
 !!!!!!}!{!!!!!!                                                ___
 !!!!!} | {!!!!!                                               /   \\
 !!!!}  |  {!!!!     _!_     ()              ()     _!_       | //  |
 !!!'   |   '!!!    |~@~|    ||______________||    |~@~|      |     |
 ~@~----+----~@~    |___|    |                |    |___|       \___/
 !!!    |    !!!      |      |      ~@@~      |      |       _________
 !!!    |    !!!     ( )     |_______  _______|     ( )     |____-____|
 !!!____|____!!!  __(___)__  {__~@~__}{__~@~__}  __(___)__  |____-____|
 !!!=========!!!   |__-__|   %%%%%%%%%%%%%%%%%%   |__-__|   |____-____|
_!!!_________!!!___|_____|_ %%%%%%%%%%%%%%%%%%%% _|_____|___|____-____|_
                   |     | %%%%%%%%%%%%%%%%%%%%%% |     |   |/       \|
                          %%%%%%%%%%%%%%%%%%%%%%%%
                         %%%%%%%%%%%%%%%%%%%%%%%%%%
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%
                       /!!!!!!!!!!!!!!!!!!!!!!!!!!!!\\
                       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                       !!!!!!!!!!!!!!!!!!!!!!!!!!lc!!
                       `======~@~==========~@~======`
                      `==============================`
                     `====~@~==================~@~====`
                    `==================================`
                   `==~@~==========================~@~==`

'''

# This function creates random nights stayed, randomizes the amount paid, and also creates artwork for the receipt.
# -parameter needed is the room being checked out of.


def room_receipt(room):
    total = random.randrange(237, 2370, 237)
    nights = format(total/237, ".0f")
    cash = str(random.randrange(total + 1, total + 9))
    change = int(cash) - int(total)
    if total > 999:
        receipt = f'''
+-------------------------------------+
|                                     |
|              Hotel  DC              |
|                                     |
|         1640 Riverside Drive        |
|            Hill Valley, CA          |
|               867-5309              |
|                                     |
|  Room {room}                $ 237      |
|                                     |
| # of nights               {nights}         |
|                                     |
|  TOTAL                    $ {str(total)}    |
|  Cash                     $ {cash}    |
|  Change Due               $ {change}       |
|                                     |
|  Item Count:  1                     |
|                                     |
|             THANK YOU!         :D_C:|
+-------------------------------------+
'''
    else:
        receipt = f'''
+-------------------------------------+
|                                     |
|              Hotel  DC              |
|                                     |
|         1640 Riverside Drive        |
|            Hill Valley, CA          |
|               867-5309              |
|                                     |
|  Room {room}                $ 237      |
|                                     |
| # of nights               {nights}         |
|                                     |
|  TOTAL                    $ {str(total)}     |
|  Cash                     $ {cash}     |
|  Change Due               $ {change}       |
|                                     |
|  Item Count:  1                     |
|                                     |
|             THANK YOU!         :D_C:|
+-------------------------------------+
'''
    return receipt


room_receipt(231)
