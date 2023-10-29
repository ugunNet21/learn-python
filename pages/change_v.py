x = [13]
hex(id(x))

# D:\Web\learn-python>python
# Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x = [13]
# >>> hex(id(x))
# '0x26897d16200'
# >>> #mengubah nilai x
# >>> x[0] = 99
# >>> hex(id(x))
# '0x26897d16200'
# >>> x = 13
# >>> hex(id(x))
# '0x7ffc2473e4a8'
# >>> nama = input ('Masukan Nama Anda :')
# Masukan Nama Anda :gugun
# >>> nama
# 'gugun'
# >>> x = input ('Masukan Bilangan :')
# Masukan Bilangan :4
# >>> x
# '4'
# >>> type (x)
# <class 'str'>
# >>> x+2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# >>> x = int(input('Masukan bilangan bulat :'))
# Masukan bilangan bulat :9
# >>> type (x)
# <class 'int'>
# >>> x+3
# 12
# >>>