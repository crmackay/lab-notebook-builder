def HTMLEditor(html):
    
    import re
    
    html = html.replace('<table>','<div class="table-responsive"><table class="table table-condensed table-striped">')
    
    html = html.replace('</table>','</table></div>')
    
    html = html.replace('[ ]', '<input type="checkbox" >')
    
    html = html.replace('[x]', '<input type="checkbox"  checked>')
    
    img_re = re.compile(r'''
        (<img           #search for img opening tag
        \s*             #any amount of white-space characters
        alt="           #an alt tag up to the beginning of the value
        (?P<alt>[a-zA-Z0-9_ ]*)    #alt value as a group labelled 'alt'
        "\s*            #close parenthesis and whitespace
        src="           #beginning of the src attribute up to the value
        (?P<src>.*?)    #src value as a group labelled 'src'
        "\s*            #close parenthesis and whitespace
        />)             #self-closing of the img tag                
        ''', re.VERBOSE)
    
    result = img_re.search(html)
    if 'img' in html:
        print('new file', html)
        
        alt, src = result.group('alt','src')
        
        replacement = '<a href="'+src+'">''<object class="svg-object" type="image/svg+xml" data="'+src+'"><a href="'+src+'">'+alt+'</a></object></a>'
    
        html = re.sub(img_re, replacement, html)
        
        print html
                
    return(html)