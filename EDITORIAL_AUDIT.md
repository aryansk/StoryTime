# StoryTime Editorial Audit

Automated editorial QA for the bundled story catalog. Structural
validation remains in `scripts/validate_catalog.py`; plot accuracy,
voice, pacing, and IP review still require human judgment.

## Summary

- Stories: 182
- Reader-facing words: 494,846
- Average words per story: 2,719
- Median words per story: 2,832
- Automated errors: 0
- Automated warnings: 406

## Errors

- None.

## Highest-priority warnings

- abbott-supply-day: 23 formulaic passage(s): s1/choice-2: 'You commit to', s2/choice-1: 'You choose to', s3/choice-1: 'You choose to', s6/choice-1: 'You choose to', s7/choice-1: 'You choose to', s7/choice-2: 'You commit to', s8/choice-1: 'You commit to', s8/choice-2: 'You commit to' ...
- abbott-supply-day: 5 one-word choice label(s): s11/choice-1, s16/choice-1, s18/choice-1, s18/choice-2, s20/choice-1
- abbott-supply-day: 20/21 decision nodes immediately converge
- bear-friday-rush: 19 formulaic passage(s): s1/choice-1: 'opens the route to', s1/choice-1: 'You choose to', s4/choice-2: 'opens the route to', s4/choice-2: 'You choose to', s5/choice-2: 'You commit to', s6/choice-2: 'opens the route to', s6/choice-2: 'You choose to', s11/choice-2: 'opens the route to' ...
- bear-friday-rush: 1 one-word choice label(s): s7/choice-1
- bear-friday-rush: 20/21 decision nodes immediately converge
- beast-games-the-final-round: 18 formulaic passage(s): s2/choice-2: 'You commit to', s3/choice-1: 'You choose to', s3/choice-2: 'You commit to', s6/choice-1: 'You commit to', s8/choice-1: 'You commit to', s8/choice-2: 'You choose to', s10/choice-2: 'You choose to', s11/choice-1: 'You commit to' ...
- black-swan-the-role: 26 formulaic passage(s): s1/choice-1: 'You choose to', s1/choice-2: 'You choose to', s2/choice-1: 'You commit to', s2/choice-2: 'You choose to', s3/choice-1: 'You choose to', s4/choice-1: 'You choose to', s4/choice-2: 'You commit to', s6/choice-1: 'You commit to' ...
- bodkin-the-podcast: 21 formulaic passage(s): s1/choice-2: 'You commit to', s2/choice-1: 'You choose to', s2/choice-2: 'You commit to', s3/choice-1: 'You commit to', s3/choice-2: 'You choose to', s4/choice-2: 'You commit to', s5/choice-1: 'You commit to', s7/choice-1: 'You commit to' ...
- bugonia-the-basement: 24 formulaic passage(s): s1/choice-1: 'You choose to', s2/choice-1: 'You commit to', s2/choice-2: 'You commit to', s3/choice-2: 'You commit to', s5/choice-2: 'You choose to', s6/choice-1: 'You choose to', s7/choice-2: 'You commit to', s8/choice-2: 'You commit to' ...
- cabin-10-the-luxury-cruise: 22 formulaic passage(s): s1/choice-1: 'You commit to', s2/choice-1: 'You choose to', s4/choice-1: 'You choose to', s4/choice-2: 'You choose to', s5/choice-1: 'You choose to', s6/choice-1: 'You commit to', s6/choice-2: 'You commit to', s8/choice-1: 'You commit to' ...
- dahmer-the-neighbor: 18 formulaic passage(s): s1/choice-2: 'You commit to', s2/choice-1: 'You commit to', s2/choice-2: 'You commit to', s3/choice-1: 'You commit to', s5/choice-2: 'You choose to', s7/choice-1: 'You choose to', s9/choice-1: 'You choose to', s10/choice-1: 'You choose to' ...
- devs-the-determinism: 18 formulaic passage(s): s1/choice-2: 'You choose to', s2/choice-2: 'You commit to', s3/choice-1: 'You choose to', s3/choice-2: 'You choose to', s8/choice-2: 'You commit to', s9/choice-2: 'You choose to', s12/choice-1: 'You commit to', s12/choice-2: 'You commit to' ...
- dhurandhar-2-the-return: 26 formulaic passage(s): s2/choice-1: 'You choose to', s2/choice-2: 'You commit to', s3/choice-2: 'You commit to', s4/choice-1: 'You commit to', s5/choice-1: 'You choose to', s5/choice-2: 'You commit to', s6/choice-1: 'You choose to', s6/choice-2: 'You commit to' ...
- dhurandhar-2-the-return: 1 one-word choice label(s): s1/choice-1
- dont-look-up-the-press-tour: 24 formulaic passage(s): s2/choice-1: 'You choose to', s2/choice-2: 'You choose to', s3/choice-1: 'You commit to', s3/choice-2: 'You choose to', s4/choice-1: 'You choose to', s5/choice-1: 'You choose to', s5/choice-2: 'You commit to', s7/choice-1: 'You commit to' ...
- dune-one-arrakeen-arrival: 10 formulaic passage(s): s2/choice-2: 'You commit to', s12/choice-2: 'You commit to', s14/choice-1: 'You choose to', s14/choice-2: 'You choose to', s15/choice-1: 'You choose to', s15/choice-2: 'You choose to', s17/choice-2: 'You choose to', s18/choice-1: 'You commit to' ...
- dune-sands-of-fate: 15 formulaic passage(s): s1/choice-2: 'You choose to', s3/choice-1: 'You commit to', s3/choice-2: 'You choose to', s6/choice-1: 'You commit to', s7/choice-2: 'You commit to', s10/choice-1: 'You commit to', s11/choice-1: 'You choose to', s12/choice-2: 'You commit to' ...
- dune-sands-of-fate: 4 one-word choice label(s): s4/choice-2, s16/choice-1, s16/choice-2, s18/choice-1
- dune-sands-of-fate: 20/21 decision nodes immediately converge
- euphoria-the-meeting: 24 formulaic passage(s): s1/choice-2: 'opens the route to', s1/choice-2: 'You choose to', s2/choice-1: 'opens the route to', s2/choice-1: 'You choose to', s3/choice-2: 'opens the route to', s3/choice-2: 'You choose to', s5/choice-2: 'opens the route to', s5/choice-2: 'You choose to' ...
- eurotrip-the-summer: 28 formulaic passage(s): s1/choice-2: 'You commit to', s2/choice-1: 'You commit to', s2/choice-2: 'You choose to', s3/choice-1: 'You choose to', s4/choice-1: 'You choose to', s4/choice-2: 'You choose to', s5/choice-2: 'You choose to', s6/choice-1: 'You choose to' ...
- eurotrip-the-summer: 6 one-word choice label(s): s3/choice-1, s9/choice-1, s9/choice-2, s10/choice-1, s10/choice-2, s11/choice-1
- eurotrip-the-summer: 20/21 decision nodes immediately converge
- fb-1984: 11 formulaic passage(s): s2/choice-2: 'You choose to', s11/choice-2: 'You choose to', s13/choice-2: 'You commit to', s14/choice-1: 'You choose to', s14/choice-2: 'You choose to', s15/choice-2: 'You commit to', s16/choice-1: 'You commit to', s17/choice-2: 'You choose to' ...
- fb-1984: 15 one-word choice label(s): s2/choice-1, s3/choice-1, s3/choice-2, s5/choice-2, s8/choice-2, s11/choice-2, s13/choice-1, s13/choice-2 ...
- fb-1984: 20/21 decision nodes immediately converge
- fb-and-then-none: 26 formulaic passage(s): s1/choice-1: 'You choose to', s2/choice-1: 'You commit to', s2/choice-2: 'You commit to', s3/choice-2: 'You commit to', s4/choice-2: 'You choose to', s5/choice-1: 'You commit to', s5/choice-2: 'You commit to', s6/choice-1: 'You commit to' ...
- fb-and-then-none: second-person voice missing from 13 node(s): s2, s3, s5, s6, s8, s9, s13, s19 ...
- fb-and-then-none: 6 one-word choice label(s): s4/choice-1, s5/choice-2, s11/choice-1, s11/choice-2, s18/choice-1, s20/choice-2
- fb-and-then-none: 20/21 decision nodes immediately converge
- fb-anna-karenina: 24 formulaic passage(s): s3/choice-2: 'opens the route to', s3/choice-2: 'You choose to', s4/choice-1: 'opens the route to', s4/choice-1: 'You choose to', s4/choice-2: 'opens the route to', s4/choice-2: 'You choose to', s5/choice-1: 'You commit to', s7/choice-1: 'You commit to' ...
- fb-anna-karenina: 12 one-word choice label(s): s1/choice-2, s2/choice-1, s2/choice-2, s3/choice-2, s4/choice-2, s7/choice-1, s9/choice-1, s11/choice-2 ...
- fb-anna-karenina: 20/21 decision nodes immediately converge
- fb-beloved: 36 formulaic passage(s): s1/choice-1: 'You commit to', s2/choice-1: 'You commit to', s3/choice-1: 'You commit to', s3/choice-2: 'opens the route to', s3/choice-2: 'You choose to', s5/choice-1: 'You commit to', s6/choice-1: 'opens the route to', s6/choice-1: 'You choose to' ...
- fb-beloved: second-person voice missing from 7 node(s): s9, s12, s13, s14, s19, s20, end_memory
- fb-beloved: 7 one-word choice label(s): s1/choice-1, s1/choice-2, s9/choice-2, s11/choice-2, s12/choice-1, s14/choice-2, s18/choice-2
- fb-beloved: 20/21 decision nodes immediately converge
- fb-brave-new-world: 20 formulaic passage(s): s2/choice-2: 'You commit to', s5/choice-1: 'You commit to', s6/choice-2: 'You choose to', s7/choice-1: 'You commit to', s7/choice-2: 'You choose to', s8/choice-2: 'You commit to', s11/choice-2: 'You commit to', s12/choice-1: 'You choose to' ...
- fb-brave-new-world: second-person voice missing from 14 node(s): s2, s4, s6, s7, s8, s9, s10, s11 ...
- fb-brave-new-world: 9 one-word choice label(s): s3/choice-1, s3/choice-2, s9/choice-1, s12/choice-2, s13/choice-2, s17/choice-2, s18/choice-2, s20/choice-1 ...
- fb-brave-new-world: 20/21 decision nodes immediately converge
- fb-catcher-rye: 23 formulaic passage(s): s5/choice-1: 'opens the route to', s5/choice-1: 'You choose to', s6/choice-1: 'You commit to', s7/choice-1: 'opens the route to', s7/choice-1: 'You choose to', s8/choice-2: 'opens the route to', s8/choice-2: 'You choose to', s9/choice-1: 'You commit to' ...
- fb-catcher-rye: 16 one-word choice label(s): s1/choice-2, s3/choice-2, s4/choice-2, s5/choice-2, s7/choice-2, s8/choice-2, s9/choice-2, s10/choice-1 ...
- fb-catcher-rye: 20/21 decision nodes immediately converge
- fb-crime-punishment: 20 formulaic passage(s): s3/choice-2: 'You commit to', s4/choice-2: 'opens the route to', s4/choice-2: 'You choose to', s9/choice-1: 'opens the route to', s9/choice-1: 'You choose to', s10/choice-1: 'opens the route to', s10/choice-1: 'You choose to', s11/choice-1: 'You commit to' ...
- fb-crime-punishment: 12 one-word choice label(s): s2/choice-2, s4/choice-2, s5/choice-1, s5/choice-2, s6/choice-1, s6/choice-2, s8/choice-1, s8/choice-2 ...
- fb-crime-punishment: 20/21 decision nodes immediately converge
- fb-don-quixote: 21 formulaic passage(s): s1/choice-1: 'You choose to', s1/choice-2: 'You commit to', s2/choice-1: 'You commit to', s3/choice-1: 'You commit to', s4/choice-1: 'You commit to', s4/choice-2: 'You commit to', s5/choice-1: 'You commit to', s6/choice-1: 'You choose to' ...
- fb-don-quixote: 15 one-word choice label(s): s4/choice-1, s5/choice-1, s5/choice-2, s7/choice-1, s8/choice-1, s8/choice-2, s9/choice-1, s10/choice-1 ...
- fb-don-quixote: 20/21 decision nodes immediately converge
- fb-dracula: 27 formulaic passage(s): s1/choice-1: 'You commit to', s1/choice-2: 'You commit to', s3/choice-1: 'You commit to', s3/choice-2: 'You choose to', s5/choice-2: 'You commit to', s6/choice-1: 'You commit to', s7/choice-1: 'You choose to', s8/choice-1: 'You commit to' ...
- fb-dracula: 12 one-word choice label(s): s1/choice-2, s4/choice-1, s4/choice-2, s7/choice-2, s9/choice-1, s9/choice-2, s10/choice-2, s12/choice-1 ...
- fb-dracula: 20/21 decision nodes immediately converge
- fb-fahrenheit-451: 9 formulaic passage(s): s2/choice-2: 'You choose to', s8/choice-2: 'You commit to', s13/choice-1: 'You choose to', s14/choice-1: 'You commit to', s14/choice-2: 'You choose to', s17/choice-2: 'You choose to', s19/choice-2: 'You choose to', s20/choice-2: 'You commit to' ...
- fb-fahrenheit-451: 21 one-word choice label(s): s1/choice-1, s2/choice-2, s3/choice-2, s4/choice-2, s5/choice-1, s5/choice-2, s7/choice-1, s8/choice-2 ...
- fb-fahrenheit-451: 20/21 decision nodes immediately converge
- fb-frankenstein: 9 formulaic passage(s): s2/choice-1: 'You choose to', s8/choice-2: 'You commit to', s9/choice-1: 'You choose to', s11/choice-2: 'You choose to', s12/choice-1: 'You commit to', s13/choice-2: 'You choose to', s16/choice-2: 'You choose to', s18/choice-2: 'You choose to' ...
- fb-frankenstein: 16 one-word choice label(s): s1/choice-1, s1/choice-2, s2/choice-1, s2/choice-2, s6/choice-1, s6/choice-2, s7/choice-2, s8/choice-1 ...
- fb-frankenstein: 20/21 decision nodes immediately converge
- fb-great-gatsby: 17 formulaic passage(s): s2/choice-2: 'You commit to', s6/choice-1: 'opens the route to', s6/choice-1: 'You choose to', s6/choice-2: 'opens the route to', s6/choice-2: 'You choose to', s7/choice-1: 'opens the route to', s7/choice-1: 'You choose to', s9/choice-1: 'You commit to' ...
- fb-great-gatsby: 13 one-word choice label(s): s2/choice-1, s2/choice-2, s3/choice-1, s4/choice-1, s6/choice-1, s6/choice-2, s7/choice-2, s8/choice-1 ...
- fb-great-gatsby: 20/21 decision nodes immediately converge
- fb-hamlet: 33 formulaic passage(s): s3/choice-2: 'You commit to', s5/choice-1: 'opens the route to', s5/choice-1: 'You choose to', s5/choice-2: 'You commit to', s7/choice-1: 'You commit to', s7/choice-2: 'You commit to', s8/choice-1: 'opens the route to', s8/choice-1: 'You choose to' ...
- fb-hamlet: 13 one-word choice label(s): s1/choice-2, s2/choice-1, s2/choice-2, s8/choice-1, s8/choice-2, s9/choice-1, s9/choice-2, s10/choice-1 ...
- fb-hamlet: 20/21 decision nodes immediately converge
- fb-harry-potter-1: 9 one-word choice label(s): s1/choice-2, s10/choice-1, s12/choice-2, s13/choice-2, s17/choice-2, s18/choice-1, s18/choice-2, s19/choice-2 ...
- fb-harry-potter-1: 20/21 decision nodes immediately converge
- fb-hobbit: 10 one-word choice label(s): s1/choice-2, s2/choice-1, s2/choice-2, s5/choice-1, s5/choice-2, s6/choice-1, s6/choice-2, s11/choice-2 ...
- fb-hobbit: 20/21 decision nodes immediately converge
- fb-jane-eyre: 9 formulaic passage(s): s5/choice-1: 'opens the route to', s5/choice-1: 'You choose to', s5/choice-2: 'opens the route to', s5/choice-2: 'You choose to', s7/choice-1: 'opens the route to', s7/choice-1: 'You choose to', s9/choice-1: 'opens the route to', s9/choice-1: 'You choose to' ...
- fb-jane-eyre: 12 one-word choice label(s): s1/choice-2, s2/choice-2, s6/choice-2, s7/choice-2, s11/choice-2, s13/choice-1, s13/choice-2, s17/choice-2 ...
- fb-jane-eyre: 20/21 decision nodes immediately converge
- fb-lotr: 2 formulaic passage(s): s1/choice-1: 'You commit to', s10/choice-1: 'You commit to'
- fb-lotr: 17 one-word choice label(s): s1/choice-1, s1/choice-2, s2/choice-1, s2/choice-2, s4/choice-1, s4/choice-2, s6/choice-1, s7/choice-1 ...
- fb-lotr: 20/21 decision nodes immediately converge
- fb-moby-dick: 13 formulaic passage(s): s2/choice-1: 'You commit to', s3/choice-2: 'opens the route to', s3/choice-2: 'You choose to', s4/choice-2: 'opens the route to', s4/choice-2: 'You choose to', s5/choice-2: 'You commit to', s7/choice-1: 'opens the route to', s7/choice-1: 'You choose to' ...
- fb-moby-dick: second-person voice missing from 12 node(s): s2, s6, s7, s12, s13, s14, s15, s16 ...
- fb-moby-dick: 8 one-word choice label(s): s3/choice-1, s9/choice-2, s13/choice-2, s14/choice-1, s15/choice-2, s17/choice-2, s21/choice-1, s21/choice-2
- fb-moby-dick: 20/21 decision nodes immediately converge
- fb-mockingbird: 9 formulaic passage(s): s10/choice-2: 'opens the route to', s10/choice-2: 'You choose to', s12/choice-1: 'opens the route to', s12/choice-1: 'You choose to', s16/choice-1: 'opens the route to', s16/choice-1: 'You choose to', s18/choice-1: 'You commit to', s20/choice-1: 'opens the route to' ...
- fb-mockingbird: 20 one-word choice label(s): s1/choice-1, s3/choice-1, s4/choice-1, s4/choice-2, s5/choice-2, s9/choice-2, s11/choice-1, s11/choice-2 ...
- fb-mockingbird: 20/21 decision nodes immediately converge
- fb-odyssey: 2 one-word choice label(s): s13/choice-2, s14/choice-2
- fb-odyssey: 20/21 decision nodes immediately converge
- fb-one-hundred-years: second-person voice missing from 10 node(s): s3, s4, s5, s9, s10, s12, s15, s21 ...
- fb-one-hundred-years: 11 one-word choice label(s): s8/choice-2, s9/choice-1, s9/choice-2, s10/choice-1, s14/choice-2, s15/choice-2, s16/choice-1, s17/choice-2 ...
- fb-one-hundred-years: 20/21 decision nodes immediately converge
- fb-pride-prejudice: 9 one-word choice label(s): s4/choice-2, s5/choice-2, s7/choice-1, s10/choice-1, s10/choice-2, s11/choice-2, s17/choice-2, s18/choice-1 ...
- fb-pride-prejudice: 20/21 decision nodes immediately converge
- fb-sherlock-holmes: second-person voice missing from 9 node(s): s1, s2, s3, s4, s5, s6, s10, s12 ...
- fb-sherlock-holmes: 9 one-word choice label(s): s3/choice-1, s4/choice-1, s13/choice-2, s15/choice-1, s16/choice-1, s16/choice-2, s18/choice-1, s19/choice-2 ...
- fb-sherlock-holmes: 20/21 decision nodes immediately converge
- fb-tale-two-cities: second-person voice missing from 24 node(s): s1, s2, s3, s4, s5, s6, s7, s8 ...
- fb-tale-two-cities: 4 one-word choice label(s): s5/choice-1, s13/choice-1, s13/choice-2, s14/choice-2
- fb-tale-two-cities: 20/21 decision nodes immediately converge
- fb-war-peace: 4 one-word choice label(s): s1/choice-2, s3/choice-1, s9/choice-2, s13/choice-2
- fb-war-peace: 20/21 decision nodes immediately converge
- fm-12-angry-men: second-person voice missing from 18 node(s): s1, s2, s3, s4, s6, s7, s8, s9 ...
- fm-12-angry-men: 11 one-word choice label(s): s2/choice-1, s2/choice-2, s10/choice-1, s10/choice-2, s12/choice-1, s13/choice-1, s13/choice-2, s17/choice-2 ...

