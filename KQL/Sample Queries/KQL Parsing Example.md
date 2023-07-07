# Sample KQL Queries

I have created and collected these queries from various sources. They serve as reminder to me how to effectively use KQL to get the data you need in Sentinel.

## Simple Entity Parsing in SecurityAlert table.

`SecurityAlert
| where ProviderName == "Azure Advanced Threat Protection"
| summarize arg_max(TimeGenerated, *) by VendorOriginalId
| mv-expand todynamic(Entities)
| extend x = parse_json(Entities)
| extend Host = x.HostName
| extend Account = x.Name
| extend IP = x.Address
| extend File = x.File
| extend Group = x.Group
| extend ResourceId = x.ResourceName
| extend Time= x.Time
| summarize
    HostNames=make_set(Host),
    AccountNames=make_set(Account),
    IPAddresses=make_set(IP),
    Files=make_set(File),
    SecurityGroups=make_set(Group),
    Resources=make_set(ResourceId),
    TimeAccessed=make_set(Time)
    by TimeGenerated, SystemAlertId, AlertName, Description`


## More precise entity parsing in SecurityAlert table


`SecurityAlert
    | extend AlertId = SystemAlertId
    | extend EntitiesDynamicArray=parse_json(Entities) | mvexpand EntitiesDynamicArray
    | extend Entitytype = tostring(parse_json(EntitiesDynamicArray).Type)
    | where Entitytype == "account"
    | extend username=tostring(parse_json(EntitiesDynamicArray).Name)
    | extend UPNSuffix=tostring(parse_json(EntitiesDynamicArray).UPNSuffix)
    | extend useraccount = strcat(username, UPNSuffix)
    | extend UserPrincipalName = tostring(parse_json(EntitiesDynamicArray).UserPrincipalName)
    | extend EntitiesDynamicArray=parse_json(Entities) | mvexpand EntitiesDynamicArray
    | extend Entitytype = tostring(parse_json(EntitiesDynamicArray).Type)
    | where Entitytype == "host"
    | extend HostName=tostring(parse_json(EntitiesDynamicArray).HostName)
    | extend DeviceDnsName=tostring(parse_json(EntitiesDynamicArray).DeviceDnsName)
    | extend RiskScore=tostring(parse_json(EntitiesDynamicArray).RiskScore)
    | extend OSFamily=tostring(parse_json(EntitiesDynamicArray).OSFamily)
    | extend OnBoardingStatus=tostring(parse_json(EntitiesDynamicArray).OnBoardingStatus)`