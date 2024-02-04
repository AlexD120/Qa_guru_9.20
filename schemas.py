post_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "aditionalProperties": False,
  "properties": {

    "job": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [

    "job",
    "id",
    "createdAt"
  ]
}