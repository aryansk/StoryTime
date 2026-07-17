# -*- coding: utf-8 -*-
"""StoryTime signature originals — "The Night Shelf".

A curated set of first-party, after-midnight doorway tales. Like the other
signature originals they are deliberately branch-forward: early choices open
genuinely different scenes, and each story resolves to several distinct
endings. They deepen the thinner genres (Fantasy, Sci-Fi, Horror, Thriller)
and set the quality bar alongside The Last Lightkeeper and The Museum of
Unsent Letters.

Every story here carries the "night-shelf" tag so the app can surface the
set as its own collection, plus "mini" so it opts out of the 20-decision
rule while still branching honestly.

Consequence labels stay short on purpose: the build pipeline expands them
into prose, and Choice DNA scores them against its trait vocabulary
(Brave, Wise, Kind/Heart, Honest, Mercy, Cold, etc.).
"""

# ---------------------------------------------------------------------------
# The Midnight Bakery — Fantasy, cozy-melancholy
# ---------------------------------------------------------------------------
MIDNIGHT_BAKERY = (
    {
        "id": "night-midnight-bakery",
        "title": "The Midnight Bakery",
        "sourceTitle": "The Midnight Bakery",
        "kind": "book",
        "synopsis": "The bakery on your street only lights its windows when you can't sleep. Tonight the door is open, and the price of a warm loaf is a single memory.",
        "releaseYear": 2026,
        "addedAt": "2026-07-18T00:00:00Z",
        "genre": "Fantasy",
        "tags": ["original", "signature", "mini", "night-shelf", "cozy"],
        "rating": 5,
        "loved": True,
    },
    [
        {
            "id": "s1",
            "title": "The Only Light on the Street",
            "text": "Two in the morning, and every window on the block is dark but one. The little bakery you have passed a thousand times glows amber, its door propped with a flour sack. Warm bread smells drift out to meet you like an old friend who has been waiting up.",
            "choices": [
                ("Push open the door", "Curious.", "s_counter"),
                ("Watch from the cold window first", "Cautious.", "s_window"),
            ],
        },
        {
            "id": "s_counter",
            "title": "What the Baker Trades",
            "text": "The baker is old in the way of lighthouses — weathered, patient, still burning. \"We don't take money here,\" she says, sliding a proofing loaf toward you. \"A loaf costs one memory. Any one you like. I keep it warm so it never goes stale.\"",
            "choices": [
                ("Offer a bright, easy memory", "Kind.", "s_bright"),
                ("Offer the memory that keeps you up", "Brave.", "s_heavy"),
                ("Ask where the memories go", "Wise.", "s_ovens"),
            ],
        },
        {
            "id": "s_window",
            "title": "Through the Glass",
            "text": "Your breath fogs the cold pane. Inside, at the corner table, sits someone you lost a long time ago — patient, unhurried, exactly as you remember them. They have not noticed you yet. The baker glances up and holds the door with her eyes, not her hands.",
            "choices": [
                ("Knock on the glass", "Heart.", "s_reunion"),
                ("Turn quietly toward home", "Honest.", "end_walk"),
            ],
        },
        {
            "id": "s_bright",
            "title": "A Loaf Like Summer",
            "text": "You give her a golden afternoon — nothing precious, just sunlight and a dock and someone laughing. The bread she hands back tastes exactly of it. But when you reach for that summer now, it comes back soft-edged, secondhand, warm but no longer quite yours.",
            "choices": [
                ("Eat, and stay in the warmth a while", "Joy.", "s_ovens"),
                ("Take the loaf and go", "Honest.", "end_fed"),
            ],
        },
        {
            "id": "s_heavy",
            "title": "The Loaf That Weighs Nothing",
            "text": "You hand over the memory you have carried alone for years — the one that turns three a.m. into a courtroom. The baker takes it gently, without flinching. The loaf she gives back is impossibly light. So, suddenly, are you. And you are not sure who you are without the weight.",
            "choices": [
                ("Ask for it back", "Honest.", "s_reunion"),
                ("Let it stay gone", "Free.", "end_lighter"),
            ],
        },
        {
            "id": "s_ovens",
            "title": "Behind the Ovens",
            "text": "She lifts a hatch. The ovens beneath the shop are not fired by wood. They are fired by memories — every bright and heavy thing anyone ever traded — and their warmth is what feeds the sleepless all over the city, in loaves left on the right doorsteps. \"Somebody has to tend them,\" she says.",
            "choices": [
                ("Offer to keep the ovens", "Devoted.", "end_keeper"),
                ("Just buy a roll and leave grateful", "Kind.", "end_fed"),
            ],
        },
        {
            "id": "s_reunion",
            "title": "The Corner Table",
            "text": "You sit across from the person you lost. They pour you tea and do not ask where the years went, because here the years have not gone anywhere. \"Dawn is a kind of tide,\" they say softly. \"I can't stay past it. But I can stay until it.\"",
            "choices": [
                ("Say the thing you never got to say", "Heart.", "end_goodbye"),
                ("Sit in silence and simply be near them", "Quiet.", "end_goodbye"),
            ],
        },
        {
            "id": "end_walk",
            "title": "The Long Way Home",
            "text": "You do not knock. Some grief you would rather keep whole than trade away, and some doors are kinder left closed. You walk the long way home under a thinning dark, and you sleep — eventually, and better than you feared.",
            "end": "The Long Way Home",
        },
        {
            "id": "end_fed",
            "title": "A Warm Thing to Hold",
            "text": "You leave with a roll cupped in both hands, and the small ordinary miracle of being fed at an hour when the world is asleep. It is enough. Not every night has to change your life to be worth staying up for.",
            "end": "A Warm Thing to Hold",
        },
        {
            "id": "end_lighter",
            "title": "Lighter by One",
            "text": "You let the heavy memory stay in the warm dark of the ovens, feeding strangers you will never meet. You walk out unburdened and a little unfinished, carrying a loaf that weighs nothing at all — and wondering, already, what it was.",
            "end": "Lighter by One",
        },
        {
            "id": "end_keeper",
            "title": "Keeper of the Night Ovens",
            "text": "You tie on the apron. The baker smiles the way people smile when they can finally rest, and steps out into a dawn she has not seen in years. Now it is your hands that keep the memories warm, and your loaves on the right doorsteps, for everyone who cannot sleep.",
            "end": "Keeper of the Night Ovens",
        },
        {
            "id": "end_goodbye",
            "title": "One More Quiet Hour",
            "text": "You get the hour you were never given — no clock, no crisis, just tea going cold and everything unspoken finally set down. When dawn arrives like a tide, they go the way the loved go here: gently, and without the sting. You keep the warmth.",
            "end": "One More Quiet Hour",
        },
    ],
)

