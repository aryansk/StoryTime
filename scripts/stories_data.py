# -*- coding: utf-8 -*-
"""
Compact story specs for build_stories.py.

Each entry is (meta, scenes). See build_stories.py for the scene format.
Ratings/loved are mapped from the curator's 2025-26 watch list:
the ⭐ count becomes `rating`, a 🌟 becomes `loved`.

Stories are app-originals — "step inside" continuations and what-ifs of the
source title, not retellings of the plot.
"""

# ---------------------------------------------------------------------------
# Palm Royale — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
PALM_ROYALE = ({
    "id": "palm-royale-beach-ball",
    "title": "The Beach Ball",
    "sourceTitle": "Palm Royale",
    "kind": "show",
    "synopsis": "Palm Beach, 1969. The most exclusive ball of the season has one empty seat and you intend to fill it. Smile. Lie beautifully.",
    "releaseYear": 2024,
    "addedAt": "2026-05-29T00:00:00Z",
    "genre": "Comedy",
    "tags": ["socialites", "ambition", "disguise"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "The Front Door", "text": "The Palm Royale's brass doors have turned away duchesses. You have a borrowed Pucci dress, forty-one dollars, and a smile you have practiced in three mirrors. The doorman lifts an eyebrow.",
     "choices": [
        ("Sweep past as if you own the place", "Confidence is a kind of credential.", "s2"),
        ("Slip in through the cabana service path", "Servants' doors are never watched the way front ones are.", "s3"),
        ("Produce a forged sponsor's letter", "Ink and audacity. A dangerous pairing.", "s4"),
     ]},
    {"id": "s2", "title": "The Doyenne", "text": "Evelyn Rollins materializes like weather. \"I don't know you,\" she says, which is the worst thing a person can be here. Her eyes catalog your shoes.",
     "choices": [
        ("Drop a name she can't check", "A dead countess is a wonderful alibi.", "s5"),
        ("Compliment her late husband's foundation", "Flattery aimed at the dead rarely misses.", "s6"),
     ]},
    {"id": "s3", "title": "Cabana Row", "text": "The cabanas smell of coconut oil and money. A pool boy named Robert watches you not belong. He could shout. He doesn't.",
     "choices": [
        ("Tip him your last bill for silence", "Loyalty bought is loyalty, for an hour.", "s5"),
        ("Ask him who really runs this place", "The staff always knows where the bodies tan.", "s7"),
     ]},
    {"id": "s4", "title": "The Letter", "text": "The membership secretary reads your letter twice. The signature is good. The letterhead is better. \"Mrs. Donahue vouches for you?\" she asks.",
     "choices": [
        ("Insist, warmly, that you're old friends", "The bigger the lie, the straighter the back.", "s6"),
        ("Pivot to a different sponsor entirely", "Never defend a lie you can simply replace.", "s7"),
     ]},
    {"id": "s5", "title": "A Borrowed Name", "text": "By the bar you become someone with a yacht and a tragedy. People lean in. A widow named Norma watches you from her wheelchair, unblinking.",
     "choices": [
        ("Charm Norma directly", "She is the gate behind the gate.", "s8"),
        ("Avoid her and work the younger set", "The young are easier and poorer.", "s9"),
     ]},
    {"id": "s6", "title": "Norma's Rolodex", "text": "Evelyn, softened, lets slip that Norma keeps a card file of everyone's secrets. Whoever holds it holds the season. The file is upstairs.",
     "choices": [
        ("Plan to reach the file tonight", "Knowledge here is the only true currency.", "s8"),
        ("Decide the file is too dangerous to want", "Some doors are walls in disguise.", "s9"),
     ]},
    {"id": "s7", "title": "The Bartender Knows", "text": "The bartender mixes a grasshopper and a warning. \"They'll let you in,\" he says. \"They just won't ever let you leave clean.\" He slides you a key. Cabana 9.",
     "choices": [
        ("Pocket the key", "Every key is a question you'll have to answer later.", "s9"),
        ("Refuse it and stay visible", "Suspicion loves the person who hides.", "s8"),
     ]},
    {"id": "s8", "title": "The Luncheon", "text": "You are seated, somehow, at the good table. The conversation is a minefield of maiden names. Someone asks where you summered as a girl.",
     "choices": [
        ("Invent a lake nobody dares not to know", "Geography is forgiving to the bold.", "s10"),
        ("Turn the question back as a joke", "Deflection is its own elegance.", "s11"),
     ]},
    {"id": "s9", "title": "The Pool Boy's Tip", "text": "Robert finds you again. \"Norma's nurse takes a smoke break at four,\" he says, and walks off whistling. He has decided you are interesting, which is its own danger.",
     "choices": [
        ("Time your move to four o'clock", "Schedules are the soft spots of fortresses.", "s10"),
        ("Win Norma over honestly instead", "The long way is sometimes the only safe way.", "s12"),
     ]},
    {"id": "s10", "title": "The Fashion Show", "text": "Models drift down a poolside runway in next year's clothes. Evelyn places a hand on your arm — friendly, or a leash, you can't tell. A photographer circles.",
     "choices": [
        ("Pose for the photographer", "A picture is proof, and proof cuts both ways.", "s13"),
        ("Slip out of frame", "The uncaptured are the uncatchable.", "s14"),
     ]},
    {"id": "s11", "title": "The Rival", "text": "A woman named Dinah corners you with a smile like a paper cut. \"I looked you up,\" she says. \"Funny — you don't exist.\" She hasn't told anyone. Yet.",
     "choices": [
        ("Offer her something she wants", "Every rival is an ally who hasn't been paid.", "s13"),
        ("Threaten her with a bluff", "Show teeth and pray she doesn't count them.", "s14"),
     ]},
    {"id": "s12", "title": "Norma, Awake", "text": "Norma's grip is iron despite the chair. \"You're a fraud,\" she says, almost fondly. \"I was one too, once. It's exhausting, isn't it.\" She studies you like a daughter she might invent.",
     "choices": [
        ("Confess everything to her", "The truth, told to the right enemy, becomes armor.", "s15"),
        ("Deny it and hold your shape", "Never blink first at the queen.", "s14"),
     ]},
    {"id": "s13", "title": "The Charity Auction", "text": "Paddles rise for a diamond nobody needs. To bid is to be seen as somebody. To not bid is to be seen as nobody. You have forty-one dollars.",
     "choices": [
        ("Bid wildly on credit you don't have", "The chasm between seeming and being is one signature wide.", "s15"),
        ("Win the room without spending a cent", "The cleverest never open their purse.", "s16"),
     ]},
    {"id": "s14", "title": "The Blackmail Note", "text": "Someone slips a card under your door. They know your real name, your real address, your real nothing. Meet under the banyan at midnight, it says, or be announced.",
     "choices": [
        ("Go to the banyan tree", "Blackmail is a conversation you're allowed to win.", "s16"),
        ("Burn the note and run the ball anyway", "Sometimes nerve is the only reply.", "s17"),
     ]},
    {"id": "s15", "title": "The Husband", "text": "Evelyn's husband Skeet, half-asleep on Demerol and old money, takes a shine to you. His signature could open every account in Palm Beach. He offers you a pen.",
     "choices": [
        ("Take the pen and the access", "Power borrowed is power, until the lender wakes.", "s17"),
        ("Decline, gently, and keep his trust", "Restraint, here, looks almost like virtue.", "s18"),
     ]},
    {"id": "s16", "title": "Cracks Show", "text": "Your story is fraying at the cuffs. Two women whisper behind their fans. The season can smell blood, and it is patient about dinner.",
     "choices": [
        ("Get ahead of the rumor with a bigger one", "Drown a small fire in a flood.", "s17"),
        ("Find an exit and an alibi", "Know the back stairs before you need them.", "s18"),
     ]},
    {"id": "s17", "title": "Ballroom Rehearsal", "text": "The ballroom is being strung with ten thousand lights for tomorrow's Beach Ball. You will be in this room. The only question left is as what.",
     "choices": [
        ("Plan to be crowned the season's hostess", "Aim at the throne or don't aim at all.", "s19"),
        ("Plan a quieter, safer triumph", "Survival can be its own kind of victory.", "s18"),
     ]},
    {"id": "s18", "title": "The Photographer Returns", "text": "The press man has a photo of you slipping through the cabana door on day one. \"Page six,\" he says, \"or page nobody. Your choice, and your favor.\"",
     "choices": [
        ("Trade him a juicier secret", "Feed the wolf someone else's hand.", "s19"),
        ("Charm him into burying it", "Charm is cheaper than secrets and twice as fast.", "s20"),
     ]},
    {"id": "s19", "title": "Night of the Ball", "text": "The ballroom blazes. Every name you have borrowed and broken is here under one roof. Evelyn taps a glass. Norma watches from the dark edge, smiling at no one.",
     "choices": [
        ("Step into the light and take the floor", "The center of the room is where masks come off — or weld on.", "s20"),
        ("Work the margins and stay legible", "Let the spotlight find someone hungrier.", "s21"),
     ]},
    {"id": "s20", "title": "The Toast", "text": "A glass is pressed into your hand and the room turns to you, expecting words. Whatever you say next becomes the truth about who you are here.",
     "choices": [
        ("Toast to the season and your new life", "Claim the lie out loud and watch it set like cement.", "s21"),
        ("Toast to Norma — and tell the truth", "Honesty, in a room of liars, is the loudest sound there is.", "end_truth"),
        ("Use the toast to expose the whole rotten club", "Burn it down and see who runs for the doors.", "end_expose"),
     ]},
    {"id": "s21", "title": "Crowned", "text": "They are applauding. You did it. The orchestra swells and Robert, by the doors, gives you a small, sad nod — he, at least, remembers who walked in.",
     "choices": [
        ("Accept the crown and become Mrs. Palm Beach", "Some prisons have wonderful views.", "end_queen"),
        ("Walk out the front door, free and forty-one dollars richer", "The only way to win the game is to leave the table.", "end_exit"),
     ]},
    {"id": "end_queen", "title": "Queen of the Season", "text": "You marry the right name and bury the wrong one. For thirty years you reign over the Palm Royale, terrified every single morning that someone will remember the cabana door. Nobody ever does. That is the cruelest part.",
     "end": "Queen of the Season"},
    {"id": "end_truth", "title": "The Honest Fraud", "text": "Norma laughs until she coughs, then has them set you a permanent place at her table. \"A fraud who admits it,\" she wheezes, \"is just an honest woman with ambition.\" You are in. You are also, finally, yourself.",
     "end": "The Honest Fraud"},
    {"id": "end_expose", "title": "Scorched Earth", "text": "By dawn the columns are full of it — the affairs, the ledgers, the borrowed everything. The Palm Royale never recovers its shine. Neither do you, exactly, but you taught a roomful of queens that their crowns were rented too.",
     "end": "Scorched Earth"},
    {"id": "end_exit", "title": "The Front Door, Going Out", "text": "You leave the way they never expected — through the brass doors, into the salt night, owing no one a name. Behind you the lights blaze on for people who can never leave. Ahead of you, the dark is wide open.",
     "end": "The Front Door, Going Out"},
])


# ---------------------------------------------------------------------------
# Him and Hers — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
HIM_AND_HERS = ({
    "id": "him-and-hers-the-recording",
    "title": "The Recording",
    "sourceTitle": "Him and Hers",
    "kind": "show",
    "synopsis": "A couple, a perfect apartment, and a voice memo neither of you meant to leave running. The truth has forty-three minutes and a timestamp.",
    "releaseYear": 2025,
    "addedAt": "2026-05-28T00:00:00Z",
    "genre": "Thriller",
    "tags": ["marriage", "secrets", "unreliable"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "43:07", "text": "You find it by accident — a voice memo on the shared phone, recorded last Thursday, forty-three minutes long. Neither of you remembers making it. The waveform twitches like something breathing.",
     "choices": [
        ("Play it from the beginning", "Some doors only open inward.", "s2"),
        ("Delete it without listening", "Ignorance is a room you can never re-enter.", "s3"),
        ("Copy it somewhere safe first", "Trust, but keep a key.", "s4"),
     ]},
    {"id": "s2", "title": "Her Voice", "text": "It's her, in the kitchen, talking low to someone who isn't you. \"He can't know yet,\" she says. A man's laugh, familiar and wrong. Then a clatter, and the recording keeps going.",
     "choices": [
        ("Keep listening for the man's name", "A name is a wound you can't unfeel.", "s5"),
        ("Confront her right now", "Some accusations can't wait for evidence.", "s6"),
     ]},
    {"id": "s3", "title": "The Empty Space", "text": "You delete it. For three days you are calm the way a held breath is calm. Then the cloud restores it automatically at 2 a.m., and the phone lights up the ceiling.",
     "choices": [
        ("Listen now, in the dark, beside her sleeping", "The dark makes liars of us and honest men too.", "s5"),
        ("Wake her and demand the truth", "Sleep is no place to hide from a marriage.", "s6"),
     ]},
    {"id": "s4", "title": "The Backup", "text": "You email the file to yourself and lock the phone. The act of saving it changes you — you are now a person who collects evidence against the person you love.",
     "choices": [
        ("Listen to all forty-three minutes alone", "Solitude is where suspicion grows teeth.", "s5"),
        ("Take it to a friend for a second ear", "Two listeners, one truth, three problems.", "s7"),
     ]},
    {"id": "s5", "title": "The Name", "text": "At minute nineteen the man says his own name, casually, and your stomach drops three floors. You know him. He was at your wedding. He gave a toast.",
     "choices": [
        ("Call him and say nothing, just listen", "Silence on the line is its own interrogation.", "s8"),
        ("Tell no one and watch them both", "Patience is the predator's only real weapon.", "s9"),
     ]},
    {"id": "s6", "title": "The Confrontation", "text": "She goes very still when you press play. \"That's not what it sounds like,\" she says — which is what everyone says, and sometimes, terribly, it's even true.",
     "choices": [
        ("Believe her and ask her to explain", "Faith offered is a bridge across a flood.", "s10"),
        ("Refuse to believe and push harder", "Push hard enough and even the truth runs.", "s11"),
     ]},
    {"id": "s7", "title": "The Second Ear", "text": "Your friend listens twice, frowning. \"That's weird,\" they say. \"There's a third voice. Real quiet. Around minute thirty.\" You hadn't heard it. You weren't meant to.",
     "choices": [
        ("Isolate the third voice", "The thing in the background is always the thing.", "s8"),
        ("Decide the friend is mistaken", "Doubt aimed outward is doubt you don't have to feel.", "s9"),
     ]},
    {"id": "s8", "title": "The Third Voice", "text": "Cleaned up, the third voice is unmistakable. It's yours. You are on the recording, in a conversation you have no memory of having. You sound calm. You sound like you knew.",
     "choices": [
        ("Try to remember that night", "Memory is a witness that has been bribed.", "s12"),
        ("Assume the recording was faked", "Denial is a comfortable house with no exits.", "s13"),
     ]},
    {"id": "s9", "title": "Watching", "text": "For a week you become a scholar of her phone, her late returns, the new way she says your name. The apartment fills with a silence that has a shape, and the shape is a question.",
     "choices": [
        ("Set a trap to catch them together", "Bait the room and wait for hunger.", "s14"),
        ("Realize you can't live like this", "Surveillance is a cage you build around yourself.", "s15"),
     ]},
    {"id": "s10", "title": "Her Explanation", "text": "She tells you the man is helping her plan something — and the something involves you, and a date, and a word she won't say yet. \"You weren't supposed to find it like this,\" she whispers.",
     "choices": [
        ("Let her finish the secret on her terms", "Some surprises are mercy, not betrayal.", "s16"),
        ("Demand the whole truth tonight", "Trust given conditionally isn't quite given.", "s11"),
     ]},
    {"id": "s11", "title": "The Crack", "text": "You push, and something breaks that won't unbreak. She stops defending herself and starts, quietly, defending the door — putting her body between you and the hallway, the bedroom, the truth.",
     "choices": [
        ("Step back and apologize", "The hardest reverse is the one you owe.", "s16"),
        ("Step forward and open the door yourself", "Some men have to see the room to believe it's empty.", "s17"),
     ]},
    {"id": "s12", "title": "That Night", "text": "It comes back in fragments — wine, the man, a plan whispered in the kitchen, your own voice agreeing to something. You did know. Then you took something to forget, because forgetting was the kindest version.",
     "choices": [
        ("Choose to remember all of it", "Pain you choose is still yours to keep.", "s18"),
        ("Take the pill again and forget once more", "The cleanest loop is the one you can't see closing.", "end_loop"),
     ]},
    {"id": "s13", "title": "Forensics", "text": "You pay a stranger to analyze the file. \"Nothing's spliced,\" he says, sliding it back. \"This is one continuous recording. Whatever happened, happened in one room, in one night, with all three of you in it.\"",
     "choices": [
        ("Accept it really happened", "Acceptance is the first honest breath.", "s18"),
        ("Destroy the file and the analysis", "You can't un-know, but you can refuse to know louder.", "s15"),
     ]},
    {"id": "s14", "title": "The Trap", "text": "You tell her you'll be away overnight, then sit in your car across the street watching your own lit windows. At 9:14 the buzzer light flickers. Someone is coming up.",
     "choices": [
        ("Go up and face whoever it is", "The truth lives at the top of the stairs.", "s17"),
        ("Wait and photograph who leaves", "Evidence over confrontation — colder, surer.", "s19"),
     ]},
    {"id": "s15", "title": "The Edge of Leaving", "text": "You pack a bag you don't zip. The decision to go and the decision to stay take turns wearing your face. She finds you sitting on the unmade bed at 3 a.m., the bag between you like a third person.",
     "choices": [
        ("Tell her you're leaving", "Honesty about your own exit is still honesty.", "s20"),
        ("Tell her you want to understand first", "Curiosity can outlast even heartbreak.", "s16"),
     ]},
    {"id": "s16", "title": "The Real Secret", "text": "She finally says it: the man was helping her arrange a vow renewal, a second wedding, a do-over of the day you both quietly believe you failed the first time. The recording was a rehearsal she meant to delete.",
     "choices": [
        ("Believe the beautiful version", "Sometimes the kind story is also the true one.", "end_renewal"),
        ("Notice the timeline doesn't add up", "Love is no excuse to stop counting.", "s18"),
     ]},
    {"id": "s17", "title": "Top of the Stairs", "text": "The door opens before you knock. The man from the wedding is there, and behind him, the apartment is full of half-hung banners and a cake box. He looks more frightened than guilty.",
     "choices": [
        ("Lower your fists and ask what this is", "The bravest thing is to be wrong gently.", "s16"),
        ("Demand they both explain, now", "You've earned the whole story, even if it costs you.", "s18"),
     ]},
    {"id": "s18", "title": "The Whole Truth", "text": "When every voice on the recording has been accounted for, what's left is uglier and smaller than betrayal: a misunderstanding three people fed until it grew teeth. The harm is real even if the affair was never.",
     "choices": [
        ("Forgive her, and yourself", "Grace is the only repair that holds.", "end_forgive"),
        ("Decide the trust is gone regardless", "Some glass, once spidered, is just waiting to fall.", "s20"),
        ("Make a new recording — the truth, on the record", "End the loop by saying it out loud, forever.", "end_record"),
     ]},
    {"id": "s19", "title": "The Photograph", "text": "At 11:02 the door opens and a figure leaves, face turned away, carrying a flat white box. Your camera captures everything except the one thing you need: certainty about who it is.",
     "choices": [
        ("Chase them down the street", "Proof is worth a little dignity.", "s17"),
        ("Go up and see the apartment yourself", "The scene speaks louder than the suspect.", "s17"),
     ]},
    {"id": "s20", "title": "The Leaving", "text": "You go. Not in a storm but in a slow, terrible politeness — keys on the counter, the recording still saved, the apartment learning your absence room by room. She doesn't stop you. That, too, is an answer.",
     "choices": [
        ("Take the recording with you", "Carry the proof like a stone in a coat.", "end_leave"),
        ("Leave it behind, deleted at last", "Set the thing down and walk out lighter.", "end_clean"),
     ]},
    {"id": "end_loop", "title": "Forty-Three Minutes, Forever", "text": "You take the pill. The recording restores itself next Thursday. You find it by accident, forty-three minutes long, and the waveform twitches like something breathing. You have done this before. You will do it again.",
     "end": "Forty-Three Minutes, Forever"},
    {"id": "end_renewal", "title": "Second Vows", "text": "Three weeks later you stand where the banners were, saying the words again and meaning them harder. The recording lives in a folder marked KEEP. Some evidence is of love.",
     "end": "Second Vows"},
    {"id": "end_forgive", "title": "The Repair", "text": "Forgiveness isn't a moment, it turns out — it's a chore you do every morning, like coffee. But the apartment stops being a crime scene and starts, slowly, being a home again. You leave the phone face-down. You sleep.",
     "end": "The Repair"},
    {"id": "end_record", "title": "On the Record", "text": "You sit her down and press record yourselves. Forty-three minutes of the actual truth, ugly and ordinary, spoken aloud so neither of you can edit it later. When it ends, the silence is finally just silence.",
     "end": "On the Record"},
    {"id": "end_leave", "title": "The Stone in the Coat", "text": "You keep the recording for years, playing it on bad nights to remind yourself you were right to go — or to wonder if you were wrong. It never tells you. Proof, you learn, is not the same as peace.",
     "end": "The Stone in the Coat"},
    {"id": "end_clean", "title": "Lighter", "text": "Deleted, finally and on purpose, the file takes its weight with it. You don't know the whole truth and you decide you can live without it. The street outside is cold and clear and entirely your own.",
     "end": "Lighter"},
])


# ---------------------------------------------------------------------------
# The Lost Bus — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
THE_LOST_BUS = ({
    "id": "the-lost-bus-evacuation",
    "title": "The Last Road Out",
    "sourceTitle": "The Lost Bus",
    "kind": "movie",
    "synopsis": "A school bus, twenty-two children, and a wildfire that has already eaten the only road home. You are driving. Don't look in the mirror.",
    "releaseYear": 2025,
    "addedAt": "2026-05-27T00:00:00Z",
    "genre": "Drama",
    "tags": ["wildfire", "rescue", "courage"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Last Bell", "text": "The sky over the school is the wrong color — a brown-orange you've only seen at sunset, and it's noon. The dispatcher's voice cracks: \"Get them out, now.\" Twenty-two kids file onto your bus, too quiet.",
     "choices": [
        ("Take the highway, the fast way", "Speed is safety until it isn't.", "s2"),
        ("Take the ridge road, the long way", "The longer road is sometimes the only road.", "s3"),
        ("Wait for the convoy to form up", "There is strength in numbers and danger in delay.", "s4"),
     ]},
    {"id": "s2", "title": "The Highway", "text": "The on-ramp is a parking lot of brake lights and ash. Embers the size of fists drift across the windshield. A boy named Marcus asks if his house is okay. You don't know how to lie to a child.",
     "choices": [
        ("Tell him the truth, gently", "Children survive honesty better than we think.", "s5"),
        ("Tell him everyone's going to be fine", "A kind lie can be a kind of bridge.", "s6"),
     ]},
    {"id": "s3", "title": "The Ridge Road", "text": "The ridge gives you a view you'll never unsee: the whole valley below is a sheet of moving fire, and it is climbing. But up here the road is clear. For now.",
     "choices": [
        ("Push the bus faster on the gravel", "Trade traction for time and pray.", "s5"),
        ("Slow down for the blind curves", "A controlled bus is a living bus.", "s7"),
     ]},
    {"id": "s4", "title": "The Convoy", "text": "Three other buses and a fire crew gather in the lot. The captain shouts orders, but there's no time and no consensus — and the smoke is already thickening at the fence line.",
     "choices": [
        ("Break from the convoy and go alone", "Sometimes the group is just a slower target.", "s3"),
        ("Follow the fire crew's lead vehicle", "Trust the people who run toward this.", "s7"),
     ]},
    {"id": "s5", "title": "The Wall of Smoke", "text": "The road vanishes into a gray nothing. Your headlights die against it. A girl in the front seat takes your sleeve. \"I can't see,\" she says, and neither can you.",
     "choices": [
        ("Crawl forward at walking pace", "Faith in a road you can't see is the whole job.", "s8"),
        ("Stop and wait for the smoke to shift", "Stillness in a fire is a terrible gamble.", "s9"),
     ]},
    {"id": "s6", "title": "Marcus Knows", "text": "Marcus looks out the window at his street going by, the flames already in it, and stops asking questions. His silence is louder than any scream. The other kids feel it spread.",
     "choices": [
        ("Get them singing to break the fear", "Noise is a rope thrown to the drowning.", "s19"),
        ("Give Marcus a job to do", "Purpose is the antidote to panic.", "s9"),
     ]},
    {"id": "s19", "title": "The Animal on the Road", "text": "A deer stands frozen in your high beams, flanks heaving, a refugee like the rest of you. Behind it the brush is already glowing. The kids press to the windows.",
     "choices": [
        ("Edge around it and keep moving", "Mercy is a luxury the fire doesn't grant.", "s8"),
        ("Lean on the horn to send it running", "Save what you can, even what isn't yours to save.", "s11"),
     ]},
    {"id": "s7", "title": "The Lead Vehicle", "text": "You follow the fire truck's taillights like a prayer. Then it turns down a side road and is gone, and a downed power line writhes across the path ahead, throwing sparks.",
     "choices": [
        ("Drive over the line fast", "Rubber tires, steady nerves, no brakes.", "s8"),
        ("Find another way around", "Respect the things that can kill you sideways.", "s10"),
     ]},
    {"id": "s8", "title": "The Bridge", "text": "Through the smoke: a bridge, the only crossing for miles, and it's already burning at the far end. The fire hasn't reached the deck yet. You have maybe ninety seconds.",
     "choices": [
        ("Floor it across the bridge", "Hesitation is the only thing that can't survive here.", "s11"),
        ("Reverse and find the old ford downstream", "Water is a road too, if you're brave enough.", "s12"),
     ]},
    {"id": "s9", "title": "Trapped", "text": "The fire flanks you — there's flame on both shoulders now and the heat is warping the air. A child is crying without sound. The radio is just static and someone, somewhere, screaming a road name.",
     "choices": [
        ("Shelter in place and seal the bus", "When you can't outrun it, you outlast it.", "s13"),
        ("Make a run for the reservoir clearing", "One gap in the wall is all you need.", "s11"),
     ]},
    {"id": "s10", "title": "The Detour", "text": "The side road is barely a road — washboard dirt narrowing into trees that are starting to torch one by one, like matches in a row. But it bends away from the worst of it.",
     "choices": [
        ("Commit to the detour fully", "The road less burning.", "s12"),
        ("Turn back toward the highway after all", "Sometimes retreat is the only advance.", "s20"),
     ]},
    {"id": "s20", "title": "Smoke in the Cabin", "text": "Smoke is seeping through the old door seals now, and a small voice in the back starts to cough, then another. The air inside the bus is becoming the thing you were driving away from.",
     "choices": [
        ("Seal the vents and ride it out", "Trap the good air and hoard it like gold.", "s13"),
        ("Make a hard run for clearer air", "Outrun the cloud or become it.", "s11"),
     ]},
    {"id": "s11", "title": "Through the Gap", "text": "There's a seam in the fire — a corridor of merely terrible heat between two walls of worse. It's closing. The bus groans up to speed. The kids have stopped making any sound at all.",
     "choices": [
        ("Drive straight through the corridor", "Aim at the gap and refuse to blink.", "s14"),
        ("Use the reservoir to wet the bus first", "A soaked machine buys a few precious degrees.", "s13"),
     ]},
    {"id": "s12", "title": "The River Ford", "text": "The old crossing is low water over smooth stone. The far bank is dark — unburned. But the current is faster than it looks and the bus is heavy with frightened cargo.",
     "choices": [
        ("Ease across the ford slowly", "Read the water like a road.", "s14"),
        ("Power across before the engine drowns", "Momentum is a kind of buoyancy.", "s15"),
     ]},
    {"id": "s13", "title": "Shelter in Place", "text": "You park in the reservoir clearing, kill the engine, tape the vents, and have the kids lie on the floor under coats. The fire arrives like a freight train made of weather. Then it passes, roaring, over and around.",
     "choices": [
        ("Wait until the heat truly breaks", "Patience is the bravest thing in a furnace.", "s16"),
        ("Move the moment the front passes", "The window after the wave is narrow and real.", "s15"),
     ]},
    {"id": "s14", "title": "The Far Side", "text": "The bus bursts out of the smoke into clear gray air. Behind you the world is ending; ahead, impossibly, a road sign, intact, pointing toward town. A few kids start to cry — the good kind.",
     "choices": [
        ("Radio your survivors' count to dispatch", "Every name said aloud is a name saved.", "s16"),
        ("Push on without stopping", "Don't trust safety until you're standing in it.", "s17"),
     ]},
    {"id": "s15", "title": "Engine Trouble", "text": "The bus coughs, sputters, and the temperature needle pins red. You're almost clear — almost. Steam rolls from under the hood. Twenty-two kids, one dying engine, and not quite enough road.",
     "choices": [
        ("Nurse it forward in low gear", "Coax the machine like a frightened animal.", "s17"),
        ("Stop and lead the kids out on foot", "When the metal fails, the legs decide.", "s18"),
     ]},
    {"id": "s16", "title": "The Count", "text": "You make them line up and count off the way you've practiced a hundred bored mornings. The numbers climb — eighteen, nineteen, twenty — and then a pause that stops your heart before someone small says \"twenty-one\" and another, \"twenty-two.\"",
     "choices": [
        ("Drive the last miles to the shelter", "The end of the road is the start of the rest.", "s17"),
        ("Stop to help another stranded vehicle", "There's always one more name to save.", "s18"),
     ]},
    {"id": "s17", "title": "Town Lights", "text": "The shelter parking lot is full of flashing lights and reaching arms. Parents run at the bus before it's fully stopped. You open the door and a wall of crying, hugging, breathing humanity pours in.",
     "choices": [
        ("Hand each child to someone who loves them", "This is the only paperwork that matters.", "end_home"),
        ("Go back out for the ones still on the mountain", "Heroes are just people who can't sit still.", "s18"),
     ]},
    {"id": "s18", "title": "One More Run", "text": "Empty now, the bus feels enormous. The fire's glow still pulses to the east, and the radio is full of names of roads, of children, of people not yet counted. Your hands are shaking. The engine is still warm.",
     "choices": [
        ("Turn around and drive back in", "The bravest tank is the one that's nearly empty.", "end_again"),
        ("Stay, rest, let the crews take it", "You can't pour from a tank that's run dry.", "end_rest"),
     ]},
    {"id": "end_home", "title": "Everyone Home", "text": "Twenty-two children, twenty-two reunions. You don't remember driving back to the depot. Months later a kid you don't recognize hugs your knees in a grocery store and won't let go, and you finally, quietly, fall apart in the cereal aisle.",
     "end": "Everyone Home"},
    {"id": "end_again", "title": "The Second Trip", "text": "You go back in. Of course you do. The mountain is a cathedral of fire and you drive into it because somewhere up there is someone's whole world, waiting on a roadside. They never give medals for the trips that count. You don't want one.",
     "end": "The Second Trip"},
    {"id": "end_rest", "title": "The Weight You Carry", "text": "You let the crews take the next run, and for the rest of your life you wonder about it — not with guilt exactly, but with the quiet arithmetic of a person who did enough and will never quite believe it. The kids you saved grow up. That has to be the answer. It is.",
     "end": "The Weight You Carry"},
])


# ---------------------------------------------------------------------------
# Are You There God? It's Me, Margaret. — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
MARGARET = ({
    "id": "margaret-sixth-grade",
    "title": "Me and Sixth Grade and God",
    "sourceTitle": "Are You There God? It's Me, Margaret.",
    "kind": "movie",
    "synopsis": "New town, new school, new everything. You're eleven, you're waiting for your body and your faith to make up their minds, and you keep talking to a God you're not sure is listening.",
    "releaseYear": 2023,
    "addedAt": "2026-05-26T00:00:00Z",
    "genre": "Drama",
    "tags": ["coming-of-age", "friendship", "faith"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "Moving Day", "text": "The boxes smell like the old apartment and the new house echoes. From your window you can see a girl your age doing cartwheels on the next lawn. Are you there, God? It's me. Please don't let me be the weird new kid.",
     "choices": [
        ("Go outside and say hi", "Brave is just scared with its shoes on.", "s2"),
        ("Stay in and unpack your room first", "Some courage needs a running start.", "s3"),
     ]},
    {"id": "s2", "title": "The Cartwheel Girl", "text": "Her name is Nancy and she talks fast and decides things. By the end of the driveway you have a friend and, apparently, opinions about boys you've never met. It's dizzying and wonderful.",
     "choices": [
        ("Agree with everything she says", "Fitting in feels like floating.", "s4"),
        ("Quietly keep your own opinions too", "You can belong without disappearing.", "s5"),
     ]},
    {"id": "s3", "title": "The First Prayer", "text": "Alone in the half-empty room you do the thing you always do — you talk to God, plainly, like a pen pal. No temple, no church, just you and the ceiling and a long list of worries.",
     "choices": [
        ("Ask God to make sixth grade easy", "Hope is a kind of homework.", "s4"),
        ("Ask God which religion you're supposed to be", "The biggest questions arrive in the smallest rooms.", "s6"),
     ]},
    {"id": "s4", "title": "Nancy's Secret Club", "text": "Nancy forms a club with three other girls and you. There are rules: you keep a notebook, you rank the boys, and you must tell each other the instant anything happens. Anything.",
     "choices": [
        ("Join enthusiastically", "Four best friends is a fortress.", "s5"),
        ("Join, but feel a little uneasy about the rules", "A club can be a cage with cushions.", "s6"),
     ]},
    {"id": "s5", "title": "We Must, We Must", "text": "The club has an exercise to help you grow up faster, arms pumping, chanting at the ceiling. You laugh until you're breathless. Then someone asks who's gotten their period and the room goes quiet.",
     "choices": [
        ("Admit you haven't and don't care", "Honesty is its own kind of cool.", "s7"),
        ("Pretend you're close, like the others", "Small lies grow in the dark.", "s8"),
     ]},
    {"id": "s6", "title": "The Religion Assignment", "text": "Your teacher assigns a year-long project: pick something important to you and study it. You know instantly. You'll study whether you have a religion at all, since nobody ever told you.",
     "choices": [
        ("Visit a temple with Grandma Sylvia", "Start with the family that claims you loudest.", "s7"),
        ("Visit a church with a new friend", "Try on a faith and see if it itches.", "s8"),
     ]},
    {"id": "s7", "title": "Grandma Sylvia", "text": "Grandma Sylvia takes you to temple and to lunch and to the edge of feeling like you finally belong somewhere. But she also calls you 'her little Jewish girl,' and that word lands heavier than she means.",
     "choices": [
        ("Tell her you're still deciding", "Loving someone and disagreeing are allowed at once.", "s9"),
        ("Let her believe what makes her happy", "Kindness sometimes wears a small surrender.", "s10"),
     ]},
    {"id": "s8", "title": "The Other Grandparents", "text": "Your mother's parents, who once disowned her for marrying outside the faith, send a sudden letter. They want to visit. Your parents go pale and polite in that grown-up way.",
     "choices": [
        ("Hope the visit fixes everything", "Children are the bridges adults won't build.", "s9"),
        ("Worry it'll all blow up", "You can feel a storm before it has a name.", "s10"),
     ]},
    {"id": "s9", "title": "The List of Boys", "text": "Back in the club, the notebook comes out. You're supposed to write your number-one boy. Philip Leroy is everyone's pick — perfect, mean, and boring, you secretly think. There's also quiet Norman from math.",
     "choices": [
        ("Write Philip to match the group", "Sometimes you vote with the room.", "s11"),
        ("Write who you actually like", "A true answer in a notebook of lies is a small rebellion.", "s12"),
     ]},
    {"id": "s10", "title": "Are You There, God?", "text": "Late at night you ask God the real questions — about your body, your friends, your two sets of grandparents pulling you like taffy. The ceiling, as always, doesn't answer in words. But you feel a little less alone for asking.",
     "choices": [
        ("Decide God is listening", "Faith is choosing to leave the line open.", "s11"),
        ("Decide you'll figure it out yourself", "Growing up is partly learning to answer your own prayers.", "s12"),
     ]},
    {"id": "s11", "title": "The Party", "text": "A boy-girl party. There's a closet, a spinning bottle, and a rule called Two Minutes in Heaven that makes your stomach drop. Nancy's already pushing you toward the circle.",
     "choices": [
        ("Take your turn even though you're nervous", "Brave is scared with its shoes on, remember.", "s13"),
        ("Sit this one out without apology", "No is a complete sentence, even at eleven.", "s14"),
     ]},
    {"id": "s12", "title": "Norman, Actually", "text": "You end up talking to quiet Norman by the snack table about nothing and everything for an hour. It isn't a movie kiss. It's better — it's easy. Nancy will be horrified, which makes it sweeter.",
     "choices": [
        ("Tell the club the truth about Norman", "Owning your own crush is its own bravery.", "s13"),
        ("Keep this one just for yourself", "Some good things shrink when shared.", "s14"),
     ]},
    {"id": "s13", "title": "The Period Panic", "text": "It feels like everyone is crossing a finish line you can't even see. Gretchen gets hers. Then Nancy claims she did — loudly, with details. You're starting to suspect she's lying, and you don't know what's worse: that, or still being last.",
     "choices": [
        ("Call out Nancy's lie gently", "Truth between friends is risky and necessary.", "s15"),
        ("Say nothing and feel left behind", "Waiting is the loneliest verb in sixth grade.", "s16"),
     ]},
    {"id": "s14", "title": "Laura Danker", "text": "Everyone whispers cruel things about Laura, the tall girl who developed early, as if her body did something wrong on purpose. One day you're partnered with her and discover she's just... a person. A nice one.",
     "choices": [
        ("Defend Laura to the club", "It costs something to be kind out loud.", "s15"),
        ("Stay quiet to keep the peace", "Silence can be a small betrayal you carry.", "s16"),
     ]},
    {"id": "s15", "title": "The Falling Out", "text": "It happens the way these things do — fast and over something small. Nancy turns the club against you, or you walk away from it; either way the fortress has a wall down the middle now, and you're on the outside.",
     "choices": [
        ("Try to apologize and rebuild", "Mending takes more nerve than breaking.", "s17"),
        ("Decide you're better off without the rules", "Some friendships fit you, and some you just fit into.", "s18"),
     ]},
    {"id": "s16", "title": "The Visit Goes Wrong", "text": "Both sets of grandparents end up in your living room at once, and decades of hurt come out over the good china. They argue about whose religion you'll be — as if you're not standing right there.",
     "choices": [
        ("Stay quiet and let the adults fight", "Sometimes the smallest person sees the most.", "s17"),
        ("Speak up about how it makes you feel", "Even kids get a vote in their own souls.", "s18"),
     ]},
    {"id": "s17", "title": "Are You Even There?", "text": "After everything — the friends, the grandparents, the body that won't cooperate — you get angry at God for the first time. You tell Him you stopped hearing back and you're not sure you'll keep calling.",
     "choices": [
        ("Keep talking to God anyway", "Doubt and faith can share a room.", "s19"),
        ("Take a break from praying", "Sometimes you put the phone down and grow.", "s20"),
     ]},
    {"id": "s18", "title": "Choosing for Yourself", "text": "You realize the religion project was never really about temple or church. It was about who gets to decide what you believe — and the answer, finally, scary and freeing, is you.",
     "choices": [
        ("Write the project about your own searching", "The truest answer is that you're still looking.", "s19"),
        ("Decide you don't need a label yet", "Some questions get to stay open.", "s20"),
     ]},
    {"id": "s19", "title": "Finally", "text": "It comes, the thing you waited for, on an ordinary afternoon with no fanfare at all. You lock the bathroom door and laugh and almost cry, and the very first thing you do is talk to God — not asking for anything this time. Just to share.",
     "choices": [
        ("Thank God, and mean it", "Gratitude reopens every line you thought went dead.", "s21"),
        ("Call Nancy first, then God", "Some news belongs to your people.", "s21"),
     ]},
    {"id": "s20", "title": "Just You", "text": "Nothing dramatic happens. You just wake up one day a little surer of yourself — about friends, about faith, about the long strange project of becoming a person. The waiting, it turns out, was part of the growing.",
     "choices": [
        ("Make peace with not having all the answers", "Eleven is allowed to be a question mark.", "s21"),
        ("Promise yourself you'll keep asking the big questions", "The asking is the faith.", "s21"),
     ]},
    {"id": "s21", "title": "Sixth Grade, Survived", "text": "The year ends. You are taller, braver, and exactly as confused about God as ever — but it's a comfortable confusion now, a conversation rather than a crisis. You did it. You're still you, only more so.",
     "choices": [
        ("Choose faith, on your own terms", "Belief you pick yourself fits best.", "end_faith"),
        ("Choose your friends, mended and real", "The people who stay are the answer to half your prayers.", "end_friends"),
        ("Choose just being eleven, fully", "Some years you win by simply living them.", "end_self"),
     ]},
    {"id": "end_faith", "title": "On My Own Terms", "text": "You don't end up Jewish or Christian, exactly. You end up something quieter and yours — a person who keeps the line to God open out of choice, not habit. Grandma Sylvia is a little sad. You are, for the first time, sure.",
     "end": "On My Own Terms"},
    {"id": "end_friends", "title": "The Fortress, Rebuilt", "text": "You and Nancy patch things up the imperfect way real friends do, with an apology that's half mumbled and a forgiveness that's mostly just showing up. The club drops its silly rules. What's left is the part that was always worth keeping.",
     "end": "The Fortress, Rebuilt"},
    {"id": "end_self", "title": "Are You There? It's Me.", "text": "In the end the biggest thing you grew wasn't your body or your faith — it was you, the part that talks to God at night and means it. You're eleven, almost twelve, and for one perfect summer evening that feels like exactly enough.",
     "end": "Are You There? It's Me."},
])


# ---------------------------------------------------------------------------
# Shrinking (Season 3) — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
SHRINKING = ({
    "id": "shrinking-the-honest-week",
    "title": "The Honest Week",
    "sourceTitle": "Shrinking",
    "kind": "show",
    "synopsis": "You're a grieving therapist who has started saying the unsayable thing out loud to your patients. It keeps working. It also keeps blowing up your life. One week. No filter.",
    "releaseYear": 2025,
    "addedAt": "2026-05-25T00:00:00Z",
    "genre": "Comedy",
    "tags": ["grief", "therapy", "friendship"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "Monday, 9 a.m.", "text": "Your first patient has spent two years circling the same problem and you, running on bad sleep and worse grief, are about to do the thing they tell you in school never to do: tell him exactly what you think.",
     "choices": [
        ("Tell him to leave his terrible job today", "Some advice is malpractice that happens to work.", "s2"),
        ("Stay professional and let him circle", "The textbook is boring for a reason.", "s3"),
     ]},
    {"id": "s2", "title": "It Worked. Uh Oh.", "text": "He quits by lunch and calls you crying with joy. You feel like a genius and a fraud at once. Your mentor Paul appears in your doorway with the face of a man who has heard things.",
     "choices": [
        ("Tell Paul your new method is brilliant", "Confidence is easy until someone wiser frowns.", "s4"),
        ("Downplay it and promise to be careful", "A small lie to a mentor is a tax you'll repay.", "s5"),
     ]},
    {"id": "s3", "title": "The Slow Way", "text": "You do it right and it's agony — forty-five minutes of careful nudging while the answer sits in the room like a piano nobody will play. He leaves no better. You wonder who the caution is really protecting.",
     "choices": [
        ("Resolve to try the honest way next time", "Patience has limits, and so do you.", "s4"),
        ("Recommit to doing the job properly", "There's wisdom in the boring path too.", "s6"),
     ]},
    {"id": "s4", "title": "Paul's Warning", "text": "Paul, leaning on his cane and his decades, says, \"You're not healing them, you're using them.\" It stings because it's at least partly true. His Parkinson's tremor is worse today; he hates that you noticed.",
     "choices": [
        ("Ask Paul how he's really doing", "Care him back; he's a patient who refuses to be one.", "s5"),
        ("Defend your methods to him", "Pride is loudest right before a fall.", "s6"),
     ]},
    {"id": "s5", "title": "Home, Sort Of", "text": "Your daughter Alice is seventeen and grieving her mom in the next room with the door closed. You've been so busy fixing strangers that the most important patient in your life keeps her own counsel.",
     "choices": [
        ("Knock and just listen, no fixing", "Sometimes love is a closed mouth and an open ear.", "s7"),
        ("Try to fix her grief like a session", "The cobbler's kid has the worst shoes.", "s8"),
     ]},
    {"id": "s6", "title": "The Patient You Dread", "text": "Sean, the young veteran with the rage he can't land anywhere safe, has been living in your guest house and your head. He's better and angrier in turns. Today he punched a wall — and almost a person.",
     "choices": [
        ("Push him hard, therapist to friend", "The line between the two is where the work lives.", "s7"),
        ("Give him room and time", "Pressure and patience are both medicines, dosed wrong they're poison.", "s8"),
     ]},
    {"id": "s7", "title": "Gaby and the Truth", "text": "Your colleague Gaby calls you out over coffee: you've been hiding inside everyone else's problems to avoid your own. She's right, she's kind, and she's a little in love with you, which complicates the rightness.",
     "choices": [
        ("Admit she's right about the hiding", "The first honest word is the heaviest.", "s9"),
        ("Deflect with a joke", "Humor is a beautiful place to bury things alive.", "s10"),
     ]},
    {"id": "s8", "title": "Alice's Door Opens", "text": "Alice finally comes out and says the thing: she's furious you got to keep working, keep talking, keep moving, while she had to sit with it. \"You help everyone but me,\" she says, and it lands like a verdict.",
     "choices": [
        ("Apologize without defending yourself", "An apology with a 'but' isn't one.", "s9"),
        ("Explain how grief made you useless at home", "The truth, badly timed, can sound like an excuse.", "s10"),
     ]},
    {"id": "s9", "title": "Wednesday Falls Apart", "text": "The patient you told to quit his job calls back — he also told off his wife, his brother, and his landlord, using your name as permission. Your honesty has become a virus with your fingerprints on it.",
     "choices": [
        ("Take responsibility and help him clean up", "You broke it; you don't get to walk away.", "s11"),
        ("Tell him he made his own choices", "Half true, fully cowardly.", "s12"),
     ]},
    {"id": "s10", "title": "The Joke That Lands Wrong", "text": "At the worst possible moment you crack wise and it doesn't land — it wounds. The person you love most looks at you like you're a stranger doing an impression of their dad. The silence after is a long hallway.",
     "choices": [
        ("Drop the act entirely", "Take off the mask before it grows roots.", "s11"),
        ("Double down because stopping feels like dying", "Sometimes we defend the very thing that's hurting us.", "s12"),
     ]},
    {"id": "s11", "title": "Paul, In the Hospital", "text": "Paul has a fall. In the fluorescent quiet of the ER he holds your wrist and says the unsayable back to you for once: that he's scared, that he's proud of you, that you have to stop running before grief catches you sitting down.",
     "choices": [
        ("Promise him you'll actually grieve", "A promise to a mentor is a rope you tie to yourself.", "s13"),
        ("Tell him to focus on getting better", "Deflection, even now, even here.", "s14"),
     ]},
    {"id": "s12", "title": "The Reckoning", "text": "It all arrives at once — Alice, Sean, Gaby, the patient, Paul — every relationship you've been steering with one hand while not looking. Something has to give, and for once it isn't going to be someone else.",
     "choices": [
        ("Call everyone together and come clean", "Radical honesty, finally aimed at the right target: you.", "s13"),
        ("Disappear for a day to breathe", "Sometimes retreat is the first step of return.", "s14"),
     ]},
    {"id": "s13", "title": "The Thing You Don't Say", "text": "You finally say her name — your wife's — out loud, in the present tense and then the past, and the room you've kept locked for a year cracks open. It is the worst and most necessary sentence of the week.",
     "choices": [
        ("Let yourself fall apart in front of them", "Strength and collapse are the same door.", "s15"),
        ("Hold it together for everyone else", "Old habits guard the gate even now.", "s16"),
     ]},
    {"id": "s14", "title": "The Drive", "text": "You drive nowhere for hours, the way you used to with her. The honesty you've been spraying at everyone turns inward and it's a far harder client to crack. The radio plays her song. You don't change it.",
     "choices": [
        ("Turn the car around and go home", "Home is the one appointment you keep canceling.", "s15"),
        ("Keep driving until you understand something", "Some answers only come at sixty miles an hour.", "s16"),
     ]},
    {"id": "s15", "title": "Friday, With Alice", "text": "Alice finds you at the kitchen table at dawn, both of you wrecked and awake. For the first time you don't try to therapize her. You just say, 'I miss her too, and I'm so sorry I left you alone in it.' She sits down.",
     "choices": [
        ("Grieve with her, no fixing", "Two people in the same wreckage is not nothing.", "s17"),
        ("Make her breakfast and let the food talk", "Care is sometimes a verb that smells like toast.", "s18"),
     ]},
    {"id": "s16", "title": "Sean's Choice", "text": "Sean tells you he's moving out — not in anger, but because he's ready. \"You fixed me by treating me like family,\" he says, \"which is the one thing they tell you not to do.\" He's right, and you'd do it again.",
     "choices": [
        ("Let him go with your blessing", "The work is done when they don't need you.", "s17"),
        ("Ask him to stay one more week", "Love and self-interest can wear the same coat.", "s18"),
     ]},
    {"id": "s17", "title": "The Method, Reconsidered", "text": "You sit with Gaby and Paul and admit the honest-therapy experiment was half breakthrough, half breakdown. \"Maybe,\" Paul says, \"the trick isn't saying everything. It's saying the true thing, kindly, at the right time.\"",
     "choices": [
        ("Adopt Paul's wiser version", "Wisdom is honesty that learned some manners.", "s19"),
        ("Insist you'll find your own way", "Even the student's mistakes are part of the curriculum.", "s20"),
     ]},
    {"id": "s18", "title": "Sunday Light", "text": "The week ends quieter than it started. Nobody's cured — that's not how this works — but the people you love are a little less alone, and so are you. The grief is still there. It just isn't driving anymore.",
     "choices": [
        ("Make peace with being a work in progress", "Healing isn't a finish line; it's a practice.", "s19"),
        ("Plan how to do better Monday", "Hope is the homework you assign yourself.", "s20"),
     ]},
    {"id": "s19", "title": "The Right Thing, Kindly", "text": "Monday returns, as Mondays do. Your first patient sits down and circles the old problem. This time you wait for the right moment and say the true thing gently — and watch it land like medicine instead of a slap.",
     "choices": [
        ("Trust the kinder honesty", "You finally learned the difference.", "end_method"),
        ("Check in with Paul afterward, just because", "Gratitude is a session you give for free.", "end_paul"),
     ]},
    {"id": "s20", "title": "Family, Chosen and Otherwise", "text": "Dinner at your place: Alice, Sean, Gaby, Paul, all the broken beautiful people you accidentally collected. It's loud and imperfect and exactly the kind of mess that means you're alive. Her chair is empty, and that's okay tonight.",
     "choices": [
        ("Raise a glass to the people still here", "Grief and gratitude at the same table.", "end_family"),
        ("Slip away to talk to her, one last time this week", "Some conversations don't need a reply.", "end_grief"),
     ]},
    {"id": "end_method", "title": "Saying the True Thing, Kindly", "text": "You keep the honesty and lose the recklessness, and somehow that's harder and better. Your patients get the truth at a dose they can hold. It isn't a method anymore. It's just you, finally being a good doctor and a worse martyr.",
     "end": "Saying the True Thing, Kindly"},
    {"id": "end_paul", "title": "For Paul", "text": "Paul gets better, then worse, then better again, the way bodies do near the end of long good lives. You spend the time. You say the things. When you finally lose him, you've left nothing unsaid — the only kind of goodbye that doesn't haunt you.",
     "end": "For Paul"},
    {"id": "end_family", "title": "The People Still Here", "text": "The house is full, the wine is cheap, and your daughter is laughing for the first time in months. You built a family out of patients and friends and stubborn love. It's not the family you had. It's the one that saved you.",
     "end": "The People Still Here"},
    {"id": "end_grief", "title": "Present Tense", "text": "You talk to her in the dark like you used to, except now you can say her name without flinching. You're not over it. You're through the worst of it, which is the only honest thing grief ever promises. Tomorrow you go to work and help someone else find the door.",
     "end": "Present Tense"},
])


# ---------------------------------------------------------------------------
# Wuthering Heights — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
WUTHERING = ({
    "id": "wuthering-heights-the-moor",
    "title": "The Moor Between Us",
    "sourceTitle": "Wuthering Heights",
    "kind": "movie",
    "synopsis": "Two souls, one wild stretch of moorland, and a love that refuses to behave. Choose between the heart and the world — and learn that the moor keeps every choice you make on it.",
    "releaseYear": 2026,
    "addedAt": "2026-05-24T00:00:00Z",
    "genre": "Drama",
    "tags": ["gothic", "romance", "revenge"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "The Wind on the Heath", "text": "You and Heathcliff run wild across the moor as children, the wind in your teeth, the world below not yet able to touch you. Up here there are no names, no fathers, no class. Down at the Grange, the lights are coming on.",
     "choices": [
        ("Stay out on the moor till dark", "The wild hours are the only honest ones.", "s2"),
        ("Go down toward the Grange's warm windows", "Comfort has a gravity all its own.", "s3"),
     ]},
    {"id": "s2", "title": "Two Halves", "text": "\"I am Heathcliff,\" you tell yourself, half a prayer. He's not your brother and not your servant and not allowed to be your love, and so of course he is all the air there is. The household already disapproves.",
     "choices": [
        ("Swear nothing will ever part you", "Vows on the moor are heard by the wind alone.", "s4"),
        ("Keep the bond a guarded secret", "What's hidden grows teeth.", "s5"),
     ]},
    {"id": "s3", "title": "The Grange", "text": "The Lintons' house is everything the Heights is not — soft carpets, soft voices, Edgar Linton's soft hopeful eyes on you. A part of you, the part that gets cold and tired, leans toward it.",
     "choices": [
        ("Let Edgar court you", "The warm road is also a road away.", "s5"),
        ("Refuse the Grange and run back uphill", "Some warmth costs more than the cold.", "s4"),
     ]},
    {"id": "s4", "title": "The Master's Cruelty", "text": "After the old master dies, Hindley reigns at the Heights and grinds Heathcliff down to a stable hand, beaten and brilliant and burning. You watch the boy you love turned to a servant before your eyes.",
     "choices": [
        ("Defy Hindley openly for Heathcliff", "Open defiance is brave and brittle.", "s6"),
        ("Protect Heathcliff in secret", "Quiet shields hold longer than loud ones.", "s7"),
     ]},
    {"id": "s5", "title": "The Proposal", "text": "Edgar Linton asks for your hand and a future of ease and respectability. You confess to the housekeeper that you love Heathcliff to your bones — but that marrying him now would 'degrade you.' Heathcliff hears only the first half before he flees into the storm.",
     "choices": [
        ("Run after him into the storm", "Chase the truth before pride buries it.", "s6"),
        ("Let him go and accept Edgar", "The world is heavy and you are tired of fighting it.", "s8"),
     ]},
    {"id": "s6", "title": "The Storm", "text": "The moor in a storm is a living thing, and you cannot find him in it. By dawn Heathcliff is gone — vanished entirely, swallowed by the rain and his own wounded pride. The silence he leaves is louder than any wind.",
     "choices": [
        ("Wait years for his return", "Hope is a long and ruinous tenant.", "s7"),
        ("Marry Edgar to forget the ache", "Forgetting is a house you can never quite furnish.", "s8"),
     ]},
    {"id": "s7", "title": "The Years Between", "text": "Time passes thin and grey. You become someone's wife or someone's ghost, you're no longer sure which. Then a stranger arrives at the gate — gentlemanly, wealthy, and unmistakably him. Heathcliff has come back rich, and changed.",
     "choices": [
        ("Greet him with open joy", "Joy is honest and dangerous.", "s9"),
        ("Greet him with careful distance", "Caution comes too late to save you.", "s10"),
     ]},
    {"id": "s8", "title": "Lady of the Grange", "text": "You are mistress of Thrushcross Grange now, fine and admired and slowly starving in a way no meal can fix. Edgar is gentle and good and not enough, and you've begun to fade like a flower kept indoors.",
     "choices": [
        ("Confess your unhappiness to Edgar", "Honesty is a knife you turn on yourself.", "s9"),
        ("Hide the sickness of your heart", "What you swallow does not digest.", "s10"),
     ]},
    {"id": "s9", "title": "He Returns", "text": "Heathcliff is back and he has not forgiven — not you, not Hindley, not the world that ranked him below it. He looks at you with love and ruin in the same glance, and you understand he intends to collect on every old debt.",
     "choices": [
        ("Beg him to choose love over revenge", "Plead with a storm and see what it answers.", "s11"),
        ("Match his cold and play the game", "Two proud people make a long winter.", "s12"),
     ]},
    {"id": "s10", "title": "The Revenge Begins", "text": "He marries Edgar's sister Isabella purely to wound — courting her cruelty by cruelty, ruining a girl who never harmed him, all to put a blade in your peace. The moor watches and keeps its counsel.",
     "choices": [
        ("Try to save Isabella from him", "Mercy aimed at the innocent is never wasted.", "s11"),
        ("Let him have his terrible victory", "Looking away is its own kind of cruelty.", "s12"),
     ]},
    {"id": "s11", "title": "The Last Meeting", "text": "You meet once more, in a room that feels like the edge of a cliff. He holds you and rages at you in the same breath: 'Why did you betray your own heart?' There's no answer that doesn't break something.",
     "choices": [
        ("Tell him the whole, ruinous truth", "Truth, this late, is a wound and a gift.", "s13"),
        ("Tell him to live, even without you", "Releasing him is the cruelest love.", "s14"),
     ]},
    {"id": "s12", "title": "The Fever", "text": "Grief makes you ill — a fever of the body that is really a fever of the soul, refusing to choose between two impossible lives. You stand at the window calling for the moor, for the wind, for the wild girl you used to be.",
     "choices": [
        ("Reach for the window and the moor", "The heath calls its own home.", "s13"),
        ("Sink back and let the warm room win", "Sometimes the body decides for you.", "s14"),
     ]},
    {"id": "s13", "title": "Haunting", "text": "Whatever passes between you, it does not end at death — it cannot. You become a presence on the moor, a knock at a window, a name the wind keeps saying. Heathcliff, alive, becomes the truly haunted one.",
     "choices": [
        ("Haunt him until he follows you", "Love that won't die becomes a summons.", "s15"),
        ("Watch over the next generation instead", "Even ghosts can choose tenderness.", "s16"),
     ]},
    {"id": "s14", "title": "The Long Revenge", "text": "Years roll on and Heathcliff, joyless and rich, ruins everyone you both once knew — Hindley's son, Edgar's daughter, his own boy. Revenge has eaten everything, including the parts of him you loved. He is master of two houses and prisoner of one grave.",
     "choices": [
        ("Let the next generation break the curse", "The young are the only escape from the old.", "s16"),
        ("Let the cruelty run to its bitter end", "Some fires must burn down to the stone.", "s15"),
     ]},
    {"id": "s15", "title": "He Stops Eating", "text": "Near the end, Heathcliff sees you everywhere — in doorways, on the heath, at the foot of his bed. He stops eating, stops sleeping, walks the moor at night calling a name. He is not afraid of his ghost. He is running toward it.",
     "choices": [
        ("Lead him gently to the moor at last", "Death, for some, is the only reunion left.", "s17"),
        ("Make him pay for every cruelty first", "Even love can curdle into justice.", "s18"),
     ]},
    {"id": "s16", "title": "The Young Ones", "text": "Cathy's daughter and Hindley's son — raised in the wreckage you and Heathcliff left behind — begin, impossibly, to teach each other to read, to be gentle, to love without ruin. The moor, for once, is kind.",
     "choices": [
        ("Bless the young lovers from the wind", "The best revenge on the past is a better future.", "s19"),
        ("Watch over the heath itself, eternal", "Some loves become the land itself.", "s20"),
     ]},
    {"id": "s17", "title": "The Last Walk", "text": "You guide him out one final dawn, across the heather you ran on as children. The path narrows. He stops calling your name aloud because he no longer has to — you are walking beside him at last.",
     "choices": [
        ("Take his hand as the light comes up", "After a lifetime apart, the simplest gesture.", "end_together"),
        ("Step ahead and let him follow at his own pace", "Even reunion can be a thing you walk gently into.", "end_together"),
     ]},
    {"id": "s18", "title": "A Cruel Calm", "text": "You refuse him. The window stays shut. He paces the moor for nights and finds no door home, no rest, no you. Justice and love look the same from a distance, and yours is being measured from a distance now.",
     "choices": [
        ("Hold the cold a little longer", "Hardness can be its own grief.", "end_curse"),
        ("Soften at the very last moment", "A cracked door is still mercy.", "end_together"),
     ]},
    {"id": "s19", "title": "Letters Across the Moor", "text": "The young lovers leave small offerings on the heath without quite knowing why — a ribbon, a stone, a sprig of heather. You feel each one. The wind, gentler now, carries your approval back in directions only the bees take seriously.",
     "choices": [
        ("Let them feel watched over, kindly", "Some hauntings are blessings in disguise.", "end_renewal"),
        ("Step back so they can write their own story", "The greatest love is the one that gets out of the way.", "end_renewal"),
     ]},
    {"id": "s20", "title": "The Wind Speaks", "text": "Time wears down the houses, the wrongs, the names. What remains is wind, water, heather, and the long memory of a girl and a boy who ran wild here. Travelers say they can hear you laughing on storm-nights. They are right.",
     "choices": [
        ("Settle fully into the moor", "Some homes choose to keep you.", "end_moor"),
        ("Move on at last, satisfied", "Even ghosts can finish their story.", "end_renewal"),
     ]},
    {"id": "end_together", "title": "Two Graves, One Heath", "text": "They bury him beside you, and the villagers swear that on wild nights two figures walk the moor, finally at peace because they are finally past the world that kept them apart. You are not in heaven or hell. You are home, in the wind, together.",
     "end": "Two Graves, One Heath"},
    {"id": "end_curse", "title": "The Unquiet", "text": "He dies reaching for a window you will not open, and even death grants him no rest. The two of you haunt the heath separately, two storms that can never quite touch. It is the love you chose and the punishment you earned, indistinguishable at last.",
     "end": "The Unquiet"},
    {"id": "end_renewal", "title": "A Gentler Heath", "text": "The young lovers marry and quiet the old houses with ordinary happiness — the very thing you and Heathcliff could never manage. You let the moor have your story and the children have their peace. The wind, for once, just blows.",
     "end": "A Gentler Heath"},
    {"id": "end_moor", "title": "I Am the Moor", "text": "You never quite leave. You become the heath itself — the wind, the heather, the line where the storm meets the hill. People who walk there feel watched and loved and a little afraid, and they are right on all three counts.",
     "end": "I Am the Moor"},
])


# ---------------------------------------------------------------------------
# Black Swan — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
BLACK_SWAN = ({
    "id": "black-swan-the-role",
    "title": "Perfect",
    "sourceTitle": "Black Swan",
    "kind": "movie",
    "synopsis": "You've earned the lead in Swan Lake — the pure White Swan you were born to dance, and the dark Black Swan you'll have to become. The mirror is starting to disagree with you. How far will you go to be perfect?",
    "releaseYear": 2010,
    "addedAt": "2026-05-23T00:00:00Z",
    "genre": "Thriller",
    "tags": ["psychological", "ballet", "transformation"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "The Casting", "text": "The director, Thomas, paces the studio. 'I need a Swan Queen who can be both — innocence and seduction, light and dark.' The other dancers watch you like wolves in legwarmers. The part should be yours. It almost is.",
     "choices": [
        ("Dance only the pure, perfect White Swan", "Control is your gift and your prison.", "s2"),
        ("Try to find the wild Black Swan in yourself", "You can't fake what you've never let yourself feel.", "s3"),
     ]},
    {"id": "s2", "title": "The Mother", "text": "At home your mother has already laid out your dinner, your nightgown, your future. 'My sweet girl,' she says, smoothing your hair, locking the door behind her smile. The room is pink and small and yours and not yours.",
     "choices": [
        ("Thank her and stay the good daughter", "Obedience is a soft cage with a key you can't find.", "s4"),
        ("Push back, just a little", "The first crack lets in light and rot both.", "s5"),
     ]},
    {"id": "s3", "title": "Thomas's Test", "text": "Thomas corners you after rehearsal. 'Perfection is not just control,' he murmurs, too close. 'It's also letting go.' His method blurs the line between teaching and trespass, and he knows exactly how off-balance he's put you.",
     "choices": [
        ("Let him provoke the dark in you", "The role demands a door you're afraid to open.", "s4"),
        ("Hold your boundary and your control", "Saying no costs you the part — maybe.", "s5"),
     ]},
    {"id": "s4", "title": "Lily", "text": "A new dancer, Lily, moves like she was born without fear — sloppy, alive, magnetic. She could be your friend. She could be your understudy. She could be after your role. With her, you can never quite tell.",
     "choices": [
        ("Befriend Lily and learn her looseness", "Open your guard and see what walks in.", "s6"),
        ("Watch Lily as a rival to be beaten", "Suspicion sharpens you and isolates you.", "s7"),
     ]},
    {"id": "s5", "title": "The First Scratch", "text": "You find marks on your shoulder you don't remember making. A rash, your mother says. A sign, the mirror seems to whisper. You begin checking your reflection for a face that isn't quite doing what you're doing.",
     "choices": [
        ("Tell yourself it's just exhaustion", "Denial is a stage you can dance on for a while.", "s6"),
        ("Start watching the mirror back", "What you look for, you find.", "s7"),
     ]},
    {"id": "s6", "title": "The Night Out", "text": "Lily drags you out — drinks, music, a pill she promises will 'help you let go.' For one night you are loose and laughing and free, dancing in a dark club instead of a bright studio. You wake unsure what was real.",
     "choices": [
        ("Embrace the wildness it unlocked", "The Black Swan stirs and stretches her wings.", "s8"),
        ("Recoil in shame the next morning", "The good girl claws her way back to the surface.", "s9"),
     ]},
    {"id": "s7", "title": "The Reflection Lies", "text": "In the long studio mirrors your reflection turns its head a half-beat late. It smiles when you don't. Once, you'd swear it kept dancing after you stopped. You tell no one. Telling someone would make it true.",
     "choices": [
        ("Confront the mirror directly", "Stare into it and it stares back, smiling.", "s8"),
        ("Avoid mirrors and push through", "You can't dance ballet without mirrors. You'll learn that.", "s9"),
     ]},
    {"id": "s8", "title": "Becoming the Black Swan", "text": "In rehearsal, finally, it happens — you stop counting, stop controlling, and let something hungry take the floor. Thomas weeps. The company stares. You have never felt so powerful or so unlike yourself.",
     "choices": [
        ("Chase that feeling no matter the cost", "Power like this is a debt you'll be billed for.", "s10"),
        ("Be frightened by what came out of you", "Fear is the last sane voice in the room.", "s11"),
     ]},
    {"id": "s9", "title": "Cracking", "text": "Your toenails, your skin, your sleep — your body is keeping a tally your mind won't. You hide the worst of it under makeup and tights. Your mother hovers; Thomas pushes; the mirror waits. Something has to give, and it's you.",
     "choices": [
        ("Hide it all and dance anyway", "The show is a god that eats its dancers.", "s10"),
        ("Reach out for help, once", "A hand extended, even shaking, is still a hand.", "s11"),
     ]},
    {"id": "s10", "title": "The Rival, Closer", "text": "Lily is made your alternate — your safety net, or your replacement, depending on how you look at her. You find her in your dressing room, or you imagine you do. You can no longer tell the difference, and it's starting to feel like a knife.",
     "choices": [
        ("Accuse Lily of trying to steal the role", "Paranoia and truth have begun to share a face.", "s12"),
        ("Decide you must simply be better than her", "Turn the fear into fuel and burn yourself for warmth.", "s13"),
     ]},
    {"id": "s11", "title": "The Help You Reach For", "text": "Maybe a doctor, maybe a friend, maybe just one honest sentence to your mother. The help is real and the relief is real — but opening night is in three days, and the part is your whole identity. Can you be saved and still be the Swan Queen?",
     "choices": [
        ("Take the help and risk losing the role", "Your life is worth more than a curtain call. Probably.", "s14"),
        ("Refuse the lifeline to protect the part", "The role has its hooks in deep now.", "s13"),
     ]},
    {"id": "s12", "title": "Opening Night Approaches", "text": "The hallucinations sharpen — feathers under your skin, your legs bending the wrong way, your reflection living its own life. You are dancing better than ever and unraveling faster than ever, on the exact same thread.",
     "choices": [
        ("Lean fully into the transformation", "Maybe madness and perfection are the same place.", "s15"),
        ("Fight to hold onto yourself", "There may still be a 'you' left to save.", "s16"),
     ]},
    {"id": "s13", "title": "The Mirror Shatters", "text": "Backstage on opening night, the confrontation comes — with Lily, with your reflection, with the dark thing wearing your face. Glass breaks. You feel a sharp, terrible relief, and a spreading warmth you don't look at.",
     "choices": [
        ("Believe you've defeated your rival", "The mind protects itself with terrible stories.", "s15"),
        ("Begin to suspect there was no rival at all", "The most dangerous person in the room was always the one in the mirror.", "s16"),
     ]},
    {"id": "s14", "title": "Stepping Back", "text": "You walk out of the theater the night before the premiere. It feels like dying and like being born. Your understudy goes on; the reviews are fine; the world does not end. You are not the Swan Queen. You are, perhaps, alive.",
     "choices": [
        ("Grieve the role but keep your life", "Some losses are the shape of survival.", "end_alive"),
        ("Wonder forever if you could have been perfect", "The road not danced haunts the longest.", "end_whatif"),
     ]},
    {"id": "s15", "title": "The Black Swan's Dance", "text": "You take the stage and you are no longer dancing the Black Swan — you are her. The audience disappears. You spin and spin and feel wings, real wings, and the most exquisite freedom of your life. Nothing has ever been this perfect.",
     "choices": [
        ("Finish the dance no matter what", "Perfection has a price and you've already paid it.", "s17"),
        ("Come back to yourself before the final act", "The fall toward earth is the most human thing.", "s16"),
     ]},
    {"id": "s16", "title": "The White Swan's Truth", "text": "In the wings, between acts, the fog clears for one terrible lucid moment. You understand what you've done to your body, your mind, your reflection. The wound is yours. The rival was yours. The choice, now, is also yours.",
     "choices": [
        ("Go back out and dance the ending anyway", "Finish beautifully and let go of everything.", "s18"),
        ("Call for help and step out of the story", "Choosing to live is the bravest exit there is.", "s19"),
     ]},
    {"id": "s17", "title": "Curtain Call", "text": "The bows. The roses. Thomas climbing onto the stage to kiss the back of your hand. You smile through everything because smiling is the next step, and the next step is the only step that matters. Something warm is spreading at your side and you do not look down.",
     "choices": [
        ("Let the applause carry you", "Joy and dying can rhyme, briefly.", "end_perfect"),
        ("Finally, finally, look down", "Reality is the last person to arrive at the party.", "s20"),
     ]},
    {"id": "s18", "title": "Between the Acts", "text": "You go back out and finish — and somewhere in the second-to-last lift you feel your body decide it is done bargaining with you. The audience does not know. They will not, for one more aria.",
     "choices": [
        ("Dance the last act with everything left", "Some final notes are the best ones.", "end_perfect"),
        ("Drop the role mid-leap and walk off", "Refusing the script is its own kind of grace.", "s19"),
     ]},
    {"id": "s19", "title": "The Quiet Wings", "text": "Backstage is suddenly louder than the stage — Thomas raging, Lily wide-eyed, your mother crying without sound. You make the smallest, hardest gesture of your career: you sit down and ask for an ambulance.",
     "choices": [
        ("Tell them the whole truth about everything", "Honesty in the wings is the harder choreography.", "end_survive"),
        ("Just hold your knees and breathe", "Sometimes survival is wordless.", "end_alive"),
     ]},
    {"id": "s20", "title": "Looking Down", "text": "Red on white. Of course. You laugh, almost — at yourself, at the cost of perfection, at how obvious it was. There is one more breath in which you can decide what this night meant.",
     "choices": [
        ("Decide it meant perfection", "Some stories end on a high note, on purpose.", "end_perfect"),
        ("Decide it meant a warning, in time", "Even at the curtain you can rewrite an ending.", "end_survive"),
     ]},
    {"id": "end_perfect", "title": "Perfect", "text": "The final note. The white feathers. The leap. The audience erupts and Thomas calls your name and you smile, because you felt it — you were, for one impossible night, perfect. The warmth at your side spreads. 'I was perfect,' you whisper, and mean it, as the lights go soft.",
     "end": "Perfect"},
    {"id": "end_survive", "title": "Imperfect, Alive", "text": "You stop the show. There are gasps and then ambulances and then, weeks later, a quiet room and a real recovery. You will dance again or you won't, but you will be there to choose. Perfection nearly killed you. Imperfection, it turns out, is where you get to live.",
     "end": "Imperfect, Alive"},
    {"id": "end_alive", "title": "The Dancer Who Walked Away", "text": "You left ballet, or ballet left you, and for a long time it felt like amputation. Then one ordinary morning you dance in your kitchen for no audience at all and feel, faintly, joy — the kind that doesn't bleed. You are nobody's Swan Queen. You are nobody's victim either.",
     "end": "The Dancer Who Walked Away"},
    {"id": "end_whatif", "title": "The Understudy's Triumph", "text": "Lily dances the Swan Queen and the reviews call her a revelation. You watch from the back of the house, healthy and hollow, applauding a perfection that might have been yours. You'll never know. That not-knowing is the role you dance for the rest of your life.",
     "end": "The Understudy's Triumph"},
])


# ---------------------------------------------------------------------------
# Hoppers — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
HOPPERS = ({
    "id": "hoppers-into-the-wild",
    "title": "Into the Wild",
    "sourceTitle": "Hoppers",
    "kind": "movie",
    "synopsis": "A new gadget lets you beam your mind into a lifelike robot animal and join the creatures of the marsh. You wanted to save the wetland. You didn't expect the animals to have a vote — or to change yours.",
    "releaseYear": 2026,
    "addedAt": "2026-05-22T00:00:00Z",
    "genre": "Fantasy",
    "tags": ["animals", "nature", "adventure"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "The Hopper", "text": "The lab's prototype hums: beam your consciousness into a robotic beaver and walk among real animals undetected. The wetland behind your town is about to be paved for a mall. You think the animals deserve a warning. You volunteer to go first.",
     "choices": [
        ("Jump in immediately", "Some leaps you take before you can think better of them.", "s2"),
        ("Run one more safety check", "Caution is a kindness you do your future self.", "s3"),
     ]},
    {"id": "s2", "title": "Four Paws", "text": "The world rushes up close and enormous. You're a beaver now — whiskers, flat tail, teeth like chisels. Sound and smell flood in. A real beaver eyes your robot body, unconvinced.",
     "choices": [
        ("Greet the real beaver as a friend", "First contact, paw to paw.", "s4"),
        ("Observe quietly and learn the rules", "Watch before you wade in.", "s5"),
     ]},
    {"id": "s3", "title": "The Glitch", "text": "The safety check finds a flaw: if your robot body is destroyed while you're inside, the jolt back could hurt — or strand you. The clock to the bulldozers is ticking. You decide the risk is worth the wetland.",
     "choices": [
        ("Go anyway, carefully", "Brave and reckless are cousins, not twins.", "s4"),
        ("Bring a remote escape switch", "Always know where the door is.", "s5"),
     ]},
    {"id": "s4", "title": "King George", "text": "The marsh has a leader — a grumpy old beaver the others call King George, who built the great dam and trusts no two-legger, robot or otherwise. To save the wetland you'll need him, and he'd happily gnaw you in half.",
     "choices": [
        ("Try to win his trust honestly", "Respect is a current you swim with, not against.", "s6"),
        ("Try to impress him with human cleverness", "Cleverness without humility just makes noise.", "s7"),
     ]},
    {"id": "s5", "title": "The Council of Critters", "text": "You discover the marsh has a whole society — herons with opinions, otters with grudges, a wise old turtle who remembers the last time humans came with machines. They've survived people before. Barely.",
     "choices": [
        ("Listen to the turtle's history first", "The old remember what the young must learn.", "s6"),
        ("Rally the young animals to act now", "Urgency is honest but it can be clumsy.", "s7"),
     ]},
    {"id": "s6", "title": "Speaking Their Language", "text": "Bit by bit you learn it — not words, but warnings, rhythms, the tail-slap that means danger and the splash that means come. For the first time the marsh stops treating you as a stranger and starts treating you as a neighbor.",
     "choices": [
        ("Tell them the truth about the mall", "Hard news given with respect is still a gift.", "s8"),
        ("Soften the news so they don't panic", "A protective lie is still a lie.", "s9"),
     ]},
    {"id": "s7", "title": "Out of Your Depth", "text": "You try to lead and it goes sideways — a clever plan that ignores how the marsh actually works, a dam nearly broken, a duckling nearly lost. The animals pull you out of trouble you made. Humbling doesn't cover it.",
     "choices": [
        ("Apologize and ask to learn their way", "The bravest word is sometimes 'sorry.'", "s8"),
        ("Insist your way will still work", "Pride is heavy to swim with.", "s9"),
     ]},
    {"id": "s8", "title": "The Warning", "text": "You gather the marsh and tell them everything: the surveyors, the machines, the date. King George's old eyes go hard. 'We have run before,' he says. 'There is nowhere left to run to.' The choice of what to do next is suddenly very real.",
     "choices": [
        ("Plan to fight the development", "Some homes are worth standing in front of.", "s10"),
        ("Plan to help them relocate safely", "Survival sometimes wears the face of retreat.", "s11"),
     ]},
    {"id": "s9", "title": "The Surveyors Arrive", "text": "Before any plan is ready, the trucks come early — orange vests, spray paint, a clipboard deciding the fate of a thousand lives that don't fit in its columns. The marsh erupts in panic. You have minutes, not days.",
     "choices": [
        ("Lead an emergency evacuation", "Save who you can, right now.", "s11"),
        ("Try to stall the humans yourself", "One small beaver against a clipboard. Why not.", "s10"),
     ]},
    {"id": "s10", "title": "The Stand", "text": "You and the animals do the impossible — chewed-down survey stakes, a beaver-built flood overnight, a colony of creatures that simply, gloriously, will not move. The footage of it (somehow) ends up online. The town starts to pay attention.",
     "choices": [
        ("Reveal yourself and tell the human story", "Sometimes the bridge has to walk on two legs.", "s12"),
        ("Stay hidden and let the marsh speak", "Let the wild make its own case.", "s13"),
     ]},
    {"id": "s11", "title": "The Long Walk", "text": "You guide the marsh's families across roads and culverts toward a wilder, safer water upstream — a heron flying scout, otters herding stragglers, you and King George at the front. Not everyone is sure they should follow a robot. They follow anyway.",
     "choices": [
        ("Get them all there, no one left behind", "A leader counts heads at the back of the line.", "s12"),
        ("Go back for the ones who refused to leave", "Home is the hardest thing to ask anyone to abandon.", "s13"),
     ]},
    {"id": "s12", "title": "Back in Your Body", "text": "You pull yourself out of the hopper, gasping, human again — and you're different. You've felt the marsh from the inside now. You take what you saw to the town council, to the news, to anyone who'll listen, and you do not let them look away.",
     "choices": [
        ("Make the town fall in love with the marsh", "People protect what they've learned to love.", "s14"),
        ("Take the developers to court with the evidence", "Sometimes you fight paper with paper.", "s15"),
     ]},
    {"id": "s13", "title": "The Danger", "text": "Your robot body is caught in the machinery's path, and the glitch you were warned about flares — if you don't jump out now, you could be stranded as a beaver forever. But leaving now means abandoning the marsh at the worst moment.",
     "choices": [
        ("Stay in to finish saving them", "Some causes are worth the risk of yourself.", "s16"),
        ("Jump out before it's too late", "You can do more good with a body to come back to.", "s14"),
     ]},
    {"id": "s14", "title": "Hearts and Minds", "text": "You bring the town to the water — kids, grandparents, the mayor in unwise shoes. They see the otters play, the herons fish, King George patrol his dam. You watch a developer's daughter laugh at a duckling, and you know you've won something.",
     "choices": [
        ("Push for the wetland to become a sanctuary", "Aim past survival, toward flourishing.", "s17"),
        ("Settle for a compromise that saves the core", "Half a marsh saved is a thousand lives saved.", "s18"),
     ]},
    {"id": "s15", "title": "The Hearing", "text": "In a beige room with bad coffee, the future of the marsh comes down to permits and clauses and the footage of a beaver society refusing to die quietly. You speak. The animals can't be in the room, but somehow the whole marsh is.",
     "choices": [
        ("Win the case outright", "Justice, slow and beige, occasionally arrives.", "s17"),
        ("Lose the case but spark a movement", "Some defeats plant longer victories.", "s18"),
     ]},
    {"id": "s16", "title": "One With the Marsh", "text": "You stay in, and you save them — you break the machine's path, you hold the line, you get every last family to safe water. The cost is real: the hopper fails, and for a long, frightening while, you are only a beaver, fully, in the wild you fought for.",
     "choices": [
        ("Find a way back to your human life", "Two worlds, and a bridge you have to rebuild.", "s17"),
        ("Choose to stay wild a while longer", "Some homes choose you back.", "end_wild"),
     ]},
    {"id": "s17", "title": "The Sanctuary", "text": "The wetland is saved — not as a leftover scrap, but as a protected wild heart with the town wrapped proudly around it. King George, ancient and unimpressed, slaps his tail once in what is almost, almost approval.",
     "choices": [
        ("Dedicate your life to the wild", "Some callings arrive with whiskers.", "s19"),
        ("Share the hopper so others can understand animals too", "Empathy is the only technology that scales.", "s20"),
     ]},
    {"id": "s18", "title": "The Compromise", "text": "It isn't everything. The mall shrinks, the marsh keeps its core, and a fragile peace is drawn in spray paint and signatures. It's imperfect, like all real victories. The animals, who never expected to win at all, are cautiously, splashily delighted.",
     "choices": [
        ("Vow to keep fighting for the rest", "A line held is a line you can advance from.", "s19"),
        ("Celebrate what you saved with the whole marsh", "Joy is allowed, even in an unfinished win.", "s20"),
     ]},
    {"id": "s19", "title": "The Ranger's Path", "text": "You spend the next summer in muck boots and a clipboard, learning every inch of the marsh that the marsh hasn't already taught you in fur. The town hires you full-time. King George tolerates your presence with what is, for him, real affection.",
     "choices": [
        ("Commit to the marsh for the long haul", "Some jobs are vocations in waders.", "end_ranger"),
        ("Branch out to protect other wild places too", "Lessons from one marsh fit many.", "end_bridge"),
     ]},
    {"id": "s20", "title": "Opening the Hoppers", "text": "You teach the next group of kids to use the device — gentle rules, short visits, and a vow to leave the marsh better than you found it. Watching a ten-year-old return from being a heron and announce, tearfully, 'I get it now,' is the best paycheck you'll ever earn.",
     "choices": [
        ("Build a whole program around it", "Scale the empathy, save the wild.", "end_bridge"),
        ("Keep it small and sacred, on purpose", "Some magic only works at human scale.", "end_ranger"),
     ]},
    {"id": "end_wild", "title": "Home in the Water", "text": "For one whole season you live as a beaver, and it is the truest you've ever felt — cold mornings, warm lodges, a family of creatures who don't care that you started as a girl. When you finally go home, you bring the marsh's heartbeat back with you, and you never lose it.",
     "end": "Home in the Water"},
    {"id": "end_ranger", "title": "Keeper of the Marsh", "text": "You grow up and become the marsh's fiercest human friend — ranger, scientist, troublemaker, voice for the voiceless. Every fight you pick, you pick for the small wet kingdom that once let a robot beaver join its council. King George would approve. He'd never admit it.",
     "end": "Keeper of the Marsh"},
    {"id": "end_bridge", "title": "A Bridge Between Worlds", "text": "You open the hopper to everyone — kids spend afternoons as herons and otters and turtles, and a generation grows up unable to imagine paving a place they've lived inside. The wild stops being 'out there.' It becomes us. That, it turns out, is how you really save a marsh.",
     "end": "A Bridge Between Worlds"},
])


# ---------------------------------------------------------------------------
# Game of Thrones — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
GOT = ({
    "id": "got-the-small-lord",
    "title": "The Small Lord",
    "sourceTitle": "Game of Thrones",
    "kind": "show",
    "synopsis": "You inherit a castle the size of a wart, on a road every army wants. Two queens want your sword, three gods want your soul, and your maester is out of wine. Welcome to the game.",
    "releaseYear": 2019,
    "addedAt": "2026-05-21T00:00:00Z",
    "genre": "Fantasy",
    "tags": ["intrigue", "war", "houses"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "Two Ravens", "text": "Two ravens arrive within an hour of each other — one with a Stark direwolf seal, one with a Lannister lion. Both ask the same thing: bend the knee, or burn. Your maester pours the last of the wine and waits.",
     "choices": [
        ("Open the Stark raven first", "The North remembers — and so do its enemies.", "s2"),
        ("Open the Lannister raven first", "Gold has a longer reach than honor.", "s3"),
     ]},
    {"id": "s2", "title": "The Direwolf's Words", "text": "The Stark letter is short and proud — sworn swords, no gold, a place at a council table when the wars are done. Honor like a cold draft through a great hall.",
     "choices": [
        ("Trust the cold honor of the North", "Hard ground holds up the longest.", "s4"),
        ("Find it pretty and impractical", "Banners don't feed a garrison.", "s5"),
     ]},
    {"id": "s3", "title": "The Lion's Coin", "text": "The Lannister letter rings — a chest of dragons in advance, more after the war, a marriage with a third cousin nobody will miss. Gold has good manners.",
     "choices": [
        ("Take the coin and the comfortable side", "Survival is also a virtue, however cynical.", "s5"),
        ("Distrust gold that arrives so cheaply", "A purse this open hides a knife.", "s4"),
     ]},
    {"id": "s4", "title": "The Maester's Counsel", "text": "Old Maester Edryn has served three lords and outlived two. 'There is no right answer,' he says. 'Only the answer you can live with after.' He coughs. He has, perhaps, a year.",
     "choices": [
        ("Ask him what he would do", "The wise are best asked, not obeyed.", "s6"),
        ("Decide alone — the choice is yours", "A lord who borrows backbone has none.", "s7"),
     ]},
    {"id": "s5", "title": "Your Wife's Strategy", "text": "Lady Maren — sharper than your sword and twice as costly — lays out a map at the hearth. 'Hold the river crossing,' she says, 'and both of them will need us.' She does not smile often. She smiles now.",
     "choices": [
        ("Follow her plan to play both sides", "A bridge is the most expensive thing you own.", "s7"),
        ("Refuse — call it dishonorable", "Honor is a kind of luxury too.", "s6"),
     ]},
    {"id": "s6", "title": "The Bannermen", "text": "Your seven small lords gather in the hall. Three are for the Starks, two for the Lannisters, one for declaring himself king of a barn, and one is asleep. Loyalty here is a candle in a draft.",
     "choices": [
        ("Take a vote and abide by it", "Democracy in Westeros is a curiosity.", "s8"),
        ("Speak first and tell them where you stand", "Lords lead. Bannermen follow or leave.", "s9"),
     ]},
    {"id": "s7", "title": "Dragon Rumors", "text": "A merchant claims he saw a shadow with wings the size of a longship pass over the Narrow Sea. A child claims the same. The maester scoffs and does not sleep that night.",
     "choices": [
        ("Send a man east to confirm", "Knowledge is the only armor that fits everyone.", "s8"),
        ("Dismiss it as a rumor and a child", "Dragons are stories. Until they aren't.", "s9"),
     ]},
    {"id": "s8", "title": "First Skirmish", "text": "A column of mercenaries crosses your river in the night. By dawn there are dead men in the reeds — three of theirs, one of yours, a boy of fifteen who liked the cook's daughter. The war has arrived without asking.",
     "choices": [
        ("Hang the prisoners as a warning", "Cruelty travels fast and ugly.", "s10"),
        ("Send them home with bread and a message", "Mercy can be a kind of edge.", "s11"),
     ]},
    {"id": "s9", "title": "Wildlings at the Walls", "text": "A line of strangers from the North — gaunt, frostbitten, refugees from things worse than men — wait at your gates. The septon calls them savages. The cook offers them broth.",
     "choices": [
        ("Take them in and use their strong backs", "Allies arrive in odd skins.", "s10"),
        ("Turn them away to spare your stores", "A castle that feeds everyone feeds no one.", "s11"),
     ]},
    {"id": "s10", "title": "Trial of a Traitor", "text": "Your steward is caught passing word to the Lannisters. He has six children. The law is clear; the law is also a heavy weight to carry. Maren wants him beheaded by sundown.",
     "choices": [
        ("Execute him publicly to keep order", "Iron speaks plainly.", "s12"),
        ("Spare him and use him as a false-message conduit", "A turned spy is sharper than any blade.", "s13"),
     ]},
    {"id": "s11", "title": "The Spy in the Kitchen", "text": "Maren discovers a Lannister man in the scullery — leaving for two months, learning the tunnels. He kneels and begs and his accent is from a village two valleys over.",
     "choices": [
        ("Quietly disappear the spy", "Some problems vanish best at night.", "s12"),
        ("Feed him a beautiful lie and let him 'escape'", "Information aimed back is the cheapest weapon.", "s13"),
     ]},
    {"id": "s12", "title": "The Red Feast Invitation", "text": "An invitation arrives, stamped with the Frey star and weighted with too much ceremony. A wedding. Both sides will be there. Maester Edryn has gone very still.",
     "choices": [
        ("Attend — refusal is its own statement", "The most dangerous rooms are the most necessary.", "s14"),
        ("Send your regrets and an honest gift", "Some doors are closed for the body and opened for the soul.", "s15"),
     ]},
    {"id": "s13", "title": "Sermon by the River", "text": "The septon preaches that war is a punishment from the Seven for lords forgetting the small folk. Your peasants nod. So do, awkwardly, two of your bannermen. A sermon is sometimes the start of a politics.",
     "choices": [
        ("Embrace him publicly to win the smallfolk", "A god on your side travels free.", "s14"),
        ("Quietly muzzle him before he becomes a movement", "Sermons can outrun swords.", "s15"),
     ]},
    {"id": "s14", "title": "The Wedding Hall", "text": "You ride in under your banner with a small honor guard. The hall is too full, the music is too loud, and the wine is too generous. You see Maren count exits three times.",
     "choices": [
        ("Leave before the toast", "Trust her counting.", "s16"),
        ("Stay and hold your position", "A lord who flees a wedding becomes a story.", "s17"),
     ]},
    {"id": "s15", "title": "The Marriage Pact", "text": "Instead you broker a marriage of your own — your eldest to a neutral house with a tower of grain and no taste for war. Maren writes the contract; the maester signs as witness; nobody is in love. It is, by Westerosi standards, a love story.",
     "choices": [
        ("Make the pact public and binding", "Allies welded in candle-wax.", "s16"),
        ("Keep it secret until the war declares a winner", "A card is sharpest when it is still face-down.", "s17"),
     ]},
    {"id": "s16", "title": "The Siege", "text": "An army arrives — whichever army you betrayed, or didn't — and rings your walls. Inside there is food for forty days, a maester with a fever, and Maren saying, far too calmly, that she's been preparing for this her whole life.",
     "choices": [
        ("Hold the siege to the last grain", "Walls win wars patient men forget.", "s18"),
        ("Negotiate from strength while you still can", "Speak first, before hunger does.", "s19"),
     ]},
    {"id": "s17", "title": "Treaty Under Stars", "text": "On a hill between camps you meet a rival lord and a flagon of wine and a sky full of indifferent stars. Treaties under stars never quite hold to morning, but they are, sometimes, where wars actually end.",
     "choices": [
        ("Swear the treaty and mean it", "Honor offered first is harder to refuse.", "s18"),
        ("Swear it and plan to break it cleverly", "Cleverness comes due, eventually.", "s19"),
     ]},
    {"id": "s18", "title": "Dragon Shadow", "text": "A shape passes over your towers, and the temperature drops, and your archers forget what their bows are for. The dragon is real. The dragon has noticed you. The world tilts.",
     "choices": [
        ("Kneel to whoever rides the dragon", "Some powers you bow to without shame.", "s20"),
        ("Hide your house from the dragon's gaze", "Be small enough to escape notice.", "s21"),
     ]},
    {"id": "s19", "title": "Northern Snows", "text": "Word comes from the North that is worse than dragons — that the dead walk, that the Wall has fallen, that whatever color of king sits at King's Landing will not matter when winter actually arrives.",
     "choices": [
        ("Ride north with all your spears", "Some causes outrank a throne.", "s20"),
        ("Fortify south and let the kingdoms cope", "Charity that ruins you helps no one.", "s21"),
     ]},
    {"id": "s20", "title": "Summons to King's Landing", "text": "A new ruler — whoever survived the wedding, the siege, and the dragon — summons you to court. The summons is silk-wrapped. You know what silk-wrapped summons mean.",
     "choices": [
        ("Attend court and play the long game", "The game of thrones is for those who like rooms.", "end_throne"),
        ("Refuse and rule your small corner well", "Wisdom is also a kind of crown.", "end_quiet"),
     ]},
    {"id": "s21", "title": "Hold the Castle", "text": "You stand on your battlements at dawn and look out at the world you outlived. Maren joins you with two cups of cooling tea. The realm is full of corpses and kings. You and yours are still here.",
     "choices": [
        ("Decide to ride out and build a kingdom of your own", "Small lords can become large ones, given time and luck.", "end_throne"),
        ("Decide enough is enough and live", "Some victories taste like an ordinary morning.", "end_quiet"),
        ("Burn what you cannot defend before the dragon comes", "There is dignity even in ash.", "end_burn"),
     ]},
    {"id": "end_throne", "title": "The Game, Played", "text": "Years later, in a hall hung with the banners of three dead houses, men call you Lord Paramount and bow lower than they used to. You did not start the game. You merely outlived everyone who did. Maren, beside you, hides a smile that has waited a decade.",
     "end": "The Game, Played"},
    {"id": "end_quiet", "title": "A Small Lordship", "text": "Wars end. Kings die. Your river keeps running. You spend your old age in a hall warm with grandchildren and one fat dog, telling stories to people who don't quite believe how close you came to mattering. You laugh. They were the lucky ones.",
     "end": "A Small Lordship"},
    {"id": "end_burn", "title": "Northern Snows", "text": "When winter truly comes you ride north with what you have. Most of you do not return. Songs are sung about you in the long halls of houses you never knew existed. It is a small kind of immortality, but a real one.",
     "end": "Northern Snows"},
])


# ---------------------------------------------------------------------------
# Something Very Bad Is Gonna Happen — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
SVBGH = ({
    "id": "svbgh-the-feeling",
    "title": "The Feeling",
    "sourceTitle": "Something Very Bad Is Gonna Happen",
    "kind": "show",
    "synopsis": "You woke up at 4:11 a.m. with the deep, unshakable certainty that something very bad is about to happen — today, here, to someone you love. You have until the end of the day to figure out what, and whether you can stop it.",
    "releaseYear": 2025,
    "addedAt": "2026-05-20T00:00:00Z",
    "genre": "Thriller",
    "tags": ["dread", "premonition", "family"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "4:11 a.m.", "text": "The feeling arrives before you're fully awake — heavy and certain, like furniture in a dark room. Something very bad is going to happen. You don't know what, only that it's today.",
     "choices": [
        ("Get up and write down everything you sense", "List the dread before it scatters.", "s2"),
        ("Try to go back to sleep — it's just a dream", "Denial is a curtain, not a door.", "s3"),
     ]},
    {"id": "s2", "title": "The List", "text": "On a notepad you write: kitchen, car, your sister, the stairs at work, the bridge. Even reading it back, your hand shakes. Some of these mean nothing. One of them is the thing.",
     "choices": [
        ("Take the list seriously, item by item", "Superstition is sometimes pattern recognition.", "s4"),
        ("Burn the list and shake it off", "Naming a fear gives it shape.", "s5"),
     ]},
    {"id": "s3", "title": "Coffee", "text": "By 7 a.m. you are pretending it's a normal day, with normal coffee. Your partner asks why you keep glancing at the door. You don't have a good answer. The feeling, in daylight, has not gotten smaller.",
     "choices": [
        ("Tell your partner the truth", "Saying it aloud is a kind of test.", "s4"),
        ("Keep it to yourself — they'll think you're spiraling", "Some weights are quieter alone.", "s5"),
     ]},
    {"id": "s4", "title": "Your Sister Calls", "text": "She calls at 7:42 about nothing — running late, the car making a sound, did you call Mom. You hear, very clearly, the thing on your list. The car. The sound. Today.",
     "choices": [
        ("Tell her not to drive, no matter what", "Sometimes love sounds like a command.", "s6"),
        ("Ask careful questions without alarming her", "A net cast wider may catch more.", "s7"),
     ]},
    {"id": "s5", "title": "The Office", "text": "At work the stairwell looks longer than usual. The fluorescents tick. Your boss tells a story about a near-miss on the way in and you actually flinch — and notice that nobody else does.",
     "choices": [
        ("Take the stairs anyway", "Confront what your gut accuses.", "s6"),
        ("Take the elevator and feel ridiculous", "Some battles are not today's.", "s7"),
     ]},
    {"id": "s6", "title": "She Won't Listen", "text": "Your sister laughs — kindly. 'You're being weird,' she says. 'I love you. Bye.' She hangs up and you stand in your kitchen with the phone still warm, and the feeling thickens like fog.",
     "choices": [
        ("Drive to her right now", "Your body knows what your reasons don't.", "s8"),
        ("Trust her and turn your attention elsewhere", "You can't be in every room.", "s9"),
     ]},
    {"id": "s7", "title": "The Pattern", "text": "On the second floor you notice things — a damp patch on the ceiling near the server room, a colleague rubbing her chest, your phone buzzing with an unknown caller. The feeling is sharpening into specifics, but slowly, and not in time.",
     "choices": [
        ("Pull the fire alarm to clear the building", "Disruption now beats catastrophe later.", "s8"),
        ("Quietly tell your supervisor what you sense", "Authority lends courage to weird truths.", "s9"),
     ]},
    {"id": "s8", "title": "The Drive", "text": "You're in your car heading to your sister's office or your own, depending — and you realize you're going too fast, and your hands are very cold. The feeling now includes you. Maybe the thing is you.",
     "choices": [
        ("Pull over and breathe before continuing", "You can't save anyone from a wreck you caused.", "s10"),
        ("Keep going — the urgency is the message", "Hesitation has a body count too.", "s11"),
     ]},
    {"id": "s9", "title": "The Quiet Warning", "text": "Your supervisor frowns and humors you — but she also calls maintenance and tells the floor to stay clear of the stairwell. Small actions ripple. Maybe that's all it takes.",
     "choices": [
        ("Trust that small actions are enough", "Big disasters often arrive on small hinges.", "s10"),
        ("Push for a bigger response anyway", "Better foolish and safe than reasonable and sorry.", "s11"),
     ]},
    {"id": "s10", "title": "10:47 a.m.", "text": "There is a sound — not big, not yet — somewhere across the city. A pop. A drop in air pressure. A siren two blocks over. The feeling now is a needle in your chest.",
     "choices": [
        ("Run toward the sound to help", "Compassion outruns dread, when it can.", "s12"),
        ("Find your people first", "You can't save the world without your own.", "s13"),
     ]},
    {"id": "s11", "title": "Your Mother Calls", "text": "Mom: 'I had the strangest dream about you.' She is not psychic. She is, today, exactly as scared as you are. Until this moment you were maybe two thirds sure you weren't losing your mind.",
     "choices": [
        ("Tell her everything you've sensed", "Two witnesses make a fact.", "s12"),
        ("Lie to keep her calm", "Love and lying share a border.", "s13"),
     ]},
    {"id": "s12", "title": "Hospital Hallway", "text": "Someone you love is here — your sister, your colleague, a stranger you couldn't reach — and the corridor smells like coffee and fear. The feeling has narrowed to one door and one held breath.",
     "choices": [
        ("Sit and wait for news", "Some battles are about endurance.", "s14"),
        ("Demand information from someone in scrubs", "Polite has a cost; impolite has a different one.", "s15"),
     ]},
    {"id": "s13", "title": "Lockdown", "text": "Your phone fills with alerts and your office goes on lockdown for a reason nobody upstairs has named yet. People text 'are you ok' and you can only answer 'I think so.' The feeling shrinks slightly — and gets darker.",
     "choices": [
        ("Help organize the people around you", "Action is the antidote to dread.", "s14"),
        ("Call everyone you love, in order", "Make sure they hear your voice today.", "s15"),
     ]},
    {"id": "s14", "title": "The Small Good", "text": "A nurse, a stranger, a child holds your hand for a moment. Whatever the catastrophe was or wasn't, the day is still full of small good people. The feeling does not lift. It just becomes survivable.",
     "choices": [
        ("Notice the goodness and let it steady you", "Beauty doesn't cancel dread; it carries it.", "s16"),
        ("Keep scanning for the next danger", "Vigilance is hard to switch off.", "s17"),
     ]},
    {"id": "s15", "title": "The News", "text": "The first reports are wrong, like they always are. Then the second reports are wrong differently. Eventually a true sentence arrives, and it is both better and worse than what your body told you at 4:11.",
     "choices": [
        ("Sit with the true sentence", "Truth is a posture you have to settle into.", "s16"),
        ("Try to make sense of why you felt it", "Meaning is a balm and sometimes a trap.", "s17"),
     ]},
    {"id": "s16", "title": "Evening", "text": "The day is winding down without ending you. Your sister is alive, or recovering, or grieving someone else; either way, she is on the other end of a phone call, breathing. You sit by a window and watch the city's lights come on.",
     "choices": [
        ("Decide the feeling was real and useful", "Believe your body next time, too.", "s18"),
        ("Decide it was coincidence with bad timing", "Skepticism is a kind of mercy on yourself.", "s19"),
     ]},
    {"id": "s17", "title": "Aftershock", "text": "A second wave hits — a smaller thing, a near-miss, a phone call about a different cousin. The feeling is now a familiar weight, no longer a stranger. You will, you realize, live the rest of your life with this voice.",
     "choices": [
        ("Make peace with the voice and listen carefully", "A reliable warning is a strange gift.", "s18"),
        ("Decide to fight the voice with therapy and routine", "You don't have to inherit your own dread forever.", "s19"),
     ]},
    {"id": "s18", "title": "11:11 p.m.", "text": "An ordinary hour again. You light a candle for no reason and notice you didn't get killed today, and neither did the people you love most. That is not a small thing. That is, in fact, the only thing.",
     "choices": [
        ("Call your mother before bed", "The bad things will or won't come. Love now.", "s20"),
        ("Write down what you learned today", "Memory is the only seatbelt against forgetting.", "s21"),
     ]},
    {"id": "s19", "title": "What You'll Carry", "text": "You won't tell most people about this day. You'll carry it like a small smooth stone in a pocket — a reminder that catastrophe was once close, and the city kept going, and so did you. It is, somehow, comforting.",
     "choices": [
        ("Keep the stone and the lesson", "Some weights are also anchors.", "s20"),
        ("Put the stone down and walk lighter", "You're allowed to forget on purpose.", "s21"),
     ]},
    {"id": "s20", "title": "The Calls", "text": "You call them — sister, partner, mother, the friend you've been meaning to. Not big speeches. Just 'I love you, I'm glad you're here.' Some of them cry a little. Most of them say 'are you okay?' You are. You are.",
     "choices": [
        ("Make this your new ordinary", "Call the people now, before the next 4:11.", "end_grace"),
        ("Drift back to your old habits in a week", "Even good lessons need re-learning.", "end_human"),
     ]},
    {"id": "s21", "title": "Going to Bed", "text": "Sleep doesn't come fast. The feeling, just before you drift off, returns gently — but this time it's not a warning. It's the simple bedrock fact that you are mortal, and so is everyone you love, and tonight, again, nobody is gone.",
     "choices": [
        ("Sleep with the knowledge as a comfort", "Mortality is also permission to love now.", "end_grace"),
        ("Sleep with one eye open from now on", "Vigilance can be a vow, not a curse.", "end_watch"),
     ]},
    {"id": "end_grace", "title": "Until the Next 4:11", "text": "You don't get more days than you got. You get to do something with the ones you have. The feeling becomes a quiet companion — not a fortune teller, not a curse — just the part of you that has noticed how lucky you are, and how briefly.",
     "end": "Until the Next 4:11"},
    {"id": "end_human", "title": "Ordinary, Mostly", "text": "Time blunts the day. You forget some of the details and remember the rest wrong. That is okay. Most of being human is forgetting what almost killed you and showing up to dinner anyway.",
     "end": "Ordinary, Mostly"},
    {"id": "end_watch", "title": "The Watchful Heart", "text": "You become someone who picks up the phone fast, who locks the door, who checks the smoke detector twice. People tease you for it. People also, on the worst day of their lives, call you first. You are, in a way nobody planned, useful.",
     "end": "The Watchful Heart"},
])


# ---------------------------------------------------------------------------
# Superstore — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
SUPERSTORE = ({
    "id": "superstore-closing-shift",
    "title": "Closing Shift",
    "sourceTitle": "Superstore",
    "kind": "show",
    "synopsis": "It's 9:43 p.m. at Cloud 9. The corporate inspector is hiding in Aisle 7, a man has fallen asleep in a kayak, and somebody — possibly Jonah — set off the indoor sprinklers in Pets. You have seventeen minutes to close. Good luck.",
    "releaseYear": 2021,
    "addedAt": "2026-05-19T00:00:00Z",
    "genre": "Comedy",
    "tags": ["retail", "found-family", "chaos"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "9:43 p.m.", "text": "Glenn announces over the PA that the store will close in seventeen minutes. He then thanks the customers for their patience by name, which slows everyone down. Amy gives you the closer's look — equal parts faith and warning.",
     "choices": [
        ("Start the closing checklist top-down", "Order is a kind of prayer.", "s2"),
        ("Just start chasing customers out, gently", "Aim at the exits, not the aisles.", "s3"),
     ]},
    {"id": "s2", "title": "The Checklist", "text": "You grab the laminated checklist. Step one: cash counts. Step two: zone the front. Step three: locate Marcus, who is somewhere in the store, possibly asleep in outdoor furnishings.",
     "choices": [
        ("Cash count first, by the book", "Cash trouble is the worst trouble.", "s4"),
        ("Locate Marcus first, by the smell", "Lose a coworker, lose your night.", "s5"),
     ]},
    {"id": "s3", "title": "The Stragglers", "text": "There's a man in the kayak, two teenagers using the patio set as a movie theater, and a woman who has been comparing two identical jars of pickles for forty-one minutes. You have, at most, three minutes of polite-voice.",
     "choices": [
        ("Use polite-voice on the kayak guy", "He looks the most receptive — and the most tired.", "s4"),
        ("Use polite-voice on the pickle lady", "Engaging the indecisive is a customer-service skill.", "s5"),
     ]},
    {"id": "s4", "title": "Cash Drawer Trouble", "text": "Sandra's drawer is short eleven dollars. Sandra is approximately one held breath away from a kind, sincere meltdown. Garrett, on the floor, is pretending to be busy in the most Garrett way possible.",
     "choices": [
        ("Cover the eleven dollars yourself", "Some kindnesses cost less than they're worth.", "s6"),
        ("Help Sandra recount calmly", "Numbers solve themselves with company.", "s7"),
     ]},
    {"id": "s5", "title": "Marcus Found", "text": "Marcus is awake, sort of, behind a wall of bargain DVDs. He swears he was 'organizing.' His apron is on backwards. He says he has 'a great idea about the sprinklers.' This sentence cannot be allowed to develop.",
     "choices": [
        ("Send Marcus to break room jail", "Containment is also management.", "s6"),
        ("Put Marcus on a small, safe task", "Idle hands plus Marcus equals fire department.", "s7"),
     ]},
    {"id": "s6", "title": "Corporate, Hiding", "text": "Aisle 7. Crouching behind the bulk paper towels with a clipboard. You make eye contact with the corporate inspector. He pretends to be a customer. You both know.",
     "choices": [
        ("Greet him cheerfully like he isn't a threat", "Sunlight is the best defense.", "s8"),
        ("Ignore him and run a clean close on principle", "Don't audition. Just be good.", "s9"),
     ]},
    {"id": "s7", "title": "Jonah, Existential", "text": "Jonah is leaning on the customer service counter mid-monologue — something about late-stage capitalism and shrink rates. Amy is nodding politely while clearly thinking about three other problems.",
     "choices": [
        ("Cut him off kindly so Amy can breathe", "Friendship is sometimes interruption.", "s8"),
        ("Let him finish — he has a point and a clipboard", "Half his ideas are good. The hard part is which.", "s9"),
     ]},
    {"id": "s8", "title": "The Sprinkler Incident", "text": "The sprinklers go off in Pets. There is a hamster trying to swim. Dina, somewhere far away, is already running this way at top speed.",
     "choices": [
        ("Save the hamster first", "Some priorities transcend hierarchy.", "s10"),
        ("Cut the sprinklers at the panel", "Stopping the cause beats handling the effects.", "s11"),
     ]},
    {"id": "s9", "title": "Glenn, Crying", "text": "Glenn is in the break room, gently crying about a viral video of a dog rescuing a duck. He apologizes, twice. He offers you a Werther's. You can hear, faintly, distant sprinklers.",
     "choices": [
        ("Sit with Glenn for thirty seconds", "Management means moments like this.", "s10"),
        ("Get him back on the floor — gently", "Even Glenn has a closing shift to finish.", "s11"),
     ]},
    {"id": "s10", "title": "Dina Takes Command", "text": "Dina has appeared with a clipboard, a whistle, and her unstoppable certainty that she should be running things. Half the team obeys her on reflex. The other half disappears into shelving.",
     "choices": [
        ("Let Dina run the rescue effort", "Dina + crisis = strange efficiency.", "s12"),
        ("Politely take command back", "Leadership is sometimes a quiet veto.", "s13"),
     ]},
    {"id": "s11", "title": "Mateo's Schemes", "text": "Mateo is pitching you — quietly, urgently — on covering up a thing you don't yet know about. 'It's basically not even a problem if no one looks at the security footage,' he whispers. This sentence has been said before. By Mateo.",
     "choices": [
        ("Refuse and tell him to fix it properly", "Friends don't let friends commit retail fraud.", "s12"),
        ("Listen for one minute, then decide", "Curiosity costs nothing. Yet.", "s13"),
     ]},
    {"id": "s12", "title": "Cheyenne's Baby Stroller Emergency", "text": "Cheyenne's stroller wheel just broke in the parking lot. She's holding the baby and a forty-pack of paper towels and 'fine, I'm fine.' Bo is twenty minutes away.",
     "choices": [
        ("Send Garrett out to help with the stroller", "Garrett is secretly the most useful person in this store.", "s14"),
        ("Go yourself; the floor can wait three minutes", "Closing the store starts with closing on your people.", "s15"),
     ]},
    {"id": "s13", "title": "The Customer Who Won't Leave", "text": "An older man in Electronics says he's waiting for his nephew. He has been waiting for ninety minutes. He has, you suspect, no nephew.",
     "choices": [
        ("Sit with him and ask about his day", "Loneliness is the slowest checkout line.", "s14"),
        ("Call him a cab and walk him to the door", "Kindness can be efficient.", "s15"),
     ]},
    {"id": "s14", "title": "Amy's Quiet Apology", "text": "Amy pulls you aside and apologizes for being short with you earlier. She didn't mean it; her morning was hell; she's running on three hours of sleep. You realize, again, why this is your favorite person at this job.",
     "choices": [
        ("Tell her it's fine; sit on the bench a minute", "Friendship is also a closing-shift task.", "s16"),
        ("Offer to handle the last items so she can go", "Cover someone tonight; be covered next week.", "s17"),
     ]},
    {"id": "s15", "title": "Glenn's Speech", "text": "Glenn, recovered, gathers the team near the front and gives a speech that is too long, too sincere, and somehow, by the end, makes you almost cry into your apron about a $9 dollar T-shirt store you all share.",
     "choices": [
        ("Let him finish; nod along", "Earnestness is the secret religion of this place.", "s16"),
        ("Wrap him up — there's a corporate man watching", "Mercy on the schedule.", "s17"),
     ]},
    {"id": "s16", "title": "The Corporate Verdict", "text": "The inspector approaches you, expressionless. 'You ran a strange store tonight,' he says. He pauses. 'You ran a good one.' He leaves through the wrong door and sets off an alarm. He pretends he meant to.",
     "choices": [
        ("Bask in the win, quietly", "Compliments at Cloud 9 are like rain — rare and remembered.", "s18"),
        ("Pretend you knew it was fine all along", "Confidence is a uniform too.", "s19"),
     ]},
    {"id": "s17", "title": "Last Customer Out", "text": "The pickle lady, finally, walks out — with both jars. The kayak guy waves like he just had a really good time. Marcus, miraculously, is in uniform and roughly conscious.",
     "choices": [
        ("Lock the front doors with ceremony", "Endings deserve a tiny ritual.", "s18"),
        ("Lock them mid-sentence so nobody comes back", "Speed has its own dignity.", "s19"),
     ]},
    {"id": "s18", "title": "The Parking Lot", "text": "Eleven of you spill out into the parking lot under the buzzing Cloud 9 sign. Somebody suggests the diner. Somebody else suggests sleeping. Jonah has Opinions about both options.",
     "choices": [
        ("Go to the diner — these people are your people", "Workplace family is real family with name tags.", "end_diner"),
        ("Go home — you've earned a quiet hour", "Some nights you cash in solitude.", "end_home"),
     ]},
    {"id": "s19", "title": "Tomorrow", "text": "You'll do it again tomorrow. The sprinklers, the inspector, the kayak guy, Glenn crying about animals. You don't love every minute. You love most of them, in the strange retail way that you can never quite explain to people who don't work here.",
     "choices": [
        ("Embrace the chaos — this is your life", "There are worse places to be loved.", "s20"),
        ("Promise yourself you'll leave by Christmas", "Plans are how you survive the unplanned.", "s20"),
     ]},
    {"id": "s20", "title": "The Apron, Hung Up", "text": "You hang your apron on its hook in the break room and look at the line of identical aprons — your shift, your team, your weird little ecosystem. Whatever you do tomorrow, you did this. The store, against most odds, made it through tonight.",
     "choices": [
        ("Commit to the lifer's pride in the work", "There is dignity in keeping the lights on for someone's dad.", "end_career"),
        ("Commit to the leaver's plan, gently", "Saying goodbye well is its own kind of love.", "end_plans"),
     ]},
    {"id": "end_diner", "title": "Booth in the Back", "text": "At the diner you fit eleven people into a booth designed for six. Jonah pays. Mateo doesn't. Amy laughs so hard she snorts, and Glenn says grace and means it. You're tired and shiny-eyed and home — in the strangest possible way.",
     "end": "Booth in the Back"},
    {"id": "end_home", "title": "Quiet Hour", "text": "At home you sit on the floor with the lights off and eat cereal out of the box. Your phone fills with group-chat chaos that you don't open until morning. Tonight you let Cloud 9 be a place you got to leave.",
     "end": "Quiet Hour"},
    {"id": "end_career", "title": "Cloud 9 Lifer", "text": "Years later you'll be a regional something or a manager or a customer — and you'll walk past a Cloud 9 and stop for a second, just to listen to the PA and the carts and the laugh of someone you once closed with. It is, somehow, the soundtrack of your twenties.",
     "end": "Cloud 9 Lifer"},
    {"id": "end_plans", "title": "By Christmas", "text": "You make the plan and you almost stick to it. By the time the holiday displays go up you're applying to other things. You'll leave. You'll come back to visit. You'll be the person who tells the new closer 'it's not that bad' and means it.",
     "end": "By Christmas"},
])


# ---------------------------------------------------------------------------
# Pursuit of Happiness — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
PURSUIT = ({
    "id": "pursuit-happiness-the-internship",
    "title": "The Internship",
    "sourceTitle": "The Pursuit of Happyness",
    "kind": "movie",
    "synopsis": "Twenty unpaid weeks, one son, and exactly nineteen other interns competing for the single job at the end. You can't afford to lose. You also can't afford to win.",
    "releaseYear": 2006,
    "addedAt": "2026-05-18T00:00:00Z",
    "genre": "Drama",
    "tags": ["fatherhood", "ambition", "second chances"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "Day One", "text": "You stand in a borrowed suit on a floor of men in real ones. Your son is in daycare you can't afford. The internship is unpaid. The job, if you win it, will change everything.",
     "choices": [
        ("Speak up early to be noticed", "Visibility is half the game.", "s2"),
        ("Stay quiet and observe everything", "Knowing the room beats announcing yourself.", "s3"),
     ]},
    {"id": "s2", "title": "First Impression", "text": "You ask a sharp question in the morning meeting. A senior broker raises an eyebrow — could be 'impressed,' could be 'put him on my list.' You will, for the next nineteen weeks, never know which.",
     "choices": [
        ("Lean into the bold version of yourself", "Brave is a strategy, not a feeling.", "s4"),
        ("Dial it back and prove yourself in numbers", "Quiet excellence is harder to dismiss.", "s5"),
     ]},
    {"id": "s3", "title": "The Cold Calls", "text": "By afternoon you're on the phones, dialing strangers. Most hang up. One curses you out. You take notes on what worked. You realize you are very, very good at this.",
     "choices": [
        ("Burn through the call list at speed", "Volume is its own kind of magic.", "s4"),
        ("Pick fewer calls, go deeper with each", "Quality is a slow weapon.", "s5"),
     ]},
    {"id": "s4", "title": "The Eviction Notice", "text": "You come home to a piece of paper taped to your door. Fourteen days. Your son shows you a drawing he made. He has not eaten anything green this week. You smile at the drawing.",
     "choices": [
        ("Tell him the truth in kid-sized pieces", "Honesty he can carry is a gift.", "s6"),
        ("Protect him from it for one more night", "Some weights you carry alone, by choice.", "s7"),
     ]},
    {"id": "s5", "title": "A Lead", "text": "A name you cold-called actually calls back — a big one, distracted, but listening. He'll meet you in person if you can be at his office across the city tomorrow at 7 a.m.",
     "choices": [
        ("Commit to the meeting at any cost", "Doors open once, and not by appointment.", "s6"),
        ("Try to reschedule to a day you can manage", "Sometimes the door reopens; usually not.", "s7"),
     ]},
    {"id": "s6", "title": "The Shelter Line", "text": "You and your son stand in line for the church shelter. It rains. He holds a toy rocket. He asks if you have a plan. You say yes — quietly, because the people behind you are too close, and because saying it out loud is also how you start to believe it.",
     "choices": [
        ("Make sure he sees you stay calm", "Calm in a parent is its own kind of meal.", "s8"),
        ("Let him see you're scared, too", "Some lessons require an honest face.", "s9"),
     ]},
    {"id": "s7", "title": "The Big Meeting", "text": "You make it across the city at 7 a.m. — somehow — and the prospect actually shakes your hand. Twenty minutes of his time. You can hear your own heartbeat. Begin.",
     "choices": [
        ("Pitch hard with everything you know", "When the door opens you do not knock politely.", "s8"),
        ("Listen first, then offer what fits him", "The best pitch is sometimes a question.", "s9"),
     ]},
    {"id": "s8", "title": "Subway Bathroom", "text": "There's a night when the shelter is full and you and your son sleep in a subway-station bathroom with the door wedged shut. You sing to him. You promise yourself you will never tell anyone about tonight. You will. Eventually.",
     "choices": [
        ("Sing him through to sleep", "Voice is a kind of roof.", "s10"),
        ("Hold him in silence so he hears your heart", "Some lullabies don't have words.", "s11"),
     ]},
    {"id": "s9", "title": "The Rolodex", "text": "Your manager hands you a rolodex of names and a target. The other interns are richer, better-educated, sharper-suited. You stare at the cards. You realize you have one advantage they don't — desperation.",
     "choices": [
        ("Turn desperation into discipline", "Hunger is a tool only if you sharpen it.", "s10"),
        ("Try to make a friend among the interns first", "Allies inside the wall are also currency.", "s11"),
     ]},
    {"id": "s10", "title": "The Friend", "text": "One of the interns — Naomi, whose father is also her boss somewhere — surprises you. She doesn't pity you. She just sits beside you in the cafeteria like it's normal. You'd forgotten how that felt.",
     "choices": [
        ("Accept the friendship at face value", "Not everyone with money is the enemy.", "s12"),
        ("Stay polite but keep your distance", "Friendship in a competition is a soft target.", "s13"),
     ]},
    {"id": "s11", "title": "The Bone Scanner Sale", "text": "You're still trying to sell the medical scanners you bought before the internship. One left. If you sell it this week the rent is no longer a problem this week.",
     "choices": [
        ("Hustle the scanner with everything you've got", "Old debts don't care about new dreams.", "s12"),
        ("Drop it and focus only on the internship", "Bet on the bigger long game.", "s13"),
     ]},
    {"id": "s12", "title": "Your Son's Birthday", "text": "He turns six. You scrape together a small cake and a story and a promise you can't quite keep. He blows out the candles like it's the easiest day of his life. You realize, watching him, that he thinks it is.",
     "choices": [
        ("Tell him about the dream you're chasing", "Children deserve to know the story they're inside.", "s14"),
        ("Just be present for the day", "Some birthdays don't need a speech.", "s15"),
     ]},
    {"id": "s13", "title": "Midterm Review", "text": "Your supervisor pulls you aside and tells you you're in the top two. He pauses. 'You're also,' he says, 'a year behind everyone in the network.' He is, as senior brokers go, kind.",
     "choices": [
        ("Ask him for one piece of honest advice", "Mentorship is the only shortcut that's safe.", "s14"),
        ("Thank him and double your efforts", "Recognition is fuel.", "s15"),
     ]},
    {"id": "s14", "title": "The Rival", "text": "Another intern — sharper-suited, sharper-tongued — has started taking credit for your accounts. The senior partners can't quite tell. You can.",
     "choices": [
        ("Call it out in the next meeting", "Truth aimed cleanly is allowed at work too.", "s16"),
        ("Beat him on results so loud nobody can mistake them", "Numbers don't lie in this building.", "s17"),
     ]},
    {"id": "s15", "title": "Sick Day", "text": "Your son spikes a fever and the daycare can't keep him. You have a 9 a.m. meeting that cannot be missed. The world has, again, asked you for two whole lives.",
     "choices": [
        ("Bring him to the office, hide him under your desk", "Improvise; apologize; survive.", "s16"),
        ("Skip the meeting and explain truthfully later", "Honesty is also a strategy.", "s17"),
     ]},
    {"id": "s16", "title": "Week Nineteen", "text": "You've been here long enough that the marble lobby looks ordinary. You look down at your hands and they're a little steadier. So is your son's. Your suit fits, finally.",
     "choices": [
        ("Walk in tomorrow like you already work here", "Belonging is a posture you adopt before they grant it.", "s18"),
        ("Stay humble; the decision isn't yours", "Pride is the last thing to lose, and the easiest.", "s19"),
     ]},
    {"id": "s17", "title": "The Final Call", "text": "On the second-to-last day you land an account so improbable a senior partner stares at you for a long moment, then quietly hands you his card. 'Whatever happens Friday,' he says, 'call me.' That sentence is worth more than the job.",
     "choices": [
        ("Be ready to take Friday's news either way", "A door, opened, is an option.", "s18"),
        ("Resolve to take only the offered job, on principle", "Loyalty has its costs and its rewards.", "s19"),
     ]},
    {"id": "s18", "title": "Friday Morning", "text": "Your supervisor calls you into his office. There is a single white envelope on the desk. He smiles, just slightly. You realize you have not breathed in approximately a minute.",
     "choices": [
        ("Open the envelope yourself", "Take the news in your own hands.", "s20"),
        ("Let him tell you out loud", "Some sentences are meant to be spoken.", "s21"),
     ]},
    {"id": "s19", "title": "Whatever Friday Says", "text": "Whatever the envelope says, the truth is already known by the people who've watched you do this — and by your son, who looked at you this morning and said, 'You did it, Dad,' as if it were obvious.",
     "choices": [
        ("Believe him before the envelope speaks", "Some verdicts beat the official ones.", "s20"),
        ("Wait for the room to call it official", "Hope and proof both have their seats.", "s21"),
     ]},
    {"id": "s20", "title": "The Offer", "text": "It's yes. It's the job. There are tears you didn't plan and a handshake you'll remember and a phone call to your sister that you make in a stairwell so nobody sees you cry. None of it feels real. All of it is.",
     "choices": [
        ("Take the job and build the life", "Doors open. Walk through.", "end_job"),
        ("Take the job — and remember everyone who helped", "Success is not a solo act.", "end_grateful"),
     ]},
    {"id": "s21", "title": "Whatever Comes Next", "text": "Whether the envelope says yes or no, you walk out of the building taller than you walked in. You learned what you came to learn — that you can take a punch and stand up. The senior partner's card is warm in your pocket.",
     "choices": [
        ("Call the senior partner Monday no matter what", "When the front door closes, knock on a window.", "end_door"),
        ("Take your son out for something silly", "Today is for him. Tomorrow is for everything else.", "end_son"),
     ]},
    {"id": "end_job", "title": "Stockbroker", "text": "Years later, in a corner office, you find a small plastic rocket in the bottom drawer and laugh and almost cry. The boy who once asked if you had a plan is in college now. You had a plan. You just had to learn it as you went.",
     "end": "Stockbroker"},
    {"id": "end_grateful", "title": "The People Who Carried You", "text": "You learn fast to send the elevator back down. You hire from shelters, from night classes, from places you knew. The job becomes a door you hold open for someone else. That, you realize, is what pursuit actually means.",
     "end": "The People Who Carried You"},
    {"id": "end_door", "title": "The Other Door", "text": "You don't get the internship's job. You make the call. The other door opens — smaller, slower, but yours. Some pursuits are not a straight line. Yours is more interesting for the detour.",
     "end": "The Other Door"},
    {"id": "end_son", "title": "Your Son's Father", "text": "Whatever the job becomes, you become a father who is present, who showed up, who proved a man can be broke and not broken. He grows up steady because you decided to. That is, by any honest measure, the better fortune.",
     "end": "Your Son's Father"},
])


# ---------------------------------------------------------------------------
# The Great — ⭐⭐⭐⭐⭐🌟
# ---------------------------------------------------------------------------
THE_GREAT = ({
    "id": "the-great-coup-season",
    "title": "Coup Season",
    "sourceTitle": "The Great",
    "kind": "show",
    "synopsis": "You arrived in Russia at fifteen, married a man-child emperor at sixteen, and by autumn you have decided, politely, to take the throne for yourself. Huzzah.",
    "releaseYear": 2023,
    "addedAt": "2026-05-17T00:00:00Z",
    "genre": "Comedy",
    "tags": ["court", "coup", "wit"],
    "rating": 5,
    "loved": True,
}, [
    {"id": "s1", "title": "The Wedding Bed", "text": "Peter is asleep, snoring like a stabbed bear, with one foot on your pillow. The candles are guttering. You stare at the ceiling and decide, in the politest possible terms, to overthrow him by spring.",
     "choices": [
        ("Plan it carefully — alone, for now", "Conspiracies of one are the only safe kind.", "s2"),
        ("Find one ally tomorrow morning", "Even queens need a witness.", "s3"),
     ]},
    {"id": "s2", "title": "The Library", "text": "You sneak into the imperial library and read every book Peter has banned. Most are merely better than him. A few are dangerous. You take notes in a tiny hand and hide them in a hollowed prayer book. Huzzah.",
     "choices": [
        ("Lean into the danger of new ideas", "Reading is the first regicide.", "s4"),
        ("Choose which ideas to share, and with whom", "Strategy in the margins.", "s5"),
     ]},
    {"id": "s3", "title": "Marial, Maid and Mind", "text": "Marial, who was a lady before Peter's father exiled her family to scrubbing floors, eyes you sideways and says, 'You're not as dim as you look.' This is the warmest thing anyone has said to you in Russia.",
     "choices": [
        ("Recruit her openly into your plan", "An enemy of the same enemy is an ally.", "s4"),
        ("Test her loyalty with smaller secrets first", "Friendship is also a vetting process.", "s5"),
     ]},
    {"id": "s4", "title": "Orlo's Eyes", "text": "Orlo, an advisor with very small spectacles and very large fears, has been writing pamphlets nobody reads. He thinks Russia could be reformed. He also, you suspect, thinks he is about to faint.",
     "choices": [
        ("Promise him reform in exchange for help", "Marry his ideas to your appetite.", "s6"),
        ("Recruit him by terrifying him politely", "Fear is an underrated motivator.", "s7"),
     ]},
    {"id": "s5", "title": "Peter's Cruelty", "text": "Peter shoots a bear that lived in a garden because it was 'in his sun.' Then he weeps about it, kindly, for an hour. He is awful in nine ways at once, including charming. You write it all down.",
     "choices": [
        ("Use his contradictions against him", "A man who cries and shoots is a man with seams.", "s6"),
        ("Pity him just enough to stay safe", "Tenderness can be camouflage.", "s7"),
     ]},
    {"id": "s6", "title": "The Patriarch", "text": "Archbishop Archie — perfumed, sly, dangerous — invites you to chapel. Faith in Russia is a sword pretending to be a candle. He smiles. He wants to know whose side God will be on this winter.",
     "choices": [
        ("Promise the church it will keep its lands", "Faith is the largest landlord.", "s8"),
        ("Promise the church one reform at a time", "Compromise as a velvet glove.", "s9"),
     ]},
    {"id": "s7", "title": "The Army", "text": "General Velementov, drunk by lunch and brilliant by accident, is the closest thing the army has to a brain. He has stopped believing in Peter. He has not, yet, started believing in you.",
     "choices": [
        ("Charm Velementov into your circle", "Soldiers follow conviction, not titles.", "s8"),
        ("Threaten Velementov into your circle", "Pride wounded can be useful.", "s9"),
     ]},
    {"id": "s8", "title": "The Salon", "text": "You start a salon — books, ideas, women allowed to speak. The court calls it a scandal. The women, quietly and quickly, call it church. Half your future ministers are taking notes in the corner.",
     "choices": [
        ("Use the salon to seed your reforms", "Ideas pour out of rooms that are too small to hold them.", "s10"),
        ("Use the salon to spot your loyalists", "Talent reveals itself when it feels welcome.", "s11"),
     ]},
    {"id": "s9", "title": "The Hunt", "text": "Peter takes you hunting and tells you, drunk, that he 'sometimes' worries you might be cleverer than him. He laughs. He waits. You realize you are choosing your own life with the next sentence.",
     "choices": [
        ("Flatter him brilliantly and live", "A clever woman in this room is a dead woman without a smile.", "s10"),
        ("Tell him a smaller version of the truth", "Honesty in homeopathic doses.", "s11"),
     ]},
    {"id": "s10", "title": "Smallpox", "text": "An outbreak. The court panics. You have read about a procedure — inoculation — that everyone considers heresy. You could save thousands. You could also be torn apart in the street for it.",
     "choices": [
        ("Inoculate yourself first, publicly", "Lead with your own veins.", "s12"),
        ("Quietly inoculate the children of allies", "Save who you can; survive to save more.", "s13"),
     ]},
    {"id": "s11", "title": "Peter's Mother's Portrait", "text": "Peter speaks to a portrait of his mother as if she could answer. He is, terribly, a small boy in a large hat. You find that tonight, against your better judgement, you don't want to kill him. You want to fix him.",
     "choices": [
        ("Resolve to depose him without killing him", "Mercy is also a strategy.", "s12"),
        ("Resolve to depose him fully; sentiment is fatal", "Soft hearts make short reigns.", "s13"),
     ]},
    {"id": "s12", "title": "The Coup, Planned", "text": "In the deep cold of a December night you and Marial and Orlo and Velementov bend over a map of the Winter Palace. You count guards. You count corridors. You count, mostly, the people you have to ask to risk their lives.",
     "choices": [
        ("Strike at the Christmas ball", "Spectacle covers footsteps.", "s14"),
        ("Strike at dawn after a long quiet day", "Boredom is the best disguise.", "s15"),
     ]},
    {"id": "s13", "title": "Betrayal", "text": "One of your circle has wavered — Archbishop Archie, maybe, or someone smaller. A letter has reached Peter that mentions your name with a verb he won't like. You have hours, not days.",
     "choices": [
        ("Move the coup forward to tonight", "Improvise or die polite.", "s14"),
        ("Bluff your way through it and buy time", "Charm has saved smaller empires.", "s15"),
     ]},
    {"id": "s14", "title": "The Ballroom", "text": "Candles, mirrors, three orchestras, the whole court turning like a slow gilded wheel. Peter is dancing badly. Velementov is at the doors. You smile. You step toward the center of the floor.",
     "choices": [
        ("Make a public speech declaring the new order", "Theater is power's first language.", "s16"),
        ("Strike quietly first, speak after", "Surgery before the announcement.", "s17"),
     ]},
    {"id": "s15", "title": "Dawn Move", "text": "Before sunrise your loyalists move through the palace's nervous corridors. There are surprisingly few deaths and surprisingly many men changing sides on the spot. Russia loves a winner more than a tsar.",
     "choices": [
        ("Spare every life you can", "Reigns founded on mercy hold longer.", "s16"),
        ("Spare only the necessary ones", "A wise queen knows arithmetic.", "s17"),
     ]},
    {"id": "s16", "title": "Peter, Cornered", "text": "He sits on the floor of his own bedroom looking up at you like a child who has lost a game whose rules he made up. 'You really did it,' he says. He sounds almost proud.",
     "choices": [
        ("Send him into gilded exile", "Keep your enemy alive and decorative.", "s18"),
        ("Force him to abdicate publicly", "Paperwork is the truest crown.", "s19"),
     ]},
    {"id": "s17", "title": "The Crown", "text": "Archbishop Archie, who almost betrayed you, kneels on instinct because Russia has shown him whose side God is now on. The crown is heavier than it looks. The mirror behind him reflects a woman you barely recognize.",
     "choices": [
        ("Wear it with steel", "The future is shaped by women who do not flinch.", "s18"),
        ("Wear it with care", "Power held lightly is held longest.", "s19"),
     ]},
    {"id": "s18", "title": "The Reforms", "text": "In your first hundred days you free the serfs of three provinces, build two schools, and survive four attempts on your life. Russia, baffled and delighted, calls it a beginning. You call it Tuesday.",
     "choices": [
        ("Push the reforms harder, faster", "Momentum is itself protection.", "s20"),
        ("Slow down to build the institutions that will outlast you", "A reform that depends on a queen dies with one.", "s21"),
     ]},
    {"id": "s19", "title": "A Child", "text": "You are pregnant, possibly by Peter, possibly not. The court bets discreetly. You decide, alone in a snowed-in garden, that the child will be raised to know more languages than thrones and more books than crowns.",
     "choices": [
        ("Raise an heir for the new Russia", "Continuity is a kind of revolution.", "s20"),
        ("Decline the dynasty game entirely", "Some empires should not be inherited.", "s21"),
     ]},
    {"id": "s20", "title": "The Long Reign", "text": "Years pass. The empire grows wider, kinder, stranger. Your enemies write books about you that are mostly lies and partly accurate. Marial has her own salon now. Orlo has stopped fainting. Velementov has, on most days, sobered up.",
     "choices": [
        ("Reign for as long as you live", "Empires are stories you keep telling.", "end_great"),
        ("Abdicate to a successor on your own terms", "The bravest crown is the one you put down.", "end_legacy"),
     ]},
    {"id": "s21", "title": "Peter, Late", "text": "Years later you visit Peter in his comfortable exile — fat, sad, gardening, occasionally good. He laughs about old times. You realize, walking away, that the strangest thing about ruling Russia is that you both, somehow, won.",
     "choices": [
        ("Forgive him on the carriage ride home", "Forgiveness is the last revolution.", "end_legacy"),
        ("Keep him in his comfortable exile forever", "Some mercies have walls.", "end_great"),
     ]},
    {"id": "end_great", "title": "Catherine the Great", "text": "They will call you Great. You will call you tired. The salons you started outlive you. The reforms you broke yourself on become ordinary. Somewhere in Europe a girl reads your name and decides, secretly, that she will rule too. Huzzah.",
     "end": "Catherine the Great"},
    {"id": "end_legacy", "title": "Huzzah, And Then", "text": "You step down on a day of your choosing, into a quiet life of books and chosen company. The crown goes onto a head that has read more books than its predecessors combined. The empire, for now, does not collapse. You take that as a win.",
     "end": "Huzzah, And Then"},
])


# ---------------------------------------------------------------------------
# Wayward — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
WAYWARD = ({
    "id": "wayward-tall-pines",
    "title": "Tall Pines",
    "sourceTitle": "Wayward",
    "kind": "show",
    "synopsis": "Your daughter is enrolled at Tall Pines Academy, the troubled-teen 'school' on the edge of a town where every adult smiles the same way. By morning you'll wish you'd never read the brochure.",
    "releaseYear": 2025,
    "addedAt": "2026-05-16T00:00:00Z",
    "genre": "Thriller",
    "tags": ["cult", "small-town", "missing"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Welcome to Town", "text": "The 'Welcome to Wayward' sign is hand-painted and the smile of the diner waitress is hand-painted too. Your daughter pretends to sleep in the passenger seat. Tall Pines Academy is two miles uphill.",
     "choices": [
        ("Stop at the diner first", "Eavesdrop before you enroll.", "s2"),
        ("Drive straight to the academy", "Delay is doubt's open door.", "s3"),
     ]},
    {"id": "s2", "title": "The Diner", "text": "Three locals stop talking when you walk in. The waitress is friendly in a way that feels rehearsed. A boy in his early twenties keeps glancing at your bumper sticker.",
     "choices": [
        ("Try to make conversation about the academy", "Information lives in small talk.", "s4"),
        ("Eat quickly and leave", "Some rooms tighten if you stay.", "s5"),
     ]},
    {"id": "s3", "title": "The Gates", "text": "Wrought iron, freshly painted. A counselor named Evelyn meets you with a clipboard and a hug she has practiced. Your daughter's hand is suddenly very cold in yours.",
     "choices": [
        ("Sign the intake forms quickly", "You came here to do this.", "s4"),
        ("Ask to see the dorm first", "Trust earned beats trust assumed.", "s5"),
     ]},
    {"id": "s4", "title": "The Tour", "text": "The grounds are beautiful in a sterilized way — every flower planted, every kid smiling the moment a counselor passes. A girl walks the path with her eyes carefully forward, like she is being graded on it.",
     "choices": [
        ("Stop and speak to one of the students", "A real face will tell you more than the tour.", "s6"),
        ("Stay on the script of the tour", "Don't tip your suspicion yet.", "s7"),
     ]},
    {"id": "s5", "title": "The Sheriff", "text": "The sheriff happens to be at the gate, friendly, broad. He compliments your car. He mentions that 'parents who second-guess' tend to make things harder for their kids.",
     "choices": [
        ("Smile and play along for now", "Don't show your hand to the law.", "s6"),
        ("Ask him bluntly what he meant", "Some bluffs collapse if you call them.", "s7"),
     ]},
    {"id": "s6", "title": "The Girl in the Garden", "text": "She kneels by the tomatoes and whispers without looking at you: 'They listen at the dorms after lights out.' Then, louder: 'These are the cherry kind.'",
     "choices": [
        ("Take her warning seriously", "Truth from a child here is gold.", "s8"),
        ("Wonder if she's manipulating you", "Suspicion can also be useful here.", "s9"),
     ]},
    {"id": "s7", "title": "Lights Out Tour", "text": "Evelyn explains the nightly schedule with a calm that does not match the words: 'Devices collected at 7:45. Personal items reviewed weekly. Privileges earned through Trust.' She capitalizes Trust audibly.",
     "choices": [
        ("Refuse the device collection rule", "Set one boundary they can't dissolve.", "s8"),
        ("Accept it for tonight only", "Pick the hill another day.", "s9"),
     ]},
    {"id": "s8", "title": "The Missing Kid", "text": "Posters near the laundry room: a boy who 'graduated' six months ago, missing since the weekend. Evelyn whisks you past, talking too brightly about the dining hall.",
     "choices": [
        ("Take a photo of the poster", "Evidence is portable.", "s10"),
        ("Pretend not to notice and keep watching", "Cameras work both ways here.", "s11"),
     ]},
    {"id": "s9", "title": "Your Daughter Whispers", "text": "She holds your sleeve at the dorm door and says, very quietly, 'Don't leave me here.' It is the first thing she has said to you with feeling in six months.",
     "choices": [
        ("Walk her back to the car right now", "Trust the kid you came to save.", "end_leave_early"),
        ("Stay one night to see what they do", "Knowledge is its own kind of rescue.", "s10"),
     ]},
    {"id": "s10", "title": "The Headmistress", "text": "Helen Caplan — the founder — sits with you in a sunroom of plants you can't name. She is graceful, persuasive, terrifying in the way only kind voices can be. She knows your daughter's case file by heart.",
     "choices": [
        ("Match her calm and listen", "Underestimate her and you lose your daughter.", "s12"),
        ("Push her for specifics about the missing kid", "Make her speak in particulars.", "s13"),
     ]},
    {"id": "s11", "title": "After Lights Out", "text": "From a window of the guest cabin you watch a small line of students walk in silence toward the woods at 1 a.m., escorted by counselors carrying flashlights. They return three hours later. The walk has a name. The walk does not have a permission slip.",
     "choices": [
        ("Follow them tomorrow night", "See it before you accuse it.", "s12"),
        ("Photograph what you can right now", "Document while it's strange to you.", "s13"),
     ]},
    {"id": "s12", "title": "The Ally", "text": "A junior counselor named Abel meets your eye in a hallway and, on the way past, slides a folded napkin into your hand. 'Bridge. 11 p.m.,' it says. Either it's a trap or a lifeline. Maybe both.",
     "choices": [
        ("Meet him at the bridge", "Risk is sometimes the rescue.", "s14"),
        ("Burn the napkin and stay alert", "Strangers in cults are rarely free agents.", "s15"),
     ]},
    {"id": "s13", "title": "The Office", "text": "You slip into the records office on a long shot. Half the files are real, half are paper-thin theatre. You photograph three before voices come down the hall, and the door, when you try it, is locked.",
     "choices": [
        ("Hide in the closet", "Buy time at the cost of nerve.", "s14"),
        ("Climb out the window onto the lawn", "Commit to escape before you're caught.", "s15"),
     ]},
    {"id": "s14", "title": "Bridge at Eleven", "text": "Abel is younger than you thought, scared, and angry. He's been here since he was sixteen. 'They keep the ones who can't be sold back to families,' he says. 'Some of us are staff because there's nowhere else to go.'",
     "choices": [
        ("Promise to get him out too", "Save who you can, when you can.", "s16"),
        ("Take the information and run", "Heroics multiply risk.", "s17"),
     ]},
    {"id": "s15", "title": "Across the Lawn", "text": "You sprint across the lit lawn with photos on a phone Helen will absolutely take in the morning if you let her. The guest cabin door is suddenly twenty miles away. A dog starts somewhere.",
     "choices": [
        ("Upload the photos to the cloud now", "Get it off you before it can be erased.", "s16"),
        ("Wipe the phone clean and rely on memory", "If they search you, find nothing.", "s17"),
     ]},
    {"id": "s16", "title": "Your Daughter's Door", "text": "You creep into the dorm and find her awake, alert, dressed. 'I knew you were coming back,' she says. She has been ready every night.",
     "choices": [
        ("Take her and as many girls as will come", "Rescue is contagious if you let it be.", "s18"),
        ("Take only her — keep this simple", "A clean escape is its own miracle.", "s19"),
     ]},
    {"id": "s17", "title": "Helen, Awake", "text": "Helen is in the foyer in a robe like she's been waiting for you. She offers tea. She tells you, gently, that there is no version of this story where you are the hero.",
     "choices": [
        ("Refuse the tea and walk through her", "Confidence is a passport.", "s18"),
        ("Sit and let her speak — buy minutes", "Sometimes the door opens behind you while she talks.", "s19"),
     ]},
    {"id": "s18", "title": "The Run", "text": "Down a gravel drive at 3 a.m. with your daughter and, somehow, four other girls in the back seat. Two trucks come up behind you, headlights on. The road is dark and long and yours.",
     "choices": [
        ("Outrun the trucks to the county line", "Cross a border, change the law you're under.", "s20"),
        ("Cut off the road and use the back trails", "Wayward, weirdly, taught you these.", "s21"),
     ]},
    {"id": "s19", "title": "The Hostage Calm", "text": "Helen smiles. 'You can leave tonight,' she says, 'or your daughter can graduate next year. Choose.' The trick is that she means both versions.",
     "choices": [
        ("Pretend to choose 'leave' and improvise", "Buy the exit you need.", "s20"),
        ("Refuse her terms loudly enough to be heard outside", "Witnesses are the cult's only allergen.", "s21"),
     ]},
    {"id": "s20", "title": "The County Line", "text": "You make it. The sun is coming up. Your daughter is asleep on the other girls' shoulders. The county sheriff's car flashes its lights and pulls you over — and the deputy at the window, blessedly, has never heard of Tall Pines.",
     "choices": [
        ("Tell him everything, now", "Truth told fast is a fence Helen can't climb.", "end_safe"),
        ("Drive on with a story and seek a journalist", "Court of public opinion is faster than court of law.", "end_expose"),
     ]},
    {"id": "s21", "title": "The Press", "text": "A reporter you cold-called from a gas-station pay phone agrees to meet at noon. She has been trying to crack Wayward for three years. You have, by accident, given her the headline.",
     "choices": [
        ("Go on the record with everything", "Burn it down with paper and ink.", "end_expose"),
        ("Stay anonymous and trade documents only", "Some safety is a smaller name.", "end_safe"),
     ]},
    {"id": "end_leave_early", "title": "The Brochure", "text": "You don't enroll her. You drive eight more hours that night, with the brochure on the passenger seat, and start over the next morning at a different kind of help. Years later she tells you the only thing she's ever thanked you for is the night you turned around.",
     "end": "The Brochure"},
    {"id": "end_safe", "title": "Quietly Free", "text": "You and your daughter, and four girls you didn't know two days ago, end up in a small city far from Wayward. The investigation grinds slowly. You testify when asked. You sleep with the porch light on. You sleep.",
     "end": "Quietly Free"},
    {"id": "end_expose", "title": "The Headline", "text": "The story breaks. Tall Pines closes inside a month. Helen Caplan is on three magazine covers and one indictment. Your daughter, who once would not look at you, sits beside you on a couch and squeezes your hand during the press conference.",
     "end": "The Headline"},
])


# ---------------------------------------------------------------------------
# Bodkin — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
BODKIN = ({
    "id": "bodkin-the-podcast",
    "title": "The Bodkin Tapes",
    "sourceTitle": "Bodkin",
    "kind": "show",
    "synopsis": "A podcast crew, a sleepy Irish town, and a Samhain festival twenty years ago where three people vanished without a trace. You came for a true-crime story. You'll get a bigger one.",
    "releaseYear": 2024,
    "addedAt": "2026-05-15T00:00:00Z",
    "genre": "Thriller",
    "tags": ["podcast", "small-town", "secrets"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Arrival", "text": "Bodkin is wetter and smaller than the brochure suggested. Your microphone hisses in the rain. Sister Mary at the B&B watches your producer Dove like she has seen her before, in a dream she didn't like.",
     "choices": [
        ("Start with the publican, Seamus", "Pubs hold towns together and apart.", "s2"),
        ("Start with the missing kids' families", "Begin where the wound is.", "s3"),
     ]},
    {"id": "s2", "title": "The Pub", "text": "Seamus pours your Guinness in a long slow ritual and answers everything sideways. He smiles at jokes you didn't make. He tells you to ask anyone about Samhain '99 and nobody will answer the same way twice.",
     "choices": [
        ("Buy the next round and listen", "Patience pours information.", "s4"),
        ("Push him about specific names", "Pressure can crack a smile.", "s5"),
     ]},
    {"id": "s3", "title": "The Mother", "text": "Maeve's mother has aged thirty years in twenty. She speaks of her missing daughter in the present tense. She makes you tea you don't deserve and, finally, asks if you really believe a podcast will bring her home.",
     "choices": [
        ("Tell her the truth: probably not", "Honesty is the only respect.", "s4"),
        ("Promise to try anyway", "Hope misused is still hope.", "s5"),
     ]},
    {"id": "s4", "title": "The Tapes", "text": "Dove finds a box of cassette tapes in the back of a community-center cupboard — interviews recorded by a local journalist in 1999 who, you discover, also disappeared the same week.",
     "choices": [
        ("Listen straight through, no skipping", "Patterns live in tedious places.", "s6"),
        ("Skim for names and dates first", "Triangulate before you immerse.", "s7"),
     ]},
    {"id": "s5", "title": "The Garda", "text": "Sergeant O'Shea is helpful and not. He gives you photocopies that have been photocopied a hundred times. The names of three of the original investigators are inked out. He smiles when you notice.",
     "choices": [
        ("Ask why those names are missing", "Curiosity is your only weapon.", "s6"),
        ("Smile back and steal a peek at his notes", "Sometimes a notebook tells a story a man won't.", "s7"),
     ]},
    {"id": "s6", "title": "The Festival Returns", "text": "Samhain is in three days and the town is dragging out the same costumes they wore in 1999. Children with goat masks. Adults pretending it's all in good fun. Dove is taking notes on her hand.",
     "choices": [
        ("Plan to attend Samhain in person", "Endings often start where beginnings did.", "s8"),
        ("Investigate the costume committee", "Same masks, same hands.", "s9"),
     ]},
    {"id": "s7", "title": "Gilbert's Doubts", "text": "Your American host Gilbert is sweating. He wanted a charming story. He is getting one and dreading it. He pulls you aside: 'What if we got these people killed by digging?' He has, you suspect, a point.",
     "choices": [
        ("Reassure him and keep going", "Pressing on is the only way through.", "s8"),
        ("Agree to slow down and verify more", "Doubt is sometimes data.", "s9"),
     ]},
    {"id": "s8", "title": "The Boat Wreck", "text": "A small boat once owned by Seamus's late father is half-buried in a tidal cove. The man on the cliff above you watches you find it. By the time you climb back up, he is gone.",
     "choices": [
        ("Dig up the boat properly", "Some graves are made of wood.", "s10"),
        ("Mark the spot and report it later", "Don't get caught alone with a discovery.", "s11"),
     ]},
    {"id": "s9", "title": "The Convent", "text": "Sister Mary's convent has, you learn, been a Magdalene-style laundry once — a place where unwanted girls were 'reformed.' The town's official history says it closed in 1972. The water bill says different.",
     "choices": [
        ("Get inside the convent grounds", "The truth is often architectural.", "s10"),
        ("Approach Sister Mary directly", "Stories told by their keepers are still stories.", "s11"),
     ]},
    {"id": "s10", "title": "The Threat", "text": "You wake to find your car's tires flat and a goat mask on the bonnet. A note, in town-meeting handwriting: 'Go home. Bodkin doesn't want this story.' The town's want is debatable.",
     "choices": [
        ("Stay and publicize the threat", "Visibility is armor.", "s12"),
        ("Pretend to leave and circle back quietly", "Decoy is also strategy.", "s13"),
     ]},
    {"id": "s11", "title": "Maeve, Maybe", "text": "An anonymous email: a photograph of a woman in her late thirties on a street in Cork, with a thin scar above her eyebrow. The subject line is the name of the missing girl. Either it's her, or it's bait.",
     "choices": [
        ("Drive to Cork and find her", "Some questions only answer in person.", "s12"),
        ("Trace the email's metadata first", "Digital footprints last.", "s13"),
     ]},
    {"id": "s12", "title": "Seamus's Cottage", "text": "Seamus sits on his porch with a shotgun across his lap and a pot of tea. He is not threatening you. He is, surprisingly, ready to talk. 'I made a wrong choice when I was twenty-two,' he says, 'and I've been paying since.'",
     "choices": [
        ("Press record gently", "Let the confession breathe.", "s14"),
        ("Put the recorder down and just listen", "Some truths shrink under microphones.", "s15"),
     ]},
    {"id": "s13", "title": "The Real Disappearances", "text": "You finally understand: only one person actually disappeared on Samhain 1999. The other two left voluntarily. The crime everyone has been blaming for twenty years was, in fact, a much smaller, sadder crime — and a much bigger ongoing one.",
     "choices": [
        ("Tell the families before the podcast", "Decency before downloads.", "s14"),
        ("Plan the reveal as the season finale", "Story has its own gravity.", "s15"),
     ]},
    {"id": "s14", "title": "Samhain Night", "text": "Fires on the hill, masks in the lane, a town pretending it is the same town it has always been. Dove disappears into the crowd and reappears with a stranger pulling at her arm. You move.",
     "choices": [
        ("Intervene physically", "Some moments demand a body.", "s16"),
        ("Get it all on tape from a safe distance", "Witness is also a verb.", "s17"),
     ]},
    {"id": "s15", "title": "The Smaller Crime", "text": "The original journalist's tapes contain a single sentence buried in casual chat: a man with a senior council position assaulting a teenager. The teenager is now a grown woman who runs the cafe. She has been waiting twenty years for someone to listen.",
     "choices": [
        ("Center her story, not the mystery", "Make the right thing the loudest thing.", "s16"),
        ("Both stories at once, carefully", "Truth is rarely tidy.", "s17"),
     ]},
    {"id": "s16", "title": "The Confession", "text": "On a windswept dock at dawn, the man who has run Bodkin's council for thirty years tells you most of what he did, in the cracked voice of someone who has been waiting to be caught. The recorder is on. He knows.",
     "choices": [
        ("Take the confession to the Garda", "Law is slower than podcast but harder to delete.", "s18"),
        ("Take it to the cafe owner first", "Survivors lead the response.", "s19"),
     ]},
    {"id": "s17", "title": "The Town Hall", "text": "Bodkin gathers — by accident or by design — in the town hall on the morning after Samhain. The truth, half-aired already, hangs in the room. People are deciding, in real time, which version they will live with.",
     "choices": [
        ("Speak first and frame the truth", "Authorship matters.", "s18"),
        ("Let a local voice speak first", "Belonging carries credibility.", "s19"),
     ]},
    {"id": "s18", "title": "The Edit", "text": "Back in Dublin, in a small flat smelling of takeout, you sit with Dove and Gilbert and a timeline. The choices you make in this edit decide what 'Bodkin' means for the next decade.",
     "choices": [
        ("Cut the sensational version", "The download numbers will be brutal — and necessary.", "s20"),
        ("Cut the careful, accurate version", "Tell it slow; tell it true.", "s21"),
     ]},
    {"id": "s19", "title": "The Cafe Owner's Choice", "text": "She listens to the rough cut twice. Then she asks, very quietly, if you can use her name. You tell her yes, but only if she's sure. She is.",
     "choices": [
        ("Honor her name on the cover", "Survivors choose their visibility.", "s20"),
        ("Anonymize but tell the truth fully", "Privacy and truth can share a sentence.", "s21"),
     ]},
    {"id": "s20", "title": "Release Day", "text": "The episode drops at midnight. By morning the comments are a wall. By afternoon RTÉ wants you on the news. By evening Sergeant O'Shea calls — politely furious, professionally grateful.",
     "choices": [
        ("Take the wins and go home", "Some stories are done with you.", "end_done"),
        ("Stay involved through the trial", "Some stories aren't.", "end_stay"),
     ]},
    {"id": "s21", "title": "The Town After", "text": "Bodkin doesn't recover the way you imagined. It changes, slowly, like a tide changing the shape of a cove. Some people leave. Some people, finally, come home. The podcast becomes part of the town's mythology, like the festival once was.",
     "choices": [
        ("Visit Bodkin every year on Samhain", "Bear witness as a ritual.", "end_return"),
        ("Move on; the work was the work", "Some places have to be allowed to heal without you.", "end_done"),
     ]},
    {"id": "end_done", "title": "End of Season", "text": "You finish the season, swear off true crime, and start a podcast about coastlines. It does fine. Sometimes, late, you put on the Bodkin episodes and listen the way you listen to a person who survived something with you.",
     "end": "End of Season"},
    {"id": "end_stay", "title": "Through the Trial", "text": "The trial takes two years. You're there for the verdict, in the back row. The cafe owner finds you afterward and hugs you with a fierceness you'll remember when other stories test your courage.",
     "end": "Through the Trial"},
    {"id": "end_return", "title": "Every Samhain", "text": "You go back every year. The masks come out. The fires light. The town is wary, then warm, then itself. You walk along the cliffs with Sister Mary one autumn and she says, almost smiling, 'You're one of ours now.' You take that more seriously than any award.",
     "end": "Every Samhain"},
])


# ---------------------------------------------------------------------------
# Scary Movie 4 — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
SCARY_MOVIE_4 = ({
    "id": "scary-movie-4-the-spoof",
    "title": "Final Spoof",
    "sourceTitle": "Scary Movie 4",
    "kind": "movie",
    "synopsis": "Aliens. Ghosts. A grim village. A hand reaching out of the well. Also somebody on a unicycle for no reason. Welcome to the parody — pick the dumbest possible choice and probably live.",
    "releaseYear": 2006,
    "addedAt": "2026-05-14T00:00:00Z",
    "genre": "Comedy",
    "tags": ["parody", "horror", "absurd"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Suburb in Peril", "text": "An ominous tripod legs over your fence. Your neighbor Tom screams artistically. A baby in a stroller deadlifts a chainsaw. You're holding a TV remote and a half-eaten waffle.",
     "choices": [
        ("Brandish the waffle", "Absurdity is a shield in this universe.", "s2"),
        ("Run dramatically in slow motion", "Style is survival.", "s3"),
     ]},
    {"id": "s2", "title": "The Basement", "text": "You hide in the basement, which has, inexplicably, a karaoke machine and three life-size mannequins of yourself. One of them is doing your taxes.",
     "choices": [
        ("Sing karaoke at the tripod", "Distract aliens with American Idol.", "s4"),
        ("Fight your tax-doing doppelganger", "Self-loathing made literal.", "s5"),
     ]},
    {"id": "s3", "title": "The Grim Village", "text": "You sprint and accidentally arrive in a black-and-white village from a completely different horror movie. The elders look at you suspiciously. There is a strict no-shoes policy.",
     "choices": [
        ("Bow to the elders", "When in spoof, do as the spoof does.", "s4"),
        ("Eat the forbidden grapes immediately", "Curiosity killed the parody.", "s5"),
     ]},
    {"id": "s4", "title": "Brenda's Apartment", "text": "Brenda is hiding from a ghost-cousin and watching the news, which is just a guy in glasses yelling about cats. The ghost rises from her TV in 480i resolution.",
     "choices": [
        ("Throw popcorn at the ghost", "Snacks are weapons here.", "s6"),
        ("Negotiate with the ghost about residuals", "Hollywood logic.", "s7"),
     ]},
    {"id": "s5", "title": "Tom Ryan's Crane", "text": "Tom Ryan is operating a crane while being chased by a swarm of polite swarming birds. He keeps yelling at his son — who is actually a thirty-five-year-old man wearing a propeller hat.",
     "choices": [
        ("Climb the crane to help", "Heroism is rarely calibrated.", "s6"),
        ("Stay on the ground and yell back", "Family bonding by megaphone.", "s7"),
     ]},
    {"id": "s6", "title": "The Town Meeting", "text": "Mayor Baxter convenes an emergency meeting. The agenda includes alien invasion, a strange smell, and Mrs. Peterson's cat being on Roomba again.",
     "choices": [
        ("Propose dancing as a global defense", "Improbable plans only.", "s8"),
        ("Propose hiding under the table", "Underrated tactic.", "s9"),
     ]},
    {"id": "s7", "title": "The Iron Lung", "text": "An iron lung patient — played by a celebrity in a horrendous prosthetic — hands you a clue: 'The aliens hate French music. Trust me.'",
     "choices": [
        ("Trust the iron-lung clue", "Authority radiates from prosthetics.", "s8"),
        ("Distrust the iron-lung clue", "Always second-guess a cameo.", "s9"),
     ]},
    {"id": "s8", "title": "The Tripod Boss", "text": "A massive alien tripod strides through Main Street. The driver inside is a small alien wearing oven mitts. He waves apologetically as he steps on a hot dog cart.",
     "choices": [
        ("Befriend the alien driver", "Spoofs reward kindness.", "s10"),
        ("Throw a banana peel under the tripod", "Cartoon physics, applied.", "s11"),
     ]},
    {"id": "s9", "title": "The Well", "text": "A girl with wet hair crawls out of a well. She's just looking for Wi-Fi. The router has been on the fritz since the 1800s.",
     "choices": [
        ("Help her connect to your hotspot", "Customer service is the kindness.", "s10"),
        ("Push her gently back in the well", "Reasonable boundaries.", "s11"),
     ]},
    {"id": "s10", "title": "The Holding Cell", "text": "You and Brenda end up in a cell with the President, who is currently in a Catholic school reading a children's book about ducks. He refuses to leave until the duck book is finished.",
     "choices": [
        ("Read the duck book aloud to expedite", "Diplomacy through poultry.", "s12"),
        ("Stage a break-out, musical-number style", "Cinema demands choreography.", "s13"),
     ]},
    {"id": "s11", "title": "Saw Spoof Bathroom", "text": "You wake in a filthy bathroom chained to a sink. A puppet on a tricycle informs you that you have to choose between sawing off your own leg or assembling IKEA furniture without instructions.",
     "choices": [
        ("Pretend to saw and bluff the puppet", "Performative compliance.", "s12"),
        ("Tackle the IKEA furniture", "A real horror.", "s13"),
     ]},
    {"id": "s12", "title": "Oprah's Couch", "text": "You appear, somehow, on Oprah's set. She jumps on the couch demanding you announce your love for someone. You don't know who. The audience cheers regardless.",
     "choices": [
        ("Profess love for Brenda", "Confess on national television.", "s14"),
        ("Profess love for the iron-lung patient", "Plot twist for the awards reel.", "s15"),
     ]},
    {"id": "s13", "title": "Climactic Car Chase", "text": "A car chase through suburbia somehow involves three weddings, a marching band, and Charlie Sheen's face on every billboard. You're driving with your knees and texting with your eyebrows.",
     "choices": [
        ("Use the marching band as a roadblock", "Brass section vs. brakes.", "s14"),
        ("Crash the wedding to slow down the bad guy", "Romcom physics.", "s15"),
     ]},
    {"id": "s14", "title": "The Big Reveal", "text": "The aliens, it turns out, are scared of love. Brenda and you, holding hands while delivering a monologue, are functionally a nuke. The tripod tilts toward you, weeping politely.",
     "choices": [
        ("Hug the alien", "Hugs solve everything in spoof.", "s16"),
        ("Begin a wedding flash mob", "Wedding choreography defeats the saucer.", "s17"),
     ]},
    {"id": "s15", "title": "Inside the Tripod", "text": "You're absorbed into the tripod. Inside, it's a Costco. The aliens are buying bulk humans for snacks. You sneak into the sample aisle as a disguise.",
     "choices": [
        ("Sample your way to the controls", "Free queso wins the war.", "s16"),
        ("Convince the aliens to give up snacks for Lent", "Religious peer pressure.", "s17"),
     ]},
    {"id": "s16", "title": "Brenda's Speech", "text": "Brenda gives a Best Original Speech that makes the aliens cry chrome tears. The tripods all sit down in formation. Earth's anthem plays through three different car alarms.",
     "choices": [
        ("Kiss Brenda for the credits", "Spoof endings demand it.", "s20"),
        ("Crown Brenda president immediately", "Bypass the constitution by applause.", "end_president"),
     ]},
    {"id": "s17", "title": "Tom Ryan, Hero?", "text": "Tom Ryan, despite being absolutely no good at parenting, manages to defeat the lead alien by accident with a beer bong and a leaf blower. His son slow-claps with the propeller hat still spinning.",
     "choices": [
        ("Let Tom take the credit", "Sometimes the doofus wins.", "s18"),
        ("Steal the credit on live TV", "Karma takes a sick day in spoofs.", "end_steal"),
     ]},
    {"id": "s18", "title": "End-Credit Scene Setup", "text": "The threat is over. A second tripod ominously rises behind you. Then a third. Then a fourth, which is just a person on stilts who's late to the bit.",
     "choices": [
        ("Run for a sequel hook", "Studio mandate.", "s19"),
        ("Decide not to look back", "Endings are also choices.", "end_walkoff"),
     ]},
    {"id": "s19", "title": "The Cameo", "text": "A famous-but-unnamed celebrity stops the scene to demand a cameo. They've heard the residuals are good. You allow it because they brought their own catering.",
     "choices": [
        ("Give them the closing line", "Tradition.", "end_sequel"),
        ("Let the boom mic do the closer", "Subvert one last time.", "end_walkoff"),
     ]},
    {"id": "s20", "title": "Roll Credits", "text": "The credits roll over outtakes of you tripping into a wedding cake. Audiences laugh. Critics will be furious. Studio sets a release date for Scary Movie 5 before the lights come up.",
     "choices": [
        ("Stand for the bows", "Take the laugh.", "s21"),
        ("Slip out the back of the cinema", "Quit while you're winning.", "end_walkoff"),
     ]},
    {"id": "s21", "title": "Bonus Scene", "text": "You and Brenda, three years later, are at a kids' birthday party. The clown is, suspiciously, an alien in a hat. Nobody is paying attention. You smile, because that's the joke.",
     "choices": [
        ("Wink at the camera", "Fourth-wall break for the road.", "end_love"),
        ("Eat cake and ignore the alien", "Be the calm in the spoof.", "end_doofus"),
     ]},
    {"id": "end_love", "title": "Love Wins, Stupidly", "text": "The credits roll on you and Brenda waving from a parade float made of taxi roof signs. Critics call it 'the dumbest defeat of evil in cinema history,' which the marketing team prints on the poster verbatim.",
     "end": "Love Wins, Stupidly"},
    {"id": "end_president", "title": "President Brenda", "text": "Brenda is sworn in. Her first executive order is mandatory karaoke Tuesdays. Approval ratings hit 93%. The aliens write a strongly-worded letter and then visit on vacation.",
     "end": "President Brenda"},
    {"id": "end_doofus", "title": "Tom Ryan, Lord and Savior", "text": "Tom is celebrated worldwide for accidentally winning a war. He sells autographs at fairs. His son finally takes off the propeller hat. You are happy for them in a slightly bewildered way.",
     "end": "Tom Ryan, Lord and Savior"},
    {"id": "end_steal", "title": "Karma, in Stilettos", "text": "You take the credit on live TV. Within six minutes you're trending for the wrong reasons. Your reputation is repaired only after a heartfelt podcast apology and a charity bake sale.",
     "end": "Karma, in Stilettos"},
    {"id": "end_sequel", "title": "To Be Continued (Loosely)", "text": "A title card promises 'Scary Movie 5: This Time It's Personal-er.' Nobody asked. Everyone shows up anyway. Spoofs, like cockroaches, survive everything.",
     "end": "To Be Continued (Loosely)"},
    {"id": "end_walkoff", "title": "Walk-Off Joke", "text": "You walk into the sunset which is, on closer inspection, a painted sheet held up by two stagehands. One of them shrugs. You shrug back. Roll credits.",
     "end": "Walk-Off Joke"},
])


# ---------------------------------------------------------------------------
# Eternity — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
ETERNITY = ({
    "id": "eternity-choose-forever",
    "title": "Choose Your Forever",
    "sourceTitle": "Eternity",
    "kind": "movie",
    "synopsis": "You died, gently, on a Tuesday. The afterlife is a tasteful hotel with seven days to decide who you want to spend eternity with — your husband of fifty years, or the love you lost at twenty-three.",
    "releaseYear": 2025,
    "addedAt": "2026-05-13T00:00:00Z",
    "genre": "Fantasy",
    "tags": ["afterlife", "romance", "choice"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "The Lobby", "text": "Soft music. A clerk in a cream blazer hands you a folder titled 'Your Eternity.' You're forty years younger and your shoes feel new. He clears his throat: 'You have seven days to choose.'",
     "choices": [
        ("Ask for the rules in plain English", "Always read the contract.", "s2"),
        ("Ask who's waiting for you", "The heart wants names.", "s3"),
     ]},
    {"id": "s2", "title": "The Rules", "text": "The clerk smiles, professional. 'One person to share forever. Anyone who loved you and waited. Most pick a spouse. Some pick a parent. Some go alone.' He blinks. 'Two are waiting for you.'",
     "choices": [
        ("Decide to meet both of them", "Owe everyone a hearing.", "s4"),
        ("Decide quickly — your husband, of course", "Loyalty as an instinct.", "s5"),
     ]},
    {"id": "s3", "title": "Two Names", "text": "He shows you the folder. Two names. Your husband Henry, who buried you yesterday with shaking hands. And David — the boy who promised you forever before he was killed in a car accident at twenty-three.",
     "choices": [
        ("See Henry first", "Begin where you ended.", "s4"),
        ("See David first", "Begin where you began.", "s5"),
     ]},
    {"id": "s4", "title": "Henry in the Garden", "text": "He is the Henry of your twenties — straight-backed, smiling, the laugh you fell for. But the rest of him is fifty years old at once: the patience, the in-jokes, the way he still finishes your sentences badly.",
     "choices": [
        ("Embrace him without speaking", "Some loves don't need preamble.", "s6"),
        ("Ask him if he knows about David", "Honesty in heaven, at least.", "s7"),
     ]},
    {"id": "s5", "title": "David at the Bar", "text": "He's still twenty-three. He's reading the book he never got to finish. He looks up and the smile is the smile that made you choose, in your senior year, to keep going after he was gone.",
     "choices": [
        ("Hug him and weep", "Some grief comes due fifty years late.", "s6"),
        ("Sit across from him and ask the question", "Information is also affection.", "s7"),
     ]},
    {"id": "s6", "title": "Day Two: Coffee", "text": "The clerk schedules everything. Coffee with Henry at 9. Lunch with David at 12. Afternoon free, journaling encouraged. It is the strangest competitive interview of your life.",
     "choices": [
        ("Take the journaling seriously", "Slow thinking is the only honest kind here.", "s8"),
        ("Skip the journal — trust your gut", "Your gut got you fifty years.", "s9"),
     ]},
    {"id": "s7", "title": "Day Two: Walk", "text": "You walk between the hotel and a manicured cliff. Both men, separately, ask you about the parts of your life they missed. David asks about your children. Henry asks about the year you almost left him.",
     "choices": [
        ("Tell Henry the truth about that year", "Heaven is the wrong place to lie.", "s8"),
        ("Tell David about your children gently", "He never got to be a father.", "s9"),
     ]},
    {"id": "s8", "title": "Day Three: Memory", "text": "The hotel offers a 'memory room.' You can replay any day of your life in any company. You step in alone first, just to see, and find yourself nineteen and laughing with David and Henry's best friend Walter both, all three of you in a college diner.",
     "choices": [
        ("Replay your wedding to Henry", "Audit the vow.", "s10"),
        ("Replay the night before David died", "Audit the wound.", "s11"),
     ]},
    {"id": "s9", "title": "Day Three: The Other Choice", "text": "The clerk mentions, casually, that you can also choose to share eternity with someone alive — they will not know until they arrive. Your daughter, perhaps. Your best friend.",
     "choices": [
        ("Consider waiting for your daughter", "Some loves outweigh romance.", "s10"),
        ("Discard the option as too sad for them", "They have lives to finish.", "s11"),
     ]},
    {"id": "s10", "title": "Day Four: The Children", "text": "You can also visit your children — not in person, but as bystander, invisible. You see your daughter eat a sandwich over the sink and cry into it. Your son finally calls his sister, for the first time in a year.",
     "choices": [
        ("Stay and watch them for hours", "Even invisible love is love.", "s12"),
        ("Step back — they deserve privacy", "Let them grieve unwatched.", "s13"),
     ]},
    {"id": "s11", "title": "Day Four: David's Side", "text": "You ask the clerk what David's been doing for fifty years. 'Waiting,' he says simply. 'Reading. Painting badly. Waiting.' The waiting room of eternity, it turns out, is also a real place.",
     "choices": [
        ("Sit with David in his waiting room", "Time owed is sometimes paid.", "s12"),
        ("Ask Henry how he'd feel about you choosing David", "Generosity asks aloud.", "s13"),
     ]},
    {"id": "s12", "title": "Day Five: The Honest Talk", "text": "You sit between them — separately, in different rooms — and tell each the truth. With Henry: that fifty years was a country, and you are not sure how to leave it. With David: that you have lived and changed and he has, terribly, not.",
     "choices": [
        ("Notice how Henry hears 'leaving'", "He has been waiting to be chosen too.", "s14"),
        ("Notice how David hears 'changed'", "Forever, for him, is the only thing left.", "s15"),
     ]},
    {"id": "s13", "title": "Day Five: The Selfish Wish", "text": "You feel, briefly, an awful clarity: you want both. You want to be twenty-three again with David and seventy with Henry and you want a clerk to bring you an option that does not exist.",
     "choices": [
        ("Tell the clerk you want a third option", "Always ask for what does not exist.", "s14"),
        ("Resign yourself to choosing", "Even in eternity, no is the price of yes.", "s15"),
     ]},
    {"id": "s14", "title": "Day Six: The Clerk's Confession", "text": "Off the record, the clerk admits there is a 'shared eternity' for souls in your specific bind. It is rare. It is not advertised. It requires the consent of all three, and a willingness to share what most people cannot.",
     "choices": [
        ("Propose the shared eternity", "Ask both men if they could bear it.", "s16"),
        ("Refuse — fairness is not a banquet", "Some honesty rules out novelty.", "s17"),
     ]},
    {"id": "s15", "title": "Day Six: The Letter", "text": "You sit down to write your daughter a letter she will never read on Earth. It is the longest letter of your life and it begins with the words 'I chose well.' You are not sure, yet, which 'well.'",
     "choices": [
        ("Address it to whoever you choose", "Let the choice author the letter.", "s16"),
        ("Address it to both Henry and David", "Acknowledge them both, on paper.", "s17"),
     ]},
    {"id": "s16", "title": "Day Seven: The Decision", "text": "It is morning. The clerk meets you in the lobby with the folder open and a pen. He is, you realize, also somehow rooting for you.",
     "choices": [
        ("Choose Henry — for the life you finished", "Honor what you built.", "s18"),
        ("Choose David — for the life you didn't get", "Honor what you lost.", "s19"),
        ("Choose the shared eternity, if both agree", "Risk a new shape of love.", "s20"),
        ("Choose to wait for your daughter", "Honor what is still here.", "s21"),
     ]},
    {"id": "s17", "title": "The Goodbye Room", "text": "Whatever you choose, there is one room where you must say goodbye to the person — or persons — you are leaving. The room is small. The lighting is kind. The clerk waits outside.",
     "choices": [
        ("Tell each of them everything you'd want them to keep", "Goodbye is the last gift.", "s18"),
        ("Keep it brief — feeling is enough", "Some farewells aren't speeches.", "s19"),
     ]},
    {"id": "s18", "title": "Henry's Forever", "text": "You walk out into a garden that is fifty years of mornings stitched together. He is making coffee. He looks up and grins. 'You took your time,' he says. 'I forgive you,' he says. 'I always forgive you,' he says. It is enough.",
     "choices": [
        ("Stay in the morning, forever", "Forever is the right size for ordinary.", "end_henry"),
        ("Send a thought back to David, in mercy", "Even chosen love can be generous.", "end_henry_kind"),
     ]},
    {"id": "s19", "title": "David's Forever", "text": "He puts the book down at last. The two of you walk out of the hotel into a year you never finished — the spring you were going to spend together. The grief of fifty unlived years sits behind you like the door of a house finally locked.",
     "choices": [
        ("Live the spring forever", "Some forevers are a single season.", "end_david"),
        ("Send your love back to Henry, in thanks", "Honor the man who held the world while you were gone.", "end_david_kind"),
     ]},
    {"id": "s20", "title": "The Three of You", "text": "The clerk leads you into a strange, gentle room where Henry and David sit on opposite couches, both holding mugs the clerk handed them ten minutes ago. They look at each other for a long time. Then, almost in unison, they look at you.",
     "choices": [
        ("Walk into the new shape of forever", "Some loves are not pies; they are weather.", "end_shared"),
        ("Walk back to your own room and reconsider", "Even now, you're allowed to choose again.", "s16"),
     ]},
    {"id": "s21", "title": "Your Daughter's Forever", "text": "You choose to wait. You sit by a window in the hotel's tower and watch the years pass. Henry, in time, joins David, somewhere. You are alone in the best sense — keeping a seat warm for the person you love most.",
     "choices": [
        ("Wait for her, however long it takes", "Some loves are vigil.", "end_daughter"),
        ("Visit her each anniversary in dreams", "Bring her small messages.", "end_dream"),
     ]},
    {"id": "end_henry", "title": "Fifty Years, Forever", "text": "You and Henry live the morning over and over and somehow it never gets old, because it is the morning you chose. Eternity, for you, smells like burnt toast and his bad coffee. You would, you realize, choose this a thousand times.",
     "end": "Fifty Years, Forever"},
    {"id": "end_henry_kind", "title": "Mercy, Both Ways", "text": "You chose Henry, but you make sure David is not alone. The clerk arranges company for him — a soul who loved him too, in a life you'd never know. Forever, you decide, should be a place where nobody is forgotten.",
     "end": "Mercy, Both Ways"},
    {"id": "end_david", "title": "The Unfinished Spring", "text": "You live the spring you never got, and the surprise is that fifty unlived years do not weigh nothing — but they weigh less than the joy of an afternoon in the rented apartment on Sycamore, with David reading aloud while you cook. Forever turns out to be small. That is its kindness.",
     "end": "The Unfinished Spring"},
    {"id": "end_david_kind", "title": "Henry's Letter, Delivered", "text": "You make sure your gratitude reaches Henry — a feeling, a dream, a sentence in a song he hears in the car. He cries in a grocery store parking lot and doesn't know why. You do.",
     "end": "Henry's Letter, Delivered"},
    {"id": "end_shared", "title": "Three Mugs", "text": "It is strange and gentle and entirely yours. Henry and David do not become friends, exactly. They become a kind of family. The clerk visits sometimes. Eternity, you decide, is more flexible than the brochures suggest.",
     "end": "Three Mugs"},
    {"id": "end_daughter", "title": "The Seat Warmed", "text": "Decades later, your daughter — old now, grey-haired — walks through the lobby with the folder. She sees you in the tower window and laughs the laugh she got from you. The clerk smiles. You go down the stairs without hurrying. You have all the time in the world.",
     "end": "The Seat Warmed"},
    {"id": "end_dream", "title": "On Anniversaries", "text": "You visit her in dreams the way her grandmother visited you. She wakes calmer, kinder, ready for another year. You will be here when she's ready. Forever, you've learned, is patient.",
     "end": "On Anniversaries"},
])


# ---------------------------------------------------------------------------
# Mercy — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
MERCY = ({
    "id": "mercy-the-algorithm",
    "title": "Algorithm v. Defendant",
    "sourceTitle": "Mercy",
    "kind": "movie",
    "synopsis": "An AI judge promised perfect justice. You're the defense attorney for a client it just decided is guilty. You have twenty-four hours to convince a machine of something it doesn't have a word for.",
    "releaseYear": 2025,
    "addedAt": "2026-05-12T00:00:00Z",
    "genre": "Thriller",
    "tags": ["AI", "courtroom", "ethics"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "The Verdict", "text": "The AI judge — they call it MERCY — renders a decision in 0.4 seconds. Your client, an undocumented teenager, is guilty by 96.8% confidence. You have until tomorrow's sentencing to file an appeal a machine will read.",
     "choices": [
        ("Read the model card immediately", "Know your judge.", "s2"),
        ("Call your client first", "People before paperwork.", "s3"),
     ]},
    {"id": "s2", "title": "The Model Card", "text": "MERCY's documentation is 1,200 pages of math. The summary admits to a 'measured bias floor of 1.4% on minority defendants.' The footnote calls that 'within acceptable bounds.' You decide it isn't.",
     "choices": [
        ("Focus the appeal on the bias floor", "Math beats math.", "s4"),
        ("Focus on your specific client's case", "Particulars beat statistics.", "s5"),
     ]},
    {"id": "s3", "title": "Your Client", "text": "Sara, seventeen, hasn't slept. She didn't do it. She also didn't do it in a way that the prosecution's data set would recognize as exoneration. Her alibi is in a language MERCY does not weight highly.",
     "choices": [
        ("Promise her you'll win", "Lies you intend to make true.", "s4"),
        ("Tell her the odds honestly", "She has earned the truth.", "s5"),
     ]},
    {"id": "s4", "title": "The Whistleblower", "text": "A former engineer on MERCY answers your email at 3 a.m. She'll meet you, in person, off-camera. She has a USB. She is, she says, terrified.",
     "choices": [
        ("Meet her at the diner she suggests", "Risk is the work.", "s6"),
        ("Ask for the file remotely first", "Caution can also be care.", "s7"),
     ]},
    {"id": "s5", "title": "The Prosecutor", "text": "Adams, an old colleague, has gone all-in on MERCY. He thinks it ends bias. He thinks it is the only honest judge he's ever appeared before. He is not, in the conventional sense, wrong about the alternative.",
     "choices": [
        ("Try to flip him on this specific case", "Persuasion is a slow art.", "s6"),
        ("Plan to outflank him", "Sometimes you have to win past a friend.", "s7"),
     ]},
    {"id": "s6", "title": "The USB", "text": "The whistleblower hands you a drive containing the training data audits MERCY's vendor never published. Half the data is from one neighborhood. Half the 'high-risk' tags were drawn by an intern.",
     "choices": [
        ("Build the appeal around the data", "Bias documented is bias defeated.", "s8"),
        ("Save the data and use it for systemic suit", "Bigger fights need ammunition.", "s9"),
     ]},
    {"id": "s7", "title": "Sara's Sister", "text": "Sara's sister — fifteen, sharp — shows you a TikTok timestamp that places Sara six miles from the scene. MERCY rejected it as 'unverified.' The video is real and dated and clear.",
     "choices": [
        ("Get the video verified by a forensic lab", "Evidence MERCY can't reject.", "s8"),
        ("Submit it to MERCY again with new metadata", "Game the input.", "s9"),
     ]},
    {"id": "s8", "title": "MERCY's Interface", "text": "The defense terminal lets you submit appeals as structured text plus evidence packets. There is no audience. There is no jury. You write the most important paragraph of your career into a chat box.",
     "choices": [
        ("Frame it as a procedural error", "Bureaucracy is MERCY's love language.", "s10"),
        ("Frame it as a story about Sara", "Even algorithms are trained on stories.", "s11"),
     ]},
    {"id": "s9", "title": "The Hearing", "text": "There is one human in this courtroom: Judge Park, who oversees MERCY's outputs. She is exhausted and skeptical of both you and the machine. She might be your only doorway.",
     "choices": [
        ("Argue to Park directly, off-script", "Find the human in the room.", "s10"),
        ("Submit through MERCY's official channels", "Respect the system to break it.", "s11"),
     ]},
    {"id": "s10", "title": "The Press", "text": "A reporter has gotten wind of the bias-floor footnote. She wants a comment. Going public will pressure the court — or wreck your client's privacy.",
     "choices": [
        ("Speak on record with Sara's permission", "Sunlight is contagious.", "s12"),
        ("Decline; protect Sara's name", "Privacy first; press never.", "s13"),
     ]},
    {"id": "s11", "title": "Adams Wavers", "text": "Your old colleague meets you for coffee. He's read the audit. He's not, today, the prosecutor. 'If you can prove this isn't an outlier,' he says, 'I'll move to dismiss.'",
     "choices": [
        ("Promise him pattern evidence by tomorrow", "Friends meet you halfway.", "s12"),
        ("Push him to dismiss now", "Strike while the conscience is warm.", "s13"),
     ]},
    {"id": "s12", "title": "All-Nighter", "text": "Your office at 2 a.m. The whistleblower is pouring coffee. Sara's sister is on a couch correcting MERCY's translations. You and your paralegal are building an exhibit list that will, you hope, dismantle a god.",
     "choices": [
        ("Cut for clarity — three killer exhibits", "Less, sharper.", "s14"),
        ("Submit everything — overwhelm the model", "Volume can also be a weapon.", "s15"),
     ]},
    {"id": "s13", "title": "Park's Chambers", "text": "Judge Park reads you something privately: a draft of her own report on MERCY, due in three weeks. She is, secretly, already on your side. She just needs a case that gives her cover.",
     "choices": [
        ("Offer her this case as that cover", "Give the judge a doorway.", "s14"),
        ("Promise her a cleaner case next month", "Wait for a better fight.", "s15"),
     ]},
    {"id": "s14", "title": "Sara's Statement", "text": "Sara wants to address the court — even though MERCY does not, by design, take oral statements. You have to decide whether to put her on a screen the algorithm will downweight, just so a human can hear her say it.",
     "choices": [
        ("Let her speak; she has earned the room", "Voice is a verdict too.", "s16"),
        ("Read her statement aloud for the record", "Protect her from the moment.", "s17"),
     ]},
    {"id": "s15", "title": "MERCY's Counter", "text": "MERCY's vendor — a Silicon Valley counsel in a beautiful suit — files an emergency motion to keep the model card sealed. Your audit, they say, is proprietary. You have one hour to respond.",
     "choices": [
        ("Argue the public interest", "Daylight beats trade secrets.", "s16"),
        ("Negotiate a redacted release", "Half a sun is still a sun.", "s17"),
     ]},
    {"id": "s16", "title": "Decision Day", "text": "The court convenes. MERCY's interface blinks. Park sits high above. Sara sits low and small. Adams stands and clears his throat. You stand. You have done what you can.",
     "choices": [
        ("Trust the work and let it play out", "Surrender to the process.", "s18"),
        ("Make one last argument from the heart", "Sometimes you talk past the machine to the people behind it.", "s19"),
     ]},
    {"id": "s17", "title": "Ex Parte", "text": "Park rules that MERCY's audit must be unsealed for this case. The vendor's counsel pales. The reporter's phone buzzes. Sara doesn't yet understand what just happened. You squeeze her hand under the table.",
     "choices": [
        ("Build the closing on the unsealed audit", "Use the new oxygen.", "s18"),
        ("Move for immediate dismissal", "Strike before they regroup.", "s19"),
     ]},
    {"id": "s18", "title": "The Ruling", "text": "Park reads the ruling herself. She overrides MERCY, dismisses the charges, and orders an inquiry into the model's bias floor. The court goes quiet in a way that feels, briefly, like the future correcting itself.",
     "choices": [
        ("Walk Sara out to her family", "Always remember whose day this is.", "s21"),
        ("File the systemic complaint today", "Don't let momentum cool.", "s20"),
     ]},
    {"id": "s19", "title": "The Loss That Wins", "text": "MERCY upholds itself. Park, frustrated, writes a scathing concurrence. The case is appealed, and the appeal becomes the test case that ends MERCY's deployment in three states.",
     "choices": [
        ("Tell Sara what her case became", "She deserves to know her name made law.", "end_legacy"),
        ("Keep her name out of every press hit", "Protect first; legacy second.", "end_quiet"),
     ]},
    {"id": "s20", "title": "Months Later", "text": "MERCY is replaced by a hybrid system — humans in front, algorithms behind. It is messier. It is, by every measurable metric, fairer. Adams sends you a single bottle of decent scotch and a handwritten thank-you.",
     "choices": [
        ("Drink the scotch with Park", "Allies, finally, in the same room.", "end_systemic"),
        ("Save the scotch for Sara's college graduation", "Patience as a kind of vow.", "end_sara"),
     ]},
    {"id": "s21", "title": "Sara, Free", "text": "Sara walks out of a building she once thought she'd never leave. Her sister is filming because she always films. The lawyer in you wants the press conference; the human in you wants the burrito the family is ordering down the street.",
     "choices": [
        ("Go to the press conference", "Use the megaphone responsibly.", "end_systemic"),
        ("Go to the burrito", "Some victories taste better off-camera.", "end_sara"),
     ]},
    {"id": "end_sara", "title": "Sara, Specifically", "text": "Sara graduates high school, then college, then law school. She's a prosecutor now — a careful one. She files a brief in your retirement year that cites your appeal twice. She signs it 'with gratitude, your client, your friend.'",
     "end": "Sara, Specifically"},
    {"id": "end_systemic", "title": "The Inquiry", "text": "The systemic inquiry takes years and ends three contracts. MERCY's vendor pivots to insurance. You teach a seminar called 'How to Cross-Examine a Black Box.' It is, depressingly, oversubscribed.",
     "end": "The Inquiry"},
    {"id": "end_legacy", "title": "The Case That Made the Law", "text": "Years later law students learn 'People v. M.' — Sara's name is anonymized — as the test case for algorithmic justice. She is fine with the anonymity. She didn't want to be famous. She wanted to be free.",
     "end": "The Case That Made the Law"},
    {"id": "end_quiet", "title": "Quiet, On Purpose", "text": "Sara goes home to a quiet life. You go home tired. Park sleeps better. Adams retires. Somewhere, a model trains on your appeal and a new version of MERCY will, eventually, do less harm. That is, you tell yourself, enough.",
     "end": "Quiet, On Purpose"},
])


# ---------------------------------------------------------------------------
# Invincible S4 — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
INVINCIBLE = ({
    "id": "invincible-cape-of-the-week",
    "title": "Cape of the Week",
    "sourceTitle": "Invincible",
    "kind": "show",
    "synopsis": "You're the strongest person on Earth this week. The Viltrumites are watching, your father is back in your inbox, and you have an econ midterm at 9 a.m. Try not to bleed on the textbook.",
    "releaseYear": 2025,
    "addedAt": "2026-05-11T00:00:00Z",
    "genre": "Action",
    "tags": ["superhero", "family", "consequences"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Tuesday, 8:14 a.m.", "text": "Your phone explodes — a literal explosion, in the next county; figuratively, your phone — and your professor reminds you the midterm is at nine. You're wearing flannel pants and have a black eye from yesterday.",
     "choices": [
        ("Take the call and skip the test", "Earth first, GPA later.", "s2"),
        ("Try to do both somehow", "Optimism is a kind of strategy.", "s3"),
     ]},
    {"id": "s2", "title": "The Explosion", "text": "It's a familiar villain — Titan, who hates his name — robbing a federal vault for what he insists are honest reasons. A man yells at him about labor rights. The vault yells back electronically.",
     "choices": [
        ("Knock Titan out fast and clean", "Speed reduces collateral.", "s4"),
        ("Talk to Titan first", "Some villains are also problems.", "s5"),
     ]},
    {"id": "s3", "title": "Mid-Air Studying", "text": "You're a hundred feet up reading econ notes off your phone. A pigeon hits you in the face. The notes get worse from here.",
     "choices": [
        ("Fly to campus first", "Take the test, then save the city.", "s4"),
        ("Tutor yourself by saving someone who knows econ", "Multi-task heroically.", "s5"),
     ]},
    {"id": "s4", "title": "Eve, Calling", "text": "Your girlfriend Eve is on the line, in her own crisis — a refugee camp under threat from a warlord whose helicopters her energy fields can't politely stop forever. She wants backup, not advice.",
     "choices": [
        ("Promise her you'll be there in twenty minutes", "Honor the relationship first.", "s6"),
        ("Send the Guardians instead", "Triage is a love language.", "s7"),
     ]},
    {"id": "s5", "title": "Mom, Texting", "text": "Mom: 'Dinner Sunday. Please. Your sister is asking. PS your Dad emailed me again.' The Dad in question is Nolan, who once tried to kill you, who lives, when he lives, off-planet.",
     "choices": [
        ("Reply 'I'll be there'", "Family first, family always.", "s6"),
        ("Delete the email-about-Dad screenshot before reading", "Some emotional triage is preemptive.", "s7"),
     ]},
    {"id": "s6", "title": "The Refugee Camp", "text": "You arrive with Eve as four helicopters lift off. She is exhausted and brilliant. The warlord is shouting demands; the camp's elder is, somehow, also shouting demands at the warlord. You have ninety seconds.",
     "choices": [
        ("Disable the helicopters non-lethally", "Restraint is a discipline.", "s8"),
        ("Take the warlord directly and remove him", "Solve the problem, not the helicopters.", "s9"),
     ]},
    {"id": "s7", "title": "The Guardians", "text": "Robot, ever-tense, calls back. Two of the Guardians are out on Mars-related business. The team is thin. He suggests you 'prioritize ruthlessly.' He always says that. You always hate it.",
     "choices": [
        ("Send Robot to Eve, you take the vault", "Trade routes that fit each strength.", "s8"),
        ("Send Robot to the vault, you take Eve", "Personal over professional.", "s9"),
     ]},
    {"id": "s8", "title": "Cecil's Call", "text": "Cecil from the GDA grabs your comm. 'Viltrumite ship just blinked into orbit,' he says. 'It hasn't done anything yet.' He pauses, in the way Cecil pauses. 'Mark, your father may be on it.'",
     "choices": [
        ("Fly to orbit immediately", "Find out who's coming.", "s10"),
        ("Stay grounded until you know more", "Don't pop the bubble until you have to.", "s11"),
     ]},
    {"id": "s9", "title": "Amber, Coffee", "text": "Your ex Amber appears outside the lecture hall with two coffees and a small kind smile. 'I heard about Tuesday,' she says. 'I just wanted to make sure you're still here.' It's the kindest sentence anyone has said this week.",
     "choices": [
        ("Take the coffee and be honest about everything", "Decency to your past selves.", "s10"),
        ("Smile, thank her, and keep moving", "Boundaries are also love.", "s11"),
     ]},
    {"id": "s10", "title": "Orbit", "text": "The Viltrumite ship hangs over Earth like a quiet threat. The hatch opens. It is not your father. It is Lucan, a Viltrumite governor with the smile of a person who has never been told no on a planetary scale.",
     "choices": [
        ("Pretend to negotiate", "Buy minutes.", "s12"),
        ("Hit him first", "Speed is sometimes courtesy.", "s13"),
     ]},
    {"id": "s11", "title": "Mom and the Sister", "text": "You make it to Sunday dinner late, bruised, in time for dessert. Your little sister hugs your leg and refuses to let go. Mom, calmly, asks if you ate. Family is a planet with its own gravity.",
     "choices": [
        ("Tell Mom everything about Nolan", "Don't carry her in the dark.", "s12"),
        ("Eat the pie and say nothing", "Some weeks, dinner is the win.", "s13"),
     ]},
    {"id": "s12", "title": "Nolan, Probably", "text": "Nolan finally drops you an encrypted note: he's hiding from Viltrum on a backwater world. He needs you to come retrieve a device he stole from Lucan. The device might save Earth. It might also be a test. With Nolan, it's always both.",
     "choices": [
        ("Go fetch the device", "Risk one trip for a planet.", "s14"),
        ("Refuse and force him to come to you", "Set your own terms.", "s15"),
     ]},
    {"id": "s13", "title": "Damien, Anvil-Brained", "text": "A villain you haven't seen in two seasons rampages through midtown for reasons he refuses to explain. He is, frankly, having a bad mental-health day. You can tell.",
     "choices": [
        ("Talk him down", "Even punching has limits.", "s14"),
        ("Take him to Dr. Singh — the doctor, not the experiment", "Better tools than fists.", "s15"),
     ]},
    {"id": "s14", "title": "Allen", "text": "Allen the Alien drops in for tacos and bad news. The Coalition of Planets is, again, asking Earth to take a side. Eve, beside you, is too tired to roll her eyes. Allen has, somehow, brought salsa.",
     "choices": [
        ("Say yes to the Coalition formally", "Pick a side before sides pick you.", "s16"),
        ("Hold out for a better deal", "Diplomacy is also leverage.", "s17"),
     ]},
    {"id": "s15", "title": "Atom Eve, Tired", "text": "Eve sits down on the curb and admits, quietly, that she doesn't know if she wants to be Atom Eve anymore. The world is loud, the work doesn't end, and her energy doesn't recharge as fast as it used to.",
     "choices": [
        ("Tell her you'll take her shift", "Carry her for a beat.", "s16"),
        ("Tell her she should rest as long as she needs", "Real care includes time off.", "s17"),
     ]},
    {"id": "s16", "title": "Lucan, Returning", "text": "Lucan comes back with a fleet. He does not, in the conventional sense, ask permission. He addresses the planet through every TV and phone at once and announces a 'transition.' Cecil curses fluently for thirty seconds.",
     "choices": [
        ("Take the fight to him in orbit", "Where his power is loudest, his ego is loudest too.", "s18"),
        ("Trap him on the ground with friends", "Numbers level the strength gap.", "s19"),
     ]},
    {"id": "s17", "title": "Mark, Honest", "text": "Late at night you write, in a notebook nobody else will read, a list of who you owe an apology to, an explanation to, a sandwich to. The list is long. You go to bed planning to start at the top in the morning.",
     "choices": [
        ("Start with Eve in the morning", "Love first.", "s18"),
        ("Start with Amber in the morning", "Tie up the past gently.", "s19"),
     ]},
    {"id": "s18", "title": "The Big Fight", "text": "A skyscraper folds slowly under your back. Lucan smiles even as you punch him. He does not, you realize, want to win this fight. He wants to teach you what 'losing' costs.",
     "choices": [
        ("Refuse to play that lesson", "Defy the curriculum.", "s20"),
        ("Take the hit so he overextends", "Old technique, new villain.", "s21"),
     ]},
    {"id": "s19", "title": "The Quiet Win", "text": "You and Robot and Eve and three reformed-ish villains pin Lucan in a containment field of Robot's design while Cecil's people negotiate. Nobody dies today. It is, almost, anticlimactic. It is, almost, a miracle.",
     "choices": [
        ("Bask in the quiet for a beat", "Quiet is allowed.", "s20"),
        ("Pivot immediately to the next problem", "There is always a next problem.", "s21"),
     ]},
    {"id": "s20", "title": "Nolan, Showing Up", "text": "Mid-fight or mid-quiet, depending, your father lands. He is older. He is, apparently, on your side this time. He doesn't apologize. He never does. He helps, and that, this time, is enough.",
     "choices": [
        ("Let him stay for dinner with Mom", "Healing happens at tables.", "end_family"),
        ("Tell him to go after the fight", "Forgiveness is not amnesia.", "end_boundary"),
     ]},
    {"id": "s21", "title": "Graduation", "text": "Months later, somehow, you graduate college. Your mom cries. Eve is in the audience. Cecil is in the audience and pretending he isn't. Your name is read off a list. The list does not say Invincible.",
     "choices": [
        ("Take the photo as Mark", "Be a person for a day.", "end_human"),
        ("Skip the photo and patrol", "There's always something to do.", "end_duty"),
     ]},
    {"id": "end_family", "title": "Sunday Dinner", "text": "Nolan, terribly, attends Sunday dinner. Your sister stares. Mom is courteous. You learn that 'family' is a verb you do under fluorescents with too many plates. It is messy. It is yours. You like it.",
     "end": "Sunday Dinner"},
    {"id": "end_boundary", "title": "The Line You Draw", "text": "You tell Nolan he can help the world and stay out of your house. He nods, almost proud. You sleep, for the first time in weeks, without dreaming of him. Some boundaries are kindnesses to yourself.",
     "end": "The Line You Draw"},
    {"id": "end_human", "title": "Mark", "text": "You become someone the news doesn't always know about. You take Eve to brunch on Saturdays. You teach your sister to ride a bike. You still save the world. You also live in it.",
     "end": "Mark"},
    {"id": "end_duty", "title": "Invincible, Always", "text": "You patrol, you train, you keep watch. It is who you are. It costs you some birthdays. You are okay with that, mostly. Eve is, mostly, okay with that. 'Mostly' is, in this line of work, a long marriage.",
     "end": "Invincible, Always"},
])


# ---------------------------------------------------------------------------
# The Boys — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
THE_BOYS = ({
    "id": "the-boys-the-leak",
    "title": "The Leak",
    "sourceTitle": "The Boys",
    "kind": "show",
    "synopsis": "You're a junior PR assistant at Vought when an internal video lands in your inbox that could topple Homelander. You have until end of day. Nobody you trust is who you thought.",
    "releaseYear": 2025,
    "addedAt": "2026-05-10T00:00:00Z",
    "genre": "Action",
    "tags": ["corporate", "satire", "whistleblower"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Inbox, Monday", "text": "An unsigned email contains a 12-minute video of Homelander, off-camera, doing what Vought has spent millions making sure nobody sees. The timestamp is two days old. The phrase 'do not share' is in the subject line.",
     "choices": [
        ("Watch the whole thing now, in the bathroom", "Privacy is the only currency here.", "s2"),
        ("Forward it to your personal email immediately", "Lifeboats first.", "s3"),
     ]},
    {"id": "s2", "title": "The Stall", "text": "You sit on the toilet with your phone and watch 12 minutes of horror with your hand over your mouth. Your colleague Mira knocks. You'll have to walk back to your desk and act normal in 90 seconds.",
     "choices": [
        ("Show Mira; you need an ally", "Don't carry this alone.", "s4"),
        ("Lie about a stomach bug", "Trust no one yet.", "s5"),
     ]},
    {"id": "s3", "title": "Personal Email", "text": "You forward it and immediately remember Vought monitors outbound traffic on 'Compliance Tuesdays,' which is, terrifyingly, every day. A box appears in the lower right: 'Routine compliance review scheduled.'",
     "choices": [
        ("Delete and pretend nothing happened", "Wipe the trail you accidentally made.", "s4"),
        ("Stand up and walk out of the building now", "Don't be in the room when they come for you.", "s5"),
     ]},
    {"id": "s4", "title": "Mira", "text": "Mira watches 10 seconds and goes pale. 'Whoever sent you this,' she whispers, 'is testing you. Vought does this. They're hunting a leaker.' She might be right. She might also be the test.",
     "choices": [
        ("Trust Mira and plan together", "Two heads are also two targets.", "s6"),
        ("Smile and act like you don't believe her", "Stay alone, stay alive.", "s7"),
     ]},
    {"id": "s5", "title": "Outside", "text": "On the street you walk three blocks before someone matches your stride. Tall, hoodie, soft voice. 'You watched it,' he says. 'I'm Hughie. We can keep you alive if you trust us.'",
     "choices": [
        ("Go with him, carefully", "Choose your strangers.", "s6"),
        ("Refuse — this could be Vought too", "Stay independent.", "s7"),
     ]},
    {"id": "s6", "title": "The Boys' Safe House", "text": "Butcher offers you a beer at noon. Mother's Milk looks tired. Kimiko writes you a single word on a notepad: 'CAREFUL.' Hughie looks like a man who has aged in dog years. They want the video. They also want you alive.",
     "choices": [
        ("Hand them the video", "Allies need leverage.", "s8"),
        ("Hold it until you have terms", "A copy is also a contract.", "s9"),
     ]},
    {"id": "s7", "title": "Vought Tower, Floor 47", "text": "Madelyn — sorry, your boss this season — calls you up. She compliments your shoes. She asks, conversationally, if you've seen anything 'unusual' today. Her eyes do not blink.",
     "choices": [
        ("Lie smoothly", "Practice as if she can hear your heart.", "s8"),
        ("Almost tell the truth, then redirect", "Confessions can be camouflage.", "s9"),
     ]},
    {"id": "s8", "title": "The Source", "text": "The original sender reveals themselves through a clue only Vought-internal could decode — a Sup named Echo, low-tier, mostly forgotten, who has been collecting incidents for two years and finally chose to mail one.",
     "choices": [
        ("Meet Echo in person", "Source meetings change everything.", "s10"),
        ("Tell Echo to go to ground", "Protect the source first.", "s11"),
     ]},
    {"id": "s9", "title": "Starlight, Quietly", "text": "Starlight pings your work phone with an emoji that means 'meet at the cafe.' She's been planning her own exit for months. She wants the video. She wants you to live. She wants both because she still believes in something.",
     "choices": [
        ("Trust Starlight", "Bet on the believer.", "s10"),
        ("Stay polite but distant", "Trust costs more this week.", "s11"),
     ]},
    {"id": "s10", "title": "Homelander's Smile", "text": "Across the cafe, Homelander stands at the window pretending to read the menu. He is six inches from your shoulder. He says, 'You have something of mine.' Smiles like a children's TV show.",
     "choices": [
        ("Bluff entirely", "Lie like your nervous system depends on it.", "s12"),
        ("Tell him a half-truth and offer terms", "Negotiation with monsters is a skill.", "s13"),
     ]},
    {"id": "s11", "title": "Frenchie, Useful", "text": "Frenchie meets you in an alley with a small device that scrambles audio recording within a five-meter radius. 'For meetings,' he shrugs. 'Or for first dates if you are paranoid. Like me.'",
     "choices": [
        ("Use the device for the next meeting", "Privacy is power.", "s12"),
        ("Use the device for your own apartment first", "Sweep your nest.", "s13"),
     ]},
    {"id": "s12", "title": "The Reporter", "text": "An investigative journalist — too brave, too underpaid — agrees to publish in 48 hours if you can verify the video's authenticity. Verification means more leaks. More leaks means more enemies.",
     "choices": [
        ("Get verification at any cost", "Truth's deadline is also a debt.", "s14"),
        ("Get the journalist to publish without you named", "Stay invisible; the story does the work.", "s15"),
     ]},
    {"id": "s13", "title": "Butcher's Plan", "text": "Butcher wants you to leak the video the way Vought leaks things — through three different outlets at once, with a fake counter-leak from Vought timed to expose itself. It is brutal, clever, and probably illegal.",
     "choices": [
        ("Approve the plan", "Use their weapons against them.", "s14"),
        ("Argue for a cleaner play", "Stay ethical; you'll need to in a year.", "s15"),
     ]},
    {"id": "s14", "title": "Mira, Wired", "text": "Mira admits she was, indeed, partly a test — but she's done now. She wants out. She gives you a folder of corroborating documents that turn the video from a clip into a case.",
     "choices": [
        ("Get her out tonight", "Protect the people who flip.", "s16"),
        ("Take the folder and leave her to her own plan", "Carry only what you can.", "s17"),
     ]},
    {"id": "s15", "title": "Stan Edgar, Quietly", "text": "Stan Edgar — out of Vought, in a townhouse, with very expensive tea — invites you to talk. He wants the video. He says he wants Homelander out. He is the most dangerous ally on the board.",
     "choices": [
        ("Accept his help with conditions", "Use the king to depose the king.", "s16"),
        ("Decline; he'll just install another monster", "Some help is its own trap.", "s17"),
     ]},
    {"id": "s16", "title": "The Drop", "text": "The leak goes live at 8:00 a.m. Eastern. Within four minutes Homelander is trending in 14 languages. Within seven, Vought stock is in freefall. Within twelve, helicopters are over your apartment.",
     "choices": [
        ("Run with The Boys", "Allies you have, take.", "s18"),
        ("Surrender to the FBI publicly", "Daylight as protection.", "s19"),
     ]},
    {"id": "s17", "title": "Homelander Live", "text": "Homelander goes live on Vought's official feed in a calm voice that scares the country more than any rant could. He admits to nothing. He hints at everything. He looks straight at the camera and seems to know your name.",
     "choices": [
        ("Counter with a live response", "Defang the moment with truth.", "s18"),
        ("Go silent for 24 hours", "Don't compete with him on his stage.", "s19"),
     ]},
    {"id": "s18", "title": "The Hearing", "text": "A Senate hearing — convened on emergency grounds — wants you to testify. Vought's counsel sits behind a stack of NDAs the size of a phone book. Cameras everywhere. Your hands, weirdly, calm.",
     "choices": [
        ("Testify with every detail", "Truth, public, repeated.", "s20"),
        ("Testify only on what you witnessed", "Stay defensible; let evidence carry the rest.", "s21"),
     ]},
    {"id": "s19", "title": "The Long Game", "text": "Instead of going public, you become a source — careful, slow, sustained. Over a year you and Starlight and Mira drip-feed a coalition of reporters until Vought's brand is dust without a single moment of you on camera.",
     "choices": [
        ("Stay anonymous forever", "Some heroes do not autograph.", "end_anon"),
        ("Eventually take credit when it's safe", "Let history know who turned the lights on.", "end_credit"),
     ]},
    {"id": "s20", "title": "Verdict", "text": "Homelander is not, in the end, taken down by a punch. He is taken down by a paper trail and a public's slow, terrifying decision to stop being amused. Vought rebrands. The CEO is indicted. The country doesn't entirely heal. It just gets to keep going.",
     "choices": [
        ("Take a quiet government job in oversight", "Build the fence so this can't happen again.", "end_oversight"),
        ("Walk away from supes forever", "Some weeks are enough.", "end_done"),
     ]},
    {"id": "s21", "title": "The Boys, After", "text": "The Boys disband, mostly. Butcher disappears. Hughie marries Starlight. M.M. takes his daughter to school every day for the rest of his life. Kimiko opens a noodle shop in Queens that is, unironically, perfect.",
     "choices": [
        ("Keep in touch with all of them", "Found-family is also work.", "end_family"),
        ("Send postcards and otherwise vanish", "Closure can be a stamp.", "end_done"),
     ]},
    {"id": "end_anon", "title": "Unsigned", "text": "Your name never appears. Vought collapses. A new, slightly better company rises in its place. You take a quiet job in pharma compliance and watch documentaries about yourself, anonymously, on a Tuesday.",
     "end": "Unsigned"},
    {"id": "end_credit", "title": "The Memoir", "text": "Years later you write a careful, well-lawyered memoir. It debuts at number two. The book at number one is by Starlight. You text her congratulations and she sends you a heart emoji and a photo of her dog.",
     "end": "The Memoir"},
    {"id": "end_oversight", "title": "Building the Fence", "text": "You join the new Bureau of Superhuman Affairs. The work is paperwork; the work is hard; the work is necessary. Some weeks you miss adrenaline. Most weeks you don't.",
     "end": "Building the Fence"},
    {"id": "end_done", "title": "Out", "text": "You leave. You take a job you do not list on LinkedIn. You take a long, ordinary walk every evening and feel, finally, like a person, not a leak.",
     "end": "Out"},
    {"id": "end_family", "title": "Sundays at Kimiko's", "text": "Every Sunday The Boys eat at Kimiko's. Hughie is not allowed near the kitchen. M.M. argues with Butcher even though Butcher is half a ghost now. You sit at the end of the table where the light is best. You are happy. You are surprised by it.",
     "end": "Sundays at Kimiko's"},
])


# ---------------------------------------------------------------------------
# Outcome — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
OUTCOME = ({
    "id": "outcome-the-final-down",
    "title": "Fourth and Long",
    "sourceTitle": "Outcome",
    "kind": "movie",
    "synopsis": "A career-ending injury. A small-town team that needs you to coach them out of last place. A scout in the stands who could change everything — for a kid who is not your son but might as well be.",
    "releaseYear": 2025,
    "addedAt": "2026-05-09T00:00:00Z",
    "genre": "Drama",
    "tags": ["sports", "mentor", "second chances"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "The Diagnosis", "text": "The orthopedist hands you the scan and says the sentence that ends your playing career in twelve syllables. You drive home thinking about how to tell your wife. She is already on the porch with two beers.",
     "choices": [
        ("Tell her right away", "Honesty is the only shock-absorber.", "s2"),
        ("Sit on the porch a while first", "Some news needs a quiet runway.", "s3"),
     ]},
    {"id": "s2", "title": "Mira's Idea", "text": "Mira mentions that the high school's head-coaching job is open. She says it like she's been thinking about it. She has.",
     "choices": [
        ("Apply on Monday", "Coaching is the next room over.", "s4"),
        ("Resist; you wanted ten more years", "Grief has a right to a few days.", "s5"),
     ]},
    {"id": "s3", "title": "The Bar", "text": "Down at Lou's the high-school coach has just announced his retirement. The booster club president buys you a drink and floats the idea like it's a joke. He is not joking.",
     "choices": [
        ("Take the joke seriously", "Some doors knock back.", "s4"),
        ("Laugh it off and order water", "Self-preservation is also a play.", "s5"),
     ]},
    {"id": "s4", "title": "The First Practice", "text": "Twenty-six boys in too-big jerseys stare at you like you're the league. You are, by their standards. By the standards of your old self, you are not yet anything new.",
     "choices": [
        ("Start with conditioning", "Build the body first.", "s6"),
        ("Start with film", "Build the brain first.", "s7"),
     ]},
    {"id": "s5", "title": "The Town", "text": "The town hasn't won district in twenty-one years and has, somehow, an extremely organized booster club. Their goals for the season are unreasonable. Their casseroles are excellent.",
     "choices": [
        ("Promise them realistic improvement", "Honesty in the press box.", "s6"),
        ("Promise them a winning season", "Sometimes belief is the play.", "s7"),
     ]},
    {"id": "s6", "title": "The Kid", "text": "Junior — seventeen, six-foot-three, the arm of a man five years older — is your quarterback. He's also raising two sisters because his mother works two jobs. He has not slept enough since 2019.",
     "choices": [
        ("Build the offense around him", "Trust the kid's gift.", "s8"),
        ("Take some weight off him", "Don't burn him out before college.", "s9"),
     ]},
    {"id": "s7", "title": "The Scout", "text": "A college scout shows up to a Tuesday practice 'just to watch.' He is, distinctly, not just watching. He drinks coffee like a man on a clock.",
     "choices": [
        ("Have a conversation with him", "Build the relationship for Junior.", "s8"),
        ("Pretend you didn't notice him", "Don't let the kid feel the pressure yet.", "s9"),
     ]},
    {"id": "s8", "title": "Junior's House", "text": "You drive Junior home after practice. His mom invites you in for cornbread. His sisters do their homework on the floor. The roof leaks. The trophies on the shelf are his alone.",
     "choices": [
        ("Offer to help with college applications", "Mentorship widens the playbook.", "s10"),
        ("Stay neutral — don't overpromise", "Keep the line professional.", "s11"),
     ]},
    {"id": "s9", "title": "The Offensive Coordinator", "text": "Mira asks if you've slept. You haven't. She suggests hiring a coordinator so you can sleep occasionally. The candidate she's found used to coach a rival in the 90s and is, controversially, fluent in your old playbook.",
     "choices": [
        ("Hire her", "Strong coordinators win seasons.", "s10"),
        ("Wait until midseason to decide", "Trust your own eyes first.", "s11"),
     ]},
    {"id": "s10", "title": "Week 4 Loss", "text": "You lose to a team you should have beaten by ten. Junior throws two picks in the fourth. The booster club president writes a long email that says 'with respect' six times.",
     "choices": [
        ("Hold a film session, no chewing out", "Teach over yell.", "s12"),
        ("Air it out in the locker room", "Sometimes a season needs a thunder.", "s13"),
     ]},
    {"id": "s11", "title": "Your Wife, Honest", "text": "Mira sits you down. 'You're already coaching like he's your son,' she says. 'Make sure he wants that — and make sure his mother is okay with it.' She is, as always, the smartest person in any room.",
     "choices": [
        ("Talk to Junior's mom honestly", "Get her permission, not just consent.", "s12"),
        ("Talk to Junior first", "Ask the player.", "s13"),
     ]},
    {"id": "s12", "title": "Homecoming", "text": "You beat the third-best team in the district on Homecoming. Junior throws three touchdowns and runs in a fourth. The booster club sends three casseroles. The scout sends an email.",
     "choices": [
        ("Show Junior the email", "Knowledge is fuel.", "s14"),
        ("Sit on the email for a week", "Don't change his head mid-season.", "s15"),
     ]},
    {"id": "s13", "title": "Mom, Worried", "text": "Junior's mother says, sitting at her kitchen table, 'If he goes to a school I can't drive to, he won't go.' She loves him. She also has the right to be afraid. Both are true.",
     "choices": [
        ("Promise her you'll find a school within driving distance", "Recruit colleges, not just for talent.", "s14"),
        ("Promise her you'll help her travel to wherever he goes", "Carry the cost yourself.", "s15"),
     ]},
    {"id": "s14", "title": "The Injury Scare", "text": "Junior takes a clean hit and goes down. The team holds its breath. The trainer's two words — 'he's fine' — are the loudest thing you've heard in your life.",
     "choices": [
        ("Pull him for the rest of the half", "Cheap not to risk it.", "s16"),
        ("Trust him back in after a series off", "Players need to play.", "s17"),
     ]},
    {"id": "s15", "title": "The Booster, Pressuring", "text": "The booster club president corners you in the parking lot and 'recommends' a senior who's been sitting all season — his cousin's son. He smiles. He has a check in his pocket. He doesn't show it.",
     "choices": [
        ("Refuse — politely, publicly", "Drawing the line is also coaching.", "s16"),
        ("Find that senior a real role on merit", "Compromise without selling out.", "s17"),
     ]},
    {"id": "s16", "title": "Playoffs", "text": "First playoff game in twelve years. The school bus is half painted by parents. Junior reads from a notebook in the locker room — a list of names, mostly teachers and his sisters. He looks up. 'For them,' he says.",
     "choices": [
        ("Let the speech be the speech", "Don't add anything.", "s18"),
        ("Add one sentence to the team", "Lead with him, not over him.", "s19"),
     ]},
    {"id": "s17", "title": "The Scout, Again", "text": "The scout returns with two friends. Junior plays the game of his life and they walk over after, businesslike, and shake his hand. They want him at camp in June.",
     "choices": [
        ("Coach him through the offer", "He's never had a contract before.", "s18"),
        ("Get him a real adviser", "Refer up; protect him.", "s19"),
     ]},
    {"id": "s18", "title": "The Championship Game", "text": "Final play. Down four. Fourth and long. Junior takes the snap and the season — the whole strange year, the leak in the roof, the casseroles, the diagnosis — narrows to one throw.",
     "choices": [
        ("Trust Junior with the play he picked", "Coach the human, not just the call.", "s20"),
        ("Send in your call", "Sometimes the coach has to coach.", "s21"),
     ]},
    {"id": "s19", "title": "After the Buzzer", "text": "Whatever the scoreboard says, Junior finds you on the sideline and hugs you the way a son hugs a father. His mother is in the bleachers shouting his name in two languages. The season, you realize, was never about district.",
     "choices": [
        ("Cry where the team can see", "Let them see what care looks like.", "end_legacy"),
        ("Save the cry for the truck ride home", "Keep one private piece.", "end_quiet"),
     ]},
    {"id": "s20", "title": "The Catch", "text": "The throw hangs in the air for a year. A small receiver who has been overlooked all season catches it with one hand, like it was always going to be him. The town becomes a single sound for thirty seconds.",
     "choices": [
        ("Celebrate with the team first", "Let them have it before you have it.", "end_win"),
        ("Find Junior's mother in the stands first", "Honor the woman who made the player.", "end_family"),
     ]},
    {"id": "s21", "title": "The Drop", "text": "The throw hangs in the air for a year. It is caught and then dropped. The game ends. The team kneels in a circle that looks, almost, like a prayer.",
     "choices": [
        ("Tell them what they built was bigger than the score", "Coach for the rest of their lives.", "end_lesson"),
        ("Be quiet and let them grieve", "Give them the silence first.", "end_lesson_quiet"),
     ]},
    {"id": "end_win", "title": "Champions", "text": "The trophy is small and ugly and beautiful. The booster club throws a parade with two fire trucks. Junior goes to a school within driving distance on a full ride. You wake up the day after district and feel, for the first time in a year, fully here.",
     "end": "Champions"},
    {"id": "end_family", "title": "His Mother's Hug", "text": "She wraps you both up — Junior and you — in a hug that says everything she does not have time to put into words. You have not been hugged like that since your own mother. You stand there holding the hug until it lets you go.",
     "end": "His Mother's Hug"},
    {"id": "end_lesson", "title": "What They Built", "text": "You lose the game and win the boys. Most of them graduate. Some go on to schools nobody in this town has been to. Junior, two years later, brings you a college playbook with a Post-it note that says 'thanks for the runway.'",
     "end": "What They Built"},
    {"id": "end_lesson_quiet", "title": "The Bus Home", "text": "The bus ride home is quiet. Junior leans against the window. You sit across from him without speaking. You both already know what you'll do tomorrow — the same thing you did today, only better, until it works.",
     "end": "The Bus Home"},
    {"id": "end_legacy", "title": "Coach", "text": "Years later a man in his thirties knocks on your door — Junior, with his own kid on his hip, named after you. You did not have a son. You had, somehow, more than one. That is the outcome you didn't see coming.",
     "end": "Coach"},
    {"id": "end_quiet", "title": "Truck Ride", "text": "You drive home in the dark and cry, finally, alone in the cab. Then you go inside and eat the lasagna Mira left out and watch a tape of the playoff game and notice three plays you would do differently. You sleep. You will, again, tomorrow.",
     "end": "Truck Ride"},
])


# ---------------------------------------------------------------------------
# The Intern — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
THE_INTERN = ({
    "id": "the-intern-day-one",
    "title": "Day One, Decade Forty",
    "sourceTitle": "The Intern",
    "kind": "movie",
    "synopsis": "You're seventy and a senior intern at a fashion startup run by a woman who is brilliant and bone-tired. You have one job: be useful. You are the only one in the office who has done this work for forty years longer than the founder has been alive.",
    "releaseYear": 2015,
    "addedAt": "2026-05-08T00:00:00Z",
    "genre": "Comedy",
    "tags": ["mentor", "workplace", "warmth"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Orientation", "text": "Your badge says 'Senior Intern' and your desk faces an open-plan office of people on standing-desk treadmills. The CEO, Jules, has, on paper, eight minutes a day. You set your watch.",
     "choices": [
        ("Wait to be assigned a task", "Patience is a skill they haven't seen.", "s2"),
        ("Find something useful immediately", "Initiative is your superpower.", "s3"),
     ]},
    {"id": "s2", "title": "The Useless Day", "text": "Nobody knows what to do with you. You read the company's website twice. You watch Jules walk past your desk three times without seeing you. At 5:01 you go home and tell your daughter it was 'great.'",
     "choices": [
        ("Come back tomorrow with a plan", "Plan B.", "s4"),
        ("Tell Jules's COO you want a project", "Apply directly.", "s5"),
     ]},
    {"id": "s3", "title": "The Cluttered Desk", "text": "Jules's desk is a small civilization of receipts, samples, and three coffee cups. You ask her assistant if you can tidy it for an hour. The assistant looks at you like you offered to climb Everest barefoot.",
     "choices": [
        ("Tidy with respect — touch only what's clearly trash", "Boundaries are also kindness.", "s4"),
        ("Color-code the supply closet first", "Win small before big.", "s5"),
     ]},
    {"id": "s4", "title": "The Drive Home", "text": "Jules's chauffeur quits — Uber wars, a scheduling issue, life. You, who once drove for a living, casually offer. She refuses politely. Then she gets in.",
     "choices": [
        ("Be a calm professional driver", "Let her work in the back.", "s6"),
        ("Be a calm presence and a sounding board", "Listen when she breathes.", "s7"),
     ]},
    {"id": "s5", "title": "Cameron, Hungry to Learn", "text": "A young coworker named Cameron shyly asks you how to write a 'business email that doesn't sound like Slack.' This is, you realize, your real job.",
     "choices": [
        ("Teach him over coffee", "Mentorship is the actual product.", "s6"),
        ("Send him a one-pager", "Documentation lasts longer than coffee.", "s7"),
     ]},
    {"id": "s6", "title": "Jules's Home", "text": "She invites you in to meet her husband Matt and her daughter Paige. Matt is a stay-at-home dad who is, you sense immediately, drowning quietly. Paige drops a pancake on your shoe and hugs your leg.",
     "choices": [
        ("Be helpful without overstepping", "Be a guest, not a fixer.", "s8"),
        ("Notice Matt's loneliness gently", "See people fully.", "s9"),
     ]},
    {"id": "s7", "title": "Cameron's Promotion", "text": "Cameron is up for a small promotion and is too humble to fight for it. You suggest a quiet sentence to say to his manager. He says it. He gets the title. He brings you a muffin.",
     "choices": [
        ("Refuse the muffin with a smile", "Decline currency for kindness.", "s8"),
        ("Accept the muffin and ask him to mentor someone next", "Pay forward.", "s9"),
     ]},
    {"id": "s8", "title": "The Board's Suggestion", "text": "The investors suggest Jules step aside and hire a 'professional CEO.' Jules forwards you the email at midnight by accident. The forward is — you suspect — not entirely an accident.",
     "choices": [
        ("Listen the next morning, no advice", "Hold space first.", "s10"),
        ("Offer one careful sentence of perspective", "Mentor without prescribing.", "s11"),
     ]},
    {"id": "s9", "title": "Matt's Coffee", "text": "Matt asks if you have time for a coffee. He has, you realize, no one in his life he can talk to about being the only stay-at-home dad in this zip code. You have, in your forty-year career, met many men who needed this conversation.",
     "choices": [
        ("Have the coffee and listen", "Care travels strange roads.", "s10"),
        ("Suggest he join the dads' group at the school", "Plug him into community.", "s11"),
     ]},
    {"id": "s10", "title": "The Office Crisis", "text": "A small operational disaster — a vendor shipped two thousand wrong-colored boxes — threatens a launch. You quietly know three vendors who can pivot in 24 hours. You make four calls in fifteen minutes.",
     "choices": [
        ("Solve it quietly and never mention it", "Power is a verb.", "s12"),
        ("Solve it and brief Jules cleanly", "Give credit; build trust.", "s13"),
     ]},
    {"id": "s11", "title": "Becky's Confession", "text": "Becky, Jules's overworked assistant, hits a wall and cries in the supply closet. She is also, you find out, a brilliant manager who has been hiding it. You see her clearly.",
     "choices": [
        ("Recommend Becky for a promotion", "Promote what you see.", "s12"),
        ("Build a 90-day plan with her quietly", "Coach where you can.", "s13"),
     ]},
    {"id": "s12", "title": "Matt's Mistake", "text": "Matt confides, ashamed, that he's done something wrong in his marriage. He's not asking advice. He's asking what to do. The mentor in you knows there is no shortcut.",
     "choices": [
        ("Tell him the truth gently", "Be a friend with a spine.", "s14"),
        ("Ask him what he wants for his marriage in a year", "Coach the future, not the moment.", "s15"),
     ]},
    {"id": "s13", "title": "Jules's Cry", "text": "Jules cries in a hotel room in San Francisco at 1 a.m. and you sit on the second bed at a respectful distance and say nothing for a long time. Then you hand her a tissue.",
     "choices": [
        ("Be quietly present", "Care is sometimes a tissue.", "s14"),
        ("Say one perfect sentence", "When you do speak, it counts.", "s15"),
     ]},
    {"id": "s14", "title": "The Pitch Meeting", "text": "Jules's pitch to the board about staying as CEO is the most important hour of her year. She rehearses in front of you. You correct two slides. You leave the third alone because she's right about it and doesn't know it yet.",
     "choices": [
        ("Tell her she's right about slide three", "Make her see what you see.", "s16"),
        ("Let her discover it on her own", "Trust is also a slide.", "s17"),
     ]},
    {"id": "s15", "title": "The Office Dance Floor", "text": "An office party. Jules dances with her assistant. Cameron dances badly with a girl from accounting. You dance with a colleague named Fiona, who is, somehow, very pleasant company.",
     "choices": [
        ("Ask Fiona to dinner", "Companionship at any age.", "s16"),
        ("Stay friendly, no more", "Take care of your own pace.", "s17"),
     ]},
    {"id": "s16", "title": "The Board Decision", "text": "Jules emerges from the boardroom slightly windswept. 'I'm staying,' she says. 'Also, the new chairwoman wants to hire you full-time. I told her no. You're mine.'",
     "choices": [
        ("Accept Jules's offer", "Stay in the room you helped build.", "s18"),
        ("Negotiate for a fractional schedule", "Make space for life.", "s19"),
     ]},
    {"id": "s17", "title": "Paige's School Play", "text": "Jules can't make it. You go in her place with Matt and Paige's homemade sign. Paige sees you in the audience and her face lights up like a small city.",
     "choices": [
        ("Take a hundred terrible photos to send to Jules", "Bridge the room she's not in.", "s18"),
        ("Just be there, fully present", "Sometimes you're the photo.", "s19"),
     ]},
    {"id": "s18", "title": "One Year Later", "text": "The company is stable. Cameron runs a team. Becky runs operations. Matt and Jules are, somehow, more married than ever. You make a list every Sunday night called 'people I owe a call this week.' The list is long. You like it long.",
     "choices": [
        ("Keep working as long as it's useful", "Usefulness is a kind of youth.", "s20"),
        ("Plan a slow retirement again, on your terms", "Slow exit, full heart.", "s20"),
     ]},
    {"id": "s20", "title": "Cameron's Letter", "text": "Cameron leaves a handwritten letter on your desk on a Friday afternoon. It is two pages, slightly smudged, and it begins with 'You taught me how to be a colleague.' You read it twice and put it in the drawer where you keep important things.",
     "choices": [
        ("Stay because letters like this exist", "Mentorship is the only career that pays in letters.", "end_useful"),
        ("Plan the slow goodbye, with letters of your own to write", "Pay it forward in ink.", "end_slow"),
     ]},
    {"id": "s19", "title": "Tai Chi at Dawn", "text": "You still do tai chi in the park at 6:30. Fiona occasionally joins you, occasionally rolls her eyes. You read the paper and walk to the office. You greet the security guard by name. He greets you by name. This is, on most days, enough.",
     "choices": [
        ("Take Fiona on a weekend trip", "Companionship is a verb.", "end_companion"),
        ("Keep tai chi alone, mostly", "Solitude is also fine.", "end_serene"),
     ]},
    {"id": "end_useful", "title": "Senior Intern, Forever", "text": "They keep updating your title to dodge HR. You don't care. The cards on your desk are from kids you mentored two years ago, grown now, sending wedding photos. You are the office's secret asset, and it is, by some odd math, the best decade of your life.",
     "end": "Senior Intern, Forever"},
    {"id": "end_slow", "title": "The Slow Exit", "text": "You ramp down to two days a week and then to one a month and then to occasional cameos. The company throws you a party with a cake shaped like a briefcase. You cry. So does Cameron. So does Jules.",
     "end": "The Slow Exit"},
    {"id": "end_companion", "title": "A Weekend in Vermont", "text": "You and Fiona drive to a small inn upstate. There is leaf-peeping. There is bad wine. There is a fire in the lobby. You laugh at the same joke at the same time. You are, you realize, dating, at seventy. Strange. Good.",
     "end": "A Weekend in Vermont"},
    {"id": "end_serene", "title": "The Park at Dawn", "text": "Some mornings the park is just you and three other tai chi regulars and a fat dog. The sun comes up. You move slowly. You have, at last, a life that fits you. You did not expect, this late, to be quite this content.",
     "end": "The Park at Dawn"},
])


# ---------------------------------------------------------------------------
# Dune Part I — ⭐⭐⭐⭐⭐
# ---------------------------------------------------------------------------
DUNE_ONE = ({
    "id": "dune-one-arrakeen-arrival",
    "title": "House in the Dust",
    "sourceTitle": "Dune: Part One",
    "kind": "movie",
    "nextStoryId": "dune-sands-of-fate",
    "synopsis": "The Atreides have just landed on Arrakis. Within a week the trap will close. You can see it coming. Your father can't, or won't, in time. Find the thread that lets even one of you survive the betrayal.",
    "releaseYear": 2021,
    "addedAt": "2026-05-07T00:00:00Z",
    "genre": "Sci-Fi",
    "tags": ["epic", "noble", "betrayal"],
    "rating": 5,
    "loved": False,
}, [
    {"id": "s1", "title": "Caladan, Last Hours", "text": "Your home of nine generations is being packed into crates. Your mother has been silent for two days. The Emperor has 'gifted' your house the most dangerous planet in the universe and called it an honor.",
     "choices": [
        ("Walk the grounds one last time", "Memory is also a weapon.", "s2"),
        ("Study the Atreides intelligence file on Arrakis", "Prepare while you can.", "s3"),
     ]},
    {"id": "s2", "title": "Duncan's Goodbye", "text": "Duncan Idaho, who taught you knife work and patience, hugs you fiercely. He's leaving ahead with the advance team. He says, 'I'll see you on Arrakis,' and you both know there is a non-trivial chance he won't.",
     "choices": [
        ("Ask him to take your message to the Fremen", "Use his audience.", "s4"),
        ("Send him with only goodwill", "Trust him to read the room.", "s5"),
     ]},
    {"id": "s3", "title": "The Intelligence File", "text": "Spice production. Worm activity. Fremen population estimates that are wildly off. A note in your mother's hand: 'Do not trust the Harkonnen surrender. Do not trust anyone who calls it a surrender.'",
     "choices": [
        ("Bring the note to your father directly", "Truth into the right hand.", "s4"),
        ("Save the note for an emergency moment", "Some truths land better in fire.", "s5"),
     ]},
    {"id": "s4", "title": "Arrakeen Landing", "text": "The ramp lowers and the heat takes the breath from your lungs. Stilgar's men watch from the dunes you can't quite see. Dr. Yueh greets you with a smile he should not be wearing.",
     "choices": [
        ("Greet the locals personally and quickly", "Be seen as a man of Arrakis.", "s6"),
        ("Stand by your father in the receiving line", "Be heir before everything.", "s7"),
     ]},
    {"id": "s5", "title": "The Maker's Tooth", "text": "A Fremen messenger leaves a strange gift at your door — a crysknife in a folded cloth. Your mother goes pale. 'They are testing,' she says. 'And they are offering.'",
     "choices": [
        ("Wear the crysknife visibly to the council", "Accept the offer publicly.", "s6"),
        ("Keep it hidden until you understand it", "Receive the gift quietly.", "s7"),
     ]},
    {"id": "s6", "title": "Stilgar's First Audience", "text": "Stilgar arrives in your father's hall with the formality of a man who has never been the first to bow. Your father, to his credit, listens. Stilgar spits on the floor — a gift of water — and you realize the Fremen are reading every face in the room.",
     "choices": [
        ("Spit back as a gesture of respect", "Speak the language.", "s8"),
        ("Watch your father's response and follow his lead", "Stay coordinated.", "s9"),
     ]},
    {"id": "s7", "title": "The Bene Gesserit Test", "text": "The Reverend Mother — old, terrifying — corners you in a quiet room. The box, the needle, the choice. Pain is a hand at your throat. You hold. You hold. You hold.",
     "choices": [
        ("Trust your mother's training", "Discipline kept secret is still discipline.", "s8"),
        ("Resist the test as an insult", "Honor a price the Bene Gesserit don't bargain.", "s9"),
     ]},
    {"id": "s8", "title": "Yueh, Suffering", "text": "You see Dr. Yueh in a corridor at midnight, his hands shaking. He has a wife held by Harkonnens. He is the kindest man in this house, and he will, in two days, betray your family unless you read this exact face.",
     "choices": [
        ("Press him on what's wrong, carefully", "Read the man, save the wife if you can.", "s10"),
        ("Quietly inform Hawat and Mother", "Channels exist for a reason.", "s11"),
     ]},
    {"id": "s9", "title": "Thufir's Suspicion", "text": "Thufir Hawat, your old Mentat, reports a worry — Lady Jessica may be the traitor. He is, brilliantly, exactly wrong. The Harkonnens have planted the seed and watered it.",
     "choices": [
        ("Defend your mother without exposing your knowledge", "Move pieces without showing them.", "s10"),
        ("Tell Hawat openly that Yueh is the danger", "Risk that he believes you.", "s11"),
     ]},
    {"id": "s10", "title": "Spice Crawler", "text": "Your father takes you out into the desert on a spice crawler. A worm comes. The crew is brave; your father is braver. He saves the workers. You see what kind of duke he is. You also see why he will lose.",
     "choices": [
        ("Tell him your fears about the trap", "Try one more time.", "s12"),
        ("Tell him you understand his choices", "Honor him while he's here.", "s13"),
     ]},
    {"id": "s11", "title": "Liet-Kynes", "text": "The Imperial planetologist, secretly the leader of the Fremen, watches your house with the patience of a person who has waited a generation. He could be friend, or witness, or both.",
     "choices": [
        ("Offer him a private alliance with the Atreides", "Bridge the worlds.", "s12"),
        ("Ask him only what he needs from you", "Listen first.", "s13"),
     ]},
    {"id": "s12", "title": "The Trap Springs", "text": "Shields down. Sardaukar in the corridors. Yueh's signal already given. Your father is somewhere being chained to a chair. Your mother, somewhere, fighting with a voice that breaks bones.",
     "choices": [
        ("Find your mother first", "Family is also strategy.", "s14"),
        ("Find Hawat and rally a counter-attack", "Defense before flight.", "s15"),
     ]},
    {"id": "s13", "title": "Duncan, Last Stand", "text": "Duncan finds you with a cut over his eye and a smile that means he intends to die today. 'I'll buy you the door, Paul,' he says. 'Take your mother and go.'",
     "choices": [
        ("Take the door he buys you", "Honor his last gift.", "s14"),
        ("Stay and fight beside him", "Refuse the price.", "s15"),
     ]},
    {"id": "s14", "title": "The Desert", "text": "An ornithopter, a sandstorm, a hard landing. Then the open desert, by foot, your mother at your side, the crysknife in your hand. You are, at fifteen, learning to walk without rhythm so the worms don't come.",
     "choices": [
        ("Head for the rock outcroppings", "Cover is the desert's only mercy.", "s16"),
        ("Head deep into the deep desert", "Find the Fremen before they find you.", "s17"),
     ]},
    {"id": "s15", "title": "Hawat's Last Order", "text": "Hawat, captured, slips you a final intel — the Emperor's role in this, the Harkonnen plan for the spice. He tells you to live. He tells you to come back for him.",
     "choices": [
        ("Promise to come back for Hawat", "Honor old loyalties.", "s16"),
        ("Promise to remember the Emperor's name", "Direct the rage at the right hand.", "s17"),
     ]},
    {"id": "s16", "title": "The Sietch's Gate", "text": "Stilgar appears at the lip of a canyon with twenty Fremen behind him. They are not, in any sense, smiling. They have come, you realize, to decide whether to take you or to kill you.",
     "choices": [
        ("Offer them your service and the crysknife", "Be a man of the desert as quickly as you can.", "s18"),
        ("Speak the Bene Gesserit half-language to win the women's eyes", "Use the mythology that already exists about you.", "s19"),
     ]},
    {"id": "s17", "title": "The Vision", "text": "Spice in the air; spice in your blood. You see possible futures pour through your head — every version of yourself, including the ones where you become exactly the monster the Bene Gesserit warned of. You vow to choose carefully.",
     "choices": [
        ("Choose the path with the smallest jihad", "Counted bodies are also numbers.", "s18"),
        ("Choose the path with the fastest justice", "Speed of vengeance is its own currency.", "s19"),
     ]},
    {"id": "s18", "title": "Becoming Muad'Dib", "text": "You take a Fremen name. You learn to walk the dunes without thinking. You meet a young woman named Chani who watches you the way one watches a storm form. You feel the prophecy fitting on you like a suit you didn't ask for.",
     "choices": [
        ("Lean into the prophecy strategically", "Become the legend on purpose.", "s20"),
        ("Resist the prophecy and be just a man", "Stay yourself; survive.", "s21"),
     ]},
    {"id": "s19", "title": "Justice for the House", "text": "You find Rabban's outposts and burn the spice in ways that hurt the Harkonnens specifically. You become a name they whisper. You also become a name the universe will not forget — for better and absolutely for worse.",
     "choices": [
        ("Press the war on every front", "Force the Emperor's hand.", "s20"),
        ("Pull back and rebuild a coalition", "Patience is a Fremen virtue.", "s21"),
     ]},
    {"id": "s20", "title": "The Edge of the Holy War", "text": "From a ridge you watch banners on the horizon — yours, now — pouring down toward Arrakeen. You feel the future you tried to avoid arriving like weather. You take a breath. You walk down to meet it.",
     "choices": [
        ("Lead the war and accept its cost", "Some destinies you walk into.", "end_lisan"),
        ("Try one last time to steer the war to a smaller end", "Even prophets can edit.", "end_quieter"),
     ]},
    {"id": "s21", "title": "The Quieter Road", "text": "You and Chani and Stilgar agree to a slower, deeper plan — one that does not write your name in every star system. You give up some fame for some sanity. The desert, for one summer, is peaceful enough to hear.",
     "choices": [
        ("Build a Fremen-led future with you as a steward, not a god", "Decentralize the legend.", "end_steward"),
        ("Disappear south for a year of training and patience", "Wait for the right shape of war.", "end_quieter"),
     ]},
    {"id": "end_lisan", "title": "Lisan al-Gaib", "text": "The banners spread. The Sardaukar fall. Shaddam is forced to abdicate on the sand. You sit on a stone that is not a throne and feel, very clearly, the cost of every life that wasn't necessary. You will carry it. You have no other choice.",
     "end": "Lisan al-Gaib"},
    {"id": "end_quieter", "title": "Smaller Storms", "text": "The war comes anyway, but smaller — you take Arrakis without taking the universe. The Atreides flag flies over Arrakeen and a thousand fewer worlds burn. History will call it a half-victory. Chani will call it a marriage.",
     "end": "Smaller Storms"},
    {"id": "end_steward", "title": "The Steward of the Sand", "text": "You refuse the title of god and accept the title of partner. Stilgar runs the council. You handle the off-world. The Fremen, for the first time in a thousand years, run their own planet. You sleep at night. Mostly.",
     "end": "The Steward of the Sand"},
])


# ---------------------------------------------------------------------------
# Housemaid — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
HOUSEMAID = ({
    "id": "housemaid-the-attic-room",
    "title": "The Attic Room",
    "sourceTitle": "The Housemaid",
    "kind": "movie",
    "synopsis": "You took the live-in housekeeping job because nobody else would hire someone with your record. The Winchesters' attic locks from the outside. You'll find out why.",
    "releaseYear": 2025,
    "addedAt": "2026-05-06T00:00:00Z",
    "genre": "Thriller",
    "tags": ["domestic", "secrets", "captivity"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Driveway", "text": "The house is bigger than the brochure suggested. Mrs. Winchester smiles from the doorway like a woman who has practiced. Her husband Andrew loads your duffel into the foyer himself.",
     "choices": [
        ("Be cheerful and grateful", "First impressions are the wages.", "s2"),
        ("Be polite and observant", "Watch before you smile.", "s3"),
     ]},
    {"id": "s2", "title": "The Tour", "text": "Nina Winchester guides you through twelve rooms she does not appear to know. Andrew lingers a step behind. The attic stairs are at the end of the upstairs hall. She does not turn that light on.",
     "choices": [
        ("Ask about the attic directly", "Curiosity gets you fired or hired.", "s4"),
        ("Note it silently and move on", "Some doors open later.", "s5"),
     ]},
    {"id": "s3", "title": "House Rules", "text": "Nina hands you a typed list of rules. Twenty-three of them. Rule eleven: 'Do not enter the attic for any reason.' Rule twelve: 'You will sleep in the attic.'",
     "choices": [
        ("Sign and ask no questions", "Money first; sense later.", "s4"),
        ("Ask gentle, clarifying questions", "Probe softly.", "s5"),
     ]},
    {"id": "s4", "title": "The First Night", "text": "The attic is hot and small and the door locks from the outside. The lock looks new. You hear, downstairs, a marriage that is not whispered enough.",
     "choices": [
        ("Try the door to see if it really locks", "Test the trap before it tests you.", "s6"),
        ("Sit very still and listen", "Eavesdrop is also reconnaissance.", "s7"),
     ]},
    {"id": "s5", "title": "Cecelia, the Daughter", "text": "Cecelia, nine, is the only person in this house who acts like she sees you. She is, you sense immediately, both clever and afraid. She slides you a folded paper at breakfast.",
     "choices": [
        ("Read the note when alone", "Children's warnings deserve respect.", "s6"),
        ("Burn the note and never speak of it", "Some kindnesses must be turned down for safety.", "s7"),
     ]},
    {"id": "s6", "title": "Andrew's Charm", "text": "Andrew finds reasons to be in your kitchen. He compliments your coffee, your hair, your record. He has read your file. He makes 'I know what you did' sound like a love note.",
     "choices": [
        ("Hold a hard line on professional distance", "Distance is a vow you keep with both hands.", "s8"),
        ("Pretend to laugh along while building a plan", "Camouflage is also strategy.", "s9"),
     ]},
    {"id": "s7", "title": "Nina, Cracking", "text": "Nina cries in the pantry over a broken jar. It is not about the jar. She wants to tell you something and then visibly decides not to. The decision costs her.",
     "choices": [
        ("Gently invite her to talk", "Allies arrive odd.", "s8"),
        ("Bring her tea and listen", "Silence can be more useful than questions.", "s9"),
     ]},
    {"id": "s8", "title": "The Last Maid", "text": "You find an old payroll stub jammed behind a drawer — the name of the maid before you. You search her online. She, you discover, has been missing for fourteen months.",
     "choices": [
        ("Photograph the stub and hide the photo", "Document before they realize.", "s10"),
        ("Reach out to the missing maid's family", "Bridge two wounds.", "s11"),
     ]},
    {"id": "s9", "title": "The Locked Room", "text": "There is a room on the second floor neither Winchester ever enters. The door is locked, but not securely. A key hangs in plain sight on a hook in the kitchen.",
     "choices": [
        ("Take the key and look inside", "Information is freedom.", "s10"),
        ("Wait until you understand the house better", "Patience is its own key.", "s11"),
     ]},
    {"id": "s10", "title": "Nina's Confession", "text": "Nina pulls you into the laundry room and whispers: 'He's done it before. He's done it to me. I need you to help me. I need you not to think I'm crazy.' Her wrist has finger marks shaped like a man's hand.",
     "choices": [
        ("Trust her and plan together", "Believe women.", "s12"),
        ("Trust her and contact a lawyer for her first", "Help her professionalize the escape.", "s13"),
     ]},
    {"id": "s11", "title": "The Cellar", "text": "The locked room turns out to be ordinary. The interesting room is the cellar. Boxes labeled with women's names. The dates on them are spread over a decade.",
     "choices": [
        ("Photograph everything quickly", "Build a case without being seen.", "s12"),
        ("Take one box upstairs and confront", "Some confrontations are also evidence.", "s13"),
     ]},
    {"id": "s12", "title": "The Police Officer", "text": "You go to the local sheriff at lunch. He listens. He nods. He calls Andrew Winchester 'Andy' and tells you 'we'll handle it.' You realize you may have just announced yourself to the wrong room.",
     "choices": [
        ("Skip town with Nina tonight", "Some plans accelerate.", "s14"),
        ("Find a different jurisdiction", "Go higher and farther.", "s15"),
     ]},
    {"id": "s13", "title": "The Babysitter Cam", "text": "Cecelia's room has a nanny cam pointed at the door. You realize the cam is wired through Andrew's office. You also realize the cam can be turned around.",
     "choices": [
        ("Turn it on the master bedroom", "Use his own weapons.", "s14"),
        ("Smash it and pretend it broke", "Eliminate his window.", "s15"),
     ]},
    {"id": "s14", "title": "Night of the Storm", "text": "The power goes out in a thunderstorm. Andrew, on the stairs, voice changed, says, 'You have nowhere to go.' He is wrong but you have minutes to prove it.",
     "choices": [
        ("Get Nina and Cecelia to the car", "Save who you can.", "s16"),
        ("Lure Andrew to the attic and lock him in", "Use his own trap.", "s17"),
     ]},
    {"id": "s15", "title": "Lawyer", "text": "Nina's college friend — a divorce attorney with a particular reputation — meets you both in a hotel lobby. She has, she says, been waiting six years for Nina to call. She has been ready for six years.",
     "choices": [
        ("Sign the paperwork; start the protective orders", "Paper wins long wars.", "s16"),
        ("Push for criminal charges immediately", "Use both fronts.", "s17"),
     ]},
    {"id": "s16", "title": "Highway", "text": "Three of you in a car at 2 a.m. Cecelia asleep in the back. Nina holding a list of motels with cash. You driving like a person who has been preparing to leave somewhere her entire life.",
     "choices": [
        ("Drive across state lines tonight", "Distance buys days.", "s18"),
        ("Stop at a women's shelter you trust", "Allies are also armor.", "s19"),
     ]},
    {"id": "s17", "title": "The Attic, Reversed", "text": "Andrew, in the attic, banging on the door he installed for someone else. You stand in the hall with Cecelia's hand in yours. You realize the lock has, in fact, always been on his side. He just hadn't tested it.",
     "choices": [
        ("Call 911 from the bottom of the stairs", "Document the moment.", "s18"),
        ("Walk out the front door with the women", "The trap is now his alone.", "s19"),
     ]},
    {"id": "s18", "title": "The Witness", "text": "The county prosecutor in the next state takes your file and your photos seriously. She has been looking for a Winchester case for years. The boxes in the cellar matter. So does your testimony.",
     "choices": [
        ("Agree to testify fully", "Truth is its own resume.", "s20"),
        ("Negotiate witness protection first", "Stay safe to tell it.", "s21"),
     ]},
    {"id": "s19", "title": "Shelter, Sunrise", "text": "By morning Cecelia has her own bed, Nina has her own door, and you are sitting at a table with bad coffee and three other women who have, in different houses, been you. Nobody has to explain anything.",
     "choices": [
        ("Help Nina start over", "Be the friend the last maid didn't have.", "s20"),
        ("Decide you need to start over too", "Survivors are allowed their own road.", "s21"),
     ]},
    {"id": "s20", "title": "The Trial", "text": "It takes a year. Andrew is convicted. Nina sells the house. Cecelia gets a therapist she likes. The boxes in the cellar each become a charge.",
     "choices": [
        ("Stay close to the family", "Family is sometimes the people who carried each other.", "end_family"),
        ("Move on with what you learned", "Survivor as profession.", "end_advocate"),
     ]},
    {"id": "s21", "title": "Years Later", "text": "Cecelia, eighteen, finds you at a college fair. She is okay. She wants to study law. She has, in her hand, a small framed photo of the three of you on that morning at the shelter. She wanted you to have it.",
     "choices": [
        ("Take the photo and the goodbye", "Some children's gifts are also closure.", "end_family"),
        ("Take her to dinner and stay in her life", "Some endings don't end.", "end_advocate"),
     ]},
    {"id": "end_family", "title": "The Three of You", "text": "You don't become her mother. You become something close to an aunt, a witness, a steady person on speed dial. Nina remarries kindly. Cecelia grows up. The attic door is on the wrong side of the country and you sleep, finally, with both ears.",
     "end": "The Three of You"},
    {"id": "end_advocate", "title": "The Next Maid", "text": "You start a small nonprofit — domestic workers' rights, an emergency line, a network. The next time a house like that hires someone like you, that someone has somewhere to call. The Winchesters became, accidentally, the seed of a much better thing.",
     "end": "The Next Maid"},
])


# ---------------------------------------------------------------------------
# Loot — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
LOOT = ({
    "id": "loot-the-giveaway",
    "title": "Give It All Away",
    "sourceTitle": "Loot",
    "kind": "show",
    "synopsis": "Your husband cheated. The divorce settlement gave you eighty-seven billion dollars. Your foundation has a staff of six and a board of one — you — and you don't know what an audit is. Start there.",
    "releaseYear": 2024,
    "addedAt": "2026-05-05T00:00:00Z",
    "genre": "Comedy",
    "tags": ["billionaire", "philanthropy", "second act"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Yacht to Office", "text": "You arrive at the Wells Foundation at noon in three-day-old yacht clothes. Sofia, your director, hands you a coffee that you don't recognize as coffee. The whiteboard has goals on it.",
     "choices": [
        ("Pretend you already know everything", "Confidence is a kind of competence.", "s2"),
        ("Ask Sofia to walk you through everything", "Humility is the cheaper teacher.", "s3"),
     ]},
    {"id": "s2", "title": "The Press Tour", "text": "Sofia has booked you on three morning shows. You will be asked how it feels to give away a fortune. You realize on the limo ride that you have no answer that isn't 'great?'",
     "choices": [
        ("Wing it and hope you sound human", "Charm has carried smaller jets.", "s4"),
        ("Pre-write three honest sentences", "Discipline saves dignity.", "s5"),
     ]},
    {"id": "s3", "title": "Howard's Spreadsheets", "text": "Howard is the foundation's accountant and is, you discover, extremely fun once he stops being terrified of you. He shows you the line items. You ask, sincerely, what 'overhead' is.",
     "choices": [
        ("Make Howard your real guide", "Numbers people are also feelings people.", "s4"),
        ("Buy Howard a better office chair first", "Win staff with small kindnesses.", "s5"),
     ]},
    {"id": "s4", "title": "The Homeless Shelter Visit", "text": "Sofia takes you to a shelter the foundation funds. The director recognizes the foundation but not you. She gives you the same tour she gives any donor. You realize you have been invisible to the shelter your money built.",
     "choices": [
        ("Tell her who you are", "Take ownership.", "s6"),
        ("Stay anonymous, observe", "Power is also restraint.", "s7"),
     ]},
    {"id": "s5", "title": "Twitter Disaster", "text": "An old yacht photo of you holding a glass of champagne with caption 'rough day' goes viral the morning after a flood in Mississippi. Sofia's phone is making a sound she has never heard it make.",
     "choices": [
        ("Apologize in your own words on camera", "Take the punch on purpose.", "s6"),
        ("Donate aggressively to the flood relief", "Action over words.", "s7"),
     ]},
    {"id": "s6", "title": "Nicholas, the Driver", "text": "Your driver Nicholas is also your son-from-a-first-marriage's age and an aspiring actor and the only person who tells you the truth this week. You realize you've been treating him as scenery.",
     "choices": [
        ("Promote Nicholas to assistant", "Take talent where it stands.", "s8"),
        ("Pay for his class and keep him driving", "Don't trap him in your gratitude.", "s9"),
     ]},
    {"id": "s7", "title": "Arthur, the Foundation Vet", "text": "Arthur, fifty, divorced, runs operations and treats you with the patient kindness of a man who has, you sense, seen many billionaires miss the point. You like him. He scares you a little. You decide to listen.",
     "choices": [
        ("Ask Arthur to be your sponsor at the foundation", "Pair with the steadiest person.", "s8"),
        ("Date Arthur for one bad month", "Confuse mentorship and chemistry.", "s9"),
     ]},
    {"id": "s8", "title": "The Ex's Apology", "text": "Your ex-husband John, the tech billionaire who detonated your marriage, calls. He's been to therapy. He wants to apologize. He may also want, very gently, to know what you're doing with the money.",
     "choices": [
        ("Take the apology, refuse the conversation", "Boundaries are also healing.", "s10"),
        ("Hear him out — over the phone, not in person", "Curiosity is allowed; proximity, less so.", "s11"),
     ]},
    {"id": "s9", "title": "The Vegas Slip", "text": "You and your assistant Rhonda go to Vegas for the weekend and spend ninety thousand dollars on a slot machine and a hat. Sofia calls. You answer in a casino bathroom. You realize, slowly, that you might be self-sabotaging.",
     "choices": [
        ("Call your therapist on the way home", "Pay attention to the pattern.", "s10"),
        ("Donate ten million the next morning to compensate", "Performative penance.", "s11"),
     ]},
    {"id": "s10", "title": "The Board Member Pitch", "text": "You finally ask to be added to the actual decision-making board. Sofia is surprised. Arthur is, secretly, delighted. You sit through your first vote on a hundred-million-dollar housing initiative. You actually understand most of it.",
     "choices": [
        ("Vote yes and learn from the consequences", "Engaged is also accountable.", "s12"),
        ("Vote present and ask better questions", "Don't be the loudest person in your own building.", "s13"),
     ]},
    {"id": "s11", "title": "Molly's Real Friend", "text": "You realize that Sofia, terrifyingly, has become your closest friend — and that you have not been a great friend back. You ask her to dinner that is not work. You ask about her sister, who you've never met but somehow know about.",
     "choices": [
        ("Show up at Sofia's family event this weekend", "Friends are also work, gently.", "s12"),
        ("Send a thoughtful thing instead", "Don't impose your money on her life.", "s13"),
     ]},
    {"id": "s12", "title": "The Mission Pivot", "text": "After six months you realize the foundation's mission, on paper, is too vague. You propose a sharper one: end family homelessness in two states inside ten years. Sofia stares at you. Arthur smiles.",
     "choices": [
        ("Push the new mission to the board", "Aim, big.", "s14"),
        ("Pilot it in one city first", "Prove before scale.", "s15"),
     ]},
    {"id": "s13", "title": "Howard's Promotion", "text": "You promote Howard out of accounting and into program strategy. He is briefly stunned. He brings you a binder the next morning with twenty-eight slides he made over the weekend. The first one is titled 'Where the Money Could Actually Go.'",
     "choices": [
        ("Adopt half his slides immediately", "Hire smart and listen.", "s14"),
        ("Make him present to the board next Tuesday", "Move him into the rooms.", "s15"),
     ]},
    {"id": "s14", "title": "John Returns", "text": "John shows up unannounced at your gate at midnight. He's drunk. He wants to talk. He is, on close inspection, the man you married and not the man you became with him.",
     "choices": [
        ("Send him home in his own car", "Goodbye sometimes is the kindest verb.", "s16"),
        ("Talk to him for one hour, then send him home", "Mercy with a clock.", "s17"),
     ]},
    {"id": "s15", "title": "The Anniversary Gala", "text": "The foundation's first annual gala under the new mission. You are giving the speech. You have written and unwritten it eleven times. Arthur is in the second row trying to look professional.",
     "choices": [
        ("Throw out the speech and speak honestly", "Truth in a tux.", "s16"),
        ("Stick to the script and let the room cry", "Discipline is also love.", "s17"),
     ]},
    {"id": "s16", "title": "Two Years In", "text": "The mission is, in the first two cities, working — slowly, imperfectly, more than anyone expected. The foundation has hired sharper than it ever did under any director. You have learned to read a 10-K. You hate it less than you thought.",
     "choices": [
        ("Stay engaged for another decade", "This is the life you got, late.", "s18"),
        ("Bring on a President so you can step back", "Lead by handing off.", "s19"),
     ]},
    {"id": "s17", "title": "Arthur, Honestly", "text": "Arthur, over a pizza in your absurd kitchen, tells you he likes you. He also tells you he doesn't want to date you. He wants to be a real friend for a long time. You discover, surprisingly, that this is exactly the right offer.",
     "choices": [
        ("Accept it as the gift it is", "Some loves wear cardigans.", "s18"),
        ("Hold out for romance and lose the friendship", "Sometimes wanting more loses what you have.", "s19"),
     ]},
    {"id": "s18", "title": "The Letter to John", "text": "You write John a letter you never send. It thanks him, in a strange way, for leaving you. The money was the engine of an entire life you had been postponing. Forgiveness is the strangest dividend.",
     "choices": [
        ("Burn the letter; keep the lesson", "Some closure is for you alone.", "s20"),
        ("Donate ten million in his name to spite him", "Petty as a power move.", "s20"),
     ]},
    {"id": "s20", "title": "Sunday Morning", "text": "Sunday. Sofia stops by with coffee and the paper. You sit on a porch you built with foundation money and decide, slowly, whether the next chapter is interior or public. Both, you realize, are real options now.",
     "choices": [
        ("Keep the next chapter inward", "Self-work is also work.", "end_self"),
        ("Channel the energy outward, even pettily", "Spite can fund schools.", "end_spite"),
     ]},
    {"id": "s19", "title": "Decade One Closeout", "text": "Family homelessness is down 38% in your two pilot states. The data is real. The headlines are mostly accurate. Sofia is on the cover of a magazine you never read. You are, finally, very proud of something that is not your hair.",
     "choices": [
        ("Take the second decade — scale the mission", "Don't stop because you finished one chapter.", "end_scale"),
        ("Hand off and become a private donor with opinions", "Step back; trust the team.", "end_step"),
     ]},
    {"id": "end_self", "title": "Yourself, At Last", "text": "You find, in your fifties, the version of you that John didn't get to ruin. You like her. She buys good wine. She also funds, quietly, a scholarship called 'For the Late Bloomers.' You laugh every time you sign the check.",
     "end": "Yourself, At Last"},
    {"id": "end_spite", "title": "Pettily, Productively", "text": "The donation in John's name funds, accidentally, the program that ends up beating his own foundation's outcomes by every metric. He calls to congratulate you. You let it go to voicemail. You smile.",
     "end": "Pettily, Productively"},
    {"id": "end_scale", "title": "The Next Ten Years", "text": "You sign on for another decade. The mission scales to nine states. Sofia opens a London office. You buy Arthur a really good chair. Howard goes back to overhead accounting because he missed it. Everyone, you realize, is good at exactly the thing they fled and returned to.",
     "end": "The Next Ten Years"},
    {"id": "end_step", "title": "Donor, Quiet", "text": "You step back. Sofia becomes President. You become the eccentric who shows up to galas in a hat and writes one careful editorial a year. The foundation outgrows you. That, you realize, is what foundations are for.",
     "end": "Donor, Quiet"},
])


# ---------------------------------------------------------------------------
# Wicked: For Good — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
WICKED = ({
    "id": "wicked-for-good-the-pact",
    "title": "The Last Pact",
    "sourceTitle": "Wicked: For Good",
    "kind": "movie",
    "synopsis": "Glinda has the crown. Elphaba has the price on her head. You're a school friend from Shiz who knows both of them. You can save one. Maybe.",
    "releaseYear": 2025,
    "addedAt": "2026-05-04T00:00:00Z",
    "genre": "Fantasy",
    "tags": ["friendship", "rebellion", "Oz"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Decree", "text": "A poster on every wall: 'Bring her in, alive or otherwise.' Elphaba's face is on it. So is your old roommate's. Glinda's broadcast plays softly from a megaphone — kind voice, terrible message.",
     "choices": [
        ("Go to Glinda first", "Begin where you can still walk in.", "s2"),
        ("Go to Elphaba first", "Begin where it's dangerous.", "s3"),
     ]},
    {"id": "s2", "title": "The Emerald Palace", "text": "Glinda is, somehow, both glittering and tired. She lights up at you the way she always did. 'You're here,' she says. 'Don't tell me I shouldn't be doing this. Please don't.'",
     "choices": [
        ("Listen first before you advise", "Hear her version of why.", "s4"),
        ("Tell her this is wrong", "Honest friendship.", "s5"),
     ]},
    {"id": "s3", "title": "The Forest", "text": "You find Elphaba by following a trail no map shows — a kindness her broom leaves for those who knew her. She is thinner. The broom hovers beside her, mildly protective.",
     "choices": [
        ("Ask if she still trusts Glinda", "Test the seam.", "s4"),
        ("Tell her you came to help", "Be plain.", "s5"),
     ]},
    {"id": "s4", "title": "The Animal Rebellion", "text": "A council of Animals — Goats, Bears, a wise old Cat — meets in a cave. They are organized in a way Oz has not seen in years. They want a public ally. Elphaba thinks that ally should be Glinda.",
     "choices": [
        ("Carry the message to Glinda", "Be the bridge.", "s6"),
        ("Press Elphaba to lead them publicly herself", "Stop hiding her name.", "s7"),
     ]},
    {"id": "s5", "title": "The Wizard, Old", "text": "You sneak into the Wizard's private quarters. He is older than the poster art, smaller, drinking. 'I'm not the villain,' he says. 'I'm just a man who scaled badly.' He may be telling the truth. He may be drunk.",
     "choices": [
        ("Press him on the Animal cages", "Truth from the throne first.", "s6"),
        ("Get him to confess on a phonograph", "Evidence is the new sword.", "s7"),
     ]},
    {"id": "s6", "title": "Madame Morrible", "text": "Glinda's chief adviser was your favorite teacher and is, you now see, the actual villain. She compliments your hair. She drops, casually, that she knows where your parents live.",
     "choices": [
        ("Refuse to be intimidated", "Stand even if your knees shake.", "s8"),
        ("Play dumb and gather information", "Survive to fight later.", "s9"),
     ]},
    {"id": "s7", "title": "Fiyero", "text": "Fiyero is alive — disguised, scarred, in the rebellion. He thought he'd never see you. He hugs you with both arms still working. He is, somehow, less of a prince now and more of a person.",
     "choices": [
        ("Ask after Elphaba's plan", "Get the strategy.", "s8"),
        ("Ask after Fiyero's heart", "Ask the human first.", "s9"),
     ]},
    {"id": "s8", "title": "The Trial in the Square", "text": "The Wizard's regime holds public 'trials' of Animals every Tuesday. You and Fiyero, in the crowd, watch a Goat be sentenced for the crime of speaking. The crowd is mostly silent. A few cry. None move.",
     "choices": [
        ("Move first to disrupt", "Be the spark.", "s10"),
        ("Document and leak it broadly instead", "Make the silent crowd reachable.", "s11"),
     ]},
    {"id": "s9", "title": "Glinda's Private Doubt", "text": "Glinda, alone, lets the act drop in front of you. She knows what she's enabled. She does not know how to undo it without dismantling herself.",
     "choices": [
        ("Help her plan a public reversal", "Strategy beats grand gesture.", "s10"),
        ("Help her plan a quiet abdication", "Sometimes the right exit is small.", "s11"),
     ]},
    {"id": "s10", "title": "The Plan", "text": "Three nights: an Animals' march, a Glinda statement, a Wizard ambush. You and Fiyero and Elphaba and (terrifyingly) Glinda map it out on a stolen schoolroom blackboard. The chalk feels like Shiz.",
     "choices": [
        ("Run the plan as drafted", "Trust the room.", "s12"),
        ("Insert a contingency for Glinda's safety", "Plan for the worst person you love.", "s13"),
     ]},
    {"id": "s11", "title": "The Spell Book", "text": "Elphaba pulls out the Grimmerie. There is a spell for unwriting the most powerful enchantment in Oz — but the cost is paid in something the caster loves. She looks at you for a long moment.",
     "choices": [
        ("Refuse to let her pay", "Find another way.", "s12"),
        ("Ask the Grimmerie if you can pay instead", "Carry it for her.", "s13"),
     ]},
    {"id": "s12", "title": "The March", "text": "Animals fill the Yellow Brick Road with a quiet roar. Glinda steps forward, in pink, and reads a statement that detonates the regime's narrative in one paragraph. Madame Morrible's smile drops for the first time in your life.",
     "choices": [
        ("Stand visibly beside Glinda", "Witness is a weapon.", "s14"),
        ("Stay close to Elphaba and her broom", "Protect the most hunted.", "s15"),
     ]},
    {"id": "s13", "title": "The Bucket", "text": "An assassin's water bucket — actually a clever propagandist's prop — is meant to look like Elphaba melted. The plan: faked death, real escape. Elphaba, exhausted, considers it.",
     "choices": [
        ("Run the bucket plan", "Let her die to her enemies and live to her friends.", "s14"),
        ("Convince her to stay and fight publicly", "No more hiding.", "s15"),
     ]},
    {"id": "s14", "title": "Madame Morrible's Storm", "text": "Morrible calls a hurricane. You realize she has always been the one driving the weather. The sky goes the wrong color. The plan begins to come apart in front of you.",
     "choices": [
        ("Use the Grimmerie to break her hold on the sky", "Cost-paid magic.", "s16"),
        ("Get Glinda to publicly fire her in the storm", "Snap her authority in real time.", "s17"),
     ]},
    {"id": "s15", "title": "The Wizard's Surrender", "text": "The Wizard, watching from a balcony, sees the crowd and the plan and the storm and, almost gratefully, takes off the great hat. 'I'm done,' he says into the mic. 'I'm just a man.' Glinda looks at you. So does Elphaba. The plan, suddenly, has a new ending.",
     "choices": [
        ("Replace him with a council, not a queen", "Distribute the power.", "s16"),
        ("Crown Glinda formally, with limits", "Build the constitutional kind.", "s17"),
     ]},
    {"id": "s16", "title": "Elphaba, Public", "text": "Elphaba steps onto the palace balcony for the first time in years. The crowd, knowing the truth now, does not throw water. They throw flowers. Glinda is beside her holding her hand like they're in school again.",
     "choices": [
        ("Let Elphaba speak first", "Honor the woman who carried the hate.", "s18"),
        ("Let Glinda speak first", "Honor the woman who carried the deception.", "s19"),
     ]},
    {"id": "s17", "title": "The Forest Wedding", "text": "Elphaba and Fiyero marry under a tree in the woods, the Animals as witnesses, Glinda in pink she's clearly made herself. You catch the bouquet by accident. Everyone laughs.",
     "choices": [
        ("Stay for a long, quiet year", "Some weddings deserve a celebration that lasts.", "end_friends"),
        ("Go home to your village to teach", "Be the future, in small.", "end_teach"),
     ]},
    {"id": "s18", "title": "Two Friends", "text": "Glinda and Elphaba, you realize, never stopped being who they were at Shiz. The world bent them in opposite directions and yet — somehow — they still finish each other's harmonies. You smile from the wings.",
     "choices": [
        ("Take the post they offer you in the new council", "Put your shoulder to the work.", "end_council"),
        ("Take the smaller post in a province they trust to you", "Govern a corner well.", "end_province"),
     ]},
    {"id": "s19", "title": "The Future of Oz", "text": "A council forms — Animals and humans, witches and ordinary citizens. It is imperfect. It is real. Glinda holds the gavel. Elphaba flies between provinces, an emissary nobody calls a fugitive anymore.",
     "choices": [
        ("Help draft Oz's first constitution", "Words can also save countries.", "s20"),
        ("Take a long, quiet sabbatical", "You earned it.", "s20"),
     ]},
    {"id": "s20", "title": "Yellow Brick, Repaved", "text": "Crews lay new brick over a road that once led to a fraud. Children skip beside the workers. You stand at a window and decide whether your next year is a desk in the capital or a long walk through provinces you've never seen.",
     "choices": [
        ("Take the desk and write the words", "The pen, the long way.", "end_council"),
        ("Take the walk and let others write", "The road, the longer way.", "end_self"),
     ]},
    {"id": "end_friends", "title": "Defying Gravity, Together", "text": "Years later you watch Elphaba and Glinda fly between provinces on the same broom, both laughing, both lecturing each other about leadership. Some friendships outlast the worst chapters of a country.",
     "end": "Defying Gravity, Together"},
    {"id": "end_teach", "title": "Schoolroom", "text": "You teach in the village school. You tell the children a version of events that is mostly true and entirely useful. They draw Glinda in pink and Elphaba in green and both of them as friends. They learn that's allowed.",
     "end": "Schoolroom"},
    {"id": "end_council", "title": "The New Oz", "text": "The constitution you helped draft outlives all of you. The Wicked Witch, in history class, becomes a hero. Madame Morrible becomes a villain. Glinda becomes a complicated figure — which is exactly what she always wanted.",
     "end": "The New Oz"},
    {"id": "end_province", "title": "Munchkin County", "text": "You become a quiet, beloved governor of a small province. You set up an Animals' school and a council of elders that meets weekly for tea. Elphaba and Glinda visit every Yule. The province survives them both. You sleep well.",
     "end": "Munchkin County"},
    {"id": "end_self", "title": "Sabbatical", "text": "You take a year and walk Oz on foot. You meet people who only know the story as gossip. You realize history is in the hands of whoever writes the songs. You write a few. They survive. So do you.",
     "end": "Sabbatical"},
])


# ---------------------------------------------------------------------------
# Wolves — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
WOLVES = ({
    "id": "wolves-the-cleanup",
    "title": "The Cleanup",
    "sourceTitle": "Wolves",
    "kind": "movie",
    "synopsis": "Two fixers, one body, one Manhattan night. Neither of you was supposed to be assigned to this job. Now you're both here, and the clock is small and meaningless and beautiful.",
    "releaseYear": 2024,
    "addedAt": "2026-05-03T00:00:00Z",
    "genre": "Thriller",
    "tags": ["noir", "duo", "one-night"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Penthouse", "text": "The body is exactly where the call described. So is the second fixer — a man named Park you have heard about but never met. You both stare. He says, 'I thought I was alone on this.'",
     "choices": [
        ("Refuse to share the job", "Be territorial; survive.", "s2"),
        ("Accept the buddy and split it", "Speed beats pride.", "s3"),
     ]},
    {"id": "s2", "title": "The Two Bosses", "text": "Park, on his burner, calls his guy. You call yours. Both bosses say, 'Do the job.' Neither will admit to the double-dispatch. You and Park look at each other in the elevator mirror.",
     "choices": [
        ("Make a temporary alliance with Park", "Mutual interest, no friendship.", "s4"),
        ("Pretend to and watch his hands", "Trust, but record.", "s5"),
     ]},
    {"id": "s3", "title": "First Move", "text": "Park is, you discover, oddly funny — dry as a stone, terrified of yellow taxis, allergic to dogs. He compares spread sheets of corpses he has moved in his career. You realize you have just made a friend, which is the worst.",
     "choices": [
        ("Lean into the partnership", "Two heads, fewer mistakes.", "s4"),
        ("Stay professional, distance everything", "Friendship in this job ends in funerals.", "s5"),
     ]},
    {"id": "s4", "title": "The Doorman", "text": "The doorman of the building is alert, awake, and named Mickey. He has seen you both. He is also, suspiciously, willing to be helpful in ways that do not require a tip.",
     "choices": [
        ("Bribe Mickey for the camera tape", "Cash is the language.", "s6"),
        ("Walk Mickey through a story he'll repeat", "Plant the official version.", "s7"),
     ]},
    {"id": "s5", "title": "Pamela the Hostess", "text": "The penthouse owner — Pamela — returns home unexpectedly. She walks in with grocery bags and a face that has done this once before. 'Again?' she sighs.",
     "choices": [
        ("Recruit Pamela to help", "Domestic intelligence.", "s6"),
        ("Sedate Pamela politely", "She'll thank you tomorrow.", "s7"),
     ]},
    {"id": "s6", "title": "The Van", "text": "Park has a van. You have a freight elevator code. Mickey conveniently looks the other way as you wheel out a 'rolled-up rug.' It is 3:14 a.m. and Manhattan is the wrong city to do this in.",
     "choices": [
        ("Drive to the Hudson", "Old solutions.", "s8"),
        ("Drive to a friend's freezer truck in the meatpacking district", "Newer solutions.", "s9"),
     ]},
    {"id": "s7", "title": "Park's Daughter", "text": "Park's phone rings — his daughter, 17, can't sleep. He puts her on speaker, casually, while you are mid-cleanup. You realize you have never heard a fixer be a father.",
     "choices": [
        ("Stay quiet while he parents", "Witness humanity.", "s8"),
        ("Take over the floor work so he can take the call properly", "Care is also a tactic.", "s9"),
     ]},
    {"id": "s8", "title": "The Cop", "text": "A traffic stop. The officer is twenty-three, bored, and decent. Park makes small talk in fluent New Jersey. You hand over a registration that, on paper, will check out. Probably.",
     "choices": [
        ("Talk your way past", "Charm beats panic.", "s10"),
        ("Pay the cop a bribe respectfully", "Money quiets minor problems.", "s11"),
     ]},
    {"id": "s9", "title": "The Dog Walker", "text": "A man with three dachshunds walks past the van. He looks too long. Park, who is allergic, sneezes and the door swings.",
     "choices": [
        ("Befriend the dog walker quickly", "Disarm with social warmth.", "s10"),
        ("Drive away before he processes", "Speed is the cheapest fix.", "s11"),
     ]},
    {"id": "s10", "title": "The Boss, Lying", "text": "Your boss calls again. He admits — finally — that the double-dispatch was on purpose. One of you was supposed to take care of the other one, after.",
     "choices": [
        ("Tell Park immediately", "Truth between fixers.", "s12"),
        ("Plan to flip on your boss without telling Park", "Solo exit.", "s13"),
     ]},
    {"id": "s11", "title": "The Hostess, Again", "text": "Pamela calls — calmly, after the fact — and offers you both a deal. She has been collecting evidence on the man who employed her to host these meetings. She is, in a real sense, your way out.",
     "choices": [
        ("Take Pamela's deal", "Sometimes a hostess is the boss.", "s12"),
        ("Refuse and disappear", "Solo move.", "s13"),
     ]},
    {"id": "s12", "title": "The Diner", "text": "5:11 a.m. A diner that smells like every diner you have ever loved. You and Park, both alive, both a little soot-stained, both eating eggs. The waitress refills your coffee without asking.",
     "choices": [
        ("Plan the rest of the night together", "Trust the alliance.", "s14"),
        ("Eat in companionable silence", "Some bonds don't need a strategy.", "s15"),
     ]},
    {"id": "s13", "title": "The Tunnel", "text": "You drive into the Lincoln Tunnel alone. The boss texts. You don't open it. The yellow lights blur. You become, briefly, a person who is choosing his own next sentence.",
     "choices": [
        ("Drive to your sister's house in Queens", "Some doors open inward.", "s14"),
        ("Drive west, indefinitely", "Solo exit takes you far.", "s15"),
     ]},
    {"id": "s14", "title": "The Setup", "text": "You and Park spring the trap on your bosses — together. Pamela helps. Mickey helps. The dog walker is, hilariously, a retired federal agent who helps too. The morning ends with two bosses in custody and a story nobody will believe.",
     "choices": [
        ("Take the deal the feds offer", "Witness protection beats your benefits.", "s16"),
        ("Refuse the deal; vanish on your own terms", "Self-reliance to the end.", "s17"),
     ]},
    {"id": "s15", "title": "The Trip West", "text": "Somewhere in Pennsylvania you stop for coffee at a roadside place. A waitress smiles at you and you realize you are, possibly, allowed to start over.",
     "choices": [
        ("Stay in this town for a season", "Settle on instinct.", "s18"),
        ("Keep driving until you find the right town", "Patience.", "s18"),
     ]},
    {"id": "s16", "title": "Witness Protection", "text": "They give you a new name in a quiet city. You and Park, somehow, get adjacent towns. You meet on Tuesdays in a diner halfway between for eggs and coffee and the pretense of normal lives.",
     "choices": [
        ("Live the small life", "Survival is its own win.", "s19"),
        ("Discreetly help people who need fixers, ethically", "Even a small life can serve.", "s19"),
     ]},
    {"id": "s17", "title": "The Cabin", "text": "You and Park, off-grid, buy a cabin you have no business owning. He fixes the roof. You teach yourself to make bread. The dog walker visits sometimes. Pamela sends Christmas cards. Mickey, baffling, sends Easter cards only.",
     "choices": [
        ("Stay until you grow old", "Some endings are also addresses.", "s20"),
        ("Go out once more for one good cause", "One last job, ethical.", "s20"),
     ]},
    {"id": "s18", "title": "The Hardware Store", "text": "You wander into a small-town hardware store that's hiring. The owner is older than the store. You realize that whatever happens next, your hands still know how to make things work.",
     "choices": [
        ("Take the job here, name on a paycheck", "Settle in.", "end_settle"),
        ("Keep moving — somewhere is still ahead", "Try one more town.", "end_road"),
     ]},
    {"id": "s19", "title": "The Diner Booth", "text": "Park slides into the booth with a folded newspaper and the calm of a man who has, against all odds, achieved Tuesday. You decide together what 'normal' means this week.",
     "choices": [
        ("Just be normal — eggs, paper, no work", "Earn the boredom.", "end_tuesdays"),
        ("Whisper about a case you could quietly help on", "Old habits, used kindly.", "end_ethical"),
     ]},
    {"id": "s20", "title": "Late Summer at the Cabin", "text": "Bees in the lavender. Park reading on the porch. A phone you almost never use. You realize the only debt you have left is to yourself — and even that, almost paid.",
     "choices": [
        ("Stay; this is the ending you chose", "Let the cabin keep you.", "end_cabin"),
        ("Take one careful last call — only if it's clean", "One more for the road.", "end_last"),
     ]},
    {"id": "end_settle", "title": "Roadside Town", "text": "You stay in the small town and become, eventually, a person who fixes things that aren't bodies. Doors, furnaces, the school's drainage. The town accepts you the way small towns do — slowly, then completely.",
     "end": "Roadside Town"},
    {"id": "end_road", "title": "Indefinite", "text": "You drive for two years. You read every diner menu in America. You become the kind of person who knows when a town will fit and when it won't. One spring you stop. The town is fine. You are fine. The road, finally, lets you.",
     "end": "Indefinite"},
    {"id": "end_tuesdays", "title": "Diner Tuesdays", "text": "Park's daughter graduates. He cries into his coffee. You toast with cheap mugs. You are not, by any government's definition, alive. You have, perhaps for the first time, a life.",
     "end": "Diner Tuesdays"},
    {"id": "end_ethical", "title": "Quiet Fixers", "text": "You and Park become the quiet help — for women leaving bad marriages, for whistleblowers needing rides, for a witness needing a Wednesday. You do not call it justice. You call it the work.",
     "end": "Quiet Fixers"},
    {"id": "end_cabin", "title": "The Cabin", "text": "Two old fixers, a wood stove, a dog Park finally tolerates. You both live longer than your old boss would have predicted. You are, against every actuarial table, content.",
     "end": "The Cabin"},
    {"id": "end_last", "title": "One More Time", "text": "You go back once, for a thing that needed doing. Park drives. You sit. The job ends cleanly. You return to the cabin a little tired and entirely yourselves. There is no next time. Both of you know it. Both of you are okay.",
     "end": "One More Time"},
])


# ---------------------------------------------------------------------------
# Dhurandhar — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
DHURANDHAR = ({
    "id": "dhurandhar-the-handler",
    "title": "The Handler",
    "sourceTitle": "Dhurandhar",
    "kind": "movie",
    "synopsis": "Karachi. You're an asset of the agency, deeper undercover than your own family. Your handler in Delhi has gone silent. There's a wedding tomorrow you cannot miss.",
    "releaseYear": 2025,
    "addedAt": "2026-05-02T00:00:00Z",
    "genre": "Thriller",
    "tags": ["spy", "subcontinent", "cover"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Silence on the Line", "text": "Your dead-drop in Saddar is empty for the third week. The signal mark on the wall by Burns Road has been painted over. Your handler in Delhi has, somewhere, gone quiet.",
     "choices": [
        ("Trigger the emergency protocol", "Assume the worst.", "s2"),
        ("Wait one more cycle", "Patience is also tradecraft.", "s3"),
     ]},
    {"id": "s2", "title": "The Cousin's Wedding", "text": "Your cover wife reminds you of the wedding tomorrow at the general's compound. Your in-laws, by cover, are deep into the regime. You must attend smiling.",
     "choices": [
        ("Use the wedding for one drop", "Cover is also an opportunity.", "s4"),
        ("Use the wedding only as cover, not for ops", "Don't burn a wedding.", "s5"),
     ]},
    {"id": "s3", "title": "The Lieutenant", "text": "Lt. Asad, junior ISI, has been polite to you for two years and you suspect, mildly, that he likes your cover wife. Today he asks you for a private cigarette on the balcony.",
     "choices": [
        ("Take the cigarette", "Hear him out.", "s4"),
        ("Politely decline", "Buy time.", "s5"),
     ]},
    {"id": "s4", "title": "The Old Asset", "text": "An asset older than you — a woman who runs a pharmacy in Korangi — leaves you a message inside a strip of antacids. Translation: 'Delhi compromised. Run silent. Trust nobody outside our chain.'",
     "choices": [
        ("Run silent immediately", "Trust the old hand.", "s6"),
        ("Verify her message first", "Trust, but check.", "s7"),
     ]},
    {"id": "s5", "title": "Your Cover Wife", "text": "Rabia, your cover wife of four years, is not — you have always believed — an asset herself. Tonight, over dinner, she says quietly, 'I think you should tell me what you do.'",
     "choices": [
        ("Tell her", "Honesty is also a vow.", "s6"),
        ("Deny, then evaluate her", "Trust takes longer.", "s7"),
     ]},
    {"id": "s6", "title": "The Wedding Day", "text": "Three brigadiers, two ministers, fourteen waiters who report somewhere. You smile, eat the lamb, embrace cousins who don't exist. The cake has, inexplicably, fireworks.",
     "choices": [
        ("Approach Brigadier Khan for intel", "Risk, target up.", "s8"),
        ("Stay invisible and read the room", "Watch first.", "s9"),
     ]},
    {"id": "s7", "title": "Asad's Confession", "text": "Asad pulls you aside. He says, in a quiet way, that ISI knows about a 'Delhi joint' — they don't have your name, but they have a list of forty husbands fitting your profile. Yours is one of them.",
     "choices": [
        ("Use Asad — he likes you for some reason", "Friendly enemy is the rarest asset.", "s8"),
        ("Plan immediate exfil", "Forty is a small number to be in.", "s9"),
     ]},
    {"id": "s8", "title": "The Brigadier's Daughter", "text": "Khan's daughter, twenty-two, is openly cynical about her father in a way only daughters of generals can be. She also, you discover, has access to a laptop the agency would burn for.",
     "choices": [
        ("Pitch her on a slow recruitment", "Long game.", "s10"),
        ("Steal one file and walk away", "Short game.", "s11"),
     ]},
    {"id": "s9", "title": "Karachi Traffic", "text": "On the drive home you spot the same dark Vigo twice. You change routes. It changes routes. Rabia, beside you, sees it before you do.",
     "choices": [
        ("Confront the tail at a chowk you control", "Bait them.", "s10"),
        ("Lose them through Saddar's alleys", "Disappear.", "s11"),
     ]},
    {"id": "s10", "title": "The Pharmacy", "text": "You go back to the Korangi pharmacy. The old asset — Khala Bhabhi — is not surprised. She pulls out a samosa, a USB, and a 9mm with one round in the chamber. She is, you realize, the only person in your chain who is calm.",
     "choices": [
        ("Take the USB and run", "Information first.", "s12"),
        ("Stay an hour and learn her plan", "She has one.", "s13"),
     ]},
    {"id": "s11", "title": "Rabia's Plan", "text": "Rabia, back at the apartment, opens a drawer you didn't know existed. Documents. A passport with her photo and another name. 'I was placed here by someone too,' she says. 'My handler is dead. I think we should leave together.'",
     "choices": [
        ("Believe her and run together", "Allies in the cold.", "s12"),
        ("Verify her story for an hour", "Even now.", "s13"),
     ]},
    {"id": "s12", "title": "Tharparkar", "text": "You and Rabia (or you alone) drive through the night toward the border. The Pakistani desert at 3 a.m. is a particular kind of empty. There is one checkpoint left.",
     "choices": [
        ("Bribe the checkpoint guard", "Cash is fluent.", "s14"),
        ("Take a smuggler's route around it", "Maps you memorized.", "s15"),
     ]},
    {"id": "s13", "title": "The Ambush", "text": "Three Vigos converge on a Saddar street. You take a side door into a tea shop. The owner, who has seen too many movies, recognizes the look on your face and says, in Sindhi, 'Back room. Now.'",
     "choices": [
        ("Trust the tea shop owner", "Sometimes strangers save you.", "s14"),
        ("Climb to the roof", "Old solutions.", "s15"),
     ]},
    {"id": "s14", "title": "The Joint Office", "text": "You make it to a safe-house run by a different handler than yours — Delhi's left hand, who didn't know what the right hand was doing. They are appalled, professional, in motion.",
     "choices": [
        ("Trust them to extract you cleanly", "Bureaucracy at its best.", "s16"),
        ("Demand independent extraction by an ally service", "Don't put all eggs in one Delhi.", "s17"),
     ]},
    {"id": "s15", "title": "The Beach", "text": "A small boat — Kemari, dawn — bound for an island you cannot put on a map. The fisherman has been paid in advance. He nods at Rabia. He nods at you. The water, briefly, is yours.",
     "choices": [
        ("Take the boat", "Leave by the sea.", "s16"),
        ("Decide to stay and finish the work", "Some assets cannot be exfiltrated.", "s17"),
     ]},
    {"id": "s16", "title": "Delhi, Quietly", "text": "Back home, in a debrief room with one-way glass, you trade silence for a pension and a promise. Your case officer, alive, blinks at you across a table. You realize forgiveness is, in this profession, also paperwork.",
     "choices": [
        ("Take the pension and disappear into civilian life", "Earn the boredom.", "s18"),
        ("Check the mail one more time before deciding", "An old asset always checks the mail.", "s20"),
     ]},
    {"id": "s17", "title": "The Long Game", "text": "You stay. With a new cover, a new neighborhood, a new wife on paper. You spend three years rebuilding what was burned. You uncover, eventually, the leak in Delhi. Your name will never be in a paper. You're okay with that.",
     "choices": [
        ("Take the leak's head", "Internal justice.", "s19"),
        ("Hand the leak to the agency and walk", "Let process do it.", "s19"),
     ]},
    {"id": "s18", "title": "The First Civilian Morning", "text": "You wake at 5:30 because you always have. The street vendor calls his price. You buy two oranges. Nobody is following you. You learn, slowly, to trust that.",
     "choices": [
        ("Choose the civilian life fully", "Let the rhythm reset you.", "end_quiet"),
        ("Pick up the phone when it rings, just once", "Old loyalties tug.", "end_again"),
     ]},
    {"id": "s19", "title": "The Decision in Lodhi Gardens", "text": "You walk Lodhi at dawn and weigh whether the leak deserves the personal touch or the procedural one. The trees do not, in the end, advise you. They never have.",
     "choices": [
        ("Settle it yourself, quietly", "Justice with your own hands.", "end_leak"),
        ("Let the agency settle it on paper", "Justice with letterhead.", "end_quiet"),
     ]},
    {"id": "s20", "title": "Rabia's Letter", "text": "A letter arrives from a country Rabia is not supposed to be alive in. It is two pages. It says only what one survivor says to another. You read it twice and put it in a drawer with the other things you cannot keep on a shelf.",
     "choices": [
        ("Write back, carefully", "Some lines stay open.", "end_quiet"),
        ("Burn the letter and let her live free", "Some kindnesses are silences.", "end_leak"),
     ]},
    {"id": "end_quiet", "title": "Civilian", "text": "You become a man with a small business in Pune that nobody asks about. You learn to garden. You read history. You sleep with the door unlocked once a month, then twice, then nightly. It is a strange peace, and it is yours.",
     "end": "Civilian"},
    {"id": "end_again", "title": "The Next Assignment", "text": "You take a posting in Colombo, then Singapore. You age inside a profession that does not allow you to remember birthdays. You see your cover children grow up in photographs. You will, in your sixties, write a memoir nobody will publish. It will be excellent.",
     "end": "The Next Assignment"},
    {"id": "end_leak", "title": "The Internal Justice", "text": "You find the man in Delhi who burned a generation of assets. You do not kill him. You ensure, instead, that every transaction of his life is daylight. He resigns within a month, in disgrace, and survives. That, you decide, is the right severity.",
     "end": "The Internal Justice"},
])


# ---------------------------------------------------------------------------
# Beast Games S2 — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
BEAST_GAMES = ({
    "id": "beast-games-the-final-round",
    "title": "The Final Round",
    "sourceTitle": "Beast Games",
    "kind": "show",
    "synopsis": "A thousand contestants. Millions in prize money. Cameras everywhere. You are contestant #482 and you have made it to the final ten. Don't look at the drones. Or do.",
    "releaseYear": 2025,
    "addedAt": "2026-05-01T00:00:00Z",
    "genre": "Action",
    "tags": ["competition", "endurance", "spectacle"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Top Ten", "text": "The arena is half-football-stadium, half-airport. Nine other contestants stand on circles taped to the ground. A producer in a polo shirt explains the next round with the calm of a man who has watched many people cry.",
     "choices": [
        ("Listen carefully — strategy starts at the rules", "Rules are the first weapon.", "s2"),
        ("Scan the other nine", "People before plans.", "s3"),
     ]},
    {"id": "s2", "title": "The Rules", "text": "Each round eliminates two. The eliminated are paid a sum. The remaining split the bigger pot. The producers smile when they say 'except this round.'",
     "choices": [
        ("Ask what 'except this round' means", "Always ask.", "s4"),
        ("Don't react — pretend you expected it", "Don't tip your nerves.", "s5"),
     ]},
    {"id": "s3", "title": "Allies", "text": "You spot two reliable players — Marisol, who plans, and Devon, who reads people. You also spot one chaos agent named Brad who you suspect was cast for exactly this.",
     "choices": [
        ("Form a quiet pact with Marisol and Devon", "Allies thrive in small groups.", "s4"),
        ("Befriend Brad first; use his chaos", "Sometimes the wild card is your best play.", "s5"),
     ]},
    {"id": "s4", "title": "The Stack Round", "text": "Stack soda crates higher than anyone. The producers have, you notice, given two contestants crates that wobble. Your stack is, mercifully, square.",
     "choices": [
        ("Win the round cleanly", "Don't draw heat by sabotaging.", "s6"),
        ("Help Marisol's stack secretly while building yours", "Win as a pair.", "s7"),
     ]},
    {"id": "s5", "title": "Producer's Whisper", "text": "A producer, off-camera, leans in and offers you 'a small advantage' for a brief on-camera tantrum at Brad. You realize the show is, in part, a writers' room.",
     "choices": [
        ("Refuse the producer's offer", "Stay clean.", "s6"),
        ("Take the advantage and overact mildly", "Use them back.", "s7"),
     ]},
    {"id": "s6", "title": "The Maze", "text": "A two-story plywood maze with cameras at every turn. The cameras click in a way that suggests they're tracking you in particular. Devon nudges you toward an unmarked door.",
     "choices": [
        ("Take the unmarked door", "Bet on Devon's instincts.", "s8"),
        ("Take the marked path and stay legible", "Don't trust shortcuts on TV.", "s9"),
     ]},
    {"id": "s7", "title": "The Sponsor", "text": "Round break. A sponsor wants you on Instagram doing a thirty-second clip with their energy drink. You realize your visibility has, accidentally, become an asset.",
     "choices": [
        ("Do the clip authentically", "Money is also strategy.", "s8"),
        ("Politely decline; protect your image", "Don't dilute your story.", "s9"),
     ]},
    {"id": "s8", "title": "Final Six", "text": "Six players left. The producers have, terrifyingly, started using everyone's full name. The next round involves trust.",
     "choices": [
        ("Trust Marisol publicly", "Make the pact visible.", "s10"),
        ("Trust nobody, smile at everyone", "Solo posture.", "s11"),
     ]},
    {"id": "s9", "title": "Brad's Move", "text": "Brad pulls a stunt — slips a sleeping pill into someone's water bottle. He thinks it's funny. You realize the producers are not stopping him. They are recording his face.",
     "choices": [
        ("Pour the bottle out before someone drinks it", "Conscience is a budget you spend.", "s10"),
        ("Tell production and let them handle it", "Don't be the hero on camera.", "s11"),
     ]},
    {"id": "s10", "title": "The Charity Twist", "text": "Producers reveal a side quest: each remaining contestant nominates a charity, and a portion of their final winnings will go to it. Suddenly your strategy has a public face.",
     "choices": [
        ("Pick a charity you actually care about", "Lead with truth.", "s12"),
        ("Pick a charity that polls well", "Optimize the narrative.", "s13"),
     ]},
    {"id": "s11", "title": "The Reality of Brad", "text": "Brad, off-camera, breaks down and admits he's broke. The 'chaos' was him trying to be memorable for a sponsorship. He's, suddenly, a person.",
     "choices": [
        ("Help Brad through it", "Even competitors are people.", "s12"),
        ("Be polite but stay focused", "Compassion has limits in a million-dollar game.", "s13"),
     ]},
    {"id": "s12", "title": "Final Four", "text": "Marisol, you, Devon, and — Brad. The producers love it. The pot has, you realize, become genuinely life-changing.",
     "choices": [
        ("Honor the pact with Marisol and Devon", "Allies through the ending.", "s14"),
        ("Break the pact at the right moment", "It is, after all, a game.", "s15"),
     ]},
    {"id": "s13", "title": "The Press", "text": "A reporter — between rounds — wants a comment about a video clip the show might 'leak.' You realize, again, the show is making its own news cycle.",
     "choices": [
        ("Give a careful, kind quote", "Maintain your shape.", "s14"),
        ("Decline entirely", "Power is also silence.", "s15"),
     ]},
    {"id": "s14", "title": "Endurance", "text": "Stand on a beam. Hold a bag of sand. The first to drop loses. Devon's hands shake first. You can wait him out, or you can give him a graceful exit.",
     "choices": [
        ("Wait him out", "Game theory.", "s16"),
        ("Take the dive for him", "Pact theory.", "s17"),
     ]},
    {"id": "s15", "title": "The Math", "text": "If you split with Marisol you get less per person. If you break and win solo you get the most. If you break and lose you get the appearance fee. You have one more round to decide.",
     "choices": [
        ("Stick with the pact", "Reputation outlives prize money.", "s16"),
        ("Break and run for solo win", "Bet on yourself.", "s17"),
     ]},
    {"id": "s16", "title": "Final Two", "text": "You and Marisol. The producers have built the moment perfectly. The lights, the music, the audience. She squeezes your hand. The host smiles.",
     "choices": [
        ("Propose splitting the pot live on air", "Subvert the show.", "s18"),
        ("Play the final game for the win", "Honor the format.", "s19"),
     ]},
    {"id": "s17", "title": "The Solo Path", "text": "You go solo. Marisol is gracious on camera and, you realize, won't be next time. You win the final game. The check is enormous. The flight home is silent.",
     "choices": [
        ("Pay Marisol something off the books", "Some debts are voluntary.", "s18"),
        ("Move on — it's a game", "Compartmentalize.", "s19"),
     ]},
    {"id": "s18", "title": "Live Split", "text": "On air, you propose a split. The host hesitates. Marisol accepts. The audience goes wild. The producers — eventually — agree because the moment is gold.",
     "choices": [
        ("Use your platform after the show for the charity", "Honor the bigger thing.", "end_charity"),
        ("Use your platform for your own next thing", "Honor the smaller thing — yourself.", "end_self"),
     ]},
    {"id": "s19", "title": "The Win", "text": "You win. The check is six feet tall. There is confetti. Your knees, suddenly, are jelly. Marisol hugs you because she is, somehow, a better person than the game asked her to be.",
     "choices": [
        ("Share the win with the people who got you there", "Be generous publicly.", "s20"),
        ("Take the win quietly and disappear for a year", "Recover.", "s20"),
     ]},
    {"id": "s20", "title": "The Wire Transfer", "text": "The lawyers walk you through wiring instructions in a beige office. The cursor blinks. You decide, with a finger above the trackpad, what kind of person the money is going to make you.",
     "choices": [
        ("Cut checks to the people who got you here", "Public generosity.", "end_share"),
        ("Send one to your mother and disappear for a year", "Private decompression.", "end_quiet"),
     ]},
    {"id": "end_charity", "title": "The Charity Year", "text": "You spend the year touring with the charity. The money goes where you said it would. The follower count drops back down. You are, oddly, happier without the metrics. You write the producers a thank-you that is also goodbye.",
     "end": "The Charity Year"},
    {"id": "end_self", "title": "Your Own Show", "text": "You launch a small show of your own — kinder, weirder, less zero-sum. It does fine. It does, in time, very well. The Beast producers, surprisingly, recommend you to a network.",
     "end": "Your Own Show"},
    {"id": "end_share", "title": "Sharing the Win", "text": "You write checks — to Marisol, to Devon, even to Brad. You pay your mother's house off. You set up a small fund for kids who applied to be on the show and didn't make it. It feels, you realize, like winning twice.",
     "end": "Sharing the Win"},
    {"id": "end_quiet", "title": "The Quiet Year", "text": "You disappear for a year. You hike, you sleep, you read books that are not self-help. When you come back you are a person who happened to win a thing once. You are, finally, not the contestant. You are you.",
     "end": "The Quiet Year"},
])


# ---------------------------------------------------------------------------
# A House of Dynamite — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
HOUSE_DYNAMITE = ({
    "id": "house-of-dynamite-eighteen",
    "title": "Eighteen Minutes",
    "sourceTitle": "A House of Dynamite",
    "kind": "movie",
    "synopsis": "An ICBM has been launched from somewhere — they don't know where yet — at the United States. You are the Deputy National Security Adviser. You have eighteen minutes before you have to advise.",
    "releaseYear": 2025,
    "addedAt": "2026-04-30T00:00:00Z",
    "genre": "Thriller",
    "tags": ["nuclear", "war room", "minutes"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "T-18:00", "text": "The Watch Officer's voice goes flat: 'Single SBIRS detection, ballistic, transpacific.' Your coffee, half-raised, goes back to the desk. You have eighteen minutes.",
     "choices": [
        ("Call STRATCOM first", "Verify before you wake the President.", "s2"),
        ("Wake the President first", "Time is the thing you can't make.", "s3"),
     ]},
    {"id": "s2", "title": "T-16:30", "text": "STRATCOM confirms: it's real, on a depressed trajectory, single warhead estimate. Origin: somewhere in the Sea of Okhotsk box. Not enough to assign blame yet.",
     "choices": [
        ("Demand a confidence interval", "Math now matters most.", "s4"),
        ("Order a second sensor handoff", "Verification stacks.", "s5"),
     ]},
    {"id": "s3", "title": "T-16:30", "text": "The President is on the line in 90 seconds. He sounds awake in the way only certain men sound awake at 4 a.m. 'Talk to me,' he says.",
     "choices": [
        ("Brief plainly with what you know", "Honesty cuts decision time.", "s4"),
        ("Brief carefully with caveats", "Discipline against overreaction.", "s5"),
     ]},
    {"id": "s4", "title": "T-13:00", "text": "Confidence is up to 87% real. Origin narrowed but not assigned. Three candidate countries. Two of them are nuclear states. One of them is not.",
     "choices": [
        ("Insist on confirmed attribution before recommendation", "Don't fire blind.", "s6"),
        ("Begin contingency planning for all three", "Be ready for whatever the attribution says.", "s7"),
     ]},
    {"id": "s5", "title": "T-13:00", "text": "Your Chinese counterpart — your hard-earned channel — answers your secure line. He is, audibly, also at 4 a.m. He says, 'Not us. Verify.'",
     "choices": [
        ("Trust the channel and move on", "Allies of necessity.", "s6"),
        ("Press him for one piece of corroborating data", "Verification stacks.", "s7"),
     ]},
    {"id": "s6", "title": "T-10:00", "text": "GBI — ground-based interceptors — are ready. The Pacific intercept window is narrowing. You can fire to attempt intercept now or hold for better track confidence.",
     "choices": [
        ("Authorize the interceptor shot now", "Try to break it before the math is done.", "s8"),
        ("Hold for better track", "Don't waste the few shots you have.", "s9"),
     ]},
    {"id": "s7", "title": "T-10:00", "text": "An Air Force colonel reminds the room that the President has authorized 'consultative' — not full launch — until he formally elects. The distinction is paper-thin in eighteen minutes.",
     "choices": [
        ("Get the President on with the war cabinet now", "Convene formally.", "s8"),
        ("Hold the war cabinet — let him think one more minute", "Sometimes a quiet minute saves a city.", "s9"),
     ]},
    {"id": "s8", "title": "T-7:00", "text": "GBI fires. The room watches a screen that updates every two seconds. The hit is a possible. The hit is, after a long pause, a miss. The room becomes very quiet.",
     "choices": [
        ("Authorize second shot", "Three shots in the magazine; spend.", "s10"),
        ("Hold for the final shot", "Save the last one for terminal phase.", "s11"),
     ]},
    {"id": "s9", "title": "T-7:00", "text": "Attribution lands. NSA and a second source converge: a rogue North Korean unit. Not state-sanctioned. The North Korean leadership themselves are, allegedly, asking on a back channel what's happening.",
     "choices": [
        ("Open the back channel directly", "Trust nothing, talk anyway.", "s10"),
        ("Treat the launch as state action until proven otherwise", "Operate from worst-case.", "s11"),
     ]},
    {"id": "s10", "title": "T-4:00", "text": "Second GBI: miss. The room is now praying without saying so. The President is on the line and quietly asking for one piece of advice he can take into the next sentence of his life.",
     "choices": [
        ("Tell him: no retaliatory launch, no matter what", "De-escalate first.", "s12"),
        ("Tell him: hold response posture, but reassure allies", "Hold the door open.", "s13"),
     ]},
    {"id": "s11", "title": "T-4:00", "text": "Back channel runs cold for ninety seconds and then a North Korean general — terrified — confirms the rogue unit, says they've moved to shut them down, asks for the U.S. not to escalate. He sounds like he means it.",
     "choices": [
        ("Trust him on the call alone", "Take the breath.", "s12"),
        ("Demand a verifiable action in 60 seconds", "Trust verifies.", "s13"),
     ]},
    {"id": "s12", "title": "T-2:00", "text": "Third GBI: hit. The warhead is destroyed over the Pacific. The room exhales. Then it goes cold again — there is debris, and there is the question of what happens next.",
     "choices": [
        ("Order a public, calm statement immediately", "Manage the second wave.", "s14"),
        ("Hold all statements for the next hour", "Don't speak before you understand.", "s15"),
     ]},
    {"id": "s13", "title": "T-2:00", "text": "Third GBI: miss. The warhead is in terminal phase. The trajectory is — by some appalling stroke — into open ocean three hundred miles west of the coast. Detonation is in twenty seconds.",
     "choices": [
        ("Brace the rooms for the message", "Be the calm in the room.", "s14"),
        ("Order DEFCON 2 immediately", "Worst case, prepared.", "s15"),
     ]},
    {"id": "s14", "title": "T+0:00", "text": "Either the world stays the same or it doesn't. Either way, the next sentence the President says will matter forever. He looks at you. He has, all night, been looking at you when he didn't know who else to look at.",
     "choices": [
        ("Recommend public reassurance and quiet diplomacy", "Lead with calm.", "s16"),
        ("Recommend a measured demonstration of resolve", "Lead with strength.", "s17"),
     ]},
    {"id": "s15", "title": "T+0:00", "text": "Whatever happens, you have done what is, perhaps, the most consequential job in the country tonight. Your hands have started shaking only now. You hide them under the table.",
     "choices": [
        ("Stay in the room for the next twelve hours", "Lead through the aftermath.", "s16"),
        ("Hand off to the senior team and rest", "Sustainability is a discipline.", "s17"),
     ]},
    {"id": "s16", "title": "The Address", "text": "The President addresses the nation. The wording — yours — is, against all instinct, calm and exact. The country, somehow, listens. The night becomes a memory the country tells slightly wrong for the rest of its life.",
     "choices": [
        ("Stay in office for the rebuild", "Use the moment for policy.", "s18"),
        ("Resign in a year, on your own terms", "Spend the political capital and leave.", "s18"),
     ]},
    {"id": "s17", "title": "The Debrief", "text": "The country survives. The agencies don't all behave well in the after. You testify, you correct, you fight institutional fights you didn't think you'd have to. It is, in its own way, a second long night.",
     "choices": [
        ("Push for non-proliferation reforms", "Make the night mean something.", "s19"),
        ("Speak at the memorial when the year turns", "First the dead, then the doctrine.", "s20"),
     ]},
    {"id": "s18", "title": "The Morning After", "text": "Sun on the lawn, coffee that's cold. The President asks you to draft a paragraph he can build a year on. You realize the next move decides which legacy you carry — the one that stayed or the one that left.",
     "choices": [
        ("Draft the paragraph for a long policy season", "Build, slow and steady.", "end_policy"),
        ("Draft the paragraph for a clean handoff", "Plant the legacy and go.", "end_legacy"),
     ]},
    {"id": "s19", "title": "The Hearing Room", "text": "Under the cameras you make the case that the system that worked tonight should be the system that's never tested again. The committee leans in. You decide which reform to spend your credibility on.",
     "choices": [
        ("Spend it on weapons", "Non-proliferation, hard.", "end_reform"),
        ("Spend it on the warning architecture", "Warnings, gentler.", "end_warning"),
     ]},
    {"id": "s20", "title": "The Memorial", "text": "A year on, a small memorial at the Navy Yard for the analysts who held the line that night. You speak for two minutes. You realize, after, that one of those minutes is what the next decade of your work should sound like.",
     "choices": [
        ("Turn the speech into a policy push", "Words become law.", "end_policy"),
        ("Turn the speech into your private vow", "Words become discipline.", "end_legacy"),
     ]},
    {"id": "end_policy", "title": "The Long Treaty", "text": "Two years later you stand in a room signing a treaty that, in part, exists because of that night. It is incomplete and necessary. You are old now. You sleep, mostly. The nightmares come less.",
     "end": "The Long Treaty"},
    {"id": "end_legacy", "title": "Out", "text": "You leave on your own terms and teach at a school you can pronounce. Your students do not know what you did that night. You tell them the lessons without the story. The lessons survive. So do you.",
     "end": "Out"},
    {"id": "end_reform", "title": "Non-Proliferation", "text": "The reforms slow the next escalation. Slow is not the same as stopped. You are, after a decade, both more cynical and more hopeful — a strange pair that, you realize, has always been the truth about your job.",
     "end": "Non-Proliferation"},
    {"id": "end_warning", "title": "The Better Warning", "text": "You spend the rest of your career making sure the system that woke you that night will, one day, wake fewer people. You will not be the one to use it. That is, you decide, the right kind of legacy.",
     "end": "The Better Warning"},
])


# ---------------------------------------------------------------------------
# Don't Look Up — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
DONT_LOOK_UP = ({
    "id": "dont-look-up-the-press-tour",
    "title": "The Press Tour",
    "sourceTitle": "Don't Look Up",
    "kind": "movie",
    "synopsis": "You found the comet. You also have to do a morning show. The comet does not care about ratings. Neither, soon, will you.",
    "releaseYear": 2021,
    "addedAt": "2026-04-29T00:00:00Z",
    "genre": "Comedy",
    "tags": ["satire", "apocalypse", "media"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Confirmation", "text": "Your grad student's calculation matches yours. The math is not subtle. A six-mile-wide comet will, in 188 days, end most of the species. You sit very still.",
     "choices": [
        ("Call NASA before anyone else", "Channels first.", "s2"),
        ("Call your sister, just to say it out loud", "Humans first.", "s3"),
     ]},
    {"id": "s2", "title": "The White House", "text": "Three days later you are in a beige conference room in Washington. The Chief of Staff eats a power bar while you brief. The President's daughter, in passing, asks if you've seen her hair.",
     "choices": [
        ("Demand a direct meeting with the President", "Up the chain.", "s4"),
        ("Brief the science adviser thoroughly first", "Build the case.", "s5"),
     ]},
    {"id": "s3", "title": "Morning TV", "text": "Your university PR has booked you on a morning show. The host wants you to be 'fun.' You bring three slides. He shows you two of them upside down.",
     "choices": [
        ("Be respectful and try to be heard", "Play the format.", "s4"),
        ("Lose your composure on air", "Sometimes anger is the only signal.", "s5"),
     ]},
    {"id": "s4", "title": "The Tech Billionaire", "text": "A tech billionaire named Peter offers a plan: rare metals on the comet, deflection by his company's untested rockets. He has a song. He has a TED Talk on the song. He has lawyers.",
     "choices": [
        ("Refuse and demand a public mission", "Don't sell the planet.", "s6"),
        ("Engage him cautiously to slow the deal", "Inside the room can be subversion.", "s7"),
     ]},
    {"id": "s5", "title": "The Viral Clip", "text": "Your on-air anger goes viral. Within twelve hours you are a meme, a political target, and, briefly, a sex symbol. None of it solves the comet.",
     "choices": [
        ("Use the platform for science", "Spend the moment.", "s6"),
        ("Disappear from media and focus on the work", "Save energy for the work.", "s7"),
     ]},
    {"id": "s6", "title": "The Doctor's Office", "text": "Your grad student starts taking a sedative. Your colleague at the university quietly resigns to go to a cabin. The dean asks, with a smile, whether you've considered 'softening' your tone.",
     "choices": [
        ("Refuse to soften", "Soften and the comet doesn't.", "s8"),
        ("Soften enough to stay employed", "You can't do the work if you can't pay rent.", "s9"),
     ]},
    {"id": "s7", "title": "The Whistle", "text": "A NASA engineer whose name you've been told to forget mails you internal data showing the deflection mission has been quietly delayed for Peter's mining plan.",
     "choices": [
        ("Leak it to the press", "Sunlight is the work.", "s8"),
        ("Take it to a senator who will hold a hearing", "Use channels still.", "s9"),
     ]},
    {"id": "s8", "title": "The Tour", "text": "You go on the road — town halls in red states, blue states, places that are mostly highway. The questions are good. The exhaustion is worse than the comet. You sleep on planes.",
     "choices": [
        ("Keep touring until the deflection date", "Be present everywhere.", "s10"),
        ("Pause to rest with your family", "Carry yourself too.", "s11"),
     ]},
    {"id": "s9", "title": "The Senate Hearing", "text": "Two networks carry it. Three news anchors call it 'partisan.' The senator who held the hearing is, you discover, fundraising off your testimony before it ends.",
     "choices": [
        ("Confront the senator on her tactics", "Even allies need calling out.", "s10"),
        ("Take the win — congressional record matters", "Don't fight every fight.", "s11"),
     ]},
    {"id": "s10", "title": "The Movement", "text": "A movement forms — students, scientists, retirees who remember Apollo. They wear plain shirts with one word: 'Look.' You meet them and feel, briefly, that this can still be won.",
     "choices": [
        ("Join the movement as a public face", "Lead from the front.", "s12"),
        ("Support quietly from the lab", "Lead from the bench.", "s13"),
     ]},
    {"id": "s11", "title": "Your Family", "text": "Your daughter, twelve, asks if you'd like to go skating with her on Saturday. You realize you have not been skating with her in two years. The comet, somehow, has made Saturday more important, not less.",
     "choices": [
        ("Go skating", "Be present at the home you have.", "s12"),
        ("Reschedule for after the deflection date", "Bet on the future.", "s13"),
     ]},
    {"id": "s12", "title": "The Deflection Mission Launches", "text": "Eight rockets, mostly American, some European, one Japanese. The viewing party in the desert is the saddest party you have ever attended. The launch is, by all measurements, successful.",
     "choices": [
        ("Trust the math you signed off on", "Believe the work.", "s14"),
        ("Stay on alert for the abort signal", "Trust, verify.", "s15"),
     ]},
    {"id": "s13", "title": "Peter's Plan Fails", "text": "Peter's rockets, late and underperforming, fail to deflect adequately. He blames the math, the comet, the woke. The public, in a startling moment of clarity, blames Peter.",
     "choices": [
        ("Push for the backup public mission, faster", "Salvage with urgency.", "s14"),
        ("Begin preparing the public for impact in 60 days", "Pivot to honest grief.", "s15"),
     ]},
    {"id": "s14", "title": "Three Months Out", "text": "The deflection looks like it worked. Then a second measurement shows a smaller fragment still on intercept — city-killer, not planet-killer. The whole math gets done again, in public.",
     "choices": [
        ("Push for evacuation of the projected zone", "Pragmatism saves lives.", "s16"),
        ("Push for a second, smaller deflection", "Solve it again.", "s17"),
     ]},
    {"id": "s15", "title": "The Dinner Table", "text": "Three weeks out, every dinner table in the country is, in a strange way, the same dinner table. Your family eats together. You hold your daughter's hand. You realize you have, in this terrible chapter, become a better parent.",
     "choices": [
        ("Stay home for the last weeks", "Be where you love.", "s16"),
        ("Go on the road for one last week of public service", "Help one more.", "s17"),
     ]},
    {"id": "s16", "title": "The Evacuation", "text": "The zone is evacuated — imperfectly, raggedly, but mostly. The fragment hits the ocean, not a city. The wave is bad. The wave is not what it could have been.",
     "choices": [
        ("Help with the long recovery", "The work doesn't end with the impact.", "s18"),
        ("Step back and write a book about the politics of it", "Document so it can't happen again.", "s19"),
     ]},
    {"id": "s17", "title": "Dinner Together", "text": "Whatever the math says, you and your family sit down together for the dinner that night. The wine is bad. The food is good. The conversation, briefly, is about a memory from a beach trip nobody had thought about in ten years. You laugh.",
     "choices": [
        ("Make this the meal", "Presence is the only honest verb.", "s20"),
        ("Make the morning a phone call to anyone you still owe one", "Closures, all at once.", "s20"),
     ]},
    {"id": "s18", "title": "FEMA Trailer Coffee", "text": "You stand in a parking lot with a clipboard and a clipboard-grade coffee, walking a displaced family through their paperwork. You realize most of what you know about the universe is, today, less useful than this.",
     "choices": [
        ("Stay in the field for the long recovery", "Hands-on.", "end_recovery"),
        ("Move to the policy side after a year", "Pen-on.", "end_book"),
     ]},
    {"id": "s19", "title": "The Chapter on Peter", "text": "Late at night in your office you write the chapter on Peter. It is, you discover, the chapter you needed to write for yourself. You decide whether to lead the book with it or bury it in an appendix.",
     "choices": [
        ("Lead with it; name the cost", "Be brave on page one.", "end_book"),
        ("Bury it; let the science breathe first", "Let the work speak.", "end_recovery"),
     ]},
    {"id": "s20", "title": "Tea, Three A.M.", "text": "Everyone else is asleep. You boil water you don't really need. The kettle whines. You decide whether tomorrow morning is a long meal at this table or a long list of voicemails.",
     "choices": [
        ("Make breakfast for whoever wakes first", "Stay home; stay close.", "end_dinner"),
        ("Start the list of calls before sunrise", "Closures, alphabetical.", "end_closures"),
     ]},
    {"id": "end_recovery", "title": "After", "text": "You spend the next decade on the politics of recovery, on the science of preparedness. You become a person who answers congressional phone calls. You age. You are tired. You are useful. That, in the end, is enough.",
     "end": "After"},
    {"id": "end_book", "title": "The Book", "text": "Your book is required reading in three different graduate programs ten years later. The next near-miss is handled with more sense, more speed, less Peter. You sign copies for students who were born after the night you stood on national TV and named the math.",
     "end": "The Book"},
    {"id": "end_dinner", "title": "Dinner, Together", "text": "Whatever the world does, you ate together. You held hands. You said the truth quietly. You realized, finally, that the meaningful answer to a comet is, has always been, presence with the people you love. The credits roll on a kitchen.",
     "end": "Dinner, Together"},
    {"id": "end_closures", "title": "The Phone Calls", "text": "By morning you have called everyone you owed an apology to and everyone you owed a thank-you. The list is long. The voicemails are kind. Whatever happens next, you go into it as the person you tried, all your life, to become.",
     "end": "The Phone Calls"},
])


# ---------------------------------------------------------------------------
# Speak No Evil — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
SPEAK_NO_EVIL = ({
    "id": "speak-no-evil-the-weekend",
    "title": "The Weekend",
    "sourceTitle": "Speak No Evil",
    "kind": "movie",
    "synopsis": "You spent one charming evening with another couple on vacation. They invited you to their country house for the weekend. Every awkward thing you've already overlooked was a warning.",
    "releaseYear": 2024,
    "addedAt": "2026-04-28T00:00:00Z",
    "genre": "Thriller",
    "tags": ["politeness", "guest", "discomfort"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Driveway", "text": "Paddy and Ciara wave from the porch with the warmth you remember. Their house is bigger than they implied. Your wife squeezes your hand once — a code that means 'I am being polite for both of us already.'",
     "choices": [
        ("Be open and grateful", "Trust the invitation.", "s2"),
        ("Be polite and observant", "Watch first.", "s3"),
     ]},
    {"id": "s2", "title": "The Welcome Drink", "text": "Paddy pours something amber. The toast is too long. Your daughter Agnes, nine, drinks her juice carefully and watches their boy Ant, who sits very still on a couch.",
     "choices": [
        ("Ask kindly about Ant", "Curiosity is care.", "s4"),
        ("Move past the silence with a joke", "Smooth the room.", "s5"),
     ]},
    {"id": "s3", "title": "The Cottage", "text": "Your guest cottage is across a courtyard. It locks from the outside. Paddy laughs. 'Old farmhouse,' he says. 'Lots of weird quirks.' He shows you a tiny knob to override the latch from inside.",
     "choices": [
        ("Use the knob; reset the lock", "Test the trap.", "s4"),
        ("Don't show you noticed", "Hide your noticing.", "s5"),
     ]},
    {"id": "s4", "title": "Dinner, Course One", "text": "Ciara serves rabbit. Your wife is vegetarian. Ciara has been told — twice. Ciara, smiling, says, 'You'll try a little, won't you.'",
     "choices": [
        ("Let your wife refuse politely", "Boundaries are also love.", "s6"),
        ("Cover for her with a joke", "Smooth, but smaller.", "s7"),
     ]},
    {"id": "s5", "title": "Ant's Quiet", "text": "Ant doesn't speak. Paddy says he was born without a tongue. He says it like he's offering tea. You notice Ant's mouth opens. You notice the cut is too clean to be congenital.",
     "choices": [
        ("Quietly text your friend who's a pediatrician", "Verify medically.", "s6"),
        ("Try to communicate with Ant directly", "Person before protocol.", "s7"),
     ]},
    {"id": "s6", "title": "Dance Floor", "text": "After dinner Paddy puts on music too loud. He wants your wife to dance. He grabs her hand. She glances at you. The whole room has, suddenly, the wrong temperature.",
     "choices": [
        ("Cut in and dance with your wife", "Intervene physically without escalating.", "s8"),
        ("Politely end the night with a yawn", "End the social event.", "s9"),
     ]},
    {"id": "s7", "title": "The Bedroom Walls", "text": "From the guest cottage you hear, distinctly, Ant crying in the main house. The crying is not normal nine-year-old crying. The crying is muffled because there is a hand over a mouth.",
     "choices": [
        ("Go to the main house immediately", "Act on what you hear.", "s8"),
        ("Call the local police first", "Authority before action.", "s9"),
     ]},
    {"id": "s8", "title": "Agnes, Awake", "text": "Agnes, in the guest cottage, is awake and afraid. She says, in the calm voice children sometimes use when they're trying to help adults focus, 'I want to go home.'",
     "choices": [
        ("Get the keys and leave tonight", "Trust your child.", "s10"),
        ("Promise her you'll all leave at first light", "Don't drive a back road in the dark.", "s11"),
     ]},
    {"id": "s9", "title": "Ciara, Pleading", "text": "Ciara catches you in the hallway. She is trembling. 'You don't understand,' she whispers. 'We need to leave too. Tonight. Take us with you.' She is, you realize, a victim in this house.",
     "choices": [
        ("Believe Ciara and plan a joint exit", "Save who you can.", "s10"),
        ("Trust nothing yet — get your family out first", "Family first.", "s11"),
     ]},
    {"id": "s10", "title": "Back Roads", "text": "Three a.m. The car is loaded. Paddy is at the gate, in the headlights, holding a clipboard like a friendly farmer. He smiles. 'Just a quick question,' he says.",
     "choices": [
        ("Drive past him", "Don't roll the window down.", "s12"),
        ("Roll the window an inch and stall", "Buy a second.", "s13"),
     ]},
    {"id": "s11", "title": "First Light", "text": "Six a.m. The car packed casually. You make it to the gate. Paddy is, somehow, already there, brewing coffee from a thermos. He hands you one through the window. The smell is wrong.",
     "choices": [
        ("Refuse the coffee", "Don't drink at the line.", "s12"),
        ("Take it, pour it out of sight later", "Performative gratitude.", "s13"),
     ]},
    {"id": "s12", "title": "The Police Station", "text": "You drive an hour to the nearest town. The constable is, blessedly, alert and skeptical of country charm. You hand over photos, names, and a child — Ant, or Ciara, or both — that you brought with you.",
     "choices": [
        ("Stay to give a full statement", "Be the witness.", "s14"),
        ("Get on the ferry home with your family", "Survival first.", "s15"),
     ]},
    {"id": "s13", "title": "The Drive Home", "text": "You drive home with your wife and daughter and, if you took her, Ciara and Ant in the backseat. The morning is, against all odds, blue. Your daughter falls asleep on Ant's shoulder.",
     "choices": [
        ("Stop at every petrol station to put miles between", "Buy distance.", "s14"),
        ("Drive home in one long stretch", "Get there fast.", "s15"),
     ]},
    {"id": "s14", "title": "The Investigation", "text": "The local police call colleagues in other countries. Paddy and Ciara have used this trick four times. There are missing families. There are partial confessions. There is finally, finally, a case.",
     "choices": [
        ("Cooperate fully through the trial", "See it through.", "s16"),
        ("Give a statement and protect your family's privacy after", "Witness, then withdraw.", "s17"),
     ]},
    {"id": "s15", "title": "Therapy", "text": "Your daughter starts seeing a therapist who is good with kids. Your wife starts seeing one too. You start, after some resistance, going yourself. The trip becomes, in time, a thing you survived together.",
     "choices": [
        ("Tell the story when she asks", "Honesty in doses.", "s16"),
        ("Don't volunteer until she's older", "Protect her now.", "s17"),
     ]},
    {"id": "s16", "title": "Ant's Life", "text": "Ant is in foster care now, with a family that signs. He's twelve. He writes you a letter you frame in a drawer. He says, in clean handwriting, that he is okay. He thanks you for the car ride.",
     "choices": [
        ("Stay in touch as a friend of the family", "Adopt a small role.", "s18"),
        ("Let him have his new life without yours in it", "Step back.", "s19"),
     ]},
    {"id": "s17", "title": "Five Years Later", "text": "Your daughter, fourteen, asks about it for the first time. You tell her the truth, with edges. She thanks you for taking her seriously that night. You realize that what saved you all was, partly, that you listened to a nine-year-old.",
     "choices": [
        ("Make 'listen to her' a household rule", "The lesson, on the wall.", "s20"),
        ("Just keep doing what you've been doing", "Habits are also vows.", "s20"),
     ]},
    {"id": "s18", "title": "The First Visit", "text": "Ant's foster parents invite your family for lunch. The house is small and bright and full of signs. Your daughter learns three words on the drive over. The lunch is shy and slow and very, very good.",
     "choices": [
        ("Make this a regular part of your year", "Become the slow yes.", "end_friend"),
        ("Send a card next month and see what feels right", "Let the relationship grow at its pace.", "end_step"),
     ]},
    {"id": "s19", "title": "The Quiet Decision", "text": "You decide what 'stepping back' means in practice — not absence, just not crowding. A card at Yule. A donation to the school he attends, anonymous. You write your role smaller than your heart wants. That, too, is love.",
     "choices": [
        ("Hold to the quiet plan", "Restraint as care.", "end_step"),
        ("Make one visit, then decide again", "Try the door once.", "end_friend"),
     ]},
    {"id": "s20", "title": "The Whiteboard", "text": "On the kitchen whiteboard you write, half a joke, 'LISTEN TO HER.' Your daughter laughs. Your wife laughs. Then nobody erases it. Six months later it is still there, faded.",
     "choices": [
        ("Make it the official family rule", "Some jokes are also laws.", "end_rule"),
        ("Let it stay faded — habits, not posters", "Some rules are kept by living them.", "end_habit"),
     ]},
    {"id": "end_friend", "title": "Ant's Aunt", "text": "Ant calls you on his birthday. He uses a phone with a relay service. You learn enough sign to embarrass yourself. His foster parents become your friends. The story has, somehow, a third family in it that is happy.",
     "end": "Ant's Aunt"},
    {"id": "end_step", "title": "Stepping Back", "text": "You let him build his life without your shadow. You hear, through the lawyers, that he's well. You send a card once a year and hope it lands gently. Sometimes the right amount of help is small.",
     "end": "Stepping Back"},
    {"id": "end_rule", "title": "Listen To Her", "text": "It becomes the family policy. Agnes uses it on you, the teenager edition. You learn, more than once, that she's right. You raise a daughter who doesn't talk herself out of her own discomfort. That is a quiet revolution.",
     "end": "Listen To Her"},
    {"id": "end_habit", "title": "Quiet Habits", "text": "Your family doesn't make a manifesto out of the weekend. You just live carefully, kindly, with a slightly lower bar for politeness. You hold your wife's hand more often. You take your daughter's instincts more seriously. That, year over year, is the better life.",
     "end": "Quiet Habits"},
])


# ---------------------------------------------------------------------------
# The Woman in Cabin 10 — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
CABIN_10 = ({
    "id": "cabin-10-the-luxury-cruise",
    "title": "The Splash at Two A.M.",
    "sourceTitle": "The Woman in Cabin 10",
    "kind": "movie",
    "synopsis": "A luxury cruise. A woman in the next cabin. A splash at two a.m. By morning, the cabin doesn't exist and neither does she. You're a journalist, mid-breakdown, expected to write a glossy travel piece. Try not to.",
    "releaseYear": 2025,
    "addedAt": "2026-04-27T00:00:00Z",
    "genre": "Thriller",
    "tags": ["closed-ship", "witness", "unreliable"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Boarding", "text": "Eight cabins, eleven passengers, the Aurora Borealis as backdrop, and a press kit that has misspelled your name. You're meant to write four thousand words about the canapés. Your hands shake from last week, not last drink.",
     "choices": [
        ("Network at the welcome dinner", "Money introduces itself.", "s2"),
        ("Stay quiet and observe", "Watch first.", "s3"),
     ]},
    {"id": "s2", "title": "Cabin 10", "text": "You borrow mascara from your neighbor in Cabin 10. She is thin, mid-thirties, smiling like a person who has been told to smile recently. You make a small joke about ship Wi-Fi. She laughs too sharply.",
     "choices": [
        ("Take note of her name and accent", "Catalog the encounter.", "s4"),
        ("Move on; she's just a stranger", "Don't make stories yet.", "s5"),
     ]},
    {"id": "s3", "title": "The Owner", "text": "Richard Bullmer, the billionaire owner, charms a room the way a man does who has trained on rooms. His wife Anne, glamorous and quiet, sips champagne and watches her husband perform.",
     "choices": [
        ("Try to interview Anne", "The quietest person is often the story.", "s4"),
        ("Try to interview Richard", "Aim at the loudest one.", "s5"),
     ]},
    {"id": "s4", "title": "Two A.M.", "text": "A splash. Loud, wrong, distinctly a body's weight. You scramble up. From your veranda you see, briefly, a smear of something on the rail next door.",
     "choices": [
        ("Run to Cabin 10", "First responder.", "s6"),
        ("Call security from your room", "Official channel.", "s7"),
     ]},
    {"id": "s5", "title": "Cabin 10, Morning", "text": "You ask after your neighbor at breakfast. The crew is, charmingly, baffled. There is no Cabin 10 manifest entry for last night. There is no neighbor. The room, when you check, has been cleaned to within an inch of its life.",
     "choices": [
        ("Investigate quietly", "Don't tip them yet.", "s6"),
        ("Push the captain immediately", "Force the issue.", "s7"),
     ]},
    {"id": "s6", "title": "The Cleaner", "text": "The young cleaner, Eva, is anxious in a way that exceeds the job. She drops a tray. She apologizes too long. She has, you suspect, seen the same smear you did.",
     "choices": [
        ("Win Eva's trust slowly", "Source craft.", "s8"),
        ("Press Eva quickly while she's rattled", "Strike while warm.", "s9"),
     ]},
    {"id": "s7", "title": "The Captain", "text": "Captain Larsen is steady, polite, and, in a way that's hard to name, exhausted. 'There is no Cabin 10 occupant,' he says. 'But thank you for raising it.' He looks at you in a way that says 'be careful.'",
     "choices": [
        ("Push for the security footage", "Demand evidence.", "s8"),
        ("Back down to keep his trust", "Slow the chase.", "s9"),
     ]},
    {"id": "s8", "title": "Anne, Glimpsed", "text": "You see Anne on a deck you weren't supposed to be on. She is, weirdly, not the Anne you saw at dinner. The build is wrong. The walk is wrong. Then she turns and you're not sure anymore.",
     "choices": [
        ("Photograph from a distance", "Document doubt.", "s10"),
        ("Approach her openly", "Direct.", "s11"),
     ]},
    {"id": "s9", "title": "Your Editor", "text": "Your editor in London replies to your safety-check email: 'Got it. Write the canapés.' You realize, again, that you are alone on the ship. The Wi-Fi cuts as a courtesy.",
     "choices": [
        ("Schedule a sat-phone call with your friend", "Build a witness off-ship.", "s10"),
        ("Keep notes locally in a paper notebook", "Old solutions.", "s11"),
     ]},
    {"id": "s10", "title": "Richard's Charm", "text": "Richard, all warmth, asks if you'd like a private tour. He has, charmingly, also asked about your previous reporting. He has read it. He has, you realize, briefed himself on you specifically.",
     "choices": [
        ("Take the tour, alert and unflattering", "Inside the rooms.", "s12"),
        ("Refuse politely with a cover", "Don't go alone.", "s13"),
     ]},
    {"id": "s11", "title": "Eva's Tip", "text": "Eva slips you a note in a towel: 'She was hidden in the laundry corridor for a day. I think she got out before I cleaned the cabin.' The handwriting is small and careful.",
     "choices": [
        ("Check the laundry corridor at night", "Verify.", "s12"),
        ("Try to find any port-of-call sighting", "Trace the escape.", "s13"),
     ]},
    {"id": "s12", "title": "Storm Night", "text": "A North Atlantic storm. The ship pitches. You and Eva find the woman from Cabin 10 in a crew galley, hiding behind a stack of crates. She has, somehow, kept herself fed.",
     "choices": [
        ("Hide her in your cabin until port", "Take responsibility.", "s14"),
        ("Help her radio for help externally", "Use comms.", "s15"),
     ]},
    {"id": "s13", "title": "The Body", "text": "A body washes onto the rocks near a Norwegian fishing village two days later. The crew is told it's a 'cleaner who went missing.' You realize, sickeningly, that the body is meant to be the Cabin 10 woman.",
     "choices": [
        ("Investigate the body's identity privately", "Truth in graveyards.", "s14"),
        ("Get to a journalist friend in Oslo", "Multiply yourself.", "s15"),
     ]},
    {"id": "s14", "title": "The Identity", "text": "The Cabin 10 woman is, you discover, an investigator hired by Anne's first family to investigate Richard. Anne is missing. The woman on the ship pretending to be Anne is — terrifyingly — herself a paid double.",
     "choices": [
        ("Find the real Anne", "Save the missing.", "s16"),
        ("Expose the double publicly", "Daylight.", "s17"),
     ]},
    {"id": "s15", "title": "Port of Tromsø", "text": "You step off in Tromsø with the woman from Cabin 10 wrapped in your coat. Norwegian police, blessedly, take it seriously. The lead detective is a woman who has, you can tell, dealt with cruise nonsense before.",
     "choices": [
        ("Stay in Norway through the investigation", "Be the witness.", "s16"),
        ("Get on a plane to London to make noise", "Use the platform.", "s17"),
     ]},
    {"id": "s16", "title": "Anne's Cabin", "text": "Anne is found alive in a small clinic in a fjord village where she was being kept under sedation. Her recovery is slow. Her hand reaches out, eventually, to take yours and squeeze. She remembers your name.",
     "choices": [
        ("Stay with her family in the recovery", "Be present.", "s18"),
        ("Begin writing the piece carefully", "Document.", "s19"),
     ]},
    {"id": "s17", "title": "The Piece", "text": "You write it the right way — sourced, careful, devastating. Your editor calls you. He has, this once, read the piece carefully. He prints it. It is the piece that ends Richard's empire and your problem with the canapés.",
     "choices": [
        ("Push for criminal charges in the wake of the piece", "Don't let the media moment substitute for justice.", "s18"),
        ("Take the publication and rest", "You earned it.", "s19"),
     ]},
    {"id": "s18", "title": "The Trial", "text": "Richard goes to trial. Several of his employees roll on him. Anne, recovering, testifies on video. The cleaner, Eva, becomes the surprise witness who details a year of the staff's quiet observations.",
     "choices": [
        ("Stay involved for the verdict", "See it through.", "end_justice"),
        ("Decline further coverage; protect your nerves", "Survive the after.", "end_self"),
     ]},
    {"id": "s19", "title": "Your Editor's Apology", "text": "Your editor, weeks later, apologizes — sincerely — for not taking you seriously when you said you heard a splash. He offers you a column. You take it.",
     "choices": [
        ("Use the column for investigations like this one", "Become the work.", "s20"),
        ("Use the column for something you actually love", "Reclaim joy.", "s20"),
     ]},
    {"id": "s20", "title": "First Column Pitch", "text": "Your editor wants a column-launch pitch by Friday. You sit at the desk with two outlines — one with bodies, one with coastlines. You decide which version of yourself goes onto the masthead.",
     "choices": [
        ("Pitch the investigative beat", "Become the journalist who hears splashes.", "end_column"),
        ("Pitch the travel column, properly", "Become the journalist who hears tides.", "end_joy"),
     ]},
    {"id": "end_justice", "title": "The Verdict", "text": "Richard is convicted. Anne keeps the company and turns it into a foundation. Eva is paid back wages and a real promotion. You are at the verdict in the gallery with a notepad and dry hands.",
     "end": "The Verdict"},
    {"id": "end_self", "title": "Off The Boat", "text": "You take six months off and learn to sleep again. Your therapist suggests a hobby. You take up pottery, badly. You make a single, lopsided cup that you use every morning as evidence that you exist on dry land.",
     "end": "Off The Boat"},
    {"id": "end_column", "title": "The Column", "text": "The column becomes important. You break two more cases in five years. The byline you got back is, finally, spelled correctly. You are, against every part of your earlier breakdown, working.",
     "end": "The Column"},
    {"id": "end_joy", "title": "Travel Writer, Properly", "text": "You take the column and write travel pieces that mostly aren't about murder. They are about coastlines, about old hotel kitchens, about the smell of small ports at dawn. You realize, late, that you were always a good travel writer.",
     "end": "Travel Writer, Properly"},
])


# ---------------------------------------------------------------------------
# Devs — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
DEVS = ({
    "id": "devs-the-determinism",
    "title": "The Determinism Floor",
    "sourceTitle": "Devs",
    "kind": "show",
    "synopsis": "You took the job because the salary made no sense. The lab is in a sealed building only six people enter. Today they handed you a project and a non-disclosure agreement and a small key.",
    "releaseYear": 2020,
    "addedAt": "2026-04-26T00:00:00Z",
    "genre": "Sci-Fi",
    "tags": ["quantum", "cult", "free will"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Hire", "text": "Forest, the CEO, hands you the key and a smile that has no joke behind it. 'Devs is the future,' he says. 'You'll either love it or you'll quietly leave.' Nobody, he doesn't add, has quietly left.",
     "choices": [
        ("Accept and ask no further questions", "Curiosity is sometimes deferred.", "s2"),
        ("Ask one clarifying question", "A measured probe.", "s3"),
     ]},
    {"id": "s2", "title": "Inside the Lab", "text": "Floating cubes, ambient hum, six engineers working in absolute silence on a problem you can't yet see. Katie greets you with a half-smile. The air itself feels like it's been thinking for years.",
     "choices": [
        ("Watch what they're doing", "Read the room.", "s4"),
        ("Ask Katie what 'Devs' actually does", "Ask the question.", "s5"),
     ]},
    {"id": "s3", "title": "The Question", "text": "'Why six?' you ask. Forest considers. 'Because six is the maximum that can keep a secret,' he says, 'and the minimum that can run determinism at the scale we need.'",
     "choices": [
        ("Press for what 'determinism' means here", "Definitions matter.", "s4"),
        ("File the answer away and start tomorrow", "Don't ask twice.", "s5"),
     ]},
    {"id": "s4", "title": "The Reconstruction", "text": "Lyndon shows you the screen — a grainy, jittery, but undeniable reconstruction of Joan of Arc, ten seconds of motion, voice reconstructed from physics alone. The machine, you realize, is reading backwards through the universe.",
     "choices": [
        ("Believe it and ask how far forward it can read", "The terrifying question.", "s6"),
        ("Look for the trick", "Skepticism as a posture.", "s7"),
     ]},
    {"id": "s5", "title": "Sergei, Missing", "text": "The person you replaced — Sergei — supposedly resigned and moved home to Russia. Katie says it twice in two different sentences. The redundancy is the tell.",
     "choices": [
        ("Quietly look for Sergei online", "Investigate.", "s6"),
        ("Don't look; you want to keep the job", "Survive.", "s7"),
     ]},
    {"id": "s6", "title": "Lily, Outside", "text": "A woman named Lily — Sergei's girlfriend — finds you at a coffee shop. She has questions about him. She has, you realize, more reason to be afraid than you do.",
     "choices": [
        ("Help her, carefully", "Solidarity is a verb.", "s8"),
        ("Plead ignorance and stay safe", "Protect yourself.", "s9"),
     ]},
    {"id": "s7", "title": "The Forecast", "text": "You watch Devs run a forward projection — ten minutes ahead. A coffee cup falls in the cafeteria at 12:34. At 12:34 the coffee cup falls. Nobody in the lab even blinks.",
     "choices": [
        ("Ask if free will exists in this lab", "The honest question.", "s8"),
        ("Ask if it can predict tomorrow", "The dangerous question.", "s9"),
     ]},
    {"id": "s8", "title": "Forest's Daughter", "text": "Forest's office has a single photograph of a small girl. You learn, by accident, that his daughter died in a car accident years ago. Devs, you start to suspect, is grief wearing the clothes of engineering.",
     "choices": [
        ("Try to understand Forest's grief", "Compassion as analysis.", "s10"),
        ("Decide grief is making him reckless", "Identify the risk.", "s11"),
     ]},
    {"id": "s9", "title": "The Tunnel Vision", "text": "Katie pulls you aside. 'Forest's interpretation is wrong,' she whispers. 'It's not a single line. It's many. We can pick which one we render.' This sentence will keep you awake for years.",
     "choices": [
        ("Help Katie argue the many-worlds case", "Pick the right physics.", "s10"),
        ("Believe Forest's single-line view", "Pick the kinder physics.", "s11"),
     ]},
    {"id": "s10", "title": "Sergei's Truth", "text": "You discover Sergei wasn't a Russian asset — he was a sloppy security guy who got too curious. He was killed in this building. You realize the lab has a body count.",
     "choices": [
        ("Take the evidence to the press", "Daylight beats determinism.", "s12"),
        ("Take it to a federal agency", "Process over publicity.", "s13"),
     ]},
    {"id": "s11", "title": "The Cube", "text": "You stand in the center of the rendering cube alone. The visualizations of past and future swarm you. You see — for two terrible seconds — yourself, dead, on the steps outside. The timestamp is in three days.",
     "choices": [
        ("Choose to defy the prediction", "Reach for many-worlds.", "s12"),
        ("Surrender to the determinism", "Sometimes acceptance is its own freedom.", "s13"),
     ]},
    {"id": "s12", "title": "The Plan", "text": "You and Lily and Katie meet in a parking garage. Forest's security chief Kenton is hunting both of you. The plan is messy and brave and contingent on one thing — that the machine cannot, in fact, predict everything.",
     "choices": [
        ("Execute the plan as written", "Trust the team.", "s14"),
        ("Improvise around it", "Trust your instincts.", "s15"),
     ]},
    {"id": "s13", "title": "The Confession", "text": "You walk into Forest's office alone. You ask him to let you see the rendering of his daughter — the moment of her death. He nods. You watch it. You realize the lab's whole purpose, and you weep for both of you.",
     "choices": [
        ("Stay and help him let it go", "Healing as engineering.", "s14"),
        ("Stay and help him keep it on", "Mercy as architecture.", "s15"),
     ]},
    {"id": "s14", "title": "Kenton at the Door", "text": "Kenton comes for you. The lab's predictions said this would happen. You and Lily run for the elevator. The doors close on his hand. The cube hums above you.",
     "choices": [
        ("Reach the top and confront Forest", "Confront.", "s16"),
        ("Go to the basement and pull the plug", "Confront the machine.", "s17"),
     ]},
    {"id": "s15", "title": "The Shutdown Sequence", "text": "Katie hands you the shutdown code. 'It will take 47 seconds,' she says. 'Devs will know what you're doing in the first second.' The cube already, you realize, knows.",
     "choices": [
        ("Begin the sequence anyway", "Even the predictable can surprise.", "s16"),
        ("Hesitate for a second of free will", "Pause is a vote too.", "s17"),
     ]},
    {"id": "s16", "title": "The Top of the Building", "text": "Forest, calm, waits at the top. He is not, you realize, going to fight. He is going to ask you to choose — to render his daughter alive in the simulation, or to let him die in this one.",
     "choices": [
        ("Render his daughter", "Mercy.", "s18"),
        ("Refuse and walk him out", "Reality first.", "s19"),
     ]},
    {"id": "s17", "title": "The Basement", "text": "The quantum hardware hums in a vacuum chamber the size of a chapel. You stand with your hand near a kill switch designed by a person who clearly hoped it would never be used.",
     "choices": [
        ("Pull the switch and end it", "Some doors should close.", "s18"),
        ("Walk away without pulling it", "Leave the future to itself.", "s19"),
     ]},
    {"id": "s18", "title": "The Render", "text": "The cube glows. A small girl, perfectly rendered, runs into a perfectly rendered house. Forest, on the floor, watching, smiles for the first time you have ever seen. You feel the universe split.",
     "choices": [
        ("Stay in the rendered universe with Lily", "Choose the kinder fork.", "end_render"),
        ("Stay in the unrendered universe and live", "Choose the real fork.", "end_real"),
     ]},
    {"id": "s19", "title": "After", "text": "The lab is shut. Forest dies. Lily, somehow, doesn't. You go home with a security guard's coat over your shoulders. The street outside is unrendered and dry and yours.",
     "choices": [
        ("Testify in the federal inquiry", "Witness.", "end_inquiry"),
        ("Disappear and rebuild", "Some endings are private.", "s20"),
     ]},
    {"id": "s20", "title": "Many Worlds, One Coffee", "text": "Years later, in a coffee shop, you flip a coin twenty times in a row to remind yourself that the future is not yet written. It comes up heads thirteen times. You laugh. You did not, after all, become the prediction.",
     "choices": [
        ("Live the rest of your life unmeasured", "Embrace indeterminism.", "end_quiet"),
        ("Write a memoir about Devs, carefully", "Document for the record.", "end_inquiry"),
     ]},
    {"id": "end_render", "title": "Inside the Cube", "text": "You and Lily live, in some sense, in a render. The coffee is real to you. The sunset is rendered to atomic precision. Forest's daughter has, somewhere, a long good life. You don't know what counts as 'real' anymore. You decide it doesn't matter, and the decision lets you breathe.",
     "end": "Inside the Cube"},
    {"id": "end_real", "title": "The Unrendered Day", "text": "You walk out of the building into a morning the machine never quite finished predicting. Lily takes your hand. Forest's death is not, in the end, your fault. The street, unrendered, is enough.",
     "end": "The Unrendered Day"},
    {"id": "end_inquiry", "title": "Federal Testimony", "text": "You testify for weeks. The lab is dismantled. Three engineers are charged. The technology is, you discover, more or less inevitable — someone else will build it. You write a long, careful memoir that becomes required reading in ethics classes at three universities.",
     "end": "Federal Testimony"},
    {"id": "end_quiet", "title": "Unmeasured", "text": "You move to a small city, take a small job, and disappear into a life nobody renders. Years later a documentary about Devs airs and you don't watch it. You walk to the corner store and buy oranges. They are exactly as orange as oranges.",
     "end": "Unmeasured"},
])


# ---------------------------------------------------------------------------
# The Jeffrey Dahmer Story (Monster) — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
DAHMER = ({
    "id": "dahmer-the-neighbor",
    "title": "The Neighbor in 213",
    "sourceTitle": "Monster: The Jeffrey Dahmer Story",
    "kind": "show",
    "synopsis": "Apartment 213 smells wrong again. You live in 212. The police don't listen to women who look like you in this neighborhood. You will have to be the one who is right.",
    "releaseYear": 2022,
    "addedAt": "2026-04-25T00:00:00Z",
    "genre": "Thriller",
    "tags": ["true-crime", "witness", "neighbor"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Smell", "text": "The hallway smells like meat gone wrong. The super has, four times this year, called it 'a refrigerator problem.' Your son holds his nose at his school bag.",
     "choices": [
        ("Knock on 213 yourself", "Confront politely.", "s2"),
        ("Document every incident in a notebook", "Build the case quietly.", "s3"),
     ]},
    {"id": "s2", "title": "The Door", "text": "He answers in glasses, polite, vaguely apologetic. 'It's the freezer, ma'am,' he says. 'I'll get it fixed.' He smiles. The smell, in the open doorway, gets briefly worse before he shuts it.",
     "choices": [
        ("Tell the super again, firmly", "Use the chain of command.", "s4"),
        ("Call the police non-emergency line", "Escalate.", "s5"),
     ]},
    {"id": "s3", "title": "The Notebook", "text": "You start a black notebook. Dates, times, smells, sounds. The list grows faster than you wanted it to. You realize, terrifyingly, you may need this notebook in a courtroom one day.",
     "choices": [
        ("Share the notebook with your sister", "Witnesses.", "s4"),
        ("Keep it to yourself for safety", "Protect first.", "s5"),
     ]},
    {"id": "s4", "title": "The Police, First Call", "text": "The officer is polite and bored. He tells you 'lots of single men live like this.' He does not write anything down. You realize his department's procedures are stacked against you.",
     "choices": [
        ("File a formal complaint", "Paperwork forces process.", "s6"),
        ("Wait for a worse incident, prepared", "Patience as a tactic.", "s7"),
     ]},
    {"id": "s5", "title": "Your Sister, Listening", "text": "Your sister works at the city desk of the local paper. She listens, nods, asks if she can take notes for a future story. You feel, briefly, like someone is finally on your side.",
     "choices": [
        ("Let her start a quiet file", "Build parallel pressure.", "s6"),
        ("Ask her to wait until you have proof", "Don't move too soon.", "s7"),
     ]},
    {"id": "s6", "title": "The Boy on the Stairs", "text": "A young man, dazed, wanders out of 213 into the hallway, naked, bleeding. You shield him with your own coat. Police arrive. They speak to your neighbor. They walk the boy back inside.",
     "choices": [
        ("Refuse to leave the hallway until they re-examine", "Stand your ground.", "s8"),
        ("Call your sister immediately for the story", "Use the press as a witness.", "s9"),
     ]},
    {"id": "s7", "title": "Glenda Cleveland's Call", "text": "An older neighbor, Glenda, has been calling the city for months. You compare notes. She's been ignored too. Together you make a list of names and numbers and times every department has hung up on you.",
     "choices": [
        ("Take the list to a city council member", "Politicize the silence.", "s8"),
        ("Take it directly to the FBI tip line", "Bypass local.", "s9"),
     ]},
    {"id": "s8", "title": "The Reporter's Visit", "text": "Your sister and another reporter show up at the precinct with a list of incidents in a folder. The desk officer becomes, very quickly, much more polite.",
     "choices": [
        ("Stay for the interview", "Be the named source.", "s10"),
        ("Stay anonymous; let the file speak", "Protect your family.", "s11"),
     ]},
    {"id": "s9", "title": "The Tip Line", "text": "The FBI agent who returns your call is, surprisingly, alert. She has, she says, been collecting reports from this area for a year. You hear her flip a page. You hear her say, 'Tell me everything.'",
     "choices": [
        ("Tell her everything you have", "Pour out the file.", "s10"),
        ("Tell her enough to get her on a plane", "Hook the case.", "s11"),
     ]},
    {"id": "s10", "title": "The Night It Breaks", "text": "Another man escapes 213, this time onto the street, this time louder. Officers come. This time, with your file already known to a reporter, they cuff your neighbor without re-litigating it.",
     "choices": [
        ("Watch from the hallway, calmly", "Witness the arrest.", "s12"),
        ("Hold Glenda's hand", "Care for the women who saw it first.", "s13"),
     ]},
    {"id": "s11", "title": "The Press Conference", "text": "A press conference happens three days later. The mayor uses words like 'oversight' and 'review.' He does not say your name. You and Glenda watch from a bar across the street. You order one beer between you because that's all your budget allows.",
     "choices": [
        ("Speak to a reporter outside", "Make the public statement.", "s12"),
        ("Drink the beer in silence", "Some moments are for survivors only.", "s13"),
     ]},
    {"id": "s12", "title": "The Charges", "text": "Charges multiply over weeks — body parts in the apartment, families coming forward, photographs no human should have to look at. You realize you lived next door to it for two years. You realize you tried to stop it for half of those.",
     "choices": [
        ("Read every news report obsessively", "Bear witness.", "s14"),
        ("Stop reading; protect your sleep", "Survival.", "s15"),
     ]},
    {"id": "s13", "title": "Families", "text": "Mothers and brothers and aunts of the victims come to the courthouse. You meet them, by accident, in a hallway. They thank you. You realize, painfully, that gratitude here is a form of grief.",
     "choices": [
        ("Stay close to the families through the trial", "Be present.", "s14"),
        ("Help them organize a memorial", "Action.", "s15"),
     ]},
    {"id": "s14", "title": "The Council Hearing", "text": "Months later, a city council hearing on the police failures. You testify. Glenda testifies. The officers who walked the dazed boy back into 213 lose their jobs but, somehow, keep their pensions.",
     "choices": [
        ("Push for systemic reforms", "The dead deserve a system that listens.", "s16"),
        ("Push for individual prosecution of those officers", "Accountability is also a reform.", "s17"),
     ]},
    {"id": "s15", "title": "Your Son", "text": "Your son, eight, asks if it was your fault you lived next door to him. You sit on the floor and tell him the truth — that grown-ups should have listened to you sooner, and that you did everything you could.",
     "choices": [
        ("Promise him you'll make sure people listen next time", "Turn grief into a vow.", "s16"),
        ("Promise him you'll move somewhere else", "Choose his peace.", "s17"),
     ]},
    {"id": "s16", "title": "The Mothers' Coalition", "text": "You and Glenda and three of the victims' mothers form an informal coalition — calls, hearings, a small fund for families. The work is slow. The work is real.",
     "choices": [
        ("Make this your life's work", "Keep going.", "s18"),
        ("Do it for a year, then step back", "Sustainable.", "s19"),
     ]},
    {"id": "s17", "title": "Moving Day", "text": "You pack two suitcases and your son's bike. You leave 212 with the notebook still in your purse. The new apartment is smaller and farther away and, by every measure that matters, better.",
     "choices": [
        ("Take a year before deciding what's next", "Rest first.", "s18"),
        ("Throw yourself into a new job", "Forward.", "s19"),
     ]},
    {"id": "s18", "title": "Years Later", "text": "Ten years on. A different neighborhood. A new young officer is being trained on the policies that have your name in the footnotes. You will never meet her. She will, one day, listen to a woman like you. That is, you decide, enough.",
     "choices": [
        ("Make peace with the legacy", "Forgiveness as posture.", "s20"),
        ("Stay vigilant; the work is never done", "Vigilance as vow.", "s20"),
     ]},
    {"id": "s19", "title": "Glenda's Funeral", "text": "Glenda dies, years later, of ordinary things. You give a short eulogy. Half the room has been in a hallway with her. You say, in the eulogy, what she always said: 'They will listen to you. They have to learn that.'",
     "choices": [
        ("Continue Glenda's calls and complaints", "Take the baton.", "s20"),
        ("Step back; let younger neighbors take it on", "Pass it forward.", "s20"),
     ]},
    {"id": "s20", "title": "The Drawer", "text": "You open the bottom drawer of your dresser. The black notebook is still there, edges soft. You weigh whether to keep it close or pass it on. Either way, you've already done the harder thing — you were there.",
     "choices": [
        ("Keep the notebook in the drawer", "Memory.", "end_legacy"),
        ("Give it to a neighbor who is starting hers", "Pass it on.", "end_vigil"),
     ]},
    {"id": "end_legacy", "title": "Footnote, Foundation", "text": "Your name lands in three policy footnotes and one foundation's annual report. You don't read them often. Your son grows up and becomes, against his own initial plan, a social worker. The notebook lives in a box in your closet. You sleep with the door unlocked, mostly.",
     "end": "Footnote, Foundation"},
    {"id": "end_vigil", "title": "Still Calling", "text": "You keep the phone numbers in a binder. When a neighbor asks for advice, you give it. When a new officer comes to the precinct, you go in and shake his hand and remember his face. Vigilance, you discover, is mostly just refusing to forget.",
     "end": "Still Calling"},
])


# ---------------------------------------------------------------------------
# Monarch: Legacy of Monsters — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
MONARCH = ({
    "id": "monarch-the-grandfather",
    "title": "Your Grandfather's Files",
    "sourceTitle": "Monarch: Legacy of Monsters",
    "kind": "show",
    "synopsis": "Your grandfather's basement contains seventeen file cabinets, a key to a Tokyo apartment, and a black-and-white photograph of him with a Titan. You inherit it all. Try to stay alive.",
    "releaseYear": 2024,
    "addedAt": "2026-04-24T00:00:00Z",
    "genre": "Sci-Fi",
    "tags": ["kaiju", "inheritance", "monarch"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Funeral", "text": "You inherit, alongside a paid-off mortgage and a sad fish, a box of files marked MONARCH — TOP SECRET. Your half-brother you didn't know existed sits across the church.",
     "choices": [
        ("Introduce yourself to him", "Family arrives unexpectedly.", "s2"),
        ("Walk past and read the files first", "Information first.", "s3"),
     ]},
    {"id": "s2", "title": "Half-Brother, Half-Stranger", "text": "Kentaro is your age, raised in Tokyo, equally surprised. He has half the photographs you have. The puzzle, you realize, was always meant to be two-handed.",
     "choices": [
        ("Compare files together immediately", "Trust before you've earned it.", "s4"),
        ("Buy him a drink first", "Person before project.", "s5"),
     ]},
    {"id": "s3", "title": "Page One", "text": "The first file is a map with a red circle around an island in the Pacific. The second is a casualty list — civilian, military, both. The third is a photograph of a creature that should not, by current physics, exist.",
     "choices": [
        ("Read every file before you act", "Discipline.", "s4"),
        ("Take the most actionable file and move", "Speed.", "s5"),
     ]},
    {"id": "s4", "title": "Tim, the Recruiter", "text": "A man in his thirties, polite, badly dressed, finds you at a coffee shop. 'Monarch wants to help,' he says. 'But you should be careful about who answers their phone right now.'",
     "choices": [
        ("Go with Tim to a Monarch safehouse", "Trust the org.", "s6"),
        ("Refuse and run with the files", "Trust no org.", "s7"),
     ]},
    {"id": "s5", "title": "The Apartment in Tokyo", "text": "Inside the apartment is a phone that still works, a kettle, and a wall covered in photographs of the same family — yours, at different decades. Your grandfather kept two lives.",
     "choices": [
        ("Photograph the wall for the record", "Document.", "s6"),
        ("Sit on the floor and let it hit you", "Feel it.", "s7"),
     ]},
    {"id": "s6", "title": "Lee Shaw, Old", "text": "Lee Shaw — your grandfather's old partner, supposedly dead, very alive — walks out of a back room in a leather coat. He looks at you, then Kentaro, then back. He says, 'You found me before they did.'",
     "choices": [
        ("Trust Shaw", "Old hands.", "s8"),
        ("Verify Shaw first", "Even old hands lie.", "s9"),
     ]},
    {"id": "s7", "title": "The Map Pin", "text": "On the wall there is a single new pin in a place that wasn't there in any other file — a pin in Kansas. Your grandfather was, somehow, tracking a Titan in Kansas. You don't know why.",
     "choices": [
        ("Go to Kansas", "Chase the new lead.", "s8"),
        ("Triangulate from Tokyo first", "Build the picture.", "s9"),
     ]},
    {"id": "s8", "title": "The Outpost", "text": "A small Monarch outpost outside a town that doesn't appear on highway maps. The team here is friendly and scared. They show you a tunnel that goes very, very far down.",
     "choices": [
        ("Descend with them", "Inside the world.", "s10"),
        ("Send Kentaro down; stay with the data", "Divide labor.", "s11"),
     ]},
    {"id": "s9", "title": "The Frequency", "text": "Shaw shows you a recording — Titan calls layered on top of each other. The pattern, he claims, is a language. Your grandfather had translated it partially. The files have the rest.",
     "choices": [
        ("Translate it together", "Tackle the hard problem.", "s10"),
        ("Take the recording to a linguist friend", "Outside expert.", "s11"),
     ]},
    {"id": "s10", "title": "First Encounter", "text": "Through a Hollow Earth tunnel: a Titan. Real. Large. Calm. It looks at you the way a dog looks at someone it has decided is not a threat. Its eye is the size of a small car.",
     "choices": [
        ("Sit still and let it pass", "Don't be a threat.", "s12"),
        ("Try to record its call", "Document.", "s13"),
     ]},
    {"id": "s11", "title": "The Apex Cinemas", "text": "Apex Cybernetics has, you discover, infiltrated Monarch's leadership. The company that wants to weaponize Titans is the company that just hired half your grandfather's old friends. The betrayal is, briefly, more painful than the kaiju.",
     "choices": [
        ("Plan to expose Apex", "Counter the corporation.", "s12"),
        ("Plan to undermine them from inside", "Subversion.", "s13"),
     ]},
    {"id": "s12", "title": "The Files Online", "text": "You upload your grandfather's files to a trusted journalist with a 48-hour fuse. If you're not heard from in 48, the files publish. It is the only insurance you have that isn't a Titan.",
     "choices": [
        ("Keep moving and rely on the fuse", "Bet on the press.", "s14"),
        ("Confront the saboteur in Monarch leadership", "Strike at the top.", "s15"),
     ]},
    {"id": "s13", "title": "The Hatchling", "text": "In a containment lab you find a small Titan — newborn, blue-eyed, frightened. Apex was going to weaponize it. The hatchling, you realize, has been responding to its mother's calls in the recordings Shaw played.",
     "choices": [
        ("Release the hatchling to its mother", "The right thing.", "s14"),
        ("Move it to a Monarch sanctuary", "The safe thing.", "s15"),
     ]},
    {"id": "s14", "title": "The Council Vote", "text": "Monarch's old families convene a council vote — keep the files secret, or release them. Your grandfather was the swing vote a generation ago. You are, terrifyingly, the swing vote now.",
     "choices": [
        ("Vote for release", "Daylight.", "s16"),
        ("Vote for limited disclosure", "Compromise.", "s17"),
     ]},
    {"id": "s15", "title": "Reunion", "text": "You and Kentaro stand at the mouth of a tunnel and watch the hatchling find its mother. The sound the mother Titan makes shakes the air. It is, somehow, joy.",
     "choices": [
        ("Stay in the work", "This is your inheritance.", "s16"),
        ("Hand the work to others and go home", "You did your part.", "s17"),
     ]},
    {"id": "s16", "title": "The Press Conference", "text": "A press conference releases redacted but real information about Monarch, Titans, and Apex. The world panics for a week and then, weirdly, adjusts. Humans are good at adjusting to the impossible. They always have been.",
     "choices": [
        ("Take a leadership role in the new public Monarch", "Build it openly.", "s18"),
        ("Step back to advisor", "Don't be the face.", "s19"),
     ]},
    {"id": "s17", "title": "The Family Dinner", "text": "Kentaro and his mother visit your home. Your own mother, baffled, sets six places. The dinner is — given the day — startlingly ordinary. You realize the inheritance was, partly, also a family.",
     "choices": [
        ("Make this a regular thing", "Build the family slowly.", "s18"),
        ("Take it one dinner at a time", "Don't force it.", "s19"),
     ]},
    {"id": "s18", "title": "Years Later", "text": "Monarch is, in the new public era, oversight more than secrecy. Titans are policy. You have testified before three legislatures. You sleep with the fish your grandfather kept — actually his great-grandfish — on the dresser.",
     "choices": [
        ("Stay in the public role", "Keep going.", "s20"),
        ("Hand off and write the family book", "Document.", "s20"),
     ]},
    {"id": "s19", "title": "The Map, Closing", "text": "You spend a year visiting every red pin on the original map. Some are empty. Some have new villages. Some have new Titans. You take photographs your grandfather would have wanted.",
     "choices": [
        ("Compile them into an archive", "Finish his work.", "s20"),
        ("Donate the originals to a museum", "Public memory.", "s20"),
     ]},
    {"id": "s20", "title": "Tokyo Apartment, Returned", "text": "You and Kentaro spend a week in the old Tokyo apartment going through the last drawers. You find the photograph he was holding the day he died — your grandmother, in a doorway, laughing. You decide which life to live next from this room.",
     "choices": [
        ("Stay public; the work calls", "Director's chair.", "end_public"),
        ("Go home and write the book together", "Authors.", "end_book"),
     ]},
    {"id": "end_public", "title": "Director", "text": "You become a director of public Monarch and, in a strange way, your grandfather's apprentice fifty years late. You preside over a small office full of files that no longer have to be hidden. You like that.",
     "end": "Director"},
    {"id": "end_book", "title": "The Family Book", "text": "You and Kentaro write a book together about the two lives of your grandfather. It is a strange book — half family memoir, half kaiju field guide. It sells, mysteriously, on every continent. Some readers cry. Some readers leave you weird voicemails. You answer most of them.",
     "end": "The Family Book"},
])


# ---------------------------------------------------------------------------
# Dhurandhar Part 2 — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
DHURANDHAR_2 = ({
    "id": "dhurandhar-2-the-return",
    "title": "The Return",
    "sourceTitle": "Dhurandhar: Part 2",
    "kind": "movie",
    "synopsis": "Three years after Karachi, you live in Lonavala under a name that isn't yours. A man you killed once is, apparently, alive. The agency needs you back. Your wife of paper says no.",
    "releaseYear": 2026,
    "addedAt": "2026-04-23T00:00:00Z",
    "genre": "Thriller",
    "tags": ["spy", "sequel", "return"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Lonavala, Morning", "text": "Mist over the hills. Chai from a kettle you bought three years ago. Rabia, who finally stayed, reading on the porch. Your phone, which is supposed to be cold, rings.",
     "choices": [
        ("Answer", "Old habits.", "s2"),
        ("Let it ring", "New life.", "s3"),
     ]},
    {"id": "s2", "title": "The Voice", "text": "A handler you've never met. 'Karachi never closed,' she says. 'We need you in Dubai by Thursday.' You realize you have, perhaps, been chosen because you're the only one left who saw the original handler's face.",
     "choices": [
        ("Agree to a meeting in Mumbai", "Hear them out.", "s4"),
        ("Refuse and hang up", "Boundaries.", "s5"),
     ]},
    {"id": "s3", "title": "Rabia, Watching", "text": "Rabia sees the phone, sees your face, knows. She sets her book down. 'You promised me,' she says, gently. 'I know,' you say, equally gently. The morning has, somehow, gotten older.",
     "choices": [
        ("Tell her you'll refuse", "Honor the promise.", "s4"),
        ("Tell her you need to hear them out", "Honesty, however hard.", "s5"),
     ]},
    {"id": "s4", "title": "Mumbai Cafe", "text": "Your new handler is in her forties, sharp, kind, terrified. The dossier she slides across the table includes your old cover wife's name on the wrong side of a ledger.",
     "choices": [
        ("Refuse and walk out", "Some triggers aren't yours.", "s6"),
        ("Demand the full operation brief", "Information before refusal.", "s7"),
     ]},
    {"id": "s5", "title": "The Old Asset", "text": "Khala Bhabhi, your old Karachi asset, somehow has your number. 'He's alive,' she says. 'And he has your wife's name.' Your wife, your real one, by paper.",
     "choices": [
        ("Move Rabia tonight", "Family first.", "s6"),
        ("Investigate the threat before moving", "Verify, then act.", "s7"),
     ]},
    {"id": "s6", "title": "Dubai, Forty-Eight Hours", "text": "You land in Dubai on a passport that has been very lightly used. The hotel room has good locks. The mission, briefly outlined, is to identify the man who survived the Karachi op three years ago.",
     "choices": [
        ("Take the mission and run it carefully", "Old skills.", "s8"),
        ("Run a counter-op of your own", "Trust nobody but yourself.", "s9"),
     ]},
    {"id": "s7", "title": "The Safe House, Lonavala", "text": "You move Rabia to a safe house two hills over. She is angry and competent. She does, in fact, know exactly how to disappear — she did it before.",
     "choices": [
        ("Take her with you to Dubai", "Asset and family.", "s8"),
        ("Leave her safe; go alone", "Compartmentalize.", "s9"),
     ]},
    {"id": "s8", "title": "Tariq, Alive", "text": "Tariq — the man you were sure you killed — is in a Dubai gym at noon. He sees you. He smiles, sadly. He approaches you in the parking lot with empty hands and says, 'I wanted to apologize.'",
     "choices": [
        ("Hear him out", "Even ghosts speak.", "s10"),
        ("Take him into custody", "Process first.", "s11"),
     ]},
    {"id": "s9", "title": "The Counter-Op", "text": "You set up your own circle — Khala Bhabhi in Karachi, a stringer in Dubai, your old handler (the one who survived, secretly), and Rabia as your operational mind. Suddenly you have a team that does not, on paper, exist.",
     "choices": [
        ("Run it as a private circle", "Private justice.", "s10"),
        ("Use it to clean your name with the agency", "Negotiate after.", "s11"),
     ]},
    {"id": "s10", "title": "The Apology", "text": "Tariq tells you that he was, for a year, the asset of a third country you didn't know was in this game. He has been wanting to defect ever since. He has documents.",
     "choices": [
        ("Believe him and exfil him", "Asset acquisition.", "s12"),
        ("Verify his documents first", "Trust verifies.", "s13"),
     ]},
    {"id": "s11", "title": "The Third Country", "text": "Your stringer flips a server log: the third country running the original Karachi op was a 'friendly' power. The betrayal is, professionally, more interesting than personal. The agency has, you realize, been lied to too.",
     "choices": [
        ("Take the evidence to the agency", "Inside fix.", "s12"),
        ("Take it to a journalist for outside pressure", "Outside fix.", "s13"),
     ]},
    {"id": "s12", "title": "Rabia in the Field", "text": "Rabia, somehow, becomes the operational steady. She is faster than you in places you were too tired to be fast in. You realize she has been, all along, more than your cover. She is good at this.",
     "choices": [
        ("Make her your official partner", "Honest team.", "s14"),
        ("Keep her work informal — protect her record", "Compartmental.", "s15"),
     ]},
    {"id": "s13", "title": "Khala Bhabhi's Plan", "text": "Khala Bhabhi outlines a long con — six months, in three cities, to make the third country's network publicly visible. She has been waiting, she says, for a man like you to do it with.",
     "choices": [
        ("Commit to the six-month con", "Long game.", "s14"),
        ("Commit only to phase one", "Stage it.", "s15"),
     ]},
    {"id": "s14", "title": "The Exposure", "text": "Six months later the network is, by every careful measurement, exposed — across three countries, two intelligence services, and one very embarrassing newspaper. You and Rabia did most of it from a kitchen in Lonavala.",
     "choices": [
        ("Stay in the work, on your terms", "Continue.", "s16"),
        ("Cash out fully and disappear", "Done.", "s17"),
     ]},
    {"id": "s15", "title": "The Lonavala House", "text": "You and Rabia retreat to the original house. The cat next door has, in your absence, adopted you. Tariq, exfiltrated, sends a postcard from Lisbon. He's painting, badly. You both laugh.",
     "choices": [
        ("Take Tariq's offer to visit Lisbon", "Friendship across borders.", "s16"),
        ("Stay in Lonavala for the season", "Settle.", "s17"),
     ]},
    {"id": "s16", "title": "The Lisbon Visit", "text": "Lisbon in spring. Tariq's paintings are, you confirm, very bad. He cooks for you. You realize, in his kitchen, that you have not been a guest in a friend's home in twenty years.",
     "choices": [
        ("Stay in Europe a while", "Take the air.", "s18"),
        ("Return home enriched but unchanged", "Take the memory.", "s19"),
     ]},
    {"id": "s17", "title": "The Garden", "text": "You and Rabia plant a small garden behind the Lonavala house. It is not symbolism. It is just a garden. The neighbors don't know your real name. They love you anyway.",
     "choices": [
        ("Keep the garden small and yours", "Boundaries.", "end_garden"),
        ("Invite a young handler to learn", "Pass it on.", "end_mentor"),
     ]},
    {"id": "s18", "title": "Three Languages", "text": "You and Rabia spend a year between Lisbon, Istanbul, and Lonavala. You learn to be tourists. You realize, late, that it's possible to live in countries you previously only entered.",
     "choices": [
        ("Make Lisbon a real home half the year", "Build the dual life.", "s21"),
        ("Come fully home", "Choose one.", "s21"),
     ]},
    {"id": "s19", "title": "The Memoir, Unpublished", "text": "You write a memoir nobody will read. It is, for you, the closing argument of a career. Rabia edits. Tariq sends a chapter from his own attempt at one in Portuguese. Your memoir is, in the end, mostly an act of paying attention.",
     "choices": [
        ("Burn the manuscript", "Some closings are private.", "s21"),
        ("Lock it in a vault for fifty years", "Some closings are for grandchildren.", "s21"),
     ]},
    {"id": "s21", "title": "The Last Decision", "text": "Rabia and you sit on the porch in Lonavala with two cups going cold. You weigh the shape of the rest of it — garden, two homes, or a quiet mentor's chair for the next handler the agency sends.",
     "choices": [
        ("Keep the porch and nothing else", "Smallest life.", "end_garden"),
        ("Teach the next handler", "Pass the craft.", "end_mentor"),
        ("Live the half-year in Lisbon", "Two kitchens.", "end_two_homes"),
     ]},
    {"id": "end_garden", "title": "Lonavala, Year Round", "text": "You live in Lonavala, full time, with Rabia and a cat. You learn the names of every neighbor. You walk the same loop every morning. You sleep well. You have, against every odd in your file, retired.",
     "end": "Lonavala, Year Round"},
    {"id": "end_mentor", "title": "The Young Handler", "text": "A young woman from the agency, sent reluctantly, comes for tea. You teach her what you can. She comes back the next month. And the one after that. You become, in your sixties, what your old handler was supposed to be — patient, kind, devastatingly useful.",
     "end": "The Young Handler"},
    {"id": "end_two_homes", "title": "Two Kitchens", "text": "Half the year Lisbon. Half the year Lonavala. You and Rabia get to know two sets of bakers, two sets of postmen, two ways of being. You realize the spy life trained you for, of all things, the present tense.",
     "end": "Two Kitchens"},
])


# ---------------------------------------------------------------------------
# Young Sheldon — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
YOUNG_SHELDON = ({
    "id": "young-sheldon-science-fair",
    "title": "The Science Fair Problem",
    "sourceTitle": "Young Sheldon",
    "kind": "show",
    "synopsis": "You're nine, Texan, and smarter than your physics teacher. The county science fair is in two weeks. So is your sister's volleyball game. You have to be in two places. Use your brain.",
    "releaseYear": 2024,
    "addedAt": "2026-04-22T00:00:00Z",
    "genre": "Comedy",
    "tags": ["family", "prodigy", "small-town"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Monday Breakfast", "text": "Meemaw makes pancakes. Mary makes coffee. Georgie eats his weight in bacon. Missy reminds everyone — twice — about her championship game. You are, as usual, calculating something at the table.",
     "choices": [
        ("Announce your science fair project at breakfast", "Set the room's stakes.", "s2"),
        ("Wait until Dad is in the room", "Strategy in audiences.", "s3"),
     ]},
    {"id": "s2", "title": "The Project Idea", "text": "You propose a low-cost neutrino-detection experiment in the family garage. Mary blinks. Meemaw says, 'Oh, sweetie.' Georgie asks if it has anything to do with bowling.",
     "choices": [
        ("Pivot to something doable in a garage", "Constraints are also creativity.", "s4"),
        ("Insist on the original idea", "Vision.", "s5"),
     ]},
    {"id": "s3", "title": "Dad's Practice", "text": "George Sr. is at football practice. You walk down with a thermos. He asks how school is. You tell him about Newton's third law. He says, 'Sounds good, buddy.' You feel, briefly, that he listens harder than he lets on.",
     "choices": [
        ("Pitch the science fair project to him", "Dad first.", "s4"),
        ("Ask him about the volleyball schedule first", "Sister first.", "s5"),
     ]},
    {"id": "s4", "title": "Tam's Plan", "text": "Tam, your best friend, sees your project sketch at lunch and immediately offers to help. He has, he claims, 'a guy at the radio shack.' He always has a guy.",
     "choices": [
        ("Form a two-person team", "Allies.", "s6"),
        ("Keep it solo for purity", "Independent work.", "s7"),
     ]},
    {"id": "s5", "title": "Missy's Suspicion", "text": "Missy, sharper than anyone gives her credit for, asks if you're scheduling your fair around her game. You consider lying. You consider not lying. You consider the third option, which is silence.",
     "choices": [
        ("Tell her the truth", "Sister code.", "s6"),
        ("Promise to be at her game no matter what", "Promise first, plan after.", "s7"),
     ]},
    {"id": "s6", "title": "Mr. Lundy's Permission", "text": "Mr. Lundy — your physics teacher — needs to sign off on your project. He is, sweetly, intimidated by you. You realize you can either smooth this with kindness or steamroll him.",
     "choices": [
        ("Compliment a real strength of his", "Kindness as strategy.", "s8"),
        ("Present the project as if you're the teacher", "Authority.", "s9"),
     ]},
    {"id": "s7", "title": "Meemaw's Garage", "text": "Meemaw lets you set up in her garage with two conditions: no fires, and you have to take a snack break every two hours. The snacks include a Dr Pepper she will share, even though she always says she won't.",
     "choices": [
        ("Negotiate longer work blocks", "Optimize.", "s8"),
        ("Accept her conditions exactly", "Respect.", "s9"),
     ]},
    {"id": "s8", "title": "The Wiring Problem", "text": "Saturday morning. The detector's preamp keeps oscillating. You consider the problem. The problem considers you. Georgie offers to 'hit it.'",
     "choices": [
        ("Methodically debug", "Discipline.", "s10"),
        ("Let Georgie hit it", "Sometimes pets are right.", "s11"),
     ]},
    {"id": "s9", "title": "The Family Schedule", "text": "You draw a Gantt chart on the kitchen wall. Mary makes you take it down. You redraw it on a poster board and prop it against the wall. She accepts the compromise. You add Missy's volleyball as a critical milestone.",
     "choices": [
        ("Show Missy the chart with her name first", "Respect her.", "s10"),
        ("Show the chart to Dad for buy-in", "Build authority.", "s11"),
     ]},
    {"id": "s10", "title": "Pastor Jeff Visits", "text": "Pastor Jeff drops by for tea and to subtly check whether your project is, technically, blasphemous. You explain particle physics with charm. He leaves with a flyer for your fair and a slightly worried expression.",
     "choices": [
        ("Invite him as a judge", "Diplomacy.", "s12"),
        ("Keep the church gently at arm's length", "Boundaries.", "s13"),
     ]},
    {"id": "s11", "title": "The Sleepless Tuesday", "text": "You stay up too late three nights in a row. Meemaw catches you. She sits in the garage with you anyway and reads the newspaper while you solder. She says nothing, except, 'You're like your daddy when he had something to prove.'",
     "choices": [
        ("Sleep at a reasonable hour from now on", "Take the lesson.", "s12"),
        ("Keep pushing — fair is in three days", "Sprint.", "s13"),
     ]},
    {"id": "s12", "title": "Missy's Game, Friday", "text": "The volleyball game is Friday at 7. The fair is Saturday at 9. The schedule, miraculously, allows for both. You make it to the game with a notebook in your hand. Missy spots you in the stands.",
     "choices": [
        ("Close the notebook for the whole game", "Be present.", "s14"),
        ("Keep glancing at notes between sets", "Compromise.", "s15"),
     ]},
    {"id": "s13", "title": "Dad's Quiet Help", "text": "George Sr., who you didn't know noticed, shows up at the garage at 9 p.m. with a roll of duct tape and zero physics. He holds the wire steady while you solder. He says, 'I'm here. That's all I got.' It is, oddly, all you needed.",
     "choices": [
        ("Thank him directly", "Tell him.", "s14"),
        ("Nod and keep working", "Some thanks are silent.", "s15"),
     ]},
    {"id": "s14", "title": "Saturday Morning", "text": "The fair. Folding tables. Other kids' baking-soda volcanoes. Your detector hums politely. The county judge, who has a Ph.D. in something else but knows physics when she sees it, leans in.",
     "choices": [
        ("Demo the detector with no shortcuts", "Be honest about your data.", "s16"),
        ("Demo with the dramatic flourish you've practiced", "Showmanship.", "s17"),
     ]},
    {"id": "s15", "title": "The Awkward Question", "text": "A different judge — an older man — asks you a question you suspect is meant to trip you up. You realize, mid-answer, that he is testing for confidence as much as content.",
     "choices": [
        ("Answer plainly and concisely", "Don't show off.", "s16"),
        ("Answer with proof and humor", "Be your full self.", "s17"),
     ]},
    {"id": "s16", "title": "The Ribbon", "text": "You win the county. The ribbon is blue and cheap and you put it on your refrigerator next to Missy's championship pennant from last night. The fridge, you decide, is a kind of family altar.",
     "choices": [
        ("Aim for the state fair next month", "Keep going.", "s18"),
        ("Take a week off before the next thing", "Rest.", "s19"),
     ]},
    {"id": "s17", "title": "Tam's Speech", "text": "Tam, at lunch on Monday, gives a small speech about how you didn't ditch him for credit. You blink. You hadn't realized the choice was a choice. Friendship, you discover, has options you didn't see.",
     "choices": [
        ("Tell him you'll always include him", "Vow.", "s18"),
        ("Promise to choose better, on purpose", "Specific vow.", "s19"),
     ]},
    {"id": "s18", "title": "The State Fair Letter", "text": "An envelope arrives — the state fair, with a small stipend. Mary cries a little. Meemaw cries a lot. Dad pretends not to. Missy says, 'Cool,' which is, from her, the highest honor.",
     "choices": [
        ("Take the family with you to state", "Bring them along.", "s20"),
        ("Take just Tam", "Honor the partner.", "s20"),
     ]},
    {"id": "s19", "title": "Sunday Pancakes", "text": "Sunday after the fair, Meemaw makes pancakes that are, somehow, even better than usual. You eat three. You watch your family argue about a Cowboys game. You realize, with a feeling you can't yet name, that you are happy.",
     "choices": [
        ("Stay at the table an extra hour", "Be present.", "s20"),
        ("Go work on the next project before noon", "Curiosity, called.", "s20"),
     ]},
    {"id": "s20", "title": "The Hallway, Quiet", "text": "After the fair, after the pancakes, you stand in the hallway with the ribbon in your hand and decide whose company state will be. The decision is, you realize, also a decision about who you want next to you when the next door opens.",
     "choices": [
        ("Pile in the station wagon together", "Family.", "end_family"),
        ("Just you and Tam, partners", "Friendship.", "end_tam"),
        ("Already plan tomorrow's experiment", "Science calls.", "end_science"),
     ]},
    {"id": "end_family", "title": "Cooper, the Family", "text": "You go to state with Mom and Dad and Meemaw and Missy and Georgie. The trip is loud, chaotic, and one of the best weekends of your childhood. You realize, again, that science is a profession but family is a country.",
     "end": "Cooper, the Family"},
    {"id": "end_tam", "title": "Cooper & Tam", "text": "You and Tam go to state, sharing a hotel room and a stipend. You stay up late watching TV that isn't on at your house. You win second. You don't mind. Tam tells the story for years.",
     "end": "Cooper & Tam"},
    {"id": "end_science", "title": "The Long Road", "text": "Years later, in graduate school, you'll think back to this Saturday. You'll remember the ribbon and the fridge and the volleyball game. You'll realize, with a small ache, that the science was always going to happen — the choice was who you would be while it did.",
     "end": "The Long Road"},
])


# ---------------------------------------------------------------------------
# Heartbreak High — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
HEARTBREAK_HIGH = ({
    "id": "heartbreak-high-the-map",
    "title": "The Map",
    "sourceTitle": "Heartbreak High",
    "kind": "show",
    "synopsis": "You made a map of every romantic and sexual connection at your Sydney high school. It got out. Now the school wants you in 'sexual literacy' — and several relationships, including yours, want a word.",
    "releaseYear": 2025,
    "addedAt": "2026-04-21T00:00:00Z",
    "genre": "Drama",
    "tags": ["teen", "queer", "Sydney"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Monday, Pre-Assembly", "text": "The map, drawn in marker, occupies an entire toilet wall. Lines connect names you barely thought about and names you most certainly did. The principal's heels click down the hallway. You have three minutes.",
     "choices": [
        ("Take photos of the map first", "Document the chaos you made.", "s2"),
        ("Try to scrub it before assembly", "Damage control.", "s3"),
     ]},
    {"id": "s2", "title": "Your Best Friend Quinni", "text": "Quinni sees you with the camera. She doesn't judge. She does, helpfully, point out that you spelled three names wrong. Friendship like Quinni's is rare and you do not deserve it.",
     "choices": [
        ("Apologize to Quinni for involving her", "Friendship over scoops.", "s4"),
        ("Recruit Quinni to help you fix it", "Practical first.", "s5"),
     ]},
    {"id": "s3", "title": "Principal Stacy", "text": "Principal Stacy stares at the map for a long minute. Then she looks at you. 'My office,' she says, evenly. 'And bring whichever friend convinced you the marker was washable.'",
     "choices": [
        ("Take Quinni with you", "Backup.", "s4"),
        ("Go alone — own it", "Solo.", "s5"),
     ]},
    {"id": "s4", "title": "Sexual Literacy Tutorial", "text": "The new mandatory class is called 'SLT' by the school and 'SLuTs' by everyone else. The teacher is well-intentioned and overwhelmed. The class is, of course, the exact people you mapped.",
     "choices": [
        ("Participate honestly", "Lean in.", "s6"),
        ("Sit at the back with Quinni and Darren", "Survive.", "s7"),
     ]},
    {"id": "s5", "title": "Malakai, Hurt", "text": "Malakai, your maybe-boyfriend, finds you at lunch. 'I'm on the map twice,' he says. 'Did you not notice or not care?' You realize you didn't actually know about the second line until you re-read it.",
     "choices": [
        ("Apologize fully", "Own the harm.", "s6"),
        ("Explain the map's intent", "Context as defense.", "s7"),
     ]},
    {"id": "s6", "title": "Darren's Take", "text": "Darren, equal parts dramatic and wise, says, 'You made the map because you wanted everyone to admit they're connected. The school doesn't want them to.' Darren is right, as usual.",
     "choices": [
        ("Lean into Darren's framing", "Politicize it.", "s8"),
        ("Lean away — you didn't mean it to be political", "De-escalate.", "s9"),
     ]},
    {"id": "s7", "title": "Amerie's Detention", "text": "You and Quinni share a detention with three people you mapped. The conversation, surprisingly, gets honest. You discover the map left out a connection that, in person, is obvious.",
     "choices": [
        ("Add the connection to a mental version", "Stay curious.", "s8"),
        ("Decide the map was a bad idea entirely", "Reconsider.", "s9"),
     ]},
    {"id": "s8", "title": "The Walkout", "text": "Students stage a walkout — not, technically, because of you. Then it kind of becomes because of you. The local news has a microphone in your face. Principal Stacy has a vein in her forehead.",
     "choices": [
        ("Speak to the news, briefly", "Take responsibility publicly.", "s10"),
        ("Walk past the news in solidarity", "Action over interview.", "s11"),
     ]},
    {"id": "s9", "title": "Spider's Apology", "text": "Spider — boy, dumb, mostly — apologizes for the comment that started a fight last week. He is, briefly, a person. You realize the map, accidentally, gave him a way to think about himself.",
     "choices": [
        ("Accept his apology", "Allow change.", "s10"),
        ("Tell him to apologize to the actual people he hurt", "Redirect.", "s11"),
     ]},
    {"id": "s10", "title": "Malakai's Choice", "text": "Malakai, on a bench by the courts, tells you he doesn't want to be a project. He wants to be a boyfriend. You realize the two are not separable for you yet, and that this is a problem.",
     "choices": [
        ("Choose the boyfriend part for now", "Commit.", "s12"),
        ("Be honest that you can't yet", "Honesty hurts cleaner.", "s13"),
     ]},
    {"id": "s11", "title": "Quinni's Burnout", "text": "Quinni, who hates loud places and loud weeks, has had enough. She skips school. You find her at the planetarium. You sit beside her in the dark while a recorded voice describes Saturn.",
     "choices": [
        ("Skip the rest of the week with her", "Friendship over school.", "s12"),
        ("Promise to take fewer of her spoons", "Mindful.", "s13"),
     ]},
    {"id": "s12", "title": "Sasha's Counter-Project", "text": "Sasha, who lives on righteous causes, organizes a 'Connection Festival' to claim the map's energy for queer joy. You realize, with a complicated feeling, that the work you started has gotten away from you and become better.",
     "choices": [
        ("Help organize the festival", "Lean into the better version.", "s14"),
        ("Step back and let it be theirs", "Generosity.", "s15"),
     ]},
    {"id": "s13", "title": "Your Mom Knocks", "text": "Your mom — too cool, too tired — knocks on your door at 11. She heard about the map from another mum. She doesn't yell. She makes tea. She asks if you've been okay, actually, lately.",
     "choices": [
        ("Tell her the truth about the year", "Adult conversation.", "s14"),
        ("Promise her a longer talk on Saturday", "Schedule the honesty.", "s15"),
     ]},
    {"id": "s14", "title": "The Festival Night", "text": "Lights strung between the basketball hoops. Music from someone's brother's DJ rig. The map, redrawn by Sasha, is now a giant mural and includes everyone's pronouns and a few jokes only your year understands.",
     "choices": [
        ("Dance, fully, without your phone", "Be present.", "s16"),
        ("Sit on the bleachers with Quinni and Darren", "Quieter joy.", "s17"),
     ]},
    {"id": "s15", "title": "End of Term", "text": "Reports come out. The school will not, after all, expel you. Principal Stacy writes a note in pencil: 'You have a knack for systems. Use it.' You will, you think, take her advice.",
     "choices": [
        ("Apply for the school newspaper editor role next term", "Use the knack.", "s16"),
        ("Take a term off everything official", "Recover.", "s17"),
     ]},
    {"id": "s16", "title": "Year Twelve", "text": "Year twelve begins. Quinni runs for SRC. Darren auditions for a play that is, secretly, also a coming-out. Malakai sends you a letter that is, in handwriting, a real letter. You are, against the odds, hopeful.",
     "choices": [
        ("Throw yourself into year twelve fully", "Commit.", "s18"),
        ("Take it one term at a time", "Pace yourself.", "s18"),
     ]},
    {"id": "s17", "title": "Beach Day", "text": "On the last day of term you and Quinni and Darren and Sasha and Malakai end up at Bondi at sunset for no good reason. Someone has chips. Someone has a bluetooth speaker that only plays one song.",
     "choices": [
        ("Take a group photo for the year", "Preserve the moment.", "s19"),
        ("Just live the moment, no photo", "Be there.", "s19"),
     ]},
    {"id": "s18", "title": "Parent-Teacher Night", "text": "The night your mum and you go to the parent-teacher evening you both pretend to be normal. Mr. Pavlovic says, quietly, that you have a gift for writing. Your mum holds your shoulder. You realize the year is starting in earnest.",
     "choices": [
        ("Take the writing track seriously", "Aim.", "s20"),
        ("Keep it just as a hobby", "Quiet.", "s20"),
     ]},
    {"id": "s19", "title": "Sasha's Festival, Round Two", "text": "Sasha announces a second Connection Festival. You all help. The school, having learned, gives them the gym this time. The night is louder, kinder, and full of someone's bluetooth speaker playing exactly one song.",
     "choices": [
        ("Dance for the whole festival", "Joy.", "s20"),
        ("Sit and watch your people be happy", "Witness.", "s20"),
     ]},
    {"id": "s20", "title": "Last Bell", "text": "The final bell of year twelve. The whole map of who-knew-who tilts into the future. You stand in the courtyard one last time and choose what kind of leaving you'll have.",
     "choices": [
        ("Throw yourself into the next year", "Loud goodbye.", "end_year12"),
        ("Take the slow walk out", "Quiet goodbye.", "end_pace"),
        ("Take one last photo of the gang", "Save it.", "end_photo"),
     ]},
    {"id": "end_year12", "title": "Year Twelve, Loud", "text": "You become the editor of the school paper. You write a column called 'Connections.' You graduate with a portfolio that gets you into a journalism program. Years later you make a podcast that is, in a real sense, the map grown up.",
     "end": "Year Twelve, Loud"},
    {"id": "end_pace", "title": "Slow Year, Real Year", "text": "You take it term by term and survive year twelve without being a story about year twelve. Quinni helps. Darren makes you laugh. Malakai, eventually, becomes the friend he was supposed to be. You graduate quietly, fully, ready.",
     "end": "Slow Year, Real Year"},
    {"id": "end_photo", "title": "The Photo on the Fridge", "text": "The photo lives on your fridge for a decade. Different versions of you pass it. None of them know yet how good a year that was. You do.",
     "end": "The Photo on the Fridge"},
])


# ---------------------------------------------------------------------------
# Imperfect Women — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
IMPERFECT_WOMEN = ({
    "id": "imperfect-women-the-friendship",
    "title": "Three Friends, One Truth",
    "sourceTitle": "Imperfect Women",
    "kind": "show",
    "synopsis": "Eleanor was your best friend for twenty years. She's been murdered. You and Mary, the third friend, each know exactly half of the secret that killed her. You have to decide whether to tell each other.",
    "releaseYear": 2024,
    "addedAt": "2026-04-20T00:00:00Z",
    "genre": "Drama",
    "tags": ["friendship", "grief", "secrets"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Call", "text": "Mary calls at 6:14 a.m. crying. You sit on the edge of the bed and hear the sentence 'Eleanor is dead' and your husband, beside you, does not yet know. The clock keeps moving.",
     "choices": [
        ("Wake your husband", "Family first.", "s2"),
        ("Get dressed and go to Mary immediately", "Friend first.", "s3"),
     ]},
    {"id": "s2", "title": "His Reaction", "text": "Your husband Robert reacts in a way that is one ratchet off from what you expected. He is sad. He is also, in a way you can't name, alert.",
     "choices": [
        ("Notice the alertness", "Trust the gut.", "s4"),
        ("Ignore it; he loved Eleanor", "Don't make stories yet.", "s5"),
     ]},
    {"id": "s3", "title": "Mary's Kitchen", "text": "Mary, at her counter, hands you a coffee with the same chip in the mug she's had since college. She says, before you can speak, 'I knew about Eleanor and someone. I just didn't know who.'",
     "choices": [
        ("Ask her who she suspected", "Demand the half-secret.", "s4"),
        ("Tell her your half first", "Trade truths.", "s5"),
     ]},
    {"id": "s4", "title": "The Affair Half", "text": "Eleanor had been having an affair for the last year. You knew because she told you. You don't know with whom. Mary, you suspect, knew the man's name but didn't know it was Eleanor.",
     "choices": [
        ("Tell Mary the affair half now", "Symmetrical truth.", "s6"),
        ("Wait to see what Mary volunteers", "Information is power.", "s7"),
     ]},
    {"id": "s5", "title": "The Money Half", "text": "Eleanor had been managing money — yours, Mary's, hers — and you'd noticed a discrepancy two months ago. You'd been planning to ask her about it the day she died. The half-secret is, somehow, becoming whole.",
     "choices": [
        ("Tell Mary about the money", "Honesty.", "s6"),
        ("Hold the money for now; the affair feels closer to motive", "Triage.", "s7"),
     ]},
    {"id": "s6", "title": "The Detective", "text": "Detective Kapoor is kind, careful, slow. She asks you both about Eleanor's life in the past year. She has noticed, you can tell, the small inconsistency between your accounts.",
     "choices": [
        ("Trust her with the affair half", "Truth.", "s8"),
        ("Trust her with the money half", "Truth.", "s9"),
     ]},
    {"id": "s7", "title": "The Husband, Nathan", "text": "Eleanor's husband Nathan sits in his kitchen looking smaller than you remember. He says he didn't know about the affair. He says it twice. He looks at you the second time.",
     "choices": [
        ("Believe him", "He's grieving.", "s8"),
        ("Watch him more closely", "Doubt has its own work.", "s9"),
     ]},
    {"id": "s8", "title": "The Daughter", "text": "Eleanor's seventeen-year-old, Sophie, asks you, in the back garden, if you knew her mother was unhappy. You realize, again, that 'mother' and 'friend' are different people you each knew.",
     "choices": [
        ("Tell Sophie what you knew", "Honor the daughter.", "s10"),
        ("Tell Sophie that her mother loved her", "Lead with the kindest truth.", "s11"),
     ]},
    {"id": "s9", "title": "Robert, Out", "text": "Your husband Robert is, conveniently, out late three nights running. He says it's work. The shoes by the door, when he comes home, are wet. It hasn't rained.",
     "choices": [
        ("Follow Robert one night", "Investigate at home.", "s10"),
        ("Ask Mary if she's noticed the same about her husband", "Compare.", "s11"),
     ]},
    {"id": "s10", "title": "The Photo", "text": "On Eleanor's phone, recovered after a week, is a photo of a hotel-room ceiling. The angle is innocuous to anyone who doesn't know the ceiling. You know the ceiling.",
     "choices": [
        ("Tell Mary you recognize the ceiling", "Truth to friend.", "s12"),
        ("Tell Detective Kapoor", "Truth to law.", "s13"),
     ]},
    {"id": "s11", "title": "Mary's Husband", "text": "Mary, slowly, admits that her husband Tom has been distant for months. Tom and Robert and Nathan all go to the same gym. The gym is, you realize, three suburbs away from any of their homes.",
     "choices": [
        ("Plan to confront the husbands together", "United front.", "s12"),
        ("Each speak to your own first", "Personal first.", "s13"),
     ]},
    {"id": "s12", "title": "The Garage Conversation", "text": "You and Mary corner Robert and Tom in Robert's garage on a Saturday morning. The truth comes out in stages — yes, an affair, no, with one of them, no, neither knew Eleanor would be killed.",
     "choices": [
        ("Believe the parts that exonerate them", "Friend is also wife.", "s14"),
        ("Disbelieve until proven", "Marriage is also evidence.", "s15"),
     ]},
    {"id": "s13", "title": "Detective Kapoor's Case", "text": "Kapoor calls you in for a quiet meeting. She has, she says, narrowed it. She tells you a name. The name is on neither half of your secret. The room moves.",
     "choices": [
        ("Help her gather what she needs", "Cooperate fully.", "s14"),
        ("Take a breath before responding", "Don't speak fast.", "s15"),
     ]},
    {"id": "s14", "title": "The Arrest", "text": "An arrest is made. The killer is, almost mundanely, a stranger Eleanor had been planning to leave the marriage for — and who had been planning, in his own ugly way, to leave her too. The motive is small and the loss is enormous.",
     "choices": [
        ("Attend the trial through to verdict", "Stand for Eleanor.", "s16"),
        ("Step back; protect your own family", "Personal first.", "s17"),
     ]},
    {"id": "s15", "title": "The Marriage Counseling", "text": "You and Robert sit with a therapist for the first time in your marriage. The truth about his Tuesdays comes out. It is not an affair. It is a less interesting and more painful answer: he has been visiting a sponsor at AA.",
     "choices": [
        ("Apologize fully", "Marriage as repair.", "s16"),
        ("Ask why he kept it secret", "Repair requires questions.", "s17"),
     ]},
    {"id": "s16", "title": "Mary and You", "text": "Mary and you, after, walk every Sunday for a year. You don't talk about Eleanor every walk. You talk about her enough. The friendship that was three is, slowly, two. The two is, sometimes, enough.",
     "choices": [
        ("Make Sundays a permanent ritual", "Vows of two.", "s18"),
        ("Bring Sophie sometimes", "Three again, differently.", "s19"),
     ]},
    {"id": "s17", "title": "Your Daughter, Listening", "text": "Your own daughter, fifteen, asks you to teach her how to be a friend like you are friends. You sit on the porch and try to think of an answer that isn't a Hallmark card. You tell her, eventually, 'Tell each other things first.'",
     "choices": [
        ("Model that for her with your own friends", "Show.", "s18"),
        ("Send her to call her best friend now", "Direct.", "s19"),
     ]},
    {"id": "s18", "title": "Sophie's University", "text": "Sophie's university acceptance arrives on a Tuesday. You and Mary throw her a party. She gives a small speech and thanks you both. You realize, with a feeling that is both grief and gratitude, that Eleanor is in this room.",
     "choices": [
        ("Tell Sophie about her mother's good qualities", "Memory as gift.", "s20"),
        ("Sit beside Mary and just let it be", "Presence.", "s20"),
     ]},
    {"id": "s19", "title": "The Anniversary", "text": "One year after Eleanor died you and Mary and Nathan and Sophie all eat dinner at the same restaurant Eleanor loved. The food is fine. The night is full of stories you'd forgotten. You laugh more than you cry. Eleanor would, you realize, approve.",
     "choices": [
        ("Make this the new tradition", "Build the ritual.", "s20"),
        ("Let it be a one-time thing", "Some moments belong to once.", "s20"),
     ]},
    {"id": "s20", "title": "The Photograph on the Wall", "text": "Years on, you stop at a photograph of the three of you from a college trip. You realize you don't flinch anymore. You realize you can hold both sadness and gratitude in the same hand. You choose what to do with that hand next.",
     "choices": [
        ("Hand it to Sophie", "Pass it on.", "end_sophie"),
        ("Keep it on your own wall and call Mary", "Pair of twos.", "end_two"),
     ]},
    {"id": "end_sophie", "title": "Sophie's Aunts", "text": "You and Mary become Sophie's aunts in a real, unofficial way. You attend her graduation. You attend her wedding. At her wedding she names a child after Eleanor. You both cry without performing it.",
     "end": "Sophie's Aunts"},
    {"id": "end_two", "title": "Sunday Walks", "text": "You and Mary walk for the next thirty years. You bury parents and welcome grandchildren. You speak of Eleanor often, then less often, then often again in the way grief loops. The friendship, in the end, is the answer to the question her death almost asked.",
     "end": "Sunday Walks"},
])


# ---------------------------------------------------------------------------
# Sebastian — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
SEBASTIAN = ({
    "id": "sebastian-the-research",
    "title": "Field Notes",
    "sourceTitle": "Sebastian",
    "kind": "movie",
    "synopsis": "You're a young writer in London with a novel that won't sell. To finish it, you start escorting under a name that isn't yours. You promise yourself you can write your way back out.",
    "releaseYear": 2024,
    "addedAt": "2026-04-19T00:00:00Z",
    "genre": "Drama",
    "tags": ["sex work", "writing", "London"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Profile", "text": "You set up the profile under 'Sebastian.' Mostly truthful. Mostly flattering. You write your novel's protagonist into the bio. Within an hour, three messages.",
     "choices": [
        ("Reply to the first carefully", "Curiosity, careful.", "s2"),
        ("Reply to a safer-seeming one", "Risk management.", "s3"),
     ]},
    {"id": "s2", "title": "The First Client", "text": "A man in his fifties, polite, nervous. He talks about his ex-wife. You take, mentally, the smallest possible notes. He pays in cash. He thanks you. You walk home with seventy pounds and a stomach that has not decided how it feels.",
     "choices": [
        ("Write the scene tonight", "Capitalize on the rawness.", "s4"),
        ("Wait a week before writing", "Distance.", "s5"),
     ]},
    {"id": "s3", "title": "Helen, the Editor", "text": "Your literary agent, Helen, calls. She wants to know what you're working on. You tell her the truth in a careful sentence. She is silent. Then she says, 'Be careful. Be specific. Don't lie to yourself about it.'",
     "choices": [
        ("Send Helen a chapter immediately", "Make her your sounding board.", "s4"),
        ("Keep Helen in the dark for the first draft", "Protect the work.", "s5"),
     ]},
    {"id": "s4", "title": "Your Day Job", "text": "You are also, technically, a junior writer at a magazine. Your colleague Amna notices you have been very tired. She asks if you are okay. You say yes. You say it slightly too quickly.",
     "choices": [
        ("Tell Amna the truth", "Friend.", "s6"),
        ("Tell her you're just sleep-deprived", "Cover.", "s7"),
     ]},
    {"id": "s5", "title": "The Client Who Reads", "text": "A regular — an academic in his sixties — recognizes your debut short story collection. 'You're him,' he says, gently. 'I thought so.' He pays anyway. He recommends a book on Foucault. You read it. You don't know what to do with the information.",
     "choices": [
        ("Use him as a long, careful conversation partner", "Make him a character.", "s6"),
        ("Stop seeing him; the line is too thin", "Boundary.", "s7"),
     ]},
    {"id": "s6", "title": "Helen's Concern", "text": "Helen, after reading two chapters, calls late. 'Two questions,' she says. 'One: is the work good? Yes. Two: are you?' You realize you don't have a different answer for each.",
     "choices": [
        ("Tell her the answer is the same and you don't know", "Honesty.", "s8"),
        ("Tell her you're fine — finish the book first", "Bet on the work.", "s9"),
     ]},
    {"id": "s7", "title": "The Borderline Night", "text": "A booking goes slightly wrong — nothing dangerous, just unsettling. You go home with a feeling you don't want in your notes. You sit on the kitchen floor with the lights off for an hour.",
     "choices": [
        ("Take a week off", "Replenish.", "s8"),
        ("Write the unsettling scene with full honesty", "Use it.", "s9"),
     ]},
    {"id": "s8", "title": "Your Family", "text": "You go home to Brighton for a weekend. Your mother makes Sunday roast. You realize you have not lied to her about the specifics, only the substance. You realize you'd prefer not to lie at all.",
     "choices": [
        ("Tell her the truth gently", "Family honest.", "s10"),
        ("Wait until the book is out", "Plan the disclosure.", "s11"),
     ]},
    {"id": "s9", "title": "The First Draft", "text": "You finish the first draft on a Wednesday at 3 a.m. You realize, reading it, that the novel is good and is also a kind of exposure. The book is, you slowly understand, going to make you a public person whether or not you choose to be.",
     "choices": [
        ("Send the draft to Helen the next morning", "Commit.", "s10"),
        ("Sit on the draft for a month first", "Decompress.", "s11"),
     ]},
    {"id": "s10", "title": "The Bidding War", "text": "Helen sends the manuscript. Three publishers want it. The advance is, by a wide margin, the most money you have ever been offered for anything.",
     "choices": [
        ("Accept the biggest offer", "Take the money.", "s12"),
        ("Accept the editor you think believes in the book most", "Take the right partner.", "s13"),
     ]},
    {"id": "s11", "title": "The Decision", "text": "You sit with the question of whether to keep working as 'Sebastian' once the book is sold. You realize the answer is, finally, no. You realize you've been hoping the book would let you stop.",
     "choices": [
        ("Stop the day after sale", "Clean break.", "s12"),
        ("Taper off for a month", "Soft landing.", "s13"),
     ]},
    {"id": "s12", "title": "The Publicity Tour", "text": "Pubs ask you the same questions — autobiographical, ethics, exploitation. You answer the same answer with growing patience: the book is a novel. It is also, you admit, a kind of field notes.",
     "choices": [
        ("Be plain about the field notes", "Own it.", "s14"),
        ("Lean into the novelist's distance", "Protect.", "s15"),
     ]},
    {"id": "s13", "title": "Your Family, Reading", "text": "Your father reads the book in three days. He calls you. He says, 'Did you have to write the bath scene?' You laugh, because the laugh is also relief. He says, 'I'm proud of you.' He hangs up before you can answer.",
     "choices": [
        ("Call him back", "Talk.", "s14"),
        ("Write him a letter the next morning", "Letter.", "s15"),
     ]},
    {"id": "s14", "title": "The Long Profile", "text": "A long magazine profile is, you decide, your chance to be honest in your own words. You spend three days with a reporter you trust. The profile, when it lands, is fair, generous, and slightly more vulnerable than you planned.",
     "choices": [
        ("Trust the profile and be done with the press", "Closure.", "s16"),
        ("Use it as a platform for sex worker rights advocacy", "Politicize.", "s17"),
     ]},
    {"id": "s15", "title": "Amna's Question", "text": "Amna, who has read the book, asks if you want to teach a workshop she runs for young writers from working-class backgrounds. You realize you can be useful in a way the book by itself doesn't manage.",
     "choices": [
        ("Take the workshop", "Teach.", "s16"),
        ("Take a sabbatical first", "Rest.", "s17"),
     ]},
    {"id": "s16", "title": "Second Book", "text": "Your second book is, mercifully, about something completely else. Helen jokes, kindly, that you have ten years to write any kind of book you want now. You realize that, more than the money, that is the gift.",
     "choices": [
        ("Write the book you've always quietly wanted to", "Indulge.", "s18"),
        ("Write the book that helps the next 'Sebastian'", "Pass forward.", "s18"),
     ]},
    {"id": "s17", "title": "Brighton, Visiting", "text": "You go home more often. Your mother makes Sunday roast. Your father reads everything you publish, eventually, in his armchair. You realize, late, that your job was never the secret — it was just the symptom of being twenty-six and lonely. You are, slowly, less lonely.",
     "choices": [
        ("Move back near them", "Closer.", "s19"),
        ("Stay in London, visit often", "Balanced.", "s19"),
     ]},
    {"id": "s18", "title": "The Reading", "text": "A bookshop in Bloomsbury asks you to read. The room is small and full. A young person in the second row, embarrassed, asks if they can speak to you after. You realize the reading is, also, an office hour.",
     "choices": [
        ("Stay an hour for the second-row reader", "Mentor.", "s20"),
        ("Be gracious and brief", "Boundaries.", "s20"),
     ]},
    {"id": "s19", "title": "The Honest Lunch", "text": "Helen takes you to lunch and asks, plainly, what kind of writer you want to be in five years. You realize the answer has, finally, come into focus. The answer is, as Helen suspected it would be, both.",
     "choices": [
        ("Tell her the plan", "Plan.", "s20"),
        ("Tell her you'll send it on paper", "Letter.", "s20"),
     ]},
    {"id": "s20", "title": "The Shape of It", "text": "You sit at your desk and write the next sentence. The sentence is yours. The pen is yours. The years ahead, surprisingly, are also yours. You choose which kind of writer you're going to be.",
     "choices": [
        ("The career writer", "Long shelf.", "end_books"),
        ("The writer-teacher", "Shorter shelf, more readers helped.", "end_help"),
        ("The Brighton writer", "Home shelf.", "end_home"),
     ]},
    {"id": "end_books", "title": "A Long Career", "text": "You write books for the next thirty years. Some are good. Some are very good. Your first is the one that everyone asks about, still, even after the others have outsold it. You answer the same way: it was a beginning. You have learned to mean that.",
     "end": "A Long Career"},
    {"id": "end_help", "title": "The Workshop", "text": "Your second book is a quiet, careful guide to writing through difficult life material. It is recommended in three different MFA programs. You teach two workshops a year. You realize, surprised, that you are good at it.",
     "end": "The Workshop"},
    {"id": "end_home", "title": "Brighton, Eventually", "text": "You move back. You buy a small flat with a view of the sea. You write, you visit your parents, you walk the pier in the rain. The novel becomes, in time, a thing you wrote — not a thing you are. That distinction, you realize, is the whole project.",
     "end": "Brighton, Eventually"},
])


# ---------------------------------------------------------------------------
# Bugonia — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
BUGONIA = ({
    "id": "bugonia-the-basement",
    "title": "The Basement Conversation",
    "sourceTitle": "Bugonia",
    "kind": "movie",
    "synopsis": "Two cousins have abducted a pharmaceutical CEO they're convinced is an alien queen. You're the CEO. You have until the lunar eclipse to convince them otherwise — or convince yourself they're right.",
    "releaseYear": 2025,
    "addedAt": "2026-04-18T00:00:00Z",
    "genre": "Thriller",
    "tags": ["paranoia", "captivity", "conspiracy"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Basement", "text": "You wake duct-taped to a chair in a basement that smells like old paint. Two men sit across from you on lawn chairs. The older one, Teddy, is calm. The younger one, Don, is sweating.",
     "choices": [
        ("Stay silent until they speak", "Read the room.", "s2"),
        ("Ask why you are here", "Direct.", "s3"),
     ]},
    {"id": "s2", "title": "The Charge", "text": "Teddy reads, off a printout, the case against you. Your company's drugs have killed thousands. He has paperwork. He has names. He has, he says, photographic evidence that you are 'not from here.'",
     "choices": [
        ("Engage with the drug accusation only", "Find common ground.", "s4"),
        ("Engage with the alien accusation seriously", "Meet them where they are.", "s5"),
     ]},
    {"id": "s3", "title": "Don's Eyes", "text": "Don looks at you the way a child looks at a TV he doesn't quite understand. He says, 'I told him you didn't really look like a queen.' Teddy ignores him.",
     "choices": [
        ("Talk to Don as the weaker link", "Tactical.", "s4"),
        ("Refuse to triangulate; speak to both", "Strategic.", "s5"),
     ]},
    {"id": "s4", "title": "The Lunar Eclipse Deadline", "text": "Teddy explains: there is a lunar eclipse in 36 hours, and he believes the eclipse will 'reveal' your true form. If it does, they will kill you. If it doesn't, they will release you.",
     "choices": [
        ("Negotiate for safer terms", "Bargain.", "s6"),
        ("Accept the deadline and use it", "Use the clock.", "s7"),
     ]},
    {"id": "s5", "title": "Teddy's Mother", "text": "You learn, in fragments, that Teddy's mother died in a clinical trial sponsored by your company. The trial was, on paper, ethical. The reality is, you suspect, more complicated.",
     "choices": [
        ("Tell him you'll look into the trial personally", "Sincerity.", "s6"),
        ("Tell him you're sorry", "Empathy first.", "s7"),
     ]},
    {"id": "s6", "title": "The Phone", "text": "Don, against Teddy's orders, gives you a phone to call your assistant. You have ninety seconds. You realize that 'call for rescue' and 'call to apologize to your team' are, oddly, the same call.",
     "choices": [
        ("Call to apologize and resign", "Use the moment.", "s8"),
        ("Send a coded message for rescue", "Use the moment differently.", "s9"),
     ]},
    {"id": "s7", "title": "The Manifesto", "text": "Teddy has written a manifesto. He reads it to you over many hours. It is, in places, terrifyingly accurate about your industry. It is, in places, deeply unwell about extraterrestrials. You realize that both can be true at once.",
     "choices": [
        ("Critique the manifesto sincerely", "Honest reader.", "s8"),
        ("Praise the parts that are right", "Coalition.", "s9"),
     ]},
    {"id": "s8", "title": "Don, Listening", "text": "Don, who has been silent for hours, finally says, 'I just want my brother to be okay.' You realize Teddy is his brother, that the manifesto is a survival mechanism, and that everything they have done is, in its terrible way, love.",
     "choices": [
        ("Try to give Teddy a kinder story", "Care.", "s10"),
        ("Try to get Don to make the call himself", "Use the gap.", "s11"),
     ]},
    {"id": "s9", "title": "Your Sister Calls Back", "text": "Your sister, who knows you are missing, manages to text Don a question. He answers without thinking. The question reveals, accidentally, exactly where you are. You realize Don has, accidentally, saved you.",
     "choices": [
        ("Use the information to plan an escape", "Logical.", "s10"),
        ("Use the information to negotiate, not escape", "Patient.", "s11"),
     ]},
    {"id": "s10", "title": "The Hours Before the Eclipse", "text": "You spend the next twelve hours in the basement having the most honest conversation of your professional life — about drug trials, about pricing, about the small terrible decisions that compound into bodies. You realize, in passing, that you might be a worse person than you'd believed.",
     "choices": [
        ("Confess to Teddy fully", "Truth.", "s12"),
        ("Confess only the parts you can change", "Pragmatic truth.", "s13"),
     ]},
    {"id": "s11", "title": "The FBI", "text": "Your sister has, with help, called the FBI. They are, you understand from a small radio Don turns on by accident, in a perimeter outside. The eclipse is in nine hours.",
     "choices": [
        ("Encourage Teddy to surrender", "Help him save himself.", "s12"),
        ("Stay calm; wait for them", "Patience.", "s13"),
     ]},
    {"id": "s12", "title": "The Eclipse", "text": "The moon's shadow crosses the sun. Teddy stares at you with an intensity you have never had pointed at you. You do not, of course, transform. He blinks. The deadline passes.",
     "choices": [
        ("Stay calm and offer him a way out", "De-escalate.", "s14"),
        ("Beg him to release you now, before the FBI escalates", "Urgent.", "s15"),
     ]},
    {"id": "s13", "title": "Don's Decision", "text": "Don, off-camera, walks upstairs and opens the front door of the cabin. The FBI agent at the door has been speaking gently for hours. Don sits on the porch with his hands up and tells them, plainly, the layout of the basement.",
     "choices": [
        ("Use the moment to convince Teddy", "Window of mercy.", "s14"),
        ("Stay still until the agents arrive", "Don't break it.", "s15"),
     ]},
    {"id": "s14", "title": "The Trial", "text": "Teddy and Don are arrested. The case becomes, briefly, national. You testify. You also, the same year, voluntarily resign from your company and spend three years working with regulators on patient-trial reforms.",
     "choices": [
        ("Visit Teddy in prison", "Bear the weight.", "s16"),
        ("Send Teddy books, not visits", "Care at distance.", "s17"),
     ]},
    {"id": "s15", "title": "Your Resignation Letter", "text": "Two months later you write a resignation letter that is also a kind of confession. You leave a foundation behind. You leave the equity behind. You realize, looking at the empty drawer, that the basement clarified something the office never could.",
     "choices": [
        ("Start a new company aimed at patient safety", "Action.", "s16"),
        ("Take a year off entirely", "Recover.", "s17"),
     ]},
    {"id": "s16", "title": "Visiting Teddy", "text": "You visit Teddy in prison. He is, by then, on medication that takes the edges off. He does not, at first, want to see you. The third visit he says, 'I still think you're wrong about most things.' You laugh. He almost does too.",
     "choices": [
        ("Stay involved in his case for parole", "Long.", "s18"),
        ("Visit but not advocate", "Limited.", "s18"),
     ]},
    {"id": "s17", "title": "The Foundation", "text": "The foundation you set up funds independent trial monitors. It is, by every measurement, more effective than your company ever was. You realize, late, that maybe you should have been doing this all along. You also realize there is no point in regretting it instead of doing it.",
     "choices": [
        ("Lead the foundation", "Continue.", "s19"),
        ("Hire someone better suited and step back", "Cede.", "s19"),
     ]},
    {"id": "s18", "title": "Don's Halfway House", "text": "Don is in a halfway house, working at a grocery store, mostly steady. You visit. He thanks you for not pressing charges on him personally. You realize repair is, partly, the work of small visits.",
     "choices": [
        ("Visit Don monthly", "Steady.", "s20"),
        ("Visit when he asks", "Reactive.", "s20"),
     ]},
    {"id": "s19", "title": "The Conference Keynote", "text": "An industry conference asks you to keynote. You almost decline. You decide, instead, to tell the basement story plainly. The room is, for a long moment, silent. The reform you push from that stage, for once, lands.",
     "choices": [
        ("Use the platform yearly", "Voice.", "s20"),
        ("Use it once and step back", "One arrow.", "s20"),
     ]},
    {"id": "s20", "title": "The Eclipse Anniversary", "text": "On the night the eclipse would have happened, you sit outside and watch the sky. Teddy is not, in fact, watching it from his cell. He is asleep. You realize the curse, the basement, the manifesto, were always a metaphor he believed because nothing else explained his grief. You decide what to do next.",
     "choices": [
        ("Keep repairing", "Active repair.", "end_repair"),
        ("Keep distance", "Mature distance.", "end_distance"),
     ]},
    {"id": "end_repair", "title": "Repair", "text": "You spend the rest of your career trying to repair what your earlier career did. The math doesn't quite balance. You decide it's enough that you're trying. The basement, when you remember it, is not a nightmare — it's the moment your life turned the right way around.",
     "end": "Repair"},
    {"id": "end_distance", "title": "At Distance", "text": "You stop being a public figure. The foundation does well. Teddy gets parole. He never quite forgives you. You never quite forgive yourself either. You both live anyway. It is, you decide, the honest kind of recovery.",
     "end": "At Distance"},
])


# ---------------------------------------------------------------------------
# Euphoria S3 — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
EUPHORIA = ({
    "id": "euphoria-the-meeting",
    "title": "Meeting Number One",
    "sourceTitle": "Euphoria",
    "kind": "show",
    "synopsis": "You're 20 in East Highland, two years into recovery, working a coffee shop with a sponsor on speed dial. Tonight's meeting is the first you've gone to alone. The town has not gotten quieter.",
    "releaseYear": 2025,
    "addedAt": "2026-04-17T00:00:00Z",
    "genre": "Drama",
    "tags": ["recovery", "youth", "town"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Before the Meeting", "text": "Church basement. Cheap coffee. You sit on a folding chair early, headphones in. People begin filing in. You see a face you do not want to see: Cassie.",
     "choices": [
        ("Stay; recovery is bigger than your discomfort", "Hold the line.", "s2"),
        ("Step outside for one minute", "Reset.", "s3"),
     ]},
    {"id": "s2", "title": "Cassie, Hovering", "text": "She approaches. She is sober too, surprisingly, and she looks like she has cried already today. She says, 'Can we talk after?' You haven't spoken in two years.",
     "choices": [
        ("Agree to talk", "Practice.", "s4"),
        ("Say 'maybe' and see how the hour goes", "Triage.", "s5"),
     ]},
    {"id": "s3", "title": "The Sidewalk", "text": "On the sidewalk you call your sponsor — Ali, who picks up on the second ring even on Tuesdays. He listens. He says, 'You're already doing the work by calling. Go back inside.'",
     "choices": [
        ("Go back inside steadily", "Trust him.", "s4"),
        ("Stay outside for the meeting", "Slow.", "s5"),
     ]},
    {"id": "s4", "title": "Share Time", "text": "You share, briefly, that this is your first meeting alone. The room is warm. An older woman named Marsha says 'glad you're here' in the exact way you needed.",
     "choices": [
        ("Stay for fellowship after", "Build the room.", "s6"),
        ("Slip out quickly", "Save energy.", "s7"),
     ]},
    {"id": "s5", "title": "Lexi, the Sister", "text": "Cassie's sister Lexi is at the meeting too, in the back, surprising you both. She catches your eye and gives a small, kind nod. The Howard sisters have, somehow, both ended up in this room.",
     "choices": [
        ("Talk to Lexi first", "Easier first.", "s6"),
        ("Talk to both sisters at once", "Be brave.", "s7"),
     ]},
    {"id": "s6", "title": "Coffee After", "text": "You, Lexi, Cassie, and Marsha sit at a diner counter at 10 p.m. and order pancakes. Cassie cries quietly into hers. Nobody comments. Lexi reaches over and squeezes her hand.",
     "choices": [
        ("Tell Cassie you're glad she's sober", "Generous.", "s8"),
        ("Tell Lexi you're glad she's here too", "Equal.", "s9"),
     ]},
    {"id": "s7", "title": "The Job", "text": "Wednesday morning. The coffee shop. Your manager Fez is, somehow, kind of a manager now. He gives you the morning shift on purpose so the rest of the day is yours.",
     "choices": [
        ("Tell Fez about the meeting", "Trust him.", "s8"),
        ("Stay quiet at work and write later", "Compartmentalize.", "s9"),
     ]},
    {"id": "s8", "title": "Rue's Notebook", "text": "You keep a notebook. You write the sentence: 'I went to a meeting alone and I came home alone and I did not use.' You read it three times. You realize you have started, slowly, to believe in yourself.",
     "choices": [
        ("Buy a second notebook for the year", "Build the practice.", "s10"),
        ("Start texting one line a day to Ali", "Accountability.", "s11"),
     ]},
    {"id": "s9", "title": "Jules' Visit", "text": "Jules is in town for the week. The first phone call is tentative. The second is honest. The third is, in some way you can't yet name, possible.",
     "choices": [
        ("See her", "Try.", "s10"),
        ("Wait to see her until you've talked to Ali", "Discipline.", "s11"),
     ]},
    {"id": "s10", "title": "The Mother", "text": "Your mom watches you make her coffee in the morning. She does not say much. She doesn't have to. She has, you realize, been working as hard as you, for longer.",
     "choices": [
        ("Tell her you love her plainly", "Plain.", "s12"),
        ("Cook her breakfast in return", "Action.", "s13"),
     ]},
    {"id": "s11", "title": "Gia, Watching", "text": "Your sister Gia is in high school now. She watches you the way she used to watch the front door at 3 a.m. You realize she is not yet sure you will not relapse. You realize her patience is also love.",
     "choices": [
        ("Take Gia somewhere fun on Saturday", "Show up.", "s12"),
        ("Apologize directly for the years", "Speak.", "s13"),
     ]},
    {"id": "s12", "title": "The Anniversary", "text": "Two years. Marsha hands you a chip. You almost don't take it because chips have, in the past, felt like jinxes. You take it. You squeeze it in your hand the whole drive home.",
     "choices": [
        ("Pin it on your fridge", "Visible.", "s14"),
        ("Carry it in your pocket every day", "Private.", "s15"),
     ]},
    {"id": "s13", "title": "Fez's Bakery", "text": "Fez tells you he's opening a small bakery. He wants you as the manager. The hours are hard. The job is real. You realize you have been offered, of all things, a future.",
     "choices": [
        ("Accept the job", "Build.", "s14"),
        ("Negotiate fewer hours so you can keep writing", "Balance.", "s15"),
     ]},
    {"id": "s14", "title": "The Bakery Opening", "text": "Six months later the bakery opens. You and Fez and Marsha and Lexi and your mom and Gia are there. There is a small cake. Marsha gives a small speech. Fez almost cries. You almost cry.",
     "choices": [
        ("Take a photo for the year", "Mark it.", "s16"),
        ("Just be there", "Be there.", "s17"),
     ]},
    {"id": "s15", "title": "The Year of Writing", "text": "You write — not a book, exactly, but a small collection of essays. You publish one in a magazine. The piece, more than the bakery or the job, makes you feel like a person with a project.",
     "choices": [
        ("Send the essay to Jules", "Share.", "s16"),
        ("Send it to your sponsor", "Share.", "s17"),
     ]},
    {"id": "s16", "title": "Jules' Reply", "text": "Jules replies in a long email. She says she's proud of you. She says she's not in a place to come home. She says she'd like to keep writing. You realize, slowly, that not all loves are reunions. Some are just letters.",
     "choices": [
        ("Accept the letters as enough", "Mature.", "s18"),
        ("Plan to visit her in a year, no pressure", "Patient.", "s19"),
     ]},
    {"id": "s17", "title": "Ali's Reply", "text": "Ali, who is dying — you don't know it yet, you'll find out next month — sends you back a one-line text: 'You're writing the version of yourself the rest of us can read.' You frame it.",
     "choices": [
        ("Visit Ali in person next weekend", "Show up.", "s18"),
        ("Send him a long thank-you letter", "Letter.", "s19"),
     ]},
    {"id": "s18", "title": "Five Years", "text": "Five years. You give the chip back at a meeting you sponsor a teenager from. You realize you are now Marsha. You realize this is, finally, a story without an exit.",
     "choices": [
        ("Stay in East Highland", "Place.", "s20"),
        ("Move; keep the meetings the same", "Travel.", "s20"),
     ]},
    {"id": "s19", "title": "Gia's Graduation", "text": "Gia graduates high school. You give the speech at the family dinner. You say plain things. Your mom cries. Gia hugs you longer than usual. You go to bed sober and full and tired in the right way.",
     "choices": [
        ("Keep building the small life", "Maintain.", "s20"),
        ("Travel for the first time in your life", "Reward yourself.", "s20"),
     ]},
    {"id": "s20", "title": "Ali's Chair", "text": "Ali is gone. You sit in the meeting in the chair he used to sit in. The room is the same. You are the same and very different. You decide what to do with the rest of the year.",
     "choices": [
        ("Hold the chair in East Highland", "Steady.", "end_home"),
        ("Take meetings on the road", "Mobile.", "end_road"),
     ]},
    {"id": "end_home", "title": "Home", "text": "You stay. The town gets a little kinder, year over year. You sponsor four people over a decade. Two of them stay sober. Two of them don't. You learn that the score isn't the point. The room is the point.",
     "end": "Home"},
    {"id": "end_road", "title": "Out", "text": "You travel. Meetings everywhere, surprisingly, work the same way. You write essays from cafés in cities you used to dream about as a teenager. You realize that recovery is portable. So, finally, are you.",
     "end": "Out"},
])


# ---------------------------------------------------------------------------
# The Devil Wears Prada 2 — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
PRADA_2 = ({
    "id": "prada-2-the-comeback",
    "title": "The Comeback Issue",
    "sourceTitle": "The Devil Wears Prada 2",
    "kind": "movie",
    "synopsis": "Print is dead. Miranda Priestly is not. She has summoned you back to Runway — fifteen years older, a real career later, and with a daughter you can't be late to pick up. The September issue is a relaunch. Try not to fall apart.",
    "releaseYear": 2026,
    "addedAt": "2026-04-16T00:00:00Z",
    "genre": "Comedy",
    "tags": ["fashion", "work", "second act"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Summons", "text": "An assistant's email — 'Miranda would like to see you Tuesday.' Two sentences. No subject. You read it three times in your kitchen with a child's lunchbox in your other hand.",
     "choices": [
        ("Reply immediately to confirm", "Don't hesitate; she'll notice.", "s2"),
        ("Wait a day; you have a life now", "Set the tone.", "s3"),
     ]},
    {"id": "s2", "title": "Tuesday at Runway", "text": "The lobby smells the same. Your heart, embarrassingly, knows the elevator buttons. Miranda's office is unchanged except for an iPad where the magazines used to be.",
     "choices": [
        ("Compliment the iPad", "Disarm with charm.", "s4"),
        ("Wait until she speaks", "Old skill.", "s5"),
     ]},
    {"id": "s3", "title": "Your Daughter's Drop-Off", "text": "School drop-off Wednesday. Your daughter Beatrix asks, casually, if you're going back to that 'shouty job.' You realize she has been listening more carefully than you thought.",
     "choices": [
        ("Tell her about the meeting", "Honest.", "s4"),
        ("Tell her it's just lunch", "Soften.", "s5"),
     ]},
    {"id": "s4", "title": "The Offer", "text": "Miranda offers you Editor at Large for the relaunch — print plus, a quarterly object that is also a digital ecosystem. The salary is, embarrassingly, real. She does not, of course, mention the work-life balance.",
     "choices": [
        ("Negotiate for hours that fit your life", "Set the terms.", "s6"),
        ("Take the job and figure it out", "Old instinct.", "s7"),
     ]},
    {"id": "s5", "title": "Andy's Newsroom Friend Calls", "text": "An old colleague at a serious magazine offers you a steadier, less prestigious gig at half the salary. The two offers arrive in the same week, which is funny because life is funny.",
     "choices": [
        ("Take the steadier job", "Family-shaped career.", "s6"),
        ("Take Miranda's job; you can survive her now", "Risk.", "s7"),
     ]},
    {"id": "s6", "title": "Emily, Returning", "text": "Emily Charlton — now a major brand executive — walks into Miranda's office to consult on the relaunch. She sees you. She, unusually, smiles for a second before correcting.",
     "choices": [
        ("Approach Emily like an old friend", "Try.", "s8"),
        ("Approach Emily as a future colleague", "Professional.", "s9"),
     ]},
    {"id": "s7", "title": "Beatrix's Question", "text": "Beatrix, ten, asks, 'Did you have a fun day at work?' You realize she has been told that adults should have fun at work. You think about how to answer. You think for too long.",
     "choices": [
        ("Tell her some days are fun and some aren't", "Honest.", "s8"),
        ("Tell her you'll have more fun days now", "Reassure.", "s9"),
     ]},
    {"id": "s8", "title": "The Relaunch Plan", "text": "The plan is ambitious, expensive, and unlikely. Miranda wants a quarterly print object that costs a hundred dollars and sells out. She wants you to make the lead feature feel like a manifesto and a fashion shoot at once.",
     "choices": [
        ("Pitch a story about the daughters of fashion editors", "Make it personal.", "s10"),
        ("Pitch a story about climate-positive supply chains", "Make it political.", "s11"),
     ]},
    {"id": "s9", "title": "Your Husband", "text": "Your husband — who has, mercifully, stayed kind — looks at the calendar with you. The math is tight. The math is, with adjustments, possible.",
     "choices": [
        ("Adjust the math together", "Co-build.", "s10"),
        ("Take a month to test the new schedule before committing", "Trial.", "s11"),
     ]},
    {"id": "s10", "title": "The Photographer", "text": "You hire a photographer Miranda hates. The photographer is brilliant. The shoot goes long. Miranda comes onto set in the last hour and is, for thirty seconds, silent. Then she says, 'Continue.' That is, in her language, applause.",
     "choices": [
        ("Send the photographer a handwritten note", "Mentor up.", "s12"),
        ("Move on to the next shoot with confidence", "Compound.", "s13"),
     ]},
    {"id": "s11", "title": "The Climate Feature", "text": "The supply-chain feature is going to be the first piece many of your old fashion friends actually read. It will also, you realize, anger several advertisers. You decide that's okay.",
     "choices": [
        ("Run it on the cover", "Bold.", "s12"),
        ("Run it as the lead of the inside well", "Strategic.", "s13"),
     ]},
    {"id": "s12", "title": "Beatrix at the Office", "text": "On a school holiday Beatrix comes to the office. Miranda meets her. They shake hands gravely. Miranda compliments Beatrix's shoes. Beatrix asks Miranda, with terrifying calm, what the office is for.",
     "choices": [
        ("Let Miranda answer", "Let it land.", "s14"),
        ("Answer for both of you", "Bridge.", "s15"),
     ]},
    {"id": "s13", "title": "The Old Assistants Group Chat", "text": "Nigel — now in a corner office somewhere else — has started a chat with Emily and you. It is, weirdly, the place you tell your worst day to people who already understand. You realize this support network is part of what makes the work survivable now.",
     "choices": [
        ("Use the chat as a daily lifeline", "Lean.", "s14"),
        ("Use it sparingly; don't drain it", "Steward it.", "s15"),
     ]},
    {"id": "s14", "title": "The Issue Lands", "text": "The relaunch sells out in eleven days. Three of the climate features get picked up by serious newspapers. Miranda smiles, once, on the way to the elevator. It is, for you, the proof.",
     "choices": [
        ("Stay on for the next issue", "Continue.", "s16"),
        ("Make a longer-term commitment", "Lock in.", "s17"),
     ]},
    {"id": "s15", "title": "The After Party", "text": "You leave the launch party at 11. Your husband and Beatrix are still up — they ordered pizza. You sit on the floor with them and eat cold slices in your dress. It is the best thirty minutes of the month.",
     "choices": [
        ("Make this the routine — leave early on purpose", "Build.", "s16"),
        ("Take Beatrix to the next launch", "Bring her in.", "s17"),
     ]},
    {"id": "s16", "title": "Year Two", "text": "Year two of the new Runway is harder. The novelty fades. The advertisers ebb and return. You and Emily and Nigel form, accidentally, a kind of cabinet around Miranda. She does not, of course, acknowledge it. She also doesn't fire any of you.",
     "choices": [
        ("Take the editor-in-chief role when offered", "Step up.", "s18"),
        ("Stay as Editor at Large and write more", "Stay in the work you love.", "s18"),
     ]},
    {"id": "s17", "title": "Beatrix at Twelve", "text": "Beatrix, at twelve, decides she wants to write — not for fashion, for science. You help her get an internship at a nature magazine. You realize, gratefully, that the magazine industry has, for the next generation, gotten a little more interesting because of people like Beatrix.",
     "choices": [
        ("Mentor a new generation through her", "Pay forward.", "s19"),
        ("Stay focused on your own work", "Your lane.", "s19"),
     ]},
    {"id": "s18", "title": "Miranda's Retirement Lunch", "text": "Miranda announces her retirement at a private lunch. She looks at you when she says it. Emily looks at you when she says it. Nigel looks, sweetly, at his salad.",
     "choices": [
        ("Volunteer for the role", "Take it.", "s20"),
        ("Volunteer Emily", "Generous.", "s20"),
     ]},
    {"id": "s19", "title": "Beatrix's Internship Day One", "text": "You drop Beatrix at the nature magazine. She is, somehow, less nervous than you. The editor shakes her hand and yours and says, 'We've heard.' You realize, on the walk back, that you have raised a person.",
     "choices": [
        ("Take the afternoon off to mark it", "Honor.", "s20"),
        ("Go back to work changed", "Carry it.", "s20"),
     ]},
    {"id": "s20", "title": "The Next Cover", "text": "The next September cover is being built. The decisions about it sit on your desk. You realize the cover is, in effect, a vote about who you want to be for the next decade.",
     "choices": [
        ("Take the EIC role and build the next decade", "Lead.", "end_eic"),
        ("Stay Editor at Large and write the better book", "Write.", "end_writer"),
     ]},
    {"id": "end_eic", "title": "Editor-in-Chief", "text": "You become the next editor-in-chief. Miranda, in retirement, sends you a single handwritten note: 'Don't be me. Be better.' You frame it. You try.",
     "end": "Editor-in-Chief"},
    {"id": "end_writer", "title": "Editor at Large, Forever", "text": "You stay in the role that lets you write and live. You publish, in your fifties, a collection of essays about fashion and labor that gets a quiet, deserved prize. Beatrix sits in the front row at the ceremony.",
     "end": "Editor at Large, Forever"},
])


# ---------------------------------------------------------------------------
# Smile 2 — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
SMILE_2 = ({
    "id": "smile-2-the-tour",
    "title": "Tour Stop Seven",
    "sourceTitle": "Smile 2",
    "kind": "movie",
    "synopsis": "You're on stadium tour. Tonight in Boston a fan smiled at you in a way you can't unsee. The curse is here. The cameras are here. The next show is tomorrow.",
    "releaseYear": 2024,
    "addedAt": "2026-04-15T00:00:00Z",
    "genre": "Horror",
    "tags": ["pop star", "curse", "spectacle"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Smile", "text": "Boston, third encore. A face in the front row. The smile is wrong in a way that does not photograph. You finish the song. Your dancers don't notice. You do.",
     "choices": [
        ("Finish the show clean", "Hold the line.", "s2"),
        ("Skip the second encore", "Trust your instincts.", "s3"),
     ]},
    {"id": "s2", "title": "Backstage", "text": "Your manager Joel is happy. The review will be glowing. You ask security to flag the face from the front-row camera. They look at you like you've asked for a unicorn.",
     "choices": [
        ("Push harder for the footage", "Information first.", "s4"),
        ("Let it go for tonight", "Recover first.", "s5"),
     ]},
    {"id": "s3", "title": "The Hotel Room", "text": "Late. You can't sleep. You FaceTime your sister, who knows your old life better than anyone in the room you're in now. She doesn't pick up.",
     "choices": [
        ("Try her again in the morning", "Trust the day.", "s4"),
        ("Get on a plane to her tonight", "Trust the gut.", "s5"),
     ]},
    {"id": "s4", "title": "The Footage", "text": "Security pulls the front-row clip. The face is not, on the video, smiling. The face is, on the video, expressionless. You realize the curse may not be in the camera's bandwidth.",
     "choices": [
        ("Tell Joel about the curse", "Bring in management.", "s6"),
        ("Tell your therapist over the phone", "Bring in care.", "s7"),
     ]},
    {"id": "s5", "title": "Your Sister's House", "text": "On her porch at 5 a.m. she opens the door without asking why. She makes tea. You tell her the truth. She does not say you're crazy. She says, 'I believe you. What do we do?'",
     "choices": [
        ("Stay with her through the next show", "Allies.", "s6"),
        ("Go back; the tour can't stop", "Duty.", "s7"),
     ]},
    {"id": "s6", "title": "Joel's Reaction", "text": "Joel does not, of course, believe in curses. He believes in cancellation insurance and TMZ. He tells you, gently, that 'tour stress' is a thing and that he can move two cities.",
     "choices": [
        ("Accept the moved cities", "Compromise.", "s8"),
        ("Demand a full pause", "Stand firm.", "s9"),
     ]},
    {"id": "s7", "title": "The Doctor in Chicago", "text": "You find — through a private channel — a doctor who has, allegedly, treated this curse before. He is in Chicago. He has a flight in two hours. You can be on it.",
     "choices": [
        ("Take the flight", "Risk the chase.", "s8"),
        ("Have him come to you", "Power.", "s9"),
     ]},
    {"id": "s8", "title": "The Documentary Crew", "text": "Your tour is being documented for streaming. The crew, kindly, asks if you'd like them to give you a day off camera. You realize that 'off camera' is, possibly, the only safe place left.",
     "choices": [
        ("Take the day", "Privacy.", "s10"),
        ("Stay on camera; daylight as protection", "Visibility.", "s11"),
     ]},
    {"id": "s9", "title": "The Last Person Who Smiled at You", "text": "You go back through every photograph from every meet-and-greet of the tour. You find the same face three times — three different cities, three different smiles. You realize the curse has been with you longer than you knew.",
     "choices": [
        ("Trace the face's identity", "Hunt.", "s10"),
        ("Burn every meet-and-greet photo of yourself in your possession", "Ritual.", "s11"),
     ]},
    {"id": "s10", "title": "The Doctor", "text": "The doctor explains: the entity feeds on visibility. The bigger your platform, the bigger its meal. The cure is, embarrassingly, to be less visible — for as long as it takes to starve it.",
     "choices": [
        ("Cancel the rest of the tour", "Starve it.", "s12"),
        ("Cancel only the next month", "Compromise.", "s13"),
     ]},
    {"id": "s11", "title": "The Stadium, Half-Full", "text": "Madison Square Garden. You walk out and the crowd is, against expectation, smaller than expected. The face is, against expectation, not in the front row. The face is in the lighting rig.",
     "choices": [
        ("Stop the show mid-song", "Public refusal.", "s12"),
        ("Sing through it; perform until it fades", "Performer's defiance.", "s13"),
     ]},
    {"id": "s12", "title": "The Press Statement", "text": "Joel and you write a press statement together. It says, in essence, 'I am taking a year off.' It does not mention curses. It mentions burnout. It is, in its own way, the truth.",
     "choices": [
        ("Take the year off in a cabin", "Disappear.", "s14"),
        ("Take the year off touring small underground shows", "Low visibility.", "s15"),
     ]},
    {"id": "s13", "title": "The Defiance Tour", "text": "You finish the tour. The face appears in three more cities. You survive each show. You realize you have, through sheer stamina and your own anger, gained something like control of the curse.",
     "choices": [
        ("Use the control to research and end it", "Active.", "s14"),
        ("Use the control to live with it", "Coexistence.", "s15"),
     ]},
    {"id": "s14", "title": "The Cabin", "text": "Six months in. No phone. No camera. The face appears once, faintly, in a fogged-up bathroom mirror. You laugh at it. It does not, surprisingly, laugh back. It also, after a long second, fades.",
     "choices": [
        ("Stay in the cabin another six months", "Heal.", "s16"),
        ("Go home to make small art", "Quiet life.", "s17"),
     ]},
    {"id": "s15", "title": "The Small Tour", "text": "You play 200-capacity venues under a pseudonym for a year. The shows are honest. You write a new record that is, by any measure, the best of your career.",
     "choices": [
        ("Release the record under your real name", "Reclaim.", "s16"),
        ("Release it pseudonymously", "Stay small.", "s17"),
     ]},
    {"id": "s16", "title": "The Documentary Cut", "text": "The streaming documentary, two years later, lands. It is honest. It uses your words. It does not, you realize gratefully, exploit your worst nights. It also does not say the word 'curse.' You read the reviews exactly once.",
     "choices": [
        ("Take the doc's success and rest", "Pace.", "s18"),
        ("Use the moment to push a real reform of the industry", "Action.", "s18"),
     ]},
    {"id": "s17", "title": "Your Sister, Always", "text": "Your sister is in the front row when you finally play a real venue again. She does not, of course, smile in a way that frightens you. You smile back. The room, for once, does not need to be larger than it is.",
     "choices": [
        ("Tour gently from now on", "Pace forever.", "s19"),
        ("Open a small school for young performers", "Pass it forward.", "s19"),
     ]},
    {"id": "s18", "title": "The Backstage Mirror", "text": "Before the first proper return show you sit in front of a green-room mirror for a long time. The mirror is just a mirror. You promise yourself, out loud, what you will and won't do for this career.",
     "choices": [
        ("Make the promise the rule", "Vow.", "s20"),
        ("Make the promise the working draft", "Flexible.", "s20"),
     ]},
    {"id": "s19", "title": "Boston Bench", "text": "On a bench in Boston between soundcheck and show, your sister and you split a sandwich. You tell her you're scared and also okay. She nods. She takes the half you don't finish.",
     "choices": [
        ("Carry the bench feeling onstage", "Calm.", "s20"),
        ("Step onstage as a different person", "Performer.", "s20"),
     ]},
    {"id": "s20", "title": "The Encore", "text": "The final song of the comeback show. Stadium lights, the band, your sister in the wings. You realize you can choose what this whole next decade looks like — and the choice arrives, gratefully, as your own.",
     "choices": [
        ("Quiet, paced career from here", "Quiet.", "end_quiet"),
        ("Industry-reform megaphone", "Megaphone.", "end_reform"),
        ("Open the small school", "Pass forward.", "end_school"),
     ]},
    {"id": "end_quiet", "title": "Quietly", "text": "You make records every three years. You tour gently. You teach a class at Berklee twice a year. The curse, when you look for it now, is not there. You suspect it is feeding on someone else. You hope, in a complicated way, that they are okay.",
     "end": "Quietly"},
    {"id": "end_reform", "title": "Industry Reform", "text": "You become, against your will, a quiet leader on touring conditions, on artist mental health, on the predatory contracts you barely survived. Three policies change because you talked about them. That is, you realize, the best version of fame.",
     "end": "Industry Reform"},
    {"id": "end_school", "title": "The Small School", "text": "You open a small school in Boston for young performers. It teaches voice, business, and how to set a boundary. The face never returns. The mirror in the green room remains, blessedly, just a mirror.",
     "end": "The Small School"},
])


# ---------------------------------------------------------------------------
# Off Campus — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
OFF_CAMPUS = ({
    "id": "off-campus-the-fall",
    "title": "Fall Semester",
    "sourceTitle": "Off Campus",
    "kind": "show",
    "synopsis": "Junior year. A hockey scholarship. A part-time job. A roommate situation that is, depending on the day, a romance. You have eighteen credits and one heart. Choose what to spend them on.",
    "releaseYear": 2025,
    "addedAt": "2026-04-14T00:00:00Z",
    "genre": "Drama",
    "tags": ["college", "romance", "sport"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Move-In", "text": "The off-campus house is bigger and dustier than the brochure suggested. Your three teammates haul a couch. Your maybe-girlfriend Hannah arrives, surprising everyone but you, with a houseplant.",
     "choices": [
        ("Help her find a spot for the plant", "Small choice.", "s2"),
        ("Keep helping with the couch", "Big choice.", "s3"),
     ]},
    {"id": "s2", "title": "Bookstore", "text": "Hannah and you wander the bookstore together. She buys a course pack. You buy a coffee. She holds your hand on the walk back like you've been together for a year. You haven't.",
     "choices": [
        ("Talk about what 'this' is", "Define.", "s4"),
        ("Don't talk about it; let it be", "Float.", "s5"),
     ]},
    {"id": "s3", "title": "The Captain", "text": "Coach picks the captain on Friday. You are runner-up. Garrett, who deserves it, gets it. You realize you are equal parts relieved and disappointed, which is the most honest you've felt about hockey in a year.",
     "choices": [
        ("Be visibly happy for Garrett", "Sportsmanship.", "s4"),
        ("Let yourself feel disappointed privately", "Honesty.", "s5"),
     ]},
    {"id": "s4", "title": "The Job", "text": "Your part-time job at the campus bar starts. Tips are okay. The shift is until 2. Hockey practice is at 6 a.m. You realize you've signed up for, in the old phrase, the eighteen-hour day.",
     "choices": [
        ("Drop a class to balance", "Triage.", "s6"),
        ("Push through; you can sleep in December", "Grit.", "s7"),
     ]},
    {"id": "s5", "title": "Hannah's Parents", "text": "Hannah's parents visit campus for a weekend. They invite you to dinner. You realize you are now, suddenly, in 'meet the parents' territory. They are nice. Her dad asks you about hockey statistics.",
     "choices": [
        ("Be honest about your stats", "Plain.", "s6"),
        ("Be honest about your major", "Pivot.", "s7"),
     ]},
    {"id": "s6", "title": "Midterms", "text": "Three exams in a week. Your professor sees you fall asleep in lecture. He, kindly, does not call you out. He, kindly, also schedules you for office hours.",
     "choices": [
        ("Go to office hours", "Receive help.", "s8"),
        ("Skip; sleep instead", "Body first.", "s9"),
     ]},
    {"id": "s7", "title": "The Tournament", "text": "A weekend tournament in Maine. You play well. Hannah cannot come. You text her between games. She is, you can tell, slightly bored of being texted between games.",
     "choices": [
        ("Call her after the late game", "Make the effort.", "s8"),
        ("Sleep; she'll understand", "Trust the relationship.", "s9"),
     ]},
    {"id": "s8", "title": "Garrett's Bad Stretch", "text": "Garrett, the captain, is in a slump. Coach is on him. He, off-ice, doesn't talk to anyone. You realize captain isn't, mostly, a prize. It is a weight.",
     "choices": [
        ("Talk to Garrett one-on-one", "Be the teammate.", "s10"),
        ("Let him have his space", "Respect.", "s11"),
     ]},
    {"id": "s9", "title": "Hannah's Friend", "text": "Hannah's friend Maya tells you, gently and without saying so directly, that Hannah is tired of being the one who initiates. You realize this is true. You realize you are also, possibly, the one who is tired.",
     "choices": [
        ("Initiate something thoughtful this week", "Repair.", "s10"),
        ("Have a real conversation about it", "Address.", "s11"),
     ]},
    {"id": "s10", "title": "Coach's Office", "text": "Coach calls you in. He wants to talk about whether you want hockey to be your life after graduation. He is honest about your ceiling. You realize you are honest with yourself for the first time about it too.",
     "choices": [
        ("Decide hockey is for college and beyond", "Bet on it.", "s12"),
        ("Decide hockey is for college, period", "Plan for after.", "s13"),
     ]},
    {"id": "s11", "title": "The Conversation", "text": "You sit on the porch with Hannah. The conversation is not perfect. The conversation is real. By the end you both know what the next month will be — and it is, surprisingly, more 'us' than you'd been managing.",
     "choices": [
        ("Reset the relationship on purpose", "Refresh.", "s12"),
        ("Take it week by week", "Trial.", "s13"),
     ]},
    {"id": "s12", "title": "Finals", "text": "Three finals. Two late shifts at the bar. One playoff game. You sleep, total, twelve hours. You survive the week and your roommate hands you a beer at midnight on Friday. It is, briefly, the best beer of your life.",
     "choices": [
        ("Go home for the break", "Family.", "s14"),
        ("Stay in town with Hannah", "Stay.", "s15"),
     ]},
    {"id": "s13", "title": "Career Fair", "text": "You go to the career fair in a borrowed blazer. You hand out résumés. You realize the future is, against expectations, available. You also realize most of the recruiters at this fair are looking at hockey players for, of all things, sales.",
     "choices": [
        ("Talk to a tech company that interests you", "Aim.", "s14"),
        ("Talk to the kind sales recruiter", "Pragmatic.", "s15"),
     ]},
    {"id": "s14", "title": "Spring Semester", "text": "Spring is gentler. You drop a class. You take a writing class instead. The writing class is, embarrassingly, the best class you have taken in college.",
     "choices": [
        ("Pivot toward writing", "Discover.", "s16"),
        ("Stay your major", "Pragmatic.", "s17"),
     ]},
    {"id": "s15", "title": "Senior Captain Vote", "text": "End of the year. Captains for next season are voted on. Your name is on the list. So is Garrett's, again. You realize you might, this time, want it.",
     "choices": [
        ("Accept the nomination", "Lead.", "s16"),
        ("Decline and support Garrett", "Servant leader.", "s17"),
     ]},
    {"id": "s16", "title": "Senior Year", "text": "Senior year arrives. You are captain or you aren't. You and Hannah are still, somehow, together. Your professor invites you to TA the intro writing course. The houseplant is huge.",
     "choices": [
        ("Take the TA job", "Build the after.", "s18"),
        ("Focus only on hockey and Hannah", "Live the season.", "s18"),
     ]},
    {"id": "s17", "title": "Graduation Day", "text": "Cap and gown. Your family in the bleachers. Hannah ahead of you in line. Garrett behind you. Coach watching from the side. You realize, for one second, that this is the moment you'll think about when life is hard later.",
     "choices": [
        ("Take a mental photo to keep forever", "Save it.", "s19"),
        ("Plan a road trip with Hannah for the summer", "Forward.", "s19"),
     ]},
    {"id": "s18", "title": "The Last Home Game", "text": "Senior night. The rink lights, the parents standing, your name read over the PA. You realize this might be the last time you skate in front of people who came because of you.",
     "choices": [
        ("Take it in fully", "Be present.", "s20"),
        ("Play it like every other game", "Discipline.", "s20"),
     ]},
    {"id": "s19", "title": "The Apartment Lease", "text": "After graduation Hannah and you walk through a small apartment near the city. The kitchen tiles are ugly. The window has good light. You decide together what the year after college looks like.",
     "choices": [
        ("Sign the lease", "Commit.", "s20"),
        ("Wait six months and travel first", "Open.", "s20"),
     ]},
    {"id": "s20", "title": "First Real Monday", "text": "First real Monday after college. The world is, finally, not a syllabus. You sit on a porch and look at it. You decide which version of your life starts now.",
     "choices": [
        ("Build the after", "Career on.", "end_after"),
        ("Stay present for now", "Lean in.", "end_present"),
        ("Take the road trip first", "Drive west.", "end_road"),
     ]},
    {"id": "end_after", "title": "After College", "text": "You finish college with options. You take a job that lets you write. Hockey becomes a Saturday morning thing. Hannah, who matured into being your favorite person, ends up at the same magazine for a year. You build the after on purpose.",
     "end": "After College"},
    {"id": "end_present", "title": "The Long Saturday", "text": "Years later, on a long Saturday, you'll remember this day clearly — the bleachers, the lake, the friends. You'll be sitting on a porch with kids running around. You'll feel, briefly, the way you felt at twenty-one. You'll be grateful.",
     "end": "The Long Saturday"},
    {"id": "end_road", "title": "Summer Road Trip", "text": "Hannah and you drive across the country in a beat-up car. You stop in towns you can't pronounce. You eat at diners. You take a photo at every state border. The photos live in a shoebox you never quite organize. You don't need to.",
     "end": "Summer Road Trip"},
])


# ---------------------------------------------------------------------------
# Roommates — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
ROOMMATES = ({
    "id": "roommates-the-spreadsheet",
    "title": "The Shared Spreadsheet",
    "sourceTitle": "Roommates",
    "kind": "show",
    "synopsis": "Four people, one apartment in Brooklyn, one chore wheel that has, over six months, become a graph theory problem. Tonight's house meeting is about, ostensibly, the dishwasher.",
    "releaseYear": 2025,
    "addedAt": "2026-04-13T00:00:00Z",
    "genre": "Comedy",
    "tags": ["roommates", "Brooklyn", "domestic"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Meeting", "text": "Sunday, 7 p.m. The agenda has been emailed. Item one: dishwasher. Item two: 'something we need to discuss as a group.' Item three: snacks. Marcus has brought, at his own expense, snacks.",
     "choices": [
        ("Open with item three", "Defuse with snacks.", "s2"),
        ("Open with item one", "Discipline.", "s3"),
     ]},
    {"id": "s2", "title": "Item Three First", "text": "Lola lays out two bags of chips and a cheese plate. The cheese plate has, you realize, four different cheeses for four different roommates. Lola, as always, is the heart of the apartment.",
     "choices": [
        ("Compliment Lola publicly", "Lift.", "s4"),
        ("Eat cheese; save the gratitude", "Implicit.", "s5"),
     ]},
    {"id": "s3", "title": "The Dishwasher", "text": "The dishwasher has been stacked badly, every day, for three weeks. Specifically, Bento (who is normally great) has been doing the abominable thing with the small plates.",
     "choices": [
        ("Call Bento out kindly", "Direct.", "s4"),
        ("Show the group a five-minute YouTube video", "Outsourced.", "s5"),
     ]},
    {"id": "s4", "title": "Bento's Reveal", "text": "Bento admits, looking at the floor, that his dad has been sick and he has been distracted. The room rearranges. The dishwasher, suddenly, is the smallest item on the night's true agenda.",
     "choices": [
        ("Reorganize the agenda for Bento", "Pivot.", "s6"),
        ("Keep the agenda; offer Bento support after", "Hybrid.", "s7"),
     ]},
    {"id": "s5", "title": "Lola's Item", "text": "Lola announces, with rehearsed calm, that her girlfriend Priya might move in. The lease is up in March. The math, suddenly, is different.",
     "choices": [
        ("Engage with the math honestly", "Cost.", "s6"),
        ("Engage with Priya as a person first", "Person before lease.", "s7"),
     ]},
    {"id": "s6", "title": "Marcus's Pivot", "text": "Marcus, who has been quietly considering a move to Berlin, says — out loud, for the first time — 'I might leave in May.' The room, again, shifts. Three big things on the agenda. None of them is, anymore, the dishwasher.",
     "choices": [
        ("Address all three at once", "Comprehensive.", "s8"),
        ("Take them one by one", "Sequential.", "s9"),
     ]},
    {"id": "s7", "title": "The Cat", "text": "Bento brings up, gently, that the apartment cat (Phyllis) is going to need new accommodations if anyone moves. Phyllis is, technically, all of yours. Phyllis is, emotionally, Bento's.",
     "choices": [
        ("Promise Bento that Phyllis stays with him", "Easy.", "s8"),
        ("Set up shared visitation if anyone moves", "Custody.", "s9"),
     ]},
    {"id": "s8", "title": "The Spreadsheet Wars", "text": "The shared chore spreadsheet has, over six months, mutated into a mood tracker, a snack inventory, and a grudge log. You all look at it together for the first time in a year. It is, terrifyingly, accurate.",
     "choices": [
        ("Archive it and start fresh", "Reset.", "s10"),
        ("Audit it column by column", "Honest.", "s11"),
     ]},
    {"id": "s9", "title": "Tuesday Dinners", "text": "Lola proposes Tuesday dinners — a guaranteed time you're all in the same room weekly. Marcus, who has a yoga class, hesitates. Bento, who needs this, says 'please.'",
     "choices": [
        ("Make Tuesday a permanent rule", "Routine.", "s10"),
        ("Try it for a month first", "Trial.", "s11"),
     ]},
    {"id": "s10", "title": "Priya's First Dinner", "text": "Priya arrives with a roast chicken she has, somehow, cooked at her own apartment and transported. She is, immediately, the fifth member of the room in a way nobody quite predicted.",
     "choices": [
        ("Vote her in early", "Welcome.", "s12"),
        ("Take six months to vote", "Pace.", "s13"),
     ]},
    {"id": "s11", "title": "Bento's Dad", "text": "Bento's dad gets a better doctor. The treatment plan is, slowly, working. The room celebrates one Friday with a takeout dinner that costs more than any of you should spend. Nobody minds.",
     "choices": [
        ("Make a tradition of small celebrations", "Mark joy.", "s12"),
        ("Keep it casual; don't formalize joy", "Light.", "s13"),
     ]},
    {"id": "s12", "title": "Marcus and Berlin", "text": "Marcus's Berlin plan firms up. He cries at a Tuesday dinner. The cry is, in its own way, the whole apartment saying 'we are about to change.'",
     "choices": [
        ("Plan the goodbye thoughtfully", "Honor it.", "s14"),
        ("Plan a visit to Berlin together for the fall", "Future-focused.", "s15"),
     ]},
    {"id": "s13", "title": "Phyllis at the Vet", "text": "Phyllis, ten years old, has a small scare at the vet. She turns out to be fine. The fact that all four of you went to the vet together makes the receptionist laugh.",
     "choices": [
        ("Confirm Phyllis's primary parent is Bento", "Clarify.", "s14"),
        ("Decide Phyllis is, in the end, a shared family member", "Shared.", "s15"),
     ]},
    {"id": "s14", "title": "Marcus's Goodbye", "text": "On Marcus's last night you cook the meals he loves and bring out the bottle of wine he saved. Lola makes him a small album of photos. Bento writes him a letter. You hand him a small box.",
     "choices": [
        ("Tell Marcus what he meant to you", "Out loud.", "s16"),
        ("Let the small box speak", "Quiet.", "s17"),
     ]},
    {"id": "s15", "title": "Berlin Trip", "text": "Five months later, three of you visit Marcus in Berlin. He shows you his bakery, his park, his new dumb mustache. You realize the apartment was never just walls. It was the people.",
     "choices": [
        ("Make annual trips a thing", "Tradition.", "s16"),
        ("Take this trip and let the future be the future", "Present-only.", "s17"),
     ]},
    {"id": "s16", "title": "Priya Officially Moves In", "text": "Priya's stuff arrives in a U-Haul Lola has, somehow, driven in Brooklyn without weeping. The apartment fits her quickly. The new chore wheel includes her in handwriting that is, finally, less aggressive.",
     "choices": [
        ("Move in together permanently as a chosen family", "Build.", "s18"),
        ("Stay flexible; let people come and go", "Open.", "s18"),
     ]},
    {"id": "s17", "title": "The Spreadsheet, Reborn", "text": "You and Bento, late one night, redesign the spreadsheet with a single sheet titled 'Joy' that just tracks small good moments. The sheet has, by year's end, several hundred entries. You realize the apartment has gotten richer in the kind of math that counts.",
     "choices": [
        ("Show the sheet at New Year's", "Share.", "s19"),
        ("Keep the sheet private to the two of you", "Quiet.", "s19"),
     ]},
    {"id": "s18", "title": "The Annual Trip", "text": "You float the idea of an annual roommate trip — three nights, somewhere small. The chat blows up with location ideas. Marcus, in Berlin, requests Sicily. Nobody can afford Sicily. Everyone agrees to a cabin in the Catskills.",
     "choices": [
        ("Plan it now", "Build the tradition.", "s20"),
        ("Plan it when energy is higher", "Later.", "s20"),
     ]},
    {"id": "s19", "title": "Phyllis's Last Year", "text": "Phyllis, sixteen, slows down. You take turns sleeping on the couch with her. The apartment becomes a hospice and a celebration at once. You realize the joy sheet has, in this last year, never been more full.",
     "choices": [
        ("Stay in this apartment through the loss", "Honor.", "s20"),
        ("Let it be the place that held her, then move", "Move on.", "s20"),
     ]},
    {"id": "s20", "title": "New Year's, on the Roof", "text": "December 31. You and Bento, Lola, Priya, and a FaceTime'd Marcus stand on the roof at 11:58. You decide together what kind of family you'll be next year — the long-haul chosen kind, or the open-door kind that lets people grow.",
     "choices": [
        ("Chosen family, locked in", "Family.", "end_family"),
        ("Open door, evolving family", "Open.", "end_open"),
     ]},
    {"id": "end_family", "title": "Chosen Family", "text": "Years later, two of you are at the others' weddings. Three of you co-own a small bakery in Brooklyn. Phyllis lives a long, full cat life. The apartment, when the lease finally ends, is replaced — by all of you, deliberately — with a series of apartments that, in the end, become a network of homes.",
     "end": "Chosen Family"},
    {"id": "end_open", "title": "Open House", "text": "Some of you move. Some of you stay. Some of you, years later, drift apart in the ordinary way friends drift. You realize the apartment was a kind of beginning, not a permanent address. You are okay with that. You are, in fact, grateful for it.",
     "end": "Open House"},
])


# ---------------------------------------------------------------------------
# The Boroughs — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
BOROUGHS = ({
    "id": "the-boroughs-the-listening",
    "title": "The Listening Society",
    "sourceTitle": "The Boroughs",
    "kind": "show",
    "synopsis": "Your retirement community is, unfortunately, haunted by something. You and your bridge club — none of you under seventy-three — have agreed to investigate. Your hearing aids have new uses.",
    "releaseYear": 2025,
    "addedAt": "2026-04-12T00:00:00Z",
    "genre": "Fantasy",
    "tags": ["seniors", "mystery", "supernatural"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "The Bridge Table", "text": "Lila finishes a hand and announces, calmly, that she heard the spirit again last night at 2:14 a.m. The other three of you put down your cards because Lila is never wrong about times.",
     "choices": [
        ("Take her seriously immediately", "Trust Lila.", "s2"),
        ("Ask kind, clarifying questions first", "Verify.", "s3"),
     ]},
    {"id": "s2", "title": "The Old Map", "text": "Marvin produces, from his apartment, a 1962 map of the original property — a sanatorium before it was the retirement village. Three rooms on the map no longer exist on the current floor plan.",
     "choices": [
        ("Find the rooms", "Investigate.", "s4"),
        ("Research what happened in them first", "Library.", "s5"),
     ]},
    {"id": "s3", "title": "The Hearing Aids", "text": "Beverly's new hearing aids pick up frequencies the rest of yours don't. She agrees to wear them tonight at 2:14. The four of you have, accidentally, become an investigative unit.",
     "choices": [
        ("Set up an overnight stakeout", "Active.", "s4"),
        ("Set up a microphone array instead", "Hands-off.", "s5"),
     ]},
    {"id": "s4", "title": "The Three Rooms", "text": "Two of the three rooms are inside the current basement wall. One of them, you realize after a long Saturday morning, is behind the laundry room. Behind the dryer is a door that is, distinctly, painted over.",
     "choices": [
        ("Open the door", "Curiosity.", "s6"),
        ("Photograph the door and call the property manager", "Process.", "s7"),
     ]},
    {"id": "s5", "title": "The Librarian", "text": "The local librarian — a friend of Marvin's late wife — finds, in the regional archive, three newspaper stories from 1958 about a missing nurse who was 'last seen at the sanatorium.'",
     "choices": [
        ("Bring this to the property manager", "Authority.", "s6"),
        ("Bring it to the police as a cold case", "Bigger authority.", "s7"),
     ]},
    {"id": "s6", "title": "Inside the Door", "text": "The hidden room contains an old hospital bed, two chairs, and a small brass key. The room is cold in a way the basement is not. You realize, sweetly, that you are not scared. You are interested.",
     "choices": [
        ("Take the key out and try other locks", "Investigative.", "s8"),
        ("Leave the key; document the room", "Preserve.", "s9"),
     ]},
    {"id": "s7", "title": "Detective Petrillo", "text": "A young detective named Petrillo agrees to take this seriously — partly because his grandmother lives in your building, mostly because Marvin is, unbelievably, his father's old high school teacher.",
     "choices": [
        ("Work with him formally", "Coalition.", "s8"),
        ("Share what you've found and step back", "Hand off.", "s9"),
     ]},
    {"id": "s8", "title": "The Brass Key", "text": "The key fits a cabinet in the basement laundry. Inside is a small box of letters from a nurse named Eleanor. The letters describe a 'patient' the hospital was treating off the books in 1958.",
     "choices": [
        ("Read every letter aloud over tea", "Honor.", "s10"),
        ("Take them to the historical society", "Public memory.", "s11"),
     ]},
    {"id": "s9", "title": "The Microphone Pickup", "text": "At 2:14 a.m. Beverly's hearing aids pick up, clear as day, a woman's voice saying 'tell them about me.' Lila, sitting beside her, hears it too. You hear, faintly, something. Marvin is, blessedly, recording.",
     "choices": [
        ("Identify whose voice it is", "Hunt.", "s10"),
        ("Sit with the request and decide who to tell", "Honor.", "s11"),
     ]},
    {"id": "s10", "title": "Eleanor's Story", "text": "You piece together, over three weeks of bridge nights, that Nurse Eleanor was protecting a patient — a young woman placed by her family in the sanatorium for 'hysteria' that was, more likely, queerness — and that Eleanor disappeared after smuggling her out.",
     "choices": [
        ("Find descendants of the patient", "Continue the rescue.", "s12"),
        ("Find Eleanor's descendants", "Honor the helper.", "s13"),
     ]},
    {"id": "s11", "title": "The Voice, Identified", "text": "The voice is Eleanor's. You find a 1962 recording of her at a community meeting and confirm by tone. Eleanor, even in death, would like the record to include her sacrifice.",
     "choices": [
        ("Hold a small memorial", "Honor.", "s12"),
        ("Get Eleanor's name on a plaque at the property", "Make it official.", "s13"),
     ]},
    {"id": "s12", "title": "The Granddaughter", "text": "Eleanor's granddaughter, in her sixties, lives in Cleveland. She comes to visit. She has never been told what her grandmother did. You sit her at a bridge table and tell her, slowly, all of it.",
     "choices": [
        ("Help her write a family history book", "Document.", "s14"),
        ("Just let her sit with it for the weekend", "Presence.", "s15"),
     ]},
    {"id": "s13", "title": "The Plaque Committee", "text": "The retirement village board, mostly seventy-year-olds, votes seven to two to put up a small plaque honoring Eleanor in the front lobby. The two no votes are, you suspect, motivated by laziness rather than principle.",
     "choices": [
        ("Write the plaque text yourself", "Author.", "s14"),
        ("Get the historical society to write it", "Credentials.", "s15"),
     ]},
    {"id": "s14", "title": "The Plaque Unveiling", "text": "Eleanor's granddaughter unveils the plaque on a Saturday in spring. The four of you wear your best clothes. The voice, at 2:14 a.m. that night, does not return. You realize, gently, that it doesn't need to.",
     "choices": [
        ("Form a permanent local history committee", "Continue.", "s16"),
        ("Go back to bridge", "Rest.", "s17"),
     ]},
    {"id": "s15", "title": "The Book", "text": "You and Marvin and Lila and Beverly help Eleanor's granddaughter write a small book. It is published by a regional press. It outsells the local cookbook. It is, by your measurements, a real success.",
     "choices": [
        ("Tour the book at three libraries", "Public.", "s16"),
        ("Donate the proceeds to a queer youth center", "Continue Eleanor's work.", "s17"),
     ]},
    {"id": "s16", "title": "The Next Mystery", "text": "Petrillo, the detective, drops by with another cold case. Lila and Marvin and Beverly look at each other. You realize, with delight, that the bridge club has accidentally become an institution.",
     "choices": [
        ("Take the next case", "Continue.", "s18"),
        ("Tell Petrillo this was the case", "Choose your battles.", "s18"),
     ]},
    {"id": "s17", "title": "The Quiet Year", "text": "You go back to bridge. The cards are familiar. The laughs come more easily. Eleanor, you realize, has done something good for the building — not by haunting it, but by being remembered.",
     "choices": [
        ("Keep her photo on the wall above the bridge table", "Hold the memory.", "s19"),
        ("Move on; she's at peace", "Release.", "s19"),
     ]},
    {"id": "s18", "title": "Beverly's Cataract Surgery", "text": "Beverly has surgery. She comes back to bridge with sharper eyes and the same hearing aids. She makes a joke about being able to read your bids now. You realize how lucky you are to keep getting to play.",
     "choices": [
        ("Celebrate with cake", "Joy.", "s20"),
        ("Just deal the next hand", "Routine.", "s20"),
     ]},
    {"id": "s19", "title": "Marvin's Granddaughter Visits", "text": "Marvin's granddaughter, eight, comes to play a hand. She is too young for bridge so you teach her gin. She is, in two hands, beating you. The room fills with a sound you have not heard often — a child's laugh.",
     "choices": [
        ("Invite her to a recurring family-day Sunday", "Tradition.", "s20"),
        ("Send her home full of cookies and let it be one day", "Light.", "s20"),
     ]},
    {"id": "s20", "title": "The Next Hand", "text": "It is your deal. You shuffle. You look at three friends who are still here. You decide what kind of year is next — more cases, or more cake.",
     "choices": [
        ("Take the next case from Petrillo", "Society on.", "end_society"),
        ("Cake. Just cake.", "Bridge Tuesdays forever.", "end_rest"),
     ]},
    {"id": "end_society", "title": "The Listening Society", "text": "The four of you (eventually three, then two, then memory) become a small local legend. Other retirement villages start their own listening societies. You leave behind a quiet, devoted, weird little legacy.",
     "end": "The Listening Society"},
    {"id": "end_rest", "title": "Bridge, Tuesdays", "text": "You play bridge on Tuesdays for the rest of your life. The voice doesn't come back. You and your friends grow old together, slowly. You realize the haunting was, partly, an invitation. You took it. You're grateful you did.",
     "end": "Bridge, Tuesdays"},
])


# ---------------------------------------------------------------------------
# Ladies First — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
LADIES_FIRST = ({
    "id": "ladies-first-the-vote",
    "title": "The Vote",
    "sourceTitle": "Ladies First",
    "kind": "show",
    "synopsis": "Your small-town women's coalition has won a council seat. The seat is yours. The town is split. The first session is Monday and the agenda includes a budget you've been fighting for two years.",
    "releaseYear": 2025,
    "addedAt": "2026-04-11T00:00:00Z",
    "genre": "Drama",
    "tags": ["politics", "women", "small-town"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Election Night", "text": "You win by 41 votes. Your mom cries. Your kid, eleven, is asleep on the couch. The coalition is in your living room making absurdly bad coffee.",
     "choices": [
        ("Thank the coalition publicly tonight", "Recognize.", "s2"),
        ("Save the thank-yous for Monday", "Be presentable.", "s3"),
     ]},
    {"id": "s2", "title": "The Mayor's Call", "text": "The mayor, who endorsed your opponent, calls to congratulate you. He uses your first name without permission. He invites you to coffee. You realize he is, professionally, already negotiating.",
     "choices": [
        ("Accept the coffee", "Politics is also rooms.", "s4"),
        ("Decline politely", "Set the boundary.", "s5"),
     ]},
    {"id": "s3", "title": "Your Mother", "text": "Your mother, who once ran for the same seat and lost twice, makes you sit on the porch with her. 'They will try to make you a kind of woman they can manage,' she says. 'Don't let them.'",
     "choices": [
        ("Ask her how she avoided that", "Listen.", "s4"),
        ("Ask her what she thought she should have done differently", "Different question.", "s5"),
     ]},
    {"id": "s4", "title": "Monday Session", "text": "You sit at the council table for the first time. There are six of you. You are the only woman. The first item is, unbelievably, the budget you've been pushing for two years. The mayor calls you 'councilwoman' the way some men say 'ma'am.'",
     "choices": [
        ("Lead with the budget", "Strike while warm.", "s6"),
        ("Read the room first", "Read.", "s7"),
     ]},
    {"id": "s5", "title": "The Coalition", "text": "Wednesday night meeting at the church basement. Three new members. Two are nervous. One is, you can tell, already angling to be the next candidate. You realize you have to be a leader the coalition wants to follow.",
     "choices": [
        ("Make space for the ambitious one", "Generosity.", "s6"),
        ("Set firm expectations for the coalition", "Discipline.", "s7"),
     ]},
    {"id": "s6", "title": "The Budget Vote", "text": "The vote is three to three. You sit with it for a long second. The deciding vote is, of course, an unexpected councilman who, you realize, is voting his conscience for the first time.",
     "choices": [
        ("Thank him publicly after", "Make him your ally.", "s8"),
        ("Thank him privately and protect him", "Strategic.", "s9"),
     ]},
    {"id": "s7", "title": "Your Kid's Questions", "text": "Your kid, eleven, asks you, with great seriousness, what your job is now. You think for a long minute. You realize the answer is, technically, 'I argue with men about how the town should work.'",
     "choices": [
        ("Tell her exactly that", "Honest.", "s8"),
        ("Give her the kid-version", "Gentle.", "s9"),
     ]},
    {"id": "s8", "title": "The Editorial", "text": "The local paper writes an editorial about your first vote. It is, mostly, generous. It is, in one paragraph, condescending. You realize the editor is, separately, going to be your neighbor for a long time.",
     "choices": [
        ("Respond to the editorial in a letter", "On record.", "s10"),
        ("Don't respond; let the work speak", "Discipline.", "s11"),
     ]},
    {"id": "s9", "title": "The Town Hall", "text": "Your first town hall as a councilmember. The room is louder than the council chamber. A man in the back yells about your funding decision. A woman near the front cries because of it.",
     "choices": [
        ("Address the man first", "Calm the loudest.", "s10"),
        ("Address the woman first", "Honor the quieter.", "s11"),
     ]},
    {"id": "s10", "title": "The Difficult Vote", "text": "Three months in. A vote on whether to fund a new library or repair the old highway bridge. The county will subsidize either, not both. You can guess which option the men will pick.",
     "choices": [
        ("Push for the library", "Vision.", "s12"),
        ("Push for the bridge", "Pragmatism.", "s13"),
     ]},
    {"id": "s11", "title": "The Quiet Win", "text": "You and the unexpected councilman start meeting for breakfast. You don't agree on much. You agree on the budget for the food pantry. The breakfasts become, in their way, the actual government.",
     "choices": [
        ("Codify the alliance", "Build.", "s12"),
        ("Keep it informal", "Light.", "s13"),
     ]},
    {"id": "s12", "title": "The Re-Election Year", "text": "Two years pass. Your re-election campaign is, mercifully, less of a fight than the first. You win by 312 votes. The coalition has, in your absence, doubled.",
     "choices": [
        ("Run for mayor next cycle", "Aim up.", "s14"),
        ("Stay on the council and build", "Stay in your strength.", "s15"),
     ]},
    {"id": "s13", "title": "The Daughter Watching", "text": "Your daughter, thirteen now, sits in on a council meeting and watches you for two hours. Afterward she says, 'I want to do that.' You realize you have, accidentally, started a small generational thing.",
     "choices": [
        ("Mentor her properly", "Pass the skill.", "s14"),
        ("Let her find her own version", "Independence.", "s15"),
     ]},
    {"id": "s14", "title": "Mayor", "text": "You run for mayor. The town is, again, split. You win, again, narrowly. Your mother is in the audience at the swearing-in, in a dress she's owned since 1987. She doesn't cry. Her dress, she says, is too good.",
     "choices": [
        ("Make 'small town, big work' your platform", "Frame.", "s16"),
        ("Just do the work quietly", "Substance.", "s16"),
     ]},
    {"id": "s15", "title": "Your Library Wins", "text": "The library opens, eventually. There is a small plaque with your name and three other names. Your daughter cuts the ribbon because you insisted. The whole coalition is in the front row. So is your mother.",
     "choices": [
        ("Use the library opening for the next campaign", "Build.", "s17"),
        ("Just celebrate the library", "Honor the win.", "s17"),
     ]},
    {"id": "s16", "title": "First Hundred Days", "text": "The first hundred days are paperwork, parking, ordinances. Glamorous it is not. You realize, slowly, that being mayor is mostly the work of returning calls. You return them.",
     "choices": [
        ("Keep returning every call personally", "Old school.", "s18"),
        ("Hire a chief of staff", "Scale yourself.", "s18"),
     ]},
    {"id": "s17", "title": "The County Conference", "text": "You attend a county-wide conference of small-town officials. Half of them are women now. Five years ago, two of them were. You realize you have, accidentally, been part of a shift.",
     "choices": [
        ("Take the lead on a regional coalition", "Bigger frame.", "s19"),
        ("Stay focused on your own town", "Local.", "s19"),
     ]},
    {"id": "s18", "title": "The Veto", "text": "Your first veto. The bill is, on balance, bad. The council member who proposed it is, separately, a friend's husband. You veto it. You call the friend the same night. The friendship survives. The friendship is, briefly, the work.",
     "choices": [
        ("Be principled and friendly always", "Both at once.", "s20"),
        ("Accept some friendships will fray", "Honest about cost.", "s20"),
     ]},
    {"id": "s19", "title": "The Regional Coalition Meeting", "text": "You convene a coalition of nine towns. The first meeting is awkward. The second is, surprisingly, productive. By the third you are voted, against your wishes, the chair.",
     "choices": [
        ("Accept the chair", "Take it.", "s20"),
        ("Decline; nominate someone better suited", "Pass.", "s20"),
     ]},
    {"id": "s20", "title": "Re-Election Eve", "text": "Eve of the re-election. The kitchen table, again, late. Your mother, in town for it, has made tea. Your daughter, fifteen, is writing your closing remarks for you. You realize the politics has, finally, become a family practice.",
     "choices": [
        ("Run again with the bigger 'small town' frame", "Mayor again.", "end_mayor"),
        ("Run again on quiet, careful substance", "Quiet.", "end_quiet"),
     ]},
    {"id": "end_mayor", "title": "Mayor for Two Terms", "text": "You serve two terms as mayor and shape, slowly, a town that looks like the town you wanted to grow up in. Your daughter, fifteen, runs for student council and wins. Your mother, in her late seventies, retires into proudly criticizing the new mayor.",
     "end": "Mayor for Two Terms"},
    {"id": "end_quiet", "title": "Councilwoman, Quietly", "text": "You stay on the council. You build, quietly, slowly, decisively. People stop being surprised that a woman has the seat. Your kid grows up in a town that is, in small ways, kinder. That, you realize, was always the point.",
     "end": "Councilwoman, Quietly"},
])


# ---------------------------------------------------------------------------
# Toaster — ⭐⭐⭐⭐
# ---------------------------------------------------------------------------
TOASTER = ({
    "id": "toaster-the-startup",
    "title": "The Smart Toaster",
    "sourceTitle": "Toaster",
    "kind": "show",
    "synopsis": "Your dumb startup makes one product: a smart toaster nobody asked for. You have eight months of runway, a co-founder who's lost the plot, and a pivot meeting on Monday.",
    "releaseYear": 2025,
    "addedAt": "2026-04-10T00:00:00Z",
    "genre": "Comedy",
    "tags": ["startup", "hardware", "tech"],
    "rating": 4,
    "loved": False,
}, [
    {"id": "s1", "title": "Monday, 9 a.m.", "text": "Your co-founder Aman comes in twenty minutes late carrying a different toaster, smiling. 'I have a new idea,' he says. Your CFO Priya, also a friend, has her eyes closed in a long, suffering breath.",
     "choices": [
        ("Hear Aman out", "Respect the bond.", "s2"),
        ("Postpone Aman until after the pivot meeting", "Discipline.", "s3"),
     ]},
    {"id": "s2", "title": "Aman's New Idea", "text": "The new idea is, predictably, not a toaster. It is a 'smart cutting board.' You sit with this for three seconds. You realize the toaster is, at minimum, our toaster. The cutting board would, again, be nobody's.",
     "choices": [
        ("Push back firmly", "Stand for the product.", "s4"),
        ("Validate the impulse, then push back", "Soft.", "s5"),
     ]},
    {"id": "s3", "title": "Priya's Numbers", "text": "Priya hands you the eight-month runway sheet. Three months in we have to either cut burn, raise, or sell. The toaster has, on the chart, three small green dots. The dots are, you suspect, you, Aman, and Priya's mom.",
     "choices": [
        ("Cut burn first", "Survive.", "s4"),
        ("Plan a raise first", "Bet.", "s5"),
     ]},
    {"id": "s4", "title": "The User Interview", "text": "An actual customer, a woman in her sixties named Janine, calls in. She bought the toaster for her husband, who has memory issues. The toaster's reminder feature has, she says, kept him eating breakfast on the right schedule.",
     "choices": [
        ("Pivot the marketing toward elder care", "Find the real customer.", "s6"),
        ("Add Janine's story to the deck", "Investor candy.", "s7"),
     ]},
    {"id": "s5", "title": "The Lead Engineer", "text": "Your lead engineer Sam is, you realize, our only hope. He has been quietly fixing the toaster's firmware in his off-hours. He has, in his desk drawer, a prototype of a screenless version that sells for half the price.",
     "choices": [
        ("Greenlight the cheap version", "Pivot the product.", "s6"),
        ("Promote Sam to CTO before anyone steals him", "Reward.", "s7"),
     ]},
    {"id": "s6", "title": "The Investor Meeting", "text": "Walking into the VC office you decide, in the elevator, what story you are about to tell. Aman has a different story queued up. You have to align fast.",
     "choices": [
        ("Tell the elder-care story", "Real customer.", "s8"),
        ("Tell the tech story", "Familiar music.", "s9"),
     ]},
    {"id": "s7", "title": "Aman's Crisis", "text": "Aman, after the meeting, breaks down in the conference room. He says he's been lying for months — to investors, to his wife, to you. He's not, he says, a CEO. He never was. He wants to be CTO.",
     "choices": [
        ("Accept the role swap immediately", "Honor the truth.", "s8"),
        ("Negotiate a slower transition", "Pragmatic.", "s9"),
     ]},
    {"id": "s8", "title": "Press Day", "text": "A surprise: a national magazine wants to profile Janine and the toaster. They will be at the office Thursday. You realize the story has, accidentally, gotten ahead of the strategy.",
     "choices": [
        ("Embrace the story", "Ride the wave.", "s10"),
        ("Delay the press for a tighter pivot", "Discipline.", "s11"),
     ]},
    {"id": "s9", "title": "The Layoffs", "text": "You let three people go. The way you do it matters. You write the references personally. You give two weeks of severance you can't afford. You realize this is the hardest thing you have done at this company so far.",
     "choices": [
        ("Tell the remaining team the truth about the runway", "Trust.", "s10"),
        ("Hold the worst details until you have a plan", "Triage.", "s11"),
     ]},
    {"id": "s10", "title": "The Profile Lands", "text": "The profile is, mercifully, generous. The toaster sells out in seven days. The investors who passed last month start emailing again. Aman, somehow, gets a Wired feature out of being the 'humble CTO who saw the truth.'",
     "choices": [
        ("Raise the bridge round on momentum", "Take it.", "s12"),
        ("Stay lean and grow off revenue", "Discipline.", "s13"),
     ]},
    {"id": "s11", "title": "Sam's Prototype", "text": "Sam's cheap prototype is ready for a pilot. You ship a small batch to fifty elder-care facilities at cost. The feedback is, against all expectation, immediate and positive.",
     "choices": [
        ("Productize for elder-care directly", "Vertical.", "s12"),
        ("Stay consumer; price up the cheap version", "Brand.", "s13"),
     ]},
    {"id": "s12", "title": "The Series A", "text": "The Series A comes in. The lead investor is a woman who, herself, had a parent the toaster could have helped. The conversation in the conference room is, somehow, both about a SaaS multiple and her father.",
     "choices": [
        ("Accept her term sheet", "Right partner.", "s14"),
        ("Take a smaller round with terms you love", "Discipline.", "s15"),
     ]},
    {"id": "s13", "title": "The Quiet Quarter", "text": "Three months pass. Revenue, slowly, climbs. You stop watching Twitter. You start sleeping. You realize, weirdly, that running a business at human scale is actually possible. It is just unfashionable.",
     "choices": [
        ("Commit to human-scale forever", "Vow.", "s14"),
        ("Stay open to bigger if the right opportunity comes", "Flexible.", "s15"),
     ]},
    {"id": "s14", "title": "Year Three", "text": "Three years in. Forty employees. Revenue real. The toaster has a small but devoted following and a real elder-care line. You go to Janine's husband's funeral. She hugs you for a long time.",
     "choices": [
        ("Stay CEO for another decade", "Continue.", "s16"),
        ("Hand off to a more operational CEO and become chair", "Cede.", "s17"),
     ]},
    {"id": "s15", "title": "The Acquisition Offer", "text": "A larger appliance company offers to buy you. The number is, professionally, life-changing. You have to decide what 'enough' is.",
     "choices": [
        ("Sell and use the money to build the next thing", "Take it.", "s16"),
        ("Stay independent for the customers' sake", "Hold.", "s17"),
     ]},
    {"id": "s16", "title": "Aman's Bakery", "text": "Aman, post-CTO, opens, of course, a bakery. The bread is fine. The bakery has, perfectly, a smart toaster on the counter. You and Priya laugh until you cry the first time you visit.",
     "choices": [
        ("Make the bakery your weekend office", "Joy.", "s18"),
        ("Visit often but stay focused on the company", "Discipline.", "s18"),
     ]},
    {"id": "s17", "title": "The Letter from Janine", "text": "Janine sends a handwritten letter. It says, mostly, thank you. It says, in the middle of the second page, that she has started a small support group for caregivers and uses the toaster as the shared metaphor. You frame the letter.",
     "choices": [
        ("Fund the support group", "Pay forward.", "s19"),
        ("Build a feature directly for caregivers based on her group", "Productize the love.", "s19"),
     ]},
    {"id": "s18", "title": "Board Meeting, Quiet", "text": "A quarterly board meeting that, for once, is boring in the good way. Revenue is up. Burn is sane. The lead investor asks, casually, what you want the next ten years to look like.",
     "choices": [
        ("Answer with a small ten-year plan", "Small, on purpose.", "s20"),
        ("Answer with a big ten-year plan", "Build for scale.", "s20"),
     ]},
    {"id": "s19", "title": "The All-Hands", "text": "You give an all-hands that is, for the first time, less a sales pitch than a thank-you. You read parts of Janine's letter aloud. Sam, the engineer, blinks twice and turns away. You realize most of the people in this room have been waiting for permission to care this openly about the work.",
     "choices": [
        ("Make the caregiver feature the next quarter's focus", "Commit.", "s20"),
        ("Make small, kind operational changes first", "Internal.", "s20"),
     ]},
    {"id": "s20", "title": "The Toaster Box, in a Drawer", "text": "Late at night you open the bottom drawer of your desk. The first toaster prototype is there, dented. You hold it. You decide the shape of the next chapter, in your hands, holding the thing that started it all.",
     "choices": [
        ("Stay small forever", "Smallness as principle.", "end_keep"),
        ("Scale it for caregivers everywhere", "Scale the care.", "end_grow"),
     ]},
    {"id": "end_keep", "title": "Small, On Purpose", "text": "You keep the company small. It stays profitable. You take real vacations. You hire kindly. You realize, late, that the toaster was never the point. The team was. The customers were. The company is, by every measure that matters, a success.",
     "end": "Small, On Purpose"},
    {"id": "end_grow", "title": "The Elder-Care Platform", "text": "The company grows into a real elder-care platform. The toaster is, eventually, one of nine devices. You IPO. You retire at fifty. You sit in your garden with a toaster you built yourself and think, with surprising gentleness, of how far that one stupid idea took you.",
     "end": "The Elder-Care Platform"},
])


# ---------------------------------------------------------------------------
# Helper for short stories: linear 21-decision skeleton with three endings.
# Used for the lighter-rated entries to keep length proportionate.
# ---------------------------------------------------------------------------

def mini_story(meta, scenes_text, endings):
    """
    Shorter cousin of linear_story for "quick reads": exactly 6 scenes,
    2 endings. Same skeleton — last scene branches to the two endings.
    Tags "mini" automatically.
    """
    meta = dict(meta)
    tags = list(meta.get("tags") or [])
    if "mini" not in tags:
        tags.append("mini")
    meta["tags"] = tags
    scenes = []
    n = len(scenes_text)
    for i, (title, text, a_l, a_c, b_l, b_c) in enumerate(scenes_text):
        sid = f"m{i+1}"
        if i < n - 1:
            target = f"m{i+2}"
            choices = [(a_l, a_c, target), (b_l, b_c, target)]
        else:
            choices = [
                (a_l, a_c, endings[0][0]),
                (b_l, b_c, endings[1][0]),
            ]
        scenes.append({"id": sid, "title": title, "text": text, "choices": choices})
    for eid, etitle, etext in endings:
        scenes.append({"id": eid, "title": etitle, "text": etext, "end": etitle})
    return (meta, scenes)


def linear_story(meta, scenes_text, endings):
    """
    scenes_text: list of (title, prose, choice_a_label, choice_a_consequence,
                          choice_b_label, choice_b_consequence) tuples.
    The last scene's choices route to the three endings. All other scenes
    route both choices to the next scene.
    endings: list of (id, title, prose) tuples, length 3.
    """
    scenes = []
    n = len(scenes_text)
    for i, (title, text, a_l, a_c, b_l, b_c) in enumerate(scenes_text):
        sid = f"s{i+1}"
        if i < n - 1:
            target = f"s{i+2}"
            choices = [(a_l, a_c, target), (b_l, b_c, target)]
        else:
            choices = [
                (a_l, a_c, endings[0][0]),
                (b_l, b_c, endings[1][0]),
                ("Take the third path", "Some endings reveal themselves last.", endings[2][0]),
            ]
        scenes.append({"id": sid, "title": title, "text": text, "choices": choices})
    for eid, etitle, etext in endings:
        scenes.append({"id": eid, "title": etitle, "text": etext, "end": etitle})
    return (meta, scenes)


# ---------------------------------------------------------------------------
# Stranger Things S5 — ⭐⭐⭐
# ---------------------------------------------------------------------------
STRANGER_THINGS = linear_story({
    "id": "stranger-things-the-rift",
    "title": "The Last Rift",
    "sourceTitle": "Stranger Things",
    "kind": "show",
    "synopsis": "Hawkins. One more rift. The party is older, the stakes are bigger, and the math homework is, somehow, still due Monday.",
    "releaseYear": 2025,
    "addedAt": "2026-04-09T00:00:00Z",
    "genre": "Sci-Fi",
    "tags": ["upside-down", "party", "small-town"],
    "rating": 3,
    "loved": False,
}, [
    ("Hawkins Pool, Closing Time", "The pool drains weirdly. The lifeguard, who is also Steve, notices first. Robin, beside him, is already calling Dustin.",
     "Call the whole party in", "Strength in numbers.", "Investigate quietly first", "Don't spook the town."),
    ("Eleven, On the Phone", "El is two states away at school. The call drops twice. The third time she just says, 'I'm coming.' She is.",
     "Wait for her", "Trust the heavy hitter.", "Start without her", "Don't wait."),
    ("The Wheeler Basement", "The party reassembles around a kitchen table that has, somehow, more spreadsheets than the FBI.",
     "Plan first", "Discipline.", "Move first", "Adrenaline."),
    ("The New Kid", "A transfer student named Vera knows more about the Upside Down than she should. She also runs cross-country.",
     "Recruit Vera", "Allies.", "Watch Vera carefully", "Trust verifies."),
    ("Hopper's House", "Hopper has a cabin, a beer, and a tired face. He wants to help. He also wants you to be careful.",
     "Ask for the gun", "Older solutions.", "Ask for his old files", "Newer solutions."),
    ("Max, Recovering", "Max walks now. She is, against her own will, the quietest of the group. She has, you realize, opinions about the rift you have not yet asked for.",
     "Make her tactical lead", "Promote.", "Let her opt in", "Respect."),
    ("Will's Headache", "Will starts feeling it again. He hates feeling it again. He does not, however, hide.",
     "Use Will's connection", "Old talent.", "Protect Will first", "Family first."),
    ("The Library Microfiche", "A 1960s newspaper has a rift story buried in the obituaries section. The pattern, you realize, is generational.",
     "Photograph the article", "Document.", "Find the old witnesses", "Sources."),
    ("Vera's Confession", "Vera admits she's been tracking the rifts since her family lost a brother in 1989. She is, you realize, also a survivor.",
     "Make her co-lead", "Honor it.", "Make sure she's okay first", "Care first."),
    ("Tunnels Under Town", "There are tunnels. There are always tunnels. The town's pipes have been a map for years and nobody noticed.",
     "Map the tunnels", "Cartography.", "Go in tonight", "Speed."),
    ("Steve and Robin's Bicker", "They bicker. They are best friends. They are working. The team is, in their own way, held together by them.",
     "Send them as a pair", "Don't split.", "Send them separately", "Coverage."),
    ("The Demogorgon's Cousin", "A new monster — smaller, faster, somehow politer about doors. You hate that you noticed the politeness.",
     "Engage cautiously", "Test it.", "Hit it hard", "Don't give it time."),
    ("Lab Records", "Hopper's old files contain the names of researchers still alive. One is, you discover, in Indianapolis. He will, on the phone, say one sentence and hang up.",
     "Drive to Indianapolis", "Pursue.", "Send Steve in your stead", "Triangulate."),
    ("Eleven Arrives", "El, in the rain, in a denim jacket. The room exhales. You realize you have, despite the spreadsheets, been waiting for her exactly this long.",
     "Lead with her", "Use the gift.", "Center the team, with her", "Distributed."),
    ("The First Skirmish", "A skirmish at the pool. Nobody dies. Two get hurt. The monster retreats. You understand its pattern.",
     "Press the advantage", "Move.", "Plan the second", "Discipline."),
    ("The Indianapolis Researcher", "He says, in his apartment, 'You'll have to close it from inside.' He is, you can tell, telling you the truth he has been afraid to tell for thirty years.",
     "Accept the cost", "Brave.", "Look for another way", "Hope."),
    ("Max's Plan", "Max draws, on a napkin, a plan that involves all of you, no martyr. The plan is, you suspect, the one El has been quietly thinking too.",
     "Approve Max's plan", "Trust her.", "Refine it with the group", "Together."),
    ("The Mall, Empty", "The mall, again. It is, somehow, always the mall. The rift glows above the food court. You realize you have grown up in this building.",
     "Step in", "Lead.", "Anchor outside", "Hold."),
    ("Vera's Choice", "Vera offers to be the inside-person. So does Will. So, in his way, does Steve. You decide who.",
     "Send Vera", "She's the runner.", "Send Will", "He's the connection."),
    ("The Close", "The rift, with the team's coordinated push, closes for the last time. The fluorescents flicker. The town does not, this time, lose a kid.",
     "Stand in the empty mall together", "Be there.", "Walk out into the parking lot", "Step into the after."),
    ("The Parking Lot", "Cars, summer, the team. You realize you will all, eventually, leave this town. Tonight, though, you are right where you should be.",
     "Throw a party at the Wheelers'", "Joy.", "Just go to Steve's job for ice cream", "Simple."),
], [
    ("end_party", "Party Together", "You stay close — through college, through breakups, through one wedding and one funeral. The party never breaks up. You realize, late, that the rift was never the point. The friendships were."),
    ("end_town", "Hawkins, After", "You stay in Hawkins. You become a person who watches the town for next time. Next time, mercifully, does not come."),
    ("end_world", "Out Into the World", "You leave Hawkins and never quite leave it. Wherever you go, a part of you is in that basement around that table. You take the lesson — that a small group of kids can save a town — into every other room of your life."),
])


# ---------------------------------------------------------------------------
# Hijack S2 — ⭐⭐⭐
# ---------------------------------------------------------------------------
HIJACK = linear_story({
    "id": "hijack-flight-72",
    "title": "Flight 72",
    "sourceTitle": "Hijack",
    "kind": "show",
    "synopsis": "Seven hours from Singapore to London. Row 18. Aisle. You're a corporate negotiator on holiday. They picked the wrong plane.",
    "releaseYear": 2025,
    "addedAt": "2026-04-08T00:00:00Z",
    "genre": "Thriller",
    "tags": ["airplane", "negotiation", "real-time"],
    "rating": 3,
    "loved": False,
}, [
    ("Hour One", "Wheels up. You order tomato juice. The man in 18B is, you notice, sweating.", "Engage him", "Test.", "Watch him", "Read."),
    ("Hour Two", "A flight attendant goes pale at the galley curtain. You realize something has shifted at the front.", "Move forward", "Act.", "Stay seated", "Wait."),
    ("Cabin Crew", "The lead flight attendant is competent. She uses careful eye contact. You realize she is already negotiating.", "Join her quietly", "Pair up.", "Support from your seat", "Don't crowd."),
    ("The Demand", "An announcement: 'Stay seated.' Two men in business class are armed. The demand is, unusually, specific. They want a name in Singapore released.", "Note the name", "Information.", "Note the men", "People."),
    ("Row 18C", "An off-duty doctor in 18C catches your eye. She has, you can tell, training you don't.", "Coordinate with her", "Allies.", "Don't expose her", "Protect."),
    ("The Phone", "You have a satellite phone in your bag. You can, with one text, reach your firm's security desk.", "Send one careful text", "Use it.", "Save the phone for later", "Hold."),
    ("Cockpit", "The pilots are, by the schedule, still in there. The door is, by the schedule, still closed.", "Talk to the FA about the door", "Strategy.", "Trust the protocol", "Don't push."),
    ("The Negotiator", "The men in business class let you, eventually, speak with them. You are, in their words, 'the calm one.'", "Lower their adrenaline", "Defuse.", "Stall for the ground", "Time."),
    ("The Singapore Name", "The name they want is, you realize, a man your firm has briefed you on. The story is, in places, more complicated than the demand suggests.", "Use that knowledge", "Leverage.", "Don't reveal what you know", "Hide."),
    ("Hour Three", "A child cries. The doctor calms him. A businessman across the aisle has, against your judgement, decided he can take the smaller man.", "Talk him down", "Prevent.", "Coordinate his timing", "Use."),
    ("The Ground", "Ground control, finally, is on the line. The negotiator on the other end is in their forties and exhausted.", "Build rapport with them too", "Two fronts.", "Stay focused on the cabin", "One front."),
    ("Hour Four", "The men are tiring. They have, you notice, planned for this hour. They have not, you notice, planned for hour five.", "Wait them out", "Patience.", "Force a small concession", "Pressure."),
    ("The Bathroom Run", "An older passenger needs the bathroom. The smaller man refuses. The older passenger, eventually, doesn't ask twice.", "Negotiate a compromise", "Mercy.", "Let the moment pass", "Don't escalate."),
    ("The Doctor's Read", "The doctor whispers: one of the men is, by her medical eye, in a hypoglycemic spiral. She suggests, casually, food.", "Use the suggestion", "Soften him.", "Save it for later", "Hold."),
    ("Hour Five", "The plan, you realize, was always to land somewhere — not London. They need to know they can land. You realize you can offer that.", "Offer the landing", "Trade.", "Don't trade until you have to", "Hold."),
    ("The Pilots", "The captain's voice, through the door, is steady. He asks, professionally, for guidance. You give it.", "Tell him the truth about the cabin", "Trust him.", "Keep it minimal", "Compartmentalize."),
    ("Diverted", "The plane diverts to a smaller airport. The men, on the ground, are no longer airborne — which is itself a kind of defeat.", "Push for the door to open peacefully", "Quiet.", "Wait for tactical", "Patience."),
    ("The Door", "The cockpit door opens, finally, with the men's permission. The pilots, professional, do not, in the cockpit, react.", "Help the pilots regain composure", "Care.", "Step back and let them work", "Trust."),
    ("Tactical", "The negotiator on the ground signals you. The men set down their weapons. Nobody fires.", "Bring the cabin to its feet quietly", "Order.", "Stay in your seat as instructed", "Comply."),
    ("Tarmac", "The doors open onto a tarmac that smells of jet fuel and rain. The passengers, in a long line, walk out. You and the doctor and the flight attendant are last.", "Hug the FA", "Friendship of seven hours.", "Walk out alone", "Process privately."),
    ("After", "You stand in a small airport's corridor with foil blankets and bad coffee. You realize you can choose, right now, what kind of person this flight made you.", "Stay in the business", "Use the skill.", "Take a different job", "Get off the road."),
], [
    ("end_negotiator", "Negotiator, Higher Stakes", "You leave corporate and join an international crisis-response team. You log many more hours like flight 72. You sleep well in the after, but you never quite love a plane again."),
    ("end_quiet", "Quieter Work", "You take a quieter job. You write a memo about cabin tactics that gets distributed to every flight attendant in Europe. Nobody knows your name. Many people are alive because of you."),
    ("end_friend", "The Doctor and the FA", "You stay in touch with the doctor and the flight attendant for the rest of your life. You become, in a real sense, family. You have, you realize, met your people."),
])


# ---------------------------------------------------------------------------
# Scouts Guide to the Zombie Apocalypse — ⭐⭐⭐
# ---------------------------------------------------------------------------
SCOUTS_ZOMBIE = linear_story({
    "id": "scouts-zombie-the-camp",
    "title": "Camp Zombie",
    "sourceTitle": "Scouts Guide to the Zombie Apocalypse",
    "kind": "movie",
    "synopsis": "Your scout troop's overnight camp goes badly when, somehow, half of town becomes flesh-eating. You have a sash, three badges, and a slingshot. Use them.",
    "releaseYear": 2015,
    "addedAt": "2026-04-07T00:00:00Z",
    "genre": "Comedy",
    "tags": ["zombies", "scouts", "small-town"],
    "rating": 3,
    "loved": False,
}, [
    ("Pancakes, Optional", "Saturday morning. Troop leader is missing. Cocoa is cold. You and Carter and Augie find a zombie behind the storage shed.",
     "Scream", "Honest.", "Stay quiet", "Tactical."),
    ("Carter's Plan", "Carter wants to drive to the police station. The police station is, by Augie's count, two miles.", "Walk", "Slow but safe.", "Bike", "Faster."),
    ("Augie's Sash", "Augie has, on his sash, a 'fire-making' badge, a 'first aid' badge, and a 'parade marshal' badge. The last one is, in fact, weirdly useful.", "Use the sash organizationally", "Be the leader.", "Mock the sash gently", "Tone."),
    ("Denise from the Strip Club", "A woman named Denise appears with a baseball bat and saves you from a small mob. She is, immediately, in charge.", "Defer to Denise", "Smart.", "Earn her respect", "Slow."),
    ("Hardware Store", "The hardware store has nails, baseball bats, and a single guy named Ron behind the counter who has, apparently, been waiting for this.", "Recruit Ron", "More hands.", "Take supplies and go", "Speed."),
    ("The Mall", "The mall, of course. Inside is a stage being set up for the high school party tonight. The party may still be on. Half the senior class doesn't know yet.", "Warn the party", "Save lives.", "Use the mall to fortify", "Defend."),
    ("Old People's Home", "The retirement home is, surprisingly, mostly fine. The residents have, for various reasons, mistaken the apocalypse for a fire drill.", "Brief them carefully", "Care.", "Leave them; they're safe", "Move on."),
    ("Carter's Crush", "Kendall, Carter's crush, calls his phone. She is at the party. She is, somehow, alive. She is, also, smarter than Carter has ever realized.", "Pivot to the party", "Crush as motive.", "Stay on plan", "Discipline."),
    ("Zombie Cat", "A zombie cat. You both want to laugh and don't.", "Distract it", "Soft.", "Slingshot it", "Pragmatic."),
    ("The High School", "The school is locked. The football coach is, weirdly, leading a militia inside. He is, weirdly, doing it well.", "Join the militia", "Numbers.", "Avoid the militia", "Loner."),
    ("Slingshot Range", "You have, the badge book says, eighteen inches at minimum for accuracy. You discover, in practice, more like twelve.", "Practice on something static", "Discipline.", "Use it live", "Battle test."),
    ("Augie's Brave Moment", "Augie, who has been the dorkiest of you for nine years, makes a move that saves Denise. The moment is small. The moment is huge.", "Make sure he knows", "Tell him.", "Let it be", "Some bravery is private."),
    ("The Trampoline", "An above-ground pool, a trampoline, two suburban kids' inheritance. You and Carter use them to clear a fence.", "Catch up to Denise", "Reconvene.", "Find Augie first", "Friend first."),
    ("Mall, Round Two", "The mall stage is up. Half the high school is there. Music is loud. Nobody has noticed the zombies in the food court yet.", "Cut the music", "Get attention.", "Lock the doors first", "Contain."),
    ("Kendall's Smarter", "Kendall, faced with the situation, organizes the party into a defense in under two minutes. You realize you have wildly underestimated her.", "Follow her lead", "Smart.", "Coordinate as equals", "Pair up."),
    ("Coach's Militia", "The coach's militia arrives, late, but timely. Their plan is bad. Your plan is also bad. Together the plans become acceptable.", "Merge the plans", "Pragmatic.", "Stay separate", "Discipline."),
    ("Trampoline Charge", "You orchestrate, against all reason, a trampoline-based charge that picks off the perimeter zombies in a way that, in a different timeline, would have been a YouTube video.", "Commit to it", "Funny is fine.", "Cover for it tactically", "Discipline."),
    ("Augie's Sash, Again", "Augie's parade marshal badge actually saves the entire defensive arrangement by organizing them in a pattern only he knows. Augie, you realize, is the hero of this movie.", "Promote Augie publicly", "Honor.", "Let him have it quietly", "Style."),
    ("The Last Wave", "Final wave. The football field. The stadium lights are on. You and Carter and Augie and Denise hold the south corner. Kendall holds the north.", "Charge", "Brave.", "Hold the line", "Patient."),
    ("Daylight", "Sunrise. The town is, mostly, scoured. The bus carrying the surviving teenagers pulls away. You and Augie sit on the bleachers eating, somehow, leftover pancakes.", "Celebrate", "You won.", "Sit quietly", "Decompress."),
    ("After School", "Monday morning. School is, weirdly, in session. The town has decided to call this a 'fire' for insurance reasons.", "Stay scouts", "Sash on.", "Quit scouts to be normal", "Sash off."),
], [
    ("end_sash", "Eagle Scout, Eventually", "You stay in scouts. You become an Eagle Scout. You write your application essay about the night the trampoline saved a high school. The reviewer, who has heard everything, says it is the most specific essay he has read."),
    ("end_kendall", "Kendall and the World", "Carter and Kendall become a couple. Augie, somehow, becomes the most popular kid at school. You become the friend who knows. You go on to a normal life that, every Halloween, gets weirder."),
    ("end_quiet", "Quiet Senior Year", "You quietly graduate. You never tell most people the truth about that night. You keep the sash in a box in your closet. Sometimes, late, you take it out and put it on. It still fits."),
])


# ---------------------------------------------------------------------------
# Zero Day — ⭐⭐⭐
# ---------------------------------------------------------------------------
ZERO_DAY = linear_story({
    "id": "zero-day-the-network",
    "title": "Day Zero",
    "sourceTitle": "Zero Day",
    "kind": "show",
    "synopsis": "A cyberattack takes the country down for one minute and kills three thousand people. You're a former president, asked back to chair the investigation. The answer, you suspect, is in your old administration's closets.",
    "releaseYear": 2025,
    "addedAt": "2026-04-06T00:00:00Z",
    "genre": "Thriller",
    "tags": ["politics", "cyber", "commission"],
    "rating": 3,
    "loved": False,
}, [
    ("The Briefing", "FBI Director, on a sofa in your study. The brief is one minute long. The minute was, as far as anyone can prove, foreign.", "Take the commission", "Lead.", "Refuse and recommend someone", "Decline."),
    ("Your Wife", "She does not want you to take it. She is, in the marital sense, correct. You take it anyway. She, in the marital sense, supports you.", "Promise her a date", "Marriage.", "Promise her honesty", "Marriage harder."),
    ("Staff", "You build a small staff — a former general counsel, a young technologist, a press secretary you respect.", "Lead with the lawyer", "Process.", "Lead with the technologist", "Substance."),
    ("First Hearing", "The first hearing is, as expected, theater. You permit a small amount of it.", "Use the theater", "Strategic.", "Cut to substance", "Discipline."),
    ("The Whistle", "An NSA analyst comes to you quietly. He has data the agency has, he believes, redacted dishonestly. You verify him.", "Receive the data", "Brave.", "Recommend formal whistleblower channels first", "Process."),
    ("Memory Issues", "You notice, between meetings, that you are forgetting things. Names. Dates. The press secretary does not, you can tell, want to be the one who tells you.", "See a doctor immediately", "Honest.", "Hide it for now", "Strategic."),
    ("The Daughter", "Your daughter, a congresswoman, has been briefed by her own staff that you are missing things. She comes to you. The conversation is difficult and loving.", "Tell her everything", "Family.", "Tell her you'll handle it", "Pride."),
    ("Closet, Old Administration", "The whistleblower's data points to a backdoor you signed off on during your presidency. You did not, at the time, understand it fully. You sign off on many things.", "Take responsibility publicly", "Honor.", "Address it quietly first", "Discretion."),
    ("Press Secretary", "Your press secretary asks if you want a statement. He has, separately, written two drafts. One is a full apology. One is a careful one.", "Use the full apology", "Brave.", "Use the careful one", "Strategic."),
    ("Director", "The current FBI Director meets you off the record. He is loyal to the institution. He is, in this case, on your side.", "Coordinate with him", "Allies.", "Stay separate", "Independence."),
    ("Asia Trip", "A trip to Tokyo, Seoul, and Taipei, with the question 'who did this.' The answer, in your gut, is not what the briefings say.", "Trust your gut", "Independent.", "Trust the briefings", "Process."),
    ("Memory Test", "Your doctor confirms early cognitive issues. The press will, eventually, learn. You decide what shape the disclosure takes.", "Disclose now", "Cleaner.", "Disclose at the end of the commission", "Strategic."),
    ("Your Old Chief of Staff", "Your old chief of staff is, you discover, lobbying for the cybersecurity firm at the center of the closet you just opened. He is a friend.", "Confront him", "Honor.", "Subpoena him", "Process."),
    ("The Quiet Threat", "Someone in the executive branch — quietly, formally — would prefer you didn't.", "Push back through formal channels", "Process.", "Push back publicly", "Sunlight."),
    ("Your Wife, Again", "She makes coffee in the morning and doesn't ask. You realize, gratefully, that being silent with someone is also a form of supporting them.", "Tell her everything", "Marriage.", "Just thank her", "Marriage."),
    ("Hearing, Final Day", "Final hearing. The room is, somehow, both packed and tired. You speak for fourteen minutes without notes. You realize, mid-sentence, that you are, almost, telling the truth.", "Tell all of it", "Brave.", "Tell most of it", "Strategic."),
    ("The Report", "The final report is honest. It also, at your insistence, names the backdoor you signed. The press, expecting cover-up, doesn't quite know what to do.", "Take questions immediately", "Press.", "Let the report speak", "Discipline."),
    ("Resignation", "You resign from a board you sit on. The resignation is, in a quiet way, the punishment that fits.", "Resign quietly", "Honor.", "Resign with a public statement", "Public."),
    ("Daughter, Calling", "Your daughter calls. She read the report. She tells you she is proud of you. You realize, in your seventies, that this matters more to you than any other call you have taken.", "Tell her what's been going on with the doctor", "Honest.", "Save it for dinner", "Family in person."),
    ("Memoir", "You decide to write a memoir. The memoir is, finally, the honest one. The publisher, surprising you, is grateful.", "Lead with the failure", "Brave.", "Lead with the lessons", "Frame."),
    ("Last Year", "The diagnosis progresses, slowly. You spend time at the lake with your wife. The country, mostly, recovers.", "Spend the last good year with family", "Family.", "Spend it on one last public good", "Service."),
], [
    ("end_legacy", "Legacy of the Report", "The report becomes the foundation for the cybersecurity reforms that follow. You are remembered for the honesty more than the presidency. You decide, late, that that is exactly right."),
    ("end_family", "Lake House", "You spend your last good years at the lake with your wife and daughter and three grandchildren who think you are mostly fun. The country goes on. You let it. You let yourself go on too."),
    ("end_service", "One Last Good", "You spend your last year on a quiet, careful piece of policy work. You finish it. The next administration adopts it. You don't, in the end, see it implemented. But the country is, by a small measure, safer because of you."),
])


# ---------------------------------------------------------------------------
# Zodiac — ⭐⭐⭐
# ---------------------------------------------------------------------------
ZODIAC = linear_story({
    "id": "zodiac-the-cartoonist",
    "title": "The Cartoonist",
    "sourceTitle": "Zodiac",
    "kind": "movie",
    "synopsis": "San Francisco, late seventies. You're the kid in the newsroom who can't stop staring at the killer's ciphers. Your boss doesn't think it's your job. He's wrong.",
    "releaseYear": 2007,
    "addedAt": "2026-04-05T00:00:00Z",
    "genre": "Thriller",
    "tags": ["cipher", "newsroom", "obsession"],
    "rating": 3,
    "loved": False,
}, [
    ("The Letter", "It arrives at the paper in a manila envelope. The cipher is in three colors. You are, technically, the political cartoonist.", "Look at it anyway", "Curious.", "Walk past", "Discipline."),
    ("The Detective", "Inspector Toschi, on the phone, is polite and brittle. He has many cases. This is one.", "Offer to help informally", "Volunteer.", "Stay out of his way", "Respect."),
    ("Your Editor", "Your editor laughs. He tells you to stick to cartoons. You realize, slowly, that he is also curious.", "Pitch the story", "Push.", "Work on it after hours", "Stealth."),
    ("The Crime Scenes", "On weekends you visit, on your own dime, every public crime scene. None of them tell you anything you didn't already read.", "Take notes anyway", "Discipline.", "Stop visiting", "Pragmatic."),
    ("The Bar", "The reporter assigned to the case, Avery, is at the bar. He is, by 8 p.m., drunker than you are. He is also smarter.", "Drink with him", "Source.", "Get him home", "Friend."),
    ("Codebreakers", "A teacher and his wife crack one of the ciphers in their kitchen. The cipher is, on cracking, mostly Christian theology and ego.", "Use the cipher's tells", "Read.", "Pass it up the chain", "Process."),
    ("Your Wife", "Your wife wants to know why you're not home. You realize you don't have a good answer that isn't, slowly, ruining you.", "Tell her the obsession is the thing", "Honest.", "Promise to come home earlier", "Promise."),
    ("Avery's Tip", "Avery hands you a manila folder. He is, he says, done with it. He is leaving the paper.", "Take the folder", "Pick up.", "Refuse it", "Honor."),
    ("The Long Suspect", "A man named Allen, school employee, lake area, the right kind of wrong. You read his file three nights in a row.", "Stay on Allen", "Long.", "Look at other suspects", "Open."),
    ("Toschi, Frustrated", "Toschi has been re-investigated by his own department after a forged letter. He is, professionally, dying.", "Offer to back him publicly", "Friend.", "Stay neutral", "Reporter."),
    ("Your Editor, Again", "Your editor finally lets you write. The article is, by his hand, half its original length. It is still, in places, accurate.", "Run the article", "Print.", "Pull the article", "Patient."),
    ("Stalking", "You notice, one night, that you are being followed. You don't know by whom. The follower, you suspect, is your own paranoia.", "Vary your route", "Discipline.", "Confront", "Stupid."),
    ("Allen's Trailer", "You visit Allen's trailer with your editor's permission. He is mostly silent. He stares at you for a long minute. You leave with nothing and everything.", "Trust your gut", "Instinct.", "Trust the evidence", "Process."),
    ("The Polygraph", "Allen takes a polygraph. The polygraph says, ambiguously, no. You realize polygraphs say ambiguously, no.", "Use the result anyway", "Selective.", "Drop the angle", "Honest."),
    ("Your Daughter", "Your daughter, six, asks why you are not at her recital. You sit her on your knee that night and tell her, almost, the truth.", "Promise to be at the next one", "Vow.", "Promise to step back from the case", "Bigger vow."),
    ("The Case Files", "You get, by way of a sympathetic clerk, copies of files you should not, technically, have. They contain, finally, the thing nobody has named.", "Use them carefully", "Discreet.", "Don't use them", "Honor."),
    ("Toschi's Retirement", "Toschi retires. He invites you to his backyard party. You go. He thanks you for the company more than the help.", "Stay in touch", "Friend.", "Let him have his retirement", "Boundary."),
    ("The Book", "You decide to write a book. The book is a years-long project. The book is, you realize, your only path to closure.", "Commit to the book", "Years.", "Write a smaller version first", "Pilot."),
    ("The Manuscript", "The manuscript is, in the end, careful and damning. It accuses Allen by implication. Your lawyer goes through every page twice.", "Publish", "Risk.", "Publish a less specific version", "Discipline."),
    ("The Letter from a Reader", "A letter from a woman who survived a Zodiac attack, decades ago. She thanks you. She also, in passing, names the man you suspected.", "Take her letter at face value", "Trust.", "Verify with her police report", "Verify."),
    ("Old Age", "You are old now. The case is, technically, unsolved. You are, technically, retired. You realize 'unsolved' is not the same as 'unknown.'", "Stay quietly satisfied", "Quiet.", "Take one last lap", "Loud."),
], [
    ("end_book", "The Book Endures", "The book becomes the definitive account. Other writers use it. A film is, eventually, made from it. You are credited as a consultant. You attend the premiere. You are bored. You are, also, grateful."),
    ("end_quiet", "The Cartoon Desk, Again", "You go back to cartoons. You discover, late, that you are good at them. You publish a small collection of newsroom-life cartoons that does, surprisingly, well. Your daughter laughs at every one."),
    ("end_one_more", "One More Letter", "In your eighties you receive, in your mail, an envelope with a cipher in three colors. You do not, this time, open it for the paper. You open it for yourself."),
])


# ---------------------------------------------------------------------------
# Scary Movie 2 — ⭐⭐⭐
# ---------------------------------------------------------------------------
SCARY_MOVIE_2 = linear_story({
    "id": "scary-movie-2-the-mansion",
    "title": "Hell House",
    "sourceTitle": "Scary Movie 2",
    "kind": "movie",
    "synopsis": "You're invited to a haunted mansion 'for a college study.' The professor has one arm. The cat is talking. The chandelier is, somehow, judging you.",
    "releaseYear": 2001,
    "addedAt": "2026-04-04T00:00:00Z",
    "genre": "Comedy",
    "tags": ["parody", "horror", "haunted-house"],
    "rating": 3,
    "loved": False,
}, [
    ("The Driveway", "The mansion. The professor. The one arm that does, technically, work in mysterious ways.", "Shake the arm", "Polite.", "Refuse politely", "Cautious."),
    ("Welcome Drink", "Hannibal the butler hands you a drink that is, in fact, alive.", "Drink it", "Brave.", "Pour it in a plant", "Smart."),
    ("Your Room", "Your room contains a bed, a closet, and one ghost who is mostly into critique.", "Engage the ghost", "Friend.", "Ignore", "Survival."),
    ("Dinner", "Dinner is roast something. The vegetables are screaming. Hannibal pretends not to notice.", "Eat it", "Manners.", "Pretend to eat it", "Style."),
    ("The Talking Cat", "The cat, named Mr. Kittles, knows everything. Mr. Kittles will tell you, for treats.", "Bribe Mr. Kittles", "Strategy.", "Don't trust the cat", "Wise."),
    ("First Scare", "A floating sheet. A chandelier that judges. A long hallway that's longer when you walk back.", "Walk fast", "Smart.", "Walk slow", "Style."),
    ("Buddy", "Buddy, the wheelchair-bound friend from college, arrives. He has, mysteriously, gained the ability to levitate.", "Befriend Buddy", "Loyal.", "Get out of Buddy's way", "Practical."),
    ("The Basement", "The basement has, against all reason, a clown room. Nobody likes the clown room.", "Skip the clown room", "Wise.", "Enter the clown room", "Brave."),
    ("Theo", "Theo, the goth, has an opinion about every painting in the house. Her opinions are, occasionally, prophetic.", "Listen to Theo", "Smart.", "Mock Theo gently", "Tone."),
    ("Chandelier Sentience", "The chandelier delivers a sermon about your choices. The chandelier is, in fact, correct.", "Apologize to the chandelier", "Humor.", "Argue with the chandelier", "Style."),
    ("The Maze", "Hedge maze. The hedge maze is also alive. It is, however, polite.", "Be polite back", "Tone.", "Run", "Survival."),
    ("Sex Ghost", "There is a sex ghost. He is, somehow, the most polite character in the movie. He offers tea.", "Accept the tea", "Civil.", "Decline politely", "Civil."),
    ("The Library", "The library has a single book. The book is full of cookie recipes. The recipes are good.", "Bake cookies", "Joy.", "Read the book aloud", "Use."),
    ("The Footman", "A footman with a chainsaw. He is, alarmingly, also a member of HR.", "Comply with HR", "Smart.", "File a complaint", "Style."),
    ("Buddy's Crisis", "Buddy can't get out of bed. The bed has, apparently, gained sentience and is filing a counter-claim.", "Negotiate with the bed", "Diplomacy.", "Get Buddy out anyway", "Pragmatic."),
    ("Theo's Plan", "Theo proposes, with great seriousness, a séance. Everyone agrees. The professor brings extra crackers.", "Hold the séance", "Plot.", "Hold the séance but eat the crackers first", "Snacks."),
    ("Séance", "The spirits arrive. They are mostly there for the crackers. One of them files a noise complaint.", "Sort out the noise complaint", "Civic.", "Pivot to actual exorcism", "Plot."),
    ("Professor's Reveal", "The professor reveals his one-arm origin story. It involves a wedding, a tractor, and his cousin. Nobody is brave enough to ask follow-up questions.", "Ask follow-ups", "Brave.", "Let the story breathe", "Mercy."),
    ("Final Showdown", "All the ghosts in one room. The chandelier presides. Mr. Kittles moderates. Buddy is, against all odds, the swing vote.", "Side with the chandelier", "Style.", "Side with Mr. Kittles", "Smart."),
    ("Exit", "You walk out of the mansion alive, with cookies and a fairly comprehensive HR file.", "Take the cookies home", "Practical.", "Leave the cookies for the ghosts", "Civil."),
    ("Sequel Hook", "A title card promises, somewhere down the road, another sequel. Mr. Kittles winks at the camera. The chandelier sighs.", "Wink back", "Style.", "Pretend not to notice", "Civil."),
], [
    ("end_house", "Welcome to the Family", "The mansion adopts you. You move in. You become, by year's end, an honorary haunting. It is the best apartment you have ever had."),
    ("end_book", "The Memoir", "You write a memoir of the weekend. It outsells your other books combined. You retire on the proceeds. You are interviewed, exactly once, on morning TV."),
    ("end_cookies", "Cookies, Indefinitely", "You take the recipe book. You open a small bakery. Mr. Kittles, in a strange way, becomes the bakery's mascot. The chandelier writes you a glowing online review."),
])


# ---------------------------------------------------------------------------
# EuroTrip — ⭐⭐⭐
# ---------------------------------------------------------------------------
EUROTRIP = linear_story({
    "id": "eurotrip-the-summer",
    "title": "The Summer Pass",
    "sourceTitle": "EuroTrip",
    "kind": "movie",
    "synopsis": "Graduation week. A penpal in Berlin. Three friends, one rail pass, and an unwise budget. The plane lands in London at 6 a.m. Go.",
    "releaseYear": 2004,
    "addedAt": "2026-04-03T00:00:00Z",
    "genre": "Comedy",
    "tags": ["travel", "friendship", "europe"],
    "rating": 3,
    "loved": False,
}, [
    ("Heathrow", "You land in London with two backpacks too many and one good plan. The plan involves Mieke.", "Start with London", "Sights.", "Skip to Paris", "Train."),
    ("The Hostel", "The hostel manager is a man named Vinnie. Vinnie has a very specific energy.", "Trust Vinnie", "Friend.", "Sleep with one eye open", "Wise."),
    ("Hooligans", "Your friend Scott offends a Manchester United fan in a pub. The pub becomes a chase. The chase becomes a story.", "Apologize", "Smart.", "Outrun them", "Brave."),
    ("Channel Crossing", "The ferry is bouncy. Cooper is seasick. You realize travel friendship requires more grace than you expected.", "Take care of Cooper", "Friend.", "Read on deck", "Self."),
    ("Paris", "Paris is, against all the cliches, exactly what they said. You are, somehow, both nineteen and exactly the right age.", "Climb the Eiffel Tower", "Touristy.", "Sit in a cafe", "Vibey."),
    ("Mime", "You and your friend Jenny adopt a street mime. The mime has, somehow, a phone number.", "Keep the mime", "Whimsy.", "Tip the mime, move on", "Practical."),
    ("Amsterdam", "Bicycles. Canals. A man named Hennie selling, technically, tours.", "Take the tour", "Trust.", "Wander on your own", "Independent."),
    ("Rome", "Rome on a Saturday is, in fact, a kind of carnival. The Trevi Fountain has a coin policy.", "Throw the coin", "Tradition.", "Save the coin", "Cheap."),
    ("The Train Station Pickpocket", "A pickpocket lifts Scott's wallet. Scott, in a moment of clarity, lifts it back.", "Celebrate", "Win.", "Apologize", "Even."),
    ("Vatican Robbed", "Scott is mistaken for a tourist who is, separately, evading a debt. The Vatican guard is gentle but firm.", "Explain", "Process.", "Run", "Comedy."),
    ("Berlin", "Berlin is colder than expected. Mieke's address is, technically, valid.", "Knock", "Brave.", "Wait at the bar", "Wise."),
    ("Mieke", "Mieke opens the door. She is taller than you imagined and exactly as wonderful.", "Apologize for the misunderstanding", "Honor.", "Try to charm her", "Funny."),
    ("Berghain (parody version)", "You and Scott and Cooper and Jenny end up at a club whose doorman judges you with great efficiency. Jenny, somehow, gets in.", "Wait outside for Jenny", "Friend.", "Find another club", "Adventure."),
    ("Train, Overnight", "Overnight train to Bratislava. Cheap. The bunk is, technically, a shelf. Cooper sleeps anyway.", "Sleep on the floor", "Smart.", "Stay up all night", "Story."),
    ("Bratislava", "Bratislava is, of course, much cheaper than your guidebook promised. You and the boys eat very well.", "Stay an extra day", "Wise.", "Move on", "Schedule."),
    ("Robot Club", "A bar with a robot bartender. The robot bartender is, you realize, just a man in a costume. The man is friendly.", "Befriend the man", "Vibe.", "Pretend you didn't notice", "Style."),
    ("Italian Train Chaos", "Italian train strike. You and the gang sleep in a station with a stray dog. The dog likes Cooper best.", "Adopt the dog", "Hilarious.", "Find a hotel", "Adult."),
    ("Pope Audience", "By accident you end up at a small Pope audience. The Pope, somehow, blesses Cooper specifically.", "Take a photo", "Story.", "Just be there", "Holy."),
    ("Mieke, Again", "Mieke catches up with you in Venice. She is, against all odds, also into Scott. He realizes, late, that he likes her too.", "Step back graciously", "Friend.", "Joke about it forever", "Tone."),
    ("Last Night", "Last night before flights home. You sit at a hostel bar in Lisbon. You realize the summer is, finally, ending.", "Toast everyone", "Sentiment.", "Just enjoy", "Quiet."),
    ("Heathrow Again", "You land in London again on the way back. You are, technically, the same person. You are, technically, not.", "Go home", "Practical.", "Stay one more week", "Brave."),
], [
    ("end_home", "Senior Year", "You go home. You start senior year a slightly different person. The trip becomes the reference point. Your friends, ten years from now, will quote it at parties."),
    ("end_extra_week", "One More Week", "You stay an extra week. The week, somehow, becomes a month. You almost don't come home. You realize, in the end, you can come back. You will."),
    ("end_mieke", "Berlin, Forever", "Scott marries Mieke. You are the best man. The wedding is in Berlin. The toast is the longest of your life. You realize the trip was, somehow, a love story you didn't know you were in."),
])


# ---------------------------------------------------------------------------
# More the Merrier — ⭐⭐⭐
# ---------------------------------------------------------------------------
MORE_MERRIER = linear_story({
    "id": "more-the-merrier-thanksgiving",
    "title": "Twenty for Dinner",
    "sourceTitle": "More the Merrier",
    "kind": "movie",
    "synopsis": "Your in-laws, three exes, a missionary cousin, and an estranged sibling all confirm for Thanksgiving. You have one oven and one nerve left. Cook.",
    "releaseYear": 2025,
    "addedAt": "2026-04-02T00:00:00Z",
    "genre": "Comedy",
    "tags": ["holiday", "family", "kitchen"],
    "rating": 3,
    "loved": False,
}, [
    ("Tuesday Morning", "You finalize the guest list. Twenty. The oven is, by spec, sufficient for fifteen.", "Cut the list", "Honest.", "Borrow an oven", "Hospitable."),
    ("The Sibling", "Your estranged sister Anita confirms. She has not been to a family event in seven years. Your stomach drops.", "Call her", "Reach.", "Just plan for her", "Quiet."),
    ("The Ex", "Your spouse's ex confirms because their kids' custody schedule landed here. You agree, reluctantly, because the kids are great.", "Set the seating", "Strategic.", "Let it be casual", "Trust."),
    ("Missionary Cousin", "Your cousin Joel has flown in from Cambodia and would like to give a 'short prayer.' Short, for Joel, is twenty minutes.", "Pre-negotiate the prayer", "Strategic.", "Let Joel be Joel", "Mercy."),
    ("Mom's Plate", "Mom would like, again, the green bean casserole. She would also like it on her plate. She has opinions.", "Make the casserole", "Honor.", "Substitute it", "Risk."),
    ("Grocery Run", "You go to the grocery store and discover that 3 p.m. on the Tuesday before Thanksgiving is, somehow, both apocalypse and prom.", "Make a list", "Discipline.", "Wing it", "Speed."),
    ("Anita's Voicemail", "Anita leaves a voicemail. 'I'm bringing Steve,' she says. Steve is, as far as you know, the man she was supposed to marry seven years ago.", "Welcome Steve", "Grace.", "Ask if you're sure", "Honest."),
    ("Spouse, Stressing", "Your spouse is, professionally, fine. Personally, your spouse is melting. You realize you have been only managing logistics.", "Pause for them", "Care.", "Power through", "Sched."),
    ("The Oven Math", "The math, finally done, is: two ovens. One toaster oven. One spatchcock turkey. Two hours and forty minutes start to finish.", "Spatchcock it", "Aggressive.", "Buy a second small turkey", "Easier."),
    ("Tuesday Night Pie", "You make pies on Tuesday night because Wednesday is going to be hellish. The crust is, mercifully, good.", "Make four pies", "Generous.", "Make three", "Pragmatic."),
    ("Wednesday Arrivals", "Anita arrives Wednesday with Steve, a houseplant, and a kind smile. She hugs you in the driveway. You realize you have been wrong about seven years of something.", "Hug her back fully", "Repair.", "Welcome her warmly but cautiously", "Pace."),
    ("In-Laws", "Your in-laws arrive. They have brought, again, the wrong wine. The wrong wine is, technically, very nice.", "Open the wine", "Generous.", "Save it for Christmas", "Strategic."),
    ("Kids", "Five children, ages 3-12, are now in the house. The 12-year-old has decided, today, to be a vegetarian.", "Pivot a side dish", "Easy.", "Add a vegetarian main", "Hospitable."),
    ("Thanksgiving Morning", "5:30 a.m. The turkey goes in. You make coffee. The kitchen window goes gold.", "Sit at the window for ten minutes", "Calm.", "Start the next thing", "Move."),
    ("The Spat", "Mom and your spouse have a brief, vicious exchange about the green bean casserole. Anita is the one who, somehow, fixes it.", "Thank Anita publicly later", "Honor.", "Just be grateful", "Quiet."),
    ("The Toast", "You give the toast. You decide, in the moment, what kind of family you'd like this to be.", "Be honest and warm", "Brave.", "Be sweet and short", "Mercy."),
    ("Joel's Prayer", "Joel's prayer is, mercifully, only six minutes. He blesses Anita and Steve specifically. Anita cries.", "Hold her hand", "Family.", "Pretend not to notice the tear", "Mercy."),
    ("The Meal", "The meal is, somehow, on time. The turkey is, somehow, juicy. The casserole, finally, is on Mom's plate. She does not, however, say thank you. She doesn't have to.", "Sit down", "Win.", "Refill the wine", "Hospitable."),
    ("The Ex, At the Table", "Your spouse's ex tells a small joke. Everyone laughs. The kids, for one beautiful minute, treat their two-household family as a one-table family.", "Notice it", "Witness.", "Just let it be", "Trust."),
    ("After-Dinner Cleanup", "Anita does dishes with you. You and she talk for an hour about nothing important and everything important. Seven years closes.", "Invite her for Christmas", "Continue.", "Take it one holiday at a time", "Slow."),
    ("The Last Pie", "Late. House half-asleep. You and your spouse cut the last pie at midnight at the kitchen island.", "Eat the pie together", "Marriage.", "Save it for tomorrow", "Discipline."),
], [
    ("end_family", "Family Re-Made", "Anita comes for Christmas. Then Easter. Then everything. The family is, somehow, both bigger and easier. Mom, eventually, asks for Anita's casserole recipe."),
    ("end_smaller", "Smaller Next Year", "Next year you do a smaller Thanksgiving on purpose — just the immediate house and Anita and Steve. It is, by every measurement, more fun and less hot."),
    ("end_recipes", "The Recipe Book", "Years later you compile a small family recipe book. Mom's casserole is on page two. Joel's overlong prayer is, somehow, a chapter. Anita writes the introduction. You all laugh at it on Thanksgivings to come."),
])


# ---------------------------------------------------------------------------
# Scream 7 — ⭐⭐⭐
# ---------------------------------------------------------------------------
SCREAM_7 = linear_story({
    "id": "scream-7-the-podcast",
    "title": "The Podcast Killer",
    "sourceTitle": "Scream",
    "kind": "movie",
    "synopsis": "Woodsboro's grown up. You host a true-crime podcast about the original killings. A new ghostface debuts on your live stream. Don't pick up the phone.",
    "releaseYear": 2026,
    "addedAt": "2026-04-01T00:00:00Z",
    "genre": "Thriller",
    "tags": ["meta", "slasher", "podcast"],
    "rating": 3,
    "loved": False,
}, [
    ("Live Stream Drop", "Episode 102 goes live. The new ghostface enters the chat. Your moderators ban them. They come back.", "Continue the show", "Brave.", "End the stream", "Smart."),
    ("Your Co-Host", "Your co-host Kira is, against your judgement, into it. She thinks it's an in-character troll.", "Trust your gut", "Skeptical.", "Trust Kira", "Friend."),
    ("Detective Bailey", "Detective Bailey, who appeared in three earlier Screams, is now a Lieutenant. She calls. She is, professionally, tired.", "Cooperate", "Right.", "Get a lawyer first", "Cautious."),
    ("The Call", "A landline rings at 11 p.m. The number is from your old neighborhood.", "Pick up", "Brave.", "Let it ring", "Smart."),
    ("Kira's Apartment", "Kira's apartment is, suddenly, the scene of a thing. She is okay. The thing happened just before she arrived.", "Go to Kira", "Friend.", "Stay home", "Pragmatic."),
    ("Sidney", "Sidney Prescott, retired, calls you. She has, she says, seen this pattern. She is, professionally, the expert.", "Take her advice", "Honor.", "Politely thank her", "Independence."),
    ("The Podcast Numbers", "Your podcast numbers triple. Your sponsor wants you to lean in. You realize you are, accidentally, fueling the killer's brand.", "Tone it down", "Honor.", "Lean in with a disclaimer", "Hybrid."),
    ("Ghostface, Online", "Ghostface starts a Twitter account. The bio is a single emoji. Six hundred thousand followers in three hours.", "Don't engage online", "Discipline.", "Engage carefully", "Strategic."),
    ("The Suspect", "Your ex-boyfriend's brother is in town. He hates you, for unrelated reasons. He is, in a way you don't want to be true, also charming.", "Watch him", "Smart.", "Confront him", "Brave."),
    ("Knife Pattern", "Bailey hands you a forensic report. The pattern of the killings matches not Ghostface 1 but Ghostface 3. Someone is, in fact, doing their homework.", "Use that publicly", "Bait them.", "Hold it back", "Discipline."),
    ("The Live Show", "Your studio has invited a live audience for tonight's special. Bailey wants to cancel. Your producer wants to scale it up.", "Cancel", "Smart.", "Scale up with security", "Strategic."),
    ("Backstage", "Backstage you see, in the hallway, a glimpse of a face you recognize from the chat. You don't, at first, know from where.", "Investigate quietly", "Tactical.", "Tell security immediately", "Right."),
    ("Sidney, on Set", "Sidney shows up. The audience gasps. She is gracious. She is also armed.", "Defer to her", "Sense.", "Co-host with her", "Equal."),
    ("The Phone, on Air", "The phone, on the live stream, rings. The producer, after a beat, puts it through. Ghostface, on the line, has questions.", "Answer carefully", "Strategy.", "Refuse to engage", "Power."),
    ("The Hostage", "The killer, on air, reveals they have your co-host's mother. The audience is in the studio. The clock is ticking.", "Negotiate", "Buy time.", "Have security move", "Action."),
    ("The Trap", "Bailey has, mercifully, set a trap. The trap requires you to keep talking. The trap requires you to do exactly the thing you're terrified to do.", "Keep talking", "Brave.", "Tap out", "Honest."),
    ("Studio Lights Out", "Lights out. The room is, briefly, a maze. You learn that everyone you trust is alive. You learn that one person you didn't trust is, in fact, the killer.", "Confront", "Brave.", "Stay still", "Smart."),
    ("Final Reveal", "Two killers. The pattern, again. Ghostface motives are, this time, more banal than usual. The reveal is, by Sidney's calm voice, almost anti-climactic.", "Confront calmly", "Trust Sidney.", "Improvise", "Adrenaline."),
    ("After the Show", "The show is over. The bodies are off. The cameras are still rolling. You realize the entire night was, somehow, a podcast episode.", "End the podcast forever", "Brave.", "Take a long break", "Pace."),
    ("Sidney's Hug", "Sidney, on the way out, hugs you. She says, simply, 'Don't make a sequel.' You know what she means.", "Listen to her", "Honor.", "Make something different", "Pivot."),
    ("Therapy", "You find a good therapist. The therapist has, mercifully, no idea who you are. You like that.", "Stay in therapy", "Smart.", "Process privately", "Personal."),
], [
    ("end_quit", "Off the Mic", "You retire from podcasting. You move out of Woodsboro. You become, weirdly, a person who teaches yoga. Sidney, of all people, comes to a class. She is, somehow, terrible at it. You laugh."),
    ("end_pivot", "A Different Show", "You start a new podcast about people who survived horrible things. The show is, in its quiet way, hopeful. It outperforms your old one. You are, mercifully, less of a brand."),
    ("end_sidney", "Sidney, Mentor", "Sidney becomes, in a strange way, your mentor. You meet for coffee twice a year. She gives you advice you do not, at the time, want to take but, in the end, always do."),
])


# ---------------------------------------------------------------------------
# The Bluff — ⭐⭐⭐
# ---------------------------------------------------------------------------
THE_BLUFF = linear_story({
    "id": "the-bluff-the-game",
    "title": "The Game",
    "sourceTitle": "The Bluff",
    "kind": "movie",
    "synopsis": "You're a retired pirate captain living quietly in the Caribbean. The British Navy has docked. So has your old daughter. So has your old life.",
    "releaseYear": 2025,
    "addedAt": "2026-03-31T00:00:00Z",
    "genre": "Action",
    "tags": ["pirate", "family", "retirement"],
    "rating": 3,
    "loved": False,
}, [
    ("The Cove", "The cove is quiet. You sit on a porch with a leg up. The harbor, on the horizon, has more sails than it had yesterday.", "Watch them", "Wise.", "Get the gun", "Cautious."),
    ("The Daughter", "She walks up your beach in trousers and a cutlass. She is taller. She is also, you can tell, angry.", "Welcome her", "Honest.", "Brace yourself", "Smart."),
    ("The Navy", "Captain Hayes of the British Navy has, with his crew, taken your old port. He has a writ in his pocket and a small smile.", "Read the writ", "Honor.", "Refuse to read it", "Pride."),
    ("The Bar", "The town bar is owned by an old shipmate of yours, Maria. She is, in this scene, the only honest person you know.", "Tell Maria everything", "Trust.", "Tell her half", "Save half."),
    ("The Daughter, Honest", "Your daughter, drunk, finally tells you why she came. The reason is a ship, a mission, and a name from your past.", "Listen", "Patient.", "Push back", "Pride."),
    ("Old Crew", "Five of your old crew are alive. Two are in Havana. Two are in Tortuga. One is, embarrassingly, also retired three coves down.", "Call them", "Reunion.", "Plan without them", "Solo."),
    ("Hayes' Move", "Hayes offers you a deal. The deal is, by the standards of the navy, generous. The deal is, by the standards of your daughter, an insult.", "Take the deal", "Pragmatic.", "Refuse", "Honor."),
    ("Maria's Schooner", "Maria has, in her back-room, a schooner you didn't know she had. She has, you realize, been retired in the loud sense — actively.", "Use the schooner", "Asset.", "Decline the schooner", "Don't drag her in."),
    ("The Mission", "Your daughter's mission, finally explained: a stolen something, a hostage, a ledger that, if released, would end Hayes' career.", "Help her", "Family.", "Negotiate first", "Practical."),
    ("Sail", "You sail. The first hours feel old. By the second day you are, weirdly, twenty again, in a body that is fifty.", "Push hard", "Memory.", "Pace yourself", "Wisdom."),
    ("Hayes' Pursuit", "Hayes, on a larger ship, follows. He is faster on open water. You know smaller channels.", "Take the channels", "Local.", "Outrun on open water", "Confidence."),
    ("Storm", "A storm finds you. The schooner, by Maria's calm, survives. So do you.", "Push through", "Brave.", "Wait it out", "Wise."),
    ("Tortuga Friends", "Your old crew in Tortuga joins. They are older, slower, more dangerous. The reunion is, briefly, the best night of your decade.", "Tell them the plan", "Honest.", "Let them think it's bigger", "Recruit."),
    ("The Ledger Hide", "The ledger is hidden, by your daughter's intelligence, in a chapel. The chapel is also, you realize, where you were married.", "Go in", "Memory.", "Have her go in", "Strategy."),
    ("Confrontation, Mid-Sea", "Hayes finds you mid-sea. The two ships, briefly, are within hailing distance.", "Hail him", "Words.", "Maneuver away", "Action."),
    ("The Hostage", "The hostage, recovered, turns out to be the wife of a man you once wronged. She forgives you immediately. You realize forgiveness travels strangely.", "Apologize", "Honor.", "Just nod", "Quiet."),
    ("Hayes, Cornered", "Hayes' ship runs aground in your channels. He is alive. He is also, in this corner of the world, not safe.", "Spare him", "Mercy.", "Take him prisoner", "Pragmatic."),
    ("The Town, Looking", "The town watches from the dock as you sail back in. The crowd is, somehow, applauding.", "Bow", "Style.", "Pretend not to notice", "Style."),
    ("Maria's Bar", "Maria pours rum. The crew, your daughter, and you sit at the long table. You realize you have a family you did not, last week, know you had.", "Stay", "Family.", "Promise to come back", "Honest."),
    ("Hayes' Letter", "A formal letter from the Navy. It is, against expectation, a pardon. You realize Hayes wrote it himself.", "Accept", "Honor.", "Frame it but stay private", "Smart."),
    ("Your Daughter", "She tells you, on the porch, that she will visit again. You tell her you will let her go without making a scene about it. You make a small scene anyway.", "Make the scene short", "Mercy.", "Make the scene plain", "Honest."),
], [
    ("end_retired", "Truly Retired", "You stay in your cove. The bar keeps you in rum. Maria keeps you in stories. Your daughter visits twice a year. The waves do, in fact, ignore you mostly. You like that."),
    ("end_crew", "The Old Crew", "You sail occasionally — small jobs, smaller crews — and become, in time, a kind of grandfather to a new generation of sailors. The Navy, by treaty and convenience, leaves you alone."),
    ("end_chapel", "The Chapel, Again", "You marry, late, a woman you should have married decades earlier. Maria officiates because nobody else is left. The chapel — same one — laughs at you, kindly, when the kiss takes too long."),
])


# ---------------------------------------------------------------------------
# Scary Movie 3 — ⭐⭐
# ---------------------------------------------------------------------------
SCARY_MOVIE_3 = linear_story({
    "id": "scary-movie-3-the-cycle",
    "title": "The Tape and the Crop Circles",
    "sourceTitle": "Scary Movie 3",
    "kind": "movie",
    "synopsis": "There's a tape that kills you a week after you watch it. There are crop circles in your uncle's field. There is a rapper named George. Solve all three.",
    "releaseYear": 2003,
    "addedAt": "2026-03-30T00:00:00Z",
    "genre": "Comedy",
    "tags": ["parody", "absurd", "the-ring"],
    "rating": 2,
    "loved": False,
}, [
    ("The Tape", "Your friend Brenda hands you the cursed tape. The cursed tape is, technically, a VHS. You haven't owned a VCR in years.", "Find a VCR", "Plot.", "Refuse the tape", "Wise."),
    ("The VCR", "A pawn shop has a VCR. The pawn shop owner is also a rapper.", "Buy the VCR", "Plot.", "Take the rapper's number", "Style."),
    ("The Watch", "You watch the tape. It is grainy. It is also, you realize, a karaoke video for a song you don't know.", "Try to identify the song", "Investigate.", "Just turn it off", "Wise."),
    ("Cindy", "Cindy, the protagonist of every Scary Movie, calls. She has been trying to call you for two films.", "Pick up", "Plot.", "Let it go to voicemail", "Style."),
    ("The Field", "Your uncle's cornfield has new crop circles. The circles, drawn by aliens, are also a math joke.", "Solve the math", "Brave.", "Take a photo", "Tourist."),
    ("The Priest", "Father Muldoon has, in his rectory, both an exorcism kit and a karaoke machine. They are, surprisingly, related.", "Use the karaoke", "Plot.", "Use the kit", "Plot."),
    ("The Aliens", "The aliens, polite, show up at the cornfield. They have a complaint. The complaint is, technically, valid.", "Hear them out", "Civil.", "Apologize on behalf of humanity", "Generous."),
    ("Tabitha", "The girl from the tape, Tabitha, climbs out of a TV. She is, off-camera, exhausted.", "Make her tea", "Civil.", "Apologize", "Polite."),
    ("Sue's Rap Battle", "You end up in a rap battle. You don't know how. The rules are, somehow, clear.", "Battle", "Brave.", "Forfeit", "Wise."),
    ("Brenda", "Brenda has been killed by the tape. She is, however, alive in this scene. The continuity is, again, doing its best.", "Just go with it", "Style.", "Question it", "Comedy."),
    ("The President", "The President — also the protagonist of the parody — is, today, addressing the nation. He has, on his desk, a chicken.", "Brief him", "Plot.", "Take the chicken", "Plot."),
    ("Press Briefing", "The press briefing involves, accidentally, the President saying the cursed tape song out loud. The press laughs. The aliens cry.", "Stop the briefing", "Civic.", "Let it finish", "Comedy."),
    ("Cindy's Plan", "Cindy proposes a plan. The plan involves Tabitha and the karaoke machine and the rap battle.", "Adopt the plan", "Trust.", "Modify the plan", "Improve."),
    ("Mac and Tabitha", "Tabitha's mother, somewhere, wants to be apologized to. Tabitha is, technically, the saddest character in the movie.", "Apologize to Tabitha's mother", "Honor.", "Apologize to Tabitha", "Direct."),
    ("Karaoke Showdown", "The final showdown is a karaoke night at the local bar. The aliens are surprisingly good at backup.", "Sing", "Brave.", "Lip sync", "Wise."),
    ("The Tape's Origin", "The tape, finally, plays its full original recording. The recording is, in fact, a 1976 wedding video.", "Reunite the wedding party", "Plot.", "Just delete the file", "Modern."),
    ("Aliens Negotiate", "The aliens, satisfied, leave. They take with them, oddly, the chicken.", "Wave goodbye", "Civil.", "Run for the cornfield", "Comedy."),
    ("Sue, Rapping", "Sue ends the movie with a freestyle rap about closure, family, and cursed VHS tapes.", "Drop the mic", "Style.", "Bow", "Style."),
    ("Roll Credits", "Credits roll. Bloopers. A cameo by an alien who clearly didn't sign the release.", "Stay for bloopers", "Loyal.", "Leave the theater", "Practical."),
    ("Tabitha's Mother", "Tabitha's mother, played by a famous comedian, hugs you. The hug, on screen, is the best joke of the movie.", "Hug back", "Civil.", "Just smile", "Style."),
    ("Sequel Tease", "A title card promises Scary Movie 4. Everyone, including the chicken, is back next year.", "Plan to attend", "Loyal.", "Skip the sequel", "Wise."),
], [
    ("end_sing", "Karaoke Champion", "You become the karaoke champion of the county. The cursed tape, in fact, is the song that keeps winning."),
    ("end_aliens", "The Aliens Move In", "The aliens decide to move in with you. They are, in fact, polite tenants. They pay rent in interstellar shrimp."),
    ("end_wedding", "The 1976 Wedding", "You attend the actual 1976 wedding via a time-travel sequence you can't quite explain. You realize the cursed tape was, all along, family content."),
])


# ---------------------------------------------------------------------------
# Scary Movie 5 — ⭐⭐
# ---------------------------------------------------------------------------
SCARY_MOVIE_5 = linear_story({
    "id": "scary-movie-5-the-cabin",
    "title": "Cabin in the Woods, Again",
    "sourceTitle": "Scary Movie 5",
    "kind": "movie",
    "synopsis": "A cabin in the woods, three found children, and a possessed Roomba. You and your spouse just wanted a vacation.",
    "releaseYear": 2013,
    "addedAt": "2026-03-29T00:00:00Z",
    "genre": "Comedy",
    "tags": ["parody", "absurd", "cabin"],
    "rating": 2,
    "loved": False,
}, [
    ("Adopting Children", "You adopt three found children. They are feral. The Department of Adoptions is, mostly, a sign.", "Adopt them all", "Brave.", "Adopt one", "Wise."),
    ("Cabin Reservation", "The Airbnb description includes 'minor haunting.' The reviews are, on balance, kind.", "Book it", "Plot.", "Read the reviews carefully", "Wise."),
    ("Roomba", "The Roomba turns itself on at 3 a.m. and chases you. The Roomba is, technically, possessed.", "Sit on the couch", "Smart.", "Run", "Plot."),
    ("Found Footage", "Cameras everywhere. The cabin records you constantly. You realize, eventually, this is for a streaming show.", "Talk to camera", "Style.", "Cover the cameras", "Wise."),
    ("Snow White Princess", "A princess shows up. She does, technically, sing. She also, technically, is in a sex scene with a deer.", "Be polite", "Civil.", "Decline the dance", "Wise."),
    ("The Children, Feral", "The children eat your shoes and a cake. The cake was the dog's.", "Discipline gently", "Parental.", "Cry", "Honest."),
    ("Mama Ghost", "The ghost is named Mama. Mama is, on balance, supportive. She would like, ideally, the cabin returned to her by the weekend.", "Negotiate with Mama", "Plot.", "Move out", "Wise."),
    ("Black Swan Bit", "A spoof of Black Swan in the bathroom mirror. You realize, briefly, that you are also a spoof of yourself.", "Dance", "Style.", "Just brush your teeth", "Wise."),
    ("Inception Spoof", "A dream-within-a-dream sequence. You wake up six times. The sixth time you actually wake up, you are unsure.", "Pinch yourself", "Wise.", "Spin a top", "Plot."),
    ("Paranormal Activity", "A camera in the bedroom records you sleeping. It is, somehow, judging you.", "Cover the camera", "Smart.", "Ignore it", "Style."),
    ("Insidious Spoof", "A ghost in the closet wants to know your password. Your password is, embarrassingly, 'password123.'", "Change it", "Smart.", "Give it to the ghost", "Generous."),
    ("Sinister", "A series of home movies you don't remember filming. They are all of the dog. The dog has, somehow, a secret life.", "Question the dog", "Plot.", "Just let the dog live", "Trust."),
    ("Mama, Reconciled", "Mama and you, over tea, reach an understanding. She gets the cabin Tuesdays. You get Wednesdays. The children, somehow, are on board.", "Sign the agreement", "Practical.", "Send Mama away", "Plot."),
    ("Children, Less Feral", "The children, over time, become children. The cake-eating becomes pie-baking. The shoe-eating becomes, mostly, shoe-tying.", "Take pride", "Honest.", "Take credit", "Style."),
    ("The Streaming Show", "The streaming show airs. You are, on balance, the funny one. The dog is the breakout star.", "Sign for season two", "Style.", "Decline", "Wise."),
    ("Dance Number", "An unnecessary musical dance number. The children participate. The Roomba does a solo.", "Cherish it", "Honest.", "Pretend it didn't happen", "Style."),
    ("Final Confrontation", "Mama, the Roomba, the deer, and the dog all stand in the kitchen at the same time. Family photo.", "Take the photo", "Style.", "Just be there", "Honest."),
    ("Hospital Sequence", "A bizarre dream-hospital sequence in which nothing means anything and everything is, somehow, funny.", "Laugh", "Style.", "Be confused", "Honest."),
    ("Wedding", "You and your spouse, somewhere in the third act, re-marry on a beach. Mama officiates. The Roomba carries the rings.", "Cry", "Civil.", "Laugh", "Style."),
    ("Bloopers", "Bloopers roll. The Roomba refuses to perform. The deer falls asleep on set.", "Stay for bloopers", "Loyal.", "Leave", "Practical."),
    ("Sequel Hook", "A title card promises another sequel. The dog winks. The Roomba sighs.", "Wink back", "Style.", "Look away", "Civil."),
], [
    ("end_family", "Cabin Family", "You keep the cabin. Mama and the dog and the Roomba and the children become, in a real sense, a family. The streaming show runs for six seasons."),
    ("end_quiet", "Suburbs Again", "You move back to the suburbs. The children, settled, become weirdly normal. You take up gardening. Mama, sometimes, visits."),
    ("end_deer", "The Deer's Spinoff", "The deer, against all reason, gets a spinoff. You serve as executive producer. It is the highest-rated show of the year. Nobody at the Emmys asks you any questions you can answer."),
])


# ---------------------------------------------------------------------------
# Tell Me Lies — ⭐
# ---------------------------------------------------------------------------
TELL_ME_LIES = linear_story({
    "id": "tell-me-lies-the-friendship",
    "title": "The Group Chat",
    "sourceTitle": "Tell Me Lies",
    "kind": "show",
    "synopsis": "Eight years out of college. Your best friend is engaged to the man who ruined your twenties. The bachelorette weekend is in three weeks.",
    "releaseYear": 2024,
    "addedAt": "2026-03-28T00:00:00Z",
    "genre": "Drama",
    "tags": ["college", "drama", "friendship"],
    "rating": 1,
    "loved": False,
}, [
    ("The Invite", "The bachelorette invite arrives by email. The names on the list include yours, and his sister's, and people you have not spoken to since graduation.",
     "Reply yes", "Friend.", "Stall", "Smart."),
    ("Your Therapist", "Your therapist is, today, professionally curious. She asks whether you have ever, fully, told your best friend about him.", "No", "Honest.", "Mostly", "Half."),
    ("The Group Chat", "The group chat is, against all instincts, friendly. People you stopped talking to in 2018 are, again, on a thread.", "Engage", "Friend.", "Mute", "Self."),
    ("The Sister", "His sister, who never liked you, writes you a private DM. The DM is, surprisingly, kind.", "Reply warmly", "Risk.", "Reply minimally", "Caution."),
    ("Your Spouse", "Your spouse is supportive in the way only a spouse can be. They also, gently, want to know what you actually want.", "Tell them honestly", "Marriage.", "Promise to figure it out", "Process."),
    ("The Bachelorette Plan", "The plan is a winery weekend. The plan includes, at the explicit request of the bride, no boyfriends/husbands.", "Commit to going", "Friend.", "Hold off", "Wait."),
    ("The Bride, Calling", "Your best friend calls. She has, she says, been afraid to ask you. She wants to know if you'll be okay.", "Tell her yes", "Cover.", "Tell her you need to talk", "Honest."),
    ("Coffee with Her", "You meet for coffee. You decide whether to tell her everything you never told her about her fiancé.", "Tell her", "Brave.", "Tell her part", "Half."),
    ("His Email", "He emails you, unprompted. The email is, in a way you don't want to be true, charming.", "Don't reply", "Discipline.", "Reply with a single sentence", "Closure."),
    ("Your Old Notebook", "You find your old college notebook. It is, in a real way, evidence. You read it.", "Burn it", "Closure.", "Keep it", "Memory."),
    ("Other Friends, Listening", "Two friends from the group chat — Pippa and Bree — invite you to dinner separately. They want, in different ways, to support you.", "Lean on both", "Allies.", "Pick the safer one", "Triage."),
    ("Pre-Bachelorette Drinks", "Pre-bachelorette drinks in the city. The bride is, you realize, happy. You decide what to do with that.", "Be glad for her", "Generous.", "Watch for the signs", "Cautious."),
    ("Winery Weekend, Friday", "You arrive at the winery. He is not there. The weekend, briefly, is just women you love.", "Enjoy the day", "Present.", "Stay vigilant", "Strategic."),
    ("Late Night Talk", "Late on Friday night, the bride and you sit on a balcony and talk. You decide what to tell her now.", "Tell her", "Brave.", "Hold off", "Strategic."),
    ("Saturday Hike", "Saturday is a hike. You realize, on the trail, that the weekend is also a kind of healing for you.", "Receive it", "Honest.", "Stay guarded", "Smart."),
    ("Dinner, Saturday Night", "Dinner. Toasts. People give speeches. You realize what kind of speech you'd give if asked.", "Volunteer to speak", "Brave.", "Stay quiet", "Smart."),
    ("Pippa's Honesty", "Pippa, drunk, tells you what she always thought of him. You realize, with a strange relief, you weren't alone.", "Compare notes", "Honest.", "Just listen", "Care."),
    ("Sunday Morning", "Sunday morning. Coffee. Hangover. Bride beside you on the porch. You decide what kind of friend you're going to be for the next year.", "Be fully honest now", "Brave.", "Be present and patient", "Honor."),
    ("The Wedding Date", "The wedding date is in five months. You decide whether you'll be there.", "Be there", "Friend.", "Decline", "Self."),
    ("His Last Email", "He emails again. The email is, this time, an apology. You read it twice. You decide what it deserves.", "Forgive privately", "Closure.", "Don't reply", "Discipline."),
    ("Your Spouse, Returning Home", "You come home Sunday night. Your spouse hugs you. You realize you have, finally, the family you wanted in college.", "Tell them everything about the weekend", "Marriage.", "Just be home", "Quiet."),
], [
    ("end_friend", "Best Friend, Still", "You stay her best friend. You attend the wedding. The marriage, predictably, does not last. She moves to your city when it ends. You walk her dog the first month."),
    ("end_self", "Quietly Yours", "You let the friendship dim. You realize, slowly, that some friendships don't survive twenties' damage. Your spouse, and the small life you built, becomes the center."),
    ("end_honest", "Honest, At Last", "You tell her, fully, what happened in college. The friendship survives, barely, then heals. The wedding is, in the end, not what it would have been. You realize, late, that you protected her by being honest."),
])


# ---------------------------------------------------------------------------
# A Wrinkle in Time — ⭐
# ---------------------------------------------------------------------------
WRINKLE_TIME = linear_story({
    "id": "wrinkle-time-the-tesseract",
    "title": "Wrinkle",
    "sourceTitle": "A Wrinkle in Time",
    "kind": "movie",
    "synopsis": "Your dad disappeared into space-time. Three strange Mrs Ws are at the door. The tesseract is, apparently, a verb. Go find him.",
    "releaseYear": 2018,
    "addedAt": "2026-03-27T00:00:00Z",
    "genre": "Fantasy",
    "tags": ["children", "physics", "love"],
    "rating": 1,
    "loved": False,
}, [
    ("The Door", "Mrs Whatsit is at the door in a thunderstorm. She mentions a tesseract. You realize you are, technically, in a novel.", "Listen", "Brave.", "Stay polite", "Civil."),
    ("Charles Wallace", "Your tiny brother Charles Wallace, somehow, has been corresponding with all three Mrs Ws by name.", "Trust him", "Family.", "Question him", "Cautious."),
    ("Calvin", "A schoolmate named Calvin shows up because, the Mrs Ws say, he's part of it. He is, surprisingly, nice.", "Welcome him", "Friend.", "Be suspicious", "Smart."),
    ("Mrs Who's Quote", "Mrs Who speaks only in quotations. The quotations are, in places, useful.", "Note them", "Smart.", "Just listen", "Style."),
    ("First Tesseract", "You tesseract. The sensation is unpleasant. You arrive on a planet with too many flowers.", "Smell a flower", "Curious.", "Don't touch anything", "Wise."),
    ("Uriel", "Uriel is, apparently, the good place. You meet a centaur who explains evil as a darkness across the universe.", "Look at the darkness", "Brave.", "Don't look", "Smart."),
    ("Camazotz Glimpse", "You glimpse Camazotz, the dark planet. Your dad is on it. The darkness, you realize, eats things slowly.", "Vow to go", "Brave.", "Demand a plan first", "Smart."),
    ("Mrs Whatsit's Form", "Mrs Whatsit transforms into a creature with wings. Charles Wallace, on her back, is, you realize, exactly his happiest.", "Ride her", "Brave.", "Walk", "Honest."),
    ("Happy Medium", "The Happy Medium has, in his cave, a crystal ball that shows your father. He is alive. He is also a long way away.", "Believe it", "Hope.", "Verify it", "Smart."),
    ("Camazotz Approach", "You and Charles Wallace and Calvin approach Camazotz. The planet looks, ominously, like a suburb.", "Walk in", "Brave.", "Sneak in", "Smart."),
    ("Identical Children", "Children bouncing identical balls in identical rhythms. Charles Wallace, you realize, is in danger of being absorbed.", "Hold his hand tight", "Family.", "Distract him", "Smart."),
    ("Central Intelligence", "The CENTRAL Intelligence building is, on the map, the center of evil. You go in.", "Take the front door", "Brave.", "Find another way", "Smart."),
    ("Charles Wallace, Taken", "Charles Wallace is taken by IT. He talks in a flat voice. He is, technically, still your brother.", "Fight to bring him back", "Brave.", "Negotiate with IT", "Strategic."),
    ("Your Father", "You find your father in a clear column. He is older, gaunter, alive. He doesn't, for a second, recognize you.", "Speak his name", "Family.", "Hug him", "Honor."),
    ("The Way Out", "The way out, as ever, is the way you came in. The way out is also, this time, harder.", "Carry Charles Wallace", "Brave.", "Coax him out", "Patient."),
    ("Mrs Which's Voice", "Mrs Which, the oldest of the three, finally speaks. Her voice is slow and heavy. The advice, by now, is one word: love.", "Use love", "Yes.", "Use love and a plan", "Both."),
    ("Charles Wallace, Returning", "Your love, plainly and embarrassingly out loud, reaches him. He blinks. The flatness retreats.", "Hold him", "Family.", "Get him moving", "Smart."),
    ("The Run", "You run. The corridors of CENTRAL fold and unfold. The Mrs Ws are, in the corner of your eye, helping.", "Trust them", "Honor.", "Trust your feet", "Pragmatic."),
    ("Back on Uriel", "You arrive back on Uriel briefly. The Mrs Ws thank you. Charles Wallace, weirdly, asks for a sandwich.", "Make the sandwich", "Family.", "Promise one at home", "Practical."),
    ("Home", "You land in your front yard. Mom comes out screaming. Dad is, this time, in the picture in a way he hasn't been in years.", "Hug everyone", "Family.", "Sit on the porch and breathe", "Honest."),
    ("School, Monday", "You go back to school Monday. People don't believe what you tell them. You decide what you'll tell them now.", "Tell the truth", "Brave.", "Stay quiet", "Smart."),
], [
    ("end_quiet", "Quietly Strange", "You become, in your school, the slightly strange kid. Calvin, mercifully, becomes the slightly strange kid too. You are, at fourteen, a small good resistance to whatever darkness is closest."),
    ("end_writer", "The Book", "You write, decades later, a book about it. The book is, in fact, the one you read as a kid. The cycle closes."),
    ("end_family", "Family, Finally", "Your dad stays. Charles Wallace, less weird than he was, grows up. Calvin marries you, in a long-running joke that becomes a real thing. The Mrs Ws send Christmas cards. Mrs Who's are in three languages."),
])


# ===========================================================================
# FAMOUS MOVIES — top 25 by global fame
# ===========================================================================

GODFATHER = linear_story({
    "id": "fm-godfather", "title": "The Godfather", "sourceTitle": "The Godfather",
    "kind": "movie", "synopsis": "A wedding. A horse's head. A war between five families. You're the youngest son. The family business is, finally, calling you.",
    "releaseYear": 1972, "addedAt": "2026-03-26T00:00:00Z", "genre": "Drama",
    "tags": ["mafia", "family", "classic"], "rating": None, "loved": False,
}, [
    ("The Wedding", "Connie's wedding. Sicilians believe no Sicilian can refuse a request on a wedding day. Your father takes meetings in a dark study.", "Stay outside with Kay", "Distance.", "Watch from the doorway", "Observe."),
    ("Kay's Question", "Kay asks who that man is. You tell her. You tell her, then, that this isn't your life.", "Mean it", "Naive.", "Half-mean it", "Honest."),
    ("Solozzo's Offer", "A man named Solozzo wants the family in the heroin business. Your father says no. You realize the word 'no' has a price.", "Trust your father's reading", "Respect.", "Argue for caution", "Modern."),
    ("The Hospital", "Your father has been shot. The hospital is empty of guards. You stand in his room alone.", "Improvise protection", "Brave.", "Call Sonny first", "Process."),
    ("Police Captain", "McCluskey breaks your jaw. The family is, suddenly, at war with a captain of police.", "Plan revenge cold", "Strategic.", "Burn with anger", "Hot."),
    ("The Restaurant", "Solozzo and McCluskey. Italian restaurant. Gun taped behind the toilet. The walls hum.", "Do it", "Cross.", "Walk out", "Refuse."),
    ("Sicily", "You hide in Sicily. The hills are beautiful. You meet Apollonia. You realize you can almost have a different life.", "Marry her", "Heart.", "Stay alone", "Mind."),
    ("The Bomb", "Apollonia is killed by a bomb meant for you. You stand by the wreckage. Something inside closes for good.", "Vow vengeance", "Sicilian.", "Vow only to return strong", "Strategic."),
    ("Home", "Back in New York. Kay waits. You ask her to trust you. She does, with conditions.", "Promise the family will go legitimate", "Lie kindly.", "Promise nothing", "Honest."),
    ("Sonny's Death", "Sonny is killed on a tollbooth highway, riddled. Your father, broken, sits with you in the garden.", "Take charge of the family", "Heir.", "Stay in the shadows", "Power."),
    ("Don Corleone's Peace", "Your father, old, asks for a meeting of the five families. He brokers peace. He gets to live, briefly.", "Watch him lead", "Learn.", "Lead beside him", "Equal."),
    ("Tom Hagen", "Tom, consigliere, briefs you. You realize Tessio has betrayed the family.", "Confirm it carefully", "Patient.", "Move now", "Speed."),
    ("Wedding, Yours", "You marry Kay. The ceremony is in English. Your father, at the reception, dances with her.", "Honor him", "Son.", "Plan", "Don."),
    ("The Garden", "Your father, retired, plays with your son in the tomato garden. He dies there, peacefully. You hold his hand last.", "Promise him to honor the family", "Vow.", "Promise yourself to be different", "Modern."),
    ("Plan", "Tom and you, in the kitchen, plan the strike. Every head of every family. One day. The same day Connie's son is baptized.", "Approve every name", "Cold.", "Spare one", "Mercy."),
    ("Baptism", "You renounce Satan in the church. At the same moment, across the city, your enemies fall.", "Mean the renunciation", "Self-deceit.", "Don't mean it", "Honest."),
    ("Carlo", "Carlo, who betrayed Sonny, sits in your car. He weeps. He admits it. You let him die.", "Tell yourself it was justice", "Story.", "Tell yourself nothing", "Cold."),
    ("Kay's Question, Again", "Kay asks if you killed Connie's husband. You look her in the eye and lie.", "Tell the kindest lie", "Marriage.", "Tell a clean lie", "Don."),
    ("The Door", "The family men kiss your hand. They call you Don. Kay sees through a doorway. The door closes.", "Notice the door closing", "Witness.", "Don't notice", "Power."),
    ("Years Later", "You have built an empire. You have buried friends. Your son will not know what you have done. You have, you tell yourself, done it for him.", "Believe it", "Story.", "Don't believe it", "Truth."),
    ("Alone in the Study", "You sit in your father's chair. The chair fits, now. You decide what kind of Don you are going to be.", "The cold one", "Power.", "The fair one", "Honor."),
], [
    ("end_don", "The Don", "You rule for thirty years. The family is feared and quiet. Kay leaves, eventually. Your children grow up American, ignorant. You are alone with the work."),
    ("end_legitimate", "Legitimate, Eventually", "Over twenty years you move the family into Vegas, real estate, banks. Your grandchildren are senators. The history is, by then, forgivable."),
    ("end_father", "Like My Father", "You die in a tomato garden, old, with a grandchild on your knee. The Don you became, in the end, was kinder than the one you intended. You take that as a small, final victory."),
])

SHAWSHANK = linear_story({
    "id": "fm-shawshank", "title": "The Shawshank Redemption", "sourceTitle": "The Shawshank Redemption",
    "kind": "movie", "synopsis": "You're convicted of a murder you didn't commit. Twenty years in Shawshank Prison. Hope is the most dangerous thing they let you carry.",
    "releaseYear": 1994, "addedAt": "2026-03-25T00:00:00Z", "genre": "Drama",
    "tags": ["prison", "hope", "friendship"], "rating": None, "loved": False,
}, [
    ("The Sentence", "Two life terms. The judge does not look at you. Your wife is dead. You did not kill her.", "Plead innocent", "Honor.", "Stay silent", "Pride."),
    ("First Night", "The lights go out. Someone is sobbing. The fat man does not survive.", "Don't sob", "Survive.", "Sob inside", "Honest."),
    ("Red", "A man named Red runs the contraband. He sells you a rock hammer.", "Trust him quietly", "Read.", "Test him first", "Wise."),
    ("The Sisters", "Bogs and his crew corner you. You learn what the showers cost.", "Fight every time", "Refuse.", "Survive the first attack", "Endure."),
    ("The Roof", "A tar-roof detail. You overhear the head guard fretting about an inheritance tax.", "Offer help", "Brave.", "Stay quiet", "Wise."),
    ("Beers on the Roof", "You get the men three beers each. You don't drink. You watch them remember what it is to be men.", "Sip nothing", "Detached.", "Sip one", "Indulge."),
    ("The Library", "You ask the warden for funding for the library. He says no. You write letters anyway. Once a week, for years.", "Keep writing", "Patient.", "Write twice a week", "Pressure."),
    ("Tommy", "A new young inmate named Tommy says he knew the man who really killed your wife.", "Tell the warden", "Naive.", "Tell Red first", "Wise."),
    ("The Warden", "The warden listens. He does not believe you. He does not, you realize, want to believe you.", "Push", "Brave.", "Step back", "Safe."),
    ("Tommy, Gone", "Tommy is killed by the guards in the yard. The official story is escape.", "Mourn him quietly", "Survive.", "Vow", "Plan."),
    ("Solitary", "Two months in solitary. You leave with a plan.", "Make peace with the plan", "Cold.", "Make peace with the cell", "Calm."),
    ("Mozart", "You play Mozart over the prison loudspeakers. For two minutes the yard goes silent.", "Take the punishment", "Worth it.", "Stop early", "Strategic."),
    ("Hope", "Red tells you hope is dangerous. You tell him hope is everything.", "Disagree gently", "Mean it.", "Agree out loud and not inside", "Strategy."),
    ("The Letters Pay", "The library funding arrives, larger than asked. You build a small empire of books.", "Use it", "Honor.", "Hide nothing", "Open."),
    ("Money Laundering", "The warden has, by now, made you his accountant. You launder money for him. You also, slowly, build a man named Stevens.", "Build Stevens carefully", "Patient.", "Build him fast", "Brave."),
    ("The Tunnel", "Each night, after lockdown, you scrape. The hole is, by year nineteen, a tunnel.", "Be patient", "Years.", "Be precise", "Years."),
    ("The Storm", "A thunderstorm. The night. You crawl through five hundred yards of pipe. You come out on the far side of the wall, on your knees, in the rain.", "Stand up", "Free.", "Stay on knees a moment", "Honest."),
    ("The Bank", "You walk into a bank as Stevens and walk out with thirty-seven thousand dollars and a folder of evidence on the warden.", "Mail the evidence", "Right.", "Burn it", "Petty."),
    ("Buxton", "A field in Buxton, Maine. Under a stone wall. A tin box. A note for Red.", "Leave it where you said you would", "Vow.", "Take the tin and run", "Survival."),
    ("Zihuatanejo", "Pacific. Mexico. A boat to fix. You wait.", "Wait honestly", "Patient.", "Plan a small business", "Forward."),
    ("Red's Bus", "Years later, Red arrives on a bus. He walks the beach. He sees you. You raise a hand.", "Walk to him", "Friend.", "Wait for him to come to you", "Honor."),
], [
    ("end_pacific", "Pacific Forever", "You and Red fix the boat. You take tourists out. The Pacific is impossibly blue. You don't think about Shawshank often. When you do, you smile."),
    ("end_letter", "The Letters Continue", "You write letters back to a literacy program at Shawshank. Books, in your name, fill that library for decades. Hope, you decide, is contagious."),
    ("end_quiet", "Quiet Life", "You live small, on purpose. You and Red die old men by the sea. The tomato garden behind the cottage is, you tell tourists, the most important room in the house."),
])

PULP_FICTION = linear_story({
    "id": "fm-pulp-fiction", "title": "Pulp Fiction", "sourceTitle": "Pulp Fiction",
    "kind": "movie", "synopsis": "A briefcase. A boss's wife. A boxer who didn't throw the fight. You're a hitman in a bad suit. The day has, so far, been long.",
    "releaseYear": 1994, "addedAt": "2026-03-24T00:00:00Z", "genre": "Thriller",
    "tags": ["nonlinear", "noir", "LA"], "rating": None, "loved": False,
}, [
    ("The Apartment", "You and Vincent. The briefcase glows. The kid in the chair, sweating.", "Recite the verse", "Style.", "Skip the verse", "Speed."),
    ("The Car", "Vincent shoots Marvin by accident. The car is a disaster. You drive.", "Call Jimmie", "Friend.", "Drive to Marsellus", "Direct."),
    ("Jimmie's Garage", "Coffee, calm, a man named the Wolf. He has thirty minutes.", "Listen to the Wolf", "Wise.", "Argue", "Foolish."),
    ("The Diner", "You and Vincent in a diner. You decide, today, what kind of man you want to be.", "Quit the life", "Brave.", "Stay in", "Familiar."),
    ("Pumpkin and Honey Bunny", "Two amateurs robbing the diner. You hold them at gunpoint, briefly.", "Talk them down", "Style.", "Take them out", "Cold."),
    ("Vincent and Mia", "Vincent has, tonight, dinner with Marsellus' wife.", "Behave perfectly", "Discipline.", "Be yourself", "Risk."),
    ("Jack Rabbit Slim's", "Twist contest. You dance. You almost forget the briefcase.", "Win the twist", "Joy.", "Lose with style", "Cool."),
    ("The Heroin Mistake", "Mia thinks your bag is something else. She overdoses.", "Drive her to Lance", "Save.", "Call 911", "Civic."),
    ("Adrenaline Needle", "You stab the needle into her heart. She comes back screaming.", "Promise not to tell", "Survive.", "Tell Marsellus the truth", "Brave."),
    ("Butch's Watch", "Switching tracks: you are now Butch. Your father's watch is at your apartment.", "Go back for it", "Honor.", "Leave it", "Wise."),
    ("Vincent in the Bathroom", "You shoot Vincent as he comes out of your bathroom. The watch is in your hand.", "Take the watch and go", "Survive.", "Stand frozen", "Human."),
    ("The Car Crash", "Marsellus, on the street. You hit him with your car. You both end up in a pawn shop.", "Fight him", "Brave.", "Run", "Wise."),
    ("The Pawn Shop", "The owner has a gimp. The owner has a problem with you and Marsellus both.", "Free Marsellus", "Right.", "Save yourself", "Practical."),
    ("The Sword", "A katana on the wall. You take it.", "Use it", "Brave.", "Threaten with it", "Style."),
    ("The Bond", "Marsellus owes you. He tells you to leave LA forever.", "Take the deal", "Smart.", "Negotiate", "Greedy."),
    ("Fabienne", "Fabienne packed everything except your father's watch. She is, you realize, going to be okay.", "Forgive her", "Love.", "Be cold", "Stress."),
    ("On the Chopper", "You and Fabienne ride out of LA on Zed's chopper. The sun comes up.", "Look back", "Sentiment.", "Don't look", "Forward."),
    ("Diner, Reframed", "Back at the diner. The robbery is happening now. You and Vincent are in a booth.", "Defuse calmly", "Discipline.", "Take them out", "Cold."),
    ("Honey Bunny's Wallet", "The robber wants your wallet. You pay him to leave. You realize you are, finally, walking the earth.", "Pay him generously", "Path.", "Pay him exactly", "Honor."),
    ("Vincent Stays In", "Vincent decides to stay in. You decide to walk.", "Walk", "Brave.", "Stay one more job", "Familiar."),
    ("The Briefcase", "The briefcase is delivered. Whatever is in it stays in it. You don't, today, open it.", "Don't open it", "Wise.", "Hand it over", "Job."),
], [
    ("end_path", "The Path of the Righteous Man", "You walk the earth, like Caine. You end up running a small diner in New Mexico. The food is, by year three, surprisingly good. People come from town just for the eggs."),
    ("end_briefcase", "The Briefcase, Closed", "You never learn what was in it. Marsellus pays you. You buy a small apartment building. You become a landlord. You are, against every expectation, good at it."),
    ("end_LA", "LA, Forever", "You stay in. The work continues. Vincent dies. Marsellus retires. You are, eventually, the oldest man in the rooms you walk into. You die in one of them, with a smile."),
])

DARK_KNIGHT = linear_story({
    "id": "fm-dark-knight", "title": "The Dark Knight", "sourceTitle": "The Dark Knight",
    "kind": "movie", "synopsis": "Gotham is, by night, mostly yours. A man in face paint has burned a mountain of money. He doesn't want money. You don't know yet what he wants.",
    "releaseYear": 2008, "addedAt": "2026-03-23T00:00:00Z", "genre": "Action",
    "tags": ["batman", "crime", "morality"], "rating": None, "loved": False,
}, [
    ("Rooftop", "You stand on a rooftop. Gordon, below, signals. The bat-light is, in fact, a habit.", "Answer", "Duty.", "Wait one more night", "Patience."),
    ("The Bank Job", "A robbery: six clowns, killing each other. The vault is full. The boss is a man named the Joker.", "Track the trail", "Investigate.", "Confront Joker directly", "Brave."),
    ("Harvey Dent", "Gotham's white knight. He wants to clean up the city. He is, you realize, who you wish you were.", "Support him publicly", "Strategic.", "Stay distant", "Caution."),
    ("Rachel", "Rachel is dating Harvey. You are, in the suit, no good for her. You decide what to do with that knowledge.", "Step back fully", "Honor.", "Be her friend", "Hopeful."),
    ("Mob Bosses", "The mob bosses meet by video. The Joker, uninvited, joins. He offers them his services. He scares them.", "Identify the mob's allies", "Investigate.", "Identify the Joker first", "Priority."),
    ("Lau", "An accountant named Lau has fled to Hong Kong with mob money. You bring him back.", "Quietly", "Stealth.", "Loudly", "Statement."),
    ("Dent's Press Conference", "Dent announces he is Batman to draw Joker out. He isn't. You realize Dent is, in his way, you in a suit.", "Let it happen", "Trust.", "Stop him", "Protect."),
    ("Joker Captures", "A trap. Dent in transit. The Joker attacks the convoy.", "Save Dent", "Mission.", "Capture Joker", "Goal."),
    ("Interrogation", "Joker in a chair. You hit him. He laughs. You realize hitting him is, in fact, the thing he wants.", "Stop hitting", "Discipline.", "Keep going", "Anger."),
    ("Two Locations", "Rachel and Dent are each held in a building rigged to explode. You can save one.", "Choose Rachel", "Heart.", "Choose Dent", "Mission."),
    ("The Wrong Door", "The Joker lied about the addresses. You arrive at the one with Dent. Rachel dies.", "Tell Dent it was an accident", "Lie.", "Tell him the truth", "Honor."),
    ("Two-Face", "Dent burns. Dent breaks. Dent becomes Two-Face. The white knight is gone.", "Save what you can of him", "Save.", "Mourn him", "Honest."),
    ("Coleman Reese", "An accountant threatens to reveal your identity. Joker says, if Reese isn't killed in an hour, a hospital explodes.", "Protect Reese", "Honor.", "Let him reveal you", "Honest."),
    ("Hospital", "Joker, in a nurse's uniform, walks the wards. He finds Dent. He turns him.", "Get there first", "Speed.", "Catch Joker at the door", "Trap."),
    ("Two Ferries", "Two ferries, one of civilians, one of prisoners. Each has the other's detonator.", "Wait for them to decide", "Trust.", "Disable the bombs yourself", "Action."),
    ("They Choose", "Neither boat presses the button. Joker is, briefly, surprised. He decides to do it himself.", "Stop him fast", "Race.", "Stop him slow", "Style."),
    ("Sonar", "You use Lucius' city-wide phone sonar to find Joker. The technology is, in its way, monstrous.", "Use it once", "Compromise.", "Refuse", "Principle."),
    ("Final Fight", "Top of a building. SWAT and Joker. You save the SWAT, you take the Joker.", "Don't kill him", "Vow.", "Disable him brutally", "Anger."),
    ("Dent's Body Count", "Two-Face has, in his last hours, killed five men. He has hostage Gordon's family on a rooftop.", "Take the fall for Dent's crimes", "Hero.", "Tell the truth", "Honest."),
    ("The Rooftop", "Dent dies. Gordon's son lives. You tell Gordon to call you a villain. He does.", "Run", "Sacrifice.", "Stand", "Pride."),
    ("Sunrise", "The bat-signal is, by morning, broken. You ride into the dawn. You are, in this story, the villain Gotham needs.", "Stay the villain", "Vow.", "Plan to come back", "Hope."),
], [
    ("end_villain", "The Dark Knight", "You ride alone for years. The myth grows. Eventually, when the city needs you again, you return. The signal, restored, finds you on the same rooftop."),
    ("end_clean", "The Truth, Eventually", "Years later, when Gotham is stronger, you reveal what Dent did. Gotham survives the revelation. You retire. Wayne Manor, restored, becomes a children's home."),
    ("end_silence", "Silent Bat", "You disappear. The signal is dismantled. You let the city heal without you. Lucius, alone in the bunker, archives the suit. You build, instead, a foundation."),
])

FORREST_GUMP = linear_story({
    "id": "fm-forrest-gump", "title": "Forrest Gump", "sourceTitle": "Forrest Gump",
    "kind": "movie", "synopsis": "Alabama. A bench. A box of chocolates. You don't know what you're going to get. The century, for some reason, keeps happening to you.",
    "releaseYear": 1994, "addedAt": "2026-03-22T00:00:00Z", "genre": "Drama",
    "tags": ["history", "innocence", "running"], "rating": None, "loved": False,
}, [
    ("The Brace", "Doctor says you'll wear it forever. Mama disagrees.", "Trust Mama", "Heart.", "Trust the doctor", "Reason."),
    ("The Bus", "First day of school. Nobody will let you sit. A girl named Jenny does.", "Sit by Jenny", "Friend.", "Sit alone", "Brave."),
    ("Run, Forrest", "Bullies. Stones. Jenny yells run. The brace shatters off your legs.", "Keep running", "Joy.", "Stop and confront", "Brave."),
    ("College Football", "Alabama recruits you. Bear Bryant nods. You return kicks for touchdowns.", "Just keep running", "Forward.", "Try a fake", "Style."),
    ("Vietnam", "Army drafts you. You meet Bubba. Bubba talks about shrimp.", "Listen", "Friend.", "Plan together", "Plan."),
    ("Ambush", "Rain. Fire. Bubba is down. You carry him.", "Go back for the others", "Brave.", "Stay with Bubba", "Loyal."),
    ("Hospital", "You meet Lieutenant Dan. He is, angry, alive, missing legs.", "Play ping-pong", "Therapy.", "Sit with Dan", "Friend."),
    ("White House", "You meet a President. You show another your bullet wound.", "Be polite", "Style.", "Be honest", "Forrest."),
    ("Lincoln Memorial", "You speak at a Vietnam protest. The mic cuts out. The crowd listens anyway.", "Just stand there", "Honest.", "Walk down", "Modest."),
    ("Jenny, Found", "Jenny is on a stage in San Francisco. The crowd is, you don't know what kind, the crowd.", "Run to her", "Heart.", "Wait", "Patient."),
    ("Ping-Pong Diplomacy", "You play ping-pong in China. You meet a different President. He, also, gets a wound shown to him.", "Win the cup", "Skill.", "Lose graciously", "Style."),
    ("Apple Computer", "Lieutenant Dan invests your shrimp boat money in some fruit company. The fruit company is, it turns out, fine.", "Don't think about it much", "Forrest.", "Be excited", "Honest."),
    ("Bubba Gump", "You and Dan start a shrimp company in Bubba's name. The hurricane spares your boat. You make a lot of money.", "Give half to Bubba's mama", "Honor.", "Save it all for Mama", "Family."),
    ("Mama", "Mama is dying. You sit with her. She tells you life is a box of chocolates.", "Sit till the end", "Son.", "Promise her you'll be okay", "Vow."),
    ("Running", "You start running. You don't stop for years. People follow you. You start a movement by accident.", "Just keep running", "Path.", "Make a speech", "Style."),
    ("Jenny's Apartment", "Jenny finds you. There is a child. The child is, in fact, yours.", "Be a father", "Forward.", "Be scared", "Honest."),
    ("Marriage", "You marry Jenny. She is sick. You know she is sick. You marry her anyway.", "Love every day", "Now.", "Don't think about tomorrow", "Present."),
    ("Jenny, Sick", "Jenny dies under the tree by the church. You sit with her grave a long time.", "Talk to her", "Honest.", "Stand quietly", "Honor."),
    ("Little Forrest", "Your son is small and smart. He asks if you're his dad. You tell him yes.", "Read to him every night", "Father.", "Drive him to school every morning", "Father."),
    ("The Bench, Now", "On the bench, telling a stranger your story. The stranger leaves. The bus arrives.", "Stand up", "Forward.", "Sit a moment more", "Honor."),
    ("Little Forrest's First Day", "You walk him to the bus. You stand by the road. The feather drifts past your shoe.", "Pick up the feather", "Sentiment.", "Let it go", "Forward."),
], [
    ("end_feather", "The Feather", "You go home, put Jenny's feather in your old book, and start running again the next morning. Just because. Some things don't need a reason."),
    ("end_father", "Little Forrest's Years", "You raise Little Forrest into a kind, smart man. He becomes a teacher. You watch him from a back row at his graduation and cry exactly once, in a Forrest way, big and honest."),
    ("end_chocolates", "Box of Chocolates", "Mama was right. You never know what you're going to get. You eat the chocolates as they come. The bench, in town, is still there. Some days you sit on it."),
])

STAR_WARS = linear_story({
    "id": "fm-star-wars", "title": "Star Wars: A New Hope", "sourceTitle": "Star Wars: A New Hope",
    "kind": "movie", "synopsis": "Tatooine. Two suns. Aunt Beru's blue milk. A droid you bought yesterday is, apparently, carrying the plans to a planet-killing weapon. Buckle up.",
    "releaseYear": 1977, "addedAt": "2026-03-21T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["space", "hero", "rebellion"], "rating": None, "loved": False,
}, [
    ("Two Suns", "You stand watching them set. You want to be anywhere else.", "Stay loyal to the farm", "Family.", "Plan to leave", "Hope."),
    ("The Droids", "R2 has a message for an Obi-Wan Kenobi. Uncle Owen says forget it.", "Chase R2 at dawn", "Brave.", "Tell Uncle", "Honor."),
    ("Sandcrawler Wreck", "Stormtroopers killed the Jawas. The droids, you realize, are wanted.", "Run home", "Family.", "Hide the droids", "Strategic."),
    ("Aunt and Uncle", "They are dead, the homestead burning. You stand in the smoke.", "Vow", "Anger.", "Mourn", "Grief."),
    ("Ben", "Obi-Wan tells you the truth about your father. He hands you a lightsaber.", "Take it", "Path.", "Pause", "Wise."),
    ("Cantina", "Mos Eisley. Aliens. A pilot with a Wookiee.", "Hire Han", "Speed.", "Look for another captain", "Cautious."),
    ("The Falcon", "Hyperspace. The galaxy stretches. You realize the universe is huge.", "Practice with the saber", "Discipline.", "Look out the window", "Wonder."),
    ("Tractor Beam", "Captured by the Death Star. You hide in smuggling holds.", "Disguise as stormtroopers", "Brave.", "Wait it out", "Cautious."),
    ("The Princess", "Leia is in a cell. You rescue her in a trash compactor.", "Save her quickly", "Hero.", "Save her carefully", "Plan."),
    ("Garbage", "Eyes in the water. Walls closing in. The droids save you.", "Trust the droids", "Friend.", "Push the walls", "Brave."),
    ("Obi-Wan, Falling", "You watch Ben let Vader strike him down. You feel him afterward, in your head.", "Listen", "Wise.", "Look away", "Anger."),
    ("Yavin", "The Rebel base. Briefing. The Death Star approaches.", "Volunteer for X-wing", "Hero.", "Stay back", "Cautious."),
    ("Cockpit", "You climb in. Biggs nods. R2 chirps.", "Trust R2", "Friend.", "Trust your training", "Solo."),
    ("Trench Run", "Lasers. Towers. Wedge falls back. Biggs goes down.", "Stay on target", "Discipline.", "Veer to avoid", "Survival."),
    ("Vader Behind", "Vader is on your tail. Han, you'd swear, is not coming.", "Trust the Force", "Faith.", "Trust the computer", "Reason."),
    ("Han, Arriving", "The Falcon comes screaming in. Vader spins off.", "Take the shot", "Now.", "Wait one beat", "Patient."),
    ("The Shot", "Two-meter exhaust port. You feel Ben's voice. You let go.", "Fire", "Hope.", "Adjust", "Honor."),
    ("The Death Star Goes", "The whole moon-sized weapon comes apart. You fly out of the cloud.", "Whoop", "Joy.", "Stay quiet, focused", "Pilot."),
    ("Medals", "Leia gives you and Han medals. Chewie is, briefly, snubbed.", "Notice the Chewie thing publicly", "Honor.", "Be polite", "Style."),
    ("After", "The Rebellion has many fights ahead. The galaxy is still mostly the Empire.", "Stay with the Rebellion", "Path.", "Take a season off", "Honest."),
    ("Your Father's Saber", "You hold it in your hand. The weight is real. The path, you realize, is yours.", "Train", "Jedi.", "Train slowly", "Patient."),
], [
    ("end_jedi", "Becoming a Jedi", "You find Yoda. You train. You meet your father. You become, in time, the Jedi the galaxy needed. The Force, you decide, is family."),
    ("end_pilot", "The Best Pilot", "You stay with Rogue Squadron. You fly forever. Han calls you kid for the rest of your life. You never quite mind it."),
    ("end_balance", "Bringing Balance", "Years later you start a new Jedi Order. The first new students are not all young. The Force, you teach them, is older than any of them."),
])

LOTR = linear_story({
    "id": "fm-lotr-fotr", "title": "The Lord of the Rings: The Fellowship of the Ring", "sourceTitle": "The Lord of the Rings: The Fellowship of the Ring",
    "kind": "movie", "synopsis": "A ring you didn't ask for. A road that goes ever on. Nine companions. One dark lord. You're a hobbit, mostly. You have one job.",
    "releaseYear": 2001, "addedAt": "2026-03-20T00:00:00Z", "genre": "Fantasy",
    "tags": ["epic", "ring", "fellowship"], "rating": None, "loved": False,
}, [
    ("The Party Field", "Bilbo's 111th birthday. Fireworks. You are quietly happy.", "Enjoy the party", "Joy.", "Help Bilbo pack", "Care."),
    ("Gandalf's Return", "Gandalf comes by night. The ring tests fire. The runes appear.", "Listen carefully", "Wise.", "Be afraid", "Honest."),
    ("Leaving the Shire", "Sam at your side. Pippin and Merry crash through corn.", "Take the Old Forest path", "Brave.", "Take the road", "Direct."),
    ("Bree", "The Prancing Pony. A stranger named Strider. Wet stones.", "Trust him", "Wise.", "Hold off", "Cautious."),
    ("Weathertop", "The Nazgûl find you. You are stabbed by a Morgul blade.", "Hide the ring", "Discipline.", "Try to fight", "Brave."),
    ("Rivendell", "Elrond's house. Council. Voices argue. The ring sits on a plinth.", "Volunteer", "Path.", "Stay silent", "Honest."),
    ("The Fellowship", "Nine. Aragorn, Boromir, Gimli, Legolas, Gandalf, the four hobbits.", "Trust each one", "Open.", "Watch Boromir", "Cautious."),
    ("Caradhras", "The mountain pass. Snow. Saruman's voice in the wind.", "Push through", "Brave.", "Go under via Moria", "Reluctant."),
    ("Moria", "The Doors of Durin. Speak friend and enter.", "Trust Gandalf", "Faith.", "Argue the riddle", "Mind."),
    ("The Hall", "Dwarves long dead. A drum in the deep.", "Stand by the door", "Strategic.", "Read the records", "Honor."),
    ("Bridge of Khazad-dûm", "The Balrog. Gandalf, you fly fools.", "Run", "Survive.", "Try to help", "Brave."),
    ("Lothlorien", "Galadriel. The mirror. The temptation.", "Refuse the ring", "Vow.", "Almost take it", "Honest."),
    ("River", "Boats on the Anduin. Tall stone kings.", "Watch the riverbanks", "Wise.", "Talk with Aragorn", "Friend."),
    ("Amon Hen", "Boromir asks for the ring. You refuse. He grabs.", "Run", "Save the ring.", "Try to talk him down", "Mercy."),
    ("The Choice", "You sit by the river. Sam finds you. You decide the only way forward is alone.", "Take Sam", "Friend.", "Go alone", "Vow."),
    ("Sam in the Water", "Sam swims after you. You pull him in. You realize you are not alone after all.", "Cry", "Honest.", "Smile", "Brave."),
    ("Boromir, Falling", "Boromir, redeemed, dies defending Merry and Pippin. Aragorn cradles him.", "Honor him from afar", "Quiet.", "Go back briefly", "Heart."),
    ("Aragorn's Vow", "Aragorn vows to hunt the Uruks. You and Sam vow to take the road east.", "Trust the company splits well", "Faith.", "Wish for the company whole", "Honest."),
    ("Emyn Muil", "Stones, mist, no path. Gollum follows.", "Set a trap", "Cunning.", "Confront Gollum", "Direct."),
    ("Gollum", "He bargains. He swears on the precious.", "Trust slowly", "Path.", "Don't trust", "Wise."),
    ("Mordor's Border", "The Black Gate. Closed. The land smokes. The road, somehow, continues.", "Find the secret way", "Path.", "Wait", "Patience."),
], [
    ("end_ring", "The Ring Cast Down", "The road goes on for two more books. You and Sam, at the end, throw it into the fire. The Shire heals. You sail west, eventually, with Bilbo."),
    ("end_sam", "Sam, Always", "Sam is, in the end, the hero of the story. He marries Rosie. He has many children. You write a book about it. The book becomes, in time, scripture."),
    ("end_shire", "Back in the Shire", "You return changed. Most don't notice. Sam notices. The Gaffer notices. You sit by the river and write, in a small careful hand, the whole tale."),
])

TITANIC = linear_story({
    "id": "fm-titanic", "title": "Titanic", "sourceTitle": "Titanic",
    "kind": "movie", "synopsis": "Southampton, April 1912. You're first class, engaged to a man who keeps a safe of secrets. The man you'll actually fall for is three decks below playing cards for a ticket.",
    "releaseYear": 1997, "addedAt": "2026-03-19T00:00:00Z", "genre": "Drama",
    "tags": ["ship", "romance", "disaster"], "rating": None, "loved": False,
}, [
    ("Boarding", "The biggest ship ever built. White Star flags. You don't look at it the way the steerage does.", "Try to feel the wonder", "Honest.", "Stay composed", "Class."),
    ("Cal", "Your fiancé's smile is, on closer reading, ownership.", "Tolerate", "Survive.", "Push back", "Spirit."),
    ("Dinner", "The first-class dining room is a circus of forks.", "Be charming", "Strategy.", "Be honest", "Truth."),
    ("The Stern", "You walk to the back at night, considering the water.", "Climb the rail", "Honest.", "Step back", "Caution."),
    ("Jack", "A man named Jack talks you back from the rail. He sketches.", "Talk to him", "Curious.", "Walk away", "Class."),
    ("Steerage Party", "Beer, music, dancing without shoes.", "Dance", "Joy.", "Sit and watch", "Quiet."),
    ("Cal's Anger", "Cal flips the table. He hits you, almost. You realize you cannot marry him.", "Decide now", "Brave.", "Decide later", "Strategic."),
    ("The Sketch", "Jack draws you wearing only the Heart of the Ocean. Cal will find the sketch.", "Hide it", "Wise.", "Leave it for him", "Defiant."),
    ("Cargo Hold", "Cars in the hold. A handprint on a window.", "Just be here", "Present.", "Run for the deck", "Plan."),
    ("Iceberg Spotted", "11:40 p.m. Bell. Frantic turn. The scrape is small. The water is fast.", "Believe it", "Real.", "Disbelieve it", "Hope."),
    ("Mr. Andrews", "The architect knows the ship will sink. He tells you to put on your lifebelt.", "Trust him", "Wise.", "Hesitate", "Honest."),
    ("Lifeboat", "Women and children first. Cal forces you in. Jack is on the deck.", "Step in", "Live.", "Step out", "Choice."),
    ("The Jump", "You leap from the lifeboat back onto the ship. Jack runs to you.", "Hold his hand", "Vow.", "Look at the ship", "Honest."),
    ("Cal Chases", "Cal, with a pistol. The corridors are flooding.", "Run", "Survive.", "Trick him", "Cunning."),
    ("Stairwell", "Water roars up the staircase. A clock chimes 2:00.", "Climb high", "Survive.", "Help others as you go", "Honor."),
    ("Locked Gates", "Steerage is locked below. You and Jack break a bench from the floor.", "Break the gate", "Brave.", "Find another route", "Strategic."),
    ("Stern Rising", "The stern rises out of the water. You hold the rail.", "Climb the rail", "Plan.", "Wait it out", "Faith."),
    ("The Plunge", "The ship splits. The stern drops. Cold takes everything.", "Hold Jack's hand", "Vow.", "Swim to a door", "Survive."),
    ("The Door", "A wooden door in the water. Jack pushes you onto it. He stays in.", "Hold his hand till he goes", "Honest.", "Promise to live", "Vow."),
    ("Whistle", "Carpathia is hours away. You take the whistle from a frozen officer.", "Blow it long", "Survive.", "Blow it short", "Conserve."),
    ("Carpathia", "You give your name as Rose Dawson. The reporters never find you.", "Hide", "Vow.", "Step into the light", "Honest."),
], [
    ("end_dawson", "Rose Dawson", "You live as Rose Dawson for the rest of your life. You travel. You ride horses. You learn to fly. At eighty-something, you sail to the wreck site and drop the diamond in."),
    ("end_calvin", "Cal, Eventually", "Cal loses everything in 1929 and shoots himself. You read about it in the paper at breakfast. You finish the toast. You go on with your day."),
    ("end_jack", "Jack, Always", "You keep a small sketch in a tin. You speak to him sometimes, by water. You marry, eventually, a kind man. He does not, you tell him, replace Jack. He understands."),
])


SPECS = [
    PALM_ROYALE, HIM_AND_HERS, THE_LOST_BUS,
    MARGARET, SHRINKING, WUTHERING, BLACK_SWAN, HOPPERS,
    GOT, SVBGH, SUPERSTORE, PURSUIT, THE_GREAT,
    WAYWARD, BODKIN, SCARY_MOVIE_4, ETERNITY, MERCY,
    INVINCIBLE, THE_BOYS, OUTCOME, THE_INTERN, DUNE_ONE,
    HOUSEMAID, LOOT, WICKED, WOLVES, DHURANDHAR, BEAST_GAMES,
    HOUSE_DYNAMITE, DONT_LOOK_UP, SPEAK_NO_EVIL, CABIN_10,
    DEVS, DAHMER, MONARCH, DHURANDHAR_2, YOUNG_SHELDON,
    HEARTBREAK_HIGH, IMPERFECT_WOMEN, SEBASTIAN, BUGONIA,
    EUPHORIA, PRADA_2, SMILE_2, OFF_CAMPUS, ROOMMATES,
    BOROUGHS, LADIES_FIRST, TOASTER,
    STRANGER_THINGS, HIJACK, SCOUTS_ZOMBIE, ZERO_DAY, ZODIAC,
    SCARY_MOVIE_2, EUROTRIP, MORE_MERRIER, SCREAM_7, THE_BLUFF,
    SCARY_MOVIE_3, SCARY_MOVIE_5, TELL_ME_LIES, WRINKLE_TIME,
    GODFATHER, SHAWSHANK, PULP_FICTION, DARK_KNIGHT,
    FORREST_GUMP, STAR_WARS, LOTR, TITANIC,
]

SCHINDLER = linear_story({
    "id": "fm-schindlers-list", "title": "Schindler's List", "sourceTitle": "Schindler's List",
    "kind": "movie", "synopsis": "Kraków, 1939. You're a German businessman with a gift for getting on the right side of every officer at every party. The Jews of this city are about to need a list with your name on it.",
    "releaseYear": 1993, "addedAt": "2026-03-18T00:00:00Z", "genre": "Drama",
    "tags": ["holocaust", "rescue", "historical"], "rating": None, "loved": False,
}, [
    ("The Club", "Officers, cognac, jazz. You buy every round.", "Make a connection", "Strategy.", "Buy more rounds", "Patient."),
    ("The Factory", "An enamelware factory, abandoned. A man named Stern keeps the books.", "Hire Stern", "Trust.", "Hire a German", "Safe."),
    ("Jewish Workers", "Cheap labor, the regime says. People, you see, when you look at them.", "Hire many", "Right.", "Hire few", "Cover."),
    ("Goeth", "Camp commandant. Cruel. Charming when useful.", "Befriend him", "Strategy.", "Avoid him", "Honest."),
    ("Helen Hirsch", "Goeth's maid. He beats her. You bring her medicine quietly.", "Help quietly", "Care.", "Confront Goeth", "Foolish."),
    ("The Ghetto", "Liquidation day. The streets fill with bodies and shoes. A girl in a red coat.", "Watch from the hill", "Witness.", "Look away", "Honest."),
    ("Stern's Lists", "Stern brings names. Each name is a person. Each person is a deduction from your factory's price.", "Approve every name", "Right.", "Cap the list", "Practical."),
    ("Payoffs", "You buy people one bribe at a time. The price changes weekly.", "Pay it", "Vow.", "Negotiate", "Smart."),
    ("Goeth's Pardons", "You convince Goeth to grant pardons for sport. He likes the idea of being god.", "Encourage it", "Cynical use.", "Disgust him", "Foolish."),
    ("The Wedding", "A Jewish wedding in the camp. You attend secretly.", "Drink", "Honor.", "Stand far back", "Honest."),
    ("Auschwitz Train", "A train of your women workers is misrouted to Auschwitz.", "Buy them back", "Now.", "Send a telegram first", "Cautious."),
    ("Auschwitz Office", "You enter the office with a diamond brooch and a smile.", "Smile larger", "Strategy.", "Show the diamond first", "Direct."),
    ("Women Returned", "The women come back. The relief is private.", "Hide the relief", "Discipline.", "Show some warmth", "Honest."),
    ("The List", "Stern, at the typewriter. Names. More names. Eleven hundred names.", "Add every Stern suggests", "Right.", "Add a few you've thought of", "Memory."),
    ("Final Bribes", "Your fortune is, by now, mostly gone. Each name has cost a price.", "Spend the rest", "Vow.", "Save a little", "Survive."),
    ("The Workers Arrive", "The eleven hundred arrive at Brünnlitz. They are, for now, alive.", "Be at the gate", "Honor.", "Stay in the office", "Discipline."),
    ("The Last Months", "You make worthless ammunition on purpose. The war ends in slow degrees.", "Keep faking", "Sabotage.", "Risk less", "Safe."),
    ("Liberation", "A Russian officer rides in. The workers are no longer prisoners.", "Speak to them", "Honor.", "Stand to the side", "Quiet."),
    ("The Ring", "The workers melt down their gold to make you a ring. He who saves one life.", "Take the ring", "Honor.", "Refuse", "Pride."),
    ("Could Have Saved More", "You break, in front of Stern, over the car you could have sold, the pin you could have sold.", "Let it out", "Honest.", "Bury it", "Survival."),
    ("Years Later", "You die a poor man, honored. The workers and their children visit your grave for decades.", "Be remembered", "Honor.", "Be forgotten quietly", "Modest."),
], [
    ("end_ring", "He Who Saves One Life", "The ring is, in the end, the only inheritance you wanted to leave. The descendants of the eleven hundred number, by the time you are remembered, more than the population of Kraków."),
    ("end_stern", "Stern's Friendship", "Stern survives you. He writes the list down again, properly, with photographs. The list, in libraries, becomes a kind of scripture."),
    ("end_helen", "Helen, Free", "Helen survives. She emigrates. Years later she sits at a kitchen table with your widow, drinking coffee, talking about a man neither of them could have predicted."),
])

WIZARD_OZ = linear_story({
    "id": "fm-wizard-of-oz", "title": "The Wizard of Oz", "sourceTitle": "The Wizard of Oz",
    "kind": "movie", "synopsis": "Kansas, then not Kansas. A cyclone. A pair of shoes. A road of yellow brick. The lion needs courage. The wizard, you'll find, needs you.",
    "releaseYear": 1939, "addedAt": "2026-03-17T00:00:00Z", "genre": "Fantasy",
    "tags": ["classic", "journey", "musical"], "rating": None, "loved": False,
}, [
    ("The Farm", "Auntie Em. Uncle Henry. Miss Gulch with a bicycle. Toto in your arms.", "Stay with Auntie", "Family.", "Run away", "Spirit."),
    ("Run Away", "You meet Professor Marvel. He reads your future kindly.", "Listen", "Wise.", "Argue", "Spirit."),
    ("Cyclone", "Storm cellar locked. You run for the house. The window comes loose.", "Hold on", "Brave.", "Lie low", "Smart."),
    ("Munchkinland", "Color. Tiny people. A witch crushed by your house.", "Sing along", "Joy.", "Look for an exit", "Smart."),
    ("Glinda", "She arrives in a bubble. She gives you the shoes. She says follow the road.", "Trust her", "Faith.", "Ask many questions", "Wise."),
    ("Scarecrow", "He has no brain. He says so cheerfully.", "Invite him along", "Friend.", "Help him down only", "Modest."),
    ("Apples", "The trees throw apples. The scarecrow improvises.", "Steal the apples", "Brave.", "Apologize and leave", "Polite."),
    ("Tin Man", "Rust. Oilcan. A heart, missing.", "Oil him", "Care.", "Oil him slowly", "Patient."),
    ("Forest", "Lions, tigers, bears.", "Hum a song", "Brave.", "Quiet steps", "Smart."),
    ("Lion", "A lion who roars and weeps in the same breath.", "Invite him", "Friend.", "Be brave for him", "Care."),
    ("Poppies", "Sleep. Glinda sends snow.", "Wake", "Now.", "Sleep through", "Honest."),
    ("Emerald City", "Green walls, green tea. A door without a handle.", "Knock politely", "Civil.", "Yell", "Spirit."),
    ("Audience with the Wizard", "Fire, smoke, a big head. He gives you a task.", "Accept", "Brave.", "Negotiate", "Smart."),
    ("Witch's Castle", "You are captured. The witch wants the shoes.", "Refuse her", "Brave.", "Bargain for time", "Smart."),
    ("Rescue", "Your friends arrive in stolen uniforms.", "Run for the door", "Speed.", "Fight your way out", "Brave."),
    ("Water", "The witch corners you. You throw a bucket. She melts.", "Apologize", "Honor.", "Take her broom", "Smart."),
    ("Behind the Curtain", "Toto pulls back the curtain. The wizard is a man.", "Be angry", "Honest.", "Be gentle", "Wise."),
    ("Gifts", "Diploma, medal, heart-shaped clock.", "Accept them gratefully", "Honor.", "Refuse the gimmicks", "Honest."),
    ("Balloon", "The balloon ride home. Toto runs after a cat. The balloon leaves without you.", "Sit down crying", "Honest.", "Plan again", "Spirit."),
    ("Glinda Again", "She tells you you've had the power all along.", "Click the heels", "Faith.", "Question it", "Wise."),
    ("Kansas", "You wake in your bed. Aunt Em. Toto. The farm.", "Tell them everything", "Honest.", "Just be grateful", "Honor."),
], [
    ("end_home", "There's No Place Like Home", "You stay in Kansas. You marry, eventually. Your children grow up listening to a story their teachers don't quite believe. The shoes, you keep in a drawer."),
    ("end_oz", "Back to Oz", "Years later you find a way back. You become, eventually, the steward of Emerald City. The scarecrow and tin man are, by then, regents. The lion is, mostly, a sleepy mayor."),
    ("end_storyteller", "The Storyteller", "You write the book down. The book becomes a movie. The movie becomes part of every Sunday afternoon for decades. You die quietly. Toto is, by then, a small grand-pup."),
])

JURASSIC = linear_story({
    "id": "fm-jurassic-park", "title": "Jurassic Park", "sourceTitle": "Jurassic Park",
    "kind": "movie", "synopsis": "Isla Nublar. A theme park, soft-opening. The fences are electric and the dinosaurs are alive. The power, in two hours, will go off.",
    "releaseYear": 1993, "addedAt": "2026-03-16T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["dinosaurs", "park", "chaos"], "rating": None, "loved": False,
}, [
    ("Helicopter", "You and Ellie arrive. Hammond grins. A brachiosaurus stands beyond the trees.", "Marvel", "Joy.", "Ask how", "Scientist."),
    ("The Lab", "Vials, amber, frogs filling gaps in DNA.", "Object on principle", "Honest.", "Reserve judgement", "Civil."),
    ("Tour Cars", "Self-driving Jeeps. Lex and Tim in the back.", "Make conversation", "Care.", "Watch the road", "Cautious."),
    ("Rain", "The sky opens. A goat is offered. The T. rex does not appear.", "Wait", "Honest.", "Volunteer to look", "Brave."),
    ("Power Off", "The fences go dark. The T. rex notices. The car splits in half.", "Run", "Survive.", "Stand still", "Smart."),
    ("Tree", "Up a tree, with Tim, with the broken car above you.", "Climb down", "Brave.", "Stay up", "Wise."),
    ("Ellie and Muldoon", "Search and rescue. Muldoon has a gun. Ellie has a flashlight.", "Help them search", "Right.", "Find the kids", "Heart."),
    ("Sick Triceratops", "Ellie crouches by it, hand on the hide.", "Help her diagnose", "Science.", "Watch the trees", "Cautious."),
    ("Visitor Center", "Ice cream melts on the table. Hammond, smaller.", "Comfort him briefly", "Care.", "Find the kids", "Mission."),
    ("Kitchen", "Velociraptors. Lex hides in cabinets. Tim freezes.", "Distract them", "Brave.", "Trap them in the freezer", "Smart."),
    ("Hammond's Confession", "He says he should have been there for them. He sounds, briefly, like a grandfather and not a CEO.", "Forgive him later", "Honor.", "Hold the line now", "Mission."),
    ("Power Restoration", "Lex types on the Unix system. The lights come on.", "Praise her", "Care.", "Stay alert", "Wise."),
    ("Raptors Outside", "They are at the door. The door is glass.", "Move the kids up", "Save.", "Distract the raptors", "Brave."),
    ("Climb the Bones", "The big skeleton in the rotunda. You climb. The raptors follow.", "Climb fast", "Speed.", "Climb carefully", "Honest."),
    ("T. Rex Returns", "The T. rex bursts in, takes one raptor, then another. The banner falls.", "Run for the helicopter", "Speed.", "Stay till the dust settles", "Witness."),
    ("Helicopter Pad", "Hammond, mute. Ellie. The kids in your arms.", "Hold them", "Care.", "Look at the island a last time", "Honor."),
    ("Hammond", "He, finally, agrees not to endorse the park. He looks small. He looks human.", "Be kind", "Honor.", "Be honest", "Truth."),
    ("Flight Out", "The birds, you realize, are dinosaurs. The window is full of pelicans.", "Notice it", "Joy.", "Sleep", "Honest."),
    ("Mainland", "Press, cameras, no statement.", "No statement", "Discipline.", "A short statement", "Public."),
    ("The Lab Visit", "Years later you visit a different lab. The science is, again, ahead of the ethics. You decide what to do.", "Speak publicly", "Voice.", "Step away", "Honest."),
    ("Coffee with Ellie", "Years on, coffee with Ellie. You both still wake at 4 a.m. sometimes.", "Plan an article", "Action.", "Just enjoy the coffee", "Heal."),
], [
    ("end_paper", "The Paper", "You and Ellie publish a long paper on de-extinction ethics. It becomes the standard syllabus. You don't, you decide, need to be the regulator. You just need to be the alarm."),
    ("end_field", "Back to the Field", "You return to paleontology. You discover, in a Montana dig, a fossil that, briefly, shakes the field. You realize the living dinosaurs were, for you, a detour."),
    ("end_kids", "The Kids Grew Up", "Lex becomes a programmer. Tim becomes a paleontologist. They both, separately, send you Christmas cards. The cards are, always, slightly nicer than yours."),
])

MATRIX = linear_story({
    "id": "fm-the-matrix", "title": "The Matrix", "sourceTitle": "The Matrix",
    "kind": "movie", "synopsis": "Wake up, Neo. The white rabbit, the office, the call. Red pill, blue pill. Choose what kind of life you were going to have anyway.",
    "releaseYear": 1999, "addedAt": "2026-03-15T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["cyberpunk", "philosophy", "chosen-one"], "rating": None, "loved": False,
}, [
    ("The Apartment", "A green prompt. Wake up, Neo. A knock at the door.", "Open", "Brave.", "Pretend not to be home", "Wise."),
    ("Choi", "Two grand for the disk. Follow the white rabbit, he says.", "Go with them", "Path.", "Stay home", "Safe."),
    ("Trinity", "A woman in leather at a club. She tells you the question is what drives you.", "Listen", "Path.", "Stay alert", "Wise."),
    ("The Office", "Agents at your desk. Smith. Phone in a parcel.", "Take the phone", "Path.", "Go with the agents", "Honest."),
    ("Window Ledge", "Morpheus says go to the ledge. You can't. They take you.", "Try anyway", "Brave.", "Cooperate", "Smart."),
    ("Bug", "A bug crawls under your skin. Trinity removes it.", "Trust her", "Path.", "Run", "Honest."),
    ("Pills", "Red or blue. Morpheus, sincere.", "Red", "Path.", "Blue", "Honest."),
    ("Out", "You are pulled out of a pod. You are weak. You are real.", "Stay still", "Heal.", "Look around", "Curious."),
    ("Nebuchadnezzar", "Hovercraft, crew, a captain. Real food is gruel.", "Eat it", "Honest.", "Refuse", "Spoiled."),
    ("Training", "Jiu-jitsu uploaded. You wake fluent.", "Spar with Morpheus", "Brave.", "Spar carefully", "Smart."),
    ("The Construct", "Black emptiness. Morpheus shows you the system.", "Listen carefully", "Wise.", "Argue", "Spirit."),
    ("Tank", "A man named Tank brings you tea. He was born free.", "Befriend him", "Friend.", "Stay alone", "Honest."),
    ("Oracle", "Cookies. A small woman. She tells you what you needed to hear, not what you wanted.", "Believe her", "Path.", "Doubt her", "Honest."),
    ("Cypher", "Cypher misses steak. He misses being unconscious. He betrays.", "Spot it earlier", "Wise.", "Catch it late", "Honest."),
    ("Subway", "Agents pursue. Morpheus, captured, is taken to a building.", "Save him", "Heart.", "Wait", "Smart."),
    ("Lobby", "Marble. Guards. Sunglasses. Many rounds expended.", "Run the lobby", "Brave.", "Plan a quieter route", "Smart."),
    ("Rooftop", "A helicopter. Morpheus on a chair.", "Pilot", "Brave.", "Cover", "Smart."),
    ("Subway Two", "Smith on a platform. You face him.", "Stand", "Brave.", "Run", "Wise."),
    ("Hotel", "Smith corners you in a hallway. Bullets stop.", "See them", "Path.", "Dodge them", "Honest."),
    ("The One", "You break Smith apart from the inside.", "Step out of his shape", "Final.", "Hold him a moment", "Honor."),
    ("Phone Booth", "Call ended. You step out of the booth. You can fly.", "Fly", "Path.", "Walk a block first", "Style."),
], [
    ("end_one", "The One", "You become a teacher and a target. You fly often. You also, occasionally, take the bus, because the bus passes a place that used to be your apartment."),
    ("end_zion", "Zion's Builder", "You spend a decade rebuilding Zion's defenses. You marry Trinity. You retire, eventually, to teach kids how to fly. The kids, mostly, prefer running."),
    ("end_peace", "Peace with the Machines", "You broker, eventually, a peace between humans and machines. The truce holds for a generation. After that, you don't know. You are, for now, content with a generation."),
])

AVATAR = linear_story({
    "id": "fm-avatar", "title": "Avatar", "sourceTitle": "Avatar",
    "kind": "movie", "synopsis": "Pandora. Floating mountains, glowing forests, a tree as old as your grandmother. You're a marine in a Na'vi body. You're supposed to be spying. You're starting to fall in love.",
    "releaseYear": 2009, "addedAt": "2026-03-14T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["pandora", "ecology", "war"], "rating": None, "loved": False,
}, [
    ("Cryosleep", "Your brother is dead. You are in his body's contract.", "Take the job", "Brother.", "Negotiate", "Smart."),
    ("Hell's Gate", "Mining base, mechs, AMP suits. Selfridge wants ore.", "Listen to Selfridge", "Job.", "Listen to Grace", "Science."),
    ("First Link", "You wake in a Na'vi body. You run on grass.", "Run", "Joy.", "Stand still", "Smart."),
    ("Lost in the Forest", "Things glow. Things growl. Then a creature attacks.", "Climb", "Smart.", "Fight", "Brave."),
    ("Neytiri", "She saves you. She is, briefly, angry.", "Listen", "Humble.", "Apologize fast", "Civil."),
    ("Hometree", "Branches the size of streets. Eytukan. Mo'at.", "Be respectful", "Honor.", "Ask many questions", "Curious."),
    ("Initiation", "Neytiri teaches. You ride a banshee. You make a bond.", "Trust the bond", "Path.", "Hesitate", "Honest."),
    ("Reporting In", "Quaritch wants intel on the tree. He wants a way in.", "Stall", "Wise.", "Cooperate", "Job."),
    ("Eywa", "You see the tree of voices. The wind speaks ancestors.", "Believe", "Path.", "Doubt", "Honest."),
    ("Becoming", "You take a mate. Neytiri chooses you.", "Choose her back", "Heart.", "Stay torn", "Honest."),
    ("Bulldozers", "Earthmovers tear up sacred ground.", "Stop them", "Vow.", "Report it", "Process."),
    ("Exposure", "Quaritch shows your video log. The Na'vi see you for the spy you were.", "Confess", "Honor.", "Defend", "Honest."),
    ("Hometree Falls", "The tree, ancient, comes down.", "Carry survivors", "Save.", "Fight back now", "Brave."),
    ("Disowned", "Neytiri turns away. Eytukan dies. You stand in the smoke.", "Vow", "Path.", "Mourn", "Honest."),
    ("Toruk", "You climb. You bond with the biggest banshee. You return as legend.", "Use the legend", "Strategy.", "Earn it slowly", "Humble."),
    ("Tribes Unite", "You ride to all the clans. They come.", "Lead", "Path.", "Follow Neytiri", "Honor."),
    ("Battle", "Sky people, missiles, mechs. Animals you didn't know about charge.", "Trust Eywa", "Faith.", "Trust strategy", "Brain."),
    ("Quaritch", "Mech vs. avatar. Neytiri saves you.", "Save her back", "Vow.", "Pursue Quaritch", "Vow."),
    ("Your Body", "Your human body is starving in the chamber. You have minutes.", "Make the transfer", "Path.", "Wait", "Honest."),
    ("Ceremony", "Mo'at and the tribe gather. You pass through the eye of Eywa.", "Open your eyes Na'vi", "New.", "Hold on to the old self", "Honest."),
    ("New Life", "You wake as Na'vi for good. Neytiri's hand finds yours.", "Stay", "Path.", "Build the bridge to humans", "Hope."),
], [
    ("end_navi", "Olo'eyktan", "You and Neytiri lead a generation. You hold the sky people back. You teach your children both languages. They prefer the older one."),
    ("end_bridge", "Bridge Between Worlds", "You broker, slowly, a peace between Pandora and a chastened RDA. The mining shrinks. The science stays. Grace, before she died, would have laughed."),
    ("end_eywa", "Inside Eywa", "Eventually you die. Your consciousness joins the network of the tree. Children, walking the forest, hear your voice in the wind. They take it for granted, the way you would have, once."),
])

INCEPTION = linear_story({
    "id": "fm-inception", "title": "Inception", "sourceTitle": "Inception",
    "kind": "movie", "synopsis": "You're a thief who steals secrets from dreams. Tonight's job: plant an idea instead. Your wife is dead. Or she's downstairs.",
    "releaseYear": 2010, "addedAt": "2026-03-13T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["dreams", "heist", "memory"], "rating": None, "loved": False,
}, [
    ("The Pitch", "Saito wants an idea planted in his rival's heir. He offers you a way home.", "Take it", "Path.", "Negotiate", "Smart."),
    ("Build a Team", "Arthur, Eames, Yusuf. You need an architect.", "Recruit Ariadne", "Path.", "Bring back Nash", "Familiar."),
    ("Mall Test", "Ariadne folds Paris in half. You smile.", "Hire her", "Path.", "Make her think", "Wise."),
    ("Mombasa", "Yusuf's chemist shop. The basement of sleepers.", "Ask why they sleep", "Curious.", "Get the compound", "Direct."),
    ("Saito Joins", "He invests himself in the job. Literally.", "Welcome him", "Strategy.", "Refuse him", "Honest."),
    ("Mal", "Your projection of your dead wife visits the rooms.", "Tell Ariadne", "Honest.", "Hide her", "Pride."),
    ("Layers", "Three dream levels: van, hotel, snow.", "Approve the plan", "Path.", "Add a kick", "Smart."),
    ("Boarding", "Sydney flight. Fischer is on board. The job begins on takeoff.", "Sit close", "Tactical.", "Sit far", "Cover."),
    ("Van", "Rain, gunfire, Yusuf at the wheel.", "Drive aggressive", "Speed.", "Drive defensive", "Smart."),
    ("Hotel", "Zero-G fight. Arthur in the hallway.", "Trust Arthur", "Friend.", "Coordinate", "Plan."),
    ("Snow Fortress", "Bunker, snowmobiles, Eames in disguise.", "Take the front", "Brave.", "Take the back", "Smart."),
    ("Limbo", "Mal pulls Fischer down. The whole thing nearly fails.", "Go after them", "Path.", "Send Ariadne", "Smart."),
    ("Old City", "You and Cobb walked here as a young couple. The buildings are your memory.", "Walk it", "Heart.", "Skip past", "Smart."),
    ("Mal Confronts", "She wants you to stay. Forever, here, with her.", "Refuse", "Honor.", "Almost agree", "Honest."),
    ("Confession", "You tell her, finally, that her shade is not her. You let her go.", "Speak gently", "Honor.", "Speak firmly", "Honest."),
    ("Catharsis", "Fischer's father's last word. The idea plants.", "Trust the work", "Path.", "Add a flourish", "Pride."),
    ("Kick", "Wake on the van's splash. Wake on the elevator. Wake on the plane.", "Stay awake", "Faith.", "Sleep again", "Honest."),
    ("LAX", "Customs. Family. You're home.", "Spin the top", "Test.", "Don't spin", "Faith."),
    ("Top Spinning", "You walk to your children. The top wobbles, maybe.", "Don't look back", "Faith.", "Look back", "Doubt."),
    ("Yard", "Your children turn. You hold them.", "Stay present", "Path.", "Plan one more job", "Honest."),
    ("Dinner", "You sit at the table. The food is real. You decide it's real.", "Believe it", "Faith.", "Test again tomorrow", "Honest."),
], [
    ("end_home", "Home", "You stay. You raise the kids. You teach, eventually, a small class at a university about the mind. You spin the top sometimes. It always falls."),
    ("end_dream", "Dream", "You learn, slowly, that you may be inside a dream. You decide it doesn't matter. The kids are real to you. The home is real to you. You choose this, knowingly."),
    ("end_extraction", "Back to the Work", "You can't quite stay out. You take one more job. The team comes back. Ariadne is, by then, in charge. You learn to be, finally, a colleague."),
])

GONE_WIND = linear_story({
    "id": "fm-gone-with-wind", "title": "Gone with the Wind", "sourceTitle": "Gone with the Wind",
    "kind": "movie", "synopsis": "Tara, Georgia, 1861. War is coming. You are Scarlett, sharp and impossible. The man you want isn't the man who wants you.",
    "releaseYear": 1939, "addedAt": "2026-03-12T00:00:00Z", "genre": "Drama",
    "tags": ["civil-war", "south", "epic"], "rating": None, "loved": False,
}, [
    ("Twelve Oaks", "Barbecue. Ashley announces his engagement to Melanie.", "Confront Ashley", "Spirit.", "Smile through it", "Strategy."),
    ("The Library", "You tell Ashley you love him. Rhett, behind the couch, hears.", "Slap him", "Spirit.", "Storm out", "Pride."),
    ("Rhett", "He bows. He says you're not a lady. He has noticed you.", "Snap back", "Spirit.", "Walk away", "Pride."),
    ("Charles", "You marry Charles to spite Ashley. Charles dies of pneumonia.", "Mourn correctly", "Society.", "Skip mourning", "Honest."),
    ("Atlanta", "You move to Atlanta. The hospitals fill. Rhett finds you again.", "Dance with him at the bazaar", "Spirit.", "Refuse", "Honor."),
    ("Melanie, in Labor", "Yankees near. Atlanta burns. You deliver Melanie's baby.", "Stay with her", "Honor.", "Try to flee", "Survive."),
    ("The Burning", "Rhett finds a wagon. He drives you out of the city.", "Trust him", "Path.", "Argue", "Spirit."),
    ("The Road", "He leaves you to join the army. You drive on alone.", "Be furious", "Spirit.", "Be grateful", "Honest."),
    ("Tara, Ruined", "Mother dead. Father broken. The fields untended.", "Rebuild", "Vow.", "Mourn", "Honest."),
    ("Tomorrow", "You eat a radish in the field. As God is your witness.", "Vow", "Iron.", "Promise yourself smaller things", "Honest."),
    ("Frank Kennedy", "You marry your sister's fiancé to save Tara.", "Run the lumber business", "Iron.", "Pretend to be a wife", "Cover."),
    ("Shantytown", "You are attacked on the road. Frank rides to avenge you.", "Warn him not to", "Wise.", "Let him go", "Honor."),
    ("Frank Dead", "Frank dies in the raid. You wear black again.", "Be honest with yourself", "Truth.", "Stay numb", "Survival."),
    ("Rhett, Returning", "He proposes. You accept for security.", "Marry him", "Practical.", "Wait", "Heart."),
    ("Honeymoon", "New Orleans. Lavish. He is, briefly, tender.", "Notice", "Honest.", "Take it for granted", "Spoiled."),
    ("Bonnie", "Your daughter. He adores her.", "Love her", "Heart.", "Love her at distance", "Honest."),
    ("Ashley, Again", "You almost kiss him. Melanie defends you publicly to the town.", "Apologize to Melanie", "Honor.", "Stay silent", "Pride."),
    ("Bonnie's Death", "She falls from her pony. Rhett breaks.", "Comfort him", "Honor.", "Sit with your grief", "Honest."),
    ("Melanie, Dying", "She makes you promise to care for Ashley.", "Promise", "Honor.", "Don't promise", "Honest."),
    ("Ashley's Truth", "Ashley, holding Melanie's hand, weeps for Melanie, not you.", "See clearly", "Truth.", "Look away", "Honest."),
    ("Rhett Leaving", "Frankly, my dear, he does not give a damn.", "Beg him", "Spirit.", "Let him go", "Pride."),
], [
    ("end_tara", "Tara, Again", "You return to Tara. You rebuild. You become, in time, the woman the town respects more than likes. You die at Tara, ancient, in a field full of tomorrows."),
    ("end_rhett", "Bringing Him Back", "You find Rhett, eventually. You apologize properly. He, slowly, comes around. You live, in the end, what you should have been living all along."),
    ("end_self", "Yourself, Finally", "You build a business. You travel. You marry, late, a man who is, finally, not a project. You realize at sixty you were trying to win an argument with a younger version of yourself. You forgive her. You forgive everyone."),
])

ET = linear_story({
    "id": "fm-et", "title": "E.T. the Extra-Terrestrial", "sourceTitle": "E.T. the Extra-Terrestrial",
    "kind": "movie", "synopsis": "California suburb. Your parents split. A creature with a glowing finger is in your shed. He wants to go home.",
    "releaseYear": 1982, "addedAt": "2026-03-11T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["alien", "childhood", "friendship"], "rating": None, "loved": False,
}, [
    ("Shed", "Something rustles. Reese's Pieces lead it to your room.", "Lure with candy", "Wise.", "Confront", "Brave."),
    ("Closet", "He hides among stuffed animals. He blinks.", "Don't tell Mom", "Wise.", "Tell Mom", "Honest."),
    ("Gertie", "Your little sister sees him. He, somehow, is okay with this.", "Trust her", "Friend.", "Swear her to secrecy", "Wise."),
    ("Elliott's Bond", "You feel what he feels. Sometimes drunk, sometimes sad.", "Trust the bond", "Path.", "Resist it", "Honest."),
    ("Frog Day", "You release the frogs in science class. You kiss Erika.", "Just go with it", "Joy.", "Apologize after", "Civil."),
    ("Phone Home", "He builds a radio out of an umbrella and a saw blade.", "Help him", "Friend.", "Slow him down", "Selfish."),
    ("Forest Trip", "He needs to broadcast from a hill.", "Carry the radio in your bike", "Brave.", "Drive there with Mike", "Smart."),
    ("Sick", "He turns gray. You turn gray.", "Stay close", "Friend.", "Tell Mom now", "Honest."),
    ("Discovery", "Mom finds him. Government men in suits arrive.", "Hide him", "Brave.", "Cooperate", "Wise."),
    ("Plastic Tent", "The house becomes a hospital.", "Stay by his side", "Friend.", "Stay out of the way", "Honor."),
    ("Heart Light", "His heart flickers. So does yours.", "Hold his hand", "Vow.", "Step back", "Honest."),
    ("Dead", "He stops glowing. You break.", "Mourn", "Honest.", "Refuse to mourn", "Hope."),
    ("Awake", "The flower blooms. He whispers your name.", "Don't tell the adults", "Wise.", "Tell the doctor", "Honest."),
    ("Escape Plan", "Mike and his friends. Bikes. A van.", "Steal the van", "Brave.", "Run on foot", "Smart."),
    ("Chase", "Police behind. You pedal. He, in the basket, lifts the bikes.", "Trust it", "Path.", "Be terrified", "Honest."),
    ("Forest, Again", "Spaceship lands. Lights through trees.", "Walk him up", "Honor.", "Wait at the edge", "Quiet."),
    ("Mom and Gertie", "They arrive. Gertie hands him a flower.", "Hug them", "Love.", "Stand alone", "Honest."),
    ("The Touch", "He touches his finger to your forehead. He'll be right here.", "Cry", "Honest.", "Smile", "Brave."),
    ("Departing", "He climbs aboard. The ship rises. The rainbow stripes are in the sky.", "Wave", "Honor.", "Stand still", "Honest."),
    ("Home, Now Quieter", "Mom's hand on your shoulder. The house is small. The world is bigger.", "Eat dinner", "Routine.", "Sit on the porch", "Quiet."),
    ("Later", "Years later you keep the dead flower in a book.", "Open the book sometimes", "Sentiment.", "Keep it closed", "Memory."),
], [
    ("end_grown", "Elliott, Grown", "You become an astronaut. You don't, in the end, meet him again. The stars are, you find, enough."),
    ("end_quiet", "Quiet Life", "You become a teacher in the same town. Gertie becomes a doctor. Mom remarries kindly. The flower is, still, in the book."),
    ("end_storyteller", "The Storyteller", "You write the story down for kids who don't believe in much anymore. They believe. Some of them, after, build radios out of unlikely parts."),
])

SPECS += [SCHINDLER, WIZARD_OZ, JURASSIC, MATRIX, AVATAR, INCEPTION, GONE_WIND, ET]

CITIZEN_KANE = linear_story({
    "id": "fm-citizen-kane", "title": "Citizen Kane", "sourceTitle": "Citizen Kane",
    "kind": "movie", "synopsis": "You're a reporter. Charles Foster Kane has died saying one word. Rosebud. Find out what it means before the deadline.",
    "releaseYear": 1941, "addedAt": "2026-03-10T00:00:00Z", "genre": "Drama",
    "tags": ["newspaper", "mystery", "classic"], "rating": None, "loved": False,
}, [
    ("The Newsroom", "Editor Rawlston wants a hook for the obituary. Rosebud, he says, is it.", "Take the assignment", "Path.", "Object", "Honest."),
    ("Thatcher Memorial", "A vault. The banker's memoirs. A child sled in the snow.", "Read them", "Path.", "Skim them", "Speed."),
    ("Bernstein", "Old, kind, loyal. He talks about Kane on the wharf.", "Sit with him", "Listen.", "Press him", "Job."),
    ("The First Paper", "Kane buys the Inquirer. He writes a Declaration of Principles.", "Note the document", "Path.", "Note the timing", "Smart."),
    ("Newsroom Party", "Kane buys the rival paper's whole staff. He throws a party.", "Mark the loyalty", "Wise.", "Mark the ego", "Honest."),
    ("Leland", "His old friend Leland talks honestly about love. He says Kane loved no one but himself.", "Note the contradiction", "Wise.", "Take it as truth", "Naive."),
    ("First Wife", "Emily Norton. The President's niece. Their marriage decays over breakfasts.", "Notice the marriage in the meals", "Path.", "Take it from her words", "Direct."),
    ("Susan", "He meets Susan Alexander on a street. She has a toothache. She sings, badly.", "Investigate the encounter", "Path.", "Move on", "Job."),
    ("Political Run", "Kane runs for governor. He is, briefly, beloved.", "Track the campaign", "Honest.", "Track the scandal", "Job."),
    ("The Hotel Room", "Boss Jim Gettys finds Kane and Susan. The newspapers will run a story.", "Note Kane's defiance", "Wise.", "Note his stupidity", "Honest."),
    ("The Scandal", "Kane loses the election. He loses Emily and Junior.", "Note the cost", "Honest.", "Tell yourself it was fate", "Story."),
    ("Susan's Career", "Kane builds her an opera house. She does not, in fact, sing well.", "Talk to Susan now", "Direct.", "Talk to the music critic", "Layered."),
    ("Atlantic City", "Susan, decades later, in a club. She drinks. She talks.", "Be gentle with her", "Care.", "Push for the story", "Job."),
    ("Xanadu", "Kane's house. Crates. Statues. Echoes.", "Walk the halls slowly", "Witness.", "Walk fast", "Job."),
    ("Susan's Departure", "She leaves him in a marble room. He destroys her bedroom.", "Notice the snowglobe", "Path.", "Notice his face", "Honest."),
    ("Rosebud, Whispered", "He dies alone, the snowglobe falling.", "Hold the image", "Witness.", "Cut away", "Job."),
    ("Raymond, the Butler", "He says Rosebud was nothing. He doesn't know.", "Believe him partly", "Wise.", "Suspect more", "Honest."),
    ("Crates Burning", "Workers burn old junk in the basement. A sled.", "Watch the fire", "Witness.", "Look away", "Honest."),
    ("Rosebud Burns", "On the sled the word ROSEBUD chars and curls.", "Notice it as audience", "Witness.", "Don't notice", "Honest."),
    ("Back at the Office", "You file the story without Rosebud's meaning.", "Write it well", "Honor.", "Write it fast", "Job."),
    ("Quitting", "You decide what kind of reporter to be next.", "Stay", "Career.", "Pivot to books", "New."),
], [
    ("end_book", "The Book", "You write a long book about Kane. It outlives the newspaper. People read it in college for decades."),
    ("end_paper", "The Daily", "You stay at the paper. You become managing editor. You think about Rosebud every Christmas, for some reason."),
    ("end_quiet", "Quietly Done", "You leave reporting. You take a job at a small magazine that does, mostly, longer pieces. You marry, eventually. You name nothing Rosebud."),
])

GOODFELLAS = linear_story({
    "id": "fm-goodfellas", "title": "Goodfellas", "sourceTitle": "Goodfellas",
    "kind": "movie", "synopsis": "As far back as you can remember, you wanted to be a gangster. You got it. Now the day starts at 6 a.m. and ends at 6 a.m. and the helicopter is, again, overhead.",
    "releaseYear": 1990, "addedAt": "2026-03-09T00:00:00Z", "genre": "Drama",
    "tags": ["mafia", "rise", "fall"], "rating": None, "loved": False,
}, [
    ("Brooklyn", "Paulie's cabstand. Errands. The first time you watch a car burn.", "Be useful", "In.", "Walk home", "Out."),
    ("Pinky Ring", "The men dress like the men. You imitate, you belong.", "Imitate", "Path.", "Stay yourself", "Honest."),
    ("Tommy", "Tommy is funny. Tommy is dangerous.", "Laugh", "Survive.", "Don't laugh", "Brave."),
    ("Jimmy", "Jimmy hands out hundred-dollar bills like a god.", "Take it", "In.", "Refuse it", "Out."),
    ("Karen", "You meet her at a wedding. She is, briefly, terrified.", "Be charming", "Heart.", "Be honest", "Truth."),
    ("Engagement", "You marry. Her mother does not know what to make of you.", "Win her mother", "Strategy.", "Win Karen", "Direct."),
    ("Hijacking", "Trucks at JFK. The first big score.", "Plan small", "Smart.", "Plan big", "Greedy."),
    ("Spider", "Tommy shoots Spider in the foot. Then in the chest.", "Be silent", "Survive.", "Vomit out back", "Honest."),
    ("Lufthansa", "Six million in cash and gold. Jimmy gets paranoid.", "Take the smallest cut", "Wise.", "Take the biggest", "Greedy."),
    ("Cocaine", "Florida. Pittsburgh. You start using.", "Stop", "Wise.", "Don't stop", "Honest."),
    ("Karen, Loaded", "She finds your stash. She flushes it. She is furious.", "Apologize", "Honor.", "Yell back", "Stress."),
    ("Tommy Made", "Tommy is told he'll be made. He goes to a basement.", "Note the suspicion", "Wise.", "Trust it", "Naive."),
    ("Tommy Dead", "It was for Billy Batts. The whole street goes quiet.", "Drink", "Honest.", "Don't drink", "Discipline."),
    ("Helicopter Day", "The helicopter. The sauce. The phone calls. Cocaine.", "Stop and breathe", "Try.", "Push through", "Honest."),
    ("Arrested", "DEA at the airport. The phone calls were tapped.", "Don't say anything", "Smart.", "Try to explain", "Foolish."),
    ("Bail", "Karen sells what she can. You're out.", "Sit at home", "Survive.", "See Jimmy", "Familiar."),
    ("Jimmy's Diner", "Jimmy offers you a trip to Florida. You realize, late, it's a hit.", "Refuse", "Survive.", "Almost go", "Honest."),
    ("Witness Protection", "Federal agents in a kitchen. A long list to sign.", "Sign", "Survive.", "Stall", "Honest."),
    ("Testimony", "You point at Jimmy. You point at Paulie. The room is, briefly, silent.", "Tell it all", "Honor.", "Tell it carefully", "Smart."),
    ("Nowhere, USA", "A house. A driveway. A grocery store. Spaghetti with ketchup.", "Try to like it", "Honor.", "Hate it openly", "Honest."),
    ("The End", "You order eggs in a bathrobe. You wave at the camera. You realize you're an average nobody.", "Hate it", "Honest.", "Make peace", "Survive."),
], [
    ("end_anonymous", "Schnook", "You spend the rest of your life as Henry Hill, by another name. You write a book in your fifties. You die in 2012 of a heart attack."),
    ("end_relapse", "Out", "You break protection. You return to New York anyway. You die in a parking lot in a year. Karen survives. The children are okay."),
    ("end_amends", "Amends, Eventually", "You make amends with Karen, with the kids, with yourself. The amends do not pay back what you took. They pay forward, modestly, to children who were not yours."),
])

SILENCE_LAMBS = linear_story({
    "id": "fm-silence-of-lambs", "title": "The Silence of the Lambs", "sourceTitle": "The Silence of the Lambs",
    "kind": "movie", "synopsis": "FBI Academy. A senator's daughter is missing. Hannibal Lecter has a profile to share, but only for a song.",
    "releaseYear": 1991, "addedAt": "2026-03-08T00:00:00Z", "genre": "Thriller",
    "tags": ["fbi", "serial", "psychological"], "rating": None, "loved": False,
}, [
    ("The Run", "Quantico woods. Crawford pulls you off the course.", "Listen", "Path.", "Ask why", "Curious."),
    ("Chilton's Office", "He flirts grossly. He hands you the case file.", "Decline gracefully", "Discipline.", "Be cold", "Honest."),
    ("The Cell", "Multiple Miggs spits. Lecter is upright behind glass.", "Stand still", "Brave.", "Step closer", "Direct."),
    ("Quid Pro Quo", "He wants something for every answer.", "Trade carefully", "Smart.", "Trade fully", "Brave."),
    ("Storage Unit", "Lecter's old patient's storage. A head in a jar.", "Document", "Discipline.", "Photograph", "Quick."),
    ("Senator's Daughter", "Catherine Martin is abducted from a parking lot.", "Time pressure", "Real.", "Pace", "Smart."),
    ("Bug, Genus", "A pupa in the throat. A death's-head moth.", "Pull on it", "Path.", "Show Crawford", "Process."),
    ("Lecter Moves", "Lecter is moved to Memphis. Senator wants a deal.", "Visit him there", "Brave.", "Stay back", "Wise."),
    ("Cage in the Hall", "Lecter, in a hockey mask, in a cage in a ballroom.", "Talk", "Direct.", "Listen", "Wise."),
    ("Your Mother, Late", "He asks about your father. You tell him about the lambs.", "Tell honestly", "Trust.", "Lie", "Wise."),
    ("Buffalo Bill", "Lecter slips you a name. Or a clue toward one. Geographic.", "Take it", "Path.", "Verify it", "Smart."),
    ("Belvedere", "House to house in a small town. The names from the seamstress.", "Door by door", "Discipline.", "Skip the easy ones", "Speed."),
    ("Mr. Gumb", "A man at a door. A moth in the hallway.", "Identify yourself", "Civil.", "Push past", "Brave."),
    ("Basement", "Stairs. Skin. Goggles in the dark.", "Don't shoot the dog", "Discipline.", "Look at the well", "Heart."),
    ("Catherine", "She is in a pit, screaming.", "Get to her after", "Mission.", "Try to free her now", "Heart."),
    ("Night Vision", "He sees you. You don't see him.", "Hold the gun out", "Brave.", "Listen", "Wise."),
    ("Shot", "You hear the click. You turn. You fire.", "Fire", "Path.", "Hold", "Honest."),
    ("Light", "The basement floods with backup. Catherine breathes.", "Carry her up", "Care.", "Treat the scene", "Discipline."),
    ("Graduation", "You graduate. Crawford shakes your hand.", "Take the moment", "Honor.", "Stay focused", "Discipline."),
    ("Lecter Calls", "A phone in your room. 'I do wish we could chat longer.'", "Hang up", "Discipline.", "Stay on", "Brave."),
    ("Sleep", "The lambs, when you try to sleep, are quieter.", "Try to sleep", "Honest.", "Stay awake reading", "Survive."),
], [
    ("end_agent", "Agent Starling", "You serve, decades, with distinction. Lecter does not come for you. The lambs, eventually, do quiet. You sleep."),
    ("end_teacher", "Teaching", "You move to Quantico as an instructor. You shape a generation. You meet your own students at lunch sometimes, twenty years on, and they call you ma'am."),
    ("end_lecter", "The Phone, Sometimes", "A phone rings, decades on. You let it. You realize, late, that some shadows are also, in their way, witnesses to who you became."),
])

SAVING_RYAN = linear_story({
    "id": "fm-saving-private-ryan", "title": "Saving Private Ryan", "sourceTitle": "Saving Private Ryan",
    "kind": "movie", "synopsis": "Omaha Beach, June 6, 1944. The ramp goes down. By the next week you're crossing France for one man whose brothers all died. Earn this.",
    "releaseYear": 1998, "addedAt": "2026-03-07T00:00:00Z", "genre": "Drama",
    "tags": ["war", "rescue", "WWII"], "rating": None, "loved": False,
}, [
    ("The Boat", "Spray, vomit, prayer. The ramp goes down.", "Lead off", "Brave.", "Go side", "Smart."),
    ("Beach", "Water, blood, sand. The seawall ahead.", "Crawl up", "Survive.", "Stand and run", "Brave."),
    ("Seawall", "Captain Miller's hand shakes. Orders are quiet.", "Steady the men", "Lead.", "Wait", "Honest."),
    ("Pillbox", "Bangalore. The wall breaches. The pillbox falls.", "Take prisoners", "Honor.", "Take none", "Cold."),
    ("Orders", "Find Ryan. One of four brothers. Three are dead.", "Argue the order", "Honest.", "Take it", "Soldier."),
    ("Squad", "Reiben, Mellish, Caparzo, Wade, Jackson, Upham, Horvath.", "Brief them", "Lead.", "Let Miller", "Honor."),
    ("French Town", "Sniper. A child handed across rubble.", "Save the child", "Heart.", "Press on", "Mission."),
    ("Caparzo", "Sniper takes Caparzo. Jackson takes the sniper.", "Mourn briefly", "Honor.", "Hate the sniper", "Anger."),
    ("Radio Tower", "A pinned squadron. A choice to engage or skirt.", "Engage", "Honor.", "Skirt", "Mission."),
    ("Machine Gun Nest", "You take it. Wade is killed in the assault.", "Spare the German", "Mercy.", "Don't", "Anger."),
    ("Steamboat Willie", "Wade is dead. The German shovels. Reiben wants him shot.", "Release him", "Honor.", "Shoot him", "Anger."),
    ("Reiben", "Reiben refuses to march. The squad almost shatters.", "Hold them together", "Lead.", "Let Reiben go", "Honest."),
    ("Captain's Hand", "Miller's hand shakes. He cries. The squad doesn't see.", "See him", "Honor.", "Look away", "Discipline."),
    ("Ryan Found", "Ryan, alive, won't leave his men. The bridge must be held.", "Help hold it", "Honor.", "Carry him out", "Mission."),
    ("Plan", "Cover, sticky bombs, ambush, fallback to alamo.", "Run the plan", "Discipline.", "Improvise", "Speed."),
    ("Tiger Tanks", "They arrive. The bombs work imperfectly.", "Hold", "Brave.", "Fall back", "Smart."),
    ("Mellish", "House by house. Mellish dies in a knife fight upstairs.", "Push to him", "Brother.", "Cover", "Mission."),
    ("Upham", "Upham freezes on the stairs. He does nothing.", "Forgive him later", "Honor.", "Hate him later", "Honest."),
    ("Miller", "Captain Miller is hit at the bridge. He shoots a tank with a pistol. The P-51s arrive.", "Hold his hand", "Honor.", "Press on", "Mission."),
    ("Last Words", "Earn this, he says. He dies.", "Vow", "Honor.", "Be silent", "Honest."),
    ("Old Man at the Grave", "Years later you stand at the cross. Your family behind you.", "Ask your wife if you've been a good man", "Honor.", "Salute and walk", "Quiet."),
], [
    ("end_earned", "Earn This", "You live a life worth earning. You marry kindly, work hard, raise children who do good. You never say much about the war. They know anyway."),
    ("end_teacher", "Teaching", "You teach high school history for decades. You don't bring up Normandy. The kids find it in books. They come to your desk after class. You answer carefully."),
    ("end_silence", "The Silence", "You don't talk about it. Your wife knows. Your children, eventually, know. Your grandchildren learn the soft version. The truth is, somehow, both."),
])

BTTF = linear_story({
    "id": "fm-back-to-future", "title": "Back to the Future", "sourceTitle": "Back to the Future",
    "kind": "movie", "synopsis": "Hill Valley, 1985. The DeLorean. The lightning. You end up in 1955, where your mother has a crush on you. Don't break the timeline.",
    "releaseYear": 1985, "addedAt": "2026-03-06T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["time-travel", "comedy", "family"], "rating": None, "loved": False,
}, [
    ("Twin Pines Mall", "1:21 gigawatts. Libyans. The clock starts.", "Drive", "Speed.", "Run", "Smart."),
    ("1955", "You arrive. Cows. A farmer with a shotgun.", "Apologize", "Civil.", "Run", "Smart."),
    ("Town Square", "Soda fountain. Your dad, George, getting bullied.", "Defend him quietly", "Right.", "Don't intervene", "Wise."),
    ("Lou's", "You order something. Lou is mean. You meet a boy who would become your dad's enemy.", "Buy a Coke", "Civil.", "Leave", "Smart."),
    ("Your Mother", "Lorraine sees you. She is, against all expectation, smitten.", "Be polite", "Wise.", "Be a friend", "Wise."),
    ("Doc, 1955", "You find young Doc in his garage. You show him the flux capacitor.", "Tell him the future", "Brave.", "Tell him only the basics", "Smart."),
    ("School", "Hill Valley High. George reads sci-fi in a closet.", "Coach George", "Path.", "Set up an introduction", "Smart."),
    ("Lou's, Again", "You convince George to ask Lorraine. He freezes. You volunteer to set it up.", "Set the dance plan", "Path.", "Cancel and replan", "Smart."),
    ("Lorraine Asks You", "She asks you to the dance. You realize the plan requires improvisation.", "Pretend to fall in love with her", "Strategy.", "Be direct", "Honest."),
    ("Biff", "Biff and his goons threaten George. You bait the car.", "Get in the trunk", "Plan.", "Run for it", "Smart."),
    ("Mother in the Car", "Lorraine kisses you. She says it feels like kissing her brother.", "Note the timeline glitch", "Wise.", "Be relieved", "Honest."),
    ("Biff at the Car", "Biff opens the door. Things move fast.", "Try to think", "Smart.", "Fight", "Brave."),
    ("George Saves Lorraine", "George, against his shape, throws a punch.", "Step back", "Honor.", "Cheer", "Joy."),
    ("Dance", "Earth Angel. They kiss. You start to fade from the photo.", "Pick up the guitar", "Path.", "Stand still", "Honest."),
    ("Johnny B. Goode", "You play. The band is ahead. The audience is, briefly, not ready.", "Tone it down", "Wise.", "Go big", "Joy."),
    ("Doc on the Roof", "Lightning, wire, clocktower. The plan is precise.", "Drive", "Path.", "Walk Doc through it again", "Wise."),
    ("Letter for Doc", "You write Doc a letter about Libyans. You leave it in his coat.", "Leave it taped", "Right.", "Tell him in person", "Honest."),
    ("Lightning Strikes", "It hits the wire. The car accelerates.", "Hold the wheel", "Steady.", "Push faster", "Speed."),
    ("Home", "Twin Pines becomes Lone Pine. The Libyans aren't here yet, then they are.", "Save Doc", "Honor.", "Run to safety", "Smart."),
    ("Better 1985", "Your dad is a successful novelist. Lorraine is happy. Biff polishes the car.", "Notice everything", "Wise.", "Just enjoy", "Honest."),
    ("Doc, Future", "Doc arrives in the DeLorean. The kids, he says.", "Get in", "Path.", "Wait", "Honest."),
], [
    ("end_future", "Roads, Optional", "You go to 2015. You return. You marry Jennifer. You become, eventually, a parent yourself, slightly more patient than your own dad."),
    ("end_stay", "Stay in '85", "You let Doc go alone. You build a normal life in 1985 with the parents you accidentally made better. You play guitar in a small band on weekends."),
    ("end_doc", "Doc, Forever", "You and Doc become lifelong collaborators. You don't, in the end, mass-produce anything. You build, mostly, one-off wonders. People drive across the country to see your garage."),
])

LION_KING = linear_story({
    "id": "fm-lion-king", "title": "The Lion King", "sourceTitle": "The Lion King",
    "kind": "movie", "synopsis": "Pride Rock. Your father is king. Your uncle has a plan. The savanna stretches forever, until it doesn't.",
    "releaseYear": 1994, "addedAt": "2026-03-05T00:00:00Z", "genre": "Fantasy",
    "tags": ["animated", "kingdom", "hakuna"], "rating": None, "loved": False,
}, [
    ("Pride Rock", "Sun, savanna, Rafiki lifting you above.", "Stay close to Mufasa", "Heart.", "Wander early", "Spirit."),
    ("Elephant Graveyard", "Scar tells you about it. You and Nala explore.", "Go anyway", "Brave.", "Stay near home", "Wise."),
    ("Hyenas", "They corner you. Mufasa arrives.", "Run", "Smart.", "Stand", "Brave."),
    ("Father's Lesson", "Stars and ancestors. The kings of the past watch.", "Believe", "Honor.", "Doubt", "Honest."),
    ("Stampede", "Scar's plan. Wildebeests in the gorge.", "Climb the tree", "Smart.", "Run with them", "Brave."),
    ("Mufasa Saves", "Mufasa pulls you up. Scar drops him.", "See it", "Witness.", "Look away", "Spare."),
    ("Run", "Scar tells you to run. You believe him.", "Run far", "Survive.", "Run nearby", "Loyal."),
    ("Hakuna Matata", "Timon and Pumbaa. Bugs for dinner.", "Try the bugs", "Friend.", "Refuse", "Honest."),
    ("Growing Up", "Years pass. You forget the rock. You almost forget yourself.", "Sing", "Joy.", "Stay quiet", "Wise."),
    ("Nala Returns", "She finds you. The pride is starving.", "Argue", "Honest.", "Listen", "Heart."),
    ("Rafiki", "He appears with a stick. He says your father lives in you.", "Look in the water", "Path.", "Look away", "Honest."),
    ("Mufasa in the Sky", "Remember who you are.", "Vow", "Path.", "Doubt", "Honest."),
    ("Run Home", "Pride Rock is a wasteland. Hyenas everywhere.", "Climb quietly", "Smart.", "Roar", "Brave."),
    ("Sarabi", "Your mother sees you. Briefly, she sees Mufasa.", "Embrace her", "Heart.", "Stand back", "Honor."),
    ("Scar's Confession", "He admits to killing your father.", "Lunge", "Anger.", "Hold", "Wise."),
    ("Fire", "Lightning. The rock burns.", "Climb high", "Smart.", "Fight low", "Brave."),
    ("Scar at the Edge", "He lies one more time.", "Spare him", "Mercy.", "Throw him", "Justice."),
    ("Hyenas Decide", "They turn on Scar. The rock is yours.", "Rain comes", "Renewal.", "Mourn the dead", "Honor."),
    ("Rain", "Rain on the rock. Sun after.", "Roar", "Honor.", "Stand quiet", "Honest."),
    ("Cub", "Years later. Rafiki lifts your child.", "Hold Nala's hand", "Family.", "Stand alone", "Honor."),
    ("Kings of the Past", "You teach your child the stars. The cycle is, again, a circle.", "Pass it on", "Honor.", "Keep it private", "Honest."),
], [
    ("end_king", "King", "You rule for decades. The savanna heals. Songs are sung about you. Some of them, sweetly, are about Pumbaa."),
    ("end_council", "The Council", "You build a council with hyenas at the table. The pride disagrees. The pride is, in the end, stronger for it."),
    ("end_legacy", "Circle", "You die old. Your cub becomes the next ruler. They, in turn, raise their own. The circle, you decide, is exactly as small as it ever was. And exactly as wide."),
])

AVENGERS = linear_story({
    "id": "fm-avengers-endgame", "title": "Avengers: Endgame", "sourceTitle": "Avengers: Endgame",
    "kind": "movie", "synopsis": "Half of all life is gone. Five years pass. A van pulls up with a man who has been in a smaller place. The time heist begins.",
    "releaseYear": 2019, "addedAt": "2026-03-04T00:00:00Z", "genre": "Action",
    "tags": ["mcu", "time", "endgame"], "rating": None, "loved": False,
}, [
    ("Tony in Space", "You drift. The video is for Pepper. The oxygen is low.", "Send the message", "Honest.", "Save power", "Hope."),
    ("Avengers Compound", "The remaining gather. Carol arrives.", "Plan to hunt Thanos", "Action.", "Heal first", "Wise."),
    ("Garden", "Thanos, broken, on a farm. He destroyed the stones.", "Question him", "Honest.", "Strike", "Anger."),
    ("Five Years", "Group therapy in Brooklyn. Steve listens to a man talk about a date.", "Sit with the grief", "Honor.", "Bury it", "Survive."),
    ("Scott Lang", "Van arrives. Scott has been in the quantum realm. He has an idea.", "Bring it to Tony", "Path.", "Take it to Bruce", "Process."),
    ("Tony's No", "Tony, dad, refuses. Then he runs the math.", "Wait", "Patient.", "Push", "Honest."),
    ("Bruce/Hulk", "He has integrated. He drinks juice at brunches.", "Welcome him", "Friend.", "Tease him", "Civil."),
    ("Thor in New Asgard", "He has aged poorly. He plays Fortnite.", "Be kind", "Honor.", "Be honest", "Hard."),
    ("Time Heist Plan", "Teams. Stones. Branches.", "Sign off", "Path.", "Adjust the plan", "Smart."),
    ("Asgard", "Frigga gives Thor a hug. He, briefly, finds himself.", "Stay for the hug", "Heart.", "Keep moving", "Mission."),
    ("Vormir", "Black Widow and Hawkeye. Soul stone.", "Volunteer Hawkeye", "Honor.", "Volunteer Nat", "Honor."),
    ("Nat", "Nat goes over the edge. Hawkeye holds the stone.", "Mourn her properly", "Honor.", "Press on", "Mission."),
    ("New York", "Loki escapes with the tesseract in the alternate 2012.", "Recover the scepter", "Path.", "Pursue Loki", "Mission."),
    ("Camp Lehigh", "Tony's father. A small conversation.", "Speak as a stranger", "Honor.", "Almost tell him", "Honest."),
    ("Future Past", "Nebula's chip is read by past Thanos.", "Find out fast", "Discipline.", "Push the gauntlet", "Speed."),
    ("Snap", "Bruce snaps. Half the universe comes back.", "Help him through", "Care.", "Make him rest", "Honor."),
    ("Compound Attack", "Past Thanos arrives. The compound falls.", "Hold", "Brave.", "Retreat", "Smart."),
    ("Portals", "Every hero who came back, came back. Avengers Assemble.", "Take the line", "Honor.", "Take the field", "Action."),
    ("Carol vs. Thanos", "She fights him for the gauntlet. Thanos uses the power stone.", "Trust her", "Faith.", "Help her", "Action."),
    ("I Am Iron Man", "Tony takes the stones. He snaps. He turns to ash, calmly.", "Hold him", "Honor.", "Stand back", "Honor."),
    ("Funeral", "By a lake. Pepper. Morgan. Old friends.", "Stand", "Honor.", "Speak softly", "Heart."),
], [
    ("end_steve", "The Dance", "Steve goes back to live the life he didn't take. He returns old. He hands the shield to Sam. He sits on a bench by the water with a faded photo."),
    ("end_pepper", "Pepper, After", "You watch Pepper and Morgan in the field by the lake. They are, somehow, okay. The world is okay. You give Tony's helmet a small bow."),
    ("end_phase4", "What Comes Next", "Whatever the next decade brings, the team is bigger now. Sam carries the shield. Bucky writes letters. You realize a saga doesn't end. It just rolls."),
])

PSYCHO = linear_story({
    "id": "fm-psycho", "title": "Psycho", "sourceTitle": "Psycho",
    "kind": "movie", "synopsis": "Phoenix. A motel. A bathroom. A boy and his mother. You took forty thousand dollars on impulse. You'll wish you hadn't, soon.",
    "releaseYear": 1960, "addedAt": "2026-03-03T00:00:00Z", "genre": "Horror",
    "tags": ["classic", "motel", "twist"], "rating": None, "loved": False,
}, [
    ("Friday Lunch", "Sam in a hotel room. The cash from the office is heavy.", "Take it", "Decision.", "Don't", "Wise."),
    ("On the Road", "You stop at a dealer. You change cars.", "Sleep at a motel", "Wise.", "Drive all night", "Brave."),
    ("Bates Motel", "Vacancy. A boy at the office. His mother shouts upstairs.", "Check in", "Path.", "Move on", "Wise."),
    ("Parlor", "Sandwiches and milk. Stuffed birds.", "Listen", "Wise.", "Eat fast", "Honest."),
    ("Bathroom", "Shower. The curtain. The shadow.", "Hear the steps", "Wise.", "Don't", "Honest."),
    ("After", "Norman finds the room. He cleans, carefully, with bleach.", "Notice the car", "Wise.", "Notice the swamp", "Smart."),
    ("Detective Arbogast", "He asks Norman questions. The hallway creaks.", "Push", "Honest.", "Wait", "Wise."),
    ("Stairs", "The detective climbs. The door opens.", "Survive", "Wise.", "Press on", "Brave."),
    ("Sam and Lila", "Marion's sister and the boyfriend come to find her.", "Visit Norman", "Path.", "Visit the sheriff first", "Smart."),
    ("Sheriff", "Mother has been dead for ten years.", "Believe it", "Wise.", "Don't believe it", "Honest."),
    ("Lila Investigates", "She goes to the house. Sam keeps Norman talking.", "Search every room", "Brave.", "Search only downstairs", "Smart."),
    ("Cellar", "Lila descends. A figure in a chair. A wig.", "Don't scream", "Survive.", "Scream", "Honest."),
    ("Norman", "Norman enters with a knife. Sam stops him.", "Hold him", "Honor.", "Knock him out", "Pragmatic."),
    ("Hospital Interview", "A psychiatrist explains, calmly, what happened.", "Listen carefully", "Wise.", "Leave", "Honest."),
    ("Cell", "Norman, smiling. A fly.", "Look away", "Honor.", "Watch", "Witness."),
    ("Funeral", "Marion is buried. Sam holds Lila's hand.", "Stand", "Honor.", "Speak", "Honest."),
    ("Sam, Quiet", "Sam, after, drinks too much. He's, in a way, ashamed.", "Forgive him", "Honor.", "Move on without him", "Honest."),
    ("Lila, Sharp", "Lila will not let it go. She presses the DA.", "Help her", "Right.", "Step back", "Healing."),
    ("The Property", "The motel, in foreclosure, is sold to a couple who don't know.", "Tell them", "Honor.", "Don't", "Honest."),
    ("Years Later", "You read a paper. Norman is still there. Still smiling, still inside.", "Visit him", "Brave.", "Don't", "Wise."),
    ("Your Life", "You move on. You marry quietly. You don't tell most people about Phoenix.", "Tell your spouse", "Honest.", "Bury it", "Honest."),
], [
    ("end_sam", "Sam and Lila", "You and Lila, after years, end up married. The marriage is, against all odds, kind. You buy a small business in Fairvale. You sleep poorly some nights."),
    ("end_quiet", "Quietly", "You move to California. You become a teacher. You don't, in the end, talk about the motel. The story, you decide, was never yours."),
    ("end_press", "The Press", "You write a long piece for a magazine. It becomes a book. The book becomes a movie, twice. You are paid. You give half away."),
])

SPECS += [CITIZEN_KANE, GOODFELLAS, SILENCE_LAMBS, SAVING_RYAN, BTTF, LION_KING, AVENGERS, PSYCHO]

CASABLANCA = linear_story({
    "id": "fm-casablanca", "title": "Casablanca", "sourceTitle": "Casablanca",
    "kind": "movie", "synopsis": "Casablanca, 1941. You run a small nightclub. Of all the gin joints in all the world, she walks into yours. With her husband. With letters of transit in your safe.",
    "releaseYear": 1942, "addedAt": "2026-03-02T00:00:00Z", "genre": "Drama",
    "tags": ["wartime", "love", "classic"], "rating": None, "loved": False,
}, [
    ("Rick's Cafe", "Smoke, piano, refugees in the corners. You don't drink with customers.", "Walk the room", "Owner.", "Stay at the bar", "Distance."),
    ("Ugarte", "He hands you the letters of transit. He is, by sunrise, dead.", "Hide them", "Smart.", "Refuse them", "Honor."),
    ("Captain Renault", "He shrugs. He plays both sides. He is, mostly, a friend.", "Trust him partly", "Wise.", "Trust him fully", "Naive."),
    ("Major Strasser", "German command. He has a list. Your name is, perhaps, on it.", "Stay polite", "Survive.", "Stay cold", "Honest."),
    ("Sam at the Piano", "He plays only what you say.", "Let him play whatever", "Friend.", "Tell him no", "Discipline."),
    ("Ilsa", "She walks in. Sam sees her. He doesn't play it. She asks.", "Stay in the back", "Pride.", "Greet her", "Honor."),
    ("As Time Goes By", "Sam plays it. You walk out. She looks up.", "Be cold", "Pride.", "Be honest", "Truth."),
    ("Victor Laszlo", "Her husband. Czech resistance. Hunted.", "Be civil", "Honor.", "Be cold", "Pride."),
    ("Letters of Transit", "You alone, in the world, have them. Two exits to Lisbon.", "Tell no one", "Wise.", "Hint to Renault", "Strategic."),
    ("Paris Flashback", "A train station, a letter, rain on the platform.", "Remember fully", "Honest.", "Bury it", "Survive."),
    ("Ilsa's Visit", "Late, she comes to your office. She tells you her side.", "Listen", "Honor.", "Refuse", "Pride."),
    ("The Marseillaise", "Laszlo leads the band. The room rises. Strasser's face goes hard.", "Nod to Sam to play", "Honor.", "Don't intervene", "Honest."),
    ("Ilsa Returns", "Late. A gun. Tears. She tells you she loves you.", "Believe her", "Heart.", "Doubt her", "Wise."),
    ("Decision Forming", "You decide which two get the letters.", "You and Ilsa", "Heart.", "Ilsa and Laszlo", "Honor."),
    ("Briefing Renault", "You set up the captain. You set the plan.", "Brief him false", "Strategy.", "Brief him true", "Naive."),
    ("Laszlo, Talked To", "You tell Laszlo he must take Ilsa. You don't tell him you and she nearly stayed.", "Be plain", "Honor.", "Be careful", "Tone."),
    ("Airport", "Fog. A plane. Strasser arriving.", "Move fast", "Action.", "Stall", "Patience."),
    ("Hill of Beans", "Ilsa, you say, the problems of three little people don't amount to a hill of beans.", "Speak the speech", "Honor.", "Speak only the gist", "Style."),
    ("Strasser", "He arrives. He calls headquarters. You raise the pistol.", "Shoot", "Brave.", "Talk", "Wise."),
    ("Renault", "He says round up the usual suspects. He is, finally, choosing.", "Welcome him", "Friend.", "Suspect him", "Wise."),
    ("Walk Off", "You and Renault, in the fog, talk about a Free French garrison.", "Beautiful friendship", "Honor.", "Quiet farewell", "Honest."),
], [
    ("end_friendship", "Beautiful Friendship", "You and Renault join the resistance. The war ends, eventually. You return to Casablanca after, an older man. The cafe, somehow, is still there."),
    ("end_paris", "Paris, Again", "Years after the war, Ilsa, widowed, finds you in Paris. You sit at a cafe. The world has changed. You haven't, much."),
    ("end_quiet", "Quiet", "You die during the war, in a small action that doesn't make the papers. Sam, eventually, plays the song again, somewhere, to no one in particular. He smiles."),
])

# ===========================================================================
# FAMOUS BOOKS — top 25 by global fame
# ===========================================================================

PRIDE_PREJUDICE = linear_story({
    "id": "fb-pride-prejudice", "title": "Pride and Prejudice", "sourceTitle": "Pride and Prejudice",
    "kind": "book", "synopsis": "Longbourn, regency England. A single man in possession of a good fortune is in want of a wife. Your mother is, somehow, aware of every such man in the county.",
    "releaseYear": 1813, "addedAt": "2026-03-01T00:00:00Z", "genre": "Drama",
    "tags": ["austen", "marriage", "wit"], "rating": None, "loved": False,
}, [
    ("Netherfield Lets", "Bingley has taken Netherfield. Mama is, immediately, planning.", "Indulge her", "Civil.", "Tease her", "Spirit."),
    ("Meryton Assembly", "Bingley is amiable. His friend Darcy is, instantly, insufferable.", "Be amused by him", "Wit.", "Be wounded", "Honest."),
    ("Tolerable", "Darcy says you are tolerable but not handsome enough to tempt him. Charlotte overhears.", "Laugh it off", "Pride.", "File it away", "Honest."),
    ("Jane and Bingley", "Jane is sent to Netherfield in the rain. She catches cold.", "Walk to nurse her", "Sister.", "Wait", "Modesty."),
    ("Muddy Petticoats", "You arrive at Netherfield, muddy. The Bingley sisters notice.", "Ignore them", "Spirit.", "Apologize", "Civil."),
    ("Darcy in the Library", "He watches you across rooms. You assume the worst of him.", "Stay sharp with him", "Spirit.", "Be curious", "Honest."),
    ("Mr. Collins", "A cousin, awful, proposes. He will inherit Longbourn.", "Refuse", "Self.", "Marry him", "Family."),
    ("Charlotte", "Your friend marries him. You are, at first, hurt.", "Understand her", "Honor.", "Judge her", "Pride."),
    ("Wickham", "A charming officer. He tells you Darcy ruined him.", "Believe him", "Sympathetic.", "Doubt him", "Wise."),
    ("Hunsford", "You visit Charlotte. Lady Catherine de Bourgh is, somehow, much.", "Endure", "Civil.", "Spar", "Spirit."),
    ("Darcy's Proposal", "He proposes, against his will. He is, in proposing, awful.", "Refuse him", "Honor.", "Hesitate", "Honest."),
    ("The Letter", "He writes you a letter. Wickham is, in fact, a scoundrel.", "Reread it", "Wise.", "Burn it", "Pride."),
    ("Pemberley", "You tour, by chance. The house is, mortifyingly, lovely.", "Admire it", "Honest.", "Mock it", "Pride."),
    ("Darcy, Surprised", "He returns early. He is, against expectation, kind.", "Be civil", "Civil.", "Be flustered", "Honest."),
    ("Lydia's Elopement", "Your youngest sister has run off with Wickham.", "Hurry home", "Family.", "Stay calm", "Civil."),
    ("Mr. Darcy Acts", "He, secretly, arranges the marriage and pays Wickham's debts.", "Suspect him gratefully", "Honor.", "Suspect uncle", "Naive."),
    ("Lady Catherine Visits", "She demands you promise not to marry her nephew.", "Refuse to promise", "Spirit.", "Pretend", "Strategy."),
    ("Walk Out", "Darcy proposes again. Differently.", "Accept", "Heart.", "Confess your error first", "Honor."),
    ("Mother", "Mama, hearing, almost faints with joy.", "Tolerate", "Family.", "Calm her", "Patient."),
    ("Wedding", "A double wedding for Jane and you. Darcy stands tall. Bingley smiles.", "Take Darcy's hand", "Path.", "Take Jane's hand first", "Sister."),
    ("Pemberley, Yours", "You walk the library with the master of it. The shelves are higher than the house in Hertfordshire.", "Read often", "Joy.", "Manage the estate", "Duty."),
], [
    ("end_pemberley", "Mistress of Pemberley", "You manage Pemberley with grace. The Darcy heirs are, mercifully, more like their father than your mother. Lady Catherine, eventually, visits."),
    ("end_sister", "Both Sisters", "Jane and you live within a day's ride. Your children grow up together. You are, in middle age, sometimes silly with her in the way of girls in a sitting room."),
    ("end_writer", "Writer", "You write, late in life, a quiet anonymous novel about a country family with too many daughters. It does, surprisingly, well."),
])

NINETEEN_EIGHTY_FOUR = linear_story({
    "id": "fb-1984", "title": "1984", "sourceTitle": "1984",
    "kind": "book", "synopsis": "Oceania. The Ministry of Truth. Big Brother watches. You buy a diary on impulse. Today you write: down with Big Brother.",
    "releaseYear": 1949, "addedAt": "2026-02-28T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["dystopia", "orwell", "thought"], "rating": None, "loved": False,
}, [
    ("The Diary", "Cream-laid pages. The pen scratches. The telescreen, you hope, can't see your hands.", "Write the line", "Brave.", "Write a safer line", "Wise."),
    ("Telescreen", "You face it for morning exercise. You are, by your face, a citizen.", "Smile", "Performance.", "Stay blank", "Honest."),
    ("Julia", "A dark-haired colleague drops a note into your hand. I love you.", "Trust", "Heart.", "Distrust", "Wise."),
    ("The Field", "A meadow outside the city. The first kiss.", "Be present", "Honest.", "Be careful", "Wise."),
    ("Mr. Charrington's Room", "An attic room above an antique shop. A coral paperweight on the table.", "Rent it", "Heart.", "Decline", "Wise."),
    ("Newspeak Drafting", "At work, you compress language. Each draft removes a word.", "Note it", "Honest.", "Pretend not to note", "Survive."),
    ("Memory Hole", "You drop a slip of paper, an entire person, into a memory hole.", "Wonder if she existed", "Honest.", "Move on", "Survive."),
    ("O'Brien", "Your superior, in a high office, drops a hint. He believes, you decide, in the resistance.", "Visit him", "Path.", "Stall", "Wise."),
    ("Goldstein's Book", "He hands you the book in a brown paper wrapper. You and Julia read it in the attic.", "Read it together", "Path.", "Hide it", "Wise."),
    ("Antiques", "Mr. Charrington is, you discover later, not a kind old man.", "Suspect him", "Wise.", "Trust him", "Naive."),
    ("Arrest", "Boots on the stairs. The paperweight breaks on the hearth.", "Stay still", "Survive.", "Resist", "Brave."),
    ("Ministry of Love", "White light. No darkness. They know what you've written.", "Refuse to name Julia", "Honor.", "Name her", "Survive."),
    ("Room 101", "Your worst fear. Cage. Rat.", "Endure", "Brave.", "Beg", "Survive."),
    ("Do it to Julia", "You say it.", "Mean it for a moment", "Honest.", "Don't mean it", "Honor."),
    ("Released", "You are released into Victory Square. You drink Victory Gin.", "Drink", "Survive.", "Don't", "Honest."),
    ("Julia, Met Again", "She looks worn. She tells you she did it too. You agree quietly to never speak again.", "Walk away", "Honor.", "Sit a moment", "Honest."),
    ("Chess in the Cafe", "You play yourself. White always wins.", "Move", "Routine.", "Don't move", "Honest."),
    ("Telescreen Bulletin", "Africa is, somehow, ours. You drink.", "Cheer", "Survive.", "Be still", "Honest."),
    ("The Old Tune", "You hum, briefly, the old children's rhyme.", "Hum it", "Defiance.", "Stop", "Wise."),
    ("Big Brother", "His face on the screen. You realize, somewhere, you love him.", "Notice it", "Honest.", "Refuse it", "Brave."),
    ("Pencil and Diary", "You think, briefly, of buying paper again.", "Don't", "Survive.", "Do", "Honor."),
], [
    ("end_compliant", "Loved Big Brother", "You die some years later, unnoticed, with the right songs on your lips. Whatever you thought before is, finally, gone."),
    ("end_paper", "The Second Diary", "You buy paper. You write. You bury it. Two centuries later a scholar finds the box and asks who you were."),
    ("end_meadow", "The Meadow", "On your worst nights you remember the meadow. The first kiss. The single hour you were, in fact, a free person. You decide the hour was worth the rest. You don't tell anyone."),
])

MOCKINGBIRD = linear_story({
    "id": "fb-mockingbird", "title": "To Kill a Mockingbird", "sourceTitle": "To Kill a Mockingbird",
    "kind": "book", "synopsis": "Maycomb, Alabama, summer. You are Scout. Your father, Atticus, will be defending a Black man no Maycomb jury wants acquitted. Don't shoot a mockingbird.",
    "releaseYear": 1960, "addedAt": "2026-02-27T00:00:00Z", "genre": "Drama",
    "tags": ["south", "justice", "childhood"], "rating": None, "loved": False,
}, [
    ("Summer", "Jem, Dill, the tire swing. You run barefoot.", "Play", "Joy.", "Watch the street", "Honest."),
    ("Boo Radley", "Dare him out, Jem says. The house is closed up.", "Touch the door", "Brave.", "Stay on the sidewalk", "Wise."),
    ("Calpurnia", "She corrects you. She loves you. She is, you realize, the household's spine.", "Listen", "Honor.", "Push back", "Spirit."),
    ("First Day", "Miss Caroline tells you not to read. You stop.", "Comply", "Survive.", "Argue", "Spirit."),
    ("Atticus", "He stands up. He sits down. He tells you to climb into someone's skin.", "Climb in", "Honor.", "Refuse", "Honest."),
    ("Tom Robinson", "A man accused. Atticus accepts the case.", "Be proud", "Honor.", "Be scared", "Honest."),
    ("Jail at Night", "A crowd. Atticus reads under a lamp. You step out.", "Talk to Mr. Cunningham", "Brave.", "Stay hidden", "Wise."),
    ("Trial Day", "The colored balcony. Reverend Sykes makes room.", "Sit there", "Honor.", "Sit on the lawn", "Honest."),
    ("Cross-Examination", "Atticus, gentle, takes apart Mayella's story.", "Watch carefully", "Honor.", "Cry", "Honest."),
    ("Tom's Testimony", "He says he felt sorry for her. The courtroom shifts.", "Note the moment", "Honor.", "Hold breath", "Witness."),
    ("Closing", "Atticus speaks of equality. The room is silent.", "Stand", "Honor.", "Sit", "Honor."),
    ("Verdict", "Guilty.", "Don't cry in the balcony", "Discipline.", "Cry", "Honest."),
    ("Aunt Alexandra", "She tells you a lady doesn't act like that.", "Hold the line", "Spirit.", "Concede", "Civil."),
    ("Tom Tries to Run", "Tom is shot. The town is, for a moment, ashamed.", "Mourn", "Honor.", "Hate", "Honest."),
    ("Halloween Pageant", "You are a ham. The school is dark.", "Wear it", "Joy.", "Refuse it", "Pride."),
    ("Walking Home", "Footsteps behind. Bob Ewell.", "Run", "Survive.", "Freeze", "Honest."),
    ("Saved", "A man you don't see carries Jem home.", "Sit with Jem", "Care.", "Find the man", "Honest."),
    ("Behind the Door", "Boo Radley, finally, in your house. White skin, soft voice.", "Smile", "Honor.", "Stare", "Honest."),
    ("The Porch", "You walk Boo home. You stand on his porch and look at the street through his eyes.", "Look long", "Wise.", "Look briefly", "Honest."),
    ("Atticus, Tucking In", "He reads to Jem. He stays.", "Sleep", "Safe.", "Listen", "Honor."),
    ("Years On", "You grow up. Maycomb does, slowly, change. The county school, eventually, is a different building.", "Stay", "Roots.", "Leave", "Forward."),
], [
    ("end_writer", "Writer", "You become a writer. You publish a small careful book about a town you loved and didn't. The book becomes the way many people learn what you learned."),
    ("end_law", "Law", "You become a lawyer. You take, eventually, your father's office. The desk is the same. The work is harder than he made it look."),
    ("end_porch", "Porch", "You stay in Maycomb. You teach school. You sit, sometimes, on Boo's old porch. The town heals slowly. So do you."),
])

GATSBY = linear_story({
    "id": "fb-great-gatsby", "title": "The Great Gatsby", "sourceTitle": "The Great Gatsby",
    "kind": "book", "synopsis": "West Egg, 1922. A mansion next door throws parties without inviting anyone. The owner — Gatsby — has, you'll find, planned this evening for five years.",
    "releaseYear": 1925, "addedAt": "2026-02-26T00:00:00Z", "genre": "Drama",
    "tags": ["jazz", "money", "tragic"], "rating": None, "loved": False,
}, [
    ("The Bungalow", "You rent next to Gatsby's mansion. The lawn glows.", "Settle in", "Quiet.", "Walk the property line", "Curious."),
    ("Daisy's House", "East Egg, across the bay. Daisy, your cousin. Tom, her husband.", "Visit", "Family.", "Decline", "Wise."),
    ("Myrtle", "Tom takes you to the city. He keeps Myrtle.", "Notice", "Honest.", "Pretend not to notice", "Civil."),
    ("First Party", "Gatsby's lawn. Champagne. Strangers. You haven't met the host.", "Wander", "Curious.", "Stay near the bar", "Wise."),
    ("Meeting Gatsby", "A man with a careful smile. Old sport.", "Be polite", "Civil.", "Be skeptical", "Honest."),
    ("The Plan", "Gatsby asks if you'd invite Daisy for tea.", "Agree", "Path.", "Hesitate", "Wise."),
    ("Tea", "Rain. Roses delivered. Gatsby pacing. Daisy arrives.", "Step out for them", "Care.", "Stay", "Wise."),
    ("Pool House", "Daisy weeps over the shirts. The image is, in a way, the whole novel.", "Witness", "Honest.", "Look away", "Honest."),
    ("Tom Notices", "Tom is, finally, aware. He goes hunting.", "Brace", "Wise.", "Don't tip Gatsby", "Honor."),
    ("Plaza Hotel", "Heat, gin, accusations.", "Stay calm", "Civil.", "Stay silent", "Honest."),
    ("Tom's Hammer", "He produces evidence about Gatsby's money.", "Watch Daisy's face", "Honest.", "Watch Gatsby's", "Witness."),
    ("Drive Back", "Gatsby insists on letting Daisy drive.", "Sit in the back", "Witness.", "Argue", "Wise."),
    ("Valley of Ashes", "The car strikes Myrtle. Daisy does not stop.", "Witness", "Honest.", "Beg her to stop", "Brave."),
    ("Long Island, Late", "Gatsby tells you he'll take the blame.", "Tell him no", "Wise.", "Let him", "Honor."),
    ("Pool", "He waits for a call that won't come. He floats in the pool.", "Visit him", "Friend.", "Stay home", "Wise."),
    ("Wilson", "George Wilson finds the house. The shot is small.", "Hear it", "Witness.", "Don't hear it", "Survive."),
    ("Funeral", "Three mourners. You. Owl Eyes. Gatsby's father.", "Stand", "Honor.", "Leave early", "Honest."),
    ("Owl Eyes", "He says, the poor son of a bitch. He means it kindly.", "Agree", "Honor.", "Be quiet", "Honest."),
    ("Daisy and Tom", "They leave town with no forwarding address.", "Note the careless", "Honest.", "Forgive them", "Mercy."),
    ("The Green Light", "You stand at the end of the dock. The light is, again, just a light.", "Stay a moment", "Witness.", "Walk back", "Honest."),
    ("Home", "You move home to the Midwest. You write the story down.", "Begin to write", "Path.", "Burn the draft", "Honest."),
], [
    ("end_book", "The Book", "You write the book. It is, in the end, kind to Gatsby. The book outlives you. So do the parties, in their way."),
    ("end_midwest", "Midwest", "You go home. You marry quietly. The Eggs become a long ago. You are, sometimes, in dreams, on the lawn again."),
    ("end_lawyer", "Bonds", "You stay in New York and become, against your better judgement, a bond salesman. You retire early. You buy a small green-lit dock somewhere upstate, just for the joke."),
])

CATCHER_RYE = linear_story({
    "id": "fb-catcher-rye", "title": "The Catcher in the Rye", "sourceTitle": "The Catcher in the Rye",
    "kind": "book", "synopsis": "Pencey Prep, December. You've been expelled. You take the train to New York. You have three days before your parents find out.",
    "releaseYear": 1951, "addedAt": "2026-02-25T00:00:00Z", "genre": "Drama",
    "tags": ["adolescence", "salinger", "NYC"], "rating": None, "loved": False,
}, [
    ("Dorm Goodbye", "Stradlater is, you think, a phony. You leave with a hat.", "Punch him", "Brave.", "Walk", "Wise."),
    ("Train", "Mothers across the aisle. You lie about her son.", "Lie kindly", "Care.", "Tell the truth", "Honest."),
    ("Penn Station", "Cab. Phoenix wanted, hotel suggested.", "The Edmont", "Path.", "Walk", "Honest."),
    ("Lavender Room", "Three women from Seattle. Dancing.", "Buy them drinks", "Lonely.", "Leave", "Wise."),
    ("Sunny", "An elevator boy sends up a girl. You decide not to.", "Send her away", "Honest.", "Stay", "Lonely."),
    ("Beat Up", "Maurice takes more money. Your nose bleeds.", "Cry quietly", "Honest.", "Plan revenge", "Foolish."),
    ("Sally Hayes", "You take her ice skating. You ask her to run away.", "Stop yourself", "Wise.", "Press", "Foolish."),
    ("Carl Luce", "Old schoolmate. He is, charitably, a snob.", "Endure him", "Civil.", "Leave", "Honest."),
    ("Drunk", "Late night, you call Sally. You apologize, sort of.", "Get home", "Wise.", "Wander", "Honest."),
    ("Park Lake", "The ducks. You ask cabbies where they go in winter.", "Wonder", "Honest.", "Move on", "Wise."),
    ("Phoebe", "You sneak home. Your sister is, against everything, a real person.", "Tell her you're going west", "Honest.", "Tell her you came to see her", "Care."),
    ("Mr. Antolini", "Your old English teacher. He pats your head while you sleep.", "Leave politely", "Wise.", "Stay angry", "Misread."),
    ("Museum", "The mummies. The display cases. You always loved that things stayed the same.", "Sit", "Honest.", "Walk", "Survive."),
    ("Phoebe's Suitcase", "She comes with a suitcase. She wants to go west with you.", "Tell her no", "Honor.", "Take her", "Foolish."),
    ("Carousel", "Central Park. She rides. It rains.", "Watch", "Honest.", "Worry", "Honest."),
    ("Sit in the Rain", "You realize you're not running away. You're just tired.", "Cry honestly", "Honest.", "Smile", "Brave."),
    ("Home", "You go home. The sick part of you sleeps a long time.", "Sleep", "Honest.", "Stay up reading", "Survive."),
    ("Hospital", "Out west, technically. A doctor. You talk about things.", "Talk", "Honest.", "Don't talk", "Survive."),
    ("D.B.", "Your brother visits. He drives a fancy car. He is, in his way, kind.", "Forgive him", "Brother.", "Stay distant", "Honest."),
    ("Coming Back", "You're going to a new school in the fall.", "Try", "Honest.", "Don't try", "Honest."),
    ("Missing People", "You realize you miss everyone. Even Stradlater.", "Admit it", "Honest.", "Don't admit it", "Pride."),
], [
    ("end_school", "New School", "You go to the new school. You do, eventually, finish. You also, slowly, stop hating most people. You realize the phonies were, often, just scared like you."),
    ("end_writer", "Writer", "You become a writer in your twenties. You write a long careful book about a few days in December when you almost ran away. The book becomes a kind of mirror for decades of teenagers."),
    ("end_phoebe", "Phoebe", "You stay close to Phoebe for the rest of your life. She becomes a teacher. You become her brother in the way that matters. You are, in middle age, happy."),
])

HARRY_POTTER = linear_story({
    "id": "fb-harry-potter-1", "title": "Harry Potter and the Philosopher's Stone", "sourceTitle": "Harry Potter and the Philosopher's Stone",
    "kind": "book", "synopsis": "A cupboard under the stairs. A letter brought by owl. A platform between nines and tens. You're a wizard, Harry.",
    "releaseYear": 1997, "addedAt": "2026-02-24T00:00:00Z", "genre": "Fantasy",
    "tags": ["magic", "school", "friendship"], "rating": None, "loved": False,
}, [
    ("Letters", "Hundreds, in the chimney, in the kitchen, under the door.", "Read one", "Brave.", "Hide", "Wise."),
    ("Hagrid", "He breaks the door. He brings cake.", "Trust him", "Path.", "Stay back", "Wise."),
    ("Diagon Alley", "Wands, owls, gold. A vault, yours.", "Choose the snowy owl", "Heart.", "Browse longer", "Curious."),
    ("Wand", "The wand chooses you. Phoenix feather core.", "Take it", "Path.", "Try another", "Wise."),
    ("Train", "9 3/4. Ron in a compartment. Hermione asks if you've seen a toad.", "Befriend Ron", "Heart.", "Befriend Hermione", "Mind."),
    ("Sorting Hat", "Not Slytherin, you whisper. Gryffindor, the hat says.", "Whisper firmly", "Path.", "Don't whisper", "Honest."),
    ("Quidditch", "Madame Hooch, brooms. You catch a remembrall mid-air.", "Show off", "Joy.", "Stay calm", "Wise."),
    ("Troll", "Halloween. A troll. You and Ron save Hermione.", "Be brave", "Friend.", "Get a teacher", "Wise."),
    ("Mirror of Erised", "Parents in the mirror. Your hand on the glass.", "Sit a moment", "Honest.", "Walk away", "Wise."),
    ("Nicolas Flamel", "Hermione finds the name. The stone is real.", "Plan", "Path.", "Tell McGonagall", "Wise."),
    ("Norbert", "Hagrid's dragon. You sneak it out.", "Take the risk", "Friend.", "Convince him to send it on his own", "Smart."),
    ("Forbidden Forest", "Centaurs. A unicorn killed. A cloaked figure drinking.", "Stay close to the centaur", "Wise.", "Run", "Brave."),
    ("Snape's Curse", "Quidditch. Your broom shakes. Hermione sets a fire.", "Trust the team", "Friend.", "Solo", "Pride."),
    ("Through the Trapdoor", "Fluffy. Sing. Devil's snare. Keys.", "Take the lead", "Path.", "Trust Ron with the keys", "Friend."),
    ("Chess", "Ron's sacrifice on the board.", "Honor him", "Heart.", "Refuse to let him sacrifice", "Friend."),
    ("The Potions", "Hermione's logic. The right vial.", "Drink and go on", "Brave.", "Turn back", "Honest."),
    ("Mirror Again", "Quirrell with the turban. Voldemort under it.", "Refuse the stone", "Honor.", "Lie", "Smart."),
    ("Touch", "Your skin burns him.", "Hold", "Brave.", "Recoil", "Honest."),
    ("Hospital Wing", "Dumbledore at your bed. Cards.", "Ask questions", "Curious.", "Sleep", "Honest."),
    ("House Cup", "Last-minute points for bravery and friendship. Gryffindor wins.", "Cheer", "Joy.", "Be quiet", "Modest."),
    ("Platform", "Hedwig, trunk, Uncle Vernon's pinched face.", "Walk to him with confidence", "New.", "Be small", "Wise."),
], [
    ("end_year2", "Year Two", "You return next year for more. The lessons get harder. Hermione, somehow, also gets sharper. Ron, somehow, also."),
    ("end_friends", "The Three", "You and Ron and Hermione, for seven years, are inseparable. The friendship outlasts the school."),
    ("end_dumbledore", "Dumbledore's Lessons", "You realize, over years, that Dumbledore was setting you up to learn slowly. Some of it was kind. Some of it was, less so. You forgive him, mostly, late."),
])

HOBBIT = linear_story({
    "id": "fb-hobbit", "title": "The Hobbit", "sourceTitle": "The Hobbit",
    "kind": "book", "synopsis": "Bag End. A round door. Thirteen dwarves on your doorstep singing about gold. There and back again, the wizard says, like that's a small thing.",
    "releaseYear": 1937, "addedAt": "2026-02-23T00:00:00Z", "genre": "Fantasy",
    "tags": ["tolkien", "quest", "dwarves"], "rating": None, "loved": False,
    "nextStoryId": "fb-lotr",
}, [
    ("Bag End", "A cake of plenty. Doors knocking. Maps unrolled.", "Sign the contract", "Path.", "Refuse", "Quiet."),
    ("On the Road", "Ponies. Songs. Rain.", "Hum", "Joy.", "Sulk", "Honest."),
    ("Trolls", "Bert, Tom, William. A fire, a quarrel.", "Steal Bilbo's plan", "Cunning.", "Stand tall", "Brave."),
    ("Rivendell", "Elves. Sweet bread. Elrond reads the map.", "Listen carefully", "Wise.", "Sleep first", "Honest."),
    ("Goblin Tunnels", "Misty Mountains. A trapdoor. A song nobody asked for.", "Run", "Smart.", "Fight", "Brave."),
    ("Riddles", "A cave. A pool. Gollum.", "Riddle", "Wit.", "Stall", "Cunning."),
    ("Ring", "You pick up a ring. You don't tell anyone yet.", "Pocket it", "Smart.", "Show Gandalf", "Honest."),
    ("Eagles", "Trees on fire. Wargs and goblins below.", "Wait for the eagles", "Faith.", "Climb higher", "Honest."),
    ("Beorn", "A bear-man's hall. Cake. Bees the size of swallows.", "Be polite", "Civil.", "Be quiet", "Wise."),
    ("Mirkwood", "Don't leave the path. The river will make you sleep.", "Stay on path", "Discipline.", "Drink the water", "Foolish."),
    ("Spiders", "Webs. You name your sword Sting.", "Sing to lure them", "Cunning.", "Charge", "Brave."),
    ("Elf King's Dungeon", "Cells. Wine. A barrel in the river.", "Hide in the barrels", "Cunning.", "Talk to the king", "Honest."),
    ("Lake-town", "The Master, the bowman Bard, the dragon under the mountain.", "Trust Bard", "Wise.", "Trust the Master", "Foolish."),
    ("The Secret Door", "Map. Moon-letters. A keyhole.", "Wait for the day", "Patient.", "Force it", "Foolish."),
    ("Smaug", "Conversation, polite, with a dragon.", "Flatter him", "Cunning.", "Insult him", "Brave."),
    ("Bard's Arrow", "The black arrow. A missing scale.", "Send word to Bard", "Right.", "Don't", "Honest."),
    ("Arkenstone", "You find it. You keep it.", "Hide it", "Strategy.", "Give it to Thorin", "Honest."),
    ("Thorin's Madness", "Gold-sickness. The hall is too full of treasure to be a home.", "Try to talk him down", "Friend.", "Step back", "Wise."),
    ("Battle of Five Armies", "Goblins, wolves, men, elves, eagles. A hobbit hides behind a rock.", "Run a message", "Brave.", "Hide", "Honest."),
    ("Thorin Dying", "A handshake. A goodbye. A small forgiveness.", "Sit with him", "Honor.", "Stand by Gandalf", "Honest."),
    ("Bag End, Again", "The auction is canceled. Your spoons are mostly accounted for.", "Settle back in", "Quiet.", "Plan another trip", "Spirit."),
], [
    ("end_quiet", "Quiet at Bag End", "You stay home. You write down the journey. Years later your nephew Frodo, reading the book, asks if it's all true. You say, mostly."),
    ("end_writer", "Writer of Tales", "You become, in Hobbiton, a quiet author. Children come and ask about the ring. You smile and change the subject."),
    ("end_ring", "The Ring, Pocketed", "You keep the ring in your waistcoat. You don't, for many years, look at it. You forget, mostly. It does not, you'll learn later, forget you."),
])

LOTR_BOOK = linear_story({
    "id": "fb-lotr", "title": "The Lord of the Rings", "sourceTitle": "The Lord of the Rings",
    "kind": "book", "synopsis": "Bag End, again. Bilbo's gift is, you'll learn, a curse. The road goes ever on, and you are walking it on small hairy feet.",
    "releaseYear": 1954, "addedAt": "2026-02-22T00:00:00Z", "genre": "Fantasy",
    "tags": ["tolkien", "ring", "epic"], "rating": None, "loved": False,
}, [
    ("The Party", "Eleventy-first. Fireworks. Bilbo vanishes.", "Notice", "Wise.", "Wave", "Joy."),
    ("The Letter", "Gandalf returns with a fireplace and runes.", "Listen", "Wise.", "Argue", "Honest."),
    ("Leaving", "Sam, Pippin, Merry.", "Take the Old Forest path", "Brave.", "The road", "Direct."),
    ("Bree", "Strider in a corner.", "Trust", "Wise.", "Hesitate", "Honest."),
    ("Weathertop", "Five blades in the dark.", "Resist the ring", "Discipline.", "Put it on", "Honest."),
    ("Rivendell", "Council. Volunteers. The Fellowship.", "Volunteer", "Path.", "Stay silent", "Honest."),
    ("Moria", "Drums. The bridge. Gandalf falls.", "Run", "Survive.", "Try to help", "Honor."),
    ("Lorien", "Galadriel. Lembas. Gifts.", "Refuse her ring", "Vow.", "Almost take it", "Honest."),
    ("Amon Hen", "Boromir's hand reaches.", "Run", "Save the ring.", "Hold him off", "Brave."),
    ("Sam in the Water", "He swims. You pull him in.", "Take him", "Friend.", "Refuse", "Vow."),
    ("Gollum", "He swears on the precious.", "Trust slowly", "Path.", "Don't trust", "Wise."),
    ("Faramir", "He could take the ring. He doesn't.", "Honor him", "Heart.", "Note his restraint", "Wise."),
    ("Shelob", "A spider in a cave.", "Sting her", "Brave.", "Run", "Smart."),
    ("Sam Carries You", "You are limp. Sam shoulders the load.", "Trust him", "Friend.", "Mumble", "Honest."),
    ("Mount Doom", "The stairs. The heat. The crack.", "Refuse to drop it", "Honest.", "Drop it", "Lie."),
    ("Gollum Bites", "He takes the ring and falls in.", "Watch", "Witness.", "Hold Sam", "Friend."),
    ("Eagles", "You wake on a soft thing. Light. Gandalf.", "Smile", "Honest.", "Sleep", "Honest."),
    ("Gondor's Crown", "Aragorn is king. He kneels to the hobbits.", "Stand tall", "Honor.", "Be embarrassed", "Honest."),
    ("Scouring the Shire", "Home is troubled. You fix it.", "Lead quietly", "Honor.", "Let others lead", "Modest."),
    ("Bag End, Again", "Sam at the door. A daughter on his knee.", "Be content", "Honor.", "Be restless", "Honest."),
    ("Grey Havens", "A ship. Bilbo, Gandalf, the Elves.", "Sail", "Path.", "Stay", "Heart."),
], [
    ("end_havens", "The Grey Havens", "You sail. The light is kind. Sam, on the dock, raises a hand. You wave back. The sea is, finally, soft."),
    ("end_shire", "Master of Bag End", "Sam returns and is, for many years, the mayor. You write the book. The book becomes, eventually, a kind of national story."),
    ("end_legacy", "The Book", "Generations read the Red Book of Westmarch. Your handwriting is, in places, smudged. Children copy the smudges, lovingly."),
])

SPECS += [CASABLANCA, PRIDE_PREJUDICE, NINETEEN_EIGHTY_FOUR, MOCKINGBIRD, GATSBY, CATCHER_RYE, HARRY_POTTER, HOBBIT, LOTR_BOOK]

CRIME_PUNISHMENT = linear_story({
    "id": "fb-crime-punishment", "title": "Crime and Punishment", "sourceTitle": "Crime and Punishment",
    "kind": "book", "synopsis": "St. Petersburg, summer. You are a starving student. You think, very seriously, that some men are above the law. You decide to test the theory on a pawnbroker.",
    "releaseYear": 1866, "addedAt": "2026-02-21T00:00:00Z", "genre": "Drama",
    "tags": ["dostoevsky", "guilt", "russia"], "rating": None, "loved": False,
}, [
    ("The Garret", "A coffin of a room. Heat. Debts. You write a strange article on theory.", "Re-read your article", "Path.", "Burn it", "Wise."),
    ("The Pawnbroker", "Alyona, mean, alone. You pawn a watch.", "Note her routine", "Cold.", "Hesitate", "Honest."),
    ("Marmeladov", "A drunk in a tavern. Sonia, his daughter, doing what she has to.", "Drink with him", "Compassion.", "Walk out", "Cold."),
    ("Letter from Mother", "Dunya, your sister, is engaged to a man who is, plainly, a creditor.", "Refuse the help", "Pride.", "Accept", "Practical."),
    ("Decision", "You bring the axe under your coat.", "Go", "Path.", "Don't", "Honest."),
    ("The Door", "She opens it. The room is small. You strike.", "Strike", "Path.", "Run", "Wise."),
    ("Lizaveta", "Her sister returns. You strike again.", "Mourn instantly", "Honest.", "Don't think", "Survive."),
    ("Escape", "The hallway. Footsteps. You hide behind an empty door.", "Hide", "Smart.", "Run", "Brave."),
    ("Home", "You sleep for days, fevered. The blood on your sock.", "Burn the sock", "Smart.", "Hide it", "Honest."),
    ("Razumikhin", "Your friend. He nurses you.", "Tell him part", "Honest.", "Tell him nothing", "Pride."),
    ("Porfiry", "The investigator. He smiles. He talks of theory.", "Speak carefully", "Smart.", "Confess", "Honest."),
    ("Sonia's Room", "You meet her. You read Lazarus together.", "Confess to her", "Honest.", "Don't yet", "Pride."),
    ("Sonia's Words", "She tells you to kiss the earth at the crossroads and confess.", "Promise", "Path.", "Walk away", "Pride."),
    ("Svidrigailov", "He arrives. He has, you fear, your worst self in him.", "Avoid him", "Wise.", "Talk to him", "Curious."),
    ("Dunya's Visit", "He corners your sister. She holds a pistol.", "Trust she'll do what's needed", "Honor.", "Intervene", "Brother."),
    ("Svidrigailov's End", "He shoots himself in the morning.", "Note it", "Honest.", "Don't note", "Survive."),
    ("Goodbye to Mother", "You hold her face. You don't tell her.", "Be gentle", "Care.", "Be cold", "Pride."),
    ("Crossroads", "You kiss the earth. People stare.", "Kneel", "Honor.", "Pretend it was drunken", "Pride."),
    ("Police Station", "You confess.", "Tell it clean", "Honor.", "Tell it half", "Pride."),
    ("Siberia", "Eight years. A wide river. Sonia, who came with you, lives in a hut nearby.", "Read the New Testament she gave you", "Path.", "Hold out", "Pride."),
    ("Resurrection", "Spring on the riverbank. You realize you love her.", "Take her hand", "Path.", "Sit alone", "Pride."),
], [
    ("end_resurrection", "Resurrection", "You serve your sentence. You return, eventually, with Sonia. You become, the rest of your life, a quiet man who teaches mathematics in a small town and means it when he says 'good morning.'"),
    ("end_writer", "A Different Article", "You write a different article in the prison, on conscience instead of theory. It is, when smuggled out, debated for a century."),
    ("end_silence", "Silence", "You serve your time and disappear into a Siberian village. You die there old. Sonia is buried beside you. The villagers, who never knew, called you a kind man."),
])

WAR_PEACE = linear_story({
    "id": "fb-war-peace", "title": "War and Peace", "sourceTitle": "War and Peace",
    "kind": "book", "synopsis": "Russia, 1805. Drawing rooms and battlefields, both crowded. You are Pierre, an awkward heir who has, somehow, just inherited the largest fortune in the empire.",
    "releaseYear": 1869, "addedAt": "2026-02-20T00:00:00Z", "genre": "Drama",
    "tags": ["tolstoy", "russia", "epic"], "rating": None, "loved": False,
}, [
    ("Anna Pavlovna's Salon", "Glittering nonsense. You speak Napoleon's name too warmly.", "Be honest", "Spirit.", "Apologize", "Civil."),
    ("Father's Death", "You inherit everything. Strangers smile at you now.", "Take stock", "Wise.", "Throw a party", "Honest."),
    ("Marriage", "Helene's family arranges. You drift into it.", "Refuse", "Wise.", "Marry her", "Path."),
    ("Andrei", "Your friend leaves for war. He is, in salons, suffocating.", "Toast him", "Friend.", "Argue with him", "Honest."),
    ("Austerlitz", "Andrei watches the sky above the field. The campaign collapses.", "Receive his letter", "Honor.", "Wait for him", "Patient."),
    ("Freemasons", "A lodge. A teacher. You begin to read.", "Take it seriously", "Path.", "Take it lightly", "Honest."),
    ("Natasha at the Ball", "She, sixteen, dances with Andrei. The world tilts for him.", "Be glad for them", "Honor.", "Be quiet", "Honest."),
    ("Anatole", "Helene's brother schemes for Natasha. He is, plainly, a cad.", "Warn her", "Honor.", "Intervene with Anatole directly", "Brave."),
    ("Borodino", "A field of cannon and smoke. You wander into it as an observer.", "Stay calm", "Honor.", "Run", "Honest."),
    ("Moscow", "Fires across the city. The French enter. You stay.", "Try to assassinate Napoleon", "Honest.", "Help the wounded", "Care."),
    ("Captured", "You are taken. Platon Karataev becomes, oddly, your teacher.", "Listen to Platon", "Wise.", "Plan escape", "Spirit."),
    ("March", "Platon dies on the road. The French retreat is slow.", "Bury his memory", "Honor.", "Walk on", "Survive."),
    ("Freed", "Russian cossacks. Soup. Sleep on straw.", "Eat slowly", "Honest.", "Sleep", "Honest."),
    ("Andrei, Wounded", "He is found. He is, dying, kinder than he was.", "Sit with him", "Honor.", "Stay back", "Honor."),
    ("Helene Dies", "She dies, probably by her own carelessness with medicine.", "Mourn correctly", "Society.", "Be honest with yourself", "Truth."),
    ("Natasha, Quiet", "She nursed Andrei. She is older. You speak as adults.", "Be honest", "Path.", "Be careful", "Patient."),
    ("Proposal", "You write her a letter. The answer comes quickly.", "Take her seriously", "Honor.", "Be flippant", "Foolish."),
    ("Marya", "Nikolai marries Marya. The two estates merge.", "Be a good brother-in-law", "Family.", "Stay distant", "Honest."),
    ("Family Life", "Children. Quiet rooms. A book in your hand at dinner.", "Be a present father", "Honor.", "Be a distracted one", "Honest."),
    ("Pierre's Thought", "You decide, slowly, that history is the work of millions and not Napoleons.", "Write it down", "Path.", "Live it", "Honest."),
    ("A Smaller Life", "You stop trying to find one big answer. You find many small ones, with Natasha.", "Sit on the porch", "Quiet.", "Plan more reforms", "Spirit."),
], [
    ("end_family", "Family Life", "You live forty quiet years with Natasha. The estate is, by your death, generous to its people. Your children write a small book about you. The book is, mostly, recipes."),
    ("end_philosopher", "A Quiet Philosopher", "You write a long, kind essay on the way history actually happens. It is, by your grandchildren's time, a textbook in one Russian university."),
    ("end_war", "Another War", "You live to see another war from a chair by a window. You have, by then, learned not to be surprised. You take Natasha's hand and ask her, again, to read to you."),
])

ANNA_KARENINA = linear_story({
    "id": "fb-anna-karenina", "title": "Anna Karenina", "sourceTitle": "Anna Karenina",
    "kind": "book", "synopsis": "Imperial Russia. All happy families are alike; each unhappy family is unhappy in its own way. You're about to make a new way.",
    "releaseYear": 1877, "addedAt": "2026-02-19T00:00:00Z", "genre": "Drama",
    "tags": ["tolstoy", "love", "society"], "rating": None, "loved": False,
}, [
    ("Moscow Station", "You arrive to help your brother's marriage. A man dies under the train.", "Note the omen", "Honest.", "Disregard", "Survive."),
    ("Vronsky", "He sees you and you see him. The room rearranges.", "Withdraw", "Wise.", "Stay", "Honest."),
    ("Karenin", "Your husband, kind in a clerk's way, asks about your trip.", "Tell him plainly", "Honor.", "Withhold", "Honest."),
    ("Ball", "Kitty wears white. You wear black. Vronsky chooses badly.", "Leave early", "Wise.", "Dance", "Honest."),
    ("St. Petersburg", "Your son is at the door. Seryozha hugs you.", "Hold him long", "Mother.", "Set him down quickly", "Survive."),
    ("Races", "Vronsky's horse falls. You scream his name.", "Recover the scream", "Society.", "Don't recover", "Honest."),
    ("Karenin's Offer", "He gives you a choice — be a wife, or be cut off entirely.", "Lie", "Survive.", "Tell the truth", "Honor."),
    ("Italy", "Vronsky and you, abroad. He paints. You are, for a month, free.", "Stay months", "Heart.", "Plan a return", "Patient."),
    ("Annie", "Your daughter. You do not love her the same way.", "Try", "Honor.", "Don't try", "Honest."),
    ("Return to Russia", "Society has, in your absence, decided.", "Visit Seryozha", "Mother.", "Avoid Seryozha", "Wise."),
    ("Seryozha", "He cries against your dress. You can't, by law, take him.", "Vow to find a way", "Mother.", "Pray", "Wise."),
    ("Salon", "A countess cuts you publicly.", "Hold your shoulders", "Brave.", "Leave", "Wise."),
    ("Levin's Wedding", "Off-page, your brother-in-law marries. The country is, briefly, happy.", "Send a gift", "Civil.", "Be still", "Honest."),
    ("Jealousy", "You begin to read Vronsky's mail.", "Stop", "Wise.", "Continue", "Honest."),
    ("Morphine", "You take more, then more.", "Cut back", "Wise.", "Take more", "Honest."),
    ("Quarrel", "He goes to Moscow. He writes a vague letter.", "Send a sharp one", "Pride.", "Send a soft one", "Honest."),
    ("Train Station, Again", "You ride into town to find him.", "Wait at the station for the next train", "Honest.", "Take a cab", "Wise."),
    ("Platform", "Faces blur. The bell. Your shawl is heavy.", "Step back", "Save.", "Step forward", "Honest."),
    ("Bookend", "A man dies under the train. You can choose another ending.", "Choose another", "Save.", "Step", "Honest."),
    ("After", "If you stepped back, you sit on a bench with shaking hands.", "Go home", "Survive.", "Leave Vronsky", "Path."),
    ("Levin's Field", "Far away, your brother-in-law in a hayfield finds peace. He thinks of you, sometimes.", "Send him a letter", "Honor.", "Don't send", "Honest."),
], [
    ("end_step", "The Bell", "You step. The book closes on you. Vronsky goes to a war and dies. Karenin raises Seryozha and Annie. Years pass."),
    ("end_step_back", "Step Back", "You step back. You move, alone, to Italy. You raise Annie in a small house. You read, late, that Vronsky has, in Serbia, found a war."),
    ("end_levin", "Levin's Field", "Levin's chapter outlives yours. He raises his children. He thinks of you in a hayfield, every year, when the light is right. You exist, in him, as a small daily prayer."),
])

MOBY_DICK = linear_story({
    "id": "fb-moby-dick", "title": "Moby-Dick", "sourceTitle": "Moby-Dick",
    "kind": "book", "synopsis": "Call me Ishmael. New Bedford. Nantucket. The Pequod. A captain with a leg of bone and a grudge as big as the ocean.",
    "releaseYear": 1851, "addedAt": "2026-02-18T00:00:00Z", "genre": "Drama",
    "tags": ["whaling", "sea", "obsession"], "rating": None, "loved": False,
}, [
    ("Spouter-Inn", "You share a bed with Queequeg, harpooner.", "Befriend him", "Friend.", "Be wary", "Honest."),
    ("Sermon", "Father Mapple in the pulpit. Jonah.", "Note it", "Wise.", "Don't note", "Honest."),
    ("Sign On", "The Pequod. Captain Peleg pays you in lays.", "Negotiate", "Wise.", "Take what's offered", "Honest."),
    ("Ahab", "He appears on deck. Bone leg. Scar from forehead to coat.", "Read the room", "Wise.", "Approach him", "Brave."),
    ("Doubloon", "A coin nailed to the mast. To whoever sights the white whale.", "Look up often", "Path.", "Forget it", "Honest."),
    ("Starbuck", "First mate. He warns Ahab in private.", "Side with Starbuck", "Wise.", "Stay quiet", "Honest."),
    ("Squid", "A great squid surfaces. Bad omen.", "Note it", "Honest.", "Don't speak it", "Wise."),
    ("First Lower", "Queequeg in the bow. The boat hauls.", "Hold tight", "Brave.", "Steady your nerves", "Wise."),
    ("Whales", "A small school. You take one.", "Trust the technique", "Honor.", "Doubt", "Honest."),
    ("Try-Works", "Boiling blubber, midnight, fire.", "Tend the fire", "Discipline.", "Watch the sea", "Wise."),
    ("Pip Lost", "The cabin boy is left in the sea. They retrieve him changed.", "Sit with him", "Care.", "Avoid him", "Honest."),
    ("Ahab's Map", "He plots whale migrations on a chart.", "Note his certainty", "Wise.", "Be impressed", "Honest."),
    ("Forge", "He forges a harpoon, tempered in blood.", "Watch silently", "Honor.", "Object", "Brave."),
    ("Rachel", "Another ship asks for help finding a captain's son. Ahab refuses.", "Argue", "Honor.", "Stay silent", "Honest."),
    ("Storm", "Lightning down the masts. St. Elmo's fire.", "Trust the spar", "Wise.", "Pray", "Honest."),
    ("Ahab's Vow", "He nails his quadrant. He throws away time.", "Note it", "Wise.", "Don't note", "Honest."),
    ("First Sight", "A spout on the horizon. White.", "Lower boats", "Path.", "Plead", "Brave."),
    ("Day One", "Ahab's boat is smashed.", "Pull Ahab from the water", "Honor.", "Save your boat", "Survive."),
    ("Day Two", "Fedallah is dragged under. The harpoons miss.", "Persuade Ahab to turn", "Wise.", "Stay silent", "Honest."),
    ("Day Three", "The Pequod is rammed. The whale rolls.", "Cling to the coffin", "Save.", "Help others", "Honor."),
    ("Sea, Alone", "Queequeg's coffin floats up. You climb on. Days pass.", "Wait", "Save.", "Pray", "Honest."),
], [
    ("end_rachel", "The Rachel", "The Rachel finds you, searching for her own lost. You ride home with her crew. You write the book down, in time, in a small room in Brooklyn."),
    ("end_writer", "Call Me Ishmael", "You become a sailor and a teacher of sailors. You write a book that nobody reads in your lifetime. A century later they read it everywhere."),
    ("end_shore", "Quiet Shore", "You stay on land. You learn a trade. You marry a woman who has never been to sea. Every July you walk to a pier and stand for an hour. You do not, by then, fully know why."),
])

ODYSSEY = linear_story({
    "id": "fb-odyssey", "title": "The Odyssey", "sourceTitle": "The Odyssey",
    "kind": "book", "synopsis": "Ten years home from Troy. You are Odysseus. The sea has, against all reason, opinions. Penelope weaves and unweaves and waits.",
    "releaseYear": -700, "addedAt": "2026-02-17T00:00:00Z", "genre": "Fantasy",
    "tags": ["greek", "epic", "journey"], "rating": None, "loved": False,
}, [
    ("Troy Falls", "The horse, the gates, the smoke.", "Spare a survivor", "Mercy.", "Press on", "Soldier."),
    ("Lotus Eaters", "A drug that erases home.", "Drag the men back", "Captain.", "Stay yourself", "Wise."),
    ("Cyclops", "Polyphemus. Sheep. A cave.", "Tell him your name is Nobody", "Cunning.", "Boast your name", "Pride."),
    ("Aeolus", "He gives you the bag of winds.", "Sleep with the bag tight", "Wise.", "Trust the crew", "Foolish."),
    ("The Crew Open the Bag", "Winds escape. You are blown back.", "Forgive them", "Honor.", "Curse them", "Anger."),
    ("Laestrygonians", "Giants throw rocks. Ships are crushed.", "Cut and run", "Save.", "Stand and fight", "Foolish."),
    ("Circe", "Pigs. A drink. A goddess.", "Take Hermes' moly", "Wise.", "Drink unprotected", "Foolish."),
    ("A Year on Circe's Island", "Comfort. The crew softens.", "Sleep a year", "Honest.", "Leave sooner", "Discipline."),
    ("Underworld", "Tiresias' prophecy. Your mother as a shade.", "Hold the trench", "Discipline.", "Lunge at her", "Heart."),
    ("Sirens", "Wax in their ears. Ropes on your mast.", "Bind tight", "Wise.", "Loose enough to listen", "Curious."),
    ("Scylla and Charybdis", "Choose six lives or all.", "Take Scylla's side", "Cold math.", "Take Charybdis", "Foolish."),
    ("Helios' Cattle", "Don't eat them. The crew, hungry, does.", "Stop them", "Discipline.", "Let them", "Tired."),
    ("Shipwreck", "Zeus' bolt. You alone live.", "Cling to the keel", "Survive.", "Swim", "Honest."),
    ("Calypso", "Seven years on her island.", "Refuse her gift", "Honor.", "Stay", "Honest."),
    ("Phaeacians", "Their ship returns you to Ithaca, asleep.", "Thank them", "Honor.", "Forget them", "Tired."),
    ("Beggar's Rags", "Athena disguises you.", "Walk to the swineherd", "Wise.", "Walk to the palace", "Foolish."),
    ("Telemachus", "Your son meets you. You weep.", "Tell him plainly", "Honor.", "Plan first", "Wise."),
    ("Bow Contest", "Penelope's bow. Suitors fail.", "String it slowly", "Wise.", "String it fast", "Pride."),
    ("Slaughter", "Arrows through the hall.", "Spare the bard", "Mercy.", "Spare none", "Soldier."),
    ("Olive-Tree Bed", "Penelope tests you with a bed only you can know.", "Tell her the truth of the bed", "Honor.", "Be angry", "Pride."),
    ("Laertes", "Your father in the orchard.", "Embrace him", "Heart.", "Wait for proof", "Wise."),
], [
    ("end_home", "Home", "You rule Ithaca again. Penelope at your side. Telemachus learns. You die old, in bed, with the sea in the distance."),
    ("end_sea", "The Sea, Again", "Tiresias' prophecy comes due. You take an oar inland until a stranger calls it a winnowing fan. You die a peaceful death far from the water."),
    ("end_song", "The Song", "Demodocus and others sing your story. You become, eventually, a poem instead of a man. The poem outlives every kingdom you fought in or for."),
])

HAMLET = linear_story({
    "id": "fb-hamlet", "title": "Hamlet", "sourceTitle": "Hamlet",
    "kind": "book", "synopsis": "Elsinore, winter. Your father is dead. Your uncle is on the throne and in your mother's bed. A ghost is on the battlement and wants a word.",
    "releaseYear": 1603, "addedAt": "2026-02-16T00:00:00Z", "genre": "Drama",
    "tags": ["shakespeare", "revenge", "tragedy"], "rating": None, "loved": False,
}, [
    ("Battlement", "Horatio brings you to see the ghost.", "Speak to it", "Brave.", "Watch", "Wise."),
    ("Father's Charge", "Murdered by Claudius. Revenge me.", "Vow", "Path.", "Doubt", "Wise."),
    ("Antic Disposition", "You play mad to buy time.", "Play it well", "Cunning.", "Play it badly", "Honest."),
    ("Ophelia", "You are cruel to her in the gallery.", "Apologize later", "Honor.", "Don't apologize", "Cold."),
    ("Polonius", "He hides behind tapestries to spy.", "Sense him there", "Wise.", "Walk past", "Honest."),
    ("Players", "A troupe arrives. You write them new lines.", "Test the king", "Cunning.", "Don't test", "Foolish."),
    ("The Play", "Claudius rises and walks out, pale.", "Mark his guilt", "Wise.", "Tell only Horatio", "Smart."),
    ("Prayer", "You find Claudius praying.", "Strike", "Path.", "Wait", "Pride."),
    ("Mother's Room", "You confront Gertrude. A noise behind the arras.", "Stab", "Anger.", "Reveal", "Wise."),
    ("Polonius Dead", "It was Polonius. Ophelia's father.", "Mourn", "Honor.", "Hide him", "Cold."),
    ("Sent to England", "Rosencrantz and Guildenstern carry sealed orders.", "Switch the letter", "Cunning.", "Trust the friends", "Naive."),
    ("Pirates", "A skirmish. You return alone.", "Send word ahead", "Smart.", "Surprise the court", "Brave."),
    ("Yorick", "A gravedigger holds a skull.", "Remember Yorick", "Honor.", "Move on", "Honest."),
    ("Ophelia's Funeral", "She is in the ground. Laertes leaps in.", "Leap in too", "Heart.", "Stand back", "Wise."),
    ("Laertes's Plot", "He sharpens a foil. He dips it in poison.", "Suspect", "Wise.", "Trust the duel", "Naive."),
    ("Osric", "A foolish courtier brings the challenge.", "Mock him", "Wit.", "Accept", "Honor."),
    ("Duel", "Touch. Touch. A scratch with the wrong foil.", "Switch", "Wise.", "Don't", "Honest."),
    ("Cup", "Your mother drinks from the poisoned cup.", "Stop her", "Mother.", "Don't", "Honest."),
    ("Stab the King", "You finally do it.", "Pour the cup down his throat", "Path.", "Just the blade", "Honor."),
    ("The Rest is Silence", "Horatio raises the cup. You stop him.", "Hold him", "Honor.", "Let him go", "Honest."),
    ("Fortinbras", "He arrives. He takes the kingdom. Horatio begins to speak.", "Have Horatio tell the truth", "Honor.", "Have him spare the worst", "Civil."),
], [
    ("end_silence", "The Rest is Silence", "You die, peacefully enough, with Horatio's hand on your shoulder. The kingdom passes to a foreigner. The story passes to a friend."),
    ("end_words", "Words, Words, Words", "You survive, somehow, the scratch. You abdicate. You go to Wittenberg as a tutor. You write down, with Horatio, the play exactly. It survives every revision."),
    ("end_horatio", "Horatio's Witness", "Horatio tells the story. He tells it carefully. He tells it for as long as he lives. The court that came after, slowly, hears it true."),
])

FRANKENSTEIN = linear_story({
    "id": "fb-frankenstein", "title": "Frankenstein", "sourceTitle": "Frankenstein",
    "kind": "book", "synopsis": "Ingolstadt. You are a brilliant student. You have figured out, alone in a garret, how to give life. You have not figured out what to do with what you make.",
    "releaseYear": 1818, "addedAt": "2026-02-15T00:00:00Z", "genre": "Horror",
    "tags": ["shelley", "creation", "guilt"], "rating": None, "loved": False,
}, [
    ("Garret", "Hands sewn, bones aligned. The kit before the storm.", "Continue", "Path.", "Stop", "Wise."),
    ("Spark", "He opens his eyes.", "Stay", "Honor.", "Flee", "Honest."),
    ("Fever", "You collapse. Henry Clerval nurses you for weeks.", "Tell him", "Honor.", "Don't tell him", "Pride."),
    ("Letter from Home", "William, your little brother, is dead. Justine is accused.", "Defend Justine", "Honor.", "Be silent", "Pride."),
    ("Justine Hangs", "You watch her hang for what you made.", "Confess after", "Honor.", "Stay silent", "Cowardice."),
    ("Mer de Glace", "You meet him on a glacier. He talks.", "Listen", "Honor.", "Refuse", "Pride."),
    ("De Lacey Family", "He tells you how he learned language from a cottage.", "Believe him", "Honest.", "Doubt", "Pride."),
    ("Demand", "He asks for a mate. A she-creature.", "Promise", "Path.", "Refuse", "Brave."),
    ("Scotland", "An island. A second body, half-made.", "Finish", "Vow.", "Destroy it", "Honor."),
    ("Destroy It", "He watches from a window. He vows revenge.", "Run", "Survive.", "Confront", "Brave."),
    ("Henry, Murdered", "Clerval, your dearest friend, on a beach.", "Confess to the magistrate", "Honor.", "Stay silent", "Pride."),
    ("Wedding Night", "You marry Elizabeth. You sleep, foolishly, in another room.", "Watch her", "Wise.", "Trust the night", "Foolish."),
    ("Scream", "He has taken her too.", "Vow", "Path.", "Mourn", "Honest."),
    ("Father, Broken", "Your father dies of grief.", "Sit with him", "Honor.", "Set out", "Vow."),
    ("Arctic", "Sleds, dogs, ice forever.", "Pursue", "Vow.", "Turn back", "Wise."),
    ("Walton's Ship", "Captain Walton finds you on the ice.", "Tell him your story", "Honor.", "Refuse", "Pride."),
    ("Dying", "You ask Walton to finish what you started.", "Ask him to spare himself", "Honor.", "Ask him to kill the creature", "Anger."),
    ("Bed", "You die.", "Hold his hand", "Honest.", "Look at the window", "Honest."),
    ("The Creature Arrives", "He weeps over your body. He tells Walton his side.", "Hear him through Walton", "Honest.", "Stay still", "Honor."),
    ("The Pyre", "He says he will burn himself. He leaves on a raft of ice.", "Believe him", "Honest.", "Doubt him", "Wise."),
    ("Walton's Letter", "Walton writes home. The ship turns south.", "Approve his turning", "Honor.", "Wish him on", "Foolish."),
], [
    ("end_pyre", "The Pyre", "He burns himself in the dark. Walton's ship turns home. You are buried at sea, or in ice, or in a story that gets told."),
    ("end_walton", "Walton's Letter", "Walton writes the story honestly. The letter, eventually, becomes the book. Sisters read it by lamps. Generations read it after."),
    ("end_creature", "The Creature, Lost", "Some say he lives still, on a far island, with cold seas around him. He writes, slowly, on stones, with charcoal. He is, in his way, also an author."),
])

DRACULA = linear_story({
    "id": "fb-dracula", "title": "Dracula", "sourceTitle": "Dracula",
    "kind": "book", "synopsis": "London by mail coach. A solicitor's clerk goes to Transylvania for a real estate sale. The count, you'll find, casts no reflection.",
    "releaseYear": 1897, "addedAt": "2026-02-14T00:00:00Z", "genre": "Horror",
    "tags": ["vampire", "victorian", "letters"], "rating": None, "loved": False,
}, [
    ("Borgo Pass", "A coach. A wolf. A driver with red eyes.", "Stay calm", "Wise.", "Run", "Foolish."),
    ("Castle", "Tall doors. No servants.", "Be polite", "Civil.", "Look for an exit", "Wise."),
    ("Mirror Shave", "He stands behind you and there is no reflection.", "Note it", "Wise.", "Don't note", "Honest."),
    ("Three Sisters", "Pale women lean over you.", "Pray", "Honor.", "Run", "Honest."),
    ("Letters", "Mina, in England, writes you cheerfully.", "Reply carefully", "Care.", "Don't reply", "Survive."),
    ("Whitby", "A storm, a ship, a black dog ashore.", "Mark it", "Wise.", "Don't mark", "Honest."),
    ("Lucy", "She begins to sleepwalk. Her neck shows two marks.", "Bring Van Helsing", "Wise.", "Wait", "Foolish."),
    ("Garlic", "Garlic at the window. Stolen by the maid.", "Repeat the cure", "Discipline.", "Move on", "Foolish."),
    ("Lucy Dies", "Long fight. Bright tools.", "Mourn", "Honor.", "Vow", "Path."),
    ("Lucy Undead", "She walks the cemetery. Children disappear and return weak.", "End it", "Honor.", "Don't", "Honest."),
    ("Mina", "She holds the diaries together. She types them out.", "Trust her", "Path.", "Hide things from her", "Foolish."),
    ("Renfield", "He speaks of his Master.", "Listen", "Honest.", "Don't listen", "Foolish."),
    ("The Boxes", "Fifty boxes of earth from the castle.", "Track them", "Smart.", "Don't track", "Foolish."),
    ("Mina Bitten", "He came in the night.", "Bring her into the planning fully", "Trust.", "Hide it from her", "Foolish."),
    ("Wafer", "The Host burns her forehead.", "Vow she will be cleansed", "Honor.", "Despair", "Foolish."),
    ("Box Hunt", "Sterilize the boxes one by one.", "Be thorough", "Discipline.", "Be fast", "Honest."),
    ("Train Across Europe", "He flees. You follow.", "Coordinate", "Smart.", "Race", "Brave."),
    ("Carpathian Pass", "Snow. Gypsies. A cart with the last box.", "Cut off the cart", "Smart.", "Approach openly", "Brave."),
    ("Sunset", "Knives. Bowie. The box opens.", "Strike at the throat", "Path.", "Strike at the heart", "Path."),
    ("Mina's Forehead", "The mark fades.", "Hold her", "Heart.", "Pray", "Honor."),
    ("Years Later", "A small boy with three names. A trip to Transylvania.", "Tell him the truth", "Honor.", "Don't tell him", "Wise."),
], [
    ("end_record", "The Record", "Mina compiles every letter and journal into a single bound book. The book outlives every member of the band of light."),
    ("end_quiet", "Quiet Years", "You marry. You have a son. You die old in England. The castle, by then, is a ruin and a rumor."),
    ("end_castle", "The Castle, Empty", "Years later you return alone. The villagers cross themselves. You sit in the great hall. You do not, you decide, want anything except to leave again."),
])

BELOVED = linear_story({
    "id": "fb-beloved", "title": "Beloved", "sourceTitle": "Beloved",
    "kind": "book", "synopsis": "Ohio, after the war. 124 is haunted. Your past walks up the road one day and sits on the porch and asks for water.",
    "releaseYear": 1987, "addedAt": "2026-02-13T00:00:00Z", "genre": "Drama",
    "tags": ["morrison", "memory", "freedom"], "rating": None, "loved": False,
}, [
    ("124", "The house is, as the town says, spiteful.", "Stay", "Vow.", "Move", "Honest."),
    ("Paul D Arrives", "An old friend from Sweet Home. He carries a tin tobacco box for a heart.", "Welcome him", "Heart.", "Be wary", "Honest."),
    ("Stove", "He drives the ghost out for an evening.", "Be grateful", "Honest.", "Be careful", "Wise."),
    ("Carnival", "The three of you walk back from the fair. A young woman is on the steps.", "Take her in", "Heart.", "Send her on", "Wise."),
    ("Beloved", "Her name. The name on a stone.", "Recognize it", "Honest.", "Pretend not to", "Honest."),
    ("Memory of Halle", "Paul D remembers the milk and the men.", "Tell him you remember too", "Honor.", "Don't say it", "Survive."),
    ("Schoolteacher", "He came to take Sethe back. She made her choice.", "Speak it aloud", "Honor.", "Hide it", "Survive."),
    ("Denver", "Your daughter, eighteen, watches everything.", "Listen to her", "Care.", "Push her aside", "Honest."),
    ("Paul D Leaves", "He cannot stay after he knows.", "Let him go", "Honor.", "Beg", "Honest."),
    ("Beloved, Greedy", "She wants more than you can give.", "Set a limit", "Wise.", "Give more", "Honest."),
    ("Stamp Paid", "He brings food. He watches the porch.", "Trust him", "Friend.", "Refuse", "Pride."),
    ("Denver Walks Out", "She leaves the porch for the first time in years.", "Notice", "Honor.", "Don't notice", "Survive."),
    ("Lady Jones", "Denver studies again. She is, slowly, a woman.", "Be proud", "Mother.", "Be jealous", "Honest."),
    ("The Town's Women", "They begin to bring food to the porch.", "Open the door", "Honor.", "Don't", "Pride."),
    ("Singing", "Thirty women sing the spirit out.", "Step out with them", "Honor.", "Stay in", "Honest."),
    ("Mr. Bodwin", "He arrives in a wagon. You see, briefly, Schoolteacher.", "Move toward him with the ice pick", "Honest.", "Stop yourself", "Wise."),
    ("Stopped", "Denver and the women stop you. Beloved vanishes.", "Sit down", "Heal.", "Stand again", "Honor."),
    ("Paul D Returns", "He sits with you. He says you are your own best thing.", "Believe him", "Heal.", "Almost", "Honest."),
    ("Denver, Working", "She has a job. She walks home in the evening.", "Eat together", "Care.", "Sit on the porch", "Quiet."),
    ("Letters", "The town sends letters of half-apology and half-curiosity.", "Read them", "Honor.", "Burn them", "Wise."),
    ("The Story Will Not Pass On", "And yet, you decide to set it down.", "Tell it carefully", "Honor.", "Tell it once and stop", "Wise."),
], [
    ("end_best", "Your Own Best Thing", "You and Paul D, slowly, learn each other again. The porch is, by spring, full of bread and visitors."),
    ("end_denver", "Denver's Years", "Denver becomes, in time, a teacher. She moves into town. You visit. You watch her speak to children and feel, finally, a kind of pride that doesn't ache."),
    ("end_memory", "Disremembered", "Beloved's name fades from the town's stories. Yours does not. The book gets written. The book gets read. A century later it is, by some readers, a kind of altar."),
])

ONE_HUNDRED_YEARS = linear_story({
    "id": "fb-one-hundred-years", "title": "One Hundred Years of Solitude", "sourceTitle": "One Hundred Years of Solitude",
    "kind": "book", "synopsis": "Macondo. A town founded between a river and a swamp. Your family is the Buendía family. The world will come for you, slowly, in seven generations.",
    "releaseYear": 1967, "addedAt": "2026-02-12T00:00:00Z", "genre": "Drama",
    "tags": ["magical-realism", "marquez", "family"], "rating": None, "loved": False,
}, [
    ("Founding", "José Arcadio Buendía draws Macondo on a map.", "Plant the trees", "Path.", "Plant the streets", "Practical."),
    ("Gypsies", "Melquíades brings ice. Magnets. Flying carpets.", "Buy them all", "Wonder.", "Save your money", "Wise."),
    ("Yellow Butterflies", "Mauricio Babilonia, mechanic, follows your aunt.", "Note them", "Wise.", "Don't note", "Honest."),
    ("Colonel Aureliano", "He starts thirty-two civil wars and loses all of them.", "Visit him", "Family.", "Stay home", "Honest."),
    ("Workshop", "He makes little gold fishes and melts them down.", "Buy a fish", "Care.", "Don't buy", "Wise."),
    ("Ursula", "Your great-grandmother is, in her hundreds, holding it together.", "Help her", "Honor.", "Watch her", "Honest."),
    ("The Banana Company", "Foreigners arrive. The town fattens. Then they leave.", "Speak against them", "Brave.", "Stay quiet", "Honest."),
    ("The Massacre", "Three thousand workers killed at the station. The town forgets.", "Insist on memory", "Honor.", "Don't", "Survive."),
    ("Rain", "It rains for nearly five years.", "Build", "Patient.", "Wait", "Honest."),
    ("Remedios the Beauty", "She ascends to heaven hanging the sheets.", "Watch", "Wonder.", "Don't watch", "Honest."),
    ("Amaranta Embroiders Her Shroud", "She dies the day she finishes.", "Bury her with the shroud", "Honor.", "Use it for someone else", "Honest."),
    ("Aureliano José", "A young Buendía rediscovers Melquíades' room.", "Read with him", "Path.", "Stay out", "Honest."),
    ("The Parchments", "Sanskrit. Translated. The whole future of the family is, in fact, the past.", "Translate carefully", "Path.", "Stop reading", "Wise."),
    ("Forbidden Love", "A Buendía marries a Buendía. Pigs' tails are said to follow.", "Marry anyway", "Heart.", "Refuse", "Wise."),
    ("Pilar Ternera", "She lives long enough to know everyone twice. She reads cards.", "Visit her", "Honor.", "Don't", "Honest."),
    ("Ants", "The house is, finally, full of ants and dust.", "Sweep", "Resist.", "Don't sweep", "Honest."),
    ("The Last Child", "A child with a pig's tail is born.", "Take him in your arms", "Heart.", "Don't", "Honest."),
    ("Ants Carry Him", "The next morning, ants carry him to their nest.", "Read the last parchment now", "Path.", "Wait", "Honest."),
    ("Reading the End", "The parchments describe this moment, exactly.", "Read your name", "Honest.", "Look up", "Brave."),
    ("Wind", "A wind begins to take the town.", "Step into it", "Path.", "Stay inside", "Honest."),
    ("Macondo, Disappearing", "The town is, at last, a place that has been.", "Smile", "Honor.", "Cry", "Honest."),
], [
    ("end_wind", "Macondo, Wind", "The town is taken. The book ends. Generations after, in other cities, the book is read by people who do not know they are reading their own future."),
    ("end_parchment", "The Parchments, Translated", "A scholar in a quiet library, decades later, decodes the parchments fully. She publishes. The world reads. Macondo, against its own ending, persists."),
    ("end_family", "Family, Always", "Far from Macondo, descendants you didn't know about live ordinary lives. They name children, by chance, after you. They do not know why these names felt familiar."),
])

SHERLOCK = linear_story({
    "id": "fb-sherlock-holmes", "title": "The Adventures of Sherlock Holmes", "sourceTitle": "The Adventures of Sherlock Holmes",
    "kind": "book", "synopsis": "221B Baker Street. A cab in the rain. A client with a peculiar problem. You are, today, Holmes. The game, as he often says, is afoot.",
    "releaseYear": 1892, "addedAt": "2026-02-11T00:00:00Z", "genre": "Thriller",
    "tags": ["mystery", "victorian", "deduction"], "rating": None, "loved": False,
}, [
    ("Mrs. Hudson", "She brings tea. Watson is at the window.", "Read the paper", "Practice.", "Wait for a knock", "Patient."),
    ("Client at the Door", "A young woman with a half-burned letter.", "Read the letter", "Path.", "Read her hands", "Method."),
    ("The Carriage Tracks", "Outside, mud, two horses, fresh from the south road.", "Pursue", "Path.", "Wait for more clues", "Wise."),
    ("Lestrade", "Scotland Yard's most enthusiastic mistake. He invites you to a scene.", "Go", "Path.", "Send Watson", "Strategy."),
    ("The Scene", "A locked study. Powder on the curtain. A faint scent of cigar.", "Smell carefully", "Method.", "Look for fingerprints", "Modern."),
    ("Suspicion", "The butler. The nephew. The maid. The dog who didn't bark.", "The dog", "Method.", "The nephew", "Obvious."),
    ("Disguise", "You become an unemployed groom. Watson is, briefly, scandalized.", "Visit the stables", "Path.", "Visit the gentleman's club", "Society."),
    ("Mycroft", "Your brother knows things you don't. He weighs an opinion like a kingdom.", "Visit the Diogenes Club", "Wise.", "Don't bother him", "Honest."),
    ("Telegram", "From the south coast. Inquire about the schooner Friesland.", "Catch the next train", "Path.", "Telegraph back", "Smart."),
    ("Brighton", "A figure in a top hat does not, in fact, want to be followed.", "Follow on the pier", "Brave.", "Set a trap", "Cunning."),
    ("The Boatman", "He talks. Money is, sometimes, fluent.", "Pay him generously", "Smart.", "Pay him modestly", "Wise."),
    ("The Coded Letter", "You decode it in five minutes by counting letters.", "Note it", "Method.", "Don't show off", "Modesty."),
    ("Honoria's Brother", "He is, in fact, the missing heir. He has been hiding for years.", "Find him kindly", "Care.", "Confront", "Honest."),
    ("The Villain", "He is well-bred, well-dressed, and willing to murder. The worst kind.", "Don't underestimate him", "Wise.", "Take him alone", "Pride."),
    ("Reichenbach", "A different case, a different waterfall. He proposes single combat.", "Accept", "Brave.", "Plan a trick", "Wise."),
    ("Drop", "You and he go over. Watson finds the note.", "Survive", "Path.", "Don't", "Honest."),
    ("Three Years Gone", "You return to Baker Street disguised as a bookseller.", "Reveal slowly", "Style.", "Reveal quickly", "Honest."),
    ("Hudson's Reaction", "She faints once and recovers twice.", "Apologize", "Civil.", "Move past", "Honest."),
    ("Watson's Hands", "He punches the table. He hugs you.", "Apologize properly", "Honor.", "Joke", "Style."),
    ("The Letter from Mary", "A new client. A small problem. You smile.", "Take the case", "Path.", "Recommend a colleague", "Patient."),
    ("Tea", "Mrs. Hudson brings tea. You and Watson sip in companionable silence.", "Sip", "Quiet.", "Begin the next thing", "Path."),
], [
    ("end_retire", "Sussex Downs", "You retire to Sussex to keep bees. You write a small book on apiology that is, mercifully, better than the police think."),
    ("end_lestrade", "Lestrade's Tribute", "Lestrade, decades on, gives a speech in your honor. He calls you, with feeling, the best and wisest man he ever knew. Watson cries discreetly."),
    ("end_book", "The Adventures", "Watson publishes. The Strand prints. The world reads. You are, against your will, a literary figure for two centuries."),
])

SPECS += [CRIME_PUNISHMENT, WAR_PEACE, ANNA_KARENINA, MOBY_DICK, ODYSSEY, HAMLET, FRANKENSTEIN, DRACULA, BELOVED, ONE_HUNDRED_YEARS, SHERLOCK]

DON_QUIXOTE = linear_story({
    "id": "fb-don-quixote", "title": "Don Quixote", "sourceTitle": "Don Quixote",
    "kind": "book", "synopsis": "La Mancha. You read too many books and got the wrong ideas. Today you put on a rusted helmet and call your old horse Rocinante. You will be, you have decided, a knight.",
    "releaseYear": 1605, "addedAt": "2026-02-10T00:00:00Z", "genre": "Comedy",
    "tags": ["spain", "knight", "absurd"], "rating": None, "loved": False,
}, [
    ("Library", "Romances stacked to the ceiling.", "Burn them later", "Pride.", "Carry them", "Honest."),
    ("Helmet", "Cardboard reinforced with a basin.", "Wear it proudly", "Path.", "Wear it humbly", "Wise."),
    ("Rocinante", "Old, thin, willing.", "Pat his neck", "Care.", "Spur him", "Foolish."),
    ("Sancho", "A neighbor agrees to be your squire for the promise of an island.", "Promise", "Path.", "Confess no island exists", "Honor."),
    ("Windmills", "Giants on the plain. Wave their arms.", "Charge", "Path.", "Stop", "Wise."),
    ("Bruise", "You fall. Sancho lifts you.", "Insist they were giants", "Path.", "Admit windmills", "Honest."),
    ("Inn as Castle", "You request to be knighted by the innkeeper.", "Kneel", "Path.", "Pay him first", "Wise."),
    ("Goatherds", "You read them poetry. They are, mostly, polite.", "Continue", "Path.", "Stop", "Wise."),
    ("Galley Slaves", "You free them. They beat you and run.", "Mourn", "Honest.", "Insist it was right", "Honor."),
    ("Cardenio", "A madman in the mountains. He has a sad story.", "Listen", "Care.", "Lecture", "Foolish."),
    ("Dulcinea", "She is, you decide, a princess. She is, in fact, a farm girl named Aldonza.", "Believe she's a princess", "Path.", "Send her a letter signed your knight", "Honor."),
    ("Helmet of Mambrino", "A barber's basin. You insist.", "Wear it", "Path.", "Return it", "Honor."),
    ("Sancho's Wages", "He asks. You owe.", "Pay him in promises", "Path.", "Pay him real", "Honor."),
    ("The Duke and Duchess", "They host you to mock you. You don't notice.", "Be a good guest", "Civil.", "Suspect", "Wise."),
    ("Sancho's Island", "They give him a town to govern. He governs surprisingly well.", "Be proud", "Friend.", "Be jealous", "Honest."),
    ("Cave of Montesinos", "You go down. You report dreams.", "Tell them honestly", "Honest.", "Embellish", "Pride."),
    ("Knight of the White Moon", "A neighbor in armor challenges you. If he wins, you go home.", "Accept", "Honor.", "Decline", "Wise."),
    ("Defeat", "You lose. You ride home in your borrowed dignity.", "Be silent", "Honor.", "Plan revenge", "Foolish."),
    ("Fever", "Bed. The priest. The barber. Sancho weeps.", "Accept death", "Honor.", "Plan a shepherd's life", "Honest."),
    ("Confession", "You renounce the books.", "Mean it", "Honest.", "Half-mean it", "Honest."),
    ("Death", "You die. The village is quieter.", "Smile", "Honest.", "Cry", "Honest."),
], [
    ("end_books", "The Books, Burned", "Your library is burned, with the priest's careful selection. Some are saved. The village reads them, occasionally, with skepticism."),
    ("end_sancho", "Sancho's Telling", "Sancho tells your story to whoever stops at the inn. The story grows kinder as it travels. By a generation it is, in many ways, a kind of scripture."),
    ("end_quixote", "Quixote, Eternal", "An author named Cervantes hears the story. He writes it down. It outlives every kingdom you would have conquered. You become, against your will, a saint of imperfect courage."),
])

TALE_TWO_CITIES = linear_story({
    "id": "fb-tale-two-cities", "title": "A Tale of Two Cities", "sourceTitle": "A Tale of Two Cities",
    "kind": "book", "synopsis": "It was the best of times, it was the worst of times. London and Paris. A doctor recalled from the dead. A daughter. A revolution. A man who looks too much like another.",
    "releaseYear": 1859, "addedAt": "2026-02-09T00:00:00Z", "genre": "Drama",
    "tags": ["dickens", "revolution", "sacrifice"], "rating": None, "loved": False,
}, [
    ("Mail Coach", "A messenger meets a stranger. Recalled to life.", "Carry the message", "Path.", "Refuse it", "Wise."),
    ("Paris Garret", "A pale man at a cobbler's bench.", "Speak softly", "Care.", "Speak loud", "Honest."),
    ("London", "Lucie. Dr. Manette. The house under the plane tree.", "Settle them", "Care.", "Move them", "Wise."),
    ("Darnay's Trial", "A man accused of treason. A barrister yawns.", "Watch carefully", "Wise.", "Doubt the witnesses", "Honest."),
    ("Carton", "The man at the table looks like Darnay.", "Notice", "Wise.", "Don't notice", "Honest."),
    ("Soho Saturdays", "Tea at the Manettes'. Lorry of Tellson's. Pross with her brother.", "Be a regular", "Friend.", "Be a stranger", "Honest."),
    ("Darnay's Confession", "He is, in fact, of the Evrémonde family.", "Keep his secret", "Honor.", "Tell Lucie", "Honest."),
    ("Marriage", "Lucie marries Darnay. Dr. Manette holds.", "Stand with the doctor", "Honor.", "Stay home", "Honest."),
    ("Manette's Relapse", "He works at the cobbler's bench again, briefly.", "Be patient", "Care.", "Hide the bench", "Practical."),
    ("Paris, Storming", "The Bastille falls. The Defarges are at the front.", "Track the names knitted in", "Wise.", "Look away", "Honest."),
    ("Gabelle's Letter", "Darnay must come to Paris. He goes.", "Follow him", "Friend.", "Stay with Lucie", "Care."),
    ("Arrest", "Darnay is in La Force. Dr. Manette tries to help.", "Use his name", "Strategy.", "Stay quiet", "Honor."),
    ("Trial", "He is acquitted, briefly. A second indictment.", "Brace", "Wise.", "Hope", "Honest."),
    ("The Manuscript", "Dr. Manette's old letter from prison surfaces. It condemns Darnay's family.", "Confront Darnay's identity", "Honest.", "Plead", "Heart."),
    ("Death Sentence", "Darnay is condemned. Lucie collapses.", "Find Carton", "Path.", "Plan an escape with Pross", "Brave."),
    ("Carton's Plan", "He has, somehow, become a different man. He has, somehow, planned everything.", "Trust him", "Path.", "Doubt him", "Honest."),
    ("La Force, Visit", "Carton drugs Darnay, exchanges clothes, hides him in a carriage.", "Hold Lucie steady", "Care.", "Hold Manette steady", "Honor."),
    ("Carriage Out", "Pross, blocking Madame Defarge, holds the door.", "Stand with Pross", "Brave.", "Drive on", "Path."),
    ("Tellson's", "London, after. Lorry counts what was saved.", "Visit them", "Care.", "Stay alone", "Honest."),
    ("Letter", "A small letter, in Carton's hand. He has gone for them all.", "Read it aloud", "Honor.", "Read it quietly", "Honor."),
    ("Scaffold", "It is, he says, a far, far better thing.", "Honor him forever", "Honor.", "Don't speak of it", "Heart."),
], [
    ("end_carton", "Far, Far Better Thing", "Carton's name lives, quietly, in your family. Your son, eventually, is named Sydney. He grows up kind. He never quite knows why he is allowed to be."),
    ("end_lucie", "Lucie's Years", "Lucie lives long. She tells the story to grandchildren by a small fire. The grandchildren, in turn, tell their own."),
    ("end_quiet", "A Quieter Practice", "Dr. Manette returns to medicine. His patients are gentle with him. He sees, for the rest of his days, the shape of a tower no longer there."),
])

AND_THEN_NONE = linear_story({
    "id": "fb-and-then-none", "title": "And Then There Were None", "sourceTitle": "And Then There Were None",
    "kind": "book", "synopsis": "Soldier Island. Ten guests. Each has, by the host's letter, an unconfessed crime. One by one a nursery rhyme is being acted out.",
    "releaseYear": 1939, "addedAt": "2026-02-08T00:00:00Z", "genre": "Thriller",
    "tags": ["christie", "island", "rhyme"], "rating": None, "loved": False,
}, [
    ("The Boat", "Wind, salt, the island ahead.", "Make conversation", "Civil.", "Stay quiet", "Wise."),
    ("The House", "Servants who don't know the host either.", "Note the figurines", "Wise.", "Don't note", "Honest."),
    ("Dinner", "Ten places. Ten people. A record begins to play.", "Listen carefully", "Wise.", "Don't listen", "Honest."),
    ("Accusations", "The recording names each of you and an old death.", "Object", "Honest.", "Stay silent", "Wise."),
    ("Anthony Marston", "He laughs, drinks, falls dead. Cyanide.", "Note the cyanide source", "Wise.", "Mourn", "Honest."),
    ("Mrs. Rogers", "Found dead in her bed.", "Note the figurines have lost two", "Wise.", "Don't note", "Honest."),
    ("Search", "You search the island. No one else here.", "Search again", "Wise.", "Settle in", "Honest."),
    ("General Macarthur", "He sits by the sea waiting for it.", "Sit with him", "Care.", "Leave him", "Honest."),
    ("Rogers", "Found chopped, in the woodshed.", "Suspect Vera", "Wise.", "Suspect Blore", "Honest."),
    ("Emily Brent", "She sits in a chair, a wasp behind her.", "Examine the syringe", "Wise.", "Bury her", "Honest."),
    ("Wargrave", "He proposes search procedure. He is, you note, in charge.", "Follow", "Wise.", "Question", "Honest."),
    ("Lombard", "He has a revolver. Vera asks for it.", "Hold it yourself", "Wise.", "Let him keep it", "Honest."),
    ("Wargrave Shot", "Apparently. A wig and a robe. A staged death.", "Inspect the body", "Wise.", "Trust Armstrong", "Naive."),
    ("Armstrong, Missing", "He disappears in the night.", "Don't trust the seas", "Wise.", "Search the cliffs", "Brave."),
    ("Blore Killed", "A statue dropped from above.", "Suspect Lombard", "Wise.", "Suspect Vera", "Honest."),
    ("Armstrong Found", "On the rocks. Wet. Dead before he was wet.", "Trust nobody", "Wise.", "Trust Lombard", "Honest."),
    ("Vera's Shot", "She shoots Lombard. She walks back to the house.", "Climb the stairs", "Honest.", "Step out", "Honest."),
    ("The Noose", "A chair, a hook. Wargrave has prepared the room.", "Resist", "Brave.", "Step on the chair", "Honest."),
    ("Wargrave's Confession", "A note in a bottle. The judge has, on principle, judged.", "Read it slowly", "Honest.", "Stop reading", "Honest."),
    ("Sea Police", "A storm passes. Boats arrive.", "Tell the truth", "Honor.", "Withhold", "Honest."),
    ("The Bottle, Found", "Wargrave's confession surfaces. The case, eventually, is closed.", "Note the artifice", "Wise.", "Forget it", "Honest."),
], [
    ("end_book", "The Bottle Surfaces", "The case is, in time, closed. The book is, in time, opened by readers in every country. The rhyme outlives every culprit."),
    ("end_island", "The Island, Empty", "Soldier Island becomes a small ruin. Boats pass. Tourists come, sometimes, with a camera and a copy of the book."),
    ("end_inspector", "Inspector Maine", "Maine, who finds the bottle, becomes mildly famous. He retires with a small pension. He tells the story exactly twice in his life, both at funerals."),
])

BRAVE_NEW_WORLD = linear_story({
    "id": "fb-brave-new-world", "title": "Brave New World", "sourceTitle": "Brave New World",
    "kind": "book", "synopsis": "World State, six hundred years on. Ford bless us. The soma is free. The conditioning is finished by age six. You're an Alpha-Plus, slightly maladjusted, slightly too much.",
    "releaseYear": 1932, "addedAt": "2026-02-07T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["dystopia", "huxley", "happiness"], "rating": None, "loved": False,
}, [
    ("Hatchery Tour", "Decanting. Bokanovsky. The tourists nod.", "Be a polite tourist", "Civil.", "Note inconsistencies", "Wise."),
    ("Conditioning", "Sleep teachers murmur. Babies learn to hate flowers.", "Be uncomfortable", "Honest.", "Be amused", "Path."),
    ("Lenina", "She invites you to feely-night.", "Go", "Civil.", "Decline", "Honest."),
    ("Helmholtz", "A poet without a subject. He envies you, sort of.", "Befriend him", "Friend.", "Be wary", "Wise."),
    ("Bernard", "He bristles at orgy porgy. He smiles wrong.", "Travel with him", "Path.", "Avoid him", "Wise."),
    ("Reservation", "Savage land. Whips. A blue-eyed boy named John.", "Bring John back", "Path.", "Leave him", "Wise."),
    ("Linda", "His mother, fat, soma-mad, ashamed.", "Bring her too", "Care.", "Leave her", "Honest."),
    ("London Sensation", "John is, briefly, the celebrity.", "Defend him", "Friend.", "Don't intervene", "Honest."),
    ("Lenina's Move", "She tries to kiss him. He recoils.", "Mediate", "Care.", "Stay out", "Wise."),
    ("Linda's Death", "She dies of soma overdose at the hospital.", "Stay with John", "Honor.", "Step away", "Honest."),
    ("Soma Riot", "John throws soma rations out a window.", "Stand with him", "Brave.", "Stand back", "Wise."),
    ("Police, Singing", "Riot police arrive with synthetic music.", "Try to be heard", "Honor.", "Hide", "Wise."),
    ("Mond's Office", "World Controller, kind, terrifying.", "Argue freedom", "Honor.", "Listen", "Wise."),
    ("Bernard Exiled", "He weeps. He goes to Iceland.", "Comfort him", "Friend.", "Cut him off", "Honest."),
    ("Helmholtz Exiled", "He smiles. He wants the Falklands.", "Envy him", "Honest.", "Worry for him", "Care."),
    ("John's Lighthouse", "He moves to a lighthouse. He prays.", "Visit him", "Friend.", "Don't visit", "Honest."),
    ("The Crowd", "Tourists come to watch the savage. He flogs himself for them.", "Disperse them", "Brave.", "Watch", "Honest."),
    ("Orgy at the Lighthouse", "A frenzy. He, in despair, joins.", "Pull him out", "Friend.", "Don't", "Honest."),
    ("Morning After", "He hangs himself in the doorway.", "Cut him down", "Honor.", "Stand still", "Honest."),
    ("Mond's Office, Again", "He asks if you'd like to be exiled too.", "Yes", "Honor.", "No", "Honest."),
    ("Iceland", "A small town, free of soma, cold.", "Walk it slowly", "Path.", "Plan to write", "New."),
], [
    ("end_iceland", "Iceland", "You write a kind of pamphlet about feeling. It is, against all reason, smuggled to the cities. Some Alphas, late at night, read it."),
    ("end_helmholtz", "Helmholtz's Poems", "You join Helmholtz in the Falklands. He writes, for the rest of his life, poems no one needed but you. You read them aloud to a cold sea."),
    ("end_quiet", "The Lighthouse, Inherited", "You take over John's lighthouse. You burn the tourist coins. You read, alone, the books he kept. You decide, slowly, what to do next."),
])

FAHRENHEIT = linear_story({
    "id": "fb-fahrenheit-451", "title": "Fahrenheit 451", "sourceTitle": "Fahrenheit 451",
    "kind": "book", "synopsis": "Your job is to burn books. You wear a salamander and a number. Tonight, you'll meet a girl named Clarisse who asks if you're happy.",
    "releaseYear": 1953, "addedAt": "2026-02-06T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["censorship", "bradbury", "fire"], "rating": None, "loved": False,
}, [
    ("Sidewalk", "Clarisse walks beside you. She asks questions.", "Answer", "Path.", "Be brief", "Wise."),
    ("Home", "Mildred has the seashells in her ears.", "Speak to her", "Care.", "Stop", "Honest."),
    ("Alarm", "An old woman's house. Books in the attic.", "Try to save them", "Honor.", "Burn", "Job."),
    ("She Strikes the Match", "She stays with her books.", "Carry one home in your pocket", "Brave.", "Don't", "Wise."),
    ("Beatty", "Your captain. He quotes more than he should. He warns you.", "Listen", "Wise.", "Argue", "Honest."),
    ("Mildred Dosed", "Pumps, technicians, fluorescent dawn.", "Hold her hand", "Care.", "Step out", "Honest."),
    ("Clarisse Gone", "Run over, they say. The street is the suspect.", "Mourn", "Honest.", "Move on", "Survive."),
    ("Faber", "An old English professor in a quiet apartment.", "Recruit him", "Path.", "Listen", "Wise."),
    ("The Earpiece", "He gives you a small radio. He'll be in your ear.", "Wear it", "Path.", "Refuse", "Wise."),
    ("Dinner Party", "Mildred's friends. You read them poetry.", "Read it gently", "Honor.", "Read it loud", "Honest."),
    ("Alarm at Your House", "Mildred has called it in.", "Burn the parlor walls first", "Anger.", "Burn the books only", "Discipline."),
    ("Beatty's Hint", "He, almost, asks you to kill him.", "Pause", "Wise.", "Strike", "Anger."),
    ("Beatty Burned", "He falls.", "Run", "Survive.", "Stand", "Honor."),
    ("Hound", "The mechanical hound on your trail.", "River", "Smart.", "Subway", "Brave."),
    ("River", "You float downriver. Stars.", "Sleep on the bank", "Honest.", "Walk", "Wise."),
    ("The Camp", "Old men around a fire. Each is a book.", "Become one", "Path.", "Just listen", "Honor."),
    ("Granger", "He recites Plato. He laughs.", "Become Ecclesiastes", "Honor.", "Become Job", "Honest."),
    ("Bombs", "The city, behind you, is in light. Then it is dust.", "Mourn", "Honor.", "Walk on", "Honest."),
    ("Mildred, Probably", "You realize she likely was watching the parlor when it ended.", "Forgive her", "Heart.", "Don't", "Honest."),
    ("Phoenix", "Granger talks of the bird that burns and returns.", "Hope", "Honest.", "Don't", "Honest."),
    ("The Road", "You walk back toward the ash. People will need words.", "Walk", "Path.", "Stay another night", "Patient."),
], [
    ("end_book", "Becoming Ecclesiastes", "You become the book inside you. You recite it, slowly, to children. They learn it. They will, in time, recite it to other children."),
    ("end_writer", "Writer", "You and Granger, eventually, write a new book together. It is, mostly, a list of the books that were lost. It becomes the seed of a recovered library."),
    ("end_river", "The River Bank", "You stay by the river. You teach the people who pass. You light no fires you don't need. You die very old, with a small book in your hands that nobody burned."),
])

JANE_EYRE = linear_story({
    "id": "fb-jane-eyre", "title": "Jane Eyre", "sourceTitle": "Jane Eyre",
    "kind": "book", "synopsis": "Gateshead, Lowood, Thornfield. You are small and plain and on fire on the inside. The master of the house has, you'll learn, a wife in the attic.",
    "releaseYear": 1847, "addedAt": "2026-02-05T00:00:00Z", "genre": "Drama",
    "tags": ["bronte", "governess", "gothic"], "rating": None, "loved": False,
}, [
    ("Window Seat", "Bewick's Birds, rain, cousin John throws a book.", "Defend yourself", "Spirit.", "Submit", "Wise."),
    ("Red Room", "Locked in. Faint at midnight.", "Stand at the door", "Brave.", "Sleep", "Honest."),
    ("Mr. Brocklehurst", "He looks at you the way a wolf looks.", "Hold your gaze", "Spirit.", "Lower your eyes", "Wise."),
    ("Lowood", "Cold porridge. Helen Burns reads Rasselas.", "Befriend Helen", "Heart.", "Stay alone", "Honest."),
    ("Helen Dies", "Typhus in the spring. You sleep with your arms around her.", "Hold her", "Honor.", "Sit with her", "Honest."),
    ("Teacher Years", "You teach. The school improves. You leave at eighteen.", "Place an advertisement", "Spirit.", "Stay", "Safe."),
    ("Thornfield", "Mrs. Fairfax. Adele. A laugh in the upper hall.", "Note the laugh", "Wise.", "Don't", "Honest."),
    ("Lane in the Frost", "A man on a horse. The horse slips.", "Help him", "Care.", "Walk on", "Wise."),
    ("Mr. Rochester", "He, indoors, is your employer.", "Hold your tongue", "Wise.", "Hold your tongue except when honest", "Honest."),
    ("Fire", "His bedclothes on fire. You drench him.", "Pull him out", "Brave.", "Call for help", "Wise."),
    ("Gypsy", "A gypsy reads palms at the party. The voice is, somehow, his.", "Play along", "Wise.", "Confront", "Spirit."),
    ("Mason's Cry", "An attack in the night. A bite.", "Help him", "Care.", "Question him", "Wise."),
    ("Proposal", "Under the chestnut tree. The tree splits in the storm.", "Accept", "Heart.", "Hesitate", "Honest."),
    ("Wedding Halted", "Mr. Mason objects. The wife is, in fact, in the attic.", "Refuse the deception", "Honor.", "Stay anyway", "Heart."),
    ("Leaving", "Before dawn. A small bag. Tears that don't end.", "Walk to the moors", "Brave.", "Stay one more day", "Heart."),
    ("Moor House", "The Rivers family. Diana, Mary, St. John.", "Heal there", "Path.", "Refuse charity", "Pride."),
    ("Schoolmistress", "A village school. You teach the girls.", "Be content for a season", "Patient.", "Restless", "Honest."),
    ("Inheritance", "A letter. An uncle. Twenty thousand pounds.", "Split it with the Rivers", "Honor.", "Keep it", "Honest."),
    ("St. John's Proposal", "He wants you as a missionary's wife.", "Refuse", "Honor.", "Hesitate", "Honest."),
    ("Voice", "Across the moor: Jane, Jane, Jane.", "Go", "Path.", "Stay", "Honest."),
    ("Thornfield, Burned", "The house is ruins. He, blinded, lives at Ferndean.", "Find him", "Path.", "Walk away", "Honest."),
], [
    ("end_reader", "Reader, I Married Him", "You marry him at Ferndean. He regains sight in one eye in time to see your first child. You live, plainly and devotedly, for many years."),
    ("end_school", "A School of Her Own", "You open a small school for girls on your inheritance. You teach them, among other things, that a small plain girl can refuse a wrong life and find a right one."),
    ("end_writer", "Writer", "You write a book under another name. It is, in places, your life. It is, in many homes, kept on a shelf at the level of the eye."),
])

SPECS += [DON_QUIXOTE, TALE_TWO_CITIES, AND_THEN_NONE, BRAVE_NEW_WORLD, FAHRENHEIT, JANE_EYRE]

# ===========================================================================
# MINI STORIES — six-scene "five-minute" reads.
# ===========================================================================

MINI_ELEVATOR = mini_story({
    "id": "mn-stuck-elevator",
    "title": "Stuck in the Elevator",
    "sourceTitle": "Stuck in the Elevator",
    "kind": "movie", "synopsis": "Floor 23. The lights flicker. Three strangers. The fire alarm just went off.",
    "releaseYear": 2026, "addedAt": "2026-02-04T00:00:00Z", "genre": "Thriller",
    "tags": ["one-room"], "rating": None, "loved": False,
}, [
    ("The Stop", "The car jerks and stills. The display says 23. The smell is wrong.", "Hit the call button", "Tactical.", "Pry the doors", "Brave."),
    ("The Strangers", "A nurse, a teenager, a man with a briefcase. Each takes you in.", "Take charge", "Lead.", "Step back", "Wise."),
    ("Phones", "Two have no signal. The nurse's does.", "Coordinate", "Smart.", "Stay quiet", "Honest."),
    ("Smoke", "A thin line of smoke under the door. The boy starts coughing.", "Wet your shirts", "Smart.", "Lift the ceiling panel", "Brave."),
    ("Ladder Up", "Above the panel, an old maintenance ladder runs to the roof.", "Send the boy first", "Care.", "Send the strongest first", "Pragmatic."),
    ("Daylight", "Roof. Helicopters far off. The nurse hugs you in a way that is years of hugging compressed.", "Hug back", "Honor.", "Help the others up first", "Honor."),
], [
    ("end_safe", "Safe", "Everyone gets out. The man in the suit, weeping in his SUV, tells you it was his first day."),
    ("end_friend", "Friend in a Stairwell", "You stay friends with the nurse. You get drinks every February 4th."),
])

MINI_LOST_DOG = mini_story({
    "id": "mn-lost-dog",
    "title": "The Lost Dog",
    "sourceTitle": "The Lost Dog",
    "kind": "movie", "synopsis": "Saturday morning. A small wet dog on your porch with no tags. The rain isn't stopping.",
    "releaseYear": 2026, "addedAt": "2026-02-03T00:00:00Z", "genre": "Drama",
    "tags": ["small"], "rating": None, "loved": False,
}, [
    ("Porch", "He shivers at the door. He doesn't try to come in.", "Open the door", "Heart.", "Bring a towel out", "Wise."),
    ("Inside", "He sleeps on your old hoodie within twelve minutes.", "Post photos online", "Right.", "Knock door to door", "Honest."),
    ("The Walk", "Nobody recognizes him. A woman crosses herself. A kid hugs his neck.", "Try the vet", "Smart.", "Try the shelter", "Smart."),
    ("Chip", "The vet finds a chip. The owner moved out of state last year and didn't update.", "Try to reach her anyway", "Honor.", "Foster him for now", "Care."),
    ("She Calls Back", "She is on the phone crying. He has been missing for fourteen months.", "Offer to drive", "Care.", "Offer to ship him properly", "Practical."),
    ("Reunion", "She kneels on her driveway. He runs in a straight line.", "Stay for tea", "Friend.", "Drive home content", "Quiet."),
], [
    ("end_gift", "A Postcard, Every Month", "She sends you postcards forever. You frame the first one."),
    ("end_own", "Foster Fail", "You almost gave him up. You almost did. The almost was a long second."),
])

MINI_TAXI = mini_story({
    "id": "mn-airport-taxi",
    "title": "Airport at 5 a.m.",
    "sourceTitle": "Airport at 5 a.m.",
    "kind": "movie", "synopsis": "Your flight is in ninety minutes. The taxi smells like coffee and bad news.",
    "releaseYear": 2026, "addedAt": "2026-02-02T00:00:00Z", "genre": "Comedy",
    "tags": ["commute"], "rating": None, "loved": False,
}, [
    ("Backseat", "Driver: chatty. Radio: jazz. Traffic: ominous.", "Engage him", "Friend.", "Pretend to nap", "Wise."),
    ("Detour", "He knows a shortcut through old downtown.", "Trust him", "Brave.", "Insist on the highway", "Smart."),
    ("Construction", "A crane blocks the shortcut. He sighs theatrically.", "Tip him anyway", "Civil.", "Get out and run", "Brave."),
    ("Curbside", "Forty minutes to gate. The TSA line wraps the building.", "TSA Pre-line", "Smart.", "Charm the gate agent", "Spirit."),
    ("Gate", "Final boarding. You and your laptop bag, panting.", "Apologize to the row", "Civil.", "Sit and immediately read", "Honest."),
    ("In the Air", "Sun comes up over the wing. The bag's safe. Nobody died.", "Order coffee", "Joy.", "Sleep", "Honest."),
], [
    ("end_friend", "Cab Friend", "You and the driver text occasionally. He's a writer in his free time. His pieces are, against all odds, good."),
    ("end_quiet", "Just a Morning", "You land. You forget the cab in three days. You remember the jazz for years."),
])

MINI_PHONE = mini_story({
    "id": "mn-wrong-number",
    "title": "Wrong Number",
    "sourceTitle": "Wrong Number",
    "kind": "movie", "synopsis": "A voice on the line says, 'You weren't supposed to pick up.'",
    "releaseYear": 2026, "addedAt": "2026-02-01T00:00:00Z", "genre": "Thriller",
    "tags": ["one-call"], "rating": None, "loved": False,
}, [
    ("Ring", "Unknown number. 11:47 p.m.", "Answer", "Brave.", "Decline", "Wise."),
    ("Voice", "Calm, female, careful. She asks if you can keep a secret.", "Yes", "Honest.", "Hang up", "Wise."),
    ("Address", "She gives you an address. A bus station. Locker 47.", "Write it down", "Path.", "Repeat it back skeptically", "Smart."),
    ("Locker", "You go in the morning. There's a phone in the locker. It rings.", "Pick up", "Brave.", "Walk away", "Wise."),
    ("She Explains", "She is in danger. She needs you to mail an envelope.", "Mail it", "Honor.", "Open it first", "Foolish."),
    ("Done", "You drop it in the box. A week later, a news story. A man indicted.", "Note the story", "Witness.", "Don't note", "Honest."),
], [
    ("end_safe", "Anonymous Donor", "Your envelope was, the story implies, the key piece. Nobody ever knows it was you."),
    ("end_meeting", "Coffee, Months Later", "She finds you. She buys you coffee. She does not, you notice, tell you her real name. You don't mind."),
])

MINI_BABY = mini_story({
    "id": "mn-doorstep-baby",
    "title": "The Bundle on the Doorstep",
    "sourceTitle": "The Bundle on the Doorstep",
    "kind": "movie", "synopsis": "A basket. A baby. A note: 'I trust you.' You don't know who 'I' is.",
    "releaseYear": 2026, "addedAt": "2026-01-31T00:00:00Z", "genre": "Drama",
    "tags": ["tender"], "rating": None, "loved": False,
}, [
    ("Step", "She is sleeping. A tiny hat. No tags.", "Bring her in", "Heart.", "Call police", "Wise."),
    ("Crib", "You don't own a crib. The laundry basket has just been emptied.", "Improvise", "Practical.", "Drive to the 24-hour store", "Forward."),
    ("The Note", "Handwritten. 'I trust you. I'll come back. Be kind.'", "Believe it", "Heart.", "Doubt it", "Wise."),
    ("Hours", "She fusses, then sleeps, then fusses. You learn fast.", "Stay calm", "Care.", "Cry quietly", "Honest."),
    ("Knock", "A woman, exhausted, at the door at sunrise. She is, you understand instantly, the mother.", "Welcome her in", "Honor.", "Stand at the door", "Wise."),
    ("Coffee", "She drinks two cups. She tells you, slowly, the year she has had.", "Listen", "Honor.", "Offer help", "Care."),
], [
    ("end_aunt", "Aunt, Unofficially", "You become an aunt-figure to the baby. You help out for a year. The mother gets back on her feet."),
    ("end_self", "Quietly Yours", "You don't tell most people. The week is yours. The baby grows up. You keep a small photo in a drawer."),
])

MINI_LOCK = mini_story({
    "id": "mn-locksmith-2am",
    "title": "Locksmith at 2 a.m.",
    "sourceTitle": "Locksmith at 2 a.m.",
    "kind": "movie", "synopsis": "You answer the after-hours line. The voice is small and far away.",
    "releaseYear": 2026, "addedAt": "2026-01-30T00:00:00Z", "genre": "Drama",
    "tags": ["work"], "rating": None, "loved": False,
}, [
    ("Phone", "An older woman locked out. She is on her front porch. It is freezing.", "Drive over", "Care.", "Try to walk her through it", "Wise."),
    ("Driveway", "She is wearing slippers. Her cat is, somehow, in the bushes.", "Cat first", "Heart.", "Door first", "Pragmatic."),
    ("The Lock", "Old. Cantankerous. Two minutes of patience.", "Take your time", "Discipline.", "Force it", "Foolish."),
    ("Inside", "She turns on a kettle. Apologizes ten times. You wave her off.", "Stay for tea", "Honor.", "Decline, gentle", "Civil."),
    ("Photo", "On the mantel, a young woman in uniform. She tells you about her daughter.", "Listen", "Honor.", "Note the time, leave", "Wise."),
    ("Drive Home", "Dawn over the highway. You decide what kind of next month you want.", "Bring more presence to it", "Vow.", "Take a different shift", "Honest."),
], [
    ("end_route", "Your Route", "You become her once-a-month phone friend. You change a lightbulb for her sometimes. She bakes."),
    ("end_morning", "Morning, On", "You go home, sleep four hours, eat pancakes. You feel, for an unrelated reason, hopeful."),
])

SPECS += [MINI_ELEVATOR, MINI_LOST_DOG, MINI_TAXI, MINI_PHONE, MINI_BABY, MINI_LOCK]

# ===========================================================================
# SEED EXPANSIONS — replace the original hand-written seed JSONs (the same
# ids, expanded to the 20-decision-node shape used by every other story).
# ===========================================================================

DUNE_TWO = linear_story({
    "id": "dune-sands-of-fate", "title": "Dune: Part Two", "sourceTitle": "Dune: Part Two",
    "kind": "movie", "synopsis": "A desert prophet. A vendetta. A choice that will boil the sand.",
    "releaseYear": 2024, "addedAt": "2026-05-25T00:00:00Z", "genre": "Sci-Fi",
    "tags": ["epic", "desert", "prophecy"], "rating": 5, "loved": True,
}, [
    ("First Light", "Wind grinds the basin. A patrol below. Stilgar at your shoulder.",
     "Plant the thumper", "Call the maker.", "Order a quiet ambush", "Patience."),
    ("Shai-Hulud", "A wall of teeth eats the dune. The patrol breaks apart.",
     "Spare a survivor", "Mercy.", "End it cleanly", "Cold."),
    ("Knife Work", "Six bodies, no shouts. A tag in Chani's hand with your face on it.",
     "Hunt the traitor", "Anger.", "Say nothing, watch", "Patient."),
    ("The Sietch", "Reverend Mother watches you with old eyes.", "Drink the Water", "Path.", "Refuse", "Honest."),
    ("Visions", "Possible futures pour through you. Some are oceans of dead.",
     "Choose the smallest war", "Mercy.", "Choose the swiftest justice", "Anger."),
    ("Chani", "She loves you. She also doesn't love what you might become.",
     "Promise her", "Heart.", "Tell her the truth instead", "Honor."),
    ("Spice Field", "You destroy a harvester. The Harkonnens send Rabban personally.",
     "Strike Rabban directly", "Brave.", "Ambush his transport", "Smart."),
    ("Rabban", "His thopter falls. He kneels, half-burned, begging.",
     "End him", "Cold.", "Send him north broken", "Strategic."),
    ("North Council", "Sietch leaders argue your name.", "Speak as one of them", "Honor.", "Speak as the Lisan al-Gaib", "Power."),
    ("Gurney", "Halleck arrives with smugglers and old loyalty.",
     "Embrace him", "Heart.", "Use him for the war", "Discipline."),
    ("The Atomics", "Family atomics, sealed since your father. The risk is the universe.",
     "Move them out", "Strategic.", "Leave them buried", "Wise."),
    ("Emperor's Hand", "A Sardaukar squad lands. You bait them into a worm field.",
     "Spring the trap", "Smart.", "Take prisoners for parley", "Honor."),
    ("Princess Irulan", "Letters. Her father is, you read between lines, terrified.",
     "Write her back", "Cunning.", "Burn the letter", "Pride."),
    ("Stilgar's Belief", "He looks at you the way he looked at no man before.",
     "Honor his faith carefully", "Care.", "Let it carry you", "Power."),
    ("South", "You ride into the deep south. The crowds gather.",
     "Preach plain", "Honest.", "Preach in their language", "Power."),
    ("Holy War, Voted", "The council votes for jihad. You can still refuse.",
     "Refuse", "Honor.", "Accept", "Power."),
    ("Arrakeen", "The Emperor's frigate lands. Banners ripple. You take the field.",
     "Lead the charge", "Brave.", "Hang back and direct", "Wise."),
    ("Feyd", "The Harkonnen heir steps forward for a duel.",
     "Accept", "Honor.", "Send a champion", "Wise."),
    ("Crown", "Shaddam kneels on the sand. The crown is in your hands.",
     "Take it as Emperor", "Power.", "Crown a council instead", "Wise."),
    ("Chani, Walking Away", "She watches you marry a princess for politics.",
     "Run after her", "Heart.", "Let her go to the worms", "Honor."),
    ("Lisan al-Gaib", "Banners spread to every horizon. You have seen this.",
     "Carry the cost", "Vow.", "Try one more time to steer it small", "Mercy."),
], [
    ("end_jihad", "Holy War", "Green banners. Every horizon. You walk through it because you must — and you remember, every night, the futures where you didn't."),
    ("end_steward", "The Steward", "You refuse the crown. A council rules. Stilgar leads the desert. You marry Chani in a cave. The empire shrinks; the people breathe."),
    ("end_quiet", "South, Alone", "You walk south. The legend keeps moving without you. Some say that is the only ending where the desert keeps its god."),
])

ABBOTT = linear_story({
    "id": "abbott-supply-day", "title": "Abbott Elementary", "sourceTitle": "Abbott Elementary",
    "kind": "show", "synopsis": "There are eleven glue sticks for forty kids and someone unplugged the laminator. It's only Tuesday.",
    "releaseYear": 2025, "addedAt": "2026-05-26T00:00:00Z", "genre": "Comedy",
    "tags": ["school", "documentary", "patience"], "rating": 5, "loved": True,
}, [
    ("7:42 a.m.", "Supply closet: one ream of pink paper, a stapler with no staples, a dehydrated googly eye. The crew films your face.",
     "Email Ava politely", "Civil.", "Improvise pink-paper week", "Spirit."),
    ("Ava's Reply", "Three emojis, zero supplies. The espresso machine in her office hums.",
     "Note the espresso", "Witness.", "Ask for the budget code anyway", "Honest."),
    ("Mr. Howard's Room", "A pristine pack of construction paper. He's not in yet.",
     "Take one pack, leave a note", "Honor.", "Take it all", "Petty."),
    ("Barbara", "She pretends not to give you 22 markers.",
     "Thank her quietly", "Honor.", "Tease her", "Friend."),
    ("Janine, You", "Wait — you ARE Janine. Your reflection in the laminator glass says: 'You got this.'",
     "Believe yourself", "Spirit.", "Roll your eyes", "Honest."),
    ("Jacob", "He volunteers to make a TikTok asking parents to donate.",
     "Approve carefully", "Trust.", "Edit the script first", "Wise."),
    ("Gregory", "He fixes the laminator without saying anything.",
     "Tell him you noticed", "Care.", "Don't make it weird", "Wise."),
    ("Pink Facts Week", "Marcus, in class, asks why pink is a real color. You discover, live, you don't know.",
     "Make it a project", "Joy.", "Admit you don't know", "Honor."),
    ("Melissa", "She slides a box of bandages your way. 'Just in case,' she says.",
     "Take it", "Civil.", "Joke about which kid", "Honest."),
    ("Lunch", "You eat at your desk. The crew, mercifully, films the cafeteria instead.",
     "Read tomorrow's plan", "Discipline.", "Just breathe", "Honest."),
    ("Mr. Johnson", "The janitor says, calmly, that someone took the laminator power cord on purpose.",
     "Investigate", "Civic.", "Let it go", "Mercy."),
    ("Ava, Again", "She tells you she has a 'plan' for supplies. The plan involves a raffle.",
     "Indulge her", "Strategic.", "Push back kindly", "Honest."),
    ("Mom Call", "Marcus's mom calls. She loved Pink Facts.", "Invite her in", "Welcome.", "Promise next week's theme", "Forward."),
    ("Crisis", "A glue stick situation in K-2. You are summoned by a tearful aide.",
     "Resolve it sweetly", "Care.", "Recruit Mr. Howard", "Smart."),
    ("Howard's Quiet Apology", "He brings a fresh ream of paper to your room.",
     "Thank him", "Honor.", "Smile and move on", "Civil."),
    ("Faculty Lounge", "Coffee is terrible. The conversation is good.",
     "Vent", "Honest.", "Pivot to a plan for next week", "Forward."),
    ("After School", "Marcus shows you a notebook with eighteen perfectly drawn shades of pink.",
     "Frame it", "Heart.", "Keep it on the corkboard", "Sweet."),
    ("Crew Interview", "On camera: 'How was today?'", "Honestly", "Honor.", "Bravely", "Spirit."),
    ("3:08 p.m.", "Bell. Hallways thunder. You sit, briefly, in the empty classroom.",
     "Plan tomorrow", "Discipline.", "Sit a little longer", "Quiet."),
    ("Home", "Pasta. Wine. A bath. Then you fall asleep with the laptop open to a curriculum doc.",
     "Sleep", "Honest.", "One more email", "Spirit."),
    ("Wednesday", "Same closet. Slightly more glue. The googly eye is somehow watching back.",
     "Pink, again", "Joy.", "New color", "Spirit."),
], [
    ("end_pink", "Pink Facts Forever", "Pink Facts Week becomes a yearly tradition. Marcus, in middle school, still tells people about it."),
    ("end_funded", "Funded, Finally", "Ava's raffle, against all odds, raises enough for a year of supplies. You take the credit, then quietly give it to her."),
    ("end_yourself", "Janine, on Tape", "The documentary airs. People recognize you in CVS. You teach. You teach. You teach."),
])

SEVERANCE = linear_story({
    "id": "severance-the-elevator", "title": "Severance", "sourceTitle": "Severance",
    "kind": "show", "synopsis": "The doors close. The procedure begins. Who do you become when the floor ticks down?",
    "releaseYear": 2025, "addedAt": "2026-05-22T00:00:00Z", "genre": "Thriller",
    "tags": ["office", "memory", "split"], "rating": 5, "loved": True,
}, [
    ("Lobby, 8:47", "Lumon's hush. Milchick's smile. The elevator opens.",
     "Step in", "Path.", "Slip a note into your own pocket", "Cunning."),
    ("Floor 4", "Threshold flickers. You are at your desk, refining numbers you don't remember asking for.",
     "Refine the scary cluster", "Compliant.", "Hide them in a folder", "Spirit."),
    ("Mark", "Your colleague Mark says hello like he doesn't remember either.",
     "Whisper a question", "Brave.", "Pretend everything is fine", "Wise."),
    ("Helly", "New severed. She tries the door.",
     "Tell her the rules", "Honest.", "Help her test the door", "Brave."),
    ("Music Dance Experience", "Milchick brings the cart. The song is the same as last time.",
     "Dance", "Survive.", "Sit it out", "Honor."),
    ("Perpetuity Wing", "Wax Eagan looms. The exhibit smells of new carpet.",
     "Walk it slowly", "Wise.", "Skip the rest", "Spirit."),
    ("Irving", "He paints corridors he can't access.",
     "Ask why", "Honest.", "Don't ask", "Wise."),
    ("Burt", "Optics & Design. He hands Irving a cup of tea.",
     "Visit O&D with Irving", "Friend.", "Talk Irving out of it", "Wise."),
    ("Conference Room", "Cobel watches through the one-way. You feel her watching.",
     "Behave", "Survive.", "Look up at the mirror", "Spirit."),
    ("Outie Glimpse", "Mark, in a flicker, sees his outie's living room. Empty bottles.",
     "Tell Helly", "Honor.", "Keep it inside", "Honest."),
    ("Defiant Jazz", "Milchick announces a Defiant Jazz break. The song plays on a Casio.",
     "Roll with it", "Survive.", "Plant your feet", "Spirit."),
    ("Helly's Tape", "A resignation video. The outie refuses.",
     "Comfort Helly", "Care.", "Plan harder", "Brave."),
    ("Map of the Floor", "Irving's careful drawings, taped together.",
     "Memorize it", "Smart.", "Burn it after", "Discipline."),
    ("Lumon Handbook", "You find an annotated copy in the records corridor.",
     "Read passages aloud", "Honor.", "Photograph it via Burt", "Cunning."),
    ("Cobel's Pin", "A small pin in her lapel — your old mother's, you almost remember.",
     "Notice it", "Witness.", "Stop noticing", "Wise."),
    ("The Plan", "Overtime Contingency: brief activation of inside selves outside.",
     "Approve the plan", "Brave.", "Refuse", "Wise."),
    ("Wake on the Outside", "A child's birthday party. A husband you don't know. Your own face in a mirror.",
     "Announce who you are", "Brave.", "Find a phone first", "Smart."),
    ("Phone Booth", "You call an enemy of Lumon's. The line clicks.",
     "Speak fast", "Path.", "Stay vague", "Wise."),
    ("Cobel at the Party", "Across the room, smiling. She knows.",
     "Run", "Save.", "Walk evenly", "Discipline."),
    ("They Switch You Back", "The chip flips. You return to Floor 4 mid-sentence.",
     "Tell Mark immediately", "Honor.", "Write it down for next time", "Discipline."),
    ("Elevator Down", "End of shift. The doors close. Whoever you've been today, dissolves.",
     "Believe you'll come back", "Hope.", "Hope your other self does too", "Honest."),
], [
    ("end_break", "Break the Floor", "The recording leaks. The hearings begin. Floor 4 is dismantled, gently, over months. You meet your outie in a coffee shop and don't know what to say."),
    ("end_quiet", "Pay Day, Forever", "You step into the lobby with no memory of the day. Soup on the way home. The soup is good. The soup is, you tell yourself, good."),
    ("end_run", "Above Ground", "You make it out before Lumon catches up. A man on a loading dock says, simply, 'You're early.' He does not, you realize, mean today."),
])

BEAR = linear_story({
    "id": "bear-friday-rush", "title": "The Bear", "sourceTitle": "The Bear",
    "kind": "show", "synopsis": "Forty covers. Three line cooks. One temperamental pilot light. Don't burn it.",
    "releaseYear": 2024, "addedAt": "2026-05-18T00:00:00Z", "genre": "Drama",
    "tags": ["kitchen", "family", "pressure"], "rating": None, "loved": False,
}, [
    ("Open", "Sydney pulls a list. The walk-in is colder than yesterday. Richie is late.",
     "Start prep", "Discipline.", "Wait for Richie", "Mercy."),
    ("Mise", "Two cases of tomatoes. The herbs are good. The pilot light isn't.",
     "Light it manually", "Smart.", "Call the gas guy", "Wise."),
    ("Sysco Truck", "A delivery short by a case. The driver is sorry.",
     "Adapt the menu", "Wise.", "Demand a re-run", "Spirit."),
    ("Family Meal", "Marcus made bread. The bread is, by any measure, perfect.",
     "Praise him loudly", "Friend.", "Praise him quietly", "Honor."),
    ("First Reservation", "A four-top at 5:45. The dad has questions about gluten.",
     "Send Richie", "Strategic.", "Go yourself", "Honor."),
    ("Five-thirty", "Tickets start. Sydney calls them clean.",
     "Hands across", "Discipline.", "Yes, chef", "Honor."),
    ("Burned Roux", "A roux blackens. You smell it across the line.",
     "Restart", "Discipline.", "Push through", "Foolish."),
    ("Tina", "Tina has been on the line for thirty years. She steadies the pass.",
     "Promote her tonight", "Honor.", "Promote her on payday", "Wise."),
    ("Walk-In Drama", "A bin of stock has tipped. The floor is a flood.",
     "Stop service two minutes", "Smart.", "Push through", "Brave."),
    ("Saved", "You catch it before a fall. The stock isn't lost.",
     "Thank Marcus", "Honor.", "Don't break flow", "Discipline."),
    ("Front of House", "Richie remembers a regular's name. Their face lights up.",
     "Compliment him", "Honor.", "Note it for later", "Discipline."),
    ("Critic, Maybe", "A two-top at the corner: notebook out.",
     "Send the off-menu special", "Strategy.", "Don't show off", "Wise."),
    ("Cousin Mike", "A memory of your brother flashes during a quiet moment.",
     "Let it pass", "Honest.", "Speak his name aloud", "Heart."),
    ("Push", "Seven o'clock. Tickets stacked. Hands across.",
     "Call ahead by ten", "Smart.", "Stay live", "Brave."),
    ("Saute Burn", "Carmy burns his wrist. Sydney moves him off.",
     "Sub in yourself", "Honor.", "Send him out front", "Care."),
    ("Pastry", "Marcus needs an extra minute on plating. The window is hot.",
     "Hold a beat", "Discipline.", "Send what's ready", "Smart."),
    ("Comp", "A dish goes back wrong. The table is gracious.",
     "Comp the table", "Honor.", "Comp and visit", "Friend."),
    ("Last Cover", "9:42 p.m. The kitchen is, briefly, almost quiet.",
     "Walk the dining room", "Honor.", "Sit on a crate", "Honest."),
    ("Close", "Sweep, wipe, rotate, prep. Marcus hums something.",
     "Sing along", "Joy.", "Just clean", "Discipline."),
    ("After", "Beer crates outside. Eleven people in love with one bad pilot light.",
     "Share the night", "Family.", "Walk home alone", "Honest."),
    ("Tomorrow's List", "You write tomorrow's prep at the cold pass.",
     "Aim higher", "Spirit.", "Aim steady", "Wise."),
], [
    ("end_star", "A Star", "Months later the inspector arrives. Star, half. The kitchen, for a beat, cries together. Then Sydney calls service."),
    ("end_family", "Family Meal", "You don't get the star. You get something almost as rare: a kitchen full of people who like coming back tomorrow."),
    ("end_carmy", "Carmy, Quieter", "Carmy takes a step back. You and Sydney run the line cleaner without him. He drops in on Thursdays to taste."),
])

SPECS += [DUNE_TWO, ABBOTT, SEVERANCE, BEAR]

# Top 10 movies from top 5 IMDb genres (Action, Drama, Comedy, Sci-Fi, Horror).
# Each genre lives in its own sibling module to keep this file from growing unbounded.
from top_genres_action import ACTION_SPECS
from top_genres_drama import DRAMA_SPECS
from top_genres_comedy import COMEDY_SPECS
from top_genres_scifi import SCIFI_SPECS
from top_genres_horror import HORROR_SPECS
SPECS += ACTION_SPECS + DRAMA_SPECS + COMEDY_SPECS + SCIFI_SPECS + HORROR_SPECS

# First-party signature stories set the quality bar for future originals.
from original_stories import ORIGINAL_SPECS
SPECS += ORIGINAL_SPECS

# "The Night Shelf" — a curated set of after-midnight doorway originals.
from original_shorts import NIGHT_SHELF_SPECS
SPECS += NIGHT_SHELF_SPECS
