"""StoryTime signature originals.

These stories are deliberately more branch-forward than the adaptation
catalog: early choices open genuinely different scenes and several distinct
endings. They establish the quality bar for future first-party releases.
"""


LAST_LIGHTKEEPER = (
    {
        "id": "original-last-lightkeeper",
        "title": "The Last Lightkeeper",
        "sourceTitle": "The Last Lightkeeper",
        "kind": "book",
        "synopsis": "On your final night tending a lighthouse, a second beacon appears where no island has ever been—and it is flashing your name.",
        "releaseYear": 2026,
        "addedAt": "2026-07-16T00:00:00Z",
        "genre": "Fantasy",
        "tags": ["original", "signature", "sea", "mystery", "mini"],
        "rating": 5,
        "loved": True,
    },
    [
        {
            "id": "lantern_room",
            "title": "The Impossible Light",
            "text": "The storm arrives before sunset, shouldering the horizon into darkness. You are trimming the lighthouse wick for the last time when another beam sweeps across the glass—far out at sea, where your charts show only a trench two miles deep. It flashes once, twice, then spells your childhood name in patient white arcs.",
            "choices": [
                ("Climb outside and answer with the great lens", "Brave.", "answer_light"),
                ("Wake the dead radio and listen first", "Wise.", "answer_radio"),
            ],
        },
        {
            "id": "answer_light",
            "title": "A Conversation in Beams",
            "text": "Rain needles your face on the gallery walk. You turn the brass wheel by hand, dragging the lighthouse beam across the black water. The distant light pauses, then mirrors every movement exactly. When you stop, it continues alone: a doorway, a wave, and the shape of a small figure waiting on a shore that should not exist.",
            "choices": [
                ("Flash the old distress pattern", "Duty.", "distress_reply"),
                ("Cover the lens and break the connection", "Cautious.", "covered_lens"),
            ],
        },
        {
            "id": "answer_radio",
            "title": "Channel Thirteen",
            "text": "The radio has been silent since the mainland decommissioned your post. Tonight its valves warm beneath your fingers. Through the static, a woman says she is the keeper of the other light. Her voice is older than the storm and younger than your memory. “Please,” she says, “before the tide remembers us both.”",
            "choices": [
                ("Tell her your name and ask what she needs", "Honest.", "voice_reply"),
                ("Say nothing and triangulate the signal", "Smart.", "chart_room"),
            ],
        },
        {
            "id": "distress_reply",
            "title": "Three Short, Three Long",
            "text": "Your distress call crosses the waves. The other beacon answers with the same pattern, then adds a final sweep toward the harbor village behind you. Below, every house goes dark at once. In the sudden absence of electric light, pale footprints appear across the sea’s surface, approaching the lighthouse step by step.",
            "choices": [
                ("Open the sea gate before the visitor arrives", "Trust.", "the_arrival"),
                ("Hold the beam steady on the village", "Duty.", "the_bargain"),
            ],
        },
        {
            "id": "covered_lens",
            "title": "Footsteps in the Dark",
            "text": "The instant you shutter the lens, something begins climbing the spiral stair below. Not a hurried intruder: a familiar tread, counting each step the way your father did when he taught you the tower. His old oilskin hangs beside the door, dry and empty. The keeper’s journal rattles inside its locked desk.",
            "choices": [
                ("Unlock the journal before the footsteps arrive", "Curious.", "the_journal"),
                ("Meet the footsteps halfway down", "Brave.", "the_bargain"),
            ],
        },
        {
            "id": "voice_reply",
            "title": "The Keeper Across the Water",
            "text": "The woman repeats your name with relief. She says every lighthouse has a twin that appears only when its keeper is ready to leave. One guides ships through water; the other guides memories through loss. If neither keeper crosses tonight, the storm will take the village’s past—names first, then faces, then every reason anyone stayed.",
            "choices": [
                ("Believe her and prepare the sea gate", "Faith.", "the_arrival"),
                ("Demand proof only the real keeper could know", "Cautious.", "the_journal"),
            ],
        },
        {
            "id": "chart_room",
            "title": "An Island Drawn in Salt",
            "text": "The signal points nowhere on the official chart. Yet spilled salt creeps across the table and gathers into coastlines. At the center is a tiny lighthouse; beside it, in your own handwriting, are the words RETURN WHAT THE SEA KEPT. The supply boat strains against its ropes below, though the tide is running the other way.",
            "choices": [
                ("Take the boat toward the salt-drawn island", "Bold.", "the_arrival"),
                ("Stay in the tower and protect the village", "Loyal.", "the_bargain"),
            ],
        },
        {
            "id": "the_arrival",
            "title": "The Boat With No Wake",
            "text": "A narrow boat glides through the sea gate without disturbing the water. Its passenger is you at nine years old, soaked from the day your brother vanished beyond the breakwater. The child holds the red scarf you searched for all that summer. “You can keep the light,” they say, “or you can finally learn what it was hiding.”",
            "choices": [
                ("Take the child's hand and step into the boat", "Heart.", "between_tides"),
                ("Close the gate and keep watch until dawn", "Duty.", "end_steadfast"),
            ],
        },
        {
            "id": "the_bargain",
            "title": "What the Tower Wants",
            "text": "The lighthouse speaks through gears, glass, and the iron bones of its stair. It has held every goodbye uttered within sight of its beam, and it is full. To survive the storm it needs a keeper’s promise: name someone who must remain, or extinguish the lamp and release every stored farewell into the night.",
            "choices": [
                ("Offer your own name to the tower", "Sacrifice.", "names_in_glass"),
                ("Extinguish the lamp and free the farewells", "Mercy.", "end_darkness"),
            ],
        },
        {
            "id": "the_journal",
            "title": "The Missing Final Page",
            "text": "Your father’s journal opens to an entry dated tomorrow. He writes that the other lighthouse is not a place but a choice every keeper postpones. Tucked into the binding is the missing final page and, beneath it, your brother’s red scarf—still smelling faintly of sun-warmed rope and the oranges he stole from the pantry.",
            "choices": [
                ("Read the final page aloud", "Truth.", "names_in_glass"),
                ("Wrap the journal in the scarf and carry it outside", "Heart.", "between_tides"),
            ],
        },
        {
            "id": "between_tides",
            "title": "The Water Between Moments",
            "text": "The boat crosses not distance but years. Around you float mornings the village forgot: weddings, storms survived, children learning the names of birds. Ahead, the second lighthouse burns inside a wave that never breaks. You may turn its beam home and restore every memory, or sail through the light toward the one person the sea never returned.",
            "choices": [
                ("Turn the impossible beam toward the village", "Care.", "end_beacon"),
                ("Sail through the light and follow the red scarf", "Love.", "end_return"),
            ],
        },
        {
            "id": "names_in_glass",
            "title": "The Lens Remembers",
            "text": "Names bloom across the great lens in salt-white script. Some belong to the living, others to those the sea carried beyond maps. There is room for one more. The tower waits without judgment, offering permanence but not freedom. Down in the village, porch lights begin returning one by one.",
            "choices": [
                ("Write your own name and become the final keeper", "Honor.", "end_guardian"),
                ("Write your brother's name and let the tower return him", "Heart.", "end_return"),
            ],
        },
        {
            "id": "end_steadfast",
            "title": "The Light That Stayed",
            "text": "You keep the gate barred and the beam moving until sunrise. The impossible lighthouse fades with the stars. The village wakes safe, though several elders cannot remember the songs they taught their children. Years later, sailors still swear your final night produced the steadiest light they ever saw—and the saddest.",
            "end": "The Light That Stayed",
        },
        {
            "id": "end_darkness",
            "title": "A Sky Full of Goodbyes",
            "text": "You lower the wick. Darkness takes the tower, then erupts with a thousand soft voices crossing the water toward home. By dawn the storm is gone and the lighthouse is only stone. The village remembers everyone it has lost. For one extraordinary morning, grief sounds less like emptiness and more like a harbor answering back.",
            "end": "A Sky Full of Goodbyes",
        },
        {
            "id": "end_beacon",
            "title": "Keeper of Returning Things",
            "text": "You turn the second beam shoreward. Memory pours across the village: misplaced names, old promises, the exact warmth of hands long gone. Your own past returns too, sharp but survivable. When the sun rises, both lighthouses remain. You tend neither alone; every remembered person keeps a small part of the watch.",
            "end": "Keeper of Returning Things",
        },
        {
            "id": "end_return",
            "title": "Beyond the Breakwater",
            "text": "The light opens like a door. On the far side, your brother waits on a summer shore, older by exactly the years you have lived without him. Whether you bring him home or choose to stay is a story the village never learns. They only know two figures stood in the dawn where the sea had always been empty.",
            "end": "Beyond the Breakwater",
        },
        {
            "id": "end_guardian",
            "title": "The Name in the Lens",
            "text": "Your name sinks into the glass and shines. The storm bends around the tower. You feel every ship seeking harbor and every memory looking for a way home, but the weight no longer frightens you. The mainland may call the post abandoned; still, on difficult nights, two beacons answer each other across the impossible water.",
            "end": "The Name in the Lens",
        },
    ],
)


