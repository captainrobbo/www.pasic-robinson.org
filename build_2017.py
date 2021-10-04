import os
import sys
import glob

import preppy

# MAIN_PIC = "2016/images/08_bergamo/IMG_C5199.jpg"
MAIN_PIC = "2017/images/01_skiing/IMG_6073.jpg"
GALLERIES_BY_YEAR = {
    "2016": [

        dict(
            title="Izet's Funeral",
            heading="Izet's Funeral in January, Mostar",
            description="""Alisa's father Izet passed away early in the New Year.
            We all assembled in his home town of Mostar in Herzegovina. More
            than 100 people gathered to say farewell.
            """,
            imagedir="01_funeral"
            ),

        dict(
            title="Skiing - February",
            heading="Skiing in Chamonix at half term",
            description="""At half term, Tim, Andy and Alisa had a brief 4 days skiing
            in Argentiere and Chamonix.  Meanwhile, Harry was in Iceland
            on a geography field trip.
            """,
            imagedir="02_chamonix",
            captions= {
                "4660": "We met up with Susannah, Jamie and Beau again"
            }
            ),

        dict(
            title="Andy's 50th",
            heading="Andy's 50th birthday",
            description="""The family went to dinner at the Shard.
            Alisa then took Andy off to Ibiza for 3 days
            as a birthday surprise
            """,
            imagedir="03_ibiza",
            captions={
                "4757": "Night out at Pacha - my wife thinks of everything",
                "5165": "Harry puts his usual razor-sharp spin on things"

            }
            ),

        dict(
            title="Random moments",
            heading="Random Moments",
            description="""
            """,
            imagedir="04_random",
            #add malaga too,
            captions={
                "english_summer": "A rare sunny day in Wimbledon",
                "4840": "On board a classic ship in Hamburg at a FIWARE event",
                "4627": "Tim showing grandmother around his university",
                "4631": "Tim showing grandmother around his university",
                "4816": "Harry broke his leg just before his AS-levels",
                "4863": "21st Wedding Anniversary - checking the clothes still fit",
                "4874": "Leg rehab",
                "4965": "17th birthday present - tent for festivals",
                "5066": "With our friends from LA, the Johnsons, in Oxford",
                "5404": "Andy hopped over to Amsterdam.  Apparently they get summer too",
                "5478": "On Brexit day, we waded to Belgium to compete for EU funds",
                "5485": "Floods made it challenging..",
                "5490": "..but we made it to Ghent, and got the grant!",
                "5492": "University open days - we stayed in Durham Castle",
                "5503": "Harry got the room above the gate!",
                "5690": "A very belated birthday treat for Tefika.",
                "5844": "Squirrels like our recycling bins",
                "IMG_W": "Ena's wedding in Bosnia"

                }
            ),

        dict(
            title="Barcelona",
            heading="Conference in Barcelona",
            description="""ReportLab's participation in FINODEX required
            us to attend many conferences and meetings around Europe.  One
            of them was in Barcelona, so we treated ourselves to two days
            R&amp;R afterwards.
            """,
            imagedir="05_barcelona",
            captions = {
                "4942": "It turned into a big party each afternoon, but the mornings were blissful"
                }
            ),

        dict(
            title="Memorial for Izet",
            heading="Memorial service for Izet",
            description="""We gathered again in Mostar on what would
            have been Izet's 79th birthday. Tefika had commissioned a
            beautiful white marble headstone, and expects to be buried
            next to him one day.  Each of the five grandchildren wrote
            and read out touching speeches.
            """,
            imagedir="06_memorial",
            captions={"15033": "Mostar's beautiful old bridge"}
            ),

        dict(
            title="Croatia",
            heading="Croatia",
            description="""We had a few brief days in Duboka
            either side of the memorial service.  Meanwhile, Tim
            was busy at student festivals all over former Yugoslavia,
            then joined his grandmother for a few weeks at the beach
            house
            """,
            imagedir="07_croatia",
            captions={
                "5576": "Dubrovnik's old port",
                "5581": "More around-the-world Yoga poses"
            }
            ),

        dict(
            title="Italy",
            heading="Italian Lakes, San Pellegrino and Milano",
            description="""The boys have such busy schedules that we
            had to work hard to find a few days together.  We managed
            to squeeze in 4 days in Northern Italy.  We enjoyed seeing 
            Lake Como again - this time in sunshine.   The highlight 
            was San Pellegrino Spa, where you can bathe in the stuff
            others drink, with a cocktail hour in bathrobes as the sun sets.
            Finally we saw downtown Milan, with its spectacular square,
            cathedral and galleria.


            """,
            imagedir="08_bergamo",
            captions={
                "5142": "First views of the lake at Lecco",
                "5156": "Beautiful Bellaggio",
                "0644": "San Pellegrino by the river",
                "5133": "Free refills!",
                "5145": "Unlimited cheese and prosecco in dressing gowns",
                "5176": "Milano's main square and cathedral",
                "5207": "The world's first covered shopping arcade"
            }

            ),

        dict(
            title="Heidi Land",
            heading="Switzerland and Black Forest",
            description="""Ela is Alisa's childhood friend. 
            We went down to Zurich for her 50th birthday in August.   
            She lives in Zollikon, a beautiful suburb of Zurich she 
            calls 'Heidi-land'. We had a great party down by the lake.
            We also spent a couple of days exploring the Black Forest
            in Germany - beautiful scenery and cuckoo clocks. 
            """,
            imagedir="09_heidi",
            captions={
                "5291": "The view from Ela's kitchen window",
                "5297": "Girls' day out in Zurich",
                "5764": "Ela's daughter, Lily",
                "5765": "Heidi-land",
                "5797": "Party by the lake",
                "5783": "Cool new Swiss relaxation technology - www.lazybag.ch",
                "5750": "Freiburg and the Black Forest",
                "5799": "Ela's brother Nebojsa, another old friend from Alisa's youth"
                }
            ),
        dict(
            title="Malaga",
            heading="Malaga",
            description="""We went to an EU event in Malaga, and had a
                        look around.
                        """,
            imagedir="10_malaga",
            #add tenerife/madrid afterwards
            ),
        dict(
            title="Aljosa's Wedding",
            heading="Aljosa and Gabriela's wedding",
            description="""Aljosa and Gabriela organised a beautiful
            wedding on El Hierro, the smallest of the Canary Islands.
                        """,
            imagedir="11_wedding",
            captions={
                "5467": 'Sisterly love',
                "5479": "Ushers Tim and Harry, with bridesmaids",
                "5533": "Tim and his three cousins",
                "5541": "Proud Tefika with children and grandchildren. Izet was sorely missed"
                }
            #add tenerife/madrid afterwards
            ),

        dict(
            title="Tenerife and Madrid",
            heading="Tenerife and Madrid",
            description="""Having gone all the way to the smallest
            Canarian island for a wedding, we stopped in 
            Tenerife for a few
            days, and Harry's friend Joe came down.  Then we went
            back via Madrid, and had a beautiful day in Retiro.
                        """,
            imagedir="12_tenerife",
            #add tenerife/madrid afterwards
            captions={
                "5604":"Wot? No ketchup?",
                "5985":"Mount Teide's caldera - a little geography",
                "6003":"El Retiro, Madrid",

                }
            ),

        dict(
            title="Dominican 2015",
            heading="Beach holiday in the Dominican Republic",
            description="""
            At the end of 2015 we had a week in the Dominican
            Republic.  The pics didn't make it onto the website
            so here they are, a year later. 
            """,
            imagedir="13_dominican_2015"
            ),

        dict(
            title="Dominican 2016",
            heading="Beach holiday in the Dominican Republic",
            description="""
            To unwind after a tough year, we treated ourselves to a week
            in the sunshine, for the second year in a row. Different
            hotel, same glorious sunshine.
            """,
            imagedir="14_dominican_2016"
            ),

    ],
    "2017": [
        dict(
            title="Skiing",
            heading="Skiing - New Year and February",
            description="""
            We saw in the New Year in the Alps, where the British team at 
            Les Hautes Auguilles had its usual superb feast.  Sadly there was
            not much snow on our side, so we went to the Italian side a couple
            of times, and explored Swiss hot baths.  Our last night was in Evian
            where they have an amazing driftwood show, Les Flottins.  We came
            back in February and were rewarded with lots of snow and blue skies.
            """,
            imagedir="01_skiing",
            captions= {
            },
            imagelist= [
                ['IMG_5894.jpg', "New Year feast at Les Hautes Aiguilles"],
                'IMG_5896.jpg',
                ['IMG_5872.jpg', "Pierre a Ric (our local piste) looking bare"],
                ['IMG_5880.jpg', "Trying Switzerland in search of more snow"],
                
                ['IMG_6076.jpg', "Le Jet d'Eau in Geneva - spot the rainbow!"],

                ['IMG_5958.jpg', "The Flottins of Evian - a Christmas show of art from driftwood"],
                'IMG_5961.jpg',
                'IMG_5971.jpg',
                'IMG_5972.jpg',

                ['IMG_5963.jpg', "Evian water - from the source"],
                'IMG_5965.jpg',
                'IMG_5974.jpg',
                'IMG_5968.jpg',

                ['IMG_6065.jpg', "The nursery slope had snow so Andy made a fool of himself on a snowboard"],
                'IMG_6067.jpg',


                ['IMG_6098.jpg', "When there's no skiing, there's always patisserie in Chamonix..."],
                'IMG_6112.jpg',
                'IMG_6113.jpg',
                ['IMG_6120.jpg', "Spring scenery in Chamonix in December"],
                ['IMG_5919.jpg', "...or skating"],


                ['IMG_6090.jpg', "Alisa's 'yoga round the world' mission - Snow Salutations"],
                'IMG_6082.jpg',
                'IMG_6083.jpg',
                'IMG_6106.jpg',

                ['IMG_6137.jpg', "Who's the mystery man?"],
                'IMG_6138.jpg',
                'IMG_6142.jpg',

                ['IMG_5984.jpg', "Driving back, the magnificent Metz cathedral"],
                'IMG_5986.jpg',

                "Attempt number two - February - lots of snow this time!",

                'IMG_6071.jpg',
                'IMG_6079.jpg',
                'IMG_6080.jpg',
                'IMG_6088.jpg',
                'IMG_6127.jpg',
                'IMG_6132b.jpg',
                'IMG_6132.jpg',
                'IMG_6135.jpg',







            ]
        ),
        dict(
            title="Mauritius",
            heading="Mauritius",
            description="""
            Andy's birthday treat was a week in Mauritius.  He had
            a holiday there as a child, and we went together with our boys in 2009.
            This time it was just the two of us.  Beautiful location near Blue Bay,
            amazing scenery, lots of watersports and some beach yoga, and Andy even
            found Gateax Piments which he had loved 40 years before...
            """,
            imagedir="02_mauritius",
            captions= {
            },
            imagelist=[
                'IMG_6198.jpg',
                ['IMG_6349.jpg', "Alisa in action"],
                ['IMG_6366.jpg', "Andy's attempt at wakeboarding"],
                ['IMG_6354.jpg', "Andy's attempt at wakeboarding"],
                ['IMG_6222.jpg', """
                While driving around we stumbled across an amazing Hindu shrine, the Ganga Talao ('Crater Lake'); 
                tens of thousands of Hindus make an annual pilgrimage, but we had it to ourselves; 
                the most spiritual place yet for Alisa's yoga hobby!
                """],
                'IMG_6215.jpg',
                'IMG_6219.jpg',
                'IMG_6236.jpg',
                ['IMG_6255.jpg', 'The view from our room...'],
                ['IMG_6274.jpg', 'More beach yoga with spectacular background...'],
                'IMG_6279.jpg',
                'IMG_6288b.jpg',
                'IMG_6286.jpg',
                'IMG_6288.jpg',
                'IMG_6289.jpg',

                ['IMG_6290.jpg', 'Gateaux Piments - last tasted in Vacoas market circa 1977 aged 12!'],


                'IMG_6300.jpg',
                'IMG_6313.jpg',
                'IMG_6316.jpg',
                'IMG_6322.jpg',
                'IMG_6361.jpg',

                ['IMG_6385.jpg', 'One year older']

            ]
        ),
        dict(
            title="Amsterdam",
            heading="Amsterdam - May bank holiday",
            description="""
            We spent our 22nd wedding anniversary with Arno and Arifa in their home
            in Amsterdam.  It was scorching hot weather so we
            spent time at the beach, and barbecuing and drinking cocktails in the garden.  
            Being so close to the canals, the mosquitoes were out in force and feasted on us.
            """,
            imagedir="03_amsterdam",
            captions= {
            },
            imagelist=[
            ["IMG_6466.jpg", "Dolce, the newest addition to the family"],
            ["IMG_6469.jpg", ""],
            ["IMG_6474.jpg", ""],
            ["IMG_6485.jpg", ""],
            ["IMG_6500.jpg", ""],
            ["IMG_6713.jpg", "The first stop on Harry's interrailing tour - Arifa hosted lunch"],
            ]
        ),
        dict(
            title="Summer - Italy",
            heading="Summer Holiday stage 1 - Italy",
            description="""
            This summer saw a long road trip south.  We had a work engagement
            in Grosseto, Tuscany at the European U23 Athletics, so we drove down through
            the Alps and stayed on a Tuscan hilltop.  We then crossed to Perugia,
            then a ferry from Ancona to Split

            """,
            imagedir="04a_italy",
            captions= {
            },
            imagelist=[
            ['IMG_6706.jpg', 'Driving through Argentiere'],
            'IMG_6707.jpg',
            ['IMG_6709.jpg', """
            Rest stop at Sestri Levante on the Italian Riviera.  We didn't quite have
            time to take the train through the Cinque Terre - next time maybe.
            """],
            #http://www.european-athletics.org/photos/gallery=grosseto-2017-european-athletics-u20-championships-photo-gallery-day-1282187/#
            ['IMG_6597.jpg',"""Grosseto was booked out with athletics teams, so we were 'forced' to stay
            in a lovely hotel facing a Tuscan hill town, Borgo Magliano.  
            """],
            'IMG_6602.jpg',
            'IMG_6592a.jpg',
            ['IMG_6588.jpg',"Some get their energy from coffee, others from Yoga"],
            ['IMG_6722.jpg',"Borgo Magliano by night - delicious dinners at sunset"],
            'IMG_6610.jpg',

            ['IMG_6628.jpg', "Perugia - stunning hilltop town, half the price and a tenth of the crowds of Tuscany"],
            'IMG_6629.jpg',
            'IMG_6630.jpg',
            'IMG_6738.jpg',
            'IMG_6739.jpg',

            ['IMG_6633.jpg', "The ferry at Ancona - easily the best way to get to Croatia"],
            'IMG_6634.jpg'
            ]
        ),
        dict(
            title="Summer - Croatia",
            heading="Summer Holiday stage 2 - Croatia",
            description="""
            """,
            imagedir="04b_croatia",
            captions= {
            },
            imagelist=[
            ['IMG_6575.jpg', "Cavtat harbour at sunset"],
            ['IMG_6686.jpg', "Andy's favourite bar"],
            ['IMG_6598.jpg', "In Duboka with Tefika, Gabriela and Adela"],
            ['IMG_6609.jpg', "Sunset beach bar in Komarna, just over the hill"],
            ['IMG_6612.jpg', ""],
            ['IMG_6740.jpg', "From the Dubrovnik town walls"],
            ['IMG_6757.jpg', "The Riva in Split"],
            ['IMG_6862.jpg', ""],
            ['IMG_6763.jpg', ""],
            ['IMG_6867.jpg', "Diocletian's Palace in Split"],
            ['IMG_6868.jpg', ""],
            ['IMG_6850.jpg', "Resupplying Harry with much-needed cash and ice cream during his Interrailing"],


            ['IMG_6764.jpg', "Dalmatian family dinner with Stipe..."],
            ['IMG_6773.jpg', "Rafting on the Cetinja above Split - sadly we couldn't take pics on the way down but it was spectacular"],
            ['IMG_6781.jpg', "The ultimate barbecue - slow-roasted lamb under the bell by moonlight"],
            ['IMG_6786.jpg', "...washed down with Roko's famous homemade wines"],

            ['IMG_6819.jpg', "Duboka gets glamorous - new wine-tasting room above our village"],
            ['IMG_6821.jpg', "Naturally, Sandra and Oggi were there already!"],
            ['IMG_6826.jpg', "Our local sea, 'Malo More'"],
            ['IMG_6828.jpg', ""],
            ['IMG_6887.jpg', ""],
            ['IMG_6901.jpg', ""],

            ['IMG_6832.jpg', "Lapad peninsula, Dubrovnik - a quiet corner and amazing swim in peak season"],
            ['IMG_6834.jpg', ""],

            ['IMG_6882.jpg', "Oggi and Sandra's boat - sunset cruise"],
            ['IMG_6874.jpg', ""],
            ['IMG_6924.jpg', ""],
            ['IMG_6926.jpg', ""],
            ['IMG_6929.jpg', "Sunset over the Drava in Maribor, Slovenia, on the way home"],
            ['IMG_6930.jpg', ""],
            ['IMG_6931.jpg', ""],
            ]
        ),
        dict(
            title="Summer - Bosnia",
            heading="Summer Holiday stage 3 - Bosnia",
            description="""
            """,
            imagedir="04c_bosnia",
            captions= {
            },
            imagelist=[
            ['IMG_6618.jpg', "Mirna's 60th birthday - an international gathering in a ski lodge above Mostar"],
            ['IMG_6564.jpg', ""],
            ['IMG_6619.jpg', ""],
            ['IMG_6621.jpg', ""],
            ['IMG_6622.jpg', ""],
            ['IMG_6630.jpg', "Alisa's aunt Mummi back over from Phoenix - sightseeing in Mostar"],
            ['IMG_6636.jpg', ""],
            ['IMG_6646.jpg', ""],
            ['IMG_6647.jpg', ""],
            # ['IMG_6651.jpg', ""],
            ['IMG_6644.jpg', "Sarajevo"],
            ['IMG_6659.jpg', "Markale market in Sarajevo, the place of terrible massacres where many lost their lives"],
            ['IMG_6661.jpg', "A memorial to those killed during the shelling in 1994/5"],
            ['IMG_6671.jpg', """Testing OpenTrack's software at an international athletics event in Bosnia
            """],
            ['IMG_6676.jpg', ""],
            ['IMG_6698.jpg', ""],
            ['IMG_6708.jpg', "Dinner by the river on Bembasa.  The site of a famous folk song about some bloke giving his girlfriend a sheep."],
            ['IMG_6883.jpg', "On the road from Sarajevo to Mostar - roast lamb on a spit above a stunning lake.  Paddy Ashdown had his chateau here when he was running the country for 5 years"],
            ['IMG_6821.jpg', "Izet's grave in Mostar"],
            ]
        ),
        dict(
            title="Summer - Germany",
            heading="Summer Holiday stage 4 - Germany",
            description="""
            We drove back across Germany, stopping for two nights to see the Rhine valley
            with all its Castles and Hansel-and-Gretel towns.  We worked our way up
            from Mannheim to Koblenz.
            """,
            imagedir="04d_germany",
            captions= {
            },
            # imagelist=[
            # ["IMG_6902.jpg", "Mannheim's water tower"],
            # ["IMG_6907.jpg", "Shoe bargains"],
            # ["IMG_6942.m4v", ""],
            # ["IMG_.jpg", ""],
            # ["IMG_.jpg", ""],
            # ["IMG_.jpg", ""],
            # ["IMG_.jpg", ""],
            # ["IMG_.jpg", ""],
            # ["IMG_.jpg", ""],
            # ["IMG_.jpg", ""],
            # ]
        ),
        dict(
            title="Portugal",
            heading="Portugal",
            description="""
            A conference in Portugal in early October gave us a chance to see
            the Algarve and top up our tans
            """,
            imagedir="05_portugal",
            captions= {
            }
        ),
        dict(
            title="Cyprus",
            heading="Cyprus",
            description="""
            Andy had to see the athletics federation in Cyprus, a country he
            last saw in 1973, so Alisa and Tefika tagged along for the ride.
            Beautiful sunshine during the (very short) days, and ancient ruins
            from Greek to Mediaeval times.
            """,
            imagedir="08_cyprus",
            captions= {
            },
            imagelist=[
            ["IMG_7339.jpg", "Our hotel near Limassol - beautiful weather and swimming in the sea in November"],
            ["IMG_7347.jpg", ""],
            ["IMG_7348.jpg", ""],
            ["IMG_7351.jpg", ""],
            ["IMG_7352.jpg", ""],
            ["IMG_7315.jpg", "The Turkish half of Nicosia"],
            ["IMG_7316.jpg", ""],
            ["IMG_7323.jpg", ""],
            ["IMG_7116.jpg", "Beautiful ruins from Greek to Mediaeval period"],
            ["IMG_7367.jpg", ""],
            ["IMG_7372.jpg", ""],
            ["IMG_7374.jpg", ""],            

            ]
        ),
        dict(
            title="Birthdays",
            heading="Birthdays",
            description="""
            Amazingly, all 4 of us had birthdays at some point this year
            """,
            imagedir="06_birthdays",
            captions= {
            }
        ),
        dict(
            title="Random Moments",
            heading="",
            description="""
            """,
            imagedir="07_misc",
            captions= {
            }
        ),
        dict(
            title="Dominican Republic",
            heading="",
            description="""
            We took our usual week's break in December before the kids came home,
            and enjoyed beautiful sunshine, sand and sea in the Dominican Republic...
            """,
            imagedir="09_dom",
            captions= {
            }
        ),
    ],

}


