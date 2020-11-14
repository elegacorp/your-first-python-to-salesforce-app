# A general connection object variable can be initialized, 
# which will then be populated with the Salesforce connection
# object as it is returned from simple_salesforce.
production_connection = None

# The content of the string variables below should be replaced
# with your own connection credentials. The API version, 50.0, 
# happens to be the latest Salesforce API version from this writing,
# but there might be changes that happen later from future Salesforce API
# versions. 
#
# The domain, specifies the login domain known from:
# https://login.salesforce.com
#
# Using 'test' for the login domain would point to:
# https://test.salesforce.com
# That domain is used for sandbox environments. A free
# developer org in this example, though, is considered a 
# 'production' Salesforce org and therefore would go to 
# the 'login' domain, not 'test' or something else.
if production_connection is None:
	production_connection = Salesforce(username="<username>",
		password="<password>",
		security_token="<security_token>",
		version=50.0, # the API version of Salesforce, for its metadata
		domain='login') # login means: a production org