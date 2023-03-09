# azureipblocking

The program for blocking IP through updating on Azure AD's Named Location (i.e. work together with Conditional Access)

Pre-process
1. Create the new Application through App Registration on Azure AD
2. Grant the proper permission for the application
   Reference URL: https://learn.microsoft.com/en-us/graph/api/resources/ipnamedlocation?view=graph-rest-1.0
3. Create the new Named Location on Azure AD with pre-set IP address
4. Get the Name Location ID and preset the JSON Dataset (i.e. please refer to file dataset.json)

Procedure
1. You need have your IP information sourceip.txt (i.e. Can be multiple line, it will process one by one)
2. Run process_json.py for JSON pre-processing
3. Run update_ipblock_range_info.py to update Azure AD's Named Location

So you may use the Conditional Access with the Named Location together to perform auto IP blocking