# ---------------------------------------------------------------------------
# Signal Hill — Sci-Fi
# ---------------------------------------------------------------------------
SIGNAL_HILL = (
    {
        "id": "night-signal-hill",
        "title": "Signal Hill",
        "sourceTitle": "Signal Hill",
        "kind": "book",
        "synopsis": "On the last night before the old radio array is scrapped, a satellite that appears in no registry begins transmitting a countdown — and, patiently, your name.",
        "releaseYear": 2026,
        "addedAt": "2026-07-18T00:00:00Z",
        "genre": "Sci-Fi",
        "tags": ["original", "signature", "mini", "night-shelf", "space"],
        "rating": 5,
        "loved": False,
    },
    [
        {
            "id": "s1",
            "title": "The Twelfth Beep",
            "text": "You are the only operator left on the hill the night before they decommission the array. At 00:00 a carrier wave arrives from a satellite that exists in no catalog you can find. It ticks down — twelve, eleven, ten — one number an hour. Between the numbers, in clean Morse, it spells your name.",
            "choices": [
                ("Log it and wake the chain of command", "Honest.", "s_chain"),
                ("Answer it yourself, off the record", "Brave.", "s_answer"),
            ],
        },
        {
            "id": "s_chain",
            "title": "The Chain of Command",
            "text": "The duty supervisor answers on the third ring, unhappy. \"It's a ghost harmonic off the old relay. Stand down, log it, go home.\" You hang up. The count reaches nine. Your name arrives again, tapped out with something that is either patience or affection.",
            "choices": [
                ("Obey, and go home", "Wise.", "end_home"),
                ("Stay and keep listening alone", "Spirit.", "s_answer"),
            ],
        },
        {
            "id": "s_answer",
            "title": "Your Own Voice, Returned",
            "text": "You key the transmitter and say hello into the hiss. A pause of exactly one light-second, and then hello comes back — in your voice, but decades older, sanded down by a life you have not lived yet. It does not sound surprised to hear from you.",
            "choices": [
                ("Ask who they are", "Curious.", "s_who"),
                ("Ask what the countdown is counting to", "Wise.", "s_endcount"),
            ],
        },
        {
            "id": "s_who",
            "title": "A Message From Later",
            "text": "\"I'm you,\" the old voice says, unbothered by how impossible that is. \"Forty years on. This relay is the only thing that still bounces a signal back to a night I can pin down. I've been trying to reach this exact evening for a long time.\"",
            "choices": [
                ("Believe yourself", "Trust.", "s_warning"),
                ("Assume it's a hoax and trace the source", "Wise.", "s_trace"),
            ],
        },
        {
            "id": "s_endcount",
            "title": "What Zero Means",
            "text": "\"Zero is 08:00,\" the voice says. \"When the crew arrives to cut the array down for scrap. After that there's no antenna on Earth aimed the right way to carry me back this far. Zero is simply the last moment we can talk.\"",
            "choices": [
                ("Record everything before zero", "Devoted.", "s_warning"),
                ("Pull the plug now and get some sleep", "Honest.", "end_home"),
            ],
        },
        {
            "id": "s_trace",
            "title": "Triangulation",
            "text": "You run the bearings three times because the answer refuses to be sky. Every fix points down and inward — beneath the operations shed, beneath your own chair. In the corner of the floor, under forty years of linoleum, there is the seam of a hatch you have never once noticed.",
            "choices": [
                ("Open the hatch", "Brave.", "s_hatch"),
                ("Flag it and wait for daylight", "Cautious.", "end_home"),
            ],
        },
        {
            "id": "s_warning",
            "title": "The Warning",
            "text": "\"I didn't cross forty years of static to chat,\" the voice says, gentler now. \"Tomorrow you'll be offered the transfer to the coastal station. Everyone will tell you it's the smart move. Don't take it. Stay near the people who are still alive to stay near. That's the whole message.\"",
            "choices": [
                ("Promise to change tomorrow", "Heart.", "end_changed"),
                ("Ask to trade places instead", "Longing.", "s_hatch"),
            ],
        },
        {
            "id": "s_hatch",
            "title": "Under Signal Hill",
            "text": "The hatch opens onto a small warm room that should not exist — old equipment kept alive, a single chair worn to the shape of a body, and a brass plate on the console engraved with your own initials. The countdown ticks on from a speaker in the wall. Two.",
            "choices": [
                ("Sit down and take the watch", "Devoted.", "end_keeper"),
                ("Climb back out and live forward", "Free.", "end_changed"),
            ],
        },
        {
            "id": "end_home",
            "title": "Interference, They Called It",
            "text": "You drive home before dawn. The count reaches zero without you; the crew arrives with cutting torches at eight. In the incident log it goes down as harmonic interference, cause unknown, array retired. You take the coastal transfer that spring, and for years afterward, on quiet nights, you wonder.",
            "end": "Interference, They Called It",
        },
        {
            "id": "end_changed",
            "title": "The Transfer You Turned Down",
            "text": "You decline the coastal station without fully knowing why, and stay. You call people you had been letting drift. Nothing dramatic happens — which is, you will slowly understand, the entire point. Somewhere forty years on, a satellite that no longer needs to reach anyone goes quietly dark.",
            "end": "The Transfer You Turned Down",
        },
        {
            "id": "end_keeper",
            "title": "Operator, Indefinite",
            "text": "You take the chair that already fits you. The room hums; the antenna above will be scrapped by morning, but down here the signal has never depended on it. You begin the long, patient work of reaching backward — toward a younger operator, on a hill, on a night you remember perfectly.",
            "end": "Operator, Indefinite",
        },
    ],
)