## Manual review batches

### Batch 1: abbott-supply-day to fb-anna-karenina

- Abbott Elementary — 3,405 words
- The Bear — 3,277 words
- Beast Games — 3,430 words
- Black Swan — 2,661 words
- Bodkin — 3,648 words
- Bugonia — 3,505 words
- The Woman in Cabin 10 — 3,759 words
- Monster: The Jeffrey Dahmer Story — 3,677 words
- Devs — 3,412 words
- Dhurandhar: Part 2 — 3,745 words
- Dhurandhar — 2,760 words
- Don't Look Up — 3,557 words
- Dune: Part One — 3,452 words
- Dune: Part Two — 3,334 words
- Eternity — 3,606 words
- Euphoria — 3,410 words
- EuroTrip — 3,456 words
- 1984 — 3,305 words
- And Then There Were None — 3,585 words
- Anna Karenina — 3,499 words

### Batch 2: fb-beloved to fb-sherlock-holmes

- Beloved — 3,739 words
- Brave New World — 3,655 words
- The Catcher in the Rye — 3,484 words
- Crime and Punishment — 3,347 words
- Don Quixote — 3,377 words
- Dracula — 3,435 words
- Fahrenheit 451 — 3,255 words
- Frankenstein — 3,299 words
- The Great Gatsby — 3,352 words
- Hamlet — 3,639 words
- Harry Potter and the Philosopher's Stone — 3,241 words
- The Hobbit — 3,067 words
- Jane Eyre — 3,258 words
- The Lord of the Rings — 3,126 words
- Moby-Dick — 3,413 words
- To Kill a Mockingbird — 3,325 words
- The Odyssey — 3,282 words
- One Hundred Years of Solitude — 2,850 words
- Pride and Prejudice — 2,907 words
- The Adventures of Sherlock Holmes — 2,877 words

