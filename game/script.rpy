## First Week Frenzy: A College Survival Comedy
## A Ren'Py Visual Novel Game Script

################################################################################
## Initialization
################################################################################

init python:
    # Character Variables
    # These track relationship status with each character
    player_name = ""
    roommate_points = 0
    professor_points = 0
    love_interest_points = 0
    social_score = 0
    academic_score = 0
    mental_health = 10
    
    # Inventory Items
    has_textbook = False
    has_coffee_card = False
    has_dorm_key = False
    has_party_invite = False
    has_study_notes = False

################################################################################
## Images Declarations
################################################################################

# Characters
image roommate normal = "images/roommate normal.png"
image roommate happy = "images/roommate happy.png"
image roommate annoyed = "images/roommate annoyed.png"

image professor normal = "images/professor normal.png"
image professor impressed = "images/professor impressed.png"
image professor disappointed = "images/professor disappointed.png"

image love_interest normal = "images/love interest normal.png"
image love_interest happy = "images/love interest happy.png"
image love_interest flirty = "images/love interest flirty.png"
image love_interest sad = "images/love interest sad.png"

# Backgrounds
image bg dorm = "images/bg dorm.jpg"
image bg campus = "images/bg campus.jpg"
image bg classroom = "images/bg classroom.jpg"
image bg cafeteria = "images/bg cafeteria.jpg"
image bg library = "images/bg library.jpg"
image bg party = "images/bg party.jpg"

# Inventory Images
image item textbook = "images/item textbook.png"
image item coffee_card = "images/item coffee card.png"
image item dorm_key = "images/item dorm key.png"
image item party_invite = "images/item party invite.png"
image item study_notes = "images/item study notes.png"

################################################################################
## Character Declarations
################################################################################

define mc = Character("[player_name]", color="#5F9EA0", image="mc")
define rm = Character("Alex", color="#FF6347", image="roommate") # Your roommate
define prof = Character("Dr. Jenkins", color="#4682B4", image="professor") # Intimidating professor
define li = Character("Jaden", color="#9370DB", image="love_interest") # Potential love interest

################################################################################
## Start of Game
################################################################################

label start:
    $ player_name = renpy.input("What's your name?", length=20)
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Insert Name"
    
    # Initialize inventory
    $ has_dorm_key = True
    
    # Title screen narration
    scene black
    show text "First Week: College Survival" with dissolve
    pause 2.0
    hide text with dissolve
    
    # Game begins
    "Welcome to Freshman Year at the Best University, where dreams are made... and occasionally shattered."
    "You have got one week to prove yourself and set the tone for your entire college experience."
    "No pressure, right?"
    
    jump day1_morning

################################################################################
## Day 1 - Monday
################################################################################

label day1_morning:
    scene bg dorm with dissolve
    play music "audio/morning_ambience.mp3" fadein 1.0
    
    "DAY 1: MONDAY - MOVE-IN DAY"
    
    "You wake up in your new dorm room."
    "Your parents dropped you off yesterday, and reality is finally sinking in. You're on your own."
        
    mc "Well, this is it. Real college. Real freedom. Real... responsibility."
    
    show roommate normal at right with dissolve
    
    "The door swings open and in walks someone."
    
    rm "Oh hey! You must be [player_name]. I'm Carson, your roommate."
    
    menu:
        "Greet enthusiastically":
            $ roommate_points += 2
            $ social_score += 1
            
            mc "Hey Carson! Great to finally meet you! I was just unpacking."
            
            show roommate happy
            
            rm "Awesome attitude! I can already tell we're going to get along great."
            
            "Carson seems pleased with your friendly approach."
            
        "Give a casual greeting":
            $ roommate_points += 1
            
            mc "Hey, what's up? Nice to meet you."
            
            rm "Same! Looks like we'll be sharing this room for a year."
            
            "Carson seems pretty fine."
            
        "Continue unpacking without enthusiasm":
            $ mental_health -= 1
            
            mc "Oh, hi. I'm just trying to figure out where to put all my stuff."
            
            show roommate annoyed
            
            rm "Uh, okay. I guess I'll start unpacking on my side too."
            
            "Carson seems weird."
    
    rm "So, orientation starts in an hour. Are you planning to go?"
    
    menu:
        "Definitely! I want to learn everything about campus.":
            $ academic_score += 1
            $ social_score += 1
            
            mc "Absolutely! I want to meet people."
            
            show roommate happy
            
            rm "Same! We can head over together if you want."
            
            jump day1_orientation
            
        "I guess I should, but I'm not excited about it.":
            
            mc "Yeah, I probably should go, even though it'll be boring."
            
            rm "It might be, but they usually give out free stuff. Plus, it's a good way to meet people."
            
            jump day1_orientation
            
        "Skip it and finish unpacking":
            $ academic_score -= 1
            $ social_score -= 1
            $ roommate_points -= 1
            
            mc "I think I'll skip it and get my room set up. I can figure things out on my own."
            
            show roommate annoyed
            
            rm "Suit yourself. But they usually cover important stuff about classes and campus resources."
            
            jump day1_solo_unpacking

label day1_orientation:
    scene bg campus with dissolve
    
    "You and Alex head to the main quad where orientation is being held."
    "Hundreds of nervous freshmen are out, holding campus maps and schedules."
    
    show roommate normal at right
    
    rm "So many people! The whole freshman class must be here."
    
    show professor normal at center with dissolve
    
    "A professor steps up to the microphone."
    
    prof "Welcome to Best University, class of 2029. I'm Dr. Jenkins, Dean of First-Year Studies."
    
    prof "This week will determine much about your future here. Choose wisely how you spend your time."
    
    "As Dr. Jenkins talks on about academic policies, you notice someone in the crowd catching your eye."
    
    show love_interest normal at center with dissolve
    hide professor
    
    "They smile at you before turning their attention back to the presentation."
    
    rm "Earth to [player_name]! They're about to hand out our welcome packages."
    
    "You receive a campus map, your student ID, and a coupon book for local businesses."
    
    $ has_coffee_card = True
    "You got a Coffee Shop Punch Card! (Free drink after 5 purchases)"
    
    show love_interest normal at center
    
    "After the orientation wraps up, you see that interesting person again, standing alone and looking at their map."
    
    menu:
        "Go introduce yourself":
            $ social_score += 2
            $ love_interest_points += 2
            
            hide roommate
            show love_interest normal at right
            
            mc "Hey, are you as confused by this map as I am?"
            
            show love_interest happy
            
            li "Completely lost! I'm Jaden, by the way."
            
            mc "I'm [player_name]. Nice to meet you."
            
            li "You too! Are you headed to the department to meet all the faculty next?"
            
            mc "I was thinking about it. What's your major?"
            
            li "Psychology. Basic, I know."
            
            "You chat for a few minutes, and Jaden seems genuinely interested in getting to know you."
            
            li "Hey, I should go find my department, but maybe I'll see you around campus?"
            
            mc "I hope so!"
            
        "Ask your roommate about them":
            $ roommate_points += 1
            
            mc "Hey Alex, do you know who that is?"
            
            rm "Oh, that's Jaden. They're in my pre-orientation group. Want an introduction?"
            
            "Before you can answer, Jaden walks away to join another group."
            
            mc "Maybe next time."
            
        "Ignore them and focus on the orientation materials":
            $ academic_score += 1
            
            "You decide to focus on reviewing the orientation materials. Relationships can wait; academics come first."
            
            rm "Ready to check out the department faculty?"
    
    jump day1_evening

label day1_solo_unpacking:
    $ has_textbook = True
    
    "While organizing your desk, you find your Introduction to College Life textbook."
    "You got the Intro to College Life textbook!"
    
    "You spend the afternoon arranging your side of the room just how you like it."
    "It feels good to have your space set up, but you wonder what information you missed at orientation."
    
    "Alex returns a few hours later with a stack of papers and a free t-shirt."
    
    show roommate normal at right
    
    rm "You missed quite a bit. Professor Jenkins was talking about how important the first week is."
    rm "Oh, and they handed out these schedules. I grabbed one for you."
    
    "Alex hands you a class schedule and campus map."
    
    rm "There's a mandatory floor meeting tonight at 8. Our RA is going to go over dorm rules."
    
    jump day1_evening

