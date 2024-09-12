import sys
import logging

def error_message_detail(error,error_details:sys):
    _,_,exc_tb= error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in file [{0}] at line [{1}] error message is [{2}]".format(
        filename,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

##testing the code
# if __name__ == "__main__": ##This code runs only when the script(file) is executed directly and used for testing purpose.
#     ## when this file is imported as a module in another file/module, the __name__ is set to filename
#     try:
#         a=1/0
#     except CustomException as e:
#         print(e)
#         logging.info('Divided by zero')
#         raise CustomException(e,sys)