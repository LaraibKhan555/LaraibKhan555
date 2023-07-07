@description('The Microsoft Sentinel workspace into which the function will be deployed. Has to be in the selected Resource Group.')
param Workspace string = '<LAW_Workspace>' //name of log analytics workspace

@description('The region of the selected workspace. The default value will use the Region selection above.')
param WorkspaceRegion string = resourceGroup().location

param name string = 'RiskFunction'
//resourcegroup resource is also mandatory for functions/savedsearches
resource Workspace_resource 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: Workspace
  location: WorkspaceRegion
}
resource savedsearch 'Microsoft.OperationalInsights/workspaces/savedSearches@2015-03-20' = {
  name: name
  parent: Workspace_resource //make workspace resource as parent of savedsearch, as savedsearch do not exist by itself as resource.
  properties: {
    etag: '*'
    category: 'Function' //select or create legacy category
    functionAlias: name //Alias is mandatory to deploy as function, otherwise it will deploy as saved search
    displayName: 'Risk Function correlated with SecurityAlert with SigninLogs'
    query: 'let unfamiliar = SecurityAlert | where ProviderName contains "IPC"\n| extend UserId = tostring(parse_json(Entities)[0].AadUserId)\n//| where UserId == "619ba921-5d1b-4204-aead-49b3b4a7b2d2"\n | extend ClientIPAddress = tostring(parse_json(ExtendedProperties).["Client IP Address"])\n| extend  AlertId = SystemAlertId;    let upn = SigninLogs\n| where RiskDetail != "none"\n| project RiskDetail, TimeGenerated, UserPrincipalName, UserId,  UserAgent, AppDisplayName, AuthenticationRequirement;\n upn \n| join unfamiliar on UserId'
    version: 3
    functionParameters: 'disabled:bool=False' //if deploying funtion
  }
}