### Batch 3: fb-tale-two-cities to fm-departed

- A Tale of Two Cities — 3,089 words
- War and Peace — 3,091 words
- 12 Angry Men — 3,089 words
- 2001: A Space Odyssey — 3,269 words
- Alien — 3,334 words
- Aliens — 3,203 words
- Amélie — 3,494 words
- American History X — 2,830 words
- The Apartment — 3,510 words
- Arrival — 2,779 words
- Avatar — 2,817 words
- Avengers: Endgame — 3,480 words
- Back to the Future — 2,738 words
- Blade Runner — 2,724 words
- Casablanca — 2,978 words
- Children of Men — 2,835 words
- Citizen Kane — 2,975 words
- City Lights — 3,392 words
- The Dark Knight — 3,408 words
- The Departed — 3,110 words

### Batch 4: fm-die-hard to fm-hereditary

- Die Hard — 3,414 words
- District 9 — 2,808 words
- Star Wars: The Empire Strikes Back — 3,334 words
- E.T. the Extra-Terrestrial — 2,946 words
- Eternal Sunshine of the Spotless Mind — 2,903 words
- Ex Machina — 2,914 words
- The Exorcist — 3,282 words
- Fight Club — 3,059 words
- Forrest Gump — 2,944 words
- Get Out — 3,422 words
- Gladiator — 3,568 words
- The Godfather — 3,064 words
- The Godfather Part II — 3,083 words
- Gone with the Wind — 3,122 words
- Goodfellas — 3,049 words
- The Grand Budapest Hotel — 3,312 words
- Grave of the Fireflies — 1,892 words
- The Great Dictator — 3,269 words
- The Green Mile — 2,071 words
- Hereditary — 3,419 words

