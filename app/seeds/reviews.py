from app.models import db, Review


def seed_reviews():

    One = Review(
        rating=4, review="I wish I could go back in time and buy this again.", user_id=1, product_id=1)
    Two = Review(rating=5, review="Best sh*t ever", user_id=2, product_id=2)
    Three = Review(
        rating=1, review="They stole my gold! Don't buy this! It's a scam!", user_id=2, product_id=2)
    Four = Review(
        rating=3, review="Dear fellow conspirators, this item is no good.", user_id=3, product_id=3)
    Five = Review(
        rating=4, review="Great stuff! All praise to his wine and ale", user_id=4, product_id=4)
    Six = Review(
        rating=5, review="May the hair on your feet grow thick and furry.", user_id=5, product_id=5)
    Seven = Review(
        rating=4, review="May the hair on this seller's toes never fall out!", user_id=6, product_id=1)
    Eight = Review(
        rating=2, review="This seller has good manners for THIEF and a LIAR.", user_id=7, product_id=2)
    Nine = Review(rating=1, review="This was actually as bad as a nasty, dirty, wet hole. No, there were no worms or an oozy smell, so I suppose you need to be grateful about the little things in life.", user_id=10, product_id=5)
    Ten = Review(rating=2, review="It was NASTY, DISTURBING and UNCOMFORTABLE! It actually made me late for my second supper. What an awful day twas!", user_id=11, product_id=1)
    Eleven = Review(
        rating=5, review="Is it nice? Yesss. Is it juicy?? Whyyy, yesss it isss! It was scrumptiously crunchable!", user_id=12, product_id=2)
    Twelve = Review(rating=5, review="May the wind under your wings bear you where the sun sails and the moon walks. And yeah you wanna buy this. It's good stuff", user_id=16, product_id=1)
    Thirteen = Review(
        rating=1, review="Gave it a one because I cannot give it a zero. Beware The mines! Beware of the Sea!", user_id=2, product_id=5)
    Fourteen = Review(
        rating=2, review="Highly recommend this sturdy and lightweight sword", user_id=9, product_id=1)
    Fifteen = Review(
        rating=4, review="Sturdy and holds up well in a sword fight. Summer cannot get here soon enough!", user_id=13, product_id=1)
    Sixteen = Review(rating=3, review="You get what you pay for",
                     user_id=14, product_id=1)
    Seventeen = Review(
        rating=4, review="I needed a sword for some fancy adventures. This worked out very well.", user_id=15, product_id=1)
    Eighteen = Review(
        rating=4, review="I needed a sword for my halloween costume and this was perfect. I suppose instead of candy, I could give out gold coins to the little trick of treaters that come to the Lonely Mountain. Oh, I cannot wait to lure them in!", user_id=14, product_id=2)
    Nineteen = Review(rating=5, review="The handle broke clean off the blade with literally just 5 minutes of play from my son. I didn't expect it to last forever but it should have lasted longer than that!", user_id=2, product_id=2)
    Twenty = Review(rating=5, review="Quick delivery, arrived just as pictured!",
                    user_id=2, product_id=2)
    TwentyOne = Review(
        rating=3, review="Made well and not at all flimsy.", user_id=3, product_id=2)
    TwentyTwo = Review(
        rating=2, review="HOW AM I SUPPOSED TO FIGHT WITH THIS?! IT DOES NOT EVEN LOOK COOL! I will be the laughing stock at tomorrow business meeting!", user_id=4, product_id=2)
    TwentyThree = Review(rating=5, review="", user_id=5, product_id=2)
    TwentyFour = Review(
        rating=2, review="Cheap and poor quality. I could have built something better with my eyes closed", user_id=6, product_id=3)
    TwentyFive = Review(
        rating=2, review="Served its purpose, but I wouldn't recommend it.", user_id=7, product_id=3)
    TwentySix = Review(
        rating=2, review="Poor quality, not worth the gold in my opinion.", user_id=8, product_id=3)
    TwentySeven = Review(
        rating=5, review="It has been helping me defend the Old Forest! And I think it goes really well with my yellow boots.", user_id=9, product_id=3)
    TwentyEight = Review(rating=5, review="Hrum, now, well, I am an Ent, or that's what they call me. And I am quite pleased with this sword. While I do not worry about the future, hrumm, I think this sword will last me a long time.", user_id=10, product_id=3)

    TwentyNine = Review(
        rating=5, review="Bought 2 and they are still being played with 3 months later. In fact I used them like a wand as I cast a spell on those silly hobbits", user_id=11, product_id=4)
    Thirty = Review(
        rating=5, review="Great stuff! Held up well in a dagger fight with my neighbours last night!", user_id=12, product_id=4)
    ThirtyOne = Review(rating=4, review="Not Flimsy", user_id=13, product_id=4)
    ThirtyTwo = Review(
        rating=4, review="Completely durable, glad I found it. It covered up the hole in my shiny armour. Not so brave now are we, Bard?!", user_id=14, product_id=4)

    ThirtyThree = Review(
        rating=5, review="Pretty good bang for your gold. It makes nice for a shelf piece", user_id=15, product_id=5)
    ThirtyFour = Review(
        rating=4, review="It has a nice feel to it. I am just starting my collection and this is the first one to arrive that I ordered and I am very happy with it.", user_id=17, product_id=5)
    ThirtyFive = Review(
        rating=2, review="Looks good from a distance but you will not find a duller blade. It could not even cut my herbs with this.", user_id=16, product_id=5)
    ThirtySix = Review(rating=3, review="", user_id=18, product_id=5)

    ThirtySeven = Review(
        rating=3, review="This sword is just a bit hook-y, probably better suited for the orcs.", user_id=19, product_id=6)
    ThirtyEight = Review(rating=5, review="Better then expected, sword is definitely worth the gold!! I am actually shocked that it is as good as it is described. Very sturdy and actually has some weight to it.", user_id=21, product_id=6)
    ThirtyNine = Review(
        rating=4, review="Nice quality sword and shipped quickly. However, I was not expecting an open/used sword.", user_id=20, product_id=6)
    Fourty = Review(
        rating=5, review="It was too small for my liking. My son, Gimli, seems to love it though. - Glóin", user_id=24, product_id=6)
    FourtyOne = Review(
        rating=5, review="It is a funny looking sword. I picked this up for my Halloween costume and did the job.", user_id=23, product_id=6)

    FourtyTwo = Review(rating=5, review="I got this for my best friend who collects falchions because he enjoys anything 'different' and he really likes this. It's super sturdy and the art work is nice!", user_id=22, product_id=7)
    FourtyThree = Review(
        rating=3, review="I know it's not a real collector, but it's pretty cool with the shaft it comes in.", user_id=25, product_id=7)
    FourtyFour = Review(
        rating=2, review="The only metal part in the dagger is the top of the handle that connects to the blade. Not as pictured. Save your gold.", user_id=26, product_id=7)
    FourtyFive = Review(
        rating=5, review="This dagger really matches the axe in my head.", user_id=27, product_id=4)
    # FourtySix = Review(rating=5, review="", user_id=28, product_id=7)
    # FourtySeven = Review(rating=5, review="", user_id=29, product_id=8)
    # FourtyEight = Review(rating=5, review="", user_id=30, product_id=8)
    # FourtyNine = Review(rating=5, review="", user_id=31, product_id=8)
    # Fifty = Review(rating=5, review="", user_id=32, product_id=9)
    # FiftyOne = Review(rating=5, review="", user_id=1, product_id=9)
    # FiftyTwo = Review(rating=5, review="", user_id=2, product_id=9)
    # FiftyThree = Review(rating=5, review="", user_id=3, product_id=9)
    # FiftyFour = Review(rating=5, review="", user_id=4, product_id=10)
    # FiftyFive = Review(rating=5, review="", user_id=5, product_id=10)
    # FiftySix = Review(rating=5, review="", user_id=6, product_id=10)
    # FiftySeven = Review(rating=5, review="", user_id=7, product_id=10)
    # FiftyEight = Review(rating=5, review="", user_id=8, product_id=11)
    # FiftyNine = Review(rating=5, review="", user_id=9, product_id=11)
    # Sixty = Review(rating=5, review="", user_id=10, product_id=11)
    # SixtyOne = Review(rating=5, review="", user_id=11, product_id=11)
    # SixtyTwo = Review(rating=5, review="", user_id=12, product_id=12)
    # SixtyThree = Review(rating=5, review="", user_id=13, product_id=12)
    # SixtyFour = Review(rating=5, review="", user_id=14, product_id=12)
    # SixtyFive = Review(rating=5, review="", user_id=15, product_id=12)
    # SixtySix = Review(rating=5, review="", user_id=16, product_id=13)
    # SixtySeven = Review(rating=5, review="", user_id=17, product_id=14)
    # SixtyEight = Review(rating=5, review="", user_id=18, product_id=14)
    # SixtyNine = Review(rating=5, review="", user_id=19, product_id=14)
    # Seventy = Review(rating=5, review="", user_id=20, product_id=15)
    # SeventyOne = Review(rating=5, review="", user_id=21, product_id=15)
    # SeventyTwo = Review(rating=5, review="", user_id=22, product_id=15)
    # SeventyThree = Review(rating=5, review="", user_id=23, product_id=16)
    # SeventyFour = Review(rating=5, review="", user_id=24, product_id=16)
    # SeventyFive = Review(rating=5, review="", user_id=25, product_id=16)
    # SeventySix = Review(rating=5, review="", user_id=26, product_id=17)
    # SeventySeven = Review(rating=5, review="", user_id=27, product_id=17)
    # SeventyEight = Review(rating=5, review="", user_id=28, product_id=17)
    # SeventyNine = Review(rating=5, review="", user_id=29, product_id=17)
    # Eighty = Review(rating=5, review="", user_id=30, product_id=18)
    # EightyOne = Review(rating=5, review="", user_id=31, product_id=18)
    # EightyTwo = Review(rating=5, review="", user_id=32, product_id=18)
    # EightyThree = Review(rating=5, review="", user_id=33, product_id=18)
    # EightyFour = Review(rating=5, review="", user_id=34, product_id=19)
    # EightyFive = Review(rating=5, review="", user_id=35, product_id=19)
    # EightySix = Review(rating=5, review="", user_id=1, product_id=19)
    # EightySeven = Review(rating=5, review="", user_id=2, product_id=19)
    # EightyEight = Review(rating=5, review="", user_id=3, product_id=20)
    # EightyNine = Review(rating=5, review="", user_id=4, product_id=20)
    # Ninety = Review(rating=5, review="", user_id=5, product_id=20)
    # NinetyOne = Review(rating=5, review="", user_id=6, product_id=20)
    # NinetyTwo = Review(rating=5, review="", user_id=7, product_id=21)
    # NinetyThree = Review(rating=5, review="", user_id=8, product_id=21)
    # NinetyFour = Review(rating=5, review="", user_id=9, product_id=21)
    # NinetyFive = Review(rating=5, review="", user_id=10, product_id=21)
    # NinetySix = Review(rating=5, review="", user_id=11, product_id=22)
    # NinetySeven = Review(rating=5, review="", user_id=12, product_id=22)
    # NinetyEight = Review(rating=5, review="", user_id=13, product_id=22)
    # NinetyNine = Review(rating=5, review="", user_id=14, product_id=22)
    # Hundred = Review(rating=1, review="", user_id=15, product_id=22)
    # HundredOne = Review(rating=4, review="", user_id=16, product_id=23)
    # HundredTwo = Review(rating=5, review="", user_id=17, product_id=23)
    # HundredThree = Review(rating=1, review="", user_id=18, product_id=23)
    # HundredFour = Review(rating=3, review="", user_id=19, product_id=23)
    # HundredFive = Review(rating=4, review="", user_id=20, product_id=24)
    # HundredSix = Review(rating=5, review="", user_id=21, product_id=24)
    # HundredSeven = Review(rating=4, review="", user_id=22, product_id=24)
    # HundredEight = Review(rating=2, review="", user_id=23, product_id=25)
    # HundredNine = Review(rating=1, review="", user_id=24, product_id=25)
    # HundredEleven = Review(rating=5, review="", user_id=25, product_id=25)
    # HundredTwelve = Review(rating=5, review="", user_id=26, product_id=26)
    # HundredThirteen = Review(rating=1, review="", user_id=27, product_id=26)
    # HundredThirteen = Review(rating=1, review="", user_id=28, product_id=26)
    # HundredFourteen = Review(rating=2, review="", user_id=29, product_id=26)
    # HundredFifteen = Review(rating=4, review="", user_id=30, product_id=27)
    # HundredSixteen = Review(rating=3, review="", user_id=31, product_id=27)
    # HundredSeventeen = Review(rating=4, review="", user_id=32, product_id=27)
    # HundredEighteen = Review(rating=4, review="", user_id=33, product_id=27)
    # HundredNineteen = Review(rating=5, review="", user_id=1, product_id=28)
    # HundredTwentyOne = Review(rating=3, review="", user_id=2, product_id=28)
    # HundredTwentyTwo = Review(rating=2, review="", user_id=3, product_id=28)
    # HundredTwentyThree = Review(rating=5, review="", user_id=4, product_id=28)
    # HundredTwentyFour = Review(rating=, review="", user_id=5, product_id=28)
    # HundredTwentyFive = Review(rating=2, review="", user_id=6, product_id=29)
    # HundredTwentySix = Review(rating=2, review="", user_id=7, product_id=29)
    # HundredTwentySeven = Review(rating=5, review="", user_id=8, product_id=29)
    # HundredTwentyEight = Review(rating=5, review="", user_id=9, product_id=29)
    # HundredTwentyNine = Review(rating=5, review="", user_id=10, product_id=29)
    # HundredThirty = Review(rating=5, review="", user_id=11, product_id=29)
    # HundredThirtyOne = Review(rating=4, review="", user_id=12, product_id=30)
    # HundredThirtyTwo = Review(rating=4, review="", user_id=13, product_id=30)
    # HundredThirtyThree = Review(rating=5, review="", user_id=14, product_id=30)
    # HundredThirtyFour = Review(rating=4, review="", user_id=15, product_id=30)
    # HundredThirtyFive = Review(rating=2, review="", user_id=16, product_id=30)
    # HundredThirtySix = Review(rating=3, review="", user_id=17, product_id=31)
    # HundredThirtySeven = Review(rating=3, review="", user_id=18, product_id=31)
    # HundredThirtyEight = Review(rating=5, review="", user_id=19, product_id=31)
    # HundredThirtyNine = Review(rating=4, review="", user_id=20, product_id=31)
    # HundredFourty = Review(rating=5, review="", user_id=21, product_id=31)
    # HundredFourtyOne = Review(rating=5, review="", user_id=22, product_id=32)
    # HundredFourtyTwo = Review(rating=5, review="", user_id=23, product_id=32)
    # HundredFourtyThree = Review(rating=5, review="", user_id=24, product_id=32)
    # HundredFourtyFour = Review(rating=5, review="", user_id=25, product_id=32)
    # HundredFourtyFive = Review(rating=5, review="", user_id=26, product_id=33)
    # HundredFourtySix = Review(rating=5, review="", user_id=27, product_id=33)
    # HundredFourtySeven = Review(rating=5, review="", user_id=28, product_id=33)
    # HundredFourtyEight = Review(rating=5, review="", user_id=29, product_id=33)
    # HundredFourtyNine = Review(rating=5, review="", user_id=30, product_id=13)
    # HundredFifty = Review(rating=5, review="", user_id=31, product_id=13)
    # HundredFiftyOne = Review(rating=5, review="", user_id=32, product_id=13)
    # HundredFiftyTwo = Review(rating=5, review="", user_id=33, product_id=13)
    # HundredFiftyThree = Review(rating=5, review="", user_id=, product_id=)
    # HundredFiftyFour = Review(rating=5, review="", user_id=, product_id=)
    # HundredFiftyFive = Review(rating=5, review="", user_id=, product_id=)
    # HundredFiftySix = Review(rating=5, review="", user_id=, product_id=)
    # HundredFiftySeven = Review(rating=5, review="", user_id=, product_id=)
    # HundredFiftyEight = Review(rating=5, review="", user_id=, product_id=)
    # HundredFiftyNine = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixty = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtyOne = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtyTwo = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtyThree = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtyFour = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtyFive = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtySix = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtySeven = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtyEight = Review(rating=5, review="", user_id=, product_id=)
    # HundredSixtyNine = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventy = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventyOne = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventyTwo = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventyThree = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventyFour = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventyFive = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventySix = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventySeven = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventyEight = Review(rating=5, review="", user_id=, product_id=)
    # HundredSeventyNine = Review(rating=5, review="", user_id=, product_id=)
    # HundredEighty = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightyOne = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightyTwo = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightyThree = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightyFour = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightyFive = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightySix = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightySeven = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightyEight = Review(rating=5, review="", user_id=, product_id=)
    # HundredEightyNine = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinety = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetyOne = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetyTwo = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetyThree = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetyFour = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetyFive = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetySix = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetySeven = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetyEight = Review(rating=5, review="", user_id=, product_id=)
    # HundredNinetyNine = Review(rating=5, review="", user_id=, product_id=)

    db.session.add(One)
    db.session.add(Two)
    db.session.add(Three)
    db.session.add(Four)
    db.session.add(Five)
    db.session.add(Six)
    db.session.add(Seven)
    db.session.add(Eight)
    db.session.add(Nine)
    db.session.add(Ten)
    db.session.add(Eleven)
    db.session.add(Twelve)
    db.session.add(Thirteen)
    db.session.add(Fourteen)
    db.session.add(Fifteen)
    db.session.add(Sixteen)
    db.session.add(Seventeen)
    db.session.add(Eighteen)
    db.session.add(Nineteen)
    db.session.add(Twenty)
    db.session.add(TwentyOne)
    db.session.add(TwentyTwo)
    db.session.add(TwentyThree)
    db.session.add(TwentyFour)
    db.session.add(TwentyFive)
    db.session.add(TwentySix)
    db.session.add(TwentySeven)
    db.session.add(TwentyEight)
    db.session.add(TwentyNine)
    db.session.add(Thirty)
    db.session.add(ThirtyOne)
    db.session.add(ThirtyTwo)
    db.session.add(ThirtyThree)
    db.session.add(ThirtyFour)
    db.session.add(ThirtyFive)
    db.session.add(ThirtySix)
    db.session.add(ThirtySeven)
    db.session.add(ThirtyEight)
    db.session.add(ThirtyNine)
    db.session.add(Fourty)
    db.session.add(FourtyOne)
    db.session.add(FourtyTwo)
    db.session.add(FourtyThree)
    db.session.add(FourtyFour)
    db.session.add(FourtyFive)
    # db.session.add(FourtySix)
    # db.session.add(FourtySeven)
    # db.session.add(FourtyEight)
    # db.session.add(FourtyNine)
    # db.session.add(Fifty)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()
