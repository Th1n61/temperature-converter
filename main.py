a = input('''For converting Celsius to Fahrenheit, type c to f.
For converting Fahrenheit to Celsius, type f to c.
''')

def c_to_f():
    celsius = int(input('''what tempature do you want to convert?
'''))

    def conv(c):
        return 9/5 * c + 32

    fahrenheit = conv(celsius)
    print(' ')
    print(fahrenheit)

def f_to_c():
    Fahrenheit = int(input('''what tempature do you want to convert?
'''))

    def Conv(f):
        return (f - 32) / 1.8

    Celsius = Conv(Fahrenheit)
    print(' ')
    print(Celsius)

if a == 'c to f':
    c_to_f()
else:
    f_to_c()