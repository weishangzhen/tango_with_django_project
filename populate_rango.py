import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 61},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views': 62},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views': 63} ]
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 64},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 65},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 66} ]
    
    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 67},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views': 68} ]

    website_pages = [
        {'title': 'TREE HOUSE',
         'url': 'https://teamtreehouse.com/',
         'views': 76},
        {'title': 'KHAN ACADEMY',
         'url': 'https://www.khanacademy.org/',
         'views': 81},
        {'title': 'CODE SCHOOL',
         'url': 'https://www.pluralsight.com/codeschool',
         'views': 96},
        {'title': 'COURSERA',
         'url': 'https://www.coursera.org/',
         'views': 102},
        {'title': 'CODECADEMY',
         'url': 'https://www.codecademy.com/',
         'views': 117} ]
    
    recommend_java_pages = [
        {'title': 'Core Java Volume I--Fundamentals (Getting Started)',
         'url': 'https://www.amazon.co.uk/Core-Java-I-Fundamentals-Cay-Horstmann/dp/0135166306'},
        {'title': 'Thinking in Java (Getting Started)',
         'url': 'https://www.amazon.co.uk/Thinking-Java-Bruce-Eckel/dp/0131872486'},
        {'title': 'Java Concurrency in Practice (Advanced)',
         'url': 'https://www.amazon.co.uk/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601'},
        {'title': 'Clean Code: A Handbook of Agile Software Craftsmanship (Advanced)',
         'url': 'https://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882'} ]

    recommend_C_pages = [
        {'title': 'C Programming: A Modern Approach (Getting Started)',
         'url': 'https://www.amazon.co.uk/C-Programming-Modern-Approach-King/dp/0393979504'},
        {'title': 'The C Programming Language (Getting Started)',
         'url': 'https://www.amazon.co.uk/C-Programming-Language-2nd/dp/0131103628'},
        {'title': 'C Traps and Pitfalls (Advanced)',
         'url': 'https://www.amazon.com/C-Traps-Pitfalls-Andrew-Koenig/dp/0201179288'},
        {'title': 'Expert C Programming: Deep C Secrets (Advanced)',
         'url': 'https://www.amazon.co.uk/Expert-Programming-Peter-van-Linden/dp/0131774298'} ]

    recommend_python_pages = [
        {'title': 'A Byte of Python (Getting Started)',
         'url': 'https://www.amazon.co.uk/Byte-Python-Swaroop-C-H-ebook/dp/B00FJ7S2JU'},
        {'title': 'Think Python (Getting Started)',
         'url': 'https://www.amazon.co.uk/Think-Python-Allen-B-Downey/dp/144933072X'},
        {'title': 'Fluent Python: Clear, Concise, and Effective Programming (Advanced)',
         'url': 'https://www.amazon.co.uk/Fluent-Python-Luciano-Ramalho/dp/1491946008'},
        {'title': 'Effective Python: 90 Specific Ways to Write Better Python (Advanced)',
         'url': 'https://www.amazon.co.uk/Effective-Python-Specific-Software-Development/dp/0134853989'} ]

    
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
            'Online Learining Programming Websites': {'pages': website_pages, 'views': 76, 'likes': 32},
            'Recommended C language textbooks': {'pages': recommend_C_pages, 'views': 46, 'likes': 92},
            'Recommended JAVA language textbooks': {'pages': recommend_java_pages, 'views': 49, 'likes': 31},
            'Recommended Python language textbooks': {'pages': recommend_python_pages, 'views': 51, 'likes': 37} }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()