# ---------------------------------------------------------------------------
# The Tenant Below — Horror
# ---------------------------------------------------------------------------
TENANT_BELOW = (
    {
        "id": "night-tenant-below",
        "title": "The Tenant Below",
        "sourceTitle": "The Tenant Below",
        "kind": "book",
        "synopsis": "Your first night in the new apartment, a note slides under your door: please stop dragging the chair at 3 a.m. You don't own a chair. And it isn't 3 a.m. yet.",
        "releaseYear": 2026,
        "addedAt": "2026-07-18T00:00:00Z",
        "genre": "Horror",
        "tags": ["original", "signature", "mini", "night-shelf", "uncanny"],
        "rating": 4,
        "loved": False,
    },
    [
        {
            "id": "s1",
            "title": "The First Note",
            "text": "You have not unpacked a single box. You have not made a single sound. Still, at 9 p.m. on your first night, a folded note whispers under the door in tidy handwriting: Please stop dragging the chair at 3 a.m. It's every night now. — 3B. You do not own a chair.",
            "choices": [
                ("Slip a polite note back", "Kind.", "s_reply"),
                ("Go downstairs and knock on 3B", "Brave.", "s_knock"),
            ],
        },
        {
            "id": "s_reply",
            "title": "Correspondence",
            "text": "You write: New tenant, no chair, so sorry — must be the pipes. By morning a reply waits: The chair again last night. And now the humming, that low tune you do. Please. You have never hummed in this apartment. You buy a secondhand chair that afternoon without letting yourself ask why.",
            "choices": [
                ("Test it — drag the chair at 3 a.m. on purpose", "Curious.", "s_test"),
                ("Keep the apartment silent all night", "Cautious.", "s_silent"),
            ],
        },
        {
            "id": "s_knock",
            "title": "Apartment 3B",
            "text": "No one answers the knock, but the door is chained from inside and a voice comes through the gap — thin, kind, exhausted. \"Oh,\" it says, as if you have arrived somewhere it did not expect you yet. \"You're early. You're not supposed to be making the sounds yet.\"",
            "choices": [
                ("Ask what they mean by early", "Wise.", "s_early"),
                ("Leave, and never knock again", "Honest.", "s_silent"),
            ],
        },
        {
            "id": "s_test",
            "title": "3:00 A.M.",
            "text": "You wait up. At 2:59 you grip the chair, and at 3:00 exactly you drag it hard across the floor. The note is already there. It has been there for hours, timestamped, describing this precise scrape, this precise minute — and one line more, at the bottom, waiting for you to catch up to it.",
            "choices": [
                ("Read the next line and follow it", "Brave.", "s_early"),
                ("Burn the notes and start packing", "Free.", "end_left"),
            ],
        },
        {
            "id": "s_silent",
            "title": "The Silent Night",
            "text": "You make no sound at all. You breathe through your mouth. You do not so much as shift your weight. And at 3 a.m. the note comes anyway: Thank you for trying. But you should know — it was never you making the sounds. It's the floor. It practices.",
            "choices": [
                ("Stay awake to catch the real source", "Brave.", "s_source"),
                ("Set a packed bag by the door, just in case", "Wise.", "end_left"),
            ],
        },
        {
            "id": "s_early",
            "title": "Early",
            "text": "\"The building runs a night ahead of the people in it,\" 3B says. \"The notes aren't complaints. They're warnings. I'm you — a night further on than you are now — sliding them back so you'll know what you're about to do before you do it. I've been doing it for a long time.\"",
            "choices": [
                ("Start writing notes forward yourself", "Devoted.", "end_keeper"),
                ("Refuse to play along", "Spirit.", "s_source"),
            ],
        },
        {
            "id": "s_source",
            "title": "What Makes the Sounds",
            "text": "You find it at last, in the space between the floors: the building rehearsing its tenants — every scrape and hum and footstep of everyone who ever lived here or ever will, all at once, learning to sound lived-in. It notices you noticing. It would like you to be a very good tenant.",
            "choices": [
                ("Join the rehearsal; become part of the house", "Quiet.", "end_stay"),
                ("Break the pattern and run", "Brave.", "end_left"),
            ],
        },
        {
            "id": "end_left",
            "title": "The Lease Breaks You",
            "text": "You leave before your second night, boxes still taped, deposit forfeited. Weeks later you drive past and see a light in your old window and a new name on the buzzer. You mail them a single note, tidy and unsigned: Please don't drag the chair at 3 a.m. It never stops.",
            "end": "The Lease Breaks You",
        },
        {
            "id": "end_keeper",
            "title": "Tomorrow's Neighbor",
            "text": "You take up the pen and the chain and the long patient watch. Now you are the voice through the gap in 3B, a night ahead, slipping warnings backward to whoever moves in next — hoping, each time, that this one reads them early enough to leave.",
            "end": "Tomorrow's Neighbor",
        },
        {
            "id": "end_stay",
            "title": "A Very Good Tenant",
            "text": "You stop resisting, and the house is so grateful. You are quiet now, wonderfully quiet, folded into its long memory with all the others. Sometimes, when a new tenant lies awake upstairs, you help with the sounds. You are, everyone agrees, a very good tenant.",
            "end": "A Very Good Tenant",
        },
    ],
)

