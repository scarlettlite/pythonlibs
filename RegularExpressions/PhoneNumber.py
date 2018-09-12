import re
r"""
using r defines this string as a raw string it means
that python compiler will not escape characters
In python regular expressions, '\d' is used to mark a
decimal character
"""
def phonenum():
    phonenum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print(phonenum.search('My number is 415-555-4242.').group())

def phonenumwithgroups():
    pn2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = pn2.search('My number is 415-555-4242.')
    print(mo.group(1))
    print(mo.group(2))
    print(mo.groups())

def phonenumbrackets():
    #
    pnbrackets = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
    mobrackets = pnbrackets.search('My number is (415)-555-4242.')
    print(mobrackets.group(1))
    print(mobrackets.group(2))

def usingpipe():
    heroregex = re.compile(r'Batman|Bruce Wayne')
    mo = heroregex.search('Batman and Bruce Wayne')
    print(mo.group())
    mo1 = heroregex.search('Bruce Wayne and Batman')
    print(mo1.group())

def matchwordswithsameprefix():
    """
    @rathor: How to output all three: 'batmobile, batman, batwoman'
    """
    prefixregex = re.compile(r'Bat(mobile|man|woman)')
    mo = prefixregex.search('Batman and Batwoman are going on a mission to Paris. They will need thei Batmobile')
    print(mo.group())

def optionalmatching():
    optional = re.compile(r'Bat(wo)?man')
    mo1 = optional.search('The adventures of Batman')
    mo2 = optional.search('The Adventures of Batwoman')
    print(mo1.group())
    print(mo2.group())


def matchzeroormore():
    zeroormore = re.compile(r'bat(wo)*man')
    mo1 = zeroormore.search('the adventures of batman')
    mo2 = zeroormore.search('the adventures of batwoman')
    mo3 = zeroormore.search('the adventures of batwowowoman')
    print('mo1', mo1.group())
    print('mo2', mo2.group())
    print('mo3', mo3.group())
    
def matchoneoremore():
    oneormore = re.compile(r'bat(wo)+man')
    mo1 = oneormore.search('the adventures of batman')
    mo2 = oneormore.search('the adventures of batwoman')
    mo3 = oneormore.search('the adventures of batwowoman')
    print('mo1', mo1) # mo1 will be None
    print('mo2' , mo2.group())
    print('mo3', mo3.group())


def matchspecificrepititions():
    #match 3 to 5 consecutive instances of Ha
    rep35 = re.compile(r'(Ha){3,5}')

    #match exactly 3 consecutive instances of Ha
    rep3 = re.compile(r'(Ha){3}')

    #match 3 or more consecutive instances of Ha
    rep3ormore = re.compile(r'(Ha){3,}')

    #match 0 to 5 consecutive instances of Ha
    rep5orless = re.compile(r'(ha){,5}')


def greedy():
    