label day1_evening:
    scene bg dorm with dissolve
    play music "audio/evening_ambience.mp3" fadein 1.0
    
    "DAY 1: MONDAY EVENING"
    
    "After a day full of orientation activities, you're back in your dorm room."
    "Your RA held a floor meeting where they went over all the rules."
    
    show roommate normal at right
    
    rm "So, what's your plan for the rest of the week? Classes don't start until Thursday."
    
    menu:
        "I want to explore campus and maybe join some clubs":
            $ social_score += 1
            
            mc "I think I'll check out the campus and see what clubs I might want to join."
            
            show roommate happy
            
            rm "Nice! There's a club fair tomorrow. We could go together if you want."
            
            mc "Sounds good to me."
            
        "I should probably get my textbooks and prepare for classes":
            $ academic_score += 1
            
            mc "I should probably hit the bookstore and get prepared before classes start."
            
            rm "Wow, so responsible, huh? The bookstore is usually quite hectic this week."
            
            mc "Better early than scrambling at the last minute."
            
        "I need to just relax and adjust before the stress begins":
            $ mental_health += 1
            
            mc "Honestly, I just want to take it easy before classes start."
            
            rm "I feel that. College can be a lot."
            
            mc "Exactly. Need to relax myself."
    
    "Your phone buzzes with an email notification."
    
    mc "Looks like Dr. Jenkins sent everyone a welcome email with a pre-class assignment."
    
    show roommate annoyed
    
    rm "n assignment before classes even start? That's not cool."
    
    "The email indicates you should read Chapter 1 of the Introduction to College Life textbook and write a short reflection on your goals."
    
    menu:
        "Do the assignment now":
            $ academic_score += 2
            $ professor_points += 2
            $ mental_health -= 1
            
            mc "I might as well get this done now."
            
            "You spend the evening reading and writing your reflection."
            
            if has_textbook:
                "Having your textbook already makes this much easier."
                $ academic_score += 1
            else:
                "You have to use the online preview of the textbook, which is missing some pages."
                $ academic_score -= 1
            
            "By the time you finish, it's late, but you feel good about completing your first college assignment."
            
        "Promise to do it tomorrow":
            $ mental_health += 1
            
            mc "I'll tackle that tomorrow when I'm not so tired."
            
            rm "Good call. First night of college should be about settling in, not homework."
            
            "You make a mental note to complete the assignment tomorrow."
            
        "Ignore it until class starts":
            $ academic_score -= 1
            $ professor_points -= 2
            
            mc "They can't seriously expect us to do work before classes even start. I'll deal with it later."
            
            rm "Bold strategy. Dr. Jenkins is known to be pretty strict, though."
            
            mc "I'll take my chances."
    
    "As you get ready for bed, you reflect on your first day of college."
    "There's a whole week ahead - full of possibilities, challenges, and important decisions."
    "Whatever happens, this first week will definitely set the tone for your freshman year."
    
    "You fall asleep wondering what tomorrow will bring."
    
    jump day2_morning

################################################################################
## Day 2 - Tuesday
################################################################################

label day2_morning:
    scene bg dorm with dissolve
    play music "audio/morning_ambience.mp3" fadein 1.0
    
    "DAY 2: TUESDAY MORNING"
    
    "You wake up to the sound of your roommate getting ready."
    
    show roommate normal at right
    
    rm "Morning! Sleep okay?"
    
    mc "Mmph..." 
    
    mc "The dorm beds are going to take some getting used to."
    
    rm "Tell me about it. I think my mattress is stuffed with concrete."
    
    rm "I'm heading to the dining hall for breakfast. Wanna join?"
    
    menu:
        "Go to breakfast with Alex":
            $ roommate_points += 1
            $ social_score += 1
            
            mc "Sure, I could use some coffee."
            
            rm "Perfect! I heard they have a waffle maker."
            
            jump day2_cafeteria
            
        "Skip breakfast and explore campus alone":
            $ mental_health += 1
            
            mc "I think I'll skip breakfast and explore the campus a bit on my own."
            
            rm "Suit yourself. I'll see you later then."
            
            jump day2_campus_exploration
            
        "Stay in bed a little longer":
            $ mental_health += 1
            $ academic_score -= 1
            
            mc "I'm going to sleep in a bit more."
            
            rm "Alright, sleepyhead."
            
            jump day2_late_start

label day2_cafeteria:
    scene bg cafeteria with dissolve
    
    "The dining hall is bustling with students."
    
    show roommate normal at center
    
    rm "Let's grab some food and then find a place to sit."
    
    "You load up your tray with what you hope is edible dining hall food."
    
    "As you look for a place to sit, you spot Dr. Jenkins at a table, reviewing some papers."
    
    show professor normal at right
    
    menu:
        "Sit far away from Dr. Jenkins":
            
            mc "Let's sit over there, away from the professor."
            
            "You and Alex find seats on the other side of the cafeteria."
            
            rm "Smart move. Who wants to eat with faculty staring at them?"
            
        "Sit near Dr. Jenkins to make a good impression":
            $ professor_points += 1
            $ academic_score += 1
            
            mc "Let's sit near Dr. Jenkins. Could be good to be noticed."
            
            "You and Alex sit at a table near the professor."
            
            "Dr. Jenkins looks up briefly and gives you a small nod of acknowledgment."
            
            rm "Making yourself known to the professors early, huh?"
    
    "As you're eating, you notice Jaden enter the dining hall, looking around for a place to sit."
    
    show love_interest normal at right
    
    menu:
        "Wave them over to join you":
            $ love_interest_points += 2
            $ social_score += 1
            
            "You wave to Jaden, gesturing for them to join your table."
            
            show love_interest happy
            
            li "Hey, thanks for the invite! It's [player_name], right?"
            
            mc "That's right! And this is my roommate, Alex."
            
            rm "Nice to meet you officially, Jaden."
            
            "The three of you chat over breakfast, and you find yourself especially enjoying Jaden's company."
            
            li "So what are you both up to today? I was thinking of checking out the club fair."
            
            rm "We were just talking about that!"
            
        "Pretend not to notice them":
            
            "You don't feel like social interaction right now."
            
            rm "Isn't that Jaden from orientation? They seem cool."
            
            mc "Yeah, maybe we'll run into them later."
    
    jump day2_club_fair

label day2_campus_exploration:
    scene bg campus with dissolve
    
    "You decide to take a solo walk around campus."
    "The university is bigger than it looked in the brochures."
        
    "As you're consulting your campus map, trying to locate the library, you hear a familiar voice."
    
    show love_interest normal at right with dissolve
    
    li "Lost already?"
    
    "It's Jaden from orientation, looking amused at your confusion."
    
    mc "Just doing some looking around."
    
    li "Sure you are. I'm heading to the library myself if you want a guide."
    
    menu:
        "Accept Jaden's help":
            $ love_interest_points += 2
            
            mc "A guide would be great, actually. Lead the way!"
            
            show love_interest happy
            
            li "Follow me. I did a campus tour during the summer, so I mostly know where I'm going."
            
            "As you walk to the library, you learn more about Jaden. They're from a small town, majoring in Psychology, and has an enthusiasm for college life."
            
            jump day2_library
            
        "Politely decline":
            
            mc "Thanks, but I'm enjoying getting lost on my own. It's part of the experience."
            
            li "I respect that! Maybe I'll see you at the club fair later? It's supposed to be in the main quad at noon."
            
            mc "Maybe! Thanks for the tip."
            
            "You continue your solo exploration, eventually finding your way to the library."
            
            jump day2_library_solo
    
label day2_late_start:
    scene bg dorm with dissolve
    
    "You doze for another hour before finally dragging yourself out of bed."
    "The dorm is quiet, with most students already out for the day."
        
    mc "So much for making the most of orientation week..."
    
    "Your stomach grumbles, reminding you that you missed breakfast."
    
    "You check your phone and see a message from Alex about a club fair happening at noon in the main quad."
    
    menu:
        "Head to the club fair":
            
            "You quickly get dressed and head out to catch the club fair."
            
            jump day2_club_fair
            
        "Go to the library to do Dr. Jenkins' assignment":
            $ academic_score += 2
            $ professor_points += 1
            
            "You decide to be responsible and get your pre-class assignment done at the library."
            
            jump day2_library_solo
            
        "Grab a late breakfast first":
            $ mental_health += 1
            
            "Food first, decisions later. You head to the cafeteria for a late breakfast."
            
            jump day2_late_breakfast

label day2_library:
    scene bg library with dissolve
    
    "Jaden leads you to the library, an impressive five-story building at the heart of campus."
    
    show love_interest normal at right
    
    li "And here we are! The intellectual heart of Best University."
    
    "The library is massive, with rows upon rows of books, study areas, and computer labs."
    
    li "Do you have any assignments yet? Dr. Jenkins already gave my class some reading."
    
    mc "Yeah, we have to read Chapter 1 of the Intro to College Life book and write a reflection."
    
    li "Classic Jenkins move. Want to work on it together? I was going to find a quiet spot and get it done."
    
    menu:
        "Study with Jaden":
            $ love_interest_points += 1
            $ academic_score += 2
            
            mc "That sounds great, actually."
            
            "You and Jaden find a quiet study room and work on your assignments together."
            
            "Jaden is focused but friendly, and you find yourself enjoying the companionable silence as you both work."
            
            $ has_study_notes = True
            "You got Study Notes! (Helps with future assignments)"
            
            li "That wasn't so bad, right? We should form a study group once classes start."
            
            mc "I'd like that."
            
        "Decline politely":
            $ academic_score -= 1
            
            mc "I think I'll check out the club fair first, but thanks for the offer."
            
            li "No problem! Maybe another time."
            
            "You leave the library and head toward the main quad."
            
            jump day2_club_fair
    
    li "I was thinking of checking out the club fair after this. Want to go together?"
    
    mc "Sure, let's do it."
    
    jump day2_club_fair