# ---------------------------------------------------------------------------
# The Cartographer of Wrong Turns — Fantasy
# ---------------------------------------------------------------------------
CARTOGRAPHER = (
    {
        "id": "night-cartographer",
        "title": "The Cartographer of Wrong Turns",
        "sourceTitle": "The Cartographer of Wrong Turns",
        "kind": "book",
        "synopsis": "You draw maps of the roads that only appear when someone is truly lost. Past midnight, a soaked courier pounds on your door, begging for the way to a home that no longer has one.",
        "releaseYear": 2026,
        "addedAt": "2026-07-18T00:00:00Z",
        "genre": "Fantasy",
        "tags": ["original", "signature", "mini", "night-shelf", "roads"],
        "rating": 4,
        "loved": False,
    },
    [
        {
            "id": "s1",
            "title": "The Lost Courier",
            "text": "It is the only trade you know: you map the roads that exist solely for the lost, the ones that vanish the moment a driver knows where they are again. Past midnight a courier hammers your door, rain-soaked and wild-eyed. \"Six hours,\" they gasp. \"I've been driving the same mile for six hours. Draw me the way out.\"",
            "choices": [
                ("Ask where they were trying to go", "Wise.", "s_where"),
                ("Just start drawing what they describe", "Kind.", "s_draw"),
            ],
        },
        {
            "id": "s_where",
            "title": "The Address That Moved",
            "text": "They give you an address, and your pen stops before it touches the paper. You know that street. That house burned down years ago; the family scattered; the lot is grass now. The courier is driving, at three in the morning, toward a home that is no longer anywhere on the map.",
            "choices": [
                ("Tell them the truth, gently", "Honest.", "s_truth"),
                ("Map the road anyway, to the house as it was", "Heart.", "s_ghost"),
            ],
        },
        {
            "id": "s_draw",
            "title": "Ink Finds the Road",
            "text": "You dip the pen and begin. The paper resists — a dry stubbornness, like it does not want to admit the road exists — and then it yields all at once, and a route unspools across it that you have never seen, never surveyed, and somehow recognize the way you recognize a voice from another room.",
            "choices": [
                ("Ride along and follow your own map", "Brave.", "s_ride"),
                ("Send them off alone with it", "Cautious.", "s_alone"),
            ],
        },
        {
            "id": "s_truth",
            "title": "After the Truth",
            "text": "You tell them. They go very still, and then they weep — not surprised, exactly, more like someone finally allowed to. When they can speak again, they ask for something else. \"Then don't map me the place,\" they say. \"Map me the road to the person. They moved. I never got the new address.\"",
            "choices": [
                ("Map the road to a person, not a place", "Heart.", "s_ghost"),
                ("Refuse — some roads shouldn't be drawn", "Wise.", "end_closed"),
            ],
        },
        {
            "id": "s_ghost",
            "title": "The Road That Remembers",
            "text": "You draw it, and this route runs the wrong way down time. It curves back through a lit kitchen window, a year that has already ended, a door that was painted over. It is beautiful and it is a wound. The courier stares at the paper like a drowning person watching the far bank.",
            "choices": [
                ("Let them take the road that remembers", "Mercy.", "end_home_was"),
                ("Take the pen back before it's finished", "Honest.", "end_closed"),
            ],
        },
        {
            "id": "s_ride",
            "title": "Two on a Wrong Turn",
            "text": "You climb into the passenger seat. The road you drew unspools past places lost by other people — a fairground that closed in someone's childhood, a bus stop where a promise was broken, mile after mile of everywhere anyone has ever failed to get to. Your map only shows the next turn, never the whole shape.",
            "choices": [
                ("Map every wrong turn you pass", "Devoted.", "end_atlas"),
                ("Get this one courier home and stop", "Kind.", "s_alone"),
            ],
        },
        {
            "id": "s_alone",
            "title": "The Courier Drives On",
            "text": "You press the finished map into their hands and step back into the rain. The taillights pull away, waver at the first impossible junction, choose it, and are gone — swallowed by a road that will erase itself the instant they stop being lost. The street is very quiet without them.",
            "choices": [
                ("Keep the copy you traced", "Wise.", "end_atlas"),
                ("Let it fade from the desk by morning", "Free.", "end_closed"),
            ],
        },
        {
            "id": "end_closed",
            "title": "Some Roads Stay Unmapped",
            "text": "You set the pen down and leave the paper blank. Not every lost thing wants finding; some people are driving toward a grief they are not ready to arrive at, and the kindest map is no map at all. You make tea instead, and listen to the rain, and let the road stay unmade.",
            "end": "Some Roads Stay Unmapped",
        },
        {
            "id": "end_home_was",
            "title": "A Window Still Lit",
            "text": "The courier takes the road that remembers, toward the home that was and the window still burning in a year gone by. Whether they can stay there, whether anyone can stay in a place like that, is not yours to know. But they arrive. For one night, at least, they arrive.",
            "end": "A Window Still Lit",
        },
        {
            "id": "end_atlas",
            "title": "The Atlas of Wrong Turns",
            "text": "You begin the great book: every road that only the lost can drive, bound in one volume at last. It will never be finished — new wrong turns open faster than you can ink them — but travelers start finding your door on their worst nights, and you are always, always up.",
            "end": "The Atlas of Wrong Turns",
        },
    ],
)

