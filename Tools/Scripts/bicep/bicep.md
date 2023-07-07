# Bicep Intro

Bicep is a domain-specific language (DSL) and a declarative language for describing and deploying Azure resources. It stands for "Bicep: The Azure Deployment DSL" and is an open-source project developed by Microsoft. Bicep is designed to simplify the authoring and management of Azure Resource Manager (ARM) templates.

ARM templates are JSON files used to define the desired state of Azure resources and their dependencies. While ARM templates are powerful, they can be complex and verbose to work with. Bicep addresses these challenges by providing a more concise and readable syntax for defining Azure resources.

Bicep files have the extension .bicep and are compiled into ARM templates (.json files) before deployment. Bicep leverages the existing ARM template ecosystem and supports all the capabilities and resource types available in ARM templates.

Some key features of Bicep include:

1. Concise Syntax: Bicep uses a cleaner syntax compared to JSON, making it easier to read, write, and maintain code.

2. Modularity and Reusability: Bicep supports modules, allowing you to define reusable code snippets that can be shared across deployments.

3. Strong Typing: Bicep provides strong typing and compile-time validation, which helps catch errors early and improves the development experience.

4. IntelliSense and Tooling Support: Bicep integrates with popular code editors and provides IntelliSense, auto-completion, and error checking, enhancing developer productivity.

5. Incremental Deployment: Bicep supports incremental deployment, enabling you to update and deploy only the necessary changes to your infrastructure.

Overall, Bicep simplifies the process of defining and deploying Azure resources while maintaining compatibility with ARM templates. It provides a more efficient and developer-friendly way to work with Azure deployments.


# Bicep Examples
## To create a JSON file out of bicep file

`az bicep build --file .\asimfunction.bicep`

## To convert existing JSON file as bicep template

`bicep decompile ASimSyslogAuthentication.json --outfile ASimSyslogAuthentication.bicep`

## To deploy bicep directly as Azure resource

`New-AzResourceGroupDeployment -TemplateFile ".\asimfunction.bicep" -ResourceGroupName <RG-Name>`
