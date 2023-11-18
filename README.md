# project_reality_scripts

Версии питона
в бф2 2.3.4
в пр 2.7

Мы будем использовать 2.7

1. Как комуницировать
2. Как запускать свой питон код в пре
1. Создать папку, назвать как хочу, создать внутри пустой __init__.py для того чтобы сделать модуль, который можно будет использовать в последующем в игре.
2.

```python
 # ------------------------------------------------------------------
 #
 # PROJECT REALITY SERVER INIT
 #
 # This file can be edited by any server (public or private).
 #
 import realityinit

 realityinit.init(False)  # Switch to True if using debugger executables (PRLauncher.exe will automatically modify this value accordingly)

 # ------------------------------------------------------------------
 # Add your custom script's initilization below
 
 import my_module_name
```

 ПО ПУТИ - C:\Project Reality\Project Reality BF2\mods\pr\python\game

 !test_command - команда которая будет запускать модуль
 !admins

Map change Pattern

1. Tickets < 100
2. Make vote
3. choose maps
4. set map

```python
def debugMessage(msg):
    host.rcon_invoke('echo "%s"' % (str(msg)))
 
def debugIngame(msg):
    #debugMessage(msg)
    try:
        host.rcon_invoke('game.sayAll "%s"' % (str(msg)))
    except:
        host.rcon_invoke('echo "debugIngame(FAIL): %s"' % (str(msg)))
```

```python
# ------------------------------------------------------------------------
# onChatMessage
# Callback that managing chat messages.
##########################################################################
# !NEVER call any messages directly from onChatMessage handler
# It causing inifite loop and game hangs
##########################################################################
# ------------------------------------------------------------------------
def onChatMessage(playerId, text, channel, flags):

    # fix for local non-dedicated servers
    if playerId == -1:
        playerId = 255

    # getting player object by player index
    player = bf2.playerManager.getPlayerByIndex(playerId)

    # standart check for invalid players
    if player is None or player.isValid() is False:
        return

    # common way to filter chat message
    # clearing text as any channel except Global are prefixed
    text = text.replace('HUD_TEXT_CHAT_COMMANDER', '')
    text = text.replace('HUD_TEXT_CHAT_TEAM', '')
    text = text.replace('HUD_TEXT_CHAT_SQUAD', '')
    text = text.replace('HUD_CHAT_DEADPREFIX', '')
    text = text.replace('* ', '')
    text = text.strip()

    # splitting filtered message text to arguments
    args = text.split(' ')

    if args[0] == C.COMMANDKEY:
        del args[0]
        if len(args) == 0:
            debugMessage('NO ARGS IN CHAT MSG')
            return
        commandHandler(player, args)
    else:
        pass
```

Useful links:
<https://web.archive.org/web/20070301124121/http://bf2tech.org/index.php/Learning_Python>
<https://web.archive.org/web/20061201183739/http://www.bf2tech.org/index.php/Big_Picture>
<https://web.archive.org/web/20070224121315/http://bf2tech.org/index.php/Event_Reference>
<https://web.archive.org/web/20070612145128/http://bf2tech.org/index.php/Object_Reference#Event_Handler_Methods>
