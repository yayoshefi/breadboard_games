class Ivrit():

    ALEF = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),\
            (1,2),(2,3),(3,4),(4,5),(5,6),\
            (5,1),(5,2),(5,3),(5,4),\
            (2,3),(2,4),(2,5),(2,6)]
    BET = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1), \
           (6,2),(6,3),(6,4),(6,5),(6,6),\
           (1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
    GIMEL = [(4,1),(5,1), (5,2),(5,3),(5,4),(5,5),(5,6), \
             (4,4), (3,4),(3,5),(3,6)]
    DALET = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1), \
              (6,2),(6,3),(6,4),(6,5),(6,6)]
    HEH = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1), \
           (6,2),(6,3),(6,4),(6,5),(6,6),  (1,4),(1,5),(1,6)]
    VAV = [(3,1),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6)]
    ZAIN = [(4,1),(4,2),(4,3),(4,4),(4,5),(4,6), (5,2),(3,1) ]
    HET = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1), \
           (6,2),(6,3),(6,4),(6,5),(6,6),\
           (1,2),(1,3),(1,4),(1,5),(1,6)]
    TET = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6), (2,6),(3,6),(4,6),(5,6),\
           (6,1),(6,2),(6,3),(6,4),(6,5),(6,6), (5,1),(4,1),(4,2)]
    YOD = [(4,1),(5,1), (5,2),(5,3)]
    KAF = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1), \
           (6,2),(6,3),(6,4),(6,5),(6,6),\
           (1,6),(2,6),(3,6),(4,6),(5,6),(6,6)]
    LAMED = [(1,0),(1,1),  (2,2),(3,2),(4,2),(5,2),(6,2), (6,3),(6,4),(6,5),\
             (5,5),(4,5),(3,5), (4,6),(3,6),(2,6)]
    MEM = [(4,6),(5,6),(6,6), (6,5),(6,4),(6,3), \
           (5,2),(5,1),(4,1),(3,2),(2,1),\
           (2,3),(2,4),(2,5),(2,6)]
    NOON = [(2,6),(3,6),(4,6),(5,6),(6,6), (6,5),(6,4),(6,3),(6,2),(6,1), (5,1)]
    SAMECH = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1), \
              (1,2),(1,3),(1,4), (2,5),(3,6),\
              (6,2),(6,3),(6,4), (5,5),(4,6)] 
    AIN = [(2,6),(3,6),(4,6),(5,6),(6,6), (6,5),(6,4),(6,3),(6,2),(6,1),\
                                          (3,5),(3,4),(3,3),(3,2),(3,1)]
    PE = [(2,1),(3,1),(4,1),(5,1),(6,1),  (2,6),(3,6),(4,6),(5,6),(6,6), \
           (2,2),(2,3),(3,3),  (6,2),(6,3),(6,4),(6,5)]         
    TZADIK = [(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),\
              (4,5),(5,5), (4,4),(5,4),\
              (3,3),(4,3),(5,3),\
              (2,2),(3,2), (5,2),(6,2),\
              (1,1),(2,1), (6,1) ]
    KOOF = [(2,1),(3,1),(4,1),(5,1),(6,1),\
            (6,2),(6,3),(6,4),(5,4),\
            (2,3),(2,4),(2,5),(2,6),(2,7)]
    RESH = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),\
            (6,2),(6,3),(6,4),(6,5),(6,6),]
    SHIN = [(2,6),(3,6),(4,6),(5,6),(6,6), (6,5),(6,4),(6,3),(6,2),(6,1),\
            (1,5),(1,4),(1,3),(1,2),(1,1), (3,5),(3,4),(3,3),(3,2),(3,1)]
    TAV = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1), \
           (1,2),(1,3),(1,4),(1,5),(1,6),\
           (6,2),(6,3),(6,4),(6,5),(6,6), (0,6) ]
    SPACE = []
    KAF_ = []
    MEM_ = []
    NOON_ = []
    PE_ = {}
    TZADIK_ = []

    _map_ord ={
        32  : SPACE,
        43  : SPACE,  # '+' in get context....
        1488: ALEF,
        1489: BET,
        1490: GIMEL,
        1491: DALET,
        1492: HEH,
        1493: VAV,
        1494: ZAIN,
        1495: HET,
        1496: TET,
        1497: YOD,
        1498: KAF_,
        1499: KAF,
        1500: LAMED,
        1501: MEM_,
        1502: MEM,
        1503: NOON_,
        1504: NOON,
        1505: SAMECH,
        1506: AIN,
        1507: PE_,
        1508: PE,
        1509: TZADIK_,
        1510: TZADIK,
        1511: KOOF,
        1512: RESH,
        1513: SHIN,
        1514: TAV,
        }
    
# hebrew abbritration
    א = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6), (1,2),(2,3),(3,4),(4,5),(5,6),\
            (6,1),(6,2),(6,3),(6,4),  (2,3),(2,4),(2,5),(2,6)]
    ת = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1), \
           (1,2),(1,3),(1,4),(1,5),(1,6),\
           (6,2),(6,3),(6,4),(6,5),(6,6), (0,6) ]

    def _init_(self):
        pass


    def _parse_hed_word(self, word):
        """
        Insert a hebrew string and outpus a list of charectest 
        with their offsets to the luma led
        """
        translate=[]
        for c in word:
            o = ord(c)
            if ord(c) in self._map_ord :
                translate.append(self._map_ord[ord(c)])
        translated_offset = self.add_char_offsets(*translate)
        return translated_offset


    def add_char_offsets(self, *argv):
        """
        input is a list of charecters
        outputs all charecters with offsets 
        first char has maximal offset of (l-1)*8
        """
        word=[] 
        l = len(argv)
        for i in range(l):
            char = argv[i]
            off = (l-1-i)*8
            word.append ([(p[0]+off,p[1]) for p in char])
        return word

    @staticmethod
    def show_word(device, word_array, delay=0.08):
        """
        passed to the luma led a list of heb charectes with offsests
        """
        from luma.core.virtual import viewport
        from luma.core.render import canvas
        import time
        virtual = viewport(device,width = 8*len(word_array), height=8)
        with canvas(virtual) as draw:
            for char in word_array:
                draw.point(char,fill='white')
        for i in reversed(range(len(word_array)*8-device.width)):
            virtual.set_position((i,0))
            time.sleep(delay)
        

    def config (self):
      from luma.core.interface.serial import spi, noop
      from luma.led_matrix.device import max7219

      serial = spi(port=0, device=0, gpio=noop())
      device = max7219(serial,rotate=2)
      return device

    def debug_1 (self, char):
      from luma.core.render import canvas
      device = self.config()
      with canvas(device) as draw:
          draw.point(char,fill='white')

    def debug_2 (self, *argv):
      from luma.core.render import canvas
      import time
      device = self.config()
      for arg in argv:
          with canvas(device) as draw:
              draw.point(arg,fill='white')
          time.sleep(1)

    def debug_3(self,*argv):
        """
        debug_3(Ivrit.MEM, Ivrit.ALEF, Ivrit.YOD, Ivrit.HEH)
        """
        from luma.core.virtual import viewport
        from luma.core.render import canvas
        import time
        device = self.config()
        word = self.add_char_offsets(*argv)

        show_word(device, word, delay=0.08)
        #virtual = viewport(device,width = 8*len(argv), height=8)
        #with canvas(virtual) as draw:
        #    for char in word:
        #        draw.point(char,fill='white')
        #for i in reversed(range((len(word)-1)*8)):
        #    virtual.set_position((i,0))
        #    time.sleep(0.08)




