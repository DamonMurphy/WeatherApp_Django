# views.py file

from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    
    if request.method == 'POST':
        
        zipcode = request.POST['zipcode']
        
        api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode + '&distance=25&API_KEY=A8A82782-D457-44E0-AF04-5F9D6BA56228')
        
        # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=43119&distance=25&API_KEY=A8A82782-D457-44E0-AF04-5F9D6BA56228
        
        try:
            api = json.loads(api_request.content)
            
        except Exception as e:
            api = 'Error...'
        
        if api[0]['Category']['Number'] == 1:
            category_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk.'
            category_color = 'AQ1'
        elif api[0]['Category']['Number'] == 2:
            category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
            category_color = 'AQ2'
        elif api[0]['Category']['Number'] == 3:
            category_description = '(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
            category_color = 'AQ3'
        elif api[0]['Category']['Number'] == 4:
            category_description = '(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
            category_color = 'AQ4'
        elif api[0]['Category']['Number'] == 5:
            category_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
            category_color = 'AQ5'
        elif api[0]['Category']['Number'] == 6:
            category_description = '(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected.'
            category_color = 'AQ6'
        else:
            category_description = 'Run for your life!!!!'
            category_color = 'AQ7'
        
        return render(request,'home.html',{'api':api,
                      'category_description':category_description,
                      'category_color':category_color})
        

    
    else:
        
        api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=43119&distance=25&API_KEY=A8A82782-D457-44E0-AF04-5F9D6BA56228')
        
        # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=43119&distance=25&API_KEY=A8A82782-D457-44E0-AF04-5F9D6BA56228
        
        try:
            api = json.loads(api_request.content)
            
        except Exception as e:
            api = 'Error...'
        
        if api[0]['Category']['Number'] == 1:
            category_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk.'
            category_color = 'AQ1'
        elif api[0]['Category']['Number'] == 2:
            category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
            category_color = 'AQ2'
        elif api[0]['Category']['Number'] == 3:
            category_description = '(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
            category_color = 'AQ3'
        elif api[0]['Category']['Number'] == 4:
            category_description = '(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
            category_color = 'AQ4'
        elif api[0]['Category']['Number'] == 5:
            category_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
            category_color = 'AQ5'
        elif api[0]['Category']['Number'] == 6:
            category_description = '(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected.'
            category_color = 'AQ6'
        else:
            category_description = 'Run for your life!!!!'
            category_color = 'AQ7'
        
        return render(request,'home.html',{'api':api,
                      'category_description':category_description,
                      'category_color':category_color})

def about(request):
    return render(request,'about.html',{})
