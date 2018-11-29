import mechanize
br = mechanize.Browser()
br.open("https://paytm.com/")
assert br.viewing_html()
#br.select_form(nr=0)
#br.form['name'] = 'Enter your Name'
#br.form['title'] = 'Enter your Title'
#br.form['message'] = 'Enter your message'
#req = br.submit()

a,b=[1,3]
print (a)
print (b)

'hello world'.replace('l','b',2)

x=[1,2,3]
y=x
x[0]=0
print (y)

def f(a,b): pass

type(f(1,10))