label day2_library_solo:
    scene bg library with dissolve
    
    "The library is impressive, with multiple floors of books, study spaces, and resources."
        
    "You find a quiet corner to work on Dr. Jenkins' assignment."
    
    if has_textbook:
        "Having your textbook with you makes the work go much faster."
        $ academic_score += 1
    else:
        "You have to use one of the library's reference copies of the textbook, which means you can't take notes directly in it."
    
    "As you're working, you notice Dr. Jenkins herself browsing the stacks nearby."
    
    show professor normal at right with dissolve
    
    menu:
        "Approach Dr. Jenkins":
            $ professor_points += 2
            
            "You gather your courage and approach the professor."
            
            mc "Excuse me, Dr. Jenkins? I'm [player_name] from your Intro to College Life class."
            
            prof "Ah, yes. One of the new freshmen. How are you finding the pre-class assignment?"
            
            mc "It's interesting! I especially like the section on building effective study habits."
            
            show professor impressed
            
            prof "I'm pleased to hear you're taking it seriously. Most students ignore the assignment until the last minute."
            
            "Dr. Jenkins seems impressed by your initiative."
            
            prof "I look forward to reading your reflection, [player_name]."
            
        "Continue working quietly":
            $ academic_score += 1
            
            "You decide not to disturb the professor and continue with your work."
            
            "Dr. Jenkins notices you studying her assigned material and gives you an approving nod as she passes by."
    
    $ has_study_notes = True
    "You completed your assignment and got Study Notes! (Helps with future assignments)"
    
    "After finishing your work, you check your phone and see it's almost time for the club fair."
    
    menu:
        "Go to the club fair":
            
            "You pack up your things and head to the main quad for the club fair."
            
            jump day2_club_fair
            
        "Keep exploring the library":
            $ academic_score += 1
            $ social_score -= 1
            
            "You decide to familiarize yourself with the library resources instead."
            
            "You discover the reserve section, the media lab, and the 24-hour study spaces."
            
            "By the time you finish your self-guided tour, the club fair is almost over."
            
            jump day2_evening

label day2_late_breakfast:
    scene bg cafeteria with dissolve
    
    "The cafeteria is nearly empty by the time you arrive, with just a few stragglers having late breakfasts like you."
        
    "You grab some cereal and a banana, the only breakfast options still available."
    
    "As you're eating, you notice Dr. Jenkins at a table nearby, reviewing some papers."
    
    show professor normal at right
    
    "She glances up and makes eye contact with you."
    
    prof "Ah, a late riser. Not the best habit to form in your first week of college."
    
    menu:
        "Apologize and explain":
            $ professor_points += 1
            
            mc "Sorry, Dr. Jenkins. Still adjusting to dorm life. I'll be more punctual when classes start."
            
            prof "See that you are. Creating good habits now will serve you well throughout your academic career."
            
            "She returns to her papers, but seems slightly less disapproving."
            
        "Make a joke of it":
            $ professor_points -= 1
            
            mc "Just practicing for those late-night study sessions I've heard so much about!"
            
            show professor disappointed
            
            prof "Humor is no substitute for discipline, I'm afraid."
            
            "She returns to her work with a slight frown."
            
        "Just nod and continue eating":
            
            "You give a respectful nod and continue eating your breakfast."
            
            "Dr. Jenkins returns to her papers, occasionally glancing your way."
    
    "After finishing your meal, you check the time and see the club fair should be starting soon."
    
    jump day2_club_fair

label day2_club_fair:
    scene bg campus with dissolve
    play music "audio/crowd_ambience.mp3" fadein 1.0
    
    "The main quad has been transformed into a colorful array of club tables, with enthusiastic student representatives trying to recruit new members."
        
    "You see clubs for everything imaginable: academic societies, sports teams, cultural groups, gaming clubs, and more."
    
    if roommate_points >= 2:
        show roommate happy at right with dissolve
        
        rm "Hey, [player_name]! Glad you made it. Any clubs catching your eye?"
        
    if love_interest_points >= 2:
        show love_interest happy at left with dissolve
        
        li "There you are! I've been checking out the Psychology Club, but there's so much else to see."
    
    "A colorful flyer catches your eye for a big welcome party happening Friday night."
    
    $ has_party_invite = True
    "You got a Party Invite! (For Friday's big campus party)"
    
    menu:
        "Focus on academic clubs":
            $ academic_score += 2
            $ social_score += 1
            
            "You decide to prioritize clubs related to your academic interests."
            
            "You sign up for email lists for the Honors Society, the Debate Club, and a major-specific study group."
            
            if professor_points >= 2:
                show professor impressed at right with dissolve
                
                "You spot Dr. Jenkins observing the club fair and she gives you an approving nod when she sees which tables you're visiting."
                
                $ professor_points += 1
            
        "Check out social and fun clubs":
            $ social_score += 2
            
            "You decide college should be fun too, so you explore the more social clubs."
            
            "You sign up for email lists for the Campus Activities Board, Outdoor Adventure Club, and the Film Society."
            
            if love_interest_points >= 2:
                li "The Film Society has a movie night every Thursday! We should go sometime."
                
                $ love_interest_points += 1
            
        "Join a mix of different clubs":
            $ academic_score += 1
            $ social_score += 1
            
            "You decide to keep your options open and check out a variety of clubs."
            
            "You sign up for email lists for an academic club, a volunteer organization, and a recreational sports league."
            
            if roommate_points >= 2:
                rm "Nice choices! I signed up for the intramural volleyball team too. We could be teammates!"
                
                $ roommate_points += 1
    
    "After exploring the club fair, you feel more connected to campus life and excited about the possibilities."
    
    jump day2_evening

label day2_evening:
    scene bg dorm with dissolve
    play music "audio/evening_ambience.mp3" fadein 1.0
    
    "DAY 2: TUESDAY EVENING"
    
    "After a full day of orientation activities, you return to your dorm room."
        
    if roommate_points >= 3:
        show roommate normal at right with dissolve
        
        rm "What a day! I'm already exhausted, and classes haven't even started yet."
        
        mc "Tell me about it. College is intense even without the academics."
        
        rm "Want to order a pizza and chill with some Netflix? I need to decompress."
        
        menu:
            "Accept the roommate bonding time":
                $ roommate_points += 2
                $ mental_health += 2
                
                mc "That sounds perfect, actually."
                
                show roommate happy
                
                "You and Alex spend the evening sharing pizza and watching a comedy, taking a much-needed break from college stress."
                
                rm "We should make this a tradition. Tuesday pizza nights!"
                
            "Decline politely":
                
                mc "I think I need some alone time tonight, but maybe another time?"
                
                rm "No problem. I get it - it's a lot to adjust to."
                
                "Alex watches shows with headphones while you have some quiet time to yourself."
    else:
        "Your roommate is out for the evening, giving you some quiet time to yourself."
        
        if has_study_notes == False and academic_score < 3:
            "You realize you still haven't done Dr. Jenkins' pre-class assignment."
            
            menu:
                "Do the assignment now":
                    $ academic_score += 1
                    $ professor_points += 1
                    $ mental_health -= 1
                    
                    "You spend the evening completing the reading and writing your reflection."
                    
                    $ has_study_notes = True
                    "You got Study Notes! (Helps with future assignments)"
                    
                "Put it off again":
                    $ academic_score -= 1
                    $ professor_points -= 1
                    
                    "You decide to procrastinate on the assignment again. You still have time before Thursday's class."
        else:
            "You take some time to relax and reflect on your first two days of college."
            
            menu:
                "Call home and check in with family":
                    $ mental_health += 2
                    
                    "You spend an hour on the phone with your family, sharing your experiences so far."
                    "Their familiar voices help ground you amid all the newness of college life."
                    
                "Browse social media and check out campus groups":
                    $ social_score += 1
                    
                    "You spend some time exploring campus social media pages and joining online groups."
                    "It helps you feel more connected to your new community."
                    
                "Review your schedule and plan for classes":
                    $ academic_score += 1
                    
                    "You organize your schedule and plan out your week, making sure you know where all your classes will be."
                    "Being prepared helps reduce your anxiety about starting classes."
    
    "As you get ready for bed, you think about your progress so far."
    
    if social_score >= 3:
        "You've been making good connections. College is as much about the people as the classes."
    elif academic_score >= 3:
        "You've been focused on academics. That dedication will serve you well when classes start."
    else:
        "You're still finding your balance between social life and academics. It's only day two, after all."
    
    "Tomorrow is another day of orientation, with departmental meetings and campus resources tours."
    "You fall asleep wondering what new experiences await you."
    
    jump day3_morning

################################################################################
## Day 3 - Wednesday
################################################################################