### Batch 5: fm-inception to fm-psycho

- Inception — 2,909 words
- Inglourious Basterds — 3,486 words
- Interstellar — 2,085 words
- It's a Wonderful Life — 2,090 words
- Jaws — 3,626 words
- John Wick — 3,550 words
- Jurassic Park — 2,161 words
- Let the Right One In — 3,695 words
- Life Is Beautiful — 3,295 words
- The Lion King — 2,043 words
- The Lord of the Rings: The Fellowship of the Ring — 2,159 words
- The Lord of the Rings: The Return of the King — 3,716 words
- The Lord of the Rings: The Two Towers — 1,948 words
- Mad Max: Fury Road — 1,951 words
- Metropolis — 2,173 words
- Modern Times — 3,330 words
- Night of the Living Dead — 3,685 words
- One Flew Over the Cuckoo's Nest — 2,003 words
- The Prestige — 2,049 words
- Psycho — 3,638 words

### Batch 6: fm-pulp-fiction to hijack-flight-72

- Pulp Fiction — 2,881 words
- Rosemary's Baby — 3,612 words
- Saving Private Ryan — 1,864 words
- Schindler's List — 2,097 words
- The Shawshank Redemption — 2,084 words
- The Shining — 2,014 words
- The Silence of the Lambs — 2,903 words
- Singin' in the Rain — 2,554 words
- Some Like It Hot — 2,499 words
- Star Wars: A New Hope — 2,172 words
- Terminator 2: Judgment Day — 1,888 words
- The Matrix — 2,059 words
- The Thing — 1,976 words
- Titanic — 2,072 words
- Toy Story — 2,569 words
- Wall-E — 2,073 words
- The Wizard of Oz — 2,105 words
- Game of Thrones — 2,755 words
- Heartbreak High — 2,507 words
- Hijack — 3,024 words

