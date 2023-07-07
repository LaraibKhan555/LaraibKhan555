param PlaybookName string = 'AddIndicatorsToWatchlist'

var MicrosoftSentinelConnectionName = 'MicrosoftSentinel-${PlaybookName}'

resource Playbook 'Microsoft.Logic/workflows@2019-05-01' = {
  properties: {
    provisioningState: 'Succeeded'
    state: 'Disabled'
    definition: {
      '$schema': 'https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#'
      contentVersion: '1.0.0.0'
      parameters: {
        '$connections': {
          defaultValue: {}
          type: 'Object'
        }
      }
      triggers: {
        Microsoft_Sentinel_alert: {
          type: 'ApiConnectionWebhook'
          inputs: {
            body: {
              callback_url: '@{listCallbackUrl()}'
            }
            host: {
              connection: {
                name: '@parameters(\'$connections\')[\'azuresentinel_1\'][\'connectionId\']'
              }
            }
            path: '/subscribe'
          }
        }
      }
      actions: {
        'Entities_-_Get_Accounts': {
          runAfter: {}
          type: 'ApiConnection'
          inputs: {
            body: '@triggerBody()?[\'Entities\']'
            host: {
              connection: {
                name: '@parameters(\'$connections\')[\'azuresentinel_1\'][\'connectionId\']'
              }
            }
            method: 'post'
            path: '/entities/account'
          }
        }
        'Entities_-_Get_Hosts': {
          runAfter: {}
          type: 'ApiConnection'
          inputs: {
            body: '@triggerBody()?[\'Entities\']'
            host: {
              connection: {
                name: '@parameters(\'$connections\')[\'azuresentinel_1\'][\'connectionId\']'
              }
            }
            method: 'post'
            path: '/entities/host'
          }
        }
        For_each: {
          foreach: '@body(\'Entities_-_Get_Hosts\')?[\'Hosts\']'
          actions: {
            'Watchlists_-_Add_a_new_watchlist_item': {
              runAfter: {}
              type: 'ApiConnection'
              inputs: {
                body: {
                  Hostname: '@items(\'For_each\')?[\'HostName\']'
                }
                host: {
                  connection: {
                    name: '@parameters(\'$connections\')[\'azuresentinel_1\'][\'connectionId\']'
                  }
                }
                method: 'put'
                path: '/Watchlists/subscriptions/@{encodeURIComponent(triggerBody()?[\'WorkspaceSubscriptionId\'])}/resourceGroups/@{encodeURIComponent(triggerBody()?[\'WorkspaceResourceGroup\'])}/workspaces/@{encodeURIComponent(triggerBody()?[\'WorkspaceId\'])}/watchlists/@{encodeURIComponent(\'FailedHosts\')}/watchlistItem'
              }
            }
          }
          runAfter: {
            'Entities_-_Get_Hosts': [
              'Succeeded'
            ]
          }
          type: 'Foreach'
        }
        For_each_2: {
          foreach: '@body(\'Entities_-_Get_Accounts\')?[\'Accounts\']'
          actions: {
            'Watchlists_-_Add_a_new_watchlist_item_2': {
              runAfter: {}
              type: 'ApiConnection'
              inputs: {
                body: {
                  Account: '@items(\'For_each_2\')?[\'Name\']'
                }
                host: {
                  connection: {
                    name: '@parameters(\'$connections\')[\'azuresentinel_1\'][\'connectionId\']'
                  }
                }
                method: 'put'
                path: '/Watchlists/subscriptions/@{encodeURIComponent(triggerBody()?[\'WorkspaceSubscriptionId\'])}/resourceGroups/@{encodeURIComponent(triggerBody()?[\'WorkspaceResourceGroup\'])}/workspaces/@{encodeURIComponent(triggerBody()?[\'WorkspaceId\'])}/watchlists/@{encodeURIComponent(\'FailedUserAccount\')}/watchlistItem'
              }
            }
          }
          runAfter: {
            'Entities_-_Get_Accounts': [
              'Succeeded'
            ]
          }
          type: 'Foreach'
        }
      }
      outputs: {}
    }
    parameters: {
      '$connections': {
        value: {
          azuresentinel_1: {
            connectionId: MicrosoftSentinelConnection.id
            connectionName: MicrosoftSentinelConnectionName
            id: '/subscriptions/${subscription().subscriptionId}/providers/Microsoft.Web/locations/${resourceGroup().location}/managedApis/Azuresentinel'
          }
        }
      }
    }
  }
  name: PlaybookName
  location: resourceGroup().location
  identity: {
    type: 'SystemAssigned'
  }
}

resource MicrosoftSentinelConnection 'Microsoft.Web/connections@2016-06-01' = {
  name: MicrosoftSentinelConnectionName
  location: resourceGroup().location
  kind: 'V1'
  properties: {
    displayName: MicrosoftSentinelConnectionName
    customParameterValues: {}
    api: {
      id: '/subscriptions/${subscription().subscriptionId}/providers/Microsoft.Web/locations/${resourceGroup().location}/managedApis/Azuresentinel'
    }
  }
}