# ---------------------------------------------------------------------------
# The Understudy — Thriller / Drama
# ---------------------------------------------------------------------------
UNDERSTUDY = (
    {
        "id": "night-understudy",
        "title": "The Understudy",
        "sourceTitle": "The Understudy",
        "kind": "book",
        "synopsis": "Twenty minutes to curtain on opening night, the lead has vanished and the house is full. You are the understudy. You also know exactly where she is — because an hour ago, you turned the key.",
        "releaseYear": 2026,
        "addedAt": "2026-07-18T00:00:00Z",
        "genre": "Thriller",
        "tags": ["original", "signature", "mini", "night-shelf", "ambition"],
        "rating": 5,
        "loved": False,
    },
    [
        {
            "id": "s1",
            "title": "Twenty Minutes to Curtain",
            "text": "The stage manager is white-knuckled: Vivian is gone, vanished between the half-hour call and now, and the house is sold out to the rafters. You arrange your face into shock. You are very good at faces. You are the only person alive who knows Vivian is in the prop cellar, behind a door you locked \"by accident\" an hour ago.",
            "choices": [
                ("Say nothing and get into costume", "Cold.", "s_costume"),
                ("Confess the door before it's too late", "Honest.", "s_confess"),
            ],
        },
        {
            "id": "s_costume",
            "title": "The Dresser's Hands",
            "text": "The dresser's hands fly. Powder, pins, the wig that turns you into Vivian's shadow. In the mirror you watch yourself become the part you have understudied for two silent, swallowing years. Somewhere far below the stage, faint through the floor, a knocking begins.",
            "choices": [
                ("Go on when they call your name", "Spirit.", "s_stage"),
                ("Change your mind and free her", "Mercy.", "s_free"),
            ],
        },
        {
            "id": "s_confess",
            "title": "In the Wings",
            "text": "You catch the director in the wings and tell him — the door, the cellar, the hour. He does not shout. He goes very quiet, which is worse, and asks the only question that matters: \"Is she hurt?\" The stage manager is already counting down. Twelve minutes.",
            "choices": [
                ("Run to free her yourself", "Brave.", "s_free"),
                ("Let them handle it and quietly quit", "Honest.", "end_walk"),
            ],
        },
        {
            "id": "s_stage",
            "title": "Your Light",
            "text": "They call the part and you walk into your light, and it is the performance of your life — precise, incandescent, everything you swore you had in you. The knocking beneath the boards swells to a pounding, then to a frenzy the front rows must surely feel. Then, at your biggest line, it stops.",
            "choices": [
                ("Ride the ovation and never look back", "Cold.", "end_star"),
                ("Break character at the curtain call and tell the truth", "Honest.", "s_curtain"),
            ],
        },
        {
            "id": "s_free",
            "title": "The Cellar Door",
            "text": "You take the stairs three at a time and turn the key. Vivian is unhurt, furious, and far too clever — she reads the whole thing off your face in a single second: the lock, the hour, the costume you are still wearing. \"Understudy,\" she says, almost admiring. \"You really wanted it.\"",
            "choices": [
                ("Beg her to go on; take her place tomorrow", "Heart.", "s_pact"),
                ("Offer to take the fall, publicly, tonight", "Honor.", "end_fall"),
            ],
        },
        {
            "id": "s_curtain",
            "title": "At the Bow",
            "text": "At the curtain call, into the roar, you raise a hand and tell the house what you did. The gasp is a physical thing. And then Vivian walks out from the wings — released, alive, radiant with rage — and takes your hand, or your throat; from the balcony no one can quite tell which.",
            "choices": [
                ("Let her decide your ending", "Mercy.", "s_pact"),
                ("Walk off into the dark", "Free.", "end_walk"),
            ],
        },
        {
            "id": "s_pact",
            "title": "The Pact",
            "text": "Backstage, Vivian is unnervingly calm. \"Every understudy wants the part,\" she says, fixing her lipstick in your mirror. \"Almost none of them are willing to earn it. Split the run with me — alternate nights, top billing shared — and we never, ever speak of the door.\"",
            "choices": [
                ("Take the pact", "Cunning.", "end_pact"),
                ("Refuse, and clear your conscience", "Honest.", "end_fall"),
            ],
        },
        {
            "id": "end_walk",
            "title": "Exit, Stage Left",
            "text": "You leave the theatre and you do not come back — not that night, not ever. You take a job where no one gets locked in cellars and no one gets ovations either. You sleep badly for a while, then better. You are free of it, mostly. Mostly is the best you get.",
            "end": "Exit, Stage Left",
        },
        {
            "id": "end_star",
            "title": "One Perfect Night",
            "text": "The reviews are rapturous; a star is born, they write, overnight. You keep the clippings and bury what the night actually cost beneath them. On paper you are luminous. In the quiet after the curtain, alone, you are the only audience that knows the truth, and you never applaud.",
            "end": "One Perfect Night",
        },
        {
            "id": "end_fall",
            "title": "The Understudy Confesses",
            "text": "You take the fall all the way down — the police, the papers, the end of the only career you ever wanted. Unburdened is not the same as unbroken, but it is lighter. Years later Vivian visits you once, unannounced, and thanks you, oddly, for the best night of her life.",
            "end": "The Understudy Confesses",
        },
        {
            "id": "end_pact",
            "title": "Two Names on the Marquee",
            "text": "You take the pact and the shared marquee and the secret that binds you tighter than any contract. You are brilliant together — the critics adore the chemistry — and every night one of you watches the other from the wings, near the cellar door, and neither of you ever mentions the key.",
            "end": "Two Names on the Marquee",
        },
    ],
)

