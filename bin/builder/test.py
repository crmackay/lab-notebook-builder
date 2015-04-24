import markdown

md = u'1. this is item 1\n\n1. this is item2 2\n1. this is item 3'

html = markdown.markdown(md)

print html