### Batch 7: him-and-hers-the-recording to night-last-ferry

- Him and Hers — 3,108 words
- Hoppers — 2,708 words
- A House of Dynamite — 2,877 words
- The Housemaid — 2,980 words
- Imperfect Women — 2,318 words
- Invincible — 2,552 words
- Ladies First — 2,245 words
- Loot — 2,642 words
- Are You There God? It's Me, Margaret. — 2,870 words
- Mercy — 3,106 words
- Airport at 5 a.m. — 825 words
- The Bundle on the Doorstep — 506 words
- Locksmith at 2 a.m. — 565 words
- The Lost Dog — 595 words
- Stuck in the Elevator — 948 words
- Wrong Number — 495 words
- Monarch: Legacy of Monsters — 2,395 words
- More the Merrier — 2,438 words
- The Cartographer of Wrong Turns — 1,029 words
- Last Call at the Ferry — 1,017 words

### Batch 8: night-midnight-bakery to severance-the-elevator

- The Midnight Bakery — 1,040 words
- Signal Hill — 1,021 words
- The Tenant Below — 938 words
- The Understudy — 976 words
- Off Campus — 2,300 words
- The Last Lightkeeper — 1,825 words
- The Museum of Unsent Letters — 1,870 words
- Outcome — 2,748 words
- Palm Royale — 2,694 words
- The Devil Wears Prada 2 — 2,445 words
- The Pursuit of Happyness — 2,946 words
- Roommates — 2,446 words
- Scary Movie 2 — 2,469 words
- Scary Movie 3 — 2,166 words
- Scary Movie 4 — 2,833 words
- Scary Movie 5 — 2,158 words
- Scouts Guide to the Zombie Apocalypse — 2,184 words
- Scream — 2,076 words
- Sebastian — 2,369 words
- Severance — 2,114 words

