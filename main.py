def process_weather_request() :
    print('processing weather request')

def process_sports_request() :
    print('processing sports request')

def process_music_request() :
    print('processing music request')

def process_current_event_request() :
    print('processing current event request')
#
#  This is the main driver program for the "Alexa" Project
#
categories = ['WEATHER','SPORTS','MUSIC','CURRENT EVENTS','EXIT']
user_category = ''
print("Welcome to Alexa")
while user_category != 'EXIT' :
    print('Please select one of the following categories for your question')
    print('\n''WEATHER\nSPORTS\nMUSIC\nCURRENT EVENTS\nEXIT\n')
    user_category = input('What is your choice : ').upper()
    #print(user_category)

    if user_category in categories :
        if user_category == 'WEATHER' :
            process_weather_request()
        elif user_category == 'SPORTS' :
            process_sports_request()
        elif user_category == 'MUSIC' :
            process_music_request()
        elif user_category == 'CURRENT EVENTS' :
            process_current_event_request()
        else :
            exit(0)
    else :
        print('Sorry, your response does not match any of the categories')
