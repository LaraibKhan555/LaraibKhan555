param workspace string

resource workspace_Microsoft_SecurityInsights_a3f428cf_3a0c_49f3_a386_32c96af6797b 'Microsoft.OperationalInsights/workspaces/providers/alertRules@2022-09-01-preview' = {
  name: '${workspace}/Microsoft.SecurityInsights/a3f428cf-3a0c-49f3-a386-32c96af6797b'
  kind: 'Scheduled'
  properties: {
    displayName: 'User Account Creation followed by User Login followed by User Account Deletion in short timeframe (CEF)'
    description: 'User Account Creation followed by User Login followed by User Account Deletion in short timeframe\n'
    severity: 'Medium'
    enabled: true
    query: 'let timeframe = 15m;\r\nlet lookback = 24h;\r\nlet account_created =\r\nCommonSecurityLog \r\n| where TimeGenerated > ago(lookback+timeframe)\r\n| where DeviceEventClassID == "1000" // A user account was created\r\n| project creationTime = TimeGenerated, CreateEventID = DeviceEventClassID, Activity, Computer, \r\n  DestinationUserName, DestinationUserPrivileges, AccountUsedToCreate = SourceUserName, SourceUserID, \r\n  DestinationUserID;\r\nlet account_deleted =\r\nCommonSecurityLog\r\n| where TimeGenerated > ago(timeframe) \r\n| where DeviceEventClassID == "1001" // A user account was deleted \r\n| project deletionTime = TimeGenerated, DeleteEventID = DeviceEventClassID, Activity, Computer, \r\n  DestinationUserName, DestinationUserPrivileges, AccountUsedToDelete = SourceUserName, SourceUserID, \r\n  DestinationUserID;\r\nlet account_create_delete=  \r\naccount_created\r\n| join kind= inner (account_deleted) on Computer, DestinationUserName\r\n| where deletionTime  - creationTime < lookback\r\n| where tolong(deletionTime - creationTime) > 0\r\n| project TimeDelta = deletionTime - creationTime, creationTime, CreateEventID, Computer, DestinationUserName, DestinationUserID, AccountUsedToCreate, \r\ndeletionTime, DeleteEventID, AccountUsedToDelete\r\n| extend timestamp = creationTime, AccountCustomEntity = AccountUsedToCreate, HostCustomEntity = Computer;\r\nlet account_login =\r\nCommonSecurityLog\r\n| where TimeGenerated > ago(timeframe) \r\n| where DeviceEventClassID == "1005" // A user account was login \r\n| project loginTime = TimeGenerated, LoginEventID = DeviceEventClassID, Activity, Computer, \r\n  DestinationUserName, DestinationUserPrivileges, AccountUsedToCreate = SourceUserName, SourceUserID, \r\n  DestinationUserID;\r\naccount_create_delete\r\n| join kind= inner (account_login) on Computer, DestinationUserName\r\n| where loginTime  - creationTime < lookback\r\n| where tolong(loginTime - creationTime) > 0\r\n| project TimeDelta = deletionTime - creationTime, creationTime, loginTime,deletionTime, Computer, DestinationUserName, DestinationUserID, AccountUsedToCreate,CreateEventID,LoginEventID, DeleteEventID, AccountUsedToDelete\r\n| extend timestamp = creationTime, AccountCustomEntity = AccountUsedToCreate, HostCustomEntity = Computer;'
    queryFrequency: 'PT15M'
    queryPeriod: 'P1D'
    triggerOperator: 'GreaterThan'
    triggerThreshold: 0
    suppressionDuration: 'PT5H'
    suppressionEnabled: false
    startTimeUtc: null
    tactics: []
    techniques: []
    alertRuleTemplateName: null
    incidentConfiguration: {
      createIncident: true
      groupingConfiguration: {
        enabled: false
        reopenClosedIncident: false
        lookbackDuration: 'PT5H'
        matchingMethod: 'AllEntities'
        groupByEntities: [
          'Account'
        ]
        groupByAlertDetails: [
          'DisplayName'
        ]
        groupByCustomDetails: []
      }
    }
    eventGroupingSettings: {
      aggregationKind: 'SingleAlert'
    }
    alertDetailsOverride: null
    customDetails: null
    entityMappings: [
      {
        entityType: 'Account'
        fieldMappings: [
          {
            identifier: 'FullName'
            columnName: 'AccountUsedToCreate'
          }
        ]
      }
      {
        entityType: 'Host'
        fieldMappings: [
          {
            identifier: 'FullName'
            columnName: 'Computer'
          }
        ]
      }
    ]
    sentinelEntitiesMappings: null
    templateVersion: null
  }
}
