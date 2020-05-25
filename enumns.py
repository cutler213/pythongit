import enum


class Animals(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

#for Ani in (Animals):
 #   print(Ani.name +'-'+ str(Ani.value))


print('\n'.join(' ' + c.name for c in Animals))



