import HTML
import webbrowser


t = HTML.Table(header_row=['x', 'square(x)', 'cube(x)'])
for x in range(1,10):
    t.rows.append([x, x*x, x*x*x])
htmlcode = str(t)
print htmlcode
try:
    with open('hello.html', 'w') as f:
        f.write(htmlcode)
        f.write('<p>')
except IOError:
    print "Could not write into the file:", f
try:
    with open('hello.html', 'r') as f:
        f.read()
        webbrowser.open_new_tab('hello.html')
except IOError:
    print "Could not read the file:", f

print '-'*79
    