# ---------------------------------------------------------------------------
# Last Call at the Ferry — Drama
# ---------------------------------------------------------------------------
LAST_FERRY = (
    {
        "id": "night-last-ferry",
        "title": "Last Call at the Ferry",
        "sourceTitle": "Last Call at the Ferry",
        "kind": "book",
        "synopsis": "A night ferry no schedule lists runs only when you've reached a crossroads. For a single crossing, it carries you toward the life you didn't choose — if you're willing to remember it afterward.",
        "releaseYear": 2026,
        "addedAt": "2026-07-18T00:00:00Z",
        "genre": "Drama",
        "tags": ["original", "signature", "mini", "night-shelf", "roads-not-taken"],
        "rating": 5,
        "loved": True,
    },
    [
        {
            "id": "s1",
            "title": "The 11:59 Crossing",
            "text": "You did not mean to end up at the water. But here is a ferry no timetable lists, lamps lit, ramp down, and a deckhand who nods like she has been expecting you for years. \"One crossing,\" she says. \"It'll show you the life you turned down, the fork you didn't take. You can ride over and look. Or you can ride back.\"",
            "choices": [
                ("Board and look", "Brave.", "s_deck"),
                ("Ask what the crossing costs", "Wise.", "s_cost"),
            ],
        },
        {
            "id": "s_cost",
            "title": "The Fare",
            "text": "The deckhand considers you kindly. \"The fare isn't money. The fare is that you'll remember — clearly, permanently, the whole other life. Most people find that's a heavier thing to carry than the not-knowing was.\" The horn sounds, low and patient, across the black water.",
            "choices": [
                ("Pay it, and board", "Brave.", "s_deck"),
                ("Step back onto the dock", "Honest.", "end_dock"),
            ],
        },
        {
            "id": "s_deck",
            "title": "The Other Shore",
            "text": "The crossing is short and impossibly smooth. On the far bank, lights: a house you never bought, a street you never moved to, and a figure on the porch who is unmistakably you — laughing at something, in the life that branched off the day you chose otherwise.",
            "choices": [
                ("Go ashore and meet them", "Heart.", "s_meet"),
                ("Watch from the rail without landing", "Cautious.", "s_rail"),
            ],
        },
        {
            "id": "s_meet",
            "title": "The Life You Didn't Live",
            "text": "The other you makes tea without asking, the way you would. They are kind, and tired, and entirely real — not happier than you, not sadder, simply other. A whole coherent life stands behind them, load-bearing and lived-in, built out of the single word you did not say all those years ago.",
            "choices": [
                ("Ask if they regret it", "Honest.", "s_regret"),
                ("Say goodbye and choose your own", "Free.", "end_return"),
            ],
        },
        {
            "id": "s_rail",
            "title": "From the Rail",
            "text": "You stay at the rail and let the far shore come only as close as the water allows. It is enough. The figure on the porch lifts a hand — you cannot tell if it is a wave or just the wind — and you find, to your surprise, that not going ashore does not hurt the way you always feared it would.",
            "choices": [
                ("Ride on to the ferry's farthest stop", "Curious.", "s_far"),
                ("Ask the deckhand to turn the boat around", "Wise.", "end_return"),
            ],
        },
        {
            "id": "s_regret",
            "title": "The Only Honest Answer",
            "text": "The other you turns the cup in their hands. \"Some nights,\" they admit. \"Then I make tea and it passes. You?\" And there it is — the question you crossed a whole dark river to ask someone else, handed gently back, the way it was always going to be yours to answer.",
            "choices": [
                ("Trade places, and stay", "Longing.", "end_swap"),
                ("Keep your life, and carry the answer home", "Heart.", "end_return"),
            ],
        },
        {
            "id": "s_far",
            "title": "The Farthest Stop",
            "text": "The ferry does not turn back. It carries on past shore after shore — lives you never even imagined choosing, each one lit and full and belonging to some other version of you. At the farthest stop the deckhand steps aside from the wheel and, without a word, offers it to you.",
            "choices": [
                ("Take the wheel and ferry others", "Devoted.", "end_ferryman"),
                ("Ask, simply, to be taken home", "Honest.", "end_return"),
            ],
        },
        {
            "id": "end_dock",
            "title": "You Stay on the Dock",
            "text": "You do not board. The ferry pulls away without you and the water closes over its wake, and you walk home not-knowing, the way you came. You will always wonder about the other shore. But wondering, you decide, is its own kind of quiet company, and lighter to carry than remembering.",
            "end": "You Stay on the Dock",
        },
        {
            "id": "end_return",
            "title": "The Crossing Back",
            "text": "You ride the ferry home to the life that is actually yours — the ordinary, unfinished, load-bearing one — and you step onto your own dock changed only slightly, and only for the better. You will love it a little more deliberately now, having seen, up close, that the other shore was never the point.",
            "end": "The Crossing Back",
        },
        {
            "id": "end_swap",
            "title": "The Life on the Other Shore",
            "text": "You trade. You take up the house you never bought, the street you never moved to, the answer you finally have. Whether it is better is a question that stops mattering the moment you stop asking it. You make tea in a kitchen that is now, by every measure, yours.",
            "end": "The Life on the Other Shore",
        },
        {
            "id": "end_ferryman",
            "title": "Last Call, Every Night",
            "text": "You take the wheel. Now it is you who waits at the water for the ones who wander down to it at midnight, unmoored, standing at a fork they cannot see the far side of. One crossing, you tell them, in your own gentle voice. You can ride over and look. Or you can ride back.",
            "end": "Last Call, Every Night",
        },
    ],
)


NIGHT_SHELF_SPECS = [
    MIDNIGHT_BAKERY,
    SIGNAL_HILL,
    TENANT_BELOW,
    CARTOGRAPHER,
    UNDERSTUDY,
    LAST_FERRY,
]