label day3_morning:
    scene bg dorm with dissolve
    play music "audio/morning_ambience.mp3" fadein 1.0
    
    "DAY 3: WEDNESDAY MORNING"
    
    "You wake up to the sound of your alarm, feeling more adjusted to dorm life."
        
    "Today's schedule includes departmental orientations and a resources fair."
    
    "Your phone buzzes with a reminder about your departmental meeting at 10 AM."
    
    menu:
        "Attend the departmental orientation":
            $ academic_score += 2
            
            "You decide to attend the departmental orientation to meet your professors and learn more about your major."
            
            jump day3_department
            
        "Skip departmental and go to the resources fair":
            $ social_score += 1
            
            "You decide to skip the departmental meeting and head straight to the resources fair to learn about campus services."
            
            jump day3_resources_fair
            
        "Sleep in and miss both":
            $ mental_health += 1
            $ academic_score -= 2
            $ social_score -= 1
            
            "You decide your sleep is more important than either event and turn off your alarm."
            
            jump day3_sleeping_in

label day3_department:
    scene bg classroom with dissolve
    
    "You arrive at your departmental orientation a few minutes early."
    "The room is filling up with other freshmen who share your academic interests."
    
    show professor normal at right with dissolve
    
    prof "Welcome, everyone! I'm Dr. Jenkins, and I'll be teaching many of your introductory courses."
    prof "Today we'll go over the department expectations, major requirements, and introduce you to key faculty."
    
    "As you listen to the presentation, you find yourself genuinely excited about your courses."
    
    "During a break, you notice Jaden from orientation is also in your department."
    
    show love_interest normal at center with dissolve
    
    li "Hey [player_name]! Same major, huh? Looks like we'll be seeing a lot of each other."
    
    menu:
        "Express enthusiasm about sharing classes":
            $ love_interest_points += 2
            
            mc "That's great! It'll be nice to have a familiar face in my classes."
            
            show love_interest happy
            
            li "Definitely! Maybe we could study together sometime? I always do better with a study buddy."
            
            mc "I'd like that!"
            
        "Keep the conversation casual":
            $ love_interest_points += 1
            
            mc "Oh hey, Jaden. Yeah, looks that way. How are you liking orientation so far?"
            
            li "It's a lot of information to take in, but I'm excited about the classes."
            
            mc "Same here."
            
        "Focus on the academic information":
            $ academic_score += 1
            
            mc "Hey. Did you catch what the professor said about the research opportunities? I was taking notes but missed that part."
            
            li "Oh, she mentioned there are first-year research positions available, but they're competitive. You have to apply by the third week of classes."
            
            mc "Thanks! I definitely want to look into that."
    
    "The orientation resumes, and you learn about course sequencing, academic resources, and department events."
    
    "Afterward, there's a small reception with refreshments where you can mingle with professors and other students."
    
    menu:
        "Network with professors":
            $ professor_points += 2
            $ academic_score += 1
            
            "You make a point to introduce yourself to several key professors in your department."
            
            "They seem impressed by your initiative and interest in their research areas."
            
            show professor impressed at right
            
            prof "It's refreshing to see a freshman so engaged already, [player_name]. I hope to see that enthusiasm in my class."
            
        "Socialize with other freshmen":
            $ social_score += 2
            
            "You focus on getting to know your fellow freshmen, figuring these will be your study partners and friends for the next four years."
            
            "You exchange contact information with several students who seem like they'd make good study group members."
            
            if love_interest_points >= 3:
                show love_interest happy at center
                
                li "I'm glad you're in this department too. I think we're going to have a great year."
                
                $ love_interest_points += 1
            
        "Grab refreshments and then leave early":
            $ mental_health += 1
            
            "You grab some cookies and punch, then slip out early. You've gotten the essential information, and social events drain your energy."
            
            "On your way out, you pick up some departmental brochures to review later."
    
    "After the departmental orientation, you check your schedule and see the campus resources fair is happening now in the main quad."
    
    jump day3_resources_fair

label day3_resources_fair:
    scene bg campus with dissolve
    
    "The main quad is filled with tables representing different campus resources: the writing center, health services, counseling, the gym, tutoring services, and more."
        
    "You wander around, collecting brochures and free swag from various tables."
    
    if roommate_points >= 3:
        show roommate normal at right with dissolve
        
        rm "Hey, [player_name]! Check out the recreation center table - they're giving out free water bottles and gym passes."
        
        "You and Alex explore the fair together, comparing notes on useful resources."
    
    "At the counseling center table, they're offering quick stress assessments."
    
    menu:
        "Take the stress assessment":
            $ mental_health += 2
            
            "You complete the brief assessment and chat with a counselor about managing college stress."
            
            "They give you some helpful tips and information about their services."
            
            "You feel more prepared knowing there's support available if you need it."
            
        "Skip the assessment but take their information":
            $ mental_health += 1
            
            "You take their brochure but pass on the assessment. It's good to know the resource exists if you need it later."
            
        "Avoid the counseling table entirely":
            
            "You decide to skip the counseling table completely. You're not interested in discussing mental health with strangers."
    
    "The financial aid office has a table with information about work-study jobs on campus."
    
    menu:
        "Inquire about work-study opportunities":
            $ academic_score += 1
            $ mental_health -= 1
            
            "You learn about various on-campus jobs that work with student schedules."
            
            "While a job would add to your workload, it would also provide valuable experience and extra income."
            
            "You pick up an application to consider your options."
            
        "Focus on other resources instead":
            
            "You decide not to add a job to your plate during your first semester."
            
            "Better to focus on adjusting to college academics and social life first."
    
    "By the time you finish exploring the resources fair, you've gathered a wealth of information about campus support services."
    
    jump day3_afternoon

label day3_sleeping_in:
    scene bg dorm with dissolve
    
    "You sleep until nearly noon, missing both the departmental orientation and the start of the resources fair."
        
    mc "Ugh, I can't believe I slept so late."
    
    "Your phone has several missed messages, including one from your roommate asking where you are."
    
    "You send a quick reply making an excuse about not feeling well."
    
    menu:
        "Rush to catch the end of the resources fair":
            $ social_score += 1
            
            "You quickly get dressed and hurry to the main quad, hoping to catch at least part of the resources fair."
            
            jump day3_resources_fair_late
            
        "Email your department apologizing for missing orientation":
            $ academic_score += 1
            $ professor_points += 1
            
            "You send a polite email to your department advisor apologizing for missing orientation and asking if there were any important materials you could pick up."
            
            "They respond with an understanding note and attach the orientation slides, asking you to stop by their office sometime this week."
            
            jump day3_afternoon
            
        "Write the day off entirely":
            $ mental_health += 1
            $ academic_score -= 1
            $ social_score -= 1
            
            "You decide that since you've already missed the morning events, you might as well take a personal day."
            
            "You spend a few hours catching up on social media and relaxing in your dorm."
            
            jump day3_afternoon

label day3_resources_fair_late:
    scene bg campus with dissolve
    
    "You arrive at the resources fair as it's winding down. Many tables are already packing up."
        
    "You quickly make your way around the remaining tables, grabbing whatever information and freebies you can."
    
    "The health services table is still fully set up, so you stop there."
    
    "The health services representative gives you information about the campus clinic, counseling services, and wellness programs."
    
    "She also mentions that they offer free flu shots next week, which might be a good idea with so many students living in close quarters."
    
    menu:
        "Sign up for a flu shot appointment":
            $ mental_health += 1
            
            "You put your name down for a flu shot appointment, figuring it's a smart precaution."
            
            "The representative gives you a reminder card and a small first aid kit as a freebie."
            
        "Take the information but don't commit":
            
            "You take their brochure but don't sign up for anything yet."
            
            "You want to see how your schedule shakes out before making appointments."
    
    "As you're about to leave, you spot your roommate at one of the last tables."
    
    show roommate normal at right with dissolve
    
    rm "Well, well, well. Look who finally decided to join the land of the living."
    
    mc "Yeah, sorry. Rough morning."
    
    rm "You missed a lot of good info, but I grabbed doubles of some stuff for you."
    
    $ roommate_points += 1
    
    "Alex hands you a folder with various campus resource brochures and a campus map with important locations highlighted."
    
    mc "Thanks, that's actually really helpful."
    
    rm "That's what roommates are for. Oh, and I signed us both up for the dorm mixer tonight. Hope that's cool."
    
    jump day3_afternoon

label day3_afternoon:
    scene bg campus with dissolve
    play music "audio/afternoon_ambience.mp3" fadein 1.0
    
    "DAY 3: WEDNESDAY AFTERNOON"
    
    "With the structured orientation events finished for the day, you have some free time this afternoon."
        
    menu:
        "Visit the campus bookstore":
            $ academic_score += 1
            
            "You decide to check out the campus bookstore to purchase any remaining textbooks or supplies you need."
            
            jump day3_bookstore
            
        "Explore the recreation center":
            $ mental_health += 1
            $ social_score += 1
            
            "You decide to check out the campus recreation center and maybe get in a workout."
            
            jump day3_rec_center
            
        "Relax in the dorm":
            $ mental_health += 2
            
            "After all the orientation activities, you decide to take some downtime in your dorm."
            
            jump day3_dorm_afternoon