def run():
    gallery_template = preppy.getModule("gallery.prep")
    for (year, galleries) in sorted(GALLERIES_BY_YEAR.items()):
        print year, "..."
        print

        for gallery in galleries:
            gallery["filename"] = year + "/" + gallery["imagedir"] + ".html"

        for gallery in galleries:
            pattern = "%s/images/%s/*.jpg" % (year, gallery["imagedir"])
            if not gallery.has_key("captions"):
                gallery["captions"] = {}
            namespace = gallery.copy()
            if gallery.has_key('imagelist'):
                images = []
                for thing in gallery['imagelist']:
                    if isinstance(thing, list):
                        fn, caption = thing
                        namespace['captions'][fn] = caption
                        filename = '%s/images/%s/%s' % (year, gallery["imagedir"], fn)
                        images.append(filename)
                    elif 'IMG_' in thing:
                        filename = '%s/images/%s/%s' % (year, gallery["imagedir"], thing)
                        images.append(filename)
                    else:
                        images.append(thing)

            else:
                pattern = "%s/images/%s/*.jpg" % (year, gallery["imagedir"])
                images = glob.glob(pattern)

            namespace["galleries"] = galleries  #need them all to iterate menus
            namespace["year"] = year
            namespace["images"] = images

            html = gallery_template.getOutput(namespace)

            outfilename = gallery["filename"]
            open(outfilename, "w").write(html)
            print "created", outfilename


        #Now do the annual index
        annual_template = preppy.getModule("annual.prep")
        outfilename = year + "/index.html"
        html = annual_template.getOutput(
            dict(year=year, galleries=galleries)
            )
        open(outfilename, "w").write(html)
        print "wrote", outfilename

    #Now do the overall index
    print "doing main site index, year=", year
    annual_template = preppy.getModule("index.prep")
    html = annual_template.getOutput(
        dict(year=year, galleries=galleries, mainpic=MAIN_PIC)
    )
    open("index.html", "w").write(html)
    print "wrote index.html"

if __name__=='__main__':
    run()