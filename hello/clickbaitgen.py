from pick_word import *

object = PairedType('source_words/object.txt')
subject = PairedType('source_words/subject.txt')
secondary = OneType('source_words/secondary.txt')
researcher_action = PairedType('source_words/researcher_action.txt')
subject_action_intrans = PairedType('source_words/subject_action_intrans.txt')
subject_action_trans = PairedType('source_words/subject_action_trans.txt')
researcher = GenderedType('source_words/researcher.txt')
person_type = PairedType('source_words/person_type.txt')
number = NumberType()
adjective = OneType('source_words/adjective.txt')
field = OneType('source_words/field.txt')
research_type = PairedType('source_words/research_type.txt')
researcher_type = PairedType('source_words/researcher_type.txt')

def create_bait():
    i = random.randint(0, 37)
    #i = 38
    print i

    if i == 0:
        s = "{0} try to make {1} for {2}. {3}".format(
            research_type.pick_plural(), object.pick_plural(), subject.pick_plural(), secondary.pick())
    elif i == 1:
        s = "This {0} was forced to {1} because it didn't have {2}. {3}".format(
            subject.pick_single(), subject_action_intrans.pick_single(), object.pick_single(), secondary.pick())
    elif i == 2:
        s = "This {0} will prove you've been {1} {2} wrong your whole life.".format(
            research_type.pick_single(), researcher_action.pick_plural(), object.pick_plural())
    elif i == 3:
        x = person_type.pick_single()
        s = "Was {0} {1} {2}?".format(
            researcher.pick()[0], a_an(x), x)
    elif i == 4:
        s = "{0} {1} that {2} like {3}.".format(
            number.pick(), subject.pick_plural(), subject_action_intrans.pick_single(), object.pick_plural())
    elif i == 5:
        s = "{0} {1} that the {2} {3} won't {4}.".format(
            number.pick(), object.pick_plural(), adjective.pick(), subject.pick_plural(), subject_action_intrans.pick_single())
    elif i == 6:
        s = "{0} {1} that can't be explained by {2}.".format(
            number.pick(), object.pick_plural(), subject_action_intrans.pick_plural())
    elif i == 7:
        x1 = researcher_type.pick_single()
        x2 = subject.pick_single()
        s = "{} {} tried to {} the {} of {} {}. {}".format(
            a_an(x1), x1, researcher_action.pick_single(), object.pick_single(), a_an(x2), x2, secondary.pick())
    elif i == 8:
        s = "{0} {1} {2} that can be verified by {3} {4}.".format(
            number.pick(), adjective.pick(), object.pick_plural(), researcher_action.pick_plural(), subject.pick_plural())
    elif i == 9:
        x1 = researcher_type.pick_single()
        x2 = object.pick_single()
        s = "{} {} tries to {} {} {}. {}".format(
            a_an(x1), x1, researcher_action.pick_single(), a_an(x2), x2, secondary.pick())
    elif i == 10:
        s = "{0} {1} that {2} {3}.".format(
            number.pick(), object.pick_plural(), subject.pick_plural(), subject_action_trans.pick_single())
    elif i == 11:
        s = "Was {0} wrong about {1}?".format(
            researcher.pick()[0], object.pick_plural())
    elif i == 12:
        s = "Is {0} wrong about {1}?".format(
            field.pick(), object.pick_plural())
    elif i == 13:
        s = "This {0} about {1} says that {2} should {3} {4}.".format(
            research_type.pick_single(), object.pick_plural(), researcher_type.pick_plural(),
            researcher_action.pick_plural(), subject.pick_plural())
    elif i == 14:
        s = "Did {0} {1} {2}?".format(
            researcher.pick()[0], researcher_action.pick_single(), subject.pick_plural())
    elif i == 15:
        s = "Who knew {0} {1} could be so {2}?".format(
            adjective.pick(), object.pick_plural(), adjective.pick())
    elif i == 16:
        s = "Do {0} {1} really cause {2} {3}?".format(
            adjective.pick(), object.pick_plural(), adjective.pick(), object.pick_plural())
    elif i == 17:
        s = "{0} find new {1} {2} that could let {3} {4}!".format(
            researcher_type.pick_plural(), adjective.pick(), object.pick_single(), object.pick_plural(), subject_action_intrans.pick_single())
    elif i == 18:
        s = "The truth about {0} {1}.".format(
            adjective.pick(), object.pick_plural())
    elif i == 19:
        s = "Have {0} been lying about {1} {2}?".format(
            researcher_type.pick_plural(), adjective.pick(), object.pick_plural())
    elif i == 20:
        s = "Meet the Bad-Ass {} who changed the way {} {} {}.".format(
            researcher_type.pick_single(), subject.pick_plural(), subject_action_trans.pick_single(), object.pick_plural())
    elif i == 21:
        s = "Ever wonder why {} {}? These {} facts will blow your mind!".format(
            subject.pick_plural(), subject_action_intrans.pick_single(), number.pick())
    elif i == 22:
        x1 = researcher.pick()
        s = "No one believed {} until {} discovered the truth about {}. Now other {} hate {}!".format(
            x1[0], get_pronoun(x1[1]), object.pick_plural(), researcher_type.pick_plural(), get_pronoun_acc(x1[1]))
    elif i == 23:
        s = "You thought all {} have the same {}, right? Here are {} reasons why you're wrong.".format(
            subject.pick_plural(), object.pick_plural(), number.pick())
    elif i == 24:
        s = "These {} needed to get their message across. How they did it amazed me. (Hint: it may have involved {}.)".format(
            subject.pick_plural(), object.pick_plural())
    elif i == 25:
        x1 = number.pick()
        x2 = number.pick()
        n1 = min([x1, x2])
        n2 = max([x1, x2])
        s = "Think you know how {} work? Listen to this {}. On page {} he'll make you think. On page {} he'll blow your mind.".format(
            object.pick_plural(), researcher_type.pick_single(), n1, n2)
    elif i == 26:
        s = "You won't believe what's causing the spread of {} {}! The shocking truth that {} don't want you to hear.".format(
            adjective.pick(), object.pick_plural(), researcher_type.pick_plural())
    elif i == 27:
        s = "Think {} like to {}? Think again.".format(
            subject.pick_plural(), subject_action_intrans.pick_single())
    elif i == 28:
        s = "These {} were forced to {} {} because of {}. {}".format(
            subject.pick_plural(), subject_action_trans.pick_single(), object.pick_plural(), object.pick_plural(), secondary.pick())
    elif i == 29:
        s = "{} {} warned us to look for {} {}. {}".format(
            object.pick_single(), researcher_type.pick_plural(), adjective.pick(), object.pick_plural(), secondary.pick())
    elif i == 30:
        s = "{} {} guaranteed to make {} {}.".format(
            number.pick(), object.pick_plural(), subject.pick_plural(), subject_action_intrans.pick_single())
    elif i == 31:
        s = "The {} new {} that every {} is talking about.".format(
            adjective.pick(), object.pick_single(), researcher_type.pick_single())
    elif i == 32:
        s = "{} warned us about {}, but look what's happening now.".format(
            researcher.pick()[0], object.pick_plural())
    elif i == 33:
        s = "Read this {} to discover the true meaning of {}.".format(
            research_type.pick_single(), object.pick_plural())
    elif i == 34:
        s = "Why all {} {}. {}".format(
            subject.pick_plural(), subject_action_intrans.pick_single(), secondary.pick())
    elif i == 35:
        s = "The real {} secrets of {}.".format(
            adjective.pick(), subject.pick_plural())
    elif i == 36:
        s = "These facts about {} will change the way you look at {} forever.".format(
            object.pick_plural(), subject.pick_plural())
    elif i == 37:
        s = "{} ways that {} {}.".format(
            number.pick(), subject.pick_plural(), subject_action_intrans.pick_single())

    lst = [word[0].upper() + word[1:] for word in s.split()]
    s = " ".join(lst)
    return s

print create_bait()