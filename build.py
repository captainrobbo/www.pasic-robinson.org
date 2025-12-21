import glob
import os

import preppy
import yaml

# MAIN_PIC = "2016/images/08_bergamo/IMG_C5199.jpg"
MAIN_PIC = "2025/images/muscle.jpg"
MAIN_TEXT = """
2025 is "in development" on 17-19 Dec, check back in a couple of days!
"""
GALLERIES_BY_YEAR = {
    "2025": [
        dict(title="Lima, Peru",
            imagedir="latam",
            captions={},
            imagelist=[],
            description="""
            In late January we set off for a tour of Latin America.  
            We flew into Sao Paolo, then on to 
            Lima, Cusco and Macchu Picchu and Arequipa in Peru;  
            Santiago in Chile; then across the Amdes from Puerto Montt to Bariloche in Argentina; 
            then Mendoza, Buenos Aires and back via Sao Paolo!  
            This page just covers Lima - later stages are in the side menu.
            """),
        dict(title="Cusco and Macchu Picchu, Peru",
            imagedir="latam2",
            captions={},
            imagelist=[],
            description="""
            Cusco, the Sacred Valley and Macchu Picchu
            """),
        dict(title="Arequipa, Peru",
            imagedir="latam3",
            captions={},
            imagelist=[],
            description="""
            Arequipa, the White City
            """),
        dict(title="Chile",
            imagedir="latam4",
            captions={},
            imagelist=[],
            description="""
            Chile:  Santiago, Maipo Valley, Valparaiso + Vina del Mar, then south to Patagonia to cross the Andes by bus...
            """),
        dict(title="Bariloche, Argentina",
            imagedir="latam5",
            captions={},
            imagelist=[],
            description="""
            The Chamonix of the southern hemisphere...
            """),
        dict(title="Mendoza",
            imagedir="latam6",
            captions={},
            imagelist=[],
            description="""
            Mendoza in Argentina. Steak and wine!
            """),
        dict(title="Buenos Aires",
            imagedir="latam7",
            captions={},
            imagelist=[],
            description="""
            Buenos Aires, the Paris of the south...
            """),
        dict(title="Monaco / Nice",
            imagedir="monaco",
            captions={},
            imagelist=[],
            description="""
            Work with World Athletics, but some time to explore as well...
            """),
        dict(title="Porto",
            imagedir="porto",
            captions={},
            imagelist=[],
            description="""
            Porto
            """),
        dict(title="Bahamas",
            imagedir="bahamas",
            captions={},
            imagelist=[],
            description="""
            30th anniversary trip to Bahamas
            """),
        dict(title="Croatia",
            imagedir="croatia",
            captions={},
            imagelist=[],
            description="""
            Usual summer expedition
            """),
        dict(title="Alisa's 60th birthday",
            imagedir="birthday",
            captions={},
            imagelist=[],
            description="""
            Alisa's 60th birthday
            """),
        dict(title="Sardinia",
            imagedir="sardinia",
            captions={},
            imagelist=[],
            description="""
            Sardinia
            """),
        dict(title="Puglia",
            imagedir="puglia",
            captions={},
            imagelist=[],
            description="""
            Puglia en route to San Marino
            """),
        dict(title="San Marino",
            imagedir="sanmarino",
            captions={},
            imagelist=[],
            description="""
            Athtech in San Marino
            """),
        dict(title="Madeira",
            imagedir="madeira",
            captions={},
            imagelist=[],
            description="""
            Madeira EMACS
            """),
        dict(title="Dominican Republic",
            imagedir="dominican",
            captions={},
            imagelist=[],
            description="""
            Family holiday in DR
            """),
    ],
    "2024": [
        dict(title="Vietnam and Cambodia",
            imagedir="01_jan",
            captions={},
            imagelist=[],
            description="""
            Our month-long adventure in Vietnam and Cambodia
            """),
        # dict(title="Nice",
        #     imagedir="02_nice",
        #     captions={},
        #     imagelist=[],
        #     description="""
        #     Meeting in Monaco, couple of days in Nice
        #     """),
        dict(title="World Cross Country",
            imagedir="03_mar",
            captions={},
            imagelist=[],
            description="""
            Watching the World Cross in scorching hot Belgrade.  My system runs athletics in Serbia,
            and we were fortunate to be invited as guests of the local organisers and World Athletics.
            """),
        dict(title="California",
            imagedir="04_apr",
            captions={},
            imagelist=[],
            description="""
            Kyle's wedding, San Diego, LA and Palm Springs 
            """),
        dict(title="Sicily",
            imagedir="05_may",
            captions={},
            imagelist=[],
            description="""
            Sicily
            """),
        dict(title="Running adventures",
            imagedir="06_jun",
            captions={},
            imagelist=[],
            description="""
            Bannister Miles and the UK Ekiden
            """),
        dict(title="European road trip",
            imagedir="07_jul",
            captions={},
            imagelist=[],
            description="""
            A month on the coast, down and back again
            """),
        dict(title="Santorini",
            imagedir="09_sep",
            captions={},
            imagelist=[],
            description="""
            4 days seeing the volcano
            """),
        dict(title="Napoli + Amalfi Coast",
            imagedir="10_oct",
            captions={},
            imagelist=[],
            description="""
            Napoli, Amalfi, Sorrento, Pompeii
            """),
        dict(title="Macedonia and Greece",
            imagedir="11_mac",
            captions={},
            imagelist=[],
            description="""
            European Convention in Skopje, Meteora and Thessaloniki
            """),
        dict(title="Madeira",
            imagedir="11_nov",
            captions={},
            imagelist=[],
            description="""
            Combining business and pleasure
            """),
        dict(title="La Romana",
            imagedir="12_dec",
            captions={},
            imagelist=[],
            description="""
            Our traditional week of sun and relaxation
            """),
        dict(title="Friends and Family",
            imagedir="13_misc",
            captions={},
            imagelist=[],
            description="""
            Various things throughout the year
            """),


    ],

    "2023": [
        dict(title="January - Spain",
            imagedir="01_jan",
            captions={},
            imagelist=[],
            description="""
            New Year in Spain - San Pedro with family, then two nights in Alicante
            """),
        dict(title="January - Dominican Republic",
            imagedir="01a_dr",
            captions={},
            imagelist=[],
            description="""
            Our annual week in the Caribbean
            """),
        dict(title="February",
            imagedir="02_feb",
            captions={},
            imagelist=[],
            description="""
            Our last ski in Chamonix; Sasha's birthday in London
            """),
        dict(title="March",
            imagedir="03_mar",
            captions={},
            imagelist=[],
            description="""
            A week in the Cape Verde islands; Dubrovnik (while we supervised builder in Duboka repair)
            """),
        dict(title="April",
            imagedir="04_apr",
            captions={},
            imagelist=[],
            description="""
            Thames Hare & Hounds annual dinner; Champagne tour with the Johnsons
            """),
        dict(title="May",
            imagedir="05_may",
            captions={},
            imagelist=[],
            description="""
            Canvey Island with Tom and Julie; Varsity Athletics Match in Cambridge, Iffley Miles and weekend in Oxford, jetwashing a patio; then a week in Turkey for our anniversary
            """),
        dict(title="June",
            imagedir="06_jun",
            captions={},
            imagelist=[],
            description="""
            Evian with friends, last trip to Chamonix, and the Cinque Terre; Oxford & Cambridge versus Penn and Cornell and dinner in St. Hilda's College, Oxford
            """),
        dict(title="July",
            imagedir="07_jul",
            captions={},
            imagelist=[],
            description="""
            The long drive south:  Frankfurt visiting Deutsche Börse, Ulm, Austria, Levico Terme, Prosecco, and then meeting the gang in Duboka
            """),
        dict(title="Tefika's 85th birthday",
            imagedir="07a_85th",
            captions={},
            imagelist=[],
            description="""
            Family gathering in a villa in Stolac, Herzegovina, for Tefika's 85th birthday party. Beautiful rivers, Turkish architecture, barbecues and lounging; local music star Bozo Vreco
            """),
        dict(title="August",
            imagedir="08_aug",
            captions={},
            imagelist=[],
            description="""
            Croatia. Then the long drive back:  Giovanni's amazing towns and vineyards in Friuli Venezia Giulia, Verona, Monto Bondone above Trento; Lindau; Strasbourg
            """),
        dict(title="September",
            imagedir="09_sep",
            captions={},
            imagelist=[],
            description="""
            Amsterdam for aister Arifa's 50th party; organising the Athtech conference in Malta
            """),
        dict(title="October",
            imagedir="10_oct",
            captions={},
            imagelist=[],
            description="""
            Richmond by the river; the Thames clubhouse; visiting David and Naomi Tomkys (and her anazing art) in Cambridge
            """),
        dict(title="November",
            imagedir="11_nov",
            captions={},
            imagelist=[],
            description="""
            Visit to Athletics Gibraltar, tours of the rock (inside and out), and a day in Vejer de la frontera and Cadiz
            """),
        dict(title="December",
            imagedir="12_dec",
            captions={},
            imagelist=[],
            description="""
            Varsity Cross Country Match; dinner at the Houses of Parliament; our week in Mexico; and  London lights
            """),
    ],

    "2022": [
        dict(title="January",
            imagedir="01_jan",
            captions={},
            imagelist=[],
            description="""
            A night out in London before they took the lights down;
            walk in Richmond Park;
            and back to Madeira for their Masters athletics meeting
            """),
        dict(title="February",
            imagedir="02_feb",
            captions={},
            imagelist=[],
            description="""
            DNA athletics in Glasgow, Edinburgh; Bryan's 50th; Skiing with the Moons family;
            """),
        dict(title="March",
            imagedir="03_mar",
            captions={},
            imagelist=[],
            description="""
            Harry's travels to South America; 
            Thames Hare and Hounds annual dinner;
            Riverside; Cyprus
            """),
        dict(title="April",
            imagedir="04_apr",
            captions={},
            imagelist=[],
            description="""
            Croatia trip to Builder; Makarska, Osejava, Royal View in Split
            """),
        dict(title="May",
            imagedir="05_may",
            captions={},
            imagelist=[],
            description="""
            Varsity Athletics, Peak District
            """),
        dict(title="June",
            imagedir="06_jun",
            captions={},
            imagelist=[],
            description="""
            Builder: Sarajevo, Zenica, Bugojno, Duboka
            """),
        dict(title="July",
            imagedir="07_jul",
            captions={},
            imagelist=[],
            description="""
            In July we drove South. The plan was to work remotely from the new beach house for a few weeks.
            Half the fun is the journey, so we took it slowly with night stops in Epernay, Alsace, Zurich and Bassano del Grappa
            """),
        dict(title="Munich Athletics",
            imagedir="08a_munich",
            captions={},
            imagelist=[],
            description="""
            On the way back Andy's work took us to Munich for the European Athletics Championships.  A wonderful city and amazing sport
            """),
        dict(title="August",
            imagedir="08_aug",
            captions={},
            imagelist=[],
            description="""
            The new bridge took us over to Orebic, when not taking shortcuts with Captain Morgan and family.  South to Trebinje in Bosnia for a few days. 
            Then the drive back!  By amazing luck, met Martyn Bowen and Nina in Primošten on the Croatian coast for lunch.  Then north to Trieste, Grado, Ljubljana and Slovenia with Alisa's friend Lila; 
            then Neuschwanstein castle, before the Munich athletics which has its own page.
            """),
        dict(title="September",
            imagedir="09_sep",
            captions={},
            imagelist=[],
            description="""
            Amsterdam for Aletta's birthday and the  Dam to Dam race; various family gatherings; Balliol Gaudy
            """),
        dict(title="October",
            imagedir="10_oct",
            captions={},
            imagelist=[],
            description="""
            London, Malmo to see Alisa's Mum, Tallinn for the European Athletics convention, and Riga on the way home
            """),
        dict(title="November",
            imagedir="11_nov",
            captions={},
            imagelist=[],
            description="""
            Treated by Tim with tickets to Abba Voyage!  An aging athletes heart study. Cross country.  ReportLab reunions. Then three days in Nice around an IT conference
            """),
        dict(title="December",
            imagedir="12_dec",
            captions={},
            imagelist=[],
            description="""
            Varsity XC and Thames' new World Heritage plaque; Balkan Athletics meeting in Athens and a tour of Pelepponese; Thames carols run
            """),
    ],

    "2021": [
        dict(
            title="Building",
            description="""Our year has been dominated by buildings, and problems with them.
            After herculean efforts doing two complete renovations, both boys are now on the property ladder, each in a 2 bedrooom
            flat near Vauxhall and sharing with friends.   We nearly killed ourselves, twice
            over, for 3 months each, trying to coordinate renovations during the pandemic,
            and ended up doing way too much of it ourselves as successive builders vanished.<br>
            Luckily, friends helped out - Tom helping us fix brickwork up a scaffold and advising
            throughout on pipes and plumbing.<br><br>
            Then there's the saga of the beach house in Croatia, with it's 1980s plumbing and wiring;
            after years talking about it, we hope the renovation is happening.  We spent 3 exhausting
            days clearing out 4 decades of clutter and old furniture.<br><br>
            Meanwhile at home we had damp problems with the neighbours' drive against our wall, which
            took forever to resolve and caused us a lot of stress (as well as damage to our study wall).
            We also had to dig a hole in the kitchen floor (mercifully finding the sagging tiles were a
            broken timber and not damp-rot).    Our own home still awaits serious attention, 
            with a new kitchen and rear needing doing in 2022 or 2023, but we can't face that just now. 
            <br><br>
            And we all have some skills we did not a year ago...
            """,
            imagedir="building",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Harrogate",
            description="""Lockdown had eased enough to travel, so we had a meeting in York followed
            by a night in Harrogate on our 26th anniversary.  It was our first time and we were very impressed
            with the town, and its beautiful neighbour Knaresborough.  The wired-up busker at Kings Cross was
            social-distancing in a highly lucrative manner!<br><br>

            On the way back, a signal failure stopped us in Peterborough, and rather than risking an all-night wait,
            we booked a local hotel and saw their lovely cathedral and town square.  I'm not quite sure why it
            was voted the most boring town in Britain - we found it quite pleasant - although the 'rush-hour' to
            London the next morning had its entire youthful population heading to town to get drunk.
            """,
            imagedir="harrogate",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Croatia 1 - August",
            description="""
            August saw one of our best Croatian holidays ever.  This summer, we really saw all the best bits
            <br><br>
            By August, everyone was vaccinated and travel could resume.  First priority was to get Alisa's mum
            (who had spent 18 months alone in her apartmet in Sweden) down to the seaside, and give her some company.
            <br><br>
            We left London in pouring rain, and 3 hours later we were in beautiful Trogir enjoying the old
            town.  The next day, Roko and Snjezana picked us up, we headed into Bosnia (with the obligatory
            amazing meal by a lake), and caught up with Tefika.  Andy was able to get his Tokyo Olympics fix on
            wifi over 3-Euro gourmet breakfasts while Alisa saw all the friends and relatives.  Then we high-tailed it
            to the beach house, after a quick pause to get our noses tested before crossing the border back into the EU.

            <br><br>
            Duboka was as calm and beautiful as ever.  All our usual friends rolled in from aroundd Europe.
            Sasha and Lela coached Andy in the fine local skill of lunchtime Rakija-tasting and having a siesta
            on the terrace their dad built.
            <br><br>
            After two weeks, we bid farewell to Tefika, and decided to see the Croatia all the tourists see -
            something we had not really down.  Two nights and a boat trip (with 100 hard-partying Polish students) 
            in Makarska, a stop in Split to meet the organiser of next month's AthTech conference and plan, and
            two more nights on the waterfront in Trogir by the airport capped off an amazing 20 days.


            """,
            imagedir="cro1",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Croatia 2 - Conference",
            description="""
            In September, Andy was co-chairing an international athletics conference in Zadar, a few
            hours up the Croatian coast from where we normally stay.  People from most countries in Europe
            flew in, and it was the best yet in this conference series.<br><br>
            After a crazy week of non-stop work, we had a day in Split with the co-organiser, Nicolas, 
            and his wife Samantha; and then met Elif and Mel to unwind and show them around.
            """,
            imagedir="cro2",
            captions= {
            },
            imagelist= [
            ]
        ),
        # dict(
        #     title="Cro 3 - Clearout",
        #     description="""The beach house is crumbling, and we finally decided to deal with it.
        #     Since builders don't work in summer, we had to fly back in October for 3 days of clearing
        #     out, destruction, and discussions with the builder.
        #     """,
        #     imagedir="croatia3",
        #     captions= {
        #     },
        #     imagelist= [
        #     ]
        # ),

        dict(
            title="Madeira",
            description="""Andy's athletics business gave us a chance to see this island
            for the first time.  An amazing place, combining a sophisticated European city,
            sub-tropical climate, incredible views (like the 640m straight down below),
            food and wine - we will be back again many times.""",
            imagedir="madeira",
            captions= {
            },
            imagelist= [
            ]
        ),

        dict(
            title="Jamaica",
            description="A week before Christmas, we escaped for a proper week of holiday in Jamaica",
            imagedir="jamaica",
            captions= {
            },
            imagelist= ['bargirl.jpeg', 'jerkhut.jpg', 'punishment.jpg', 'runner.jpeg', 'sleigh.jpeg', 'sunset2.jpg', 'beach.jpg', 'noganja.jpeg', 'reggae.jpg', 'sailing1.jpeg', 'smiley.jpg', 'sunset3.jpg', 'inverted.jpeg', 'poolsnacks.jpeg', 'rickspool.jpeg', 'sailing2.jpeg', 'sunset.jpg'
            ]
        ),

        dict(
            title="Adventures",
            description="Many fun and interesting moments from 2021",
            imagedir="misc",
            captions= {
            },
            imagelist= [
                
            ]
        ),



        ],



    "2020": [
        dict(
            title="25th Wedding Anniversary",
            description="""We should have been swimming with pigs in the Bahamas :-( 
            Instead, we did the best we could with a punting trip in Oxford, where we were married.  <br><br>
            Then we looked at some old albums.
            """,
            imagedir="wedding",
            captions= {
            },
            imagelist= [
                # 'wedding_1.jpeg',
                # 'wedding_2.jpeg',
                # 'wedding_3.jpeg',
                # 'wedding_4.jpeg',
                # 'wedding_5.jpeg',
                # 'wedding_6.jpeg',
                # 'wedding_7.jpeg',
                # 'wedding_8.jpeg',
                # 'wedding_9.jpeg',
                # 'wedding_10.jpeg',
                # 'wedding_11.jpeg',
                # 'wedding_12.jpeg',
                # 'wedding_13.jpeg',
            ]
        ),
        dict(
            title="Harry's Graduation",
            description="""
            Harry still hasn't had a proper graduation, as Bristol is waiting for normality
            to resume. He had a rough final year at uni, with the first term ruined by a
            teacher's strike, and the spring and summer by the pandemic.

            We went to pick him up at the end of university.
            """,
            imagedir="graduation",
            captions= {
            },
            imagelist= [
            ]
        ),

        dict(
            title="A strange year...",
            description="""
            This was a year like none other.    The pandemic made us all do things differently.  An endless perfect summer, deer in the park, rivers
            and vineyards inland beaches, our home gym, zoom fitness classes...
            """,
            imagedir="misc",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Spain",
            description="""
            The moment it was allowed, at the start of June, we got on the first plane to Spain, where Aljosa (Alisa's brother) had
            bought a house by the seaside in San Pedro del Pinatar.  The cunning devil managed to spend lockdown
            there instead of in Madrid, and it took a few months for his bosses to realise.  
            <br><br>
            It's a beautiful area with historic cities, deserted beaches, bike paths and cafes by the sea - and 
            a delightful terrace to relax on. We spent six days in heaven after the locked-down spring at home.
            """,
            imagedir="spain",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Greece",
            description="""Our usual Croatian summer wasn't going to happen, so we took a week's package
            to Kalamata in Greece in August.  It's a novely spending a week in a nice hotel in August,
            rather than fixing up the family beach house and doing it all ourselves.
            <br><br>
            We had two excursions - one driving down into the wild and historic Mani, and one to ancient Messini, the best preserved
            ruins in Greece, just down the road
            """,
            imagedir="greece",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Italy",
            description="""Right at the end of summer, when rules were changing every Friday, we combined
            some business in Treviso just north of Venice, and a wedding in the beatiful Prosecco hills.
            At the end Harry flew out and we spent 24 hours exploring Venice itself - the main island and the Lido. 
            This was a once-in-a-lifetime
            chance to see it without massive crowds and with reasonable prices! 
            """,
            imagedir="italy",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Cuba",
            description="""
            After constant cancellations and rearrangements, a window amazingly opened for a proper
            family holiday - in Cuba!  We flew out for a week returning on Christmas Day.  Cuba, uniquely,
            tested everyone on landing, and the 98% of tourists who were negative got to enjoy a week in
            paradise.  The unlucky ended up in a military hospital, which added a frisson of excitement
            to the journey!

            A beautiful country full of incredibly nice, smart, educated and organised people stuck in
            a tough situation.  Havana was spectacular,
            as was the car for our day trip.   Beaches and the hotel were perfect.  
            """,
            imagedir="cuba",
            captions= {
            },
            imagelist= [
            ]
        ),

        ],
    "2019": [
        dict(
            title="Andy's Stroke",
            description="""
            The year started with a shock:  I (Andy) collapsed with a major stroke on Sat 19th Jan
            while drinking my morning coffee,
            and was unable to move or speak for a couple of days.  Fortunately Alisa was watching,
            the roads were quiet and the ambulance got to us and then took me to St. George's Hospital in record time.
            Fortunately, after a couple of days things started to improve rapidly.
            <br><br>
            Apparently, a small part of my brain is now dead.  I am convinced it's the part that does
            the gardening.
            <br><br>
            I took rehab fairly seriously and have got back to full strength and almost full coordination.
            Any drop in my running speed probably has more to do with age, food and taking things easy
            than anything sinister!
            """,
            imagedir="stroke",
            captions= {
            },
            imagelist= [
            'IMG_0727.jpg', 
            'IMG_0726.jpg', 
            ['IMG_0732.jpg', """
                Mike's friend Brett at the Ledbury restaurant in Notting Hill sent us an amazing hamper 
                as a get-well-soon gift.  Too much Michelin-starred cuising was "enjoyed" by Alisa and her mum 
                while I was in hospital, but they did smuggle me some stuff in, and I got discharged in time 
                to polish off what remained.  Thanks, Brett!"""],
            ['rehab.jpg', """
                We already had a trip to the Alps arranged, scheduled for a few weeks after it happened. 
                I was still very wobbly and in no shape to hurtle down a mountainside, so decided to try cross 
                country for the first time in 30 years!
                When the doc agreed, but he probably didn't know pistes have corners, which were 'challenging'
                """],
            ['IMG_0807.jpg', """
                I'm now on blood thinners, which make you bruise quite impressively when you fall
                and land on ice...even despite the layer of padding I had developed in the preceding couple of years.
                """],
            ['IMG_0123.jpg', """
                Alisa had also booked a birthday treat for me - a trip to St. Lucia in late March, where we had honeymooned.
                My 'balance challenge' was carrying this up 3 floors from the bar without spilling a drop!
                I highly recommend beach holidays to anyone in the same position - ping pong, pool volleyball, and 
                yoga classes are exactly what you need to get movement skills right again. And it was
                and ex-Saga hotel, so I actually got to compare stroke stories and medicines with the people on the deck
                chairs to my left and my right!
                """],
            ['IMG_0164.jpg', """
                After ten weeks very serious focus on getting fit, I was able to trot slowly around
                my club's end-of-season five-mile handicap.
                """],
            ['back_on_track.jpg', """
                You're supposed to seek out new challenges for your coordination.  So at the end of April,
                I entered the Southern Vets League 100m, managing to come last - but only by the thickness
                of a vest - in 15.0 seconds.  Any good coach would be horrified by my form, but I'm
                incredibly grateful and lucky to have ended up 'normal' again, albeit a bit slower.
                Then again, maybe it's just age!
                """]
            ]
        ),
        dict(
            title="Tim's Graduation",
            description="""
            Tim graduated from University College, London, on 1st September, making us all very proud.
            No wild partying though - this was also supposed to be the day he started work, so after 
            a quick celebration at the Royal Festival Hall, he jumped on a train for his induction week at
            a country house hotel.  He has joined 
            a multinational accounting firm as a trainee Auditor.  (At the time of writing' he's just 
            passed his first professional accounting exam - two and a half more years of study to go!)
            """,
            imagedir="timgrad",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Alps",
            description="""
            We had a few short days in the Alps with Tim, as Andy was recovering.  A little skiing, and a lot of sun (and cakes!)
            """,
            imagedir="alps",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="At Home",
            description="""
            Some wonderful moments from throughout the year at home
            """,
            imagedir="staycation",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="St.Lucia",
            description="""
            My birthday trip to St. Lucia, 24 years after we honeymooned there.
            """,
            imagedir="stlucia",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Harry",
            description="""
            Harry seems to have had way more fun than is normal for a final year student!
            He worked as a security guard at Wimbledon Tennis, passed his driving test and
            borrowed our car to impress his mates.  He has a big shared house
            in Bristol where they apparently host frequent dinner parties.
            """,
            imagedir="harry",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Istanbul",
            description="""

            We were in Sarajevo in late May working with the Bosnian athletics federation, 
            so made the short hop to Istanbul 
            to meet some people.  It happened to coincide with our 24th anniversary,
            so the hotel had a little surprise for us. Wow!
            """,
            imagedir="istanbul",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Marmaris",
            description="""
            We managed one week together as a family in mid June,
            and went to Marmaris in Southern Turkey.  Amazing
            coastline and really well organised town with miles
            of beautiful coastal walks.
            """,
            imagedir="marmaris",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Hillside",
            description="""
            In October we had a week of pure holiday with some Anglo-Turkish
            friends at the magical Hillside Beach Resort
            in Fethiye
            """,
            imagedir="hillside",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Rhodes",
            description="""
            In our week in Marmaris, we took a ferry to Rhodes for the day.
            Andy had been a couple of times, 40 years earlier. A beautiful
            old town with castles and a great urban beach
            """,
            imagedir="rhodes",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Euro Tour - Alsace",
            description="""
            We travelled south in July via Strasbourg and the vineyards
            of Alsace, which we saw in traditional French fashion on 
            bicycles.  And, at the very end on the way back, we stayed in
            the amazing Nancy and watched the light show at Place Stanislas
            """,
            imagedir="alsace",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Euro Tour - Switzerland",
            description="""
            We drove through Switzerland on the way South, and back later on.
            We are very lucky to have great friends in the nicest suburb of
            Zurich, so we barbecued by and swam in the lake, as well as exploring
            the beautiful Old Town.
            """,
            imagedir="switzerland",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Euro Tour - Italy",
            description="""
            Om the way south, we had a stunning night at an Italian lake,
            and another in Trieste, which has the most stunning public square
            in Italy and definitely the best street bands.  Coming back
            we stopped in Padua, Mantua and Lake Maggiore.  We really have seen
            the best of Italy this summer...
            """,
            imagedir="italy",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Euro Tour - Croatia",
            description="""
            We thought we'd show some pics of other parts, not our
            usual beach village which we show every year.
            We were lucky to see Brela and Baska Voda on 1st June,
            before the crowds came - our reward from a couple of days
            crazy work trying to stabilize the family beach house.
            And on our last night at end of season, we stayed in Opatija,
            the Habsburg's version of Monaco...
            """,
            imagedir="croatia",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Euro Tour - Bosnia",
            description="""
            We've been in Bosnia a few times this year.  When Andy was out with
            the Athletics Federation in May, Alisa met
            her old college friend; then in August, they took us out 
            and also showed us their mountains and ski slopes.   And, on the way
            home, we drove out inland, through an amazing canyon
            """,
            imagedir="bosnia",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Euro Tour - Nancy",
            description="""
            On the way home we had a meeting in Nancy, a city we had never seen
            before.  It turned out to be a beautiful town with an amzing square
            and sound-and-light show
            """,
            imagedir="nancy",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Abu Dhabi",
            description="""
            We had some meetings in Abu Dhabi at beginning of December, and a day to relax after.
            What a beautiful city!  We rode bikes down the Corniche, Andy ran in the local 5k,
            and had a couple of great evenings enjoying the beach just yards from where all
            the work gets done.
            """,
            imagedir="abudhabi",
            captions= {
            },
            imagelist= [
            ]
        ),
        ],
    "2018": [
        dict(
            title="Algarve and Seville",
            description="""
            Waking up on New Year's Day to the sound of birds and the lovely sunshine is such 
            a contrast to the (usually) grey and wet welcome we would have had at home. We
            were very lucky to be able to explore Algarve and Seville on the way back in
            glorious sunshine, after a family gathering in Castro Marim
            """,
            imagedir="portugal",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Thailand and Malaysia",
            heading="Tefika's Asian Tour",
            description="""
            Tefika's big adventure and 80th birthday trip coincided with Tim's winter break 
            from Seoul National University, where he was on an exchange.  She was planning to
            ask Tim to accompany her on her SE Asian tour but in the end we joined them too.
            Having 3 generations together had its challenges.
            We explored Bangkok, relaxed in Hua Hin and flew down to KL to see the Petronas Towers.
            """,
            imagedir="thailand",
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Mexico",
            heading="Mexico in March",
            imagedir="mexico",
            description="""
            Andy's 52nd birthday treat was a surprise week in an all-inclusive resort near Cancun.
            Highlights included St Patrick's Day, mexican style, and exploring the ruins of Tulum.
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Malta",
            heading="Malta, April",
            imagedir="malta",
            description="""
            A business visit to Malta (the Malta Athletics Federation is a customer of ours) 
            provided us with an opportunity to do a bit of tourism. It was a first visit for
            Andy and a return for Alisa after 27 years.
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="London",
            heading="London in the summer",
            imagedir="london",
            description="""
            This was the best summer anyone can remember, and London was at its best.  
            Highlights included royal wedding parties, dining by the Thames, and just
            plain enjoying the garden.
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Serbia and Danube",
            heading="Serbia and the Danube",
            imagedir="serbia",
            description="""
            At the end of May we went to Belgrade, and drove out to the Iron Gorges on the
            Danube - the narrowest and most scenic point.  Spectacular views
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Korea",
            heading="Korea",
            imagedir="korea",
            description="""
            Tim was finishing his exchange year at Seoul National University, so we flew out to
            join him and explore.  We spent a week seeing Seoul, and 3 nights on Jeju Island,
            their (slightly smaller) version of Hawaii.
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Euro Tour Phase 1",
            heading="Euro Tour Phase 1",
            imagedir="heidelberg",
            description="""
            A long drive to Croatia but we managed to fit in business meetings, tourism and
            seeing friends on the way there.  We stopped in Metz, Heidelberg, the Black
            Forest and Zurich
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Phase 2: Croatia",
            heading="Croatia",
            imagedir="croatia",
            description="""
            Croatia was as perfect as ever, with family gathering at the beach house, and side trips
            to Split and Dubrovnik.  We took some short trips inland to Bosnia to see Mostar, and swim in the
            waterfalls at Kravice.  Alisa's friend Ela came back for the first time in 30 years.
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Phase 3: Bosnia",
            heading="Bosnia",
            imagedir="bosnia",
            description="""
            All the family gathered for Tefika's 80th birthday, in a ski lodge up the hill from
            Bugojno...
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Intermission: Berlin",
            heading="European Athletics Championships in Berlin",
            imagedir="berlin",
            description="""
            We interrupted the summer hols to fly up to Berlin,
            where Andy was working very hard at the European Championships. The perk was a chance
            to see the City as well as one of the best athletics championships ever held.
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Phase 4: Italy",
            heading="Italy",
            imagedir="italy",
            description="""
            Homeward bound, we drove through Italy from East to West.  Starting with the
            fishing port of Muggia on the Slovenian border, we stayed in a hilltop above
            Vicenza, had meetings in Milan, then the beautiful Lido Palace on Lake Maggiore, where Churchill
            honeymooned and the Pope and Queen Mum have stayed - poossibly the best view
            we have ever had.   After that, a break in the
            German spa town of Baden-Baden.  The last night was a weird last-minute B&B in the Belgian
            countryside - clearly Peter Stringfellow's country pad. 
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Asturias",
            heading="AthTech in Asturias",
            imagedir="asturias",
            description="""
            This year's Athletics Tech conference was in Gijon in Spain,
            on their green northern coast.  We flew down to Bilbao,
            stayed the night before in Santander, and managed to enjoy perfect
            weather (in a place renowned for its rain) when not conferencing.
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Lyon and Lausanne",
            heading="Lyon and Lausanne",
            imagedir="lyonlausanne",
            description="""
            Late October saw us at the World Wide Web Consortium conference in Lyon on a Tuesday and Wednesday, then
            a quick train ride to the European Athletics event in Lausanne on Thu/Fri.  We explored Old Lyon,
            culinary capital of France, but wished we had longer to see it properly.  In Lausanne we stayed
            in a beautiful gothic hotel close to the lake where the conference was taking place, and Andy had
            to lead a workshop.  When off duty, he enjoyed a lunch hosted by Seb Coe at the
            Olympic Museum, while Alisa had fun in Charlie Chaplin's house. We finished with the annual Golden 
            Tracks Gala Dinner, where we met European 100/200 champion Dina Asher-Smith, and Olympic/World/Euro 
            Long Jump champion (and Strictly Come Dancing contestant) Greg Rutherford...
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Tim",
            heading="Tim",
            imagedir="tim",
            description="""
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Harry",
            heading="Harry",
            imagedir="harry",
            description="""
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
        dict(
            title="Punta Cana",
            heading="Punta Cana",
            imagedir="domrep",
            description="""
            As soon as the boys' terms ended, we had a week of all-inclusive holiday in the
            Dominican Republic - something the boys finally conceded was a "proper holiday"!
            """,
            captions= {
            },
            imagelist= [
            ]
        ),
    ]
}





def run():
    gallery_template = preppy.getModule("gallery.prep")
    for (year, galleries) in sorted(GALLERIES_BY_YEAR.items()):
        print(year, "...")
        

        iyr = int(year)
        rng = reversed(range(2004, iyr))
        previous_years = list(map(str, rng))

        for gallery in galleries:
            # does it have a yaml file?  new system 2025

            gallery["filename"] = year + "/" + gallery["imagedir"] + ".html"
            if 'heading' not in gallery:
                gallery['heading'] = gallery['title']

        for gallery in galleries:
            info_file_name = year + "/images/" + gallery["imagedir"] + "/index.yaml"
            if os.path.isfile(info_file_name):
                print("YAML:" + info_file_name)
                info = yaml.safe_load(open(info_file_name).read())
                gallery.update(info)


            pattern = "{}/images/{}/*.jp*".format(year, gallery["imagedir"])
            if "captions" not in gallery:
                gallery["captions"] = {}
            namespace = gallery.copy()
            if gallery.get('imagelist'):
                images = []
                for thing in gallery['imagelist']:
                    if isinstance(thing, list):
                        fn, caption = thing
                        namespace['captions'][fn] = caption
                        filename = '%s/images/%s/%s' % (year, gallery["imagedir"], fn)
                        images.append(filename)
                    elif ('IMG_' in thing) or thing.lower().endswith('jpg') or thing.lower().endswith('jpeg'):
                        filename = '%s/images/%s/%s' % (year, gallery["imagedir"], thing)
                        images.append(filename)
                    else:
                        images.append(thing)

            else:
                pattern = "%s/images/%s/*.jp*" % (year, gallery["imagedir"])
                images = sorted(glob.glob(pattern))

                notes = gallery.get("notes", {})
                if notes:
                    print("Gallery has notes!", notes)

                # new in 2025.  Loop over a structure, not just a filename
                imageinfo = []
                for image in images:
                    imgfilename = os.path.split(image)[-1]

                    title = text = caption = ""
                    if imgfilename in notes:
                        note = notes[imgfilename]
                        title = note.get("title", "")
                        text = note.get("text", "")
                        caption = note.get("caption", "")


                    info = dict(
                        imagename=image,
                        title=title,
                        text=text,
                        caption=caption
                        )

                    if info["caption"]:
                        print(info)
                    imageinfo.append(info)

            namespace["galleries"] = galleries  #need them all to iterate menus
            namespace["year"] = year
            namespace["previous_years"] = previous_years
            namespace["images"] = images
            namespace["imageinfo"] = imageinfo
            html = gallery_template.getOutput(namespace)

            outfilename = gallery["filename"]
            open(outfilename, "w").write(html)
            print("created", outfilename)


        #Now do the annual index
        annual_template = preppy.getModule("annual.prep")
        outfilename = year + "/index.html"
        html = annual_template.getOutput(
            dict(year=year, galleries=galleries, previous_years=previous_years)
            )
        open(outfilename, "w").write(html)
        print("wrote", outfilename)

    #Now do the overall index
    year = str(iyr)
    print("doing main site index, year=", year)
    annual_template = preppy.getModule("index.prep")
    galleries = GALLERIES_BY_YEAR[year]
    html = annual_template.getOutput(
        dict(year=year, galleries=galleries, mainpic=MAIN_PIC, maintext=MAIN_TEXT)
    )
    open("index.html", "w").write(html)
    print("wrote index.html")

if __name__=='__main__':
    run()