label day3_bookstore:
    scene bg campus with dissolve
    
    "The campus bookstore is crowded with students hunting for textbooks and Best University merchandise."
        
    "You navigate the textbook section, checking your course list against the shelves."
    
    if academic_score >= 4:
        "Thanks to your early preparation, you already have most of your books, but you pick up a few supplies and a planner."
    else:
        "You're later than most students, so some of the used textbooks are already gone, forcing you to buy the more expensive new copies."
        $ mental_health -= 1
    
    "As you're browsing, you spot Dr. Jenkins examining a book display near the academic journals."
    
    show professor normal at right with dissolve
    
    menu:
        "Approach Dr. Jenkins":
            $ professor_points += 1
            
            mc "Hello, Dr. Jenkins. I'm [player_name], from your department."
            
            if professor_points >= 3:
                show professor impressed
                
                prof "Ah, yes. You've been quite proactive during orientation. Looking forward to having you in class."
                
                $ professor_points += 1
            else:
                prof "Hello. I hope you're preparing adequately for the start of classes tomorrow."
                
                mc "Yes, just picking up my remaining books and supplies."
                
                prof "Good. Being prepared is the first step to academic success."
            
        "Avoid interaction":
            
            "You decide not to bother the professor during her personal time and continue your shopping."
            
            "You notice her glance your way, but she returns to her browsing without approaching."
    
    "At the checkout, you bite the bullet and also buy a Best University hoodie, even though it's ridiculously overpriced."
    "Might as well look the part of a college student."
    
    jump day3_evening

label day3_rec_center:
    scene bg campus with dissolve
    
    "The campus recreation center is an impressive facility with a gym, pool, basketball courts, and various fitness studios."
        
    "You take a self-guided tour, noting the different amenities available to students."
    
    "In the main gym area, you spot Jaden using one of the treadmills."
    
    show love_interest normal at right with dissolve
    
    menu:
        "Join them for a workout":
            $ love_interest_points += 2
            $ mental_health += 1
            
            "You grab a treadmill next to Jaden and start a casual jog."
            
            li "Hey, [player_name]! Glad to see I'm not the only freshman trying to avoid the 'Freshman 15'."
            
            mc "Just checking out the facilities, but figured I might as well get a workout in while I'm here."
            
            "You and Jaden exercise side by side, chatting between breaths. It's a nice way to get to know each other better."
            
            show love_interest happy
            
            li "We should make this a regular thing. Having a workout buddy would help me actually show up."
            
            mc "I'd be up for that!"
            
        "Wave but keep to yourself":
            $ love_interest_points += 1
            
            "You wave to Jaden but decide to explore the weight room instead of interrupting their workout."
            
            "They wave back with a smile before returning to their run."
            
            "After exploring the facility, you bump into Jaden in the lobby."
            
            li "Hey! Did you check out the rock climbing wall? It's supposed to be free for students on Fridays."
            
            mc "No, I missed that. Maybe we could check it out sometime?"
            
            li "Definitely!"
            
        "Avoid them and check out a different area":
            
            "You duck into the weight room before they notice you, preferring to explore on your own."
            
            "You spend some time checking out the equipment and fitness class schedule, noting a few that interest you."
    
    "After your visit to the rec center, you feel more energized and have a better understanding of the fitness options available on campus."
    
    jump day3_evening

label day3_dorm_afternoon:
    scene bg dorm with dissolve
    
    "You decide to take some downtime in your dorm room, away from the constant social interaction of orientation."
        
    "The quiet is nice after days of information overload and meeting new people."
    
    if academic_score < 3 and has_study_notes == False:
        "You realize you still haven't completed Dr. Jenkins' pre-class assignment, and classes start tomorrow."
        
        menu:
            "Complete the assignment now":
                $ academic_score += 1
                $ professor_points += 1
                
                "You spend a couple of hours reading the chapter and writing your reflection."
                
                "It's not your best work, but at least it's done before the first class."
                
                $ has_study_notes = True
                "You got Study Notes! (Helps with future assignments)"
                
            "Skip the assignment":
                $ academic_score -= 2
                $ professor_points -= 2
                
                "You decide to risk it and skip the pre-class assignment. How important could it really be?"
                
                "You can always make up an excuse or try to complete it before class tomorrow if needed."
    else:
        menu:
            "Call home":
                $ mental_health += 2
                
                "You video call your family and give them an update on your college experience so far."
                
                "Their familiar faces and enthusiasm about your adventures make you feel supported and less homesick."
                
            "Organize your desk and materials":
                $ academic_score += 1
                
                "You spend time organizing your desk, setting up your planner, and preparing your notebooks for classes tomorrow."
                
                "Being organized helps you feel more in control and ready for the academic challenges ahead."
                
            "Take a nap":
                $ mental_health += 2
                
                "You decide to catch up on sleep with an afternoon nap."
                
                "The orientation activities have been more exhausting than you expected, and the rest does you good."
    
    "Your roommate returns later in the afternoon."
    
    show roommate normal at right with dissolve
    
    rm "Hey, there's a dorm mixer tonight. Just casual games and pizza in the common room. Wanna go?"
    
    jump day3_evening

label day3_evening:
    scene bg dorm with dissolve
    play music "audio/evening_ambience.mp3" fadein 1.0
    
    "DAY 3: WEDNESDAY EVENING"
    
    "Your dorm is hosting a mixer for all the residents on your floor - a last social event before classes start tomorrow."
    
    show roommate normal at right
    
    rm "So, are you up for the mixer? Could be a good way to meet our neighbors."
    
    menu:
        "Go to the dorm mixer":
            $ social_score += 2
            $ roommate_points += 1
            
            mc "Sure, why not? Free pizza is always a good incentive."
            
            show roommate happy
            
            rm "That's the spirit! Plus, it's good to know who else lives on our floor."
            
            jump day3_mixer
            
        "Skip the mixer and prepare for classes":
            $ academic_score += 2
            
            mc "I think I'll skip it and make sure I'm fully prepared for classes tomorrow."
            
            rm "Your call. I'll bring you back a slice of pizza if there's any left."
            
            jump day3_prep_alone
            
        "Have a quiet evening with just your roommate":
            $ roommate_points += 2
            $ mental_health += 1
            
            mc "Actually, I'm kind of people'd out. Would you mind if we just hung out here instead?"
            
            rm "Not at all. We could order our own pizza and watch a movie or something."
            
            jump day3_roommate_bonding

label day3_mixer:
    scene bg dorm with dissolve
    
    "The dorm common room is decorated with balloons and streamers. Music plays from a speaker, and several pizzas are laid out on a table."
    
    show roommate normal at center
    
    "Your RA stands in the middle of the room, trying to get everyone's attention."
    
    "RA" "Alright everyone! Welcome to our floor mixer! Tonight is about getting to know your neighbors before we all get busy with classes."
    
    "She organizes a few icebreaker games, which are awkward but effective at getting people talking."
    
    "You meet several people from your floor, including some who share classes with you."
    
    if love_interest_points >= 3:
        show love_interest normal at right with dissolve
        
        li "Fancy seeing you here! Small campus, huh?"
        
        mc "Jaden! Do you live in this dorm too?"
        
        li "No, I'm in Westwood Hall, but my friend lives here and invited me along. Lucky coincidence!"
        
        menu:
            "Stick with Jaden for the evening":
                $ love_interest_points += 2
                
                "You and Jaden spend most of the mixer together, chatting and participating in games as a team."
                
                show love_interest happy
                
                li "I'm really glad I ran into you tonight. It's nice having someone I click with right away."
                
                mc "I feel the same way. Makes the whole college transition less intimidating."
                
            "Split your time between Jaden and meeting new people":
                $ love_interest_points += 1
                $ social_score += 1
                
                "You divide your attention between Jaden and meeting other residents from your floor."
                
                "It's a good balance of deepening one connection while also expanding your social circle."
                
                li "You're a natural at this socializing thing. I've been clinging to my one friend all night."
                
                mc "Just trying to meet my neighbors. We're all in the same boat, after all."
    else:
        "You make an effort to be social, introducing yourself to people and joining in the games."
        
        "By the end of the night, you've exchanged contacts with several new people and feel more connected to your dorm community."
    
    "As the mixer winds down, your RA reminds everyone that quiet hours will be strictly enforced starting tomorrow, as classes begin."
    
    rm "Not a bad night, right? I think I'm going to like living here."
    
    mc "Yeah, it was fun. But now I should probably get ready for tomorrow."
    
    jump day3_bedtime

