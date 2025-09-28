# Images are stored in `images/Renpy App/`. Reference them directly to avoid
# runtime copy issues on different systems.


# Using a single pose named "neutral" for Ava. If the image doesn't exist,
# Ren'Py will warn but the script will still run.
## Ava transforms and images
# Positioning: bottom-center portrait, scaled to 40% width for a character sprite.
# Use the raw ava.png as Ava's image. Show it with `show ava`.
## Character sprites: use transformed portraits so they appear as characters
# (scaled and bottom-aligned) instead of full-screen images.
## Images removed: this project will display no pictures.
## All image declarations intentionally removed so the script shows text only.


# Character declarations
define kayla = Character("Kayla", color="#88ccff")
define lucas = Character("Lucas", color="#ffcc88")
define ava = Character("Ava", color="#ff77aa")
define mom = Character("Mom", color="#aaff88")

# Simple game state: which day it is, a tiny conflict meter, and how many
# reserved slices remain for future days (we start with 11 slices reserved
# per future day, per the story). These are small examples you can expand.
default day = 1
default conflict = 0
default reserved_day2 = 11
default reserved_day3 = 11
default told = False


label start:

    # Start at the living room background. You can add your own background
    # image files to the images/ directory (e.g., "bg room.png").
    scene

    # Begin the story at the new house scene.
    jump new_house


label new_house:

    # Opening scene: Kayla playing while Mom arrives with pizza.
    scene
    kayla "I was on the floor, knees tucked into a fort of cardboard boxes and stuffed animals, when Mom came in carrying three glossy pizza boxes."

    # images removed: show ava removed

    mom "Okay, kids. Now that we've finished moving into our new house, I won't be able to make dinner for the next three days while we get settled. I bought three large pizzas. Three boxes should last us three days. If you fatties eat them all tonight, I guess you can starve - I don't care."

    mom "One for today. The rest are up to you. Since there are three of you and eleven slices in each box, you'll have to figure out who earns the extra slice for the day. I'm locking the kitchen every night at eight. No water, no pizza after that. Don't touch the boxes that are for another day. I won't be here to monitor - you take care of it."

    kayla "She set the boxes in the pantry, tapped the lock, and left the rules like a small, final law."

    # Move to bedroom scene
    jump new_bedroom


label new_bedroom:

    scene


    lucas "You heard Mom. If I find out any of you took an extra slice, you're dead."

    ava "I don't know why you're trying to talk like that. We all know you're the biggest of the three of us."

    scene
    kayla "They argued the way siblings do. I pretended to read with the lamp on until sleep finally dragged me under."

    kayla "Sometime later, I felt the bed creak - Ava slipping out like a shadow. I lay still, counting my breaths, and watched her vanish into the doorway."

    kayla "I followed."

    jump stair_case


label stair_case:

    scene

    # images removed: show ava removed

    scene
    kayla "She moved like a practiced thief, barefoot on the stairs. The pantry cast a moon of shadow where the boxes were stacked. Ava reached for the third day's box - the one that wasn't supposed to be touched until morning."

    kayla "My chest tightened. Mom had been clear: no touching the boxes for the next days. Mom's voice threaded back through my head. I thought of Mom at work, trusting us to be sensible. Should I tell?"

    ava "Don't you dare snitch on me."

    # Present the player with a choice: tell Mom or stay silent.
    menu:
        "Tell Mom":
            $ conflict += 1
            $ told = True
            kayla "I ran."
            kayla "I banged on Mom's door until she opened it, groggy and annoyed."

            mom "Why are you pigs banging on my door this late at night? There better be a good reason for it."

            kayla "Ava - she's in the kitchen. She's touching the box. She's getting the third day's pizza."

            mom "If you're going to break the rules, you face the consequences."

            # Mom takes one of the reserved slices for day 2 as punishment.
            $ reserved_day2 = max(0, reserved_day2 - 1)

            mom "You stole from what's for tomorrow. If you can't follow the rules, you don't get rewards."

            kayla "Mom took the slice Ava had reached for and, to our shock, ate it herself. Ava stood there, cheeks pink and furious."

            ava "You'd better watch your back, Kayla. I will get the last slice."

        "Stay silent":
            $ conflict += 1
            $ told = False
            kayla "I hesitated. The pantry was warm with cardboard and sauce. Ava's fingers closed over the lid and she slipped the slice into her hand."

            kayla "She moved back into the shadows and closed the pantry like nothing had happened."

            # Ava successfully takes one reserved slice for day 3 in this branch.
            $ reserved_day3 = max(0, reserved_day3 - 1)

            ava "Ha. Easy. Don't tell Mom you saw anything."

            kayla "Her whisper was a promise and a threat both."

    # After the choice, close the scene with reflection and a jump back to the
    # house rhythm so the player can continue. We'll keep the narration similar
    # but acknowledge the player's choice.
    scene
    if told:
        kayla "I wanted to say I did the right thing. I wanted to say sorry. Both sounded false. The next morning felt like the start of something angrier."
    else:
        kayla "I wanted to say I did the right thing. I wanted to say sorry. Both sounded false. But at least for tonight, no one had been caught. The next morning felt like the start of something angrier."

    kayla "Every day after that felt like a small battle - counting, bargaining, hiding crumbs and making deals over coffee mugs. Lucas blustered about fairness, Ava planned distractions, and I kept score in my head."

    kayla "The lock clicked every night like a starting gun. We were supposed to be a team unpacking our lives into a new house. Instead, we learned how to keep score on pizza slices and grudges."

    # Advance to day 2 and show how your choice affected the morning.
    $ day = 2
    jump day_two


label day_two:

    scene

    # Morning routine: Mom leaves for work and the consequences of the
    # player's choice become visible in dialogue.
    mom "Morning. I'm off to work. Keep the kitchen locked at eight and behave."
    scene

    if told:
        kayla "Mom left with a tired wave. In the kitchen, a new quiet had settled - one shaped by last night's punishment."

        ava "You told on me, Kayla."

        kayla "I did. Mom said rules matter. You lost a slice because you couldn't follow them."

        lucas "That was harsh, Ava. You shouldn't have risked it."

        kayla "Ava didn't answer. Her jaw worked like she was counting something else - grudges."

        mom "(off) Make sure you split things fairly today. I'm counting on you."

        kayla "The day felt thinner, as if someone had already eaten away at trust."

    else:
        kayla "Mom waved and left for work, none the wiser. The kitchen smelled like morning and missed chances."

        ava "Nice and easy. You didn't tell. Smart."

        lucas "What happened? Did someone sneak something?"

        kayla "Ava shrugged, the edges of her smile sharp. She'd already taken something for herself and the air between us hummed with it."

        mom "(off) Don't forget to lock up tonight, and be sensible."

    kayla "It was a quieter kind of betrayal - no punishment, but a small, secret advantage gone to Ava."

    # Continue the story from here or return to main flow.
    return
