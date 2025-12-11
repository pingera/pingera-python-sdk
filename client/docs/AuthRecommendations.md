# AuthRecommendations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | **List[Dict[str, object]]** | List of authentication setup recommendations | [optional] [readonly] 

## Example

```python
from pingera.models.auth_recommendations import AuthRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRecommendations from a JSON string
auth_recommendations_instance = AuthRecommendations.from_json(json)
# print the JSON string representation of the object
print(AuthRecommendations.to_json())

# convert the object into a dict
auth_recommendations_dict = auth_recommendations_instance.to_dict()
# create an instance of AuthRecommendations from a dict
auth_recommendations_from_dict = AuthRecommendations.from_dict(auth_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


