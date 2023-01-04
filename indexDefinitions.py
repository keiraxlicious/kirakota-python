"""
The database will be organized as such.
Commands
    Extensions: Such as...
        lavalink for musicbot
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    Games
        Battle Ships
        RPG
        Fishing
        Rock Paper Scissors
        Cat Girls
        Waifus
        Husbandos - request >.<
    Help
        Template for each:
            Moderation Commands
            General Commands
            Games
                Listeners
                    levels
                        skills
                            Runescape Combat Skills
                                Hitpoints
                                Attack
                                Strength
                                Defence
                                Ranged
                                Magic
                                Prayer
                                Summoning
                                    Skiller Skills Go Here
                                    Herblore... etc...
                    on member
                        join
                        leave
                        ban
                        update-status
                    on message
                        commands
                        statements
                        typing
                    on react
                        give role
                        remove role
                        resets reactions and gives prompts
                    on ready
                        startup
                            logging
                            member count
                            verify all servers cached are the same still
                    on voice state update
                        create one of these:
                            Streaming
                                give new temp role, no one else can join
                                temp role can be assigned to others by stream leader
                            Collab
                                give new temp role, others w/ same role can join. 
                                    temp role can be assigned to others by collab leader
                            Apex
                            Fortnite
                            Valorant
                            Vibing
                            Cool Kids
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
                            Support
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
                            Watch Party
                            Cool Kids
                            Vibin
                        Some will create a temp text channel
                        once all participants leave, temp channel is deleted.
            Slash Commands
                    General
                        "I'm lost,"
                            Creates temporary text channel for the user.
                            give option to select friends, support, stream. 
                            removes access to channel, adds correct role w/ permissions.
                            if user picks " I joined from a friend of Keira's"
                                gives "Worthless Role"
                                    Must Have 500 hours to get promoted from Worthless to a General Channel
                    Members
                        Can drag general users from "Drag Me / Waiting Room" into Member Chat Channels
                        .General Command Removed.
                        "Ping" -Pong
                        "Rock Paper Scissors"
                        "BattleShip"
                        "Skills"
                            set current skill, can check combat level, skill level, and set current task to level up.
                        "fishing"
                        "leaderboards"
                        Access to self-promo
                        Access to tier 1 list promo
                        
                        .
                    Cool Kids
                        .Members +
                        Can Drag people into the Cool Kids Channels.
                        Access to Member Skills
                        Access to PvP
                        Access to Raid Leading
                        Access to General Announcements.
                        Access to Making polls for themselves.
                        Access to Tier 2 list promo
                        .
                    Moderators
                        .Cool Kids +
                        Can Ban / Kick / Timeout Users
                        Can Delete / Purge Messages
                        Can Post Announcements on my behalf.
                        Can Create Polls
                        Can Post Giveaways on my behalf.
                        Access to mod channels.
                        Listed as a Mod below Tier 1 and Tier 2 Promo, but have access to it when LIVE
                        .
                    Administrative
                        .Moderators +
                        Can add/remove/reset points if a skill is broken or a user is abusing the system.
                        Listed as Admin below Tier 1 and Tier 2 Promo, but have access to it when LIVE
                        .


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
Intelligent commands I want to make..
general terms I need...
message.id, role.id, emoji(''), invites-keys
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

Role Swap
once member joins, give role.id1,
    once member accepts roles by reacting to a message.id w/emoji('')
        remove role.id1 and assign role.id2

invite roles
    if user joins via invite-key1
        give temp-role.id1
            welcome person based on role to respective welcome channel.
    if user joins via invite-key2
        give temp-role.id2
            welcome person based on role to respective welcome channel.
    if user joins via invite-key3
        give temp-role.id3
            welcome person based on role to respective welcome channel.

Set Logging channel
    select channel to receive logs.
    send message on every event.

role reacts
    role reacts need to be setup like this...
        command input to bind to message,
            select role.id select message.id
                await react
                    bind react emoji to role.b



Status Updates
    Streamers
        if user is LIVE and their current role contains one of the Friend roles
            give them Friend-Live-role.id
        if user is LIVE and their current role contains one of the Support roles
            give them Support-Live-role.id
        if user is LIVE and their current role contains one of the Streaming Community roles
            give them CreatorsCoterie-Live-role.id

Status Reminders
    Send message to one of four chats for this.
        Friends get a going live channel.
        cool kids get a live channel and a noti sent to u by dm


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
            CreatorsCoterie Community
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    emoji('')
        gives role.id-Gamer
    emoji('')
        gives role.id-Member
    emoji('')
        gives role.id-WatchParty
    emoji('')
        gives role.id-Apex
    emoji('')
        gives role.id-Fortnite
    emoji('')
        gives role.id-Sea of Thieves
    emoji('')
        gives role.id-Terraria
    emoji('')
        gives role.id-Valorant
    emoji('')
        gives role.id-Vibin
    emoji('')
        gives role.id-Cool Kids
    emoji('')
        gives role.id-Moderators
    emoji('')
        gives role.id-Admins
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
            Support Community
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    emoji('')
        gives role.id-Gamer
    emoji('')
        gives role.id-Member
    emoji('')
        gives role.id-Support
    emoji('')
        gives role.id-Cool Kids
    emoji('')
        gives role.id-Moderators
    emoji('')
        gives role.id-Admins
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
            Friends Community
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    emoji('')
        gives role.id-Gamer
    emoji('')
        gives role.id-Member
    emoji('')
        gives role.id-WatchParty
    emoji('')
        gives role.id-Apex
    emoji('')
        gives role.id-Fortnite
    emoji('')
        gives role.id-Sea of Thieves
    emoji('')
        gives role.id-Terraria
    emoji('')
        gives role.id-Valorant
    emoji('')
        gives role.id-Vibin
    emoji('')
        gives role.id-Cool Kids
    emoji('')
        gives role.id-Moderators
    emoji('')
        gives role.id-Admins
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
            Bonus Rooms
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    emoji('')
        gives role.id-Collabs
    emoji('')
        gives role.id-Streaming
    emoji('')
        gives role.id-Keira's Room




























"""
