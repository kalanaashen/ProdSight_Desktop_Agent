from  trackers.activity_tracker import (get_active_window)
from services.auth_services import (login)



EMAIL="kalana@gmail.com"
PASSWORD="12345678"

try:
    
    token=login(EMAIL,PASSWORD)
    
    if token:
        get_active_window(token)
        
except Exception as e:
    print (f"Error Happen in apis {e}")