UNSENT_LETTERS = (
    {
        "id": "original-museum-unsent-letters",
        "title": "The Museum of Unsent Letters",
        "sourceTitle": "The Museum of Unsent Letters",
        "kind": "book",
        "synopsis": "A museum that opens for one hour each year offers to deliver a letter you never sent—but every delivery changes two lives.",
        "releaseYear": 2026,
        "addedAt": "2026-07-16T00:00:00Z",
        "genre": "Drama",
        "tags": ["original", "signature", "magical-realism", "letters", "grief", "mini"],
        "rating": 5,
        "loved": True,
    },
    [
        {
            "id": "invitation",
            "title": "Open Between 2:00 and 3:00 A.M.",
            "text": "The invitation arrives in your own handwriting, though you have never seen the black envelope before. It names a museum absent from every map and promises one service: bring the letter you most regret not sending. At 2:07 a.m., a brass door appears between the laundromat and the closed florist downstairs.",
            "choices": [
                ("Bring the letter you wrote to your mother", "Heart.", "archive_desk"),
                ("Enter empty-handed and ask who invited you", "Cautious.", "delivery_room"),
            ],
        },
        {
            "id": "archive_desk",
            "title": "The Archivist",
            "text": "An archivist with ink-stained cuffs weighs your letter on a silver scale. The needle trembles between APOLOGY and EXPLANATION. “We can deliver it to the day it was meant for,” she says, “or to the person your mother became after never receiving it. Those are not the same address.”",
            "choices": [
                ("Send it backward to the day you left home", "Brave.", "letter_to_past"),
                ("Send it to your mother as she is now", "Honest.", "letter_to_present"),
            ],
        },
        {
            "id": "delivery_room",
            "title": "Shelves Without End",
            "text": "Beyond the desk, millions of sealed letters rise in dark wooden stacks. Some hum with anger; others are almost weightless. The archivist admits your invitation was written by a future visitor using your name. Before she can explain, one envelope falls open at your feet. It is addressed to you from your mother.",
            "choices": [
                ("Read your mother's unsent letter", "Curious.", "letter_to_you"),
                ("Leave it sealed and search for the future visitor", "Discipline.", "future_gallery"),
            ],
        },
        {
            "id": "letter_to_past",
            "title": "The Kitchen, Twelve Years Ago",
            "text": "The delivery room becomes your childhood kitchen. Your younger self stands in the hall with a packed bag while your mother pretends to wash an already clean cup. The letter can change what happens next, but the archivist warns that you will keep only one version of this memory: the repaired one or the true one.",
            "choices": [
                ("Place the letter where your mother will find it", "Hope.", "changed_home"),
                ("Give it to your younger self instead", "Truth.", "younger_self"),
            ],
        },
        {
            "id": "letter_to_present",
            "title": "The Address She Never Gave You",
            "text": "The museum prints a current address beneath your mother’s name. It is three streets from your apartment. She has been living nearby for four years, respecting the silence she believed you requested. A courier waits beside a bicycle made of folded envelopes and asks whether the letter should arrive alone or with you behind it.",
            "choices": [
                ("Let the courier deliver it first", "Patient.", "waiting_bench"),
                ("Carry it to her door yourself", "Brave.", "her_door"),
            ],
        },
        {
            "id": "letter_to_you",
            "title": "Dear You, Whenever You Are Ready",
            "text": "Your mother’s letter contains no defense. She writes that love can be sincere and still fail someone, that she mistook providing answers for listening, and that she would accept any boundary except one built from a lie you both kept repeating. At the bottom she asks a single question: What happened from your side?",
            "choices": [
                ("Answer her question in a new letter", "Honest.", "writing_room"),
                ("Take her letter home without answering", "Boundaries.", "end_kept_letter"),
            ],
        },
        {
            "id": "future_gallery",
            "title": "Portrait of a Visitor",
            "text": "In the final gallery, portraits show everyone who has ever used the museum. Your future self hangs in the last frame, older and calmer, holding two unopened letters. A plaque says you founded this place after learning that closure is not the same thing as an answer. The painted eyes turn toward a small writing room.",
            "choices": [
                ("Meet the future version of yourself", "Curious.", "future_self"),
                ("Refuse the prophecy and enter the writing room", "Spirit.", "writing_room"),
            ],
        },
        {
            "id": "changed_home",
            "title": "A Memory Rearranged",
            "text": "Your mother finds the letter before you leave. The argument becomes a conversation—not gentle, not perfect, but honest enough to alter the years ahead. New memories flicker into place: cautious phone calls, a graduation seat filled, ordinary Tuesdays shared. One old truth begins disappearing with them: the person you became while surviving alone.",
            "choices": [
                ("Accept the kinder history", "Hope.", "end_rewritten"),
                ("Restore the life you actually lived", "Honor.", "end_true_memory"),
            ],
        },
        {
            "id": "younger_self",
            "title": "What You Needed Then",
            "text": "Your younger self reads the first line and knows exactly who you are. They do not ask whether life improves. They ask whether leaving was cruel. You can offer the comfort you spent years waiting to hear, or tell them the harder truth: protecting yourself may hurt someone and still be necessary.",
            "choices": [
                ("Tell them they are not cruel", "Care.", "end_true_memory"),
                ("Tell them courage can still carry guilt", "Wise.", "end_open_door"),
            ],
        },
        {
            "id": "waiting_bench",
            "title": "Across the Street",
            "text": "You watch from a museum bench that now faces your mother’s building. The courier leaves the envelope. A lamp comes on upstairs; a silhouette reads without moving. Ten minutes later the front door opens. Your mother steps outside with no coat, looking both directions as if she has remembered how hope works but not where to find it.",
            "choices": [
                ("Cross the street", "Brave.", "end_open_door"),
                ("Let the letter be enough for tonight", "Patient.", "end_kept_letter"),
            ],
        },
        {
            "id": "her_door",
            "title": "Three Knocks",
            "text": "Your mother opens the door before the third knock. For a long moment neither of you performs surprise. You hold out the letter; she asks whether you want tea. The museum clock sounds in the distance, warning that its hour is almost over and any conversation begun inside its magic must be chosen freely to continue.",
            "choices": [
                ("Go in for tea and begin without the letter", "Honest.", "end_open_door"),
                ("Give her the letter and ask for time", "Boundaries.", "end_kept_letter"),
            ],
        },
        {
            "id": "writing_room",
            "title": "A Page That Does Not Judge",
            "text": "The writing room offers paper but no eraser. You begin with the sentence you avoided for years: I loved you, and I was hurt. The words do not cancel each other. When you finish, the museum offers two envelopes—one addressed to your mother, the other to the person you were when silence felt safest.",
            "choices": [
                ("Send the letter to your mother", "Hope.", "end_open_door"),
                ("Send it to your younger self", "Care.", "end_true_memory"),
            ],
        },
        {
            "id": "future_self",
            "title": "The Founder",
            "text": "Your future self steps out of the portrait and sets two letters on the table. One contains reconciliation; the other, a peaceful goodbye. “I cannot tell you which I chose,” they say. “The museum exists because both can be acts of love.” They offer you the keys, but taking them means remaining after the brass door vanishes.",
            "choices": [
                ("Take the keys and keep the museum open", "Service.", "end_archivist"),
                ("Leave both futures unwritten and go home", "Free.", "end_true_memory"),
            ],
        },
        {
            "id": "end_rewritten",
            "title": "The Kinder History",
            "text": "You wake with photographs from years you never lived and a dozen affectionate messages waiting on your phone. The loneliness is gone. So are several fierce, beloved parts of the life it pushed you to build. You grieve them quietly, then call your mother. A kinder history is still a history; now you must learn how to inhabit it.",
            "end": "The Kinder History",
        },
        {
            "id": "end_true_memory",
            "title": "Nothing Erased",
            "text": "You keep the life that happened—the hurt, the distance, and the strength that grew around both. Yet the memory no longer feels like a locked room. When the museum disappears, the florist’s window reflects someone capable of honoring the past without living inside it. In your pocket is a blank page for whatever comes next.",
            "end": "Nothing Erased",
        },
        {
            "id": "end_open_door",
            "title": "Tea Before Answers",
            "text": "You do not solve twelve years in one night. You make tea. You say what can be said, stop when it becomes too much, and agree on a day to try again. At 3:00 a.m. the museum vanishes, but the ordinary door across from you remains open. For now, ordinary is more than enough.",
            "end": "Tea Before Answers",
        },
        {
            "id": "end_kept_letter",
            "title": "The Letter You Keep",
            "text": "Not every unsent letter is unfinished business. Sometimes it is a record of what you survived and what you are not ready to reopen. You leave the museum with both letters in your coat. Months later, you read them without shaking. Whether you ever send one matters less than knowing the choice is finally yours.",
            "end": "The Letter You Keep",
        },
        {
            "id": "end_archivist",
            "title": "Keeper of the Unsaid",
            "text": "The brass keys warm in your hand. Shelves unfold beyond the walls, full of apologies, confessions, boundaries, and goodbyes waiting for honest timing. When the next visitor arrives, you do not promise delivery will fix anything. You promise only a quiet room, a truthful page, and the dignity of choosing what happens to it.",
            "end": "Keeper of the Unsaid",
        },
    ],
)


ORIGINAL_SPECS = [LAST_LIGHTKEEPER, UNSENT_LETTERS]
