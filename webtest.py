from robot.api import logger
import pandas as pd
import requests

def log_dataframe_as_error(dataframe: pd.DataFrame) -> None:
    with pd.option_context("display.max_columns", 10, "display.max_rows", 10, "display.max_colwidth", 100,
                               "display.precision", 10, "display.width", 100, 'display.expand_frame_repr', False):
        html_string = dataframe.to_html(index=False, justify="center", float_format='{:.16G}'.format,
                                    table_id="dataframe_errors")
        logger.info(html_string, html=True)
def restapi_endpoints(url):
    r= requests.get(url).json()
    animal_d = pd.DataFrame(r)
    print(animal_d.columns)
    # data_user=pd.DataFrame(user_d)
    log_dataframe_as_error(animal_d[['user', 'text', 'source']])

web_url='https://cat-fact.herokuapp.com/facts?animal_type=cat,horse'
restapi_endpoints(web_url)