### Batch 9: shrinking-the-honest-week to young-sheldon-science-fair

- Shrinking — 2,700 words
- Smile 2 — 2,439 words
- Speak No Evil — 2,484 words
- Stranger Things — 2,329 words
- Superstore — 2,817 words
- Something Very Bad Is Gonna Happen — 2,726 words
- Tell Me Lies — 2,144 words
- The Bluff — 1,989 words
- The Boroughs — 2,266 words
- The Boys — 2,491 words
- The Great — 2,778 words
- The Intern — 2,446 words
- The Lost Bus — 2,777 words
- Toaster — 2,173 words
- Wayward — 2,724 words
- Wicked: For Good — 2,655 words
- Wolves — 2,648 words
- A Wrinkle in Time — 2,158 words
- Wuthering Heights — 2,601 words
- Young Sheldon — 2,464 words

### Batch 10: zero-day-the-network to zodiac-the-cartoonist

- Zero Day — 2,247 words
- Zodiac — 2,222 words

## Human-review rubric

- Verify plot, character, setting, and source-title accuracy.
- Read every branch transition and confirm the consequence leads
  naturally into the destination scene.
- Remove repeated sentence shapes and generic dramatic filler.
- Confirm second-person voice, tense, and tone stay consistent.
- Check that sibling choices express meaningfully different values.
- Confirm each ending reflects the decisions that can reach it.
- Review commercial, licensing, and attribution implications.
