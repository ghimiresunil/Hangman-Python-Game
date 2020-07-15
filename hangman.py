from tkinter import *
from string import ascii_uppercase
import random
from tkinter import messagebox

window = Tk()
window.title("PYTHON | HANGMAN")
window.resizable(width=False, height=False)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
x = int(width / 2 - 600 / 2)
y = int(height / 2 - 400 / 2)
str1 = "594x399+" + str(x) + "+" + str(y)
window.geometry(str1)
footer = Label(text="© 2020 Tech Tutor. All Right Reserved", bg = "white")
footer.config(font=('Courier', 11, 'bold'))
footer.place(x=x - 222, y=y + 190)

word_list = ['ABACK', 'ABAFT', 'ABANDONED', 'ABASHED', 'ABERRANT', 'ABHORRENT', 'ABIDING', 'ABJECT', 'ABLAZE', 'ABLE',
             'ABNORMAL', 'ABOARD', 'ABORIGINAL', 'ABORTIVE', 'ABOUNDING', 'ABRASIVE', 'ABRUPT', 'ABSENT', 'ABSORBED',
             'ABSORBING', 'ABSTRACTED', 'ABSURD', 'ABUNDANT', 'ABUSIVE', 'ACCEPTABLE', 'ACCESSIBLE', 'ACCIDENTAL',
             'ACCURATE', 'ACID', 'ACIDIC', 'ACOUSTIC', 'ACRID', 'ACTUALLY', 'AD HOC', 'ADAMANT', 'ADAPTABLE',
             'ADDICTED', 'ADHESIVE', 'ADJOINING', 'ADORABLE', 'ADVENTUROUS', 'AFRAID', 'AGGRESSIVE', 'AGONIZING',
             'AGREEABLE', 'AHEAD', 'AJAR', 'ALCOHOLIC', 'ALERT', 'ALIKE', 'ALIVE', 'ALLEGED', 'ALLURING', 'ALOOF',
             'AMAZING', 'AMBIGUOUS', 'AMBITIOUS', 'AMUCK', 'AMUSED', 'AMUSING', 'ANCIENT', 'ANGRY', 'ANIMATED',
             'ANNOYED', 'ANNOYING', 'ANXIOUS', 'APATHETIC', 'AQUATIC', 'AROMATIC', 'ARROGANT', 'ASHAMED', 'ASPIRING',
             'ASSORTED', 'ASTONISHING', 'ATTRACTIVE', 'AUSPICIOUS', 'AUTOMATIC', 'AVAILABLE', 'AVERAGE', 'AWAKE',
             'AWARE', 'AWESOME', 'AWFUL', 'AXIOMATIC', 'BAD', 'BARBAROUS', 'BASHFUL', 'BAWDY', 'BEAUTIFUL', 'BEFITTING',
             'BELLIGERENT', 'BENEFICIAL', 'BENT', 'BERSERK', 'BEST', 'BETTER', 'BEWILDERED', 'BIG', 'BILLOWY',
             'BITE-SIZED', 'BITTER', 'BIZARRE', 'BLACK', 'BLACK-AND-WHITE', 'BLOODY', 'BLUE', 'BLUE-EYED', 'BLUSHING',
             'BOILING', 'BOORISH', 'BORED', 'BORING', 'BOUNCY', 'BOUNDLESS', 'BRAINY', 'BRASH', 'BRAVE', 'BRAWNY',
             'BREAKABLE', 'BREEZY', 'BRIEF', 'BRIGHT', 'BRIGHT', 'BROAD', 'BROKEN', 'BROWN', 'BUMPY', 'BURLY',
             'BUSTLING', 'BUSY', 'CAGEY', 'CALCULATING', 'CALLOUS', 'CALM', 'CAPABLE', 'CAPRICIOUS', 'CAREFUL',
             'CARELESS', 'CARING', 'CAUTIOUS', 'CEASELESS', 'CERTAIN', 'CHANGEABLE', 'CHARMING', 'CHEAP', 'CHEERFUL',
             'CHEMICAL', 'CHIEF', 'CHILDLIKE', 'CHILLY', 'CHIVALROUS', 'CHUBBY', 'CHUNKY', 'CLAMMY', 'CLASSY', 'CLEAN',
             'CLEAR', 'CLEVER', 'CLOISTERED', 'CLOUDY', 'CLOSED', 'CLUMSY', 'CLUTTERED', 'COHERENT', 'COLD', 'COLORFUL',
             'COLOSSAL', 'COMBATIVE', 'COMFORTABLE', 'COMMON', 'COMPLETE', 'COMPLEX', 'CONCERNED', 'CONDEMNED',
             'CONFUSED', 'CONSCIOUS', 'COOING', 'COOL', 'COOPERATIVE', 'COORDINATED', 'COURAGEOUS', 'COWARDLY',
             'CRABBY', 'CRAVEN', 'CRAZY', 'CREEPY', 'CROOKED', 'CROWDED', 'CRUEL', 'CUDDLY', 'CULTURED', 'CUMBERSOME',
             'CURIOUS', 'CURLY', 'CURVED', 'CURVY', 'CUT', 'CUTE', 'CUTE', 'CYNICAL', 'DAFFY', 'DAILY', 'DAMAGED',
             'DAMAGING', 'DAMP', 'DANGEROUS', 'DAPPER', 'DARK', 'DASHING', 'DAZZLING', 'DEAD', 'DEADPAN', 'DEAFENING',
             'DEAR', 'DEBONAIR', 'DECISIVE', 'DECOROUS', 'DEEP', 'DEEPLY', 'DEFEATED', 'DEFECTIVE', 'DEFIANT',
             'DELICATE', 'DELICIOUS', 'DELIGHTFUL', 'DEMONIC', 'DELIRIOUS', 'DEPENDENT', 'DEPRESSED', 'DERANGED',
             'DESCRIPTIVE', 'DESERTED', 'DETAILED', 'DETERMINED', 'DEVILISH', 'DIDACTIC', 'DIFFERENT', 'DIFFICULT',
             'DILIGENT', 'DIREFUL', 'DIRTY', 'DISAGREEABLE', 'DISASTROUS', 'DISCREET', 'DISGUSTED', 'DISGUSTING',
             'DISILLUSIONED', 'DISPENSABLE', 'DISTINCT', 'DISTURBED', 'DIVERGENT', 'DIZZY', 'DOMINEERING', 'DOUBTFUL',
             'DRAB', 'DRACONIAN', 'DRAMATIC', 'DREARY', 'DRUNK', 'DRY', 'DULL', 'DUSTY', 'DUSTY', 'DYNAMIC',
             'DYSFUNCTIONAL', 'EAGER', 'EARLY', 'EARSPLITTING', 'EARTHY', 'EASY', 'EATABLE', 'ECONOMIC', 'EDUCATED',
             'EFFICACIOUS', 'EFFICIENT', 'EIGHT', 'ELASTIC', 'ELATED', 'ELDERLY', 'ELECTRIC', 'ELEGANT', 'ELFIN',
             'ELITE', 'EMBARRASSED', 'EMINENT', 'EMPTY', 'ENCHANTED', 'ENCHANTING', 'ENCOURAGING', 'ENDURABLE',
             'ENERGETIC', 'ENORMOUS', 'ENTERTAINING', 'ENTHUSIASTIC', 'ENVIOUS', 'EQUABLE', 'EQUAL', 'ERECT', 'ERRATIC',
             'ETHEREAL', 'EVANESCENT', 'EVASIVE', 'EVEN', 'EXCELLENT', 'EXCITED', 'EXCITING', 'EXCLUSIVE', 'EXOTIC',
             'EXPENSIVE', 'EXTRA-LARGE', 'EXTRA-SMALL', 'EXUBERANT', 'EXULTANT', 'FABULOUS', 'FADED', 'FAINT', 'FAIR',
             'FAITHFUL', 'FALLACIOUS', 'FALSE', 'FAMILIAR', 'FAMOUS', 'FANATICAL', 'FANCY', 'FANTASTIC', 'FAR',
             'FAR-FLUNG', 'FASCINATED', 'FAST', 'FAT', 'FAULTY', 'FEARFUL', 'FEARLESS', 'FEEBLE', 'FEIGNED', 'FEMALE',
             'FERTILE', 'FESTIVE', 'FEW', 'FIERCE', 'FILTHY', 'FINE', 'FINICKY', 'FIRST', 'FIVE', 'FIXED', 'FLAGRANT',
             'FLAKY', 'FLASHY', 'FLAT', 'FLAWLESS', 'FLIMSY', 'FLIPPANT', 'FLOWERY', 'FLUFFY', 'FLUTTERING', 'FOAMY',
             'FOOLISH', 'FOREGOING', 'FORGETFUL', 'FORTUNATE', 'FOUR', 'FRAIL', 'FRAGILE', 'FRANTIC', 'FREE',
             'FREEZING', 'FREQUENT', 'FRESH', 'FRETFUL', 'FRIENDLY', 'FRIGHTENED', 'FRIGHTENING', 'FULL', 'FUMBLING',
             'FUNCTIONAL', 'FUNNY', 'FURRY', 'FURTIVE', 'FUTURE', 'FUTURISTIC', 'FUZZY', 'GABBY', 'GAINFUL', 'GAMY',
             'GAPING', 'GARRULOUS', 'GAUDY', 'GENERAL', 'GENTLE', 'GIANT', 'GIDDY', 'GIFTED', 'GIGANTIC', 'GLAMOROUS',
             'GLEAMING', 'GLIB', 'GLISTENING', 'GLORIOUS', 'GLOSSY', 'GODLY', 'GOOD', 'GOOFY', 'GORGEOUS', 'GRACEFUL',
             'GRANDIOSE', 'GRATEFUL', 'GRATIS', 'GRAY', 'GREASY', 'GREAT', 'GREEDY', 'GREEN', 'GREY', 'GRIEVING',
             'GROOVY', 'GROTESQUE', 'GROUCHY', 'GRUBBY', 'GRUESOME', 'GRUMPY', 'GUARDED', 'GUILTLESS', 'GULLIBLE',
             'GUSTY', 'GUTTURAL', 'HABITUAL', 'HALF', 'HALLOWED', 'HALTING', 'HANDSOME', 'HANDSOMELY', 'HANDY',
             'HANGING', 'HAPLESS', 'HAPPY', 'HARD', 'HARD-TO-FIND', 'HARMONIOUS', 'HARSH', 'HATEFUL', 'HEADY',
             'HEALTHY', 'HEARTBREAKING', 'HEAVENLY', 'HEAVY', 'HELLISH', 'HELPFUL', 'HELPLESS', 'HESITANT', 'HIDEOUS',
             'HIGH', 'HIGHFALUTIN', 'HIGH-PITCHED', 'HILARIOUS', 'HISSING', 'HISTORICAL', 'HOLISTIC', 'HOLLOW',
             'HOMELESS', 'HOMELY', 'HONORABLE', 'HORRIBLE', 'HOSPITABLE', 'HOT', 'HUGE', 'HULKING', 'HUMDRUM',
             'HUMOROUS', 'HUNGRY', 'HURRIED', 'HURT', 'HUSHED', 'HUSKY', 'HYPNOTIC', 'HYSTERICAL', 'ICKY', 'ICY',
             'IDIOTIC', 'IGNORANT', 'ILL', 'ILLEGAL', 'ILL-FATED', 'ILL-INFORMED', 'ILLUSTRIOUS', 'IMAGINARY',
             'IMMENSE', 'IMMINENT', 'IMPARTIAL', 'IMPERFECT', 'IMPOLITE', 'IMPORTANT', 'IMPORTED', 'IMPOSSIBLE',
             'INCANDESCENT', 'INCOMPETENT', 'INCONCLUSIVE', 'INDUSTRIOUS', 'INCREDIBLE', 'INEXPENSIVE', 'INFAMOUS',
             'INNATE', 'INNOCENT', 'INQUISITIVE', 'INSIDIOUS', 'INSTINCTIVE', 'INTELLIGENT', 'INTERESTING', 'INTERNAL',
             'INVINCIBLE', 'IRATE', 'IRRITATING', 'ITCHY', 'JADED', 'JAGGED', 'JAZZY', 'JEALOUS', 'JITTERY', 'JOBLESS',
             'JOLLY', 'JOYOUS', 'JUDICIOUS', 'JUICY', 'JUMBLED', 'JUMPY', 'JUVENILE', 'KAPUT', 'KEEN', 'KIND',
             'KINDHEARTED', 'KINDLY', 'KNOTTY', 'KNOWING', 'KNOWLEDGEABLE', 'KNOWN', 'LABORED', 'LACKADAISICAL',
             'LACKING', 'LAME', 'LAMENTABLE', 'LANGUID', 'LARGE', 'LAST', 'LATE', 'LAUGHABLE', 'LAVISH', 'LAZY', 'LEAN',
             'LEARNED', 'LEFT', 'LEGAL', 'LETHAL', 'LEVEL', 'LEWD', 'LIGHT', 'LIKE', 'LIKEABLE', 'LIMPING', 'LITERATE',
             'LITTLE', 'LIVELY', 'LIVELY', 'LIVING', 'LONELY', 'LONG', 'LONGING', 'LONG-TERM', 'LOOSE', 'LOPSIDED',
             'LOUD', 'LOUTISH', 'LOVELY', 'LOVING', 'LOW', 'LOWLY', 'LUCKY', 'LUDICROUS', 'LUMPY', 'LUSH', 'LUXURIANT',
             'LYING', 'LYRICAL', 'MACABRE', 'MACHO', 'MADDENING', 'MADLY', 'MAGENTA', 'MAGICAL', 'MAGNIFICENT',
             'MAJESTIC', 'MAKESHIFT', 'MALE', 'MALICIOUS', 'MAMMOTH', 'MANIACAL', 'MANY', 'MARKED', 'MASSIVE',
             'MARRIED', 'MARVELOUS', 'MATERIAL', 'MATERIALISTIC', 'MATURE', 'MEAN', 'MEASLY', 'MEATY', 'MEDICAL',
             'MEEK', 'MELLOW', 'MELODIC', 'MELTED', 'MERCIFUL', 'MERE', 'MESSY', 'MIGHTY', 'MILITARY', 'MILKY',
             'MINDLESS', 'MINIATURE', 'MINOR', 'MISCREANT', 'MISTY', 'MIXED', 'MOANING', 'MODERN', 'MOLDY', 'MOMENTOUS',
             'MOTIONLESS', 'MOUNTAINOUS', 'MUDDLED', 'MUNDANE', 'MURKY', 'MUSHY', 'MUTE', 'MYSTERIOUS', 'NAIVE',
             'NAPPY', 'NARROW', 'NASTY', 'NATURAL', 'NAUGHTY', 'NAUSEATING', 'NEAR', 'NEAT', 'NEBULOUS', 'NECESSARY',
             'NEEDLESS', 'NEEDY', 'NEIGHBORLY', 'NERVOUS', 'NEW', 'NEXT', 'NICE', 'NIFTY', 'NIMBLE', 'NINE', 'NIPPY',
             'NOISELESS', 'NOISY', 'NONCHALANT', 'NONDESCRIPT', 'NONSTOP', 'NORMAL', 'NOSTALGIC', 'NOSY', 'NOXIOUS',
             'NULL', 'NUMBERLESS', 'NUMEROUS', 'NUTRITIOUS', 'NUTTY', 'OAFISH', 'OBEDIENT', 'OBEISANT', 'OBESE',
             'OBNOXIOUS', 'OBSCENE', 'OBSEQUIOUS', 'OBSERVANT', 'OBSOLETE', 'OBTAINABLE', 'OCEANIC', 'ODD', 'OFFBEAT',
             'OLD', 'OLD-FASHIONED', 'OMNISCIENT', 'ONE', 'ONEROUS', 'OPEN', 'OPPOSITE', 'OPTIMAL', 'ORANGE',
             'ORDINARY', 'ORGANIC', 'OSSIFIED', 'OUTGOING', 'OUTRAGEOUS', 'OUTSTANDING', 'OVAL', 'OVERCONFIDENT',
             'OVERJOYED', 'OVERRATED', 'OVERT', 'OVERWROUGHT', 'PAINFUL', 'PAINSTAKING', 'PALE', 'PALTRY', 'PANICKY',
             'PANORAMIC', 'PARALLEL', 'PARCHED', 'PARSIMONIOUS', 'PAST', 'PASTORAL', 'PATHETIC', 'PEACEFUL', 'PENITENT',
             'PERFECT', 'PERIODIC', 'PERMISSIBLE', 'PERPETUAL', 'PETITE', 'PETITE', 'PHOBIC', 'PHYSICAL', 'PICAYUNE',
             'PINK', 'PIQUANT', 'PLACID', 'PLAIN', 'PLANT', 'PLASTIC', 'PLAUSIBLE', 'PLEASANT', 'PLUCKY', 'POINTLESS',
             'POISED', 'POLITE', 'POLITICAL', 'POOR', 'POSSESSIVE', 'POSSIBLE', 'POWERFUL', 'PRECIOUS', 'PREMIUM',
             'PRESENT', 'PRETTY', 'PREVIOUS', 'PRICEY', 'PRICKLY', 'PRIVATE', 'PROBABLE', 'PRODUCTIVE', 'PROFUSE',
             'PROTECTIVE', 'PROUD', 'PSYCHEDELIC', 'PSYCHOTIC', 'PUBLIC', 'PUFFY', 'PUMPED', 'PUNY', 'PURPLE',
             'PURRING', 'PUSHY', 'PUZZLED', 'PUZZLING', 'QUACK', 'QUAINT', 'QUARRELSOME', 'QUESTIONABLE', 'QUICK',
             'QUICKEST', 'QUIET', 'QUIRKY', 'QUIXOTIC', 'QUIZZICAL', 'RABID', 'RACIAL', 'RAGGED', 'RAINY',
             'RAMBUNCTIOUS', 'RAMPANT', 'RAPID', 'RARE', 'RASPY', 'RATTY', 'READY', 'REAL', 'REBEL', 'RECEPTIVE',
             'RECONDITE', 'RED', 'REDUNDANT', 'REFLECTIVE', 'REGULAR', 'RELIEVED', 'REMARKABLE', 'REMINISCENT',
             'REPULSIVE', 'RESOLUTE', 'RESONANT', 'RESPONSIBLE', 'RHETORICAL', 'RICH', 'RIGHT', 'RIGHTEOUS', 'RIGHTFUL',
             'RIGID', 'RIPE', 'RITZY', 'ROASTED', 'ROBUST', 'ROMANTIC', 'ROOMY', 'ROTTEN', 'ROUGH', 'ROUND', 'ROYAL',
             'RUDDY', 'RUDE', 'RURAL', 'RUSTIC', 'RUTHLESS', 'SABLE', 'SAD', 'SAFE', 'SALTY', 'SAME', 'SASSY',
             'SATISFYING', 'SAVORY', 'SCANDALOUS', 'SCARCE', 'SCARED', 'SCARY', 'SCATTERED', 'SCIENTIFIC',
             'SCINTILLATING', 'SCRAWNY', 'SCREECHING', 'SECOND', 'SECOND-HAND', 'SECRET', 'SECRETIVE', 'SEDATE',
             'SEEMLY', 'SELECTIVE', 'SELFISH', 'SEPARATE', 'SERIOUS', 'SHAGGY', 'SHAKY', 'SHALLOW', 'SHARP', 'SHINY',
             'SHIVERING', 'SHOCKING', 'SHORT', 'SHRILL', 'SHUT', 'SHY', 'SICK', 'SILENT', 'SILENT', 'SILKY', 'SILLY',
             'SIMPLE', 'SIMPLISTIC', 'SINCERE', 'SIX', 'SKILLFUL', 'SKINNY', 'SLEEPY', 'SLIM', 'SLIMY', 'SLIPPERY',
             'SLOPPY', 'SLOW', 'SMALL', 'SMART', 'SMELLY', 'SMILING', 'SMOGGY', 'SMOOTH', 'SNEAKY', 'SNOBBISH',
             'SNOTTY', 'SOFT', 'SOGGY', 'SOLID', 'SOMBER', 'SOPHISTICATED', 'SORDID', 'SORE', 'SORE', 'SOUR',
             'SPARKLING', 'SPECIAL', 'SPECTACULAR', 'SPICY', 'SPIFFY', 'SPIKY', 'SPIRITUAL', 'SPITEFUL', 'SPLENDID',
             'SPOOKY', 'SPOTLESS', 'SPOTTED', 'SPOTTY', 'SPURIOUS', 'SQUALID', 'SQUARE', 'SQUEALING', 'SQUEAMISH',
             'STAKING', 'STALE', 'STANDING', 'STATUESQUE', 'STEADFAST', 'STEADY', 'STEEP', 'STEREOTYPED', 'STICKY',
             'STIFF', 'STIMULATING', 'STINGY', 'STORMY', 'STRAIGHT', 'STRANGE', 'STRIPED', 'STRONG', 'STUPENDOUS',
             'STUPID', 'STURDY', 'SUBDUED', 'SUBSEQUENT', 'SUBSTANTIAL', 'SUCCESSFUL', 'SUCCINCT', 'SUDDEN', 'SULKY',
             'SUPER', 'SUPERB', 'SUPERFICIAL', 'SUPREME', 'SWANKY', 'SWEET', 'SWELTERING', 'SWIFT', 'SYMPTOMATIC',
             'SYNONYMOUS', 'TABOO', 'TACIT', 'TACKY', 'TALENTED', 'TALL', 'TAME', 'TAN', 'TANGIBLE', 'TANGY', 'TART',
             'TASTEFUL', 'TASTELESS', 'TASTY', 'TAWDRY', 'TEARFUL', 'TEDIOUS', 'TEENY', 'TEENY-TINY', 'TELLING',
             'TEMPORARY', 'TEN', 'TENDER', 'TENSE', 'TENSE', 'TENUOUS', 'TERRIBLE', 'TERRIFIC', 'TESTED', 'TESTY',
             'THANKFUL', 'THERAPEUTIC', 'THICK', 'THIN', 'THINKABLE', 'THIRD', 'THIRSTY', 'THIRSTY', 'THOUGHTFUL',
             'THOUGHTLESS', 'THREATENING', 'THREE', 'THUNDERING', 'TIDY', 'TIGHT', 'TIGHTFISTED', 'TINY', 'TIRED',
             'TIRESOME', 'TOOTHSOME', 'TORPID', 'TOUGH', 'TOWERING', 'TRANQUIL', 'TRASHY', 'TREMENDOUS', 'TRICKY',
             'TRITE', 'TROUBLED', 'TRUCULENT', 'TRUE', 'TRUTHFUL', 'TWO', 'TYPICAL', 'UBIQUITOUS', 'UGLIEST', 'UGLY',
             'ULTRA', 'UNABLE', 'UNACCOUNTABLE', 'UNADVISED', 'UNARMED', 'UNBECOMING', 'UNBIASED', 'UNCOVERED',
             'UNDERSTOOD', 'UNDESIRABLE', 'UNEQUAL', 'UNEQUALED', 'UNEVEN', 'UNHEALTHY', 'UNINTERESTED', 'UNIQUE',
             'UNKEMPT', 'UNKNOWN', 'UNNATURAL', 'UNRULY', 'UNSIGHTLY', 'UNSUITABLE', 'UNTIDY', 'UNUSED', 'UNUSUAL',
             'UNWIELDY', 'UNWRITTEN', 'UPBEAT', 'UPPITY', 'UPSET', 'UPTIGHT', 'USED', 'USEFUL', 'USELESS', 'UTOPIAN',
             'UTTER', 'UTTERMOST', 'VACUOUS', 'VAGABOND', 'VAGUE', 'VALUABLE', 'VARIOUS', 'VAST', 'VENGEFUL',
             'VENOMOUS', 'VERDANT', 'VERSED', 'VICTORIOUS', 'VIGOROUS', 'VIOLENT', 'VIOLET', 'VIVACIOUS', 'VOICELESS',
             'VOLATILE', 'VORACIOUS', 'VULGAR', 'WACKY', 'WAGGISH', 'WAITING', 'WAKEFUL', 'WANDERING', 'WANTING',
             'WARLIKE', 'WARM', 'WARY', 'WASTEFUL', 'WATERY', 'WEAK', 'WEALTHY', 'WEARY', 'WELL-GROOMED', 'WELL-MADE',
             'WELL-OFF', 'WELL-TO-DO', 'WET', 'WHIMSICAL', 'WHISPERING', 'WHITE', 'WHOLE', 'WHOLESALE', 'WICKED',
             'WIDE', 'WIDE-EYED', 'WIGGLY', 'WILD', 'WILLING', 'WINDY', 'WIRY', 'WISE', 'WISTFUL', 'WITTY', 'WOEBEGONE',
             'WOMANLY', 'WONDERFUL', 'WOODEN', 'WOOZY', 'WORKABLE', 'WORRIED', 'WORTHLESS', 'WRATHFUL', 'WRETCHED',
             'WRONG', 'WRY', 'YELLOW', 'YIELDING', 'YOUNG', 'YOUTHFUL', 'YUMMY', 'ZANY', 'ZEALOUS', 'ZESTY', 'ZIPPY',
             'ZONKED', 'ACCOUNT', 'ACHIEVER', 'ACOUSTICS', 'ACT', 'ACTION', 'ACTIVITY', 'ACTOR', 'ADDITION',
             'ADJUSTMENT', 'ADVERTISEMENT', 'ADVICE', 'AFTERMATH', 'AFTERNOON', 'AFTERTHOUGHT', 'AGREEMENT', 'AIR',
             'AIRPLANE', 'AIRPORT', 'ALARM', 'AMOUNT', 'AMUSEMENT', 'ANGER', 'ANGLE', 'ANIMAL', 'ANTS', 'APPARATUS',
             'APPAREL', 'APPLIANCE', 'APPROVAL', 'ARCH', 'ARGUMENT', 'ARITHMETIC', 'ARM', 'ARMY', 'ART', 'ATTACK',
             'ATTRACTION', 'AUNT', 'AUTHORITY', 'BABIES', 'BABY', 'BACK', 'BADGE', 'BAG', 'BAIT', 'BALANCE', 'BALL',
             'BASE', 'BASEBALL', 'BASIN', 'BASKET', 'BASKETBALL', 'BAT', 'BATH', 'BATTLE', 'BEAD', 'BEAR', 'BED',
             'BEDROOM', 'BEDS', 'BEE', 'BEEF', 'BEGINNER', 'BEHAVIOR', 'BELIEF', 'BELIEVE', 'BELL', 'BELLS', 'BERRY',
             'BIKE', 'BIKES', 'BIRD', 'BIRDS', 'BIRTH', 'BIRTHDAY', 'BIT', 'BITE', 'BLADE', 'BLOOD', 'BLOW', 'BOARD',
             'BOAT', 'BOMB', 'BONE', 'BOOK', 'BOOKS', 'BOOT', 'BORDER', 'BOTTLE', 'BOUNDARY', 'BOX', 'BOY', 'BRAKE',
             'BRANCH', 'BRASS', 'BREATH', 'BRICK', 'BRIDGE', 'BROTHER', 'BUBBLE', 'BUCKET', 'BUILDING', 'BULB', 'BURST',
             'BUSHES', 'BUSINESS', 'BUTTER', 'BUTTON', 'CABBAGE', 'CABLE', 'CACTUS', 'CAKE', 'CAKES', 'CALCULATOR',
             'CALENDAR', 'CAMERA', 'CAMP', 'CAN', 'CANNON', 'CANVAS', 'CAP', 'CAPTION', 'CAR', 'CARD', 'CARE',
             'CARPENTER', 'CARRIAGE', 'CARS', 'CART', 'CAST', 'CAT', 'CATS', 'CATTLE', 'CAUSE', 'CAVE', 'CELERY',
             'CELLAR', 'CEMETERY', 'CENT', 'CHALK', 'CHANCE', 'CHANGE', 'CHANNEL', 'CHEESE', 'CHERRIES', 'CHERRY',
             'CHESS', 'CHICKEN', 'CHICKENS', 'CHILDREN', 'CHIN', 'CHURCH', 'CIRCLE', 'CLAM', 'CLASS', 'CLOTH', 'CLOVER',
             'CLUB', 'COACH', 'COAL', 'COAST', 'COAT', 'COBWEB', 'COIL', 'COLLAR', 'COLOR', 'COMMITTEE', 'COMPANY',
             'COMPARISON', 'COMPETITION', 'CONDITION', 'CONNECTION', 'CONTROL', 'COOK', 'COPPER', 'CORN', 'COUGH',
             'COUNTRY', 'COVER', 'COW', 'COWS', 'CRACK', 'CRACKER', 'CRATE', 'CRAYON', 'CREAM', 'CREATOR', 'CREATURE',
             'CREDIT', 'CRIB', 'CRIME', 'CROOK', 'CROW', 'CROWD', 'CROWN', 'CUB', 'CUP', 'CURRENT', 'CURTAIN', 'CURVE',
             'CUSHION', 'DAD', 'DAUGHTER', 'DAY', 'DEATH', 'DEBT', 'DECISION', 'DEER', 'DEGREE', 'DESIGN', 'DESIRE',
             'DESK', 'DESTRUCTION', 'DETAIL', 'DEVELOPMENT', 'DIGESTION', 'DIME', 'DINNER', 'DINOSAURS', 'DIRECTION',
             'DIRT', 'DISCOVERY', 'DISCUSSION', 'DISTANCE', 'DISTRIBUTION', 'DIVISION', 'DOCK', 'DOCTOR', 'DOG', 'DOGS',
             'DOLL', 'DOLLS', 'DONKEY', 'DOOR', 'DOWNTOWN', 'DRAIN', 'DRAWER', 'DRESS', 'DRINK', 'DRIVING', 'DROP',
             'DUCK', 'DUCKS', 'DUST', 'EAR', 'EARTH', 'EARTHQUAKE', 'EDGE', 'EDUCATION', 'EFFECT', 'EGG', 'EGGNOG',
             'EGGS', 'ELBOW', 'END', 'ENGINE', 'ERROR', 'EVENT', 'EXAMPLE', 'EXCHANGE', 'EXISTENCE', 'EXPANSION',
             'EXPERIENCE', 'EXPERT', 'EYE', 'EYES', 'FACE', 'FACT', 'FAIRIES', 'FALL', 'FANG', 'FARM', 'FEAR',
             'FEELING', 'FIELD', 'FINGER', 'FINGER', 'FIRE', 'FIREMAN', 'FISH', 'FLAG', 'FLAME', 'FLAVOR', 'FLESH',
             'FLIGHT', 'FLOCK', 'FLOOR', 'FLOWER', 'FLOWERS', 'FLY', 'FOG', 'FOLD', 'FOOD', 'FOOT', 'FORCE', 'FORK',
             'FORM', 'FOWL', 'FRAME', 'FRICTION', 'FRIEND', 'FRIENDS', 'FROG', 'FROGS', 'FRONT', 'FRUIT', 'FUEL',
             'FURNITURE', 'GATE', 'GEESE', 'GHOST', 'GIANTS', 'GIRAFFE', 'GIRL', 'GIRLS', 'GLASS', 'GLOVE', 'GOLD',
             'GOVERNMENT', 'GOVERNOR', 'GRADE', 'GRAIN', 'GRANDFATHER', 'GRANDMOTHER', 'GRAPE', 'GRASS', 'GRIP',
             'GROUND', 'GROUP', 'GROWTH', 'GUIDE', 'GUITAR', 'GUN', 'HAIR', 'HAIRCUT', 'HALL', 'HAMMER', 'HAND',
             'HANDS', 'HARBOR', 'HARMONY', 'HAT', 'HATE', 'HEAD', 'HEALTH', 'HEAT', 'HILL', 'HISTORY', 'HOBBIES',
             'HOLE', 'HOLIDAY', 'HOME', 'HONEY', 'HOOK', 'HOPE', 'HORN', 'HORSE', 'HORSES', 'HOSE', 'HOSPITAL', 'HOT',
             'HOUR', 'HOUSE', 'HOUSES', 'HUMOR', 'HYDRANT', 'ICE', 'ICICLE', 'IDEA', 'IMPULSE', 'INCOME', 'INCREASE',
             'INDUSTRY', 'INK', 'INSECT', 'INSTRUMENT', 'INSURANCE', 'INTEREST', 'INVENTION', 'IRON', 'ISLAND', 'JAIL',
             'JAM', 'JAR', 'JEANS', 'JELLY', 'JELLYFISH', 'JEWEL', 'JOIN', 'JUDGE', 'JUICE', 'JUMP', 'KETTLE', 'KEY',
             'KICK', 'KISS', 'KITTENS', 'KITTY', 'KNEE', 'KNIFE', 'KNOT', 'KNOWLEDGE', 'LABORER', 'LACE', 'LADYBUG',
             'LAKE', 'LAMP', 'LAND', 'LANGUAGE', 'LAUGH', 'LEATHER', 'LEG', 'LEGS', 'LETTER', 'LETTERS', 'LETTUCE',
             'LEVEL', 'LIBRARY', 'LIMIT', 'LINE', 'LINEN', 'LIP', 'LIQUID', 'LOAF', 'LOCK', 'LOCKET', 'LOOK', 'LOSS',
             'LOVE', 'LOW', 'LUMBER', 'LUNCH', 'LUNCHROOM', 'MACHINE', 'MAGIC', 'MAID', 'MAILBOX', 'MAN', 'MARBLE',
             'MARK', 'MARKET', 'MASK', 'MASS', 'MATCH', 'MEAL', 'MEASURE', 'MEAT', 'MEETING', 'MEMORY', 'MEN', 'METAL',
             'MICE', 'MIDDLE', 'MILK', 'MIND', 'MINE', 'MINISTER', 'MINT', 'MINUTE', 'MIST', 'MITTEN', 'MOM', 'MONEY',
             'MONKEY', 'MONTH', 'MOON', 'MORNING', 'MOTHER', 'MOTION', 'MOUNTAIN', 'MOUTH', 'MOVE', 'MUSCLE', 'NAME',
             'NATION', 'NECK', 'NEED', 'NEEDLE', 'NERVE', 'NEST', 'NIGHT', 'NOISE', 'NORTH', 'NOSE', 'NOTE', 'NOTEBOOK',
             'NUMBER', 'NUT', 'OATMEAL', 'OBSERVATION', 'OCEAN', 'OFFER', 'OFFICE', 'OIL', 'ORANGE', 'ORANGES', 'ORDER',
             'OVEN', 'PAGE', 'PAIL', 'PAN', 'PANCAKE', 'PAPER', 'PARCEL', 'PART', 'PARTNER', 'PARTY', 'PASSENGER',
             'PAYMENT', 'PEACE', 'PEAR', 'PEN', 'PENCIL', 'PERSON', 'PEST', 'PET', 'PETS', 'PICKLE', 'PICTURE', 'PIE',
             'PIES', 'PIG', 'PIGS', 'PIN', 'PIPE', 'PIZZAS', 'PLACE', 'PLANE', 'PLANES', 'PLANT', 'PLANTATION',
             'PLANTS', 'PLASTIC', 'PLATE', 'PLAY', 'PLAYGROUND', 'PLEASURE', 'PLOT', 'PLOUGH', 'POCKET', 'POINT',
             'POISON', 'POLLUTION', 'POPCORN', 'PORTER', 'POSITION', 'POT', 'POTATO', 'POWDER', 'POWER', 'PRICE',
             'PRODUCE', 'PROFIT', 'PROPERTY', 'PROSE', 'PROTEST', 'PULL', 'PUMP', 'PUNISHMENT', 'PURPOSE', 'PUSH',
             'QUARTER', 'QUARTZ', 'QUEEN', 'QUESTION', 'QUICKSAND', 'QUIET', 'QUILL', 'QUILT', 'QUINCE', 'QUIVER',
             'RABBIT', 'RABBITS', 'RAIL', 'RAILWAY', 'RAIN', 'RAINSTORM', 'RAKE', 'RANGE', 'RAT', 'RATE', 'RAY',
             'REACTION', 'READING', 'REASON', 'RECEIPT', 'RECESS', 'RECORD', 'REGRET', 'RELATION', 'RELIGION',
             'REPRESENTATIVE', 'REQUEST', 'RESPECT', 'REST', 'REWARD', 'RHYTHM', 'RICE', 'RIDDLE', 'RIFLE', 'RING',
             'RINGS', 'RIVER', 'ROAD', 'ROBIN', 'ROCK', 'ROD', 'ROLL', 'ROOF', 'ROOM', 'ROOT', 'ROSE', 'ROUTE', 'RUB',
             'RULE', 'RUN', 'SACK', 'SAIL', 'SALT', 'SAND', 'SCALE', 'SCARECROW', 'SCARF', 'SCENE', 'SCENT', 'SCHOOL',
             'SCIENCE', 'SCISSORS', 'SCREW', 'SEA', 'SEASHORE', 'SEAT', 'SECRETARY', 'SEED', 'SELECTION', 'SELF',
             'SENSE', 'SERVANT', 'SHADE', 'SHAKE', 'SHAME', 'SHAPE', 'SHEEP', 'SHEET', 'SHELF', 'SHIP', 'SHIRT',
             'SHOCK', 'SHOE', 'SHOES', 'SHOP', 'SHOW', 'SIDE', 'SIDEWALK', 'SIGN', 'SILK', 'SILVER', 'SINK', 'SISTER',
             'SISTERS', 'SIZE', 'SKATE', 'SKIN', 'SKIRT', 'SKY', 'SLAVE', 'SLEEP', 'SLEET', 'SLIP', 'SLOPE', 'SMASH',
             'SMELL', 'SMILE', 'SMOKE', 'SNAIL', 'SNAILS', 'SNAKE', 'SNAKES', 'SNEEZE', 'SNOW', 'SOAP', 'SOCIETY',
             'SOCK', 'SODA', 'SOFA', 'SON', 'SONG', 'SONGS', 'SORT', 'SOUND', 'SOUP', 'SPACE', 'SPADE', 'SPARK',
             'SPIDERS', 'SPONGE', 'SPOON', 'SPOT', 'SPRING', 'SPY', 'SQUARE', 'SQUIRREL', 'STAGE', 'STAMP', 'STAR',
             'START', 'STATEMENT', 'STATION', 'STEAM', 'STEEL', 'STEM', 'STEP', 'STEW', 'STICK', 'STICKS', 'STITCH',
             'STOCKING', 'STOMACH', 'STONE', 'STOP', 'STORE', 'STORY', 'STOVE', 'STRANGER', 'STRAW', 'STREAM', 'STREET',
             'STRETCH', 'STRING', 'STRUCTURE', 'SUBSTANCE', 'SUGAR', 'SUGGESTION', 'SUIT', 'SUMMER', 'SUN', 'SUPPORT',
             'SURPRISE', 'SWEATER', 'SWIM', 'SWING', 'SYSTEM', 'TABLE', 'TAIL', 'TALK', 'TANK', 'TASTE', 'TAX',
             'TEACHING', 'TEAM', 'TEETH', 'TEMPER', 'TENDENCY', 'TENT', 'TERRITORY', 'TEST', 'TEXTURE', 'THEORY',
             'THING', 'THINGS', 'THOUGHT', 'THREAD', 'THRILL', 'THROAT', 'THRONE', 'THUMB', 'THUNDER', 'TICKET',
             'TIGER', 'TIME', 'TIN', 'TITLE', 'TOAD', 'TOE', 'TOES', 'TOMATOES', 'TONGUE', 'TOOTH', 'TOOTHBRUSH',
             'TOOTHPASTE', 'TOP', 'TOUCH', 'TOWN', 'TOY', 'TOYS', 'TRADE', 'TRAIL', 'TRAIN', 'TRAINS', 'TRAMP',
             'TRANSPORT', 'TRAY', 'TREATMENT', 'TREE', 'TREES', 'TRICK', 'TRIP', 'TROUBLE', 'TROUSERS', 'TRUCK',
             'TRUCKS', 'TUB', 'TURKEY', 'TURN', 'TWIG', 'TWIST', 'UMBRELLA', 'UNCLE', 'UNDERWEAR', 'UNIT', 'USE',
             'VACATION', 'VALUE', 'VAN', 'VASE', 'VEGETABLE', 'VEIL', 'VEIN', 'VERSE', 'VESSEL', 'VEST', 'VIEW',
             'VISITOR', 'VOICE', 'VOLCANO', 'VOLLEYBALL', 'VOYAGE', 'WALK', 'WALL', 'WAR', 'WASH', 'WASTE', 'WATCH',
             'WATER', 'WAVE', 'WAVES', 'WAX', 'WAY', 'WEALTH', 'WEATHER', 'WEEK', 'WEIGHT', 'WHEEL', 'WHIP', 'WHISTLE',
             'WILDERNESS', 'WIND', 'WINDOW', 'WINE', 'WING', 'WINTER', 'WIRE', 'WISH', 'WOMAN', 'WOMEN', 'WOOD', 'WOOL',
             'WORD', 'WORK', 'WORM', 'WOUND', 'WREN', 'WRENCH', 'WRIST', 'WRITER', 'WRITING', 'YAK', 'YAM', 'YARD',
             'YARN', 'YEAR', 'YOKE', 'ZEBRA', 'ZEPHYR', 'ZINC', 'ZIPPER', 'ZOO', 'ACCEPT', 'ADD', 'ADMIRE', 'ADMIT',
             'ADVISE', 'AFFORD', 'AGREE', 'ALERT', 'ALLOW', 'AMUSE', 'ANALYSE', 'ANNOUNCE', 'ANNOY', 'ANSWER',
             'APOLOGISE', 'APPEAR', 'APPLAUD', 'APPRECIATE', 'APPROVE', 'ARGUE', 'ARRANGE', 'ARREST', 'ARRIVE', 'ASK',
             'ATTACH', 'ATTACK', 'ATTEMPT', 'ATTEND', 'ATTRACT', 'AVOID', 'BACK', 'BAKE', 'BALANCE', 'BAN', 'BANG',
             'BARE', 'BAT', 'BATHE', 'BATTLE', 'BEAM', 'BEG', 'BEHAVE', 'BELONG', 'BLEACH', 'BLESS', 'BLIND', 'BLINK',
             'BLOT', 'BLUSH', 'BOAST', 'BOIL', 'BOLT', 'BOMB', 'BOOK', 'BORE', 'BORROW', 'BOUNCE', 'BOW', 'BOX',
             'BRAKE', 'BRANCH', 'BREATHE', 'BRUISE', 'BRUSH', 'BUBBLE', 'BUMP', 'BURN', 'BURY', 'BUZZ', 'CALCULATE',
             'CALL', 'CAMP', 'CARE', 'CARRY', 'CARVE', 'CAUSE', 'CHALLENGE', 'CHANGE', 'CHARGE', 'CHASE', 'CHEAT',
             'CHECK', 'CHEER', 'CHEW', 'CHOKE', 'CHOP', 'CLAIM', 'CLAP', 'CLEAN', 'CLEAR', 'CLIP', 'CLOSE', 'COACH',
             'COIL', 'COLLECT', 'COLOUR', 'COMB', 'COMMAND', 'COMMUNICATE', 'COMPARE', 'COMPETE', 'COMPLAIN',
             'COMPLETE', 'CONCENTRATE', 'CONCERN', 'CONFESS', 'CONFUSE', 'CONNECT', 'CONSIDER', 'CONSIST', 'CONTAIN',
             'CONTINUE', 'COPY', 'CORRECT', 'COUGH', 'COUNT', 'COVER', 'CRACK', 'CRASH', 'CRAWL', 'CROSS', 'CRUSH',
             'CRY', 'CURE', 'CURL', 'CURVE', 'CYCLE', 'DAM', 'DAMAGE', 'DANCE', 'DARE', 'DECAY', 'DECEIVE', 'DECIDE',
             'DECORATE', 'DELAY', 'DELIGHT', 'DELIVER', 'DEPEND', 'DESCRIBE', 'DESERT', 'DESERVE', 'DESTROY', 'DETECT',
             'DEVELOP', 'DISAGREE', 'DISAPPEAR', 'DISAPPROVE', 'DISARM', 'DISCOVER', 'DISLIKE', 'DIVIDE', 'DOUBLE',
             'DOUBT', 'DRAG', 'DRAIN', 'DREAM', 'DRESS', 'DRIP', 'DROP', 'DROWN', 'DRUM', 'DRY', 'DUST', 'EARN',
             'EDUCATE', 'EMBARRASS', 'EMPLOY', 'EMPTY', 'ENCOURAGE', 'END', 'ENJOY', 'ENTER', 'ENTERTAIN', 'ESCAPE',
             'EXAMINE', 'EXCITE', 'EXCUSE', 'EXERCISE', 'EXIST', 'EXPAND', 'EXPECT', 'EXPLAIN', 'EXPLODE', 'EXTEND',
             'FACE', 'FADE', 'FAIL', 'FANCY', 'FASTEN', 'FAX', 'FEAR', 'FENCE', 'FETCH', 'FILE', 'FILL', 'FILM', 'FIRE',
             'FIT', 'FIX', 'FLAP', 'FLASH', 'FLOAT', 'FLOOD', 'FLOW', 'FLOWER', 'FOLD', 'FOLLOW', 'FOOL', 'FORCE',
             'FORM', 'FOUND', 'FRAME', 'FRIGHTEN', 'FRY', 'GATHER', 'GAZE', 'GLOW', 'GLUE', 'GRAB', 'GRATE', 'GREASE',
             'GREET', 'GRIN', 'GRIP', 'GROAN', 'GUARANTEE', 'GUARD', 'GUESS', 'GUIDE', 'HAMMER', 'HAND', 'HANDLE',
             'HANG', 'HAPPEN', 'HARASS', 'HARM', 'HATE', 'HAUNT', 'HEAD', 'HEAL', 'HEAP', 'HEAT', 'HELP', 'HOOK', 'HOP',
             'HOPE', 'HOVER', 'HUG', 'HUM', 'HUNT', 'HURRY', 'IDENTIFY', 'IGNORE', 'IMAGINE', 'IMPRESS', 'IMPROVE',
             'INCLUDE', 'INCREASE', 'INFLUENCE', 'INFORM', 'INJECT', 'INJURE', 'INSTRUCT', 'INTEND', 'INTEREST',
             'INTERFERE', 'INTERRUPT', 'INTRODUCE', 'INVENT', 'INVITE', 'IRRITATE', 'ITCH', 'JAIL', 'JAM', 'JOG',
             'JOIN', 'JOKE', 'JUDGE', 'JUGGLE', 'JUMP', 'KICK', 'KILL', 'KISS', 'KNEEL', 'KNIT', 'KNOCK', 'KNOT',
             'LABEL', 'LAND', 'LAST', 'LAUGH', 'LAUNCH', 'LEARN', 'LEVEL', 'LICENSE', 'LICK', 'LIE', 'LIGHTEN', 'LIKE',
             'LIST', 'LISTEN', 'LIVE', 'LOAD', 'LOCK', 'LONG', 'LOOK', 'LOVE', 'MAN', 'MANAGE', 'MARCH', 'MARK',
             'MARRY', 'MATCH', 'MATE', 'MATTER', 'MEASURE', 'MEDDLE', 'MELT', 'MEMORISE', 'MEND', 'MESS UP', 'MILK',
             'MINE', 'MISS', 'MIX', 'MOAN', 'MOOR', 'MOURN', 'MOVE', 'MUDDLE', 'MUG', 'MULTIPLY', 'MURDER', 'NAIL',
             'NAME', 'NEED', 'NEST', 'NOD', 'NOTE', 'NOTICE', 'NUMBER', 'OBEY', 'OBJECT', 'OBSERVE', 'OBTAIN', 'OCCUR',
             'OFFEND', 'OFFER', 'OPEN', 'ORDER', 'OVERFLOW', 'OWE', 'OWN', 'PACK', 'PADDLE', 'PAINT', 'PARK', 'PART',
             'PASS', 'PASTE', 'PAT', 'PAUSE', 'PECK', 'PEDAL', 'PEEL', 'PEEP', 'PERFORM', 'PERMIT', 'PHONE', 'PICK',
             'PINCH', 'PINE', 'PLACE', 'PLAN', 'PLANT', 'PLAY', 'PLEASE', 'PLUG', 'POINT', 'POKE', 'POLISH', 'POP',
             'POSSESS', 'POST', 'POUR', 'PRACTISE', 'PRAY', 'PREACH', 'PRECEDE', 'PREFER', 'PREPARE', 'PRESENT',
             'PRESERVE', 'PRESS', 'PRETEND', 'PREVENT', 'PRICK', 'PRINT', 'PRODUCE', 'PROGRAM', 'PROMISE', 'PROTECT',
             'PROVIDE', 'PULL', 'PUMP', 'PUNCH', 'PUNCTURE', 'PUNISH', 'PUSH', 'QUESTION', 'QUEUE', 'RACE', 'RADIATE',
             'RAIN', 'RAISE', 'REACH', 'REALISE', 'RECEIVE', 'RECOGNISE', 'RECORD', 'REDUCE', 'REFLECT', 'REFUSE',
             'REGRET', 'REIGN', 'REJECT', 'REJOICE', 'RELAX', 'RELEASE', 'RELY', 'REMAIN', 'REMEMBER', 'REMIND',
             'REMOVE', 'REPAIR', 'REPEAT', 'REPLACE', 'REPLY', 'REPORT', 'REPRODUCE', 'REQUEST', 'RESCUE', 'RETIRE',
             'RETURN', 'RHYME', 'RINSE', 'RISK', 'ROB', 'ROCK', 'ROLL', 'ROT', 'RUB', 'RUIN', 'RULE', 'RUSH', 'SACK',
             'SAIL', 'SATISFY', 'SAVE', 'SAW', 'SCARE', 'SCATTER', 'SCOLD', 'SCORCH', 'SCRAPE', 'SCRATCH', 'SCREAM',
             'SCREW', 'SCRIBBLE', 'SCRUB', 'SEAL', 'SEARCH', 'SEPARATE', 'SERVE', 'SETTLE', 'SHADE', 'SHARE', 'SHAVE',
             'SHELTER', 'SHIVER', 'SHOCK', 'SHOP', 'SHRUG', 'SIGH', 'SIGN', 'SIGNAL', 'SIN', 'SIP', 'SKI', 'SKIP',
             'SLAP', 'SLIP', 'SLOW', 'SMASH', 'SMELL', 'SMILE', 'SMOKE', 'SNATCH', 'SNEEZE', 'SNIFF', 'SNORE', 'SNOW',
             'SOAK', 'SOOTHE', 'SOUND', 'SPARE', 'SPARK', 'SPARKLE', 'SPELL', 'SPILL', 'SPOIL', 'SPOT', 'SPRAY',
             'SPROUT', 'SQUASH', 'SQUEAK', 'SQUEAL', 'SQUEEZE', 'STAIN', 'STAMP', 'STARE', 'START', 'STAY', 'STEER',
             'STEP', 'STIR', 'STITCH', 'STOP', 'STORE', 'STRAP', 'STRENGTHEN', 'STRETCH', 'STRIP', 'STROKE', 'STUFF',
             'SUBTRACT', 'SUCCEED', 'SUCK', 'SUFFER', 'SUGGEST', 'SUIT', 'SUPPLY', 'SUPPORT', 'SUPPOSE', 'SURPRISE',
             'SURROUND', 'SUSPECT', 'SUSPEND', 'SWITCH', 'TALK', 'TAME', 'TAP', 'TASTE', 'TEASE', 'TELEPHONE', 'TEMPT',
             'TERRIFY', 'TEST', 'THANK', 'THAW', 'TICK', 'TICKLE', 'TIE', 'TIME', 'TIP', 'TIRE', 'TOUCH', 'TOUR', 'TOW',
             'TRACE', 'TRADE', 'TRAIN', 'TRANSPORT', 'TRAP', 'TRAVEL', 'TREAT', 'TREMBLE', 'TRICK', 'TRIP', 'TROT',
             'TROUBLE', 'TRUST', 'TRY', 'TUG', 'TUMBLE', 'TURN', 'TWIST', 'TYPE', 'UNDRESS', 'UNFASTEN', 'UNITE',
             'UNLOCK', 'UNPACK', 'UNTIDY', 'USE', 'VANISH', 'VISIT', 'WAIL', 'WAIT', 'WALK', 'WANDER', 'WANT', 'WARM',
             'WARN', 'WASH', 'WASTE', 'WATCH', 'WATER', 'WAVE', 'WEIGH', 'WELCOME', 'WHINE', 'WHIP', 'WHIRL', 'WHISPER',
             'WHISTLE', 'WINK', 'WIPE', 'WISH', 'WOBBLE', 'WONDER', 'WORK', 'WORRY', 'WRAP', 'WRECK', 'WRESTLE',
             'WRIGGLE', 'X-RAY', 'YAWN', 'YELL', 'ZIP', 'ZOOM']

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
          PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"),
          PhotoImage(file="images/hang11.png")]


def newgame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    img_label.config(image=photos[0])
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    label_word.set(" ".join("_" * len(the_word)))


def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(the_word_withSpaces)
        guessed = list(label_word.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                label_word.set("".join(guessed))
                if label_word.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You won the Game")
                    newgame()
        else:
            numberOfGuesses += 1
            img_label.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Sorry, Game Over ")


img_label = Label(window)
img_label.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
img_label.config(image=photos[0])

label_word = StringVar()
Label(window, textvariable=label_word, font=("Conscias 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

n = 0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row=1 + n // 9,
                                                                                              column=n % 9)
    n += 1

Button(window, text="New \n Game", command=lambda: newgame(), font=("Helvetica 10 bold")).grid(row=3, column=8,
                                                                                               sticky="NSWE")

newgame()
window.mainloop()
