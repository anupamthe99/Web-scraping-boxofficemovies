import requests
from requests_html import HTML
import pandas as pd
from sqlalchemy import false 


# bs4 :: requests-html 

#requests : > way of interacting with websites using python 
"""
REST API:
PUT
DELETE

# most familar 
GET : geting request from web : data 
POST :data send 
"""

"""
Status_code :
404 : website not found : url link invalid \
200 : success 
500 : server error : crash 
"""
"""
Scrape HTML page :
<HTML/>

class : .imdb-scroll-table

CSS ,JS : . notation for classes and # for id 

<table>
<tr>
 : th tag is for header 
    <th>
    </th>
</tr>
<tr>
 : td tag for the col
    <td>
    </td>
</tr>
<tr>
 : td tag for the col
    <td>
    </td>
</tr>
0 : header
1:10 : top 10 data
200
</table>

"""



# print(r.status_code)
# print(r.text)

def text_to_HTML_page(r):
    if r.status_code == 200:
        html_text=r.text
        # print(html_text)
        with open("world.html",'w', encoding="utf-8") as f:
            f.write(html_text)
        return html_text
    return ""


r= requests.get('https://www.boxofficemojo.com/year/world/')
html_text=text_to_HTML_page(r)
r_html=HTML(html=html_text)
table_class_value=r_html.find(".imdb-scroll-table")
# print(r_html.find(".imdb-scroll-table"))


if len(table_class_value)==1:
    # print(table_class_value[0].text)
    parsed_table=table_class_value[0]
    tr=parsed_table.find("tr")
    header_row=tr[0]
    header_col=header_row.find("th")
    header_name=[h.text for h in header_col]
    print(header_name)
    # print(tr)
    table_data=[]
    for row in tr[1:11]:
        # print(row.text+"\n\n")

        td=row.find("td")
        row_table=[]
        for i,col in enumerate(td):
            # print(i,col.text,"\n\n")
            row_table.append(col.text)
        table_data.append(row_table)

    print(table_data)

df=pd.DataFrame(table_data,columns=header_name)
df.to_csv('movies.csv',index=False)



