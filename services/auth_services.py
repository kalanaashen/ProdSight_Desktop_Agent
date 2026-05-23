import requests

BASE_URL= "http://localhost:5000/api"



def login(email,password):
    
    try:
        response=requests.post(f"{BASE_URL}/auth",json={
            "email":email,
            "password":password,
        })
        if response.status_code==200:
            token=response.text
            print("Login Successful")
            return token
        else:
            print(response.text)
            return None
        
    except Exception as e:
        print(f"error occrued while logging {e}")
        return None
    
  



    