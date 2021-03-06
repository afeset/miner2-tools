from common import validkey, KeyPress, make_KeyPress_from_keydescr
import sys
import select
import re
import os

_sequence2KeyPressInitialized = False

# sequences can be discovered with command:
#   showkey -k -a
sequence2KeyPress = {
    000: KeyPress(char=' ', control=True, keyname='space'),
    011: KeyPress(char='\011', keyname="tab"),
    015: KeyPress(char='\015', keyname="return"),
    033: {
        None: KeyPress(char='\033', keyname="escape"),
        040: KeyPress(char=' ', meta=True, keyname='space'),
        0117: {
            061: {
                073: {
                    062: {
                        0120:  KeyPress(shift=True, keyname='f1'), # gnome-terminal
                        0121:  KeyPress(shift=True, keyname='f2'), # gnome-terminal
                        0122:  KeyPress(shift=True, keyname='f3'), # gnome-terminal
                        0123:  KeyPress(shift=True, keyname='f4'), # gnome-terminal
                    },
                },
            },
            062: {
                0120:  KeyPress(shift=True, keyname='f1'), # Konsole
                0121:  KeyPress(shift=True, keyname='f2'), # Konsole
                0122:  KeyPress(shift=True, keyname='f3'), # Konsole
                0123:  KeyPress(shift=True, keyname='f4'), # Konsole
            },
            0106:  KeyPress(keyname='end'),  # gnome-terminal
            0110:  KeyPress(keyname='home'), # gnome-terminal
            0120:  KeyPress(keyname='f1'),
            0121:  KeyPress(keyname='f2'),
            0122:  KeyPress(keyname='f3'),
            0123:  KeyPress(keyname='f4'),
        },
        0133: {
            061: {
                061: {
                    0176:  KeyPress(keyname='f1'), # putty
                },
                062: {
                    0176:  KeyPress(keyname='f2'), # putty
                },
                063: {
                    0176:  KeyPress(keyname='f3'), # putty
                    073:   {
                        062: {
                            0176:  KeyPress(shift=True, keyname='insert'), # xterm?
                        },
                    },
                },
                064: {
                    0176:  KeyPress(keyname='f4'), # putty
                },
                065: {
                    0176:  KeyPress(keyname='f5'),
                },
                067: {
                    0176:  KeyPress(keyname='f6'),
                },
                070: {
                    0176:  KeyPress(keyname='f7'),
                },
                071: {
                    0176:  KeyPress(keyname='f8'),
                },
                073: {
                    062: {
                        0106: KeyPress(shift=True, keyname='end'), # xterm?
                        0110: KeyPress(shift=True, keyname='home'), # xterm?
                        0120: KeyPress(shift=True, keyname='f1'), # xterm
                        0121: KeyPress(shift=True, keyname='f2'), # xterm
                        0122: KeyPress(shift=True, keyname='f3'), # xterm
                        0123: KeyPress(shift=True, keyname='f4'), # xterm
                        0176: KeyPress(shift=True, keyname='delete'), # xterm
                    },
                    063: {
                        0101: KeyPress(meta=True, keyname='up'),
                        0102: KeyPress(meta=True, keyname='down'),
                        0103: KeyPress(meta=True, keyname='right'),
                        0104: KeyPress(meta=True, keyname='left'),
                    },
                    065: {
                        0101: KeyPress(control=True, keyname='up'),
                        0102: KeyPress(control=True, keyname='down'),
                        0103: KeyPress(control=True, keyname='right'),
                        0104: KeyPress(control=True, keyname='left'),
                    },
                },
                0176:  KeyPress(keyname='home'), # putty
            },
            062: {
                060: {
                    0176:  KeyPress(keyname='f9'),
                },
                061: {
                    0176:  KeyPress(keyname='f10'),
                },
                063: {
                    0176:  KeyPress(keyname='f11'),
                },
                064: {
                    0176:  KeyPress(keyname='f12'),
                },
                0176:  KeyPress(keyname='insert'),
            },
            063: {
                073: {
                    063: {
                        0176: KeyPress(meta=True, keyname='delete'),
                    },
                },
                0176:  KeyPress(keyname='delete'),
            },
            064: {
                0176:  KeyPress(keyname='end'), # putty
            },
            065: {
                0176:  KeyPress(keyname='prior'), # page up
            },
            066: {
                0176:  KeyPress(keyname='next'),  # page down
            },
            0101:  KeyPress(keyname='up'),
            0102:  KeyPress(keyname='down'),
            0103:  KeyPress(keyname='right'),
            0104:  KeyPress(keyname='left'),
            0110:  KeyPress(keyname='home'),
            0105:  KeyPress(keyname='center'),
            0106:  KeyPress(keyname='end'),
            0132:  KeyPress(shift=True, keyname='tab'),
        },
        0177: KeyPress(char='', meta=True, keyname="backspace"),
    },
    040:  KeyPress(char=' ', keyname="space"),
    0177: KeyPress(char='', keyname="backspace"),
}

