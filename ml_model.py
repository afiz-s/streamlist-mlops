from abacusai import ApiClient
import pprint
pp = pprint.PrettyPrinter(indent=2)

deployment_token = '5a54a7a366b44302b7eea6b39ab15b1a'
deployment_id = '92383280'
def get_movie_recommendations(user_id='1', movie_id='466'):
    results = ApiClient().get_related_items(deployment_token=deployment_token,
                deployment_id=deployment_id,
                query_data={"user_id":"1","movie_id":"466"})
    
    return results