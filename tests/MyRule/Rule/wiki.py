from infini.rule import WikiModel


class Wiki(WikiModel):

    class THE_RULES(WikiModel.Setting):
        @property
        def desc(self):
            return self.__str__()

        def __str__(self):
            return """The Pool is a role-playing system geared toward player and GM narrative 
    collaboration. You can use it for any setting you like. One person in your 
    group needs to be the Game Master, or GM—this is the person who 
    runs the game. To play you need a lot of d6s (six-sided dice) including a 
    handful of “GM dice” that look different from the rest. 
    Before character creation begins, each player needs 15 dice for their 
    starting Pool. The rest of the dice go into a common pool. """

        def __repr__(self):
            return self.__str__()

    class CHARACTER_CREATION:
        @property
        def character_creation(self) -> str:
            return """Once your group has decided on a setting you can begin creating 
    characters. 
    Making a character is simple: just write a 50 word Story. Pretend you’re 
    writing a book and this is the introduction of your main character. 
    You only have 50 words to play with, so focus on the most important 
    elements of your new character and how the character fits into the setting 
    your group has chosen. Mentioning your character’s name does not 
    count towards the word limit."""

        @property
        def example(self) -> str:
            return """\
I’ve created my first character for The Pool. The setting is a world of 
darkish magical fantasy. 
“Damart is a sorcerer trained in elemental magic by the secret Lost Land order. 
He was expelled from the Order after falling in love with a young initiate who 
died when he tried to teach her a spell she could not control. Now Damart 
seeks the means to bring her back to life.” """

    class ASSIGNING_TRAITS_AND_BONUSES:
        @property
        def desc(self) -> str:
            return """\
Now pick the most important elements of your Story. These are Traits 
that will help you gain narrative control during play. 
Traits can be anything from friends and enemies to a good horse or a 
knack for attracting trouble. Whatever is important about your character 
can be a Trait. Though you can word a Trait any way you wish, make sure 
it doesn’t contradict or expand your Story. 

For example, Damart’s Story reads “seeks the means to bring her back to 
life” so a Trait based on that statement could be called “Searching for a way 
to bring his love back from the dead” or “Trying to find a way to raise his 
love from the dead” or something similar. But calling the Trait “Has vast 
knowledge of death magic and resurrection” would not work because the 
Story does not relate any special death-related skills or knowledge. 

Make sure your Traits are specific enough to avoid game conflicts over 
vagueness. For example, Damart is an elemental sorcerer. When he uses 
magic it is elemental magic, not death magic or shooting stars from his 
fingers. Avoid listing Traits as vague as “Magic” or “Scholar”—be specific.

You can assign Bonuses to important traits, in the form of dice. Bonuses 
increase the effectiveness of traits during play. You do not have to assign 
a Bonus to every Trait. To assign a Bonus, spend dice from your starting 
Pool. The cost is the Bonus times itself. Thus, a +2 would cost 4 dice and 
a +3 would cost 9 dice and so on. It is very important to leave some dice in 
your Pool — at least 3 or 4"""

        def example(self) -> str:
            return """\
After writing Damart’s Story, I choose the Traits I want and assign Bonuses 
to them. These Bonuses cost a total of 9 dice, leaving 6 dice in my Pool. 
• Elemental sorcerer of the Lost Land Order +2 
• Outcast of the Lost Land Order 
• He is driven by love +2 
• Searching for the means to raise his love from the dead +1"""

    class CASTING_THE_DICE:
        @property
        def desc(self) -> str:
            return """\
Dice are cast to determine the general outcome of conflicts. This is not 
the same as rolling when you simply want to take an action. The swing of 
a sword can be achieved through simple dialogue with the GM, without 
throwing dice. The effect of a die roll in The Pool is much broader than the 
swing of a sword. 

Anyone can call for a die roll whenever a conflict is apparent or when 
someone wants to introduce a new conflict. Just broadly state your 
intention and roll. 

To win a die roll, roll a 1 on any of the dice you cast. Ignore any other 
results. If you don’t roll a 1, you fail the roll. 
When you roll, the GM will provide 1-3 GM dice to add to the throw. If 
you can show an obvious connection between your intention and one of 
your character’s Traits, you can add Bonus dice to your roll if that Trait 
has a Bonus. 

In addition, you can gamble up to 9 dice from your Pool. Adding dice to 
your roll greatly increases your chances of getting a 1. But if you fail a roll 
you lose all the dice you gambled. A bad throw can instantly reduce your 
Pool to nothing. """

        @property
        def example(self) -> str:
            return """\
Damart is in an ancient library. I want him to find a piece of knowledge 
that will help him on his quest, so I ask for a roll based on the Trait 
“searching for the means to bring his love from the dead +1”. The GM 
hands me 1 GM die (for my +1 Trait) and decides to give me 2 more to roll 
as well (he can give me an extra 1-3, remember). I still have 6 dice in my 
Pool, so I add 4 of them to the roll as a gamble to increase my chances. 

I cast all 7 dice and, luckily, I get a 1. If I had not rolled a 1 I would have lost 
the 4 gambled dice from my Pool, leaving me with only 2"""

    class SUCCESS_AND_FAILURE:
        @property
        def desc(self) -> str:
            return """\
When you roll successfully, you have two options: add a die to your Pool, 
or make a Monologue of Victory. 

If you chose to add a die to your Pool then the GM will narrate a positive 
outcome to the conflict, but he will do so any way he chooses. This 
means things might not go exactly the way you wanted. 

Making a Monologue of Victory (or MOV) is the only way to ensure 
that the conflict results in what you want. Giving an MOV is like taking 
control of the game for a few moments. You can describe your character’s 
actions, the actions of those around him, and the outcome of those 
actions. You can even focus on less direct elements of the conflict such as 
what’s happening in the next room or who’s entering the scene. 

You can do just about anything. In fact, these are the only real limitations 
you must observe: 
    1) Don’t make alterations to the characters of other players (such as killing 
them). You can add complications for them and affect the things 
around them, but don’t intrude on the creation of a fellow player. 
    2) Keep your narration in synch with the established facts and tone 
of the game. If you need to ask the GM questions or prompt the 
other players for responses during your MOV, do so. 
    3) Keep your narration reasonably short. 
Observing these rules of courtesy and continuity will help everyone enjoy 
the game even more. If you ignore these rules, the GM may end your 
MOV at any time. 

If you fail a die roll two things will happen. First, you will lose any dice 
you gambled. Second, the GM will narrate an outcome that is not what 
you intended. The details of the outcome are entirely up to him. He may 
introduce new complications for your character or simply narrate a scene 
that is opposite of what you wanted. """

        @property
        def example(self) -> str:
            return """\
With my successful die roll from the previous example, I choose to give an 
MOV. The GM turns it over to me, everyone listens... 
“After a frustrating couple of hours searching through ancient tomes, 
Damart is ready to give it up. There’s nothing here. But then he notices 
a very strange thing. In a darkened corner a book is leaning against the 
wall. But it isn’t just leaning, its moving! He takes a closer look and the 
book scurries under a table. It can walk! He crawls under the table and 
manages to get his hands on it. The book squirms, but isn’t strong enough 
to break free. On it’s cover are letters from a very old language he has 
some familiarity with. They read ‘Land of the Dead’. There are bloodstains 
on the edges of the pages.” 
I decide that’s a good stopping point. Everyone is very curious about this 
walking book and now the GM resumes control of the game, taking into 
consideration this new element I have just invented. """

    class THE_CONTINUING_STORY:
        @property
        def desc(self) -> str:
            return """\
If you have 9 dice or more left in your Pool at the end of a session, you 
start the next session with the same number. If you have less than that, 
you start the next session with 9 dice in your Pool. 
At the end of each session, you may add up to 15 new words to your 
character’s Story. They can be new lines or additions to old lines. You can 
also save them until the end of the next session and then write a total of 
30 new words. 
You may add new Traits when you choose. You may add or increase 
Bonuses to Traits anytime you wish the same way you did when you 
created your character: the desired Bonus times itself (+2 costs 4 dice, 
+3 costs 9 dice, etc.)."""

    class AT_DEATHS_DOOR:
        @property
        def desc(self) -> str:
            return """\
Your character does not have “hit points” or any other measure of life. 
But he can die. If your character fails a die roll in a situation the GM 
deems utterly lethal, you can either accept death and make a final MOV 
to describe it (no rolling required), or make a final roll to save his life. In 
this roll you cannot use any Traits and the GM cannot grant you any extra 
dice. All dice must be gambled. Your fellow players may pitch in up to 9 
dice each to help your character survive. 
No matter what the outcome of the roll, all the dice you cast are lost--
even dice gambled by other players. 
If you win this roll your character has survived the incident, but you do 
not get a MOV nor do you get to add any dice to your Pool. The GM will 
describe how death was cheated. 
If you fail the roll, your character dies. In this case, you get to make a final 
MOV in which you describe your character’s death in detail. Make it a 
good one."""

    class END_NOTES:
        @property
        def desc(self) -> str:
            return """\
This game was designed more-or-less in a single night back around 
2001 or so. I presented it to the community of the lamentably defunct 
indierpgs.com website and got quite a bit of positive feedback, 
including this from Ron Edwards (Sorcerer): 
“Here is a two-page freebie available on the internet that may be the beginning of 
a whole new wave in RPG design. It presents an amazing concept, astonishingly 
strong, and so pure. My players, hardened RPG veterans, cannot stop gushing 
about it.” 
Here is a video of Ron Edwards delivering a talk about The Pool at the 
University of Milan: Game Designers on Stage YouTube link 
I did eventually develop the system into a finished RPG called The 
Questing Beast, also thanks to much feedback at The Forge. So my 
special thanks goes to Ron Edwards, Scott Knipe, Paul Czege, Mike 
Holmes, Blake Hutchins, Nathan E. Banks, Rene Vernon, Tim Denee 
(and rpg.net), bankuei, David Farmer (and the other folks at Collector 
Comics...now called Little Monsters.), Shawn Martin, James Perrin, 
Phillip Keeney, Dawna Keeney (wink), etc. 
There were many variations of this game created by the RPG 
community as well as some non-English translations (French, Italian 
and Portuguese). I have made these available in a zipped file at 
www.jwarts.com/thepoolvariations.zip. 
I’m always eager to hear about other people’s experiences with The 
Pool. Write a review on one of the great RPG websites, such as rpg.net. 
Or send me an email with your thoughts, comments, criticisms, etc. 
Thanks for checking out The Pool!"""
