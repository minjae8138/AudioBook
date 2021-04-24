from django.apps import AppConfig
from .deep_model.loadBert import *
class BookappConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name =  'bookApp'

class BertConfig(AppConfig):
    tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')
    loaded_model = create_sentiment_bert()
    # loaded_model.load_weights('./deep_model/sentiment_bert_split_ep20.h5')
    loaded_model.load_weights('./bookApp/deep_model/sentiment_bert_split_ep20.h5')