label day3_prep_alone:
    scene bg dorm with dissolve
    
    "With your roommate at the mixer, you have the room to yourself to prepare for your first day of classes."
        
    "You check your schedule, locate your classrooms on the campus map, and organize your backpack."
    
    if has_study_notes:
        "You review your notes from Dr. Jenkins' pre-class assignment, feeling well-prepared for tomorrow."
        $ academic_score += 1
    else:
        "You feel a twinge of anxiety about not having completed the pre-class assignment, but try to focus on other preparations."
    
    "You set out your clothes for tomorrow and set multiple alarms to ensure you won't be late."
    
    "Your roommate returns as you're getting ready for bed."
    
    show roommate normal at right with dissolve
    
    rm "Hey, brought you some pizza as promised. How was your evening of scholarly preparation?"
    
    mc "Productive. I feel ready for tomorrow. How was the mixer?"
    
    rm "Pretty fun, actually. Made some new friends, played some ridiculous games. The usual college bonding stuff."
    
    "You chat for a bit about your schedules for tomorrow, discovering you have one class in the same building, though at different times."
    
    jump day3_bedtime

label day3_roommate_bonding:
    scene bg dorm with dissolve
    
    "You and Alex decide to skip the mixer in favor of a quieter evening together."
    
    show roommate normal at right
    
    "You order a pizza and pull up a movie on Alex's laptop."
    
    rm "So, nervous about classes starting tomorrow?"
    
    menu:
        "Admit you're nervous":
            $ roommate_points += 1
            $ mental_health += 1
            
            mc "Yeah, a bit. It's a big change from high school."
            
            show roommate happy
            
            rm "Same here. But hey, that's what everyone's feeling. We're all just pretending to have it together."
            
            "Your honest conversation helps ease some of your anxiety."
            
        "Play it cool":
            
            mc "Not really. Classes are classes, right? I'm sure it'll be fine."
            
            rm "Look at you, all confident. I'm low-key freaking out about my 8 AM calculus class."
            
            mc "Early classes are rough. Good luck with that."
            
        "Express excitement instead of nerves":
            $ academic_score += 1
            
            mc "I'm actually excited to finally start the real college experience. The orientation stuff is helpful, but I'm here to learn."
            
            rm "That's a healthy attitude. I'm trying to see it that way too, instead of stressing about workload."
            
            "You discuss your academic goals and interests, discovering you have complementary study habits that might work well for your shared living space."
    
    "As the evening progresses, you learn more about your roommate's background, interests, and quirks."
    
    "It's nice to have this one-on-one time to establish a foundation for your year of living together."
    
    rm "I'm glad we did this instead of the mixer. Don't get me wrong, I like parties, but sometimes you need the chill nights too."
    
    mc "Agreed. Balance is key for surviving college, from what I've heard."
    
    jump day3_bedtime

label day3_bedtime:
    scene bg dorm with dissolve
    
    "DAY 3: WEDNESDAY NIGHT"
        
    "As you get ready for bed, you can't help but feel a mix of excitement and nervousness about starting classes tomorrow."
    
    "You set your alarm, making sure you'll have plenty of time to get ready and find your first classroom."
    
    "Tomorrow is the real beginning of your college experience - the academics that you're actually here for."
    
    if mental_health <= 5:
        "You're feeling quite stressed about everything, but remind yourself that everyone is in the same boat."
        "Taking a few deep breaths, you try to calm your mind for sleep."
    elif mental_health >= 8:
        "Despite the normal first-day jitters, you're feeling pretty good about how orientation has gone."
        "You're confident you can handle whatever tomorrow brings."
    else:
        "You have the usual nerves about starting classes, but overall you feel like you're adjusting to college life."
        "You hope the connections and preparations you've made during orientation will serve you well."
    
    "You fall asleep thinking about what your first day of college classes will bring."
    
    jump day4_morning

################################################################################
## Day 4 - Thursday
################################################################################

label day4_morning:
    scene bg dorm with dissolve
    play music "audio/morning_ambience.mp3" fadein 1.0
    
    "DAY 4: THURSDAY MORNING"
    
    "Your alarm blares, signaling the start of your first day of actual college classes."
        
    "You get dressed and gather your materials, double-checking your schedule for your first class location."
    
    if roommate_points >= 4:
        show roommate normal at right with dissolve
        
        rm "Ready for the big day? Want to grab breakfast together before we head out?"
        
        menu:
            "Have breakfast with Alex":
                $ roommate_points += 1
                $ mental_health += 1
                
                mc "Sure, that sounds good. I could use the moral support."
                
                show roommate happy
                
                rm "Plus, they say never to start class on an empty stomach. Brain food and all that."
                
                "You head to the cafeteria together, chatting about your schedules and professors."
                
                rm "Good luck today! Text me how it goes."
                
            "Head straight to class":
                $ academic_score += 1
                
                mc "Thanks, but I want to get to class early to get a good seat."
                
                rm "No problem. Catch you later!"
                
                "You head out, your backpack filled with notebooks and your heart with determination."
    else:
        "Your roommate is still asleep, having lucked out with no early classes on Thursdays."
        
        "You quietly gather your things and head out, stopping to grab a coffee and granola bar from the campus café."
    
    scene bg campus with dissolve
    
    "The campus has a different energy today - more purposeful, less chaotic than orientation week."
    "Students stream toward academic buildings, coffees in hand, backpacks slung over shoulders."
    
    "You consult your map and make your way to your first class: Introduction to College Life with Dr. Jenkins."
    
    jump day4_first_class

