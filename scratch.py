#read

def read_file():
    pass

#process

def process_file():
    pass


#write

def write_file():
    pass

def f(qty, item, price):
    print(f'{qty} {item} cost £{price:.2f}')

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting,name)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# Main Process
f(6,'bananas',1.74)
print(hello_func('hi', name = 'Dave'))

student_info('Math','Art')