def initSequence2KeyPress():
    global _sequence2KeyPressInitialized
    if _sequence2KeyPressInitialized:
        return
    for i in range(ord('z')+1-ord('a')):
        if not sequence2KeyPress.get(i+1, None):
            sequence2KeyPress[i+1] = KeyPress(char=chr(ord('a')+i), control=True)
    escapeDict = sequence2KeyPress[033]
    # fill rest of escape,printablecharacter as alt-chr
    for i in range(ord(' '), ord('~')+1):
        if not escapeDict.get(i, None):
            escapeDict[i] = KeyPress(char=chr(i), meta=True)
    _sequence2KeyPressInitialized = True

def convertSequence(sequence, offset=0, dictionary=sequence2KeyPress):
    initSequence2KeyPress()
    if offset == len(sequence):
        current = dictionary.get(None, None)
        return (current, offset)
    current = dictionary.get(ord(sequence[offset]), None)
    if not current:
        if dictionary == sequence2KeyPress:
            # default characters
            k = KeyPress(char=sequence[offset])
            return (k, offset+1)
        # we are somewhere inside tree - stop here
        prev = dictionary.get(None, None)
        return (prev, offset)
    if isinstance(current, dict):
        res = convertSequence(sequence, offset=offset+1, dictionary=current)
        if res[0] == None:
            if dictionary == sequence2KeyPress:
                # failed to resolve full sequence so provide input char by char
                k = KeyPress(char=sequence[offset])
                return (k, offset+1)
            else:
                # failed to convert with current
                prev = dictionary.get(None, None)
                return (prev, offset)
        else:
            return res
    else:
        return (current, offset+1)

_MAX_READ_SIZE = 1000

def readSequence(timeout):
    i,o,e = select.select([sys.stdin], [], [], timeout)
    if sys.stdin in i:
        input = os.read(sys.stdin.fileno(), _MAX_READ_SIZE)
        return input
    else:
        return None

_cursorPositionResponseRegexp = re.compile("\033\\[(\d+);(\d+)R")

class KeyPressReader:
    def __init__(self):
        self.offset = 0
        self.sequence = ""

    def _resetSequence(self):
        self.sequence = ""
        self.offset = 0

    def _updateSequence(self, timeout):
        while True:
            s = readSequence(timeout)
            if not s:
                return
            self.sequence += s
            if len(s) < _MAX_READ_SIZE:
                break
            timeout = 0.01
    
    def getKey(self, timeout=365*24*3600):
        if not self.sequence:
            self._updateSequence(timeout)
            if not self.sequence:
                return None
        res = convertSequence(self.sequence, offset=self.offset)
        self.offset = res[1]

        if self.offset == len(self.sequence):
            self._resetSequence()
        
        return res[0]
        
    def getCursorPosition(self, timeout):
        # Try to do it immediately
        self._updateSequence(timeout)
        res = self.extractCursorPosition()
        return res

    def extractCursorPosition(self):
        if self.offset > 0:
            self.sequence = self.sequence[self.offset:]
            self.offset = 0
        
        match = _cursorPositionResponseRegexp.search(self.sequence)
        if not match:
            return None
        line = int(match.group(1))
        col = int(match.group(2))
        
        #if match.start() > 0:
        #    print "Pending:", self.sequence
        # remove match from sequence
        self.sequence = self.sequence[:match.start()] + self.sequence[match.end():]
        return (line, col)
            

        
        
def testNonCanon():
    import termios, sys, tty
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        new = termios.tcgetattr(fd)
        new[2] = new[2] & ~termios.ICANON       # cflags
        new[3] = new[3] & ~termios.ECHO         # lflags
        new[6][termios.VTIME] = 0
        new[6][termios.VMIN] = 0
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        reader = KeyPressReader()
        for repeat in range(20):
            k = reader.getKey(10)
            print "Selected\r"
            if k:
                print "keypress = '%s'\r" % str(k)
            #
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def remains():
            i,o,e = select.select([sys.stdin],[],[],10)
            print 'Selected\r'
            for s in i:
                if s == sys.stdin:
                    input = os.read(fd, 100)
                    s = ""
                    for ch in input:
                        s = s+("\\%03d" % int(oct(ord(ch))))
                    print '%d bytes \"%s\"\r' % (len(input) ,s)
                    #for ch in input:
                    #    print '  ch = %d %03d\r' % (ord(ch), int(oct(ord(ch))))
                    offset = 0
                    while offset < len(input):
                        k,offset = convertSequence(input, offset=offset)
                        print "keypress = '%s'\r" % str(k)

if __name__ == u"__main__":
    testNonCanon()


        

