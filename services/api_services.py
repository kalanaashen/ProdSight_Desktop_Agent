import requests



BASE_URL="http://localhost:5000/api"





def send_app_usage(data,token):
    
    try:
        
        response=requests.post(f"{BASE_URL}/appusage",json=data,headers={"X-auth-token":token})
        
        print(response.status_code)
        print(response.json())
        
        
        
    except Exception as e:
        print(f"error occrerd while sending data {e}")
        
def send_active_data(data,token):
    
    try:
        response=requests.post(f"{BASE_URL}/activity",json=data,headers={"X-auth-token":token})
        
        print(response.status_code)
        print(response.text)
        
    except Exception as e:
        
        print (f"Error Occured while sending activity data {e}")
        
        