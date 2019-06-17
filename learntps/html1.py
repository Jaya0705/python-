import HTML
import webbrowser

table_data = [
        ['Smith',       'John',         30],
        ['Carpenter',   'Jack',         47],
        ['Johnson',     'Paul',         62],
    ]

htmlcode = HTML.table(table_data,
    header_row=['Last name',   'First name',   'Age'])
print htmlcode
try:
    with open('hi.html', 'w') as f:
        f.write(htmlcode)
        f.write('<p>')
except IOError:
    print "Could not write into the file:", f
try:
    with open('hi.html', 'r') as f:
        f.read()
        webbrowser.open_new_tab('hi.html')
except IOError:
    print "Could not read the file:", f

print '-'*79

