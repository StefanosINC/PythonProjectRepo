from RequestHandler import RequestHandler
class services:


    def validateRegistration(username):
    #Declare booleans
        upper_letter = False
        lower_letter = False
        lower_letter = any(c.islower() for c in username)
        upper_letter = any(c.isupper() for c in username)
        
        if len(username) > 0 and username[-1].isdigit():
            if lower_letter and upper_letter:
                return RequestHandler.successfull_entry(username)
            else:
                return RequestHandler.HandleError(username)
            
