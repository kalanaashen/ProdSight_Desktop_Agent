import requests



BASE_URL="http://localhost:5000/api"





def send_app_usage(data,token):
    
    try:
        
        response=requests.post(f"{BASE_URL}/appusage",json=data,headers={"X-auth-token":token})
        
        print(response.status_code)
        print(response.json())
        
        
        
    except Exception as e:
        print(f"error occrerd while sending data {e}")