label day4_first_class:
    scene bg classroom with dissolve
    
    "You arrive at Dr. Jenkins' classroom about 10 minutes early."
    "Some students are already there, claiming seats and arranging their notebooks."
        
    "You choose a seat in the second row - not too eager-looking, but still engaged."
    
    if love_interest_points >= 4:
        show love_interest normal at right with dissolve
        
        li "Mind if I sit here?"
        
        "Jaden gestures to the seat next to you, looking relieved to see a familiar face."
        
        mc "Please do! Glad we have this class together."
        
        show love_interest happy
        
        li "Same! Having allies makes everything less intimidating."
        
        "You both get settled as more students file in."
    
    show professor normal at center with dissolve
    
    "Precisely at the scheduled time, Dr. Jenkins walks in and sets her materials on the desk with practiced efficiency."
    
    prof "Good morning. Welcome to Introduction to College Life. I am Dr. Jenkins, as many of you know from orientation."
    
    prof "This course is designed to help you transition successfully to college-level academics and university life."
    
    "She begins taking attendance, making notes as she goes through the names."
    
    prof "Before we proceed to the syllabus, I'll collect the pre-class assignments I emailed everyone about."
    
    if has_study_notes:
        "You take out your completed assignment, feeling prepared and confident."
        
        prof "Please pass your papers forward."
        
        "When Dr. Jenkins gets to your paper, she gives a slight nod of approval."
        
        $ professor_points += 1
        $ academic_score += 1
    else:
        "Your stomach drops as you realize you never completed the assignment."
        
        menu:
            "Be honest about not doing it":
                $ professor_points -= 1
                $ academic_score -= 1
                $ mental_health -= 1
                
                "When your name is called, you admit you don't have the assignment."
                
                show professor disappointed
                
                prof "I see. Not the strongest start to your college career, [player_name]. I expect it on my desk by tomorrow morning."
                
            "Make up an excuse":
                
                mc "I'm so sorry, Dr. Jenkins. My computer crashed last night while I was finishing it. I have most of it done - could I email it to you this evening?"
                
                show professor disappointed
                
                prof "This is college, not high school. I expect better planning, including backups of your work. Have it to me by 5 PM today."
                
                "You sink slightly in your seat, feeling the weight of her disapproval."
                
            "Try to discreetly copy from someone else":
                
                "You glance around desperately, trying to see if you can quickly copy someone's work."
                
                if love_interest_points >= 4:
                    "Jaden notices and subtly slides their paper slightly toward you."
                    
                    menu:
                        "Copy Jaden's work":
                            $ love_interest_points += 1
                            $ honesty_score -= 2
                            $ academic_integrity -= 2
                            
                            "You hastily scribble down some answers from Jaden's paper."
                            "When papers are collected, you hand yours in with a nervous smile."
                            
                            show professor normal
                            
                            "Dr. Jenkins takes it without comment, but you notice her glancing between your paper and Jaden's with a slight frown."
                            
                            "You'll have to see if she notices the similarities later..."
                            
                        "Decide against it":
                            $ honesty_score += 1
                            $ love_interest_points += 2
                            
                            "You appreciate the gesture but shake your head slightly."
                            
                            "When your name is called, you admit you don't have the assignment."
                            
                            show professor disappointed
                            
                            prof "I see. Not the strongest start to your college career, [player_name]. I expect it on my desk by tomorrow morning."
                            
                            "After class, Jaden catches up with you."
                            
                            li "Hey, that was brave of you. A lot of people would have just copied."
                            
                            mc "Thanks. I didn't want to start off on the wrong foot with academic integrity."
                            
                            show love_interest admiring
                            
                            li "I respect that. Want to work on the next assignment together? Properly, I mean."
                else:
                    "You look around but everyone seems to be guarding their papers."
                    
                    "When your name is called, you have to admit you don't have the assignment."
                    
                    show professor disappointed
                    
                    prof "I see. Not the strongest start to your college career, [player_name]. I expect it on my desk by tomorrow morning."

    prof "Now, let's go through the syllabus. This course meets three times a week, and you'll have both individual and group assignments."
    
    "Dr. Jenkins begins reviewing the course structure, assignment weights, and her expectations."
    
    prof "I want to emphasize that attendance and participation make up a large portion of your grade. This isn't a class you can skip and still expect to do well."
    
    "She clicks to the next slide showing a calendar."
    
    prof "You'll notice four major projects throughout the semester. The first will be due in two weeks."
    
    if love_interest_points >= 4:
        "Jaden leans over and whispers to you."
        
        li "Want to be study partners for this class? I could use the support."
        
        menu:
            "Accept the offer":
                $ love_interest_points += 2
                $ academic_score += 1
                
                mc "Definitely. Two heads are better than one."
                
                show love_interest happy
                
                "Jaden smiles and jots something in their planner."
                
                li "Perfect. Let's exchange numbers after class and set up a schedule."
                
            "Politely decline":
                $ love_interest_points -= 1
                
                mc "I think I'm going to try to handle this one on my own, but thanks."
                
                show love_interest neutral
                
                "Jaden nods with a slightly disappointed expression."
                
                li "No problem. Offer stands if you change your mind."

    "As Dr. Jenkins continues explaining the curriculum, you take notes and try to get a feel for her teaching style."
    
    prof "College is about taking initiative and responsibility for your own learning. I'm here to guide you, but ultimately your success depends on your effort."
    
    prof "For Thursday, please read chapters one and two of your textbook and complete the reflection questions at the end of each chapter."
    
    "The class continues with a discussion about effective study habits and campus resources."
    
    prof "Before we end, I'd like to do a quick icebreaker activity. Turn to the person next to you and share one academic goal you have for this semester."
    
    if love_interest_points >= 4:
        "You turn to Jaden."
        
        menu:
            "Share an ambitious goal":
                $ academic_score += 1
                $ love_interest_points += 1
                
                mc "I'm aiming to maintain at least a 3.8 GPA and join the honors program by next semester."
                
                show love_interest impressed
                
                li "Wow, that's ambitious. Mine's a bit more modest - I just want to find a good balance between academics and getting involved on campus."
                
                mc "That's actually really smart. No point in getting all A's if you're miserable."
                
                li "Exactly. Though I'm impressed by your drive."
                
            "Share a balanced goal":
                $ mental_health += 1
                $ love_interest_points += 1
                
                mc "I want to do well academically while still making time for clubs and friends. Finding that balance is important to me."
                
                show love_interest happy
                
                li "That's exactly what I was going to say! After seeing how some seniors burn out, I want to pace myself better."
                
                mc "Great minds think alike, I guess!"
                
                "You both laugh, and it feels like you're on the same wavelength."
    else:
        "You turn to the student next to you, someone you haven't met before."
        
        "You exchange pleasantries and share your academic goals for the semester."
        
        "It's a brief conversation, but it's nice to make another connection on campus."

    "The class winds down with Dr. Jenkins answering a few questions from students."
    
    prof "That's all for today. Remember your reading for Thursday, and those with missing assignments, I'll be expecting them as discussed."
    
    "As you gather your things, you reflect on your first proper college class experience."
    
    if love_interest_points >= 6:
        show love_interest happy
        
        li "Hey, want to grab coffee before the next class? We could go over the reading list."
        
        menu:
            "Accept the invitation":
                $ love_interest_points += 2
                
                mc "That sounds great! I could use some caffeine."
                
                li "Perfect! I know a quiet spot in the student center that has decent coffee."
                
                "You leave the classroom together, feeling like college might be off to a pretty good start after all."
                
                jump day4_coffee_with_li
                
            "Decline but suggest another time":
                $ love_interest_points += 1
                
                mc "I can't right now, but how about tomorrow after the morning class?"
                
                li "Sure, that works for me. I'll text you."
                
                "You exchange numbers before heading your separate ways."
                
                jump day4_next_event
                
    else:
        "You pack up your bag and head out, mentally reviewing your schedule for the rest of the day."
        
        jump day4_next_event

label day4_coffee_with_li:
    scene bg student_cafe with dissolve
    
    "The campus cafe is bustling with students catching up between classes."
    
    show love_interest normal at right
    
    li "So what made you choose this university anyway?"
    
    "As you sip your coffee, you find yourself enjoying the easy conversation with Jaden."
    
    "Maybe the transition to college life won't be as overwhelming as you feared."
    
    jump day4_next_event

label day4_next_event:
    # This will lead to the next scene in your game
    "The rest of your day stretches ahead, full of possibilities."
    
label day5_morning:
    scene bg dorm_room with dissolve
    
    "You wake up on day 5 feeling different. The first week of college is almost over, and you've already experienced so much."
    
    "Your phone buzzes with a notification - a campus-wide email about a major end-of-week event happening tonight."
        
    mc "Hmm, a 'First Week Party'. Could be fun."
    
    "You get ready for the day, thinking about how your choices this week might shape your college experience moving forward."
    
    # Check stats to determine which path the player is on
    if social_score >= 6 and love_interest_points >= 8:
        jump day5_popular_path
    elif social_score >= 3 and mental_health >= 3:
        jump day5_fitting_in_path
    else:
        jump day5_struggling_path

# POPULAR/WELL-CONNECTED ENDING PATH
label day5_popular_path:
    scene bg campus_common with dissolve
    
    "As you walk across campus toward your morning class, it seems like everyone knows you."
        
    "Several students wave, call out your name, or stop to chat briefly. Your social circle has grown impressively in just one week."
    
    "Your phone keeps buzzing with group chat messages and invitations for weekend plans."
    
    "Roommate: 'The crew's meeting for breakfast before class. You coming?'"
    
    menu:
        "Join them for breakfast":
            
            scene bg campus_cafe with dissolve
            
            "You find a large table of students from your dorm already laughing and sharing stories when you arrive."
            
            "Friend 1" "There they are! The social butterfly has arrived!"
            
            "Friend 2" "Save us seats at the party tonight! We heard you know the event organizers."
            
            mc "I'll see what I can do."
            
            "You realize you've developed a reputation already - someone who knows everyone and can make things happen."
        
        "Text that you'll catch up later":
            
            "You decide to have a quiet moment to yourself before the day gets busy."
            
            "Even as you carve out alone time, you know your social calendar will be full later. It's nice to be wanted."
    
    scene bg classroom with dissolve
    
    "In class, you notice even the professor seems to recognize your social standing."
    
    show professor normal at center
    
    prof "For the group project, I'll let you all choose your teams. [player_name], perhaps you could help ensure everyone finds a group?"
    
    "You nod, comfortable with the leadership role that's naturally fallen to you."
    
    scene bg campus_path with dissolve
    
    "After class, you spot Jaden waiting for you outside."
    
    show love_interest happy at right with dissolve
    
    li "There you are! I was hoping to catch you before your next class."
    
    "Their face brightens when they see you, and you feel a flutter of excitement yourself."
    
    li "About tonight's party... I know you probably have a million invites, but I was hoping we could go together? Maybe as more than friends?"
    
    menu:
        "Accept enthusiastically":
            $ love_interest_points += 2
            
            mc "I was hoping you'd ask. I'd love to go with you - definitely as more than friends."
            
            show love_interest flirty
            
            li "Really? That's... wow. I wasn't sure if you'd be interested, with so many people vying for your attention."
            
            mc "You're the one I want to spend time with, Jaden. The rest are just friends."
            
            "Jaden takes your hand, giving it a gentle squeeze."
            
            li "Pick me up at 7?"
        
        "Accept but keep it casual":
            $ love_interest_points += 1
            
            mc "I'd love to go with you! I do have a few groups I promised to meet up with there too, though."
            
            show love_interest understanding
            
            li "That's fine! I know you're popular. We can start together and see how the night goes?"
            
            mc "Sounds perfect. Meet at the main entrance at 7?"
            
            li "It's a date. Well, sort of."
            
            "You both laugh, keeping things light but with potential for more."
    
    "News of your plans with Jaden spreads quickly, as gossip tends to do in college."
    
    "By afternoon, it seems to have enhanced your social standing even more."
    
    jump day5_popular_ending

