from Questgen import main
import ssl
from pydantic import BaseModel
class question(BaseModel):
    text: str
    type: str


class aiml:

    def __init__(self) -> None:

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context
            pass

    def question_gen(self,text,type):
       
        payload = {
                    "input_text": text
                }

        if type == "boolq":
            qe= main.BoolQGen()
            output = qe.predict_boolq(payload)
        elif type == "mcq":
            qe= main.QGen()
            output = qe.predict_mcq(payload)
        elif type == "shortq": 
            qe= main.QGen()
            output = qe.predict_shortq(payload)
        elif type == "paraphrase": 
            qe= main.QGen()
            output = qe.paraphrase(payload)        
       
        return output