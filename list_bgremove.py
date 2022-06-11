import requests
import pandas as pd

#We are loading the excel file and converting into dataframe
df = pd.read_excel('/home/nerd/Downloads/St. DASSI.xlsx',names= ['Photo'])
data = pd.DataFrame(df)

#Now, iterating through the urls of image in excel file

for photo,count in enumerate(data['Photo']):
    response = requests.post(
         'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': f'{photo}',
        'size': 'auto'},
    headers={'X-Api-Key': 'Enter_your_bgremover_api'},)
    if response.status_code == requests.codes.ok:
       with open(f'/home/nerd/campt130/Image/bg{count}'+'.png', 'wb') as out:    #Enter you directory for                                                                          
        out.write(response.content)                                              # BG removed Saving Images 
    else:
        print("Error:", response.status_code, response.text)