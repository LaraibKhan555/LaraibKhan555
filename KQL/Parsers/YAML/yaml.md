# YAML Ain't Makrup Language (YAML)

YAML uses human-friendly syntax to define configuration files but in this case, KQL parsers and KQL functions are publically shared in YAMl format for ease of understanding.

However, these formats cannot be deployed as it is in Microsoft Sentinel Environment. They require conversion to (ARM) .json file in order to be deployed as Azure only understands ARM which comes in .json. 