# FITTING IN WELL ENDING PATH
label day5_fitting_in_path:
    scene bg campus with dissolve
    
    "You walk to class with a comfortable sense of belonging. After a week, you've found your rhythm at college."
        
    "You've made a handful of good friends, know your way around campus, and generally feel at ease in your new environment."
    
    "You spot a familiar face - a classmate from your Tuesday seminar."
    
    "Classmate" "Hey [player_name]! Ready for the quiz later?"
    
    mc "As ready as I'll ever be. Want to compare notes at lunch?"
    
    "Classmate" "Sure thing. The usual spot?"
    
    "You nod, appreciating how you've already established 'usual spots' and routines."
    
    scene bg classroom with dissolve
    
    "In class, you participate in discussions confidently. Not trying to stand out, but engaged and present."
    
    show professor normal at center
    
    prof "Good point, [player_name]. I appreciate your consistent preparation for class."
    
    "You feel a quiet satisfaction. You're doing well academically without killing yourself with stress."
    
    scene bg campus with dissolve
    
    "During lunch, you sit with your small but solid group of friends."
    
    "The conversation flows easily - classes, weekend plans, a new movie coming out."
    
    "Friend" "Are you going to the party tonight?"
    
    mc "I think so. It could be fun."
    
    "Friend" "Cool, we'll probably go around 8. Text if you want to meet up."
    
    "No pressure, just options. You appreciate the balance you've found."
    
    show love_interest normal at right with dissolve
    
    "You notice Jaden approaching your table with a tray."
    
    li "Mind if I join?"
    
    menu:
        "Welcome them warmly":
            $ love_interest_points += 1
            
            mc "Of course! We were just talking about the party tonight."
            
            show love_interest happy
            
            "Jaden sits down, easily joining the conversation."
            
            li "I'm planning to check it out too. Maybe we could all go together?"
            
            "Your friends nod, making space for Jaden in your circle."
            
            "There's no dramatic romance, but a comfortable friendship with potential for more."
        
        "Keep things friendly but casual":
            
            mc "Sure, plenty of room."
            
            "Jaden joins you, and while the conversation is pleasant, you maintain some emotional distance."
            
            "You've decided to focus on establishing yourself independently before pursuing any romantic connections."
            
            "It feels like the right approach for you right now."
    
    "After lunch, you head to your afternoon commitments with a sense of calm confidence."
    
    "Your college experience isn't flashy or dramatic, but it's genuine and sustainable."
    
    jump day5_fitting_in_ending

# STRUGGLING/DROPOUT ENDING PATH
label day5_struggling_path:
    scene bg dorm with dissolve
    
    "While other students are heading to class, you remain sitting on your bed, overwhelmed by a growing sense of disconnect."
        
    "Your first week of college has been a series of missteps and mounting anxiety."
    
    "You check your phone - no messages, no invitations, nothing from the few acquaintances you tried to connect with."
    
    "Your academic performance hasn't been any better. The assignments pile up, incomprehensible and overwhelming."
    
    menu:
        "Force yourself to go to class":
            
            "You drag yourself to your morning lecture, arriving late and drawing unwanted attention."
            
            scene bg classroom with dissolve
            
            show professor disappointed at center
            
            prof "Nice of you to join us, [player_name]. We've already begun the quiz."
            
            "Your stomach sinks as you fumble to your seat, unprepared and already failing."
            
            "During the lecture, the content washes over you without sticking. You're physically present but mentally elsewhere."
            
            "After class, you overhear two students making weekend plans. No one thinks to include you."
        
        "Skip class and stay in bed":
            $ academic_score -= 2
            
            "You can't face another day of feeling like an outsider. You pull the covers back over your head."
            
            "Your phone buzzes - an automated email from your professor noting your absence and reminding you of the attendance policy."
            
            "The thought of falling behind creates even more anxiety, trapping you in a downward spiral."
    
    scene bg campus with dissolve
    
    "Later, you wander the campus alone while everyone else seems to move in coordinated social groups."
        
    "You pass by Jaden, who gives you a brief wave but continues walking with their new friends."
    
    if love_interest_points >= 3:
        "They look like they might stop, perhaps feeling some obligation from your earlier interactions, but ultimately continue on."
        
        "Whatever connection might have developed has withered from neglect and your increasing isolation."
    else:
        "There's no recognition in their eyes beyond basic politeness. You're just another face in the crowd to them."
    
    "You check your student portal and see notifications about missed assignments and failing grades after just one week."
    
    "The thought of the First Week Party fills you with dread rather than excitement."
    
    mc "How can everyone celebrate when I feel this lost?"
    
    jump day5_dropout_ending

# THE THREE ENDINGS

label day5_popular_ending:
    scene bg party with dissolve
    
    "The party is in full swing when you arrive, and heads turn as you and Jaden walk in together."
    
    show love interest happy at right
    
    "Friends call out to you from every direction, and you navigate the social landscape effortlessly, introducing Jaden to everyone you know."
    
    "Friend Group 1" "There they are! We saved you space at the front for the concert!"
    
    "Friend Group 2" "Are you coming to the after-party at the lake house?"
    
    "Sports Team Captain" "Hey! We need you for the team challenge later!"
    
    "Jaden looks impressed, even slightly overwhelmed by your popularity."
    
    li "I knew you were well-liked, but this is another level."
    
    mc "What can I say? I connect with people easily."
    
    "As the night progresses, you float between social circles, always the center of attention, always bringing people together."
    
    "The student body president even approaches you about joining student government."
    
    scene bg party with dissolve
    
    "When the fireworks begin, you find a perfect spot with Jaden and your closest friends."
    
    "Looking around at the connections you've made in just one week, you feel a deep sense of belonging and excitement for what's ahead."
    
    "Jaden's fingers intertwine with yours as the sky lights up with color."
    
    li "I'm really glad I met you on day one. I have a feeling these next four years are going to be amazing."
    
    "You smile, knowing you've found not just a significant other, but a whole community where you truly belong."
    
    "YOU ARE SOCIALLY SUCCESSFUL!"
    
    "You became one of the most well-known students on campus, with a wide circle of friends, involvement in multiple organizations, and a fulfilling relationship with Jaden that lasted through graduation."
    
    return

label day5_fitting_in_ending:
    scene bg party with dissolve
    
    "You arrive at the party with your small group of friends, feeling comfortable and at ease."
        
    "The event is crowded, but not overwhelming. You recognize faces from your classes and dorm, exchanging friendly nods and brief conversations."
    
    "Friend" "Want to check out the games area? I heard they have some great prizes."
    
    "You spend the evening moving between activities, neither the center of attention nor on the outside looking in."
    
    "When you run into Jaden, it feels natural to include them in your group."
    
    show love interest normal at right
    
    li "Having fun?"
    
    mc "Yeah, it's been a good night. A good week, really."
    
    li "I know what you mean. It took a few days, but I feel like I can be myself here."
    
    "You share a moment of mutual understanding. College isn't perfect, but you've both found your places."
    
    scene bg campus with dissolve
    
    "As the party winds down, you and your friends take a walk around the illuminated campus."
    
    "The conversation turns to plans for the semester - study groups, movie nights, a road trip during fall break."
    
    "You realize you've built the foundation for a college experience that feels authentic to you."
    
    "Not the most popular student, not struggling to fit in - just comfortably yourself, with people who appreciate you for who you are."
    
    "YOU ARE PRETTY COMFORTABLE HERE."
    
    "Throughout your college years, you maintained a balance of meaningful friendships, academic success, and personal growth. You graduated with connections that would last a lifetime."
    
    return

label day5_dropout_ending:
    scene bg dorm with dissolve
    
    "While the sounds of the party echo across campus, you sit alone in your darkened dorm room, packing your belongings."
        
    "The decision didn't come suddenly. It's been building all week - the growing certainty that you don't belong here."
    
    "Your roommate is out enjoying the party, which makes this easier. You've already emailed your parents."
    
    mc "It's not working. I'm not ready for this."
    
    "You look at your course schedule and feel nothing but dread. The assignments you don't understand. The social connections you failed to make."
    
    "A knock at your door startles you."
    
    "RA" "Hey, [player_name]? Can we talk for a minute?"
    
    menu:
        "Let them in":
            $ mental_health += 1
            
            "You open the door to find your Resident Advisor looking concerned."
            
            "RA" "Your professor contacted me about your absences. And I've noticed you've been isolating yourself."
            
            mc "I've decided to leave. College isn't for me. Not right now, anyway."
            
            "RA" "I understand it can be overwhelming. Have you considered talking to a counselor before making a final decision? Or maybe looking into a reduced course load?"
            
            mc "I've thought about it a lot. I need some time to figure things out before trying again."
            
            "RA" "Well, if you're sure, let me help you with the withdrawal paperwork. And know you can always come back when you're ready."
            
            "Though your decision remains the same, it helps to have someone acknowledge your struggle without judgment."
        
        "Ignore the knock":
            
            "You remain silent until your RA eventually leaves a note under your door."
            
            "You'll deal with the official withdrawal process tomorrow. Tonight, you just want to be alone with your decision."
            
            "It feels like failure, but also like release. The constant pressure of trying to fit in somewhere you don't belong is finally lifting."
    
    scene bg campus with dissolve
    
    "The next morning, you board a bus home, watching the campus recede in the distance."
    
    "It's not the ending you imagined when you arrived a week ago full of hopes and expectations."
    
    "But as the familiar countryside replaces the college town through the window, you feel a complicated mix of regret and relief."
    
    mc "Maybe I'll try again. Just not here. Not now."
    
    "YOU HATE IT HERE. YOU DROP OUT."
    
    "You took a year off to reassess your goals and build your confidence. When you returned to education, it was at a smaller college closer to home, where you eventually found your path at your own pace."
    
